"""F2-E2 v2: relatório ao conselho, a partir do levantamento (F2-E2_Levantamento_v1.md) e das decisões D-026 e D-027.
Base de formatação: F2-E1 v2 (capa só com título e subtítulo, cabeçalho e rodapé do design system)."""
import re, sys, docx
from docx.shared import Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE = 'C:/Users/gusta/Downloads/LumisOS/'
MODELO = BASE + '02_Fase2_O_Mercado/F2-E1_Mapa_do_Territorio/F2-E1_Mapa_do_Territorio_v2.docx'
FIG = BASE + '02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/figuras/'
OUT = sys.argv[1]

d = docx.Document(MODELO)
st = d.styles
body = d.element.body

# cabeçalho das páginas internas
hp = d.sections[0].header.paragraphs[0]
feito = False
for r in hp.runs:
    if r.text.strip():
        r.text = '' if feito else '\tF2-E2 · Auditoria do Ativo'
        feito = True

# título e subtítulo; apaga o resto do corpo
for p, t in ((d.paragraphs[0], 'Auditoria do Ativo'),
             (d.paragraphs[1], 'Relatório ao Conselho: de que é feito o ativo da Lumis e que números sobrevivem a uma auditoria independente')):
    p.runs[0].text = t
    for r in p.runs[1:]:
        r.text = ''
sub = d.paragraphs[1]._p
apagar = False
for el in list(body):
    if apagar and el.tag != qn('w:sectPr'):
        body.remove(el)
    if el is sub:
        apagar = True

TAG = re.compile(r'(\[(?:fonte|hipótese|não consta|risco)[^\]]*\])')
TAGSTYLE = {'fonte': 'Tag Fonte', 'hipótese': 'Tag Hipótese', 'não consta': 'Tag Não consta', 'risco': 'Tag Risco'}


def runs(p, text):
    for i, seg in enumerate(text.split('**')):
        for part in TAG.split(seg):
            if not part:
                continue
            r = p.add_run(part)
            if TAG.fullmatch(part):
                r.style = st[TAGSTYLE[next(k for k in TAGSTYLE if part[1:].startswith(k))]]
            elif i % 2:
                r.bold = True
    return p


def P(text, style='Normal'):
    return runs(d.add_paragraph(style=style), text)


def B(text):
    return P(text, 'List Bullet')


def H1(t): d.add_heading(t, level=1)
def H2(t): d.add_heading(t, level=2)


def FIGURA(arq, legenda):
    p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(FIG + arq, width=Cm(16))
    P(legenda, 'Caption')


def shade(cell, fill):
    s = OxmlElement('w:shd'); s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), fill)
    cell._tc.get_or_add_tcPr().append(s)


def TABELA(linhas, larguras, legenda, junta=False):
    tb = d.add_table(rows=len(linhas), cols=len(linhas[0])); tb.alignment = WD_TABLE_ALIGNMENT.CENTER
    bd = OxmlElement('w:tblBorders')
    for side in ('top', 'bottom', 'insideH'):
        e = OxmlElement(f'w:{side}'); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '4'); e.set(qn('w:color'), 'D3DEDB')
        bd.append(e)
    tb._tbl.tblPr.append(bd); tb.autofit = False
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tb._tbl.tblPr.append(lay)
    th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), 'true'); tb.rows[0]._tr.get_or_add_trPr().append(th)
    for gc, w in zip(tb._tbl.tblGrid.findall(qn('w:gridCol')), larguras):
        gc.set(qn('w:w'), str(int(w * 567)))
    for r in tb.rows:  # linha não se parte entre páginas
        r._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
    for i, row in enumerate(linhas):
        for j, txt in enumerate(row):
            c = tb.cell(i, j); c.width = Cm(larguras[j])
            p = c.paragraphs[0]; p.style = st['Lumis Tabela']
            if i == 0:
                p.paragraph_format.keep_with_next = True  # cabeçalho não fica sozinho no pé da página
                r = p.add_run(txt); r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                shade(c, '0F2D3A')
            else:
                partes = txt.split('\n')
                runs(p, partes[0])
                for extra in partes[1:]:
                    runs(c.add_paragraph(style='Lumis Tabela'), extra)
                if junta or i == len(linhas) - 1:  # junta: a tabela inteira fica na mesma página
                    for q in c.paragraphs:
                        q.paragraph_format.keep_with_next = True  # legenda não fica sozinha na página seguinte
                if i % 2 == 0:
                    shade(c, 'F1F6F4')
    P(legenda, 'Caption')


# ---------------- abertura ----------------
# Versão para o documento único (07/10/2026): o essencial, com figuras no lugar de tabelas de texto.
P('Hoje o ativo da Lumis não passa numa auditoria independente. A parte da base que só a Lumis tem está sob contratos frágeis, e o modelo erra mais justamente com quem mais precisa de prioridade.', 'Lumis Destaque')

# ---------------- 1. dados ----------------
H1('1. De onde vêm os dados e se a Lumis pode usá-los')
FIGURA('v2_fig1_base.png', 'Figura 1. A base de treinamento do Lumis Insight. Fonte: Cap. 2, Quadro 7.')
B('**Só pouco mais de um quarto da base é da Lumis.** O DATASUS, que é a maior parte, está aberto a qualquer concorrente. Dos dados de clientes, um terço vem de contratos que não autorizam o treino com clareza, e esses são os primeiros a vencer.')
B('**O risco já existe.** Nenhum dos seis contratos de dados passou por revisão jurídica, e o modelo atual já foi treinado com esses dados. Dado de saúde é dado sensível, e a LGPD pede finalidade específica e informada². Quem trata dados em nome do cliente só pode usá-los para a finalidade definida por ele³, e uma cláusula de "melhoria contínua do serviço" dificilmente cobre treinar um produto vendido a outros clientes.')
B('**Parte dos dados é anterior à empresa.** Há registros desde 2019, e a Lumis foi fundada em 2022 [fonte: Cap. 2, Quadros 3 e 7]. Sob que cláusula esse histórico chegou [não consta].')
P('**Recomendação:** parecer da DPO sobre os seis contratos antes do próximo treino, e renegociação de Prisma e Vila Ipê antes do vencimento, incluindo o histórico.')

