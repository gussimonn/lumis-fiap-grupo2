"""F3-D v2: monta o documento único da Fase 3 (dossiê técnico do Lumis Insight para a auditoria independente),
no padrão visual da Lumis (00_Lumis/Design_System/Modelo_Entrega_Lumis.docx).

Adaptado do script da Fase 2 (02_Fase2_O_Mercado/F2-D_Documento_Integrado/scripts/montar_v2.py); a escrita no Word não mudou.
Uso:
    python montar_v2.py dossie <saida.docx>   # documento único
    python montar_v2.py lint                  # confere o texto (códigos internos, travessões, chaves)

O texto fica em ../texto/*.txt, lidos em ordem alfabética, uma instrução por linha:
# título 1, ## título 2, > destaque, - item, 1. item numerado, FIG[chave]: legenda, TAB[chave]: larguras | legenda
seguida das linhas "| ... |", CAIXA ... FIMCAIXA (prompt), QUEBRA, NOTA:, LINHA:, ROTULO:.
Base: a v1 da equipe em PDF (03_Fase3_O_Motor/Lumis Intelligence - Fase 3.pdf) e a revisão em
F3-D_Revisao_da_v1_da_equipe.md.
"""

import os, re, sys
import docx
from docx.shared import Cm, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT as VA
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE = 'C:/Users/gusta/Downloads/LumisOS/'
MODELO = BASE + '00_Lumis/Design_System/Modelo_Entrega_Lumis.docx'
F3 = '03_Fase3_O_Motor/'
TEXTO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'texto')
LARGURA_UTIL = 16.0  # cm (A4 com margens de 2,5 cm)

META = {
    'dossie': {
        'rotulo': 'Fase 3 · O Motor',
        'titulo': 'Traduzir o motor',
        'subtitulo': 'Dossiê técnico do Lumis Insight para a auditoria independente: lógica de decisão, decisões embutidas, economia, métricas, ética e prontidão',
        'equipe': 'Equipe: Bruno Müller, Diego Franca Evangelista, Felipe Alef, Gustavo Halfen Simon e Maria Fernanda Barros',
        'data': 'Data: 08/11/2026',
        'cabecalho': 'Fase 3 · Traduzir o motor',
    },
}

FIGS = {
    'fluxo': (F3 + 'F3-E1_Traducao_da_Logica/figuras/fluxograma_logica.png', 16.0),
    'arvore': (F3 + 'F3-E4_Arvore_de_Metricas/figuras/arvore_metricas.png', 16.0),
}

REFS = {}

# Cores dos níveis da tabela "difícil de copiar" (mesmas da Entrega 1).
NIVEIS_COR = {
    'Copiável': ('6B7C85', None),
    'Parcialmente difícil': ('0F2D3A', 'F1F6F4'),
    'Moderadamente difícil': ('0F2D3A', None),
    'Valioso, mas travado': ('B7791F', 'FBF3E6'),
    'Difícil de copiar': ('1E8C6B', 'EEF7F3'),
}

TAG = re.compile(r'(\[(?:fonte|hipótese|não consta|risco)[^\]]*\])')
TAGSTYLE = {'fonte': 'Tag Fonte', 'hipótese': 'Tag Hipótese', 'não consta': 'Tag Não consta', 'risco': 'Tag Risco'}
SUP = re.compile(r'\x01(\d+(?:,\d+)*)\x02')
SUPMAP = str.maketrans('0123456789,', '⁰¹²³⁴⁵⁶⁷⁸⁹˒')
DIRETIVA = re.compile(r'^(FIG|TAB|NIVEIS)\[([^\]|]+)(?:\|([\d.,]+))?\]:\s*(.*)$')


# ------------------------------------------------------------------ leitura
def _ler_arquivos(caminho):
    if os.path.isdir(caminho):
        arqs = sorted(f for f in os.listdir(caminho) if f.endswith('.txt'))
        linhas = []
        for f in arqs:
            with open(os.path.join(caminho, f), encoding='utf-8') as fh:
                linhas += [(f, i + 1, l.rstrip('\n')) for i, l in enumerate(fh)]
        return linhas
    with open(caminho, encoding='utf-8') as fh:
        return [(os.path.basename(caminho), i + 1, l.rstrip('\n')) for i, l in enumerate(fh)]


