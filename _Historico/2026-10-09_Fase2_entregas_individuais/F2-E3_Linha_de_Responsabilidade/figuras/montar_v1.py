"""F2-E3 v1: Linha de Responsabilidade, versão enxuta para o documento integrado.
Base: F2-E3_Levantamento_v1.md. Cargos citados pelo papel, sem nome. Tabelas com células curtas.
Formatação: a mesma da F2-E2 v2 (capa, cabeçalho e rodapé do design system)."""
import re, sys, docx
from docx.shared import Cm, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE = 'C:/Users/gusta/Downloads/LumisOS/'
MODELO = BASE + '02_Fase2_O_Mercado/F2-E1_Mapa_do_Territorio/F2-E1_Mapa_do_Territorio_v2.docx'
OUT = sys.argv[1]

d = docx.Document(MODELO)
st = d.styles
body = d.element.body

hp = d.sections[0].header.paragraphs[0]
feito = False
for r in hp.runs:
    if r.text.strip():
        r.text = '' if feito else '\tF2-E3 · Linha de Responsabilidade'
        feito = True

for p, t in ((d.paragraphs[0], 'Linha de Responsabilidade'),
             (d.paragraphs[1], 'Quem autoriza, quem monitora e quem pode desligar cada decisão do Lumis Insight')):
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


def shade(cell, fill):
    s = OxmlElement('w:shd'); s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), fill)
    cell._tc.get_or_add_tcPr().append(s)


def TABELA(linhas, larguras, legenda):
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
    for r in tb.rows:
        r._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
    for i, row in enumerate(linhas):
        for j, txt in enumerate(row):
            c = tb.cell(i, j); c.width = Cm(larguras[j])
            p = c.paragraphs[0]; p.style = st['Lumis Tabela']
            p.paragraph_format.keep_with_next = True  # tabelas curtas: ficam inteiras na página, com a legenda
            if i == 0:
                r = p.add_run(txt); r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                shade(c, '0F2D3A')
            else:
                runs(p, txt)
                if i % 2 == 0:
                    shade(c, 'F1F6F4')
    P(legenda, 'Caption')


# ---------------- abertura ----------------
P('Os registros da Lumis não mostram, para nenhuma decisão do Lumis Insight, um cargo que autorizou o uso, um que acompanha o erro e um que pode desligar o sistema em prazo conhecido. A única porta com dono é a liberação de novas versões, e, pela nossa leitura, os incidentes dos últimos dois anos entraram por outras portas.', 'Lumis Destaque')
P('O sistema toma cerca de um milhão de decisões por mês. A maior parte delas, a priorização da fila de atendimento, foi autorizada por uma diretoria comercial do cliente, sem aprovação interna formal. A Lumis não tem comitê de ética nem de risco, metade dos incidentes foi descoberta pelo cliente e só cerca de uma em cada quatro pessoas da empresa sabe a quem levar um problema ético do produto [fonte: Cap. 2, Quadros 12, 14 e 15]. Esta entrega dá um cargo a cada etapa: autorizar, acompanhar, suspender e religar.')

# ---------------- 1. mapa ----------------
H1('1. As decisões que o sistema toma hoje')
P('Classificamos como de alto impacto toda decisão que afeta a saúde ou o acesso a um serviço essencial. Volume alto e revisão já existente não rebaixam o nível; só mudam o controle necessário. Decisão sem erro medido por grupo fica como alta até ser medida.')
TABELA([
    ['Decisão', 'Por mês', 'Revisão humana hoje', 'Quem autorizou o uso', 'Impacto'],
    ['Priorização da fila de atendimento', '640 mil', 'Amostra de 2%', 'Diretoria comercial do cliente, sem aprovação interna formal', '**Alto**'],
    ['Sugestão de protocolo clínico', '210 mil', 'Sempre, pelo médico', 'Comitê clínico do hospital', '**Alto**'],
    ['Classificação de risco de sinistro', '74 mil', 'Só acima de R$ 50 mil', 'Diretoria da seguradora', '**Alto**'],
    ['Sinalização de risco de crédito', '31 mil', 'Sempre', 'Comitê de crédito do banco', '**Alto**'],
    ['Roteamento de mensagens de suporte', '95 mil', 'Nenhuma', 'Operação da Lumis', 'Baixo'],
], [4.4, 1.6, 3.2, 4.8, 1.6], 'Tabela 1. Decisões delegadas ao sistema. Fonte: Cap. 2, Quadro 12. A coluna Impacto é classificação da equipe.')
B('**O controle segue o costume de cada cliente.** O crédito, com 31 mil decisões, tem revisão em todos os casos. A priorização, com 640 mil e viés já medido, tem revisão em 2%. O impacto sobre as pessoas não entra na conta.')
B('**Nenhuma autorização termina em um cargo.** Quatro foram dadas por órgãos do cliente e uma por uma área da Lumis. Na priorização, o quadro registra que não houve aprovação interna formal; no protocolo, no sinistro e no crédito, ela [não consta].')
B('**Sinistro e roteamento.** No sinistro, o erro por grupo não é acompanhado, e o corte de R$ 50 mil olha o valor do sinistro, não o efeito sobre o segurado [hipótese]. O roteamento sobe de nível se o canal receber contestação de decisão do sistema.')