# ---------------- 2. variáveis ----------------
H1('2. O que o modelo mede de fato')
P('As variáveis que mais pesam no modelo deveriam medir necessidade e gravidade. Na prática, medem acesso: quem conseguiu ser atendido e quanto isso custou. Quem teve menos acesso parece menos grave. Esse é o caso de proxy que o capítulo descreve, e ele diz que "foi exatamente isso que aconteceu no incidente da Fase 1" [fonte: Cap. 2, 2.2].')
FIGURA('v2_fig2_proxy.png', 'Figura 2. Quatro variáveis, que somam metade do peso do modelo, medem acesso. Fonte: Cap. 2, Quadro 8; leitura da equipe.')
P('**Um caso real com o mesmo erro.** Em 2019, um estudo publicado na revista Science mostrou que um algoritmo usado nos Estados Unidos previa o custo do paciente, e não a doença¹. Pacientes negros, com menos acesso, gastavam menos e recebiam o mesmo escore de pacientes brancos mais saudáveis. O caso não faz parte da história da Lumis e entra como comparação.')

# ---------------- 3. campo ----------------
H1('3. O que acontece em campo')
P('Os 94% de acurácia vêm de uma amostra de 2023 com dois hospitais da mesma região. Em campo, a parcela de pacientes que precisavam de prioridade e não receberam mais que dobrou, e o erro se concentra em quem já é mais vulnerável [fonte: Cap. 2, Quadros 9 e 10].')
FIGURA('fig1_subgrupo_v2.png', 'Figura 3. Pacientes que precisavam de prioridade e não receberam, por grupo, 1º semestre de 2026. Fonte: Cap. 2, Quadros 9 e 10.')
P('Quem mediu o pior número foi o Hospital Vila Ipê, e não a Lumis. Só 2% das decisões passam por revisão humana, e as reclamações, que vêm na maioria de pacientes de CEP D/E, nunca foram cruzadas com o desempenho do modelo [fonte: Cap. 2, Quadros 10, 12 e 17].')

# ---------------- 4. métricas ----------------
H1('4. Os números que mostramos ao mercado')
P('O Vetor Capital avisou que número que não sobrevive a uma auditoria independente vira passivo. Passamos as métricas de hoje pelas quatro perguntas do capítulo [fonte: Cap. 2, 2.3], e nenhuma fica como está. O caso mais grave são os "5 milhões de vidas": a contagem repetida foi achada em janeiro e continua no material comercial [fonte: Cap. 2, Quadro 14]. Manter esses números contradiz o compromisso de Transparência da nossa Declaração de Intenção.')
FIGURA('v2_fig4_metricas.png', 'Figura 4. As métricas de hoje e as quatro perguntas. Todas saem ou são trocadas. Fonte: Cap. 2, Quadros 9, 11 e 14.')

# ---------------- 5. indicadores ----------------
H1('5. O que passamos a medir e o que decidimos agora')
P('No lugar delas, propomos cinco indicadores. Cada um muda uma decisão concreta e se abre por grupo. Como a Lumis mede o erro do próprio produto, cada um tem alguém de fora que confere.')
P('**A decisão de agora.** Dois grupos já passam do limite do indicador 1, o dobro do erro do melhor grupo: idosos de CEP C e de CEP D/E. O compromisso de Não Amplificação de Danos, da nossa Declaração de Intenção, manda suspender o uso até a correção quando há padrão de viés. Por isso recomendamos restringir já a recomendação automática nesses grupos. Cerca de um quarto das decisões volta à triagem do hospital, e o modelo segue rodando em paralelo para medir a correção. A Entrega 3 define quem executa a restrição.')
FIGURA('v2_fig5_indicadores.png', 'Figura 5. Os cinco indicadores e as quatro perguntas. Os limites que disparam cada decisão são proposta da equipe. Fonte: Cap. 2, Quadros 7, 10, 14 e 17.')

# ---------------- 6. tese ----------------
H1('6. O que isso muda na tese')
P('A base de clientes só vira vantagem difícil de copiar quando tiver direito de uso limpo e erro por grupo que alguém de fora consiga refazer. Por isso, o memorando leva três condições prévias ao aporte: regularizar os contratos antes do vencimento, tirar do mercado os números que não se sustentam e medir o erro por grupo com conferência externa.')

H2('Referências')
for t in [
    '1. OBERMEYER, Z. et al. Dissecting racial bias in an algorithm used to manage the health of populations. Science, v. 366, n. 6464, p. 447-453, 2019.',
    '2. BRASIL. Lei nº 13.709/2018 (LGPD), arts. 5º, 6º e 11. Consulta em 06/10/2026.',
    '3. ANPD. Guia Orientativo para Definições dos Agentes de Tratamento de Dados Pessoais e do Encarregado. Versão 2.0, 2022.',
]:
    P(t, 'Lumis Nota')
P('Dados da Lumis: Cap. 2, Anexo A. Contas e propostas são da equipe. A empresa real citada é análogo e não faz parte do caso Lumis.', 'Lumis Nota')

d.save(OUT)
print('ok')