def blocos(linhas):
    """Agrupa as linhas em blocos (tipo, dados, origem)."""
    out, i = [], 0
    while i < len(linhas):
        arq, n, l = linhas[i]
        s = l.strip()
        org = f'{arq}:{n}'
        if not s or s.startswith('%'):
            i += 1; continue
        m = DIRETIVA.match(s)
        if m:
            tipo, chave, larg, resto = m.group(1), m.group(2).strip(), m.group(3), m.group(4)
            if tipo == 'FIG':
                out.append(('FIG', dict(chave=chave, largura=float(larg.replace(',', '.')) if larg else None, legenda=resto.strip()), org))
                i += 1; continue
            partes = resto.split('|', 1)
            larguras = [float(x) for x in partes[0].replace(' ', '').split(';' if ';' in partes[0] else ',') if x] if len(partes) == 2 else []
            legenda = partes[1].strip() if len(partes) == 2 else resto.strip()
            linhas_tab = []
            i += 1
            while i < len(linhas) and linhas[i][2].strip().startswith('|'):
                cel = linhas[i][2].strip()
                cel = cel[1:-1] if cel.endswith('|') else cel[1:]
                linhas_tab.append([c.strip() for c in cel.split('|')])
                i += 1
            out.append((tipo, dict(chave=chave, larguras=larguras, legenda=legenda, linhas=linhas_tab), org))
            continue
        if s == 'CAIXA':
            conteudo = []
            i += 1
            while i < len(linhas) and linhas[i][2].strip() != 'FIMCAIXA':
                conteudo.append(linhas[i][2])
                i += 1
            i += 1
            out.append(('CAIXA', dict(linhas=conteudo), org)); continue
        out.append(('LINHA', dict(texto=s), org))
        i += 1
    return out


def ler_conteudo(caminho):
    if caminho == ':dossie':
        caminho = TEXTO
    return _ler_arquivos(caminho)


# ------------------------------------------------------------------ numeração
def numerar(bs):
    figs, tabs, refs = {}, {}, {}
    for tipo, d, org in bs:
        if tipo == 'FIG':
            figs.setdefault(d['chave'], len(figs) + 1)
        elif tipo in ('TAB', 'NIVEIS'):
            tabs.setdefault(d['chave'], len(tabs) + 1)
    textos = []
    for tipo, d, org in bs:
        if tipo == 'LINHA':
            textos.append(d['texto'])
        elif tipo in ('TAB', 'NIVEIS'):
            textos += [c for row in d['linhas'] for c in row] + [d['legenda']]
        elif tipo == 'FIG':
            textos.append(d['legenda'])
    for t in textos:
        for k in re.findall(r'\{ref:([^}]+)\}', t):
            for kk in k.split(','):
                refs.setdefault(kk.strip(), len(refs) + 1)
    return figs, tabs, refs


def resolver(texto, figs, tabs, refs, avisos, org):
    def fig(m):
        k = m.group(1)
        if k not in figs:
            avisos.append(f'{org}: figura citada sem bloco FIG: {k}')
            return '??'
        return str(figs[k])

    def tab(m):
        k = m.group(1)
        if k not in tabs:
            avisos.append(f'{org}: tabela citada sem bloco TAB: {k}')
            return '??'
        return str(tabs[k])

    def ref(m):
        nums = []
        for k in m.group(1).split(','):
            k = k.strip()
            if k not in REFS:
                avisos.append(f'{org}: referência fora do registro: {k}')
            nums.append(str(refs.get(k, 0)))
        return '\x01' + ','.join(nums) + '\x02'

    texto = re.sub(r'\{fig:([^}]+)\}', fig, texto)
    texto = re.sub(r'\{tab:([^}]+)\}', tab, texto)
    texto = re.sub(r'\{ref:([^}]+)\}', ref, texto)
    if re.search(r'\{[a-z]+:', texto):
        avisos.append(f'{org}: marcador não resolvido: {texto[:80]}')
    return texto


