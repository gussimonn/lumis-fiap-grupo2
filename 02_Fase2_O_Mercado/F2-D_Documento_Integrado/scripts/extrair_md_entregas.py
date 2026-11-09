"""Extrai do documento único o texto de cada entrega e grava um .md na pasta de cada uma (D-048).
Uso (de qualquer pasta): python extrair_md_entregas.py [documento_unico.docx]
Sem argumento, usa o F2-D_Documento_Integrado_v3.docx. Grava 02_Fase2_O_Mercado/F2-EX_<Nome>/F2-EX_<Nome>.md com o
corpo da entrega, os quadros dela no Apêndice B e as referências citadas. As imagens são ligadas ao .png de mesmo
conteúdo na pasta figuras/ das entregas; se uma imagem não tiver arquivo correspondente, o script para."""
import sys, os, re, hashlib, glob, datetime
import docx
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.ns import qn

F2 = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
DOCX = sys.argv[1] if len(sys.argv) > 1 else os.path.join(F2, 'F2-D_Documento_Integrado', 'F2-D_Documento_Integrado_v3.docx')
d = docx.Document(DOCX)

# mapa de imagens: rId -> hash; hash -> arquivo png da pasta da fase
png_por_hash = {}
for f in glob.glob(os.path.join(F2, '**', '*.png'), recursive=True):
    if '_Historico' in f:
        continue
    h = hashlib.sha1(open(f, 'rb').read()).hexdigest()
    png_por_hash.setdefault(h, []).append(os.path.relpath(f, F2).replace('\\', '/'))

def imagens(p):
    out = []
    for blip in p._p.iter(qn('a:blip')):
        rid = blip.get(qn('r:embed'))
        blob = d.part.related_parts[rid].blob
        h = hashlib.sha1(blob).hexdigest()
        out.append(png_por_hash.get(h, ['?' + h[:8]]))
    return out

SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')

def runs_md(p):
    partes = []
    for item in p.iter_inner_content():
        rs = item.runs if hasattr(item, 'runs') else [item]
        for r in rs:
            t = r.text
            if not t:
                continue
            if all(c in '⁰¹²³⁴⁵⁶⁷⁸⁹' for c in t):
                partes.append('[^%s]' % t.translate(SUP))
            elif r.bold and t.strip():
                lead = t[:len(t) - len(t.lstrip())]
                trail = t[len(t.rstrip()):]
                partes.append(f'{lead}**{t.strip()}**{trail}')
            else:
                partes.append(t)
    s = ''.join(partes)
    s = s.replace('****', '').replace('** **', ' ')
    return s.strip()

def cel(c):
    return ' '.join(runs_md(p).replace('**', '') for p in c.paragraphs if p.text.strip()).replace('|', '\\|')

def tabela_md(t):
    linhas = []
    for i, row in enumerate(t.rows):
        cells = []
        prev = None
        for c in row.cells:
            if c._tc is prev:   # célula mesclada repetida
                continue
            prev = c._tc
            cells.append(cel(c))
        linhas.append('| ' + ' | '.join(cells) + ' |')
        if i == 0:
            linhas.append('|' + '---|' * len(cells))
    return '\n'.join(linhas)

# percorre o corpo em ordem
blocos = []  # (nivel_h1_titulo, md)
atual_h1, atual_h2 = None, None
secoes = {}   # chave -> lista de md
def add(md):
    chave = atual_h1 if not (atual_h1 or '').startswith('Apêndice B') else 'B:' + (atual_h2 or '')
    secoes.setdefault(chave, []).append(md)

for el in d.element.body.iterchildren():
    tag = el.tag.split('}')[1]
    if tag == 'tbl':
        add(tabela_md(Table(el, d)))
        continue
    if tag != 'p':
        continue
    p = Paragraph(el, d)
    st = p.style.name
    imgs = imagens(p)
    texto = runs_md(p)
    if st == 'Heading 1':
        atual_h1, atual_h2 = p.text.strip(), None
        add('## ' + p.text.strip())
        continue
    if st == 'Heading 2':
        atual_h2 = p.text.strip()
        add('### ' + p.text.strip())
        continue
    for im in imgs:
        add(f'![]({im[0]})')
    if not texto:
        continue
    if st == 'List Bullet':
        add('- ' + texto)
    elif st == 'List Number':
        add('1. ' + texto)
    elif st == 'Caption':
        add('*' + texto.replace('**', '') + '*')
    elif st == 'Lumis Nota':
        add('> ' + texto)
    elif st == 'Lumis Destaque':
        add('> **' + texto.replace('**', '') + '**')
    elif st == 'Lumis Rótulo':
        add('**' + texto.replace('**', '') + '**')
    else:
        add(texto)

def juntar(itens):
    out = []
    for i, m in enumerate(itens):
        if out:
            ant = out[-1]
            lista = m.startswith(('- ', '1. ')) and ant.startswith(('- ', '1. '))
            nota = m.startswith('>') and ant.startswith('>')
            out.append('\n' if (lista) else ('>\n' if nota else '\n\n'))
        out.append(m)
    return ''.join(out)

# referências numeradas
refs = {}
for m in secoes.get('Referências', []):
    mm = re.match(r'> (\d+)\. (.*)', m)
    if mm:
        refs[mm.group(1)] = mm.group(2)

ENTREGAS = {
    '1': ('F2-E1_Mapa_do_Territorio', 'Mapa do Território'),
    '2': ('F2-E2_Auditoria_do_Ativo', 'Auditoria do Ativo: Dados e Métricas'),
    '3': ('F2-E3_Linha_de_Responsabilidade', 'Linha de Responsabilidade'),
    '4': ('F2-E4_Cultura_e_Funil_de_Inovacao', 'Diagnóstico de Cultura e Funil de Inovação'),
    '5': ('F2-E5_Due_Diligence_ESG', 'Due Diligence ESG da Expansão'),
}
hoje = datetime.date.today().strftime('%d/%m/%Y')
for n, (pasta, nome) in ENTREGAS.items():
    h1 = next(k for k in secoes if k and k.startswith(f'Entrega {n} '))
    md = juntar(secoes[h1])
    apb = secoes.get(f'B:Entrega {n}', [])[1:]  # sem o próprio título
    if apb:
        md += '\n\n## Quadros de apoio (Apêndice B do documento único)\n\n' + juntar(apb)
    citadas = sorted(set(re.findall(r'\[\^(\d+)\]', md)), key=int)
    if citadas:
        md += '\n\n## Referências citadas\n\n' + '\n'.join(f'[^{c}]: {refs[c]}' for c in citadas)
    if '](?' in md:
        sys.exit(f'Entrega {n}: imagem sem .png correspondente nas pastas figuras/')

    def rel(m):
        p = m.group(1)
        return f'](figuras/{p.split("/figuras/")[1]})' if p.startswith(pasta + '/') else f'](../{p})'
    md = re.sub(r'\]\(([^)]+\.png)\)', rel, md)
    cab = (f'# F2-E{n} · {nome}\n\n'
           f'> Texto da Entrega {n} como foi no documento único (`{os.path.basename(DOCX)}`), '
           f'com os quadros de apoio desta entrega que estão no Apêndice B. É uma cópia para leitura: se houver diferença, vale o .docx. '
           f'Os números de figura, tabela, seção e nota são os do documento único. Extraído em {hoje}.\n\n')
    destino = os.path.join(F2, pasta, pasta + '.md')
    open(destino, 'w', encoding='utf-8').write(cab + md + '\n')
    print(os.path.relpath(destino, F2), len(md.split()), 'palavras')
