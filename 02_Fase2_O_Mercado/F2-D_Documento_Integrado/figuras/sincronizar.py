"""Aplica no .docx editado no Word (formatação/capa da equipe) o texto novo gerado pelo script.
Uso: python sincronizar.py <editado.docx> <gerado.docx> <saida.docx>
Alinha os elementos do corpo a partir do primeiro Título 1; parágrafos com texto diferente recebem os runs do gerado
(mantendo o pPr do editado: justificação etc.); tabelas diferentes são trocadas inteiras; elementos novos são inseridos."""
import sys, copy, difflib, docx
from docx.oxml.ns import qn
ed, ge, out = sys.argv[1:4]
U, G = docx.Document(ed), docx.Document(ge)
JUST = ('Normal', 'List Bullet', 'List Number')

def elems(d):
    body = d.element.body
    els = [e for e in body.iterchildren() if e.tag in (qn('w:p'), qn('w:tbl'))]
    for i, e in enumerate(els):
        if e.tag == qn('w:p') and docx.text.paragraph.Paragraph(e, d).style.name == 'Heading 1':
            return els[i:]
def sig(d, e):
    if e.tag == qn('w:tbl'):
        t = docx.table.Table(e, d); return ('tbl', len(t.columns))
    return ('p', docx.text.paragraph.Paragraph(e, d).style.name)
def txt(d, e):
    if e.tag == qn('w:tbl'):
        return '\n'.join('|'.join(c.text for c in r.cells) for r in docx.table.Table(e, d).rows)
    return docx.text.paragraph.Paragraph(e, d).text
eu, eg = elems(U), elems(G)
# os ids de estilo mudam quando o Word salva (ex.: Heading2 -> Ttulo2); traduz pelo nome
nome_u = {s.name: s.style_id for s in U.styles}
mapa = {s.style_id: nome_u[s.name] for s in G.styles if s.name in nome_u}
def ids(x):
    for tag in ('w:pStyle', 'w:rStyle', 'w:tblStyle'):
        for e in x.iter(qn(tag)):
            v = e.get(qn('w:val'))
            if v in mapa: e.set(qn('w:val'), mapa[v])
    return x
su, sg = [sig(U, e) for e in eu], [sig(G, e) for e in eg]
log = []
def troca_par(a, b):
    for r in [c for c in a if c.tag != qn('w:pPr')]:
        a.remove(r)
    for r in b:
        if r.tag != qn('w:pPr'):
            a.append(ids(copy.deepcopy(r)))
def novo(b):
    n = ids(copy.deepcopy(b))
    if n.tag == qn('w:p'):
        p = docx.text.paragraph.Paragraph(n, G)
        if p.style.name in JUST and p.text.strip():
            from docx.enum.text import WD_ALIGN_PARAGRAPH
            docx.text.paragraph.Paragraph(n, U).alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return n
sm = difflib.SequenceMatcher(None, [s + (txt(U, e)[:40],) for s, e in zip(su, eu)], [s + (txt(G, e)[:40],) for s, e in zip(sg, eg)], autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal':
        for a, b in zip(eu[i1:i2], eg[j1:j2]):
            if txt(U, a) != txt(G, b):
                if a.tag == qn('w:p'): troca_par(a, b)
                else: a.getparent().replace(a, ids(copy.deepcopy(b)))
                log.append('atualizado (igual): ' + txt(G, b)[:70])
        continue
    A, Bs = eu[i1:i2], eg[j1:j2]
    k = 0
    while k < min(len(A), len(Bs)) and sig(U, A[k]) == sig(G, Bs[k]):
        a, b = A[k], Bs[k]
        if a.tag == qn('w:p'):
            if a.xpath('.//w:drawing') or b.xpath('.//w:drawing'):
                log.append('ATENÇÃO figura: ' + txt(G, b)[:60]); k += 1; continue
            troca_par(a, b)
        else:
            a.getparent().replace(a, ids(copy.deepcopy(b)))
        log.append('atualizado: ' + txt(G, b)[:70]); k += 1
    ancora = A[k - 1] if k > 0 else (eu[i1 - 1] if i1 > 0 else None)
    for b in Bs[k:]:
        n = novo(b); ancora.addnext(n); ancora = n
        log.append('inserido: ' + txt(G, b)[:70])
    for a in A[k:]:
        log.append('removido: ' + txt(U, a)[:70]); a.getparent().remove(a)
U.save(out)
print('\n'.join(log))