# ------------------------------------------------------------------ verificação de texto
INTERNOS = [
    (re.compile(r'\bD-\d{2,3}\b'), 'código de decisão interna (D-xx)'),
    (re.compile(r'\bC[1-5]\b'), 'código de compromisso (C1 a C5)'),
    (re.compile(r'\bF\d-[EAMD]\d?\b'), 'código de entrega (FX-EY)'),
    (re.compile(r'\bQ-\d+\b'), 'código de pergunta interna (Q-x)'),
    (re.compile(r'DECISOES|ESTADO\.md|[Ll]evantamento_v\d|\.md\b'), 'nome de arquivo interno'),
    (re.compile(r'[—–]'), 'travessão (trocar por vírgula, dois-pontos, ponto ou parênteses)'),
    (re.compile(r'\b(crucial|robust[oa]s?|alavanc\w+|potencializ\w+|jornada|ressalt\w+|destaca\w*)\b', re.I), 'palavra marcada pelo humanizer'),
    (re.compile(r'não (?:é|são) [^.;:]{1,60}, e sim\b|\bnão só\b[^.]*\bmas também\b', re.I), 'contraste "não X, e sim Y"'),
    (re.compile(r'\{(?!fig:|tab:|ref:)'), 'chave estranha'),
]


def checar_texto(texto, org, avisos, celula=False):
    for rx, nome in INTERNOS:
        if celula and nome.startswith('travessão') and texto.strip() in ('—', '–'):
            continue
        m = rx.search(texto)
        if m:
            avisos.append(f'{org}: {nome}: "...{texto[max(0, m.start() - 30):m.end() + 30]}..."')
    if texto.count('**') % 2:
        avisos.append(f'{org}: negrito sem fechamento: {texto[:60]}')
    if texto.count('[') != texto.count(']'):
        avisos.append(f'{org}: colchete sem par: {texto[:60]}')