# ---------------- 2. hoje ----------------
H1('2. Quem responde hoje e o que os incidentes mostram')
P('A estrutura atual tem sete papéis com dono, mas só um deles controla o que entra em produção: a decisão de liberar uma nova versão do modelo é exclusiva do CTO [fonte: Cap. 2, Quadros 12 e 13]. Nenhum registro diz quem pode suspender o sistema nem em quanto tempo [não consta]. Na Fase 1, esse poder ficou com a liderança em conjunto, sem prazo [fonte: F1-E2].')
TABELA([
    ['Quando', 'O que aconteceu', 'Quem percebeu', 'Correção', 'Por onde entrou'],
    ['03/2025', 'Exames de um laboratório novo passaram a ser descartados', 'Cliente', '22 dias', 'Dados de entrada'],
    ['09/2025', 'Queda de desempenho após atualização do fornecedor do modelo', 'Equipe interna', '6 dias', 'Fornecedor'],
    ['01/2026', 'Registros duplicados inflaram as "vidas analisadas"', 'Auditoria interna', 'Só no sistema', 'Material comercial'],
    ['07/2026', 'Viés etário e regional na priorização', 'Hospital Vila Ipê', 'Em tratamento', 'Acompanhamento por grupo'],
], [1.7, 5.4, 2.8, 2.4, 3.3], 'Tabela 2. Incidentes dos últimos 24 meses. Fonte: Cap. 2, Quadro 14. A coluna Por onde entrou é leitura da equipe.')
P('Pela nossa leitura, os incidentes entraram por portas sem dono: dados novos, mudança do fornecedor, material comercial e uso autorizado só pelo cliente [hipótese]. Se a atualização do fornecedor de 09/2025 passou pela liberação do CTO [não consta].')

# ---------------- 3. linha ----------------
H1('3. A linha de responsabilidade proposta')
P('Três regras orientam o desenho. Quem libera uma versão não é o único que acompanha o erro nem o único que pode suspender. Suspender exige um só cargo, e religar exige dois. A autorização do cliente continua necessária, mas a Lumis também passa a autorizar.')
TABELA([
    ['Etapa', 'Cargo responsável', 'Contrapeso'],
    ['Autorizar cada uso em cada cliente', 'CEO', 'Parecer obrigatório do Head of AI Management e da DPO'],
    ['Liberar versão nova ou atualização do fornecedor', 'CTO', 'Head of AI Management confere o teste por grupo e pode barrar'],
    ['Medir o erro por grupo e cruzar as reclamações', 'Responsável por Dados', 'Auditor externo, contratado pela CEO, refaz a conta'],
    ['Acompanhar e confirmar o alerta', 'Head of AI Management', 'DPO como suplente'],
    ['Suspender ou restringir', 'Head of AI Management', 'CTO e DPO também podem suspender'],
    ['Executar a suspensão', 'CTO', 'Responsável por Dados como suplente'],
    ['Religar', 'CTO e Head of AI Management, juntos', 'Sem acordo, segue suspenso e a CEO leva o caso ao conselho'],
    ['Aprovar os números divulgados ao mercado', 'Head of AI Management', 'Responsável Comercial corrige o material'],
    ['Proteger dados pessoais e direito de uso', 'DPO', 'Responsável por Dados retira o dado sem autorização'],
    ['Prestar contas ao conselho', 'CEO', 'Head of AI Management relata as suspensões diretamente'],
], [5.6, 4.4, 5.6], 'Tabela 3. Quem responde por cada etapa. Proposta da equipe sobre os cargos do Cap. 2, Quadro 13.')
P('A linha vale para as quatro decisões de alto impacto. O que muda entre elas é o sinal que dispara o alerta, lido a cada quinze dias, como prevê o compromisso de Não Amplificação de Danos. Qualquer queixa de cliente, contestação de paciente ou incidente dispara o alerta na hora, sem esperar a leitura.')
TABELA([
    ['Decisão', 'Sinal de alerta'],
    ['Priorização da fila', 'Grupo com o dobro do erro do melhor grupo'],
    ['Protocolo clínico', 'Grupo com o dobro de sugestões alteradas pelo médico'],
    ['Risco de crédito', 'Faixa de CEP com aprovação abaixo de 80% da melhor'],
    ['Risco de sinistro', 'Faixa de CEP com o dobro de negativas da melhor'],
], [4.6, 11.0], 'Tabela 4. Alertas por decisão. Priorização: Entrega 2. Protocolo e crédito: Entrega 5. Sinistro: proposta da equipe; ainda não é medido.')
P('**Prazo para suspender.** Confirmado o alerta, a decisão sai em até 24 horas e a execução em mais 24. Com dano clínico em curso, a execução é imediata, dentro do mesmo teto. Usamos como teto as 48 horas que já prometemos para revisar um caso contestado: desligar o sistema não deve demorar mais que isso. Como o tempo real de suspensão não é conhecido [não consta], o prazo é uma meta até o primeiro teste. Se o teste passar de 48 horas, o teto continua e o CTO corrige o procedimento até cumpri-lo.')
P('**O que fazemos já:**')
B('Executar a restrição recomendada na Entrega 2. O Head of AI Management ordena e o CTO executa de imediato: a priorização de idosos de CEP C e D/E volta à triagem do hospital, com o modelo rodando em paralelo, sem decidir.')
B('Testar a suspensão em até 30 dias, por cliente e por grupo, e repetir a cada trimestre. O Head of AI Management conduz o teste e o CTO executa.')
B('Exigir, nos contratos, um cargo do lado do cliente que assine a autorização de uso. A cláusula fica com a DPO.')