# ------------------------------------------------------------------ escrita no Word
class Doc:
    def __init__(self, modo):
        self.d = docx.Document(MODELO)
        self.st = self.d.styles
        self.body = self.d.element.body
        self.modo = modo
        self.lista_num_aberta = False
        self._preparar(modo)

    # capa, cabeçalho e limpeza do exemplo do modelo
    def _preparar(self, modo):
        d, meta = self.d, META[modo]
        hp = d.sections[0].header.paragraphs[0]
        feito = False
        for r in hp.runs:
            if r.text.strip():
                r.text = '' if feito else '\t' + meta['cabecalho']
                feito = True
        paras = d.paragraphs
        corte = None
        for p in paras:  # o parágrafo com a quebra de página fecha a capa
            if p._p.xpath('.//w:br[@w:type="page"]'):
                corte = p._p
                break
        if modo == 'dossie':
            def trocar(p, t):
                if p.runs:
                    p.runs[0].text = t
                    for r in p.runs[1:]:
                        r.text = ''
                else:
                    p.add_run(t)
            for p in paras:
                nome = p.style.name
                if p._p is corte:
                    break
                if nome == 'Lumis Rótulo':
                    trocar(p, meta['rotulo'])
                elif nome == 'Title':
                    trocar(p, meta['titulo'])
                elif nome == 'Subtitle':
                    trocar(p, meta['subtitulo'])
                elif nome == 'Lumis Nota' and p.text.startswith('Equipe'):
                    trocar(p, meta['equipe'])
                elif nome == 'Lumis Nota' and p.text.startswith('Data'):
                    trocar(p, meta['data'])
            apagar = False
            for el in list(self.body):
                if apagar and el.tag != qn('w:sectPr'):
                    self.body.remove(el)
                if el is corte:
                    apagar = True
        else:  # memorando: sem capa; cabeçalho e rodapé já na primeira página
            for el in list(self.body):
                if el.tag != qn('w:sectPr'):
                    self.body.remove(el)
            d.sections[0].different_first_page_header_footer = False

    # texto com negrito, marcadores de origem e números sobrescritos
    def runs(self, p, texto):
        for i, seg in enumerate(texto.split('**')):
            for parte in TAG.split(seg):
                if not parte:
                    continue
                if TAG.fullmatch(parte):
                    r = p.add_run(parte)
                    r.style = self.st[TAGSTYLE[next(k for k in TAGSTYLE if parte[1:].startswith(k))]]
                    continue
                pos = 0
                for m in SUP.finditer(parte):
                    if m.start() > pos:
                        r = p.add_run(parte[pos:m.start()])
                        if i % 2:
                            r.bold = True
                    r = p.add_run(m.group(1).translate(SUPMAP))
                    pos = m.end()
                if pos < len(parte):
                    r = p.add_run(parte[pos:])
                    if i % 2:
                        r.bold = True
        return p

    def par(self, texto, estilo='Normal'):
        p = self._aplicar_quebra(self.d.add_paragraph(style=estilo))
        return self.runs(p, texto)

    def numerado(self, texto, inicio=1):
        p = self.par(texto, 'List Number')
        if not self.lista_num_aberta:  # cada lista começa no número escrito no primeiro item
            num_id = self._nova_numeracao(inicio)
            if num_id is not None:
                pPr = p._p.get_or_add_pPr()
                numPr = OxmlElement('w:numPr')
                il = OxmlElement('w:ilvl'); il.set(qn('w:val'), '0')
                ni = OxmlElement('w:numId'); ni.set(qn('w:val'), str(num_id))
                numPr.append(il); numPr.append(ni)
                pPr.append(numPr)
                self._num_atual = num_id
        else:
            if getattr(self, '_num_atual', None) is not None:
                pPr = p._p.get_or_add_pPr()
                numPr = OxmlElement('w:numPr')
                il = OxmlElement('w:ilvl'); il.set(qn('w:val'), '0')
                ni = OxmlElement('w:numId'); ni.set(qn('w:val'), str(self._num_atual))
                numPr.append(il); numPr.append(ni)
                pPr.append(numPr)
        self.lista_num_aberta = True
        return p

    def _nova_numeracao(self, inicio=1):
        try:
            estilo = self.st['List Number']
            numPr = estilo.element.pPr.find(qn('w:numPr'))
            base = numPr.find(qn('w:numId')).get(qn('w:val'))
            numbering = self.d.part.numbering_part.element
            abstract = None
            for n in numbering.findall(qn('w:num')):
                if n.get(qn('w:numId')) == base:
                    abstract = n.find(qn('w:abstractNumId')).get(qn('w:val'))
            novo = max(int(n.get(qn('w:numId'))) for n in numbering.findall(qn('w:num'))) + 1
            num = OxmlElement('w:num'); num.set(qn('w:numId'), str(novo))
            an = OxmlElement('w:abstractNumId'); an.set(qn('w:val'), abstract); num.append(an)
            lo = OxmlElement('w:lvlOverride'); lo.set(qn('w:ilvl'), '0')
            so = OxmlElement('w:startOverride'); so.set(qn('w:val'), str(inicio)); lo.append(so); num.append(lo)
            numbering.append(num)
            return novo
        except Exception:
            return None

    def figura(self, caminho, largura, legenda):
        p = self._aplicar_quebra(self.d.add_paragraph()); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.keep_with_next = True
        p.add_run().add_picture(BASE + caminho, width=Cm(largura))
        self.par(legenda, 'Caption')

    @staticmethod
    def shade(cell, fill):
        s = OxmlElement('w:shd'); s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), fill)
        cell._tc.get_or_add_tcPr().append(s)

    def _tabela_base(self, nlin, ncol, larguras):
        tb = self.d.add_table(rows=nlin, cols=ncol); tb.alignment = WD_TABLE_ALIGNMENT.CENTER
        bd = OxmlElement('w:tblBorders')
        for side in ('top', 'bottom', 'insideH'):
            e = OxmlElement(f'w:{side}'); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '4'); e.set(qn('w:color'), 'D3DEDB')
            bd.append(e)
        tb._tbl.tblPr.append(bd); tb.autofit = False
        lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tb._tbl.tblPr.append(lay)
        for gc, w in zip(tb._tbl.tblGrid.findall(qn('w:gridCol')), larguras):
            gc.set(qn('w:w'), str(int(w * 567)))
        for r in tb.rows:  # linha não se parte entre páginas
            r._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
        th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), 'true'); tb.rows[0]._tr.get_or_add_trPr().append(th)
        return tb

    def tabela(self, linhas, larguras, legenda):
        ncol = max(len(r) for r in linhas)
        tb = self._tabela_base(len(linhas), ncol, larguras)
        zebra = 0
        grupos = []
        for i, row in enumerate(linhas):
            # linha de grupo: só a primeira célula, em negrito; vira faixa mesclada em Papel
            grupo = i > 0 and row and row[0].startswith('**') and row[0].endswith('**') and all(not c for c in row[1:])
            if grupo:
                grupos.append(i)
                zebra = 0
            else:
                zebra += 1
            for j in range(ncol):
                txt = row[j] if j < len(row) else ''
                c = tb.cell(i, j); c.width = Cm(larguras[j])
                p = c.paragraphs[0]; p.style = self.st['Lumis Tabela']
                if i == 0:
                    p.paragraph_format.keep_with_next = True  # cabeçalho não fica sozinho no pé da página
                    r = p.add_run(txt.replace('**', '')); r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                    self.shade(c, '0F2D3A')
                elif grupo:
                    self.shade(c, 'EEF7F3')
                    p.paragraph_format.keep_with_next = True  # a faixa do grupo não fica sozinha no pé da página
                    if j == 0:
                        r = p.add_run(txt.strip('*')); r.bold = True; r.font.color.rgb = RGBColor.from_string('1E8C6B')
                else:
                    self.runs(p, txt)
                    if zebra % 2 == 0:
                        self.shade(c, 'F1F6F4')
                    n = len(linhas)
                    if i == n - 1:  # a última linha leva a legenda junto (o cabeçalho já segura a 1ª linha)
                        p.paragraph_format.keep_with_next = True
        for i in grupos:  # mescla a faixa do grupo
            cel = tb.cell(i, 0).merge(tb.cell(i, ncol - 1))
            for extra in cel.paragraphs[1:]:
                extra._p.getparent().remove(extra._p)
        self.par(legenda, 'Caption')

    def tabela_niveis(self, linhas, larguras, legenda):
        """Tabela agrupada por nível (Entrega 1): célula do nível mesclada, cor por grupo e 'destrava' em itálico."""
        cab, dados = linhas[0], linhas[1:]
        tb = self._tabela_base(len(dados) + 1, 3, larguras)
        for j, txt in enumerate(cab[:3]):
            c = tb.cell(0, j); c.width = Cm(larguras[j]); p = c.paragraphs[0]; p.style = self.st['Lumis Tabela']
            p.paragraph_format.keep_with_next = True
            r = p.add_run(txt); r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); self.shade(c, '0F2D3A')
        grupos = []
        for row in dados:
            nivel = row[0] or (grupos[-1][0] if grupos else '')
            if grupos and grupos[-1][0] == nivel and not row[0]:
                grupos[-1][1].append(row)
            elif grupos and grupos[-1][0] == nivel:
                grupos[-1][1].append(row)
            else:
                grupos.append((nivel, [row]))
        i = 1
        for nivel, itens in grupos:
            cor, fundo = NIVEIS_COR.get(nivel, ('0F2D3A', None))
            first = i
            for row in itens:
                elemento = row[1] if len(row) > 1 else ''
                porque = row[2] if len(row) > 2 else ''
                destrava = row[3] if len(row) > 3 else ''
                for j in range(3):
                    c = tb.cell(i, j); c.width = Cm(larguras[j]); c.vertical_alignment = VA.CENTER
                    c.paragraphs[0].style = self.st['Lumis Tabela']
                    if fundo:
                        self.shade(c, fundo)
                self.runs(tb.cell(i, 1).paragraphs[0], '**' + elemento + '**' if elemento and '**' not in elemento else elemento)
                self.runs(tb.cell(i, 2).paragraphs[0], porque)
                if destrava:
                    q = tb.cell(i, 2).add_paragraph(style='Lumis Tabela')
                    rr = q.add_run(destrava); rr.italic = True; rr.font.color.rgb = RGBColor.from_string('1E8C6B')
                if i == len(dados):  # a última linha leva a legenda junto
                    for cc in tb.rows[i].cells:
                        cc.paragraphs[0].paragraph_format.keep_with_next = True
                if len(itens) > 1 and i < first + len(itens) - 1:  # mantém o grupo junto
                    for cc in tb.rows[i].cells:
                        cc.paragraphs[0].paragraph_format.keep_with_next = True
                i += 1
            cel = tb.cell(first, 0)
            if i - 1 > first:
                cel = cel.merge(tb.cell(i - 1, 0))
                for extra in cel.paragraphs[1:]:
                    extra._p.getparent().remove(extra._p)
            p0 = cel.paragraphs[0]; p0.style = self.st['Lumis Tabela']
            rn = p0.add_run(nivel); rn.bold = True; rn.font.color.rgb = RGBColor.from_string(cor)
            cel.vertical_alignment = VA.CENTER
        self.par(legenda, 'Caption')

    def caixa(self, linhas):
        tb = self.d.add_table(rows=1, cols=1); tb.alignment = WD_TABLE_ALIGNMENT.CENTER
        c = tb.cell(0, 0); self.shade(c, 'F1F6F4')
        c.paragraphs[0].style = self.st['Lumis Tabela']; c.paragraphs[0].add_run(linhas[0] if linhas else '')
        for l in linhas[1:]:
            c.add_paragraph(l, style='Lumis Tabela')
        self.d.add_paragraph(style='Lumis Nota')

    def quebra(self):
        self.quebra_pendente = True  # vira 'quebra antes' no próximo parágrafo criado

    def _aplicar_quebra(self, p):
        if getattr(self, 'quebra_pendente', False):
            p.paragraph_format.page_break_before = True
            self.quebra_pendente = False
        return p

    def titulo(self, texto, nivel):
        return self._aplicar_quebra(self.d.add_heading(texto, level=nivel))


def montar(modo, conteudo, saida=None):
    linhas = ler_conteudo(conteudo)
    bs = blocos(linhas)
    figs, tabs, refs = numerar(bs)
    avisos = []
    D = Doc(modo) if saida else None
    for tipo, d, org in bs:
        if tipo != 'LINHA':
            pass
        if tipo == 'LINHA':
            t = d['texto']
            mnum = re.match(r'^(\d+)\.\s+(.*)$', t)
            if not mnum and D:
                D.lista_num_aberta = False
            if t.startswith('### '):
                txt = resolver(t[4:], figs, tabs, refs, avisos, org); checar_texto(txt, org, avisos)
                D and D.titulo(txt, 3)
            elif t.startswith('## '):
                txt = resolver(t[3:], figs, tabs, refs, avisos, org); checar_texto(txt, org, avisos)
                D and D.titulo(txt, 2)
            elif t.startswith('# '):
                txt = resolver(t[2:], figs, tabs, refs, avisos, org); checar_texto(txt, org, avisos)
                D and D.titulo(txt, 1)
            elif t.startswith('> '):
                txt = resolver(t[2:], figs, tabs, refs, avisos, org); checar_texto(txt, org, avisos)
                D and D.par(txt, 'Lumis Destaque')
            elif t.startswith('ROTULO:'):
                txt = resolver(t[7:].strip(), figs, tabs, refs, avisos, org); checar_texto(txt, org, avisos)
                D and D.par(txt, 'Lumis Rótulo')
            elif t.startswith('TITULO:'):
                D and D.par(t[7:].strip(), 'Title')
            elif t.startswith('SUBTITULO:'):
                D and D.par(t[10:].strip(), 'Subtitle')
            elif t.startswith('NOTA:'):
                txt = resolver(t[5:].strip(), figs, tabs, refs, avisos, org); checar_texto(txt, org, avisos)
                D and D.par(txt, 'Lumis Nota')
            elif t.startswith('LINHA:'):
                txt = resolver(t[6:].strip(), figs, tabs, refs, avisos, org); checar_texto(txt, org, avisos)
                D and D.par(txt, 'Lumis Tabela')
            elif t.startswith('- '):
                txt = resolver(t[2:], figs, tabs, refs, avisos, org); checar_texto(txt, org, avisos)
                D and D.par(txt, 'List Bullet')
            elif mnum:
                txt = resolver(mnum.group(2), figs, tabs, refs, avisos, org); checar_texto(txt, org, avisos)
                D and D.numerado(txt, int(mnum.group(1)))
            elif t == 'QUEBRA':
                D and D.quebra()
            elif t == 'REFERENCIAS':
                for k, n in sorted(refs.items(), key=lambda kv: kv[1]):
                    D and D.par(f'{n}. {REFS.get(k, "[referência não encontrada: " + k + "]")}', 'Lumis Nota')
            else:
                txt = resolver(t, figs, tabs, refs, avisos, org); checar_texto(txt, org, avisos)
                D and D.par(txt)
        elif tipo == 'FIG':
            D and setattr(D, 'lista_num_aberta', False)
            if d['chave'] not in FIGS:
                avisos.append(f'{org}: figura desconhecida: {d["chave"]}'); continue
            caminho, larg = FIGS[d['chave']]
            leg = f'Figura {figs[d["chave"]]}. ' + resolver(d['legenda'], figs, tabs, refs, avisos, org)
            checar_texto(leg, org, avisos)
            D and D.figura(caminho, d['largura'] or larg, leg)
        elif tipo in ('TAB', 'NIVEIS'):
            D and setattr(D, 'lista_num_aberta', False)
            if not d['linhas']:
                avisos.append(f'{org}: tabela sem linhas: {d["chave"]}'); continue
            ncol = max(len(r) for r in d['linhas'])
            larg = d['larguras']
            if tipo == 'NIVEIS':
                ncol = 3
            if len(larg) != ncol:
                avisos.append(f'{org}: tabela {d["chave"]} tem {ncol} colunas e {len(larg)} larguras')
                larg = (larg + [LARGURA_UTIL / ncol] * ncol)[:ncol]
            if sum(larg) > LARGURA_UTIL + 0.05:
                avisos.append(f'{org}: tabela {d["chave"]} com {sum(larg):.1f} cm (máximo {LARGURA_UTIL})')
            for r_i, row in enumerate(d['linhas']):
                if len(row) != len(d['linhas'][0]) and tipo == 'TAB':
                    avisos.append(f'{org}: tabela {d["chave"]}, linha {r_i + 1} com {len(row)} células (cabeçalho tem {len(d["linhas"][0])})')
            linhas_res = [[resolver(c, figs, tabs, refs, avisos, org) for c in row] for row in d['linhas']]
            for row in linhas_res:
                for c in row:
                    checar_texto(c, org, avisos, celula=True)
            leg = f'Tabela {tabs[d["chave"]]}. ' + resolver(d['legenda'], figs, tabs, refs, avisos, org)
            checar_texto(leg, org, avisos)
            if D:
                (D.tabela_niveis if tipo == 'NIVEIS' else D.tabela)(linhas_res, larg, leg)
        elif tipo == 'CAIXA':
            D and setattr(D, 'lista_num_aberta', False)
            D and D.caixa(d['linhas'])
    if saida:
        D.d.save(saida)
    return avisos, figs, tabs, refs



if __name__ == '__main__':
    modo = sys.argv[1] if len(sys.argv) > 1 else 'lint'
    sys.stdout.reconfigure(encoding='utf-8')
    if modo == 'lint':
        avisos, figs, tabs, refs = montar('dossie', ':dossie', None)
    else:
        avisos, figs, tabs, refs = montar('dossie', ':dossie', sys.argv[2])
    for a in avisos:
        print('AVISO', a)
    print(f'avisos: {len(avisos)}; figuras: {len(figs)}; tabelas: {len(tabs)}')