# ---------------- 4. revisão humana ----------------
H1('4. Quando a revisão humana é obrigatória')
B('**Priorização em grupo com o dobro do erro do melhor:** todos os casos voltam ao profissional responsável pela triagem no hospital. Critério: erro medido em grupo vulnerável é o padrão de viés que, pelo compromisso de Não Amplificação de Danos, justifica suspender o uso até a correção. Nos demais grupos críticos, a revisão sobe de 2% para 10%, como proposto na Entrega 2, para que a leitura quinzenal tenha casos suficientes.')
B('**Toda contestação** de paciente, profissional ou cliente: imediata na urgência e em até 48 horas nos demais casos. Critério: o compromisso de Reversibilidade.')
B('**Toda sugestão de protocolo clínico**, como já ocorre, agora com registro de aceite, alteração ou rejeição pelo médico. Critério: o dano é à saúde, e revisão sem registro não pode ser auditada.')
B('**Classificação de sinistro que leve a negativa ou atraso**, no lugar do corte de R$ 50 mil. Critério: o efeito sobre a pessoa.')
B('**Toda sinalização de risco de crédito**, como já ocorre. Critério: acesso a serviço essencial.')
B('**Fonte de dados nova, cliente novo ou versão nova:** revisão de 10% dos casos até uma leitura quinzenal sem piora em nenhum grupo. Critério: os incidentes de 03/2025 e 09/2025 começaram assim.')

# ---------------- 5. novo setor ----------------
H1('5. O que muda num setor novo')
P('Num setor novo a Lumis não sabe reconhecer o erro típico nem tem dado local para medi-lo. O backlog já traz um pedido assim, um produto para o setor veterinário, e o Vetor Capital propõe transformar o produto em plataforma e abrir dois países [fonte: Cap. 2, 1.1 e Quadro 16]. A estrutura muda em cinco pontos:')
B('**Portão de entrada.** O responsável por Produto leva o pedido, a CEO decide e o Head of AI Management e a DPO dão parecer obrigatório. Os critérios de entrada e de encerramento ficam no funil da Entrega 4.')
B('**Modo sombra.** O sistema roda em paralelo, sem decidir, até haver erro medido por grupo no novo domínio.')
B('**Responsável do domínio.** Um especialista do setor, do cliente ou contratado, assina o que conta como erro grave, por exemplo um médico-veterinário.')
B('**Suspensão testada antes de começar.** O CTO testa a suspensão por mercado e por cliente antes da entrada.')
B('**Quem mede o erro em cada mercado.** O responsável por Dados indica a pessoa antes da entrada, e o Head of AI Management aprova. O time de dados teve rotatividade de 27% em doze meses [fonte: Cap. 2, Quadro 15].')
P('O capítulo resume o risco: sem uma linha de responsabilidade explícita, a expansão para novos setores "multiplica exposição sem multiplicar controle" [fonte: Cap. 2, 2.4]. Por isso a linha precisa estar pronta antes do aporte.')

# ---------------- 6. coerência ----------------
H1('6. Coerência com o que já assumimos')
P('Os compromissos da Declaração de Intenção continuam valendo, agora com cargo: Transparência com o Head of AI Management, Segurança e Privacidade com a DPO, e a leitura quinzenal de Não Amplificação de Danos com o responsável por Dados e o Head of AI Management.')
P('Três atribuições mudam. O poder de suspender, que na Fase 1 era da liderança em conjunto, passa ao Head of AI Management, que já coordenava a investigação de incidentes, com CTO e DPO como chaves adicionais. A liberação de versão continua com o CTO, com a conferência do Head of AI Management. E cada uso passa a precisar da autorização da CEO, além da do cliente. A Entrega 5 já indicava o Head of AI Management para suspender, e aqui o cargo fica confirmado.')

P('Dados da Lumis: Cap. 2, Anexo A. Classificações, alertas, prazos e cargos propostos são da equipe.', 'Lumis Nota')

d.save(OUT)
print('ok')
