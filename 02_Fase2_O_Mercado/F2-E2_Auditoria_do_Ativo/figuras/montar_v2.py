"""F2-E2 v2: relatório ao conselho, a partir do levantamento (F2-E2_Levantamento_v1.md) e das decisões D-023 e D-024.
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
                if i == len(linhas) - 1:
                    for q in c.paragraphs:
                        q.paragraph_format.keep_with_next = True  # legenda não fica sozinha na página seguinte
                if i % 2 == 0:
                    shade(c, 'F1F6F4')
    P(legenda, 'Caption')


# ---------------- abertura ----------------
P('Hoje o ativo da Lumis não passa numa auditoria independente. A parte da base que só a Lumis tem está sob contratos frágeis, e o modelo erra mais justamente com quem mais precisa de prioridade.', 'Lumis Destaque')
P('A parte exclusiva da base são 5,9 milhões de registros de clientes. Desses, 35,4% vêm de contratos com autorização frágil para treinamento, e nenhum dos seis contratos de dados passou por revisão jurídica desde a assinatura. Em campo, de cada 10 pacientes com 60 anos ou mais de CEP D/E que precisavam de prioridade, 3 foram classificados como baixa prioridade, e quem mediu isso foi o hospital. Das cinco afirmações que a Lumis divulga ao mercado, nenhuma passa numa auditoria do jeito que é divulgada.')
P('**Pedido ao conselho.** Duas decisões agora: restringir a recomendação automática para pacientes com 60 anos ou mais de CEP C e D/E, com o custo descrito na seção 5, e tirar do material comercial os números que não se sustentam. A regularização dos contratos e os cinco indicadores de gestão seguem com prazo e responsável.')

# ---------------- 1. dados ----------------
H1('1. De onde vêm os dados e se a Lumis pode usá-los')
P('A base de treinamento soma 22,0 milhões de registros. O DATASUS responde por 63,6% e os dados sintéticos gerados pela própria Lumis por 9,5%. O DATASUS tem uso autorizado, só que está aberto a qualquer concorrente. O que é exclusivo da Lumis são os 26,8% vindos de clientes, e é nessa parte que estão as fragilidades [fonte: Cap. 2, Quadro 7].')
TABELA([
    ['Fonte', 'Volume e período', 'O que o contrato diz sobre treino', 'Vence', 'Leitura da equipe'],
    ['**Seguradora Prisma**', '890 mil sinistros, 2021 a 2026', 'Nada (contrato silente)', '12/2026', 'Sem autorização. Vence em menos de três meses'],
    ['**Hospital Vila Ipê**', '1,2 mi atendimentos, 2019 a 2026', 'Cláusula genérica: "melhoria contínua do serviço"', '03/2027', 'Autorização frágil. É também o hospital que notificou o viés'],
    ['**Rede Sanare** (7 unidades)', '3,4 mi atendimentos, 2020 a 2026', 'Sim, para uso agregado e anonimizado', '08/2028', 'Autoriza com condição. Se o treino cumpre a condição [não consta]'],
    ['**Banco Meridiano**', '410 mil operações, 2023 a 2026', 'Sim, com auditoria anual do cliente', '05/2028', 'Autoriza com condição. Sigilo bancário pede atenção própria'],
    ['**DATASUS**', '14,0 mi registros, 2015 a 2024', 'Uso público', 'Não se aplica', 'Autorizado e aberto a todos'],
    ['**Sintéticos internos**', '2,1 mi registros, 2024 a 2026', 'Geração própria', 'Não se aplica', 'De que dados foram gerados [não consta]'],
], [3.0, 3.1, 3.7, 1.7, 4.5], 'Tabela 1. As seis fontes da base de treinamento, da mais frágil para a mais segura. Fonte: Cap. 2, Quadro 7; leitura da equipe.')
P('Os pontos frágeis são quatro:')
B('**Autorização.** Prisma e Vila Ipê somam 2,09 milhões de registros, 35,4% dos dados de clientes. Nenhum dos seis instrumentos passou por revisão jurídica, e a política de privacidade para dados de saúde está em elaboração desde 2024, sem versão aprovada [fonte: Cap. 2, Quadros 7 e 17]. O modelo atual já foi treinado com esses dados, então o risco existe hoje, antes de qualquer vencimento.')
B('**Base legal.** Dado de saúde é dado pessoal sensível, e a LGPD pede finalidade específica e informada ao titular³. Uma cláusula de "melhoria contínua do serviço" dificilmente cobre treinar um produto vendido a outros clientes. Quem trata dados em nome do cliente só pode usá-los para a finalidade definida por ele⁴. Ao treinar o próprio modelo, a Lumis passa a decidir uma finalidade própria e precisaria de base legal própria [hipótese].')
B('**Prazo.** As duas fontes frágeis são as que vencem primeiro: Prisma em 12/2026 e Vila Ipê em 03/2027. O Vila Ipê é, ao mesmo tempo, fonte de dados e o cliente que mandou a notificação formal sobre o viés [fonte: Cap. 2, Quadros 7 e 14].')
B('**Histórico anterior ao contrato.** A Lumis foi fundada em 2022, mas os dados do Vila Ipê começam em 2019, os da Sanare em 2020 e o contrato da Prisma é de 2021 [fonte: Cap. 2, Quadros 3 e 7]. Se esse histórico chegou à Lumis e sob que cláusula [não consta]. É a primeira pergunta que uma due diligence faria.')
P('**O que é defensável hoje.** No máximo os 3,81 milhões de registros da Sanare e do Meridiano, 64,6% dos dados de clientes, que têm autorização expressa. Mesmo essa parte depende de condições que ninguém verificou [fonte: conta da equipe sobre o Quadro 7]. Com autorização expressa e parecer jurídico, a parcela é zero.')
P('**Tamanho do risco.** Se Prisma e Vila Ipê pagam perto do ticket médio de R$ 1,084 milhão, os dois contratos valem cerca de R$ 2,2 milhões por ano, uns 5% do ARR [hipótese]. A LGPD prevê multa de até 2% do faturamento, limitada a R$ 50 milhões por infração, e também a eliminação dos dados³. O custo maior tende a ser retirar dados e retreinar o modelo [hipótese], e esse custo [não consta].')
P('O Cap. 2 diz em um trecho que são três os contratos com cláusula que ninguém releu, e o Quadro 5 fala em dois. Seguimos o Quadro 7, que mostra dois.', 'Lumis Nota')

# ---------------- 2. variáveis ----------------
H1('2. O que o modelo mede de fato')
P('As duas variáveis de maior peso no modelo são o número de atendimentos nos últimos 24 meses (18,4%) e o custo acumulado de procedimentos (15,1%). A empresa diz que elas medem necessidade de cuidado e gravidade [fonte: Cap. 2, Quadro 8]. Elas medem quem conseguiu ser atendido e quanto isso custou. Esse é o caso de variável proxy que o próprio capítulo descreve: quem usa gasto com saúde como indicador de gravidade mede "quem teve mais acesso a atendimento", e "foi exatamente isso que aconteceu no incidente da Fase 1" [fonte: Cap. 2, 2.2].')
P('Juntas, as duas somam 33,5% do peso do modelo. Numa população desigual, o paciente que teve menos acesso parece menos grave para o modelo do que é. Um caso real mostra o mesmo mecanismo: nos Estados Unidos, um algoritmo que usava custo no lugar de necessidade dava o mesmo escore a pacientes negros que estavam mais doentes que pacientes brancos¹.')
TABELA([
    ['Variável (peso)', 'A empresa diz medir', 'O que tende a medir', 'Distorção possível'],
    ['Nº de atendimentos em 24 meses (18,4%)', 'Necessidade de cuidado', 'Quem conseguiu ser atendido', 'Quem tem menos acesso parece precisar de menos'],
    ['Custo acumulado (15,1%)', 'Gravidade', 'Acesso a procedimentos pagos', 'Quem gasta menos parece menos grave'],
    ['Faixa de CEP (8,9%)', 'Região de residência', 'Renda e oferta de serviços perto de casa', 'Leva a desigualdade regional para dentro do modelo'],
    ['Tipo de plano (7,4%)', 'Cobertura contratada', 'Renda', 'Prioridade passa a depender do plano'],
    ['Idade (12,7%)', 'Idade', 'Idade, com fundamento clínico', 'Depende de como entra no modelo; o pior erro está nos idosos'],
    ['Comorbidades registradas (11,2%)', 'Carga de doença', 'Doença já diagnosticada', 'Quem não foi diagnosticado parece mais saudável'],
], [3.8, 3.0, 3.8, 5.4], 'Tabela 2. As variáveis de acesso e as de leitura discutível. As outras quatro estão no Anexo. Fonte: Cap. 2, Quadro 8; colunas 3 e 4: leitura da equipe [hipótese].')
P('A faixa de CEP reforça o caso. Ela mede o que a empresa diz, a região, e por isso mesmo carrega renda e oferta de serviços. Com a idade fixa, o falso negativo sobe de A/B para D/E nas duas faixas etárias: 9,6 pontos entre 18 e 59 anos e 15,9 pontos entre os de 60 ou mais [fonte: conta da equipe sobre o Quadro 10].')
P('Pelo critério da equipe, as variáveis que registram uso passado de serviços ou renda (atendimentos, custo, CEP e plano) somam 49,8% do peso do modelo [hipótese]. O único sinal clínico direto, o painel de exames laboratoriais, pesa 6,9%. O efeito da idade tem duas explicações que o anexo não permite separar: o rótulo do treino reflete uso passado, ou há poucos idosos na base [hipótese]. Os testes que separam as duas ficam para a Fase 3, e nenhum foi feito pela Lumis [não consta].')

# ---------------- 3. campo ----------------
H1('3. O que acontece em campo')
P('Os 94% de acurácia vêm de 48 mil registros de 2023, de dois hospitais da mesma região. Em campo, no primeiro semestre de 2026, com 1,94 milhão de registros, a acurácia foi de 87,6%. O número que importa para priorização piorou mais: o falso negativo, paciente que deveria ser priorizado e foi classificado como baixa prioridade, foi de 7,4% para 17,7%, quase 2,4 vezes [fonte: Cap. 2, Quadro 9]. Em IA clínica essa queda é comum. O modelo de sepse mais usado nos hospitais americanos teve, numa validação independente, desempenho bem abaixo do declarado pelo fornecedor².')
FIGURA('fig1_subgrupo_v2.png', 'Figura 1. Falso negativo em campo por subgrupo, 1º semestre de 2026. O grupo de 60 anos ou mais de CEP D/E tem três vezes o erro do melhor grupo. Fonte: Cap. 2, Quadros 9 e 10.')
P('O erro se concentra em quem já é mais vulnerável. Entre os pacientes com 60 anos ou mais de CEP D/E que precisavam de prioridade, 31,8% ficaram para trás. No grupo de 18 a 59 anos de CEP A/B, foram 10,6%. A sensibilidade do pior grupo é 68,2% [fonte: Cap. 2, Quadro 10].')
B('**Quem descobriu.** O 31,8% foi apurado pelo Hospital Vila Ipê, por conta própria, e enviado junto com a notificação formal [fonte: Cap. 2, Quadro 10].')
B('**Quanto passa por revisão humana.** Das 640 mil decisões de priorização por mês, 2% são revisadas por amostragem, cerca de 12.800 [fonte: Cap. 2, Quadro 12].')
B('**O que as reclamações já diziam.** Pacientes de CEP D/E são 25% da base e respondem por 47 das 74 reclamações formais do último ano, 64%. Esse registro nunca foi cruzado com o desempenho do modelo [fonte: Cap. 2, Quadro 17].')

# ---------------- 4. métricas ----------------
H1('4. Os números que mostramos ao mercado')
P('O Vetor Capital avisou que "qualquer número que não sobreviva a uma auditoria independente será tratado como passivo, não como diferencial" [fonte: Cap. 2, memorando]. Na maior parte dos casos, o problema está na forma de divulgar. Como diz o próprio caso sobre os 94%, "o número nunca foi mentira. Ele apenas nunca foi o que o comercial acreditava que era" [fonte: Cap. 2, 1.2].')
TABELA([
    ['Afirmação', 'O que autoriza dizer', 'O que não autoriza', 'Destino'],
    ['"Acurácia de 94%"', 'Que o modelo acertou 94,1% numa amostra de 2023 de dois hospitais', 'Que acerta 94% hoje, em qualquer cliente ou grupo', 'Aposentar. Entra o falso negativo por subgrupo (indicador 1)'],
    ['"Redução de 30% no tempo de triagem"', 'Que o tempo caiu 30,4% num piloto de seis semanas, sem grupo de controle', 'Atribuir a queda ao produto ou estender a outros hospitais', 'Retirar até haver estudo com comparação'],
    ['"Mais de 5 milhões de vidas analisadas"', 'Que houve 5,2 milhões de processamentos', 'Falar em vidas ou pessoas: há reprocessamento do mesmo paciente', 'Retirar já'],
    ['"NPS 72"', 'Que 9 clientes indicados pelo comercial aprovam o produto', 'Falar em satisfação da carteira de 38 contas', 'Aposentar. Entram as reclamações por subgrupo (indicador 3)'],
    ['"Disponibilidade de 99,9%"', 'Que a interface de programação ficou no ar 99,92% do tempo', 'Que o hospital recebeu a priorização correta a tempo', 'Sai do material comercial; segue como meta técnica'],
], [3.4, 4.5, 4.4, 3.7], 'Tabela 3. As cinco afirmações do painel comercial. As quatro perguntas aplicadas a cada uma estão no Anexo. Fonte: Cap. 2, Quadros 9 e 11.')
P('Os "5 milhões de vidas" são o caso mais grave. A auditoria interna achou a duplicidade em 01/2026, ela foi corrigida no sistema e o número continua no material comercial [fonte: Cap. 2, Quadro 14]. Manter qualquer uma das cinco afirmações como está contradiz o nosso compromisso de Transparência, que manda informar as limitações do sistema (C1).')

# ---------------- 5. indicadores ----------------
H1('5. O que passamos a medir e o que decidimos agora')
P('No lugar dos números de vitrine, propomos cinco indicadores de gestão. Cada um muda uma decisão, tem um limite que dispara essa decisão e termina num cargo. Os cargos vêm do Quadro 13 e são provisórios até a Entrega 3, que define quem responde por cada decisão. Os limites são propostas da equipe [hipótese]. Nenhuma fonte fixa valores para este caso.')
P('Para medir equidade, escolhemos uma regra: a mesma taxa de erro grave em todos os grupos. Em priorização, o erro grave é deixar de priorizar quem precisava. A regra tem custo: baixar o falso negativo de um grupo tende a priorizar mais pacientes nesse grupo, o que aumenta a carga do hospital. O indicador 1 acompanha esse custo junto.')
TABELA([
    ['Indicador', 'Hoje', 'Decisão que muda', 'Limite [hipótese]', 'Quem apura e quem decide'],
    ['**1. Falso negativo em campo por subgrupo** (idade e CEP, também por cliente)', 'Pior grupo 31,8%, melhor 10,6%: 3,0 vezes', 'Restringir a recomendação automática num grupo; liberar ou barrar nova versão', 'A partir de 1,5 vez o melhor grupo, a revisão humana sobe para 10%. A partir de 2 vezes, a recomendação automática é suspensa no grupo. Versão que piora algum grupo em mais de 1 ponto não sobe', 'Yuri Nakamura (Dados) apura. Head of AI Management confere. CEO decide a suspensão. CTO libera versão dentro da regra'],
    ['**2. Direito de uso da base de treino** (por fonte e contrato)', 'Com autorização expressa e parecer jurídico: 0%. Só com autorização expressa: 64,6%', 'O que entra no próximo treino; a ordem de renegociação', 'Nada sem autorização expressa e parecer entra no treino. Contrato a seis meses do vencimento sem cláusula nova dispara plano de retirada', 'Yuri Nakamura mantém o inventário. Ana Beatriz Rangel (DPO) dá o parecer. CEO decide renegociar ou retirar'],
    ['**3. Reclamações por faixa de CEP, cruzadas com o falso negativo** (CEP e idade)', 'D/E: 64% das reclamações com 25% da base, índice 2,54', 'Abrir revisão clínica dos casos e levar o grupo ao indicador 1', 'Índice a partir de 1,5 numa janela de 90 dias', 'Registro no time de sucesso do cliente, cargo [não consta]. Yuri Nakamura cruza. Head of AI Management decide a investigação'],
    ['**4. Incidentes detectados pela Lumis antes do cliente** (por tipo e grupo afetado)', '2 de 4 detectados por cliente; 1 em tratamento; 1 sem correção no material', 'Rever o monitoramento e a regra de liberação. Incidente só fecha com o material público corrigido', 'Incidente detectado pelo cliente, ou aberto há mais de 30 dias, vai ao conselho', 'Head of AI Management registra. DPO confere. CEO recebe o relato'],
    ['**5. Afirmações públicas auditáveis** (pior grupo sempre ao lado)', '0 de 5', 'O que pode ir para o material comercial', 'Afirmação que alguém de fora não consegue refazer sai antes da próxima apresentação', 'Camila Torres (Comercial) propõe. Head of AI Management aprova. Cliente ou auditor refaz o número'],
], [3.3, 2.7, 3.0, 3.8, 3.2], 'Tabela 4. Os cinco indicadores de gestão. As quatro perguntas aplicadas a cada um e aos descartados estão no Anexo. Fonte: Cap. 2, Quadros 7, 10, 11, 13, 14 e 17; contas e limites da equipe.')
P('**Amostra suficiente.** O nosso compromisso de Não Amplificação de Danos pede revisão quinzenal por grupo (C2). Com a revisão em 2%, o grupo de 60 anos ou mais de CEP D/E teria uns 64 casos por quinzena que de fato precisavam de prioridade, e a margem de erro ficaria perto de 11 pontos [hipótese: 10% dos casos precisam de prioridade]. Por isso a revisão sobe para 10% nos grupos críticos, o que dá uns 320 casos por quinzena e margem perto de 5 pontos. Nos demais grupos, a leitura quinzenal usa os últimos 90 dias.')
P('**Quem confere.** A Lumis mede o erro do próprio produto. Por isso cada indicador tem conferência de fora: o cliente que manda o desfecho recalcula o próprio grupo, como o Vila Ipê já fez, e um auditor contratado refaz o cálculo a cada trimestre [hipótese: a contratação é tema da Entrega 3]. O NIST pede que todo sistema de IA tenha responsável e mecanismo definidos para ser desligado quando sai do uso pretendido⁵.')
P('**O que descartamos.** A acurácia global esconde o falso negativo. A comparação com a versão aprovada passou a ser a regra de liberação do indicador 1. A disponibilidade de ponta a ponta é decisão técnica e não chega ao conselho. "Auditorias contratuais concluídas" mede atividade, e o indicador 2 mede registros. "Pacientes únicos analisados" é volume. A discordância do revisor humano virou a fonte de medição do indicador 1.')
P('**A decisão de agora.** Pelo limite do indicador 1, dois grupos já passam do ponto de suspensão: 60 anos ou mais de CEP D/E (3,0 vezes) e de CEP C (2,2 vezes). Mantemos o compromisso de Não Amplificação de Danos (C2), que manda suspender o uso até a correção quando há padrão de viés, e recomendamos restringir já a recomendação automática nesses dois grupos (D-023). O modelo segue rodando em paralelo, sem decidir, para medir a correção.')
B('**Custo.** Cerca de 154 mil decisões por mês, 24% do total, passam ao protocolo de triagem do próprio hospital. A revisão por amostra sobe de 12.800 para cerca de 24 mil casos por mês [hipótese: as decisões se distribuem como a base].')
B('**O que falta saber.** A carga em cada hospital e a receita afetada [não consta]. A Entrega 3 define quem executa a restrição e com que poder.')

# ---------------- 6. tese ----------------
H1('6. O que isso muda na tese')
P('A base de clientes só vira vantagem difícil de copiar com direito de uso limpo e desempenho por subgrupo que alguém de fora consiga refazer, como a Entrega 1 já apontava. Por isso, levamos ao memorando três condições prévias ao aporte: regularizar a Prisma antes de 12/2026 e o Vila Ipê antes de 03/2027, incluindo o histórico anterior aos contratos; tirar do mercado os números que não se sustentam; e medir o erro por subgrupo com conferência externa. O falso negativo por subgrupo é também a métrica pública de impacto que a Entrega 5 vai propor.')

H2('Referências')
for t in [
    '1. OBERMEYER, Z. et al. Dissecting racial bias in an algorithm used to manage the health of populations. Science, v. 366, n. 6464, p. 447-453, 2019. DOI: 10.1126/science.aax2342.',
    '2. WONG, A. et al. External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients. JAMA Internal Medicine, v. 181, n. 8, p. 1065-1070, 2021.',
    '3. BRASIL. Lei nº 13.709, de 14 de agosto de 2018 (Lei Geral de Proteção de Dados Pessoais), arts. 5º, 6º, 11 e 52. Consulta em 06/10/2026.',
    '4. ANPD. Guia Orientativo para Definições dos Agentes de Tratamento de Dados Pessoais e do Encarregado. Versão 2.0, abr. 2022.',
    '5. NIST. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1, jan. 2023 (função MANAGE 2.4).',
]:
    P(t, 'Lumis Nota')
P('Dados da Lumis: Cap. 2, Anexo A. Contas, limites e leituras são da equipe e estão marcados no texto. As empresas reais citadas são análogos e não fazem parte do caso Lumis.', 'Lumis Nota')

# ---------------- anexo ----------------
d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
H1('Anexo: detalhes da auditoria')

H2('A1. As dez variáveis do modelo')
TABELA([
    ['Variável', 'Peso', 'A empresa diz medir', 'O que tende a medir [hipótese]'],
    ['Nº de atendimentos em 24 meses', '18,4%', 'Histórico de necessidade de cuidado', 'Quem conseguiu ser atendido'],
    ['Custo acumulado de procedimentos', '15,1%', 'Gravidade do quadro clínico', 'Acesso a procedimentos pagos'],
    ['Idade do paciente', '12,7%', 'Idade', 'Idade, com fundamento clínico'],
    ['Nº de comorbidades registradas', '11,2%', 'Carga de doença', 'Doença já diagnosticada, que depende de acesso'],
    ['Tempo médio entre consulta e exame', '9,8%', 'Urgência percebida pelo médico', 'Fila e oferta da rede'],
    ['Faixa de CEP agrupada', '8,9%', 'Região de residência', 'Renda e oferta de serviços'],
    ['Tipo de plano ou cobertura', '7,4%', 'Nível de cobertura contratada', 'Renda'],
    ['Painel de exames laboratoriais', '6,9%', 'Estado clínico atual', 'Estado clínico, quando o exame foi pedido'],
    ['Nº de faltas em consultas', '5,3%', 'Adesão ao tratamento', 'Transporte, trabalho e tempo de espera'],
    ['Especialidade de origem', '4,3%', 'Via de entrada no sistema', 'Via de entrada, que depende de acesso'],
], [4.6, 1.5, 4.6, 5.3], 'Tabela A1. Fonte: Cap. 2, Quadro 8; última coluna: leitura da equipe.')
P('Os dez pesos somam 100,0%, embora o quadro fale em "dez maiores pesos". A definição técnica de peso, o sinal de cada variável e o rótulo do treino [não consta]. O peso das variáveis de acesso muda com o critério: 49,8% (atendimentos, custo, CEP e plano), 64,9% (somando tempo até o exame e faltas) ou 69,2% (somando também a especialidade) [hipótese]. Testes sugeridos para a Fase 3: trocar o rótulo do treino, retirar o bloco de variáveis de acesso e trocar só o CEP e o plano de um mesmo paciente para ver se a prioridade muda.')

H2('A2. As quatro perguntas aplicadas às afirmações do mercado')
TABELA([
    ['Afirmação', 'Medida em quê?', 'Medida por quem?', 'Muda alguma decisão?', 'Esconde qual distribuição?'],
    ['Acurácia de 94%', '48 mil registros de 2023, dois hospitais da mesma região', 'Apuração interna [hipótese]; quem apurou [não consta]', 'Não. Virou discurso comercial (Goodhart)', 'O falso negativo e os subgrupos: 17,7% em campo e 31,8% no pior grupo'],
    ['Redução de 30% na triagem', 'Seis semanas, um hospital, sem grupo de controle', '[não consta]', 'Não, sem comparação', 'Não há abertura por grupo nem por hospital'],
    ['5 milhões de vidas', 'Registros processados, com reprocessamento', 'Duplicidade achada pela auditoria interna em 01/2026', 'Não. É volume', 'Quantas pessoas únicas há [não consta]'],
    ['NPS 72', '9 respondentes', 'Escolhidos pelo time comercial', 'Não', 'As 38 contas e as 74 reclamações, 47 delas de CEP D/E'],
    ['Disponibilidade de 99,9%', 'Só a interface de programação', '[não consta]', 'Pouco. É operacional', 'O serviço de ponta a ponta e a qualidade da resposta'],
], [2.8, 3.4, 3.2, 3.0, 3.6], 'Tabela A2. Fonte: Cap. 2, Quadros 9, 11, 14 e 17; as quatro perguntas: Cap. 2, 2.3.')
P('Com 9 respostas, cada uma move o NPS em 11,1 pontos, e 72 não é um resultado possível: os vizinhos são 66,7 e 77,8. Como o 72 foi calculado [não consta]. Os 99,92% admitem cerca de 7 horas fora do ar por ano. Em 03/2025, o modelo descartou exames de um laboratório por 22 dias com a interface no ar, e quem detectou foi o cliente [fonte: Cap. 2, Quadro 14].')

H2('A3. As quatro perguntas aplicadas aos indicadores propostos')
TABELA([
    ['Indicador', 'Medida em quê?', 'Medida por quem?', 'Muda alguma decisão?', 'Esconde qual distribuição?'],
    ['1. Falso negativo por subgrupo', 'Revisão humana (10% nos grupos críticos) e desfecho informado pelo cliente', 'Pela Lumis, que tem interesse no resultado. Cliente e auditor refazem', 'Sim: restrição de grupo e liberação de versão', 'Diferenças por cliente e especialidade; grupos que o Quadro 10 não abre, como sexo'],
    ['2. Direito de uso', 'Inventário de contratos contra a base de treino', 'Pela DPO, que também responde pelo jurídico. Cliente e parecer externo conferem', 'Sim: entrada no treino e renegociação', 'A concentração (Sanare é 57,6% dos dados de clientes) e o período anterior ao contrato'],
    ['3. Reclamações por CEP', 'Registro formal de reclamações, janela de 90 dias', 'Por time ligado ao Comercial. O registro do cliente confere', 'Sim: revisão clínica e pauta do indicador 1', 'Quem não reclama. Quem tem menos acesso tende a reclamar menos [hipótese]'],
    ['4. Incidentes', 'Registro de incidentes contra as notificações dos clientes', 'Pelo Head of AI Management, que conduz os incidentes. A DPO confere', 'Sim: monitoramento e liberação', 'A gravidade e o grupo afetado; o incidente que ninguém viu'],
    ['5. Afirmações auditáveis', 'Material público contra um checklist de relato de modelos clínicos', 'Por quem não vende. Cliente ou auditor refaz o número', 'Sim: publicar ou retirar', 'Quem escolhe o recorte escolhe o grupo que aparece; os usos em seguros e bancos'],
], [2.8, 3.4, 3.4, 2.8, 3.6], 'Tabela A3. Fonte: análise da equipe sobre o Cap. 2, Quadros 7, 10, 13, 14 e 17.')

H2('A4. As quatro perguntas aplicadas aos indicadores descartados')
TABELA([
    ['Candidato', 'Medida em quê?', 'Medida por quem?', 'Muda alguma decisão?', 'Esconde qual distribuição?'],
    ['Acurácia global em campo (87,6%)', 'Base completa', '[não consta]', 'Pouco. Descartado', 'O falso negativo e os subgrupos'],
    ['Comparação com a versão aprovada (indicador 2 da v1)', 'Troca de versão', 'Pelo CTO, que também libera a versão', 'Sim, mas repete o indicador 1. Vira a regra de liberação dele', 'O mesmo que o indicador 1'],
    ['Disponibilidade de ponta a ponta (indicador 4 da v1)', 'Cadeia técnica completa', 'Pelo CTO [hipótese]', 'Decisão operacional, que não chega ao conselho. Segue como meta técnica', 'Não tem abertura útil para equidade'],
    ['Auditorias contratuais concluídas', 'Número de auditorias', 'Pela DPO [hipótese]', 'Não. Mede atividade. O indicador 2 mede registros', 'O volume de registros afetados'],
    ['Pacientes únicos analisados', 'Base sem duplicidade', 'Pela área de Dados [hipótese]', 'Não. É volume', 'Quem foi mal atendido'],
    ['Discordância do revisor humano', 'Amostra de revisão', 'Quem executa a revisão [não consta]', 'Alimenta o indicador 1 e vira a fonte dele', 'Depende do tamanho da amostra por grupo'],
], [3.4, 2.8, 3.0, 3.6, 3.2], 'Tabela A4. Fonte: análise da equipe sobre o Cap. 2, Quadros 9, 11 e 13 e a v1 do colega.')

H2('A5. Contas de conferência')
for t in [
    'Base: 5,9 mi de clientes + 14,0 mi do DATASUS + 2,1 mi sintéticos = 22,0 mi. Clientes: 1,2 + 3,4 + 0,89 + 0,41 = 5,9 mi [fonte: conta da equipe sobre o Quadro 7].',
    'Autorização frágil: (1,2 + 0,89) ÷ 5,9 = 35,4%. Autorização expressa: (3,4 + 0,41) ÷ 5,9 = 64,6%. Sanare: 3,4 ÷ 5,9 = 57,6%.',
    'O falso negativo médio, ponderado pela participação de cada grupo no Quadro 10, dá 17,65%, coerente com os 17,7% do Quadro 9. A validação de 2023 equivale a 2,5% da amostra de campo de um semestre.',
    'Reclamações: participação nas reclamações dividida pela participação na base. D/E (47 ÷ 74) ÷ 25% = 2,54; C (19 ÷ 74) ÷ 41% = 0,63; A/B (8 ÷ 74) ÷ 34% = 0,32 [fonte: conta da equipe sobre o Quadro 17].',
    'Restrição recomendada: 24% de 640 mil = cerca de 154 mil decisões por mês. Revisão: 10% de 179 mil (grupos no nível 1) + 2% de 307 mil (demais) = cerca de 24 mil por mês [hipótese: decisões distribuídas como a base].',
    'Amostra do indicador 1, com 10% dos casos precisando de prioridade [hipótese]: grupo 60+ D/E = 64 mil decisões por mês; com 2% de revisão, 1.280 revisões e 128 casos a priorizar por mês (64 por quinzena); com 10%, 640 por mês (320 por quinzena).',
]:
    B(t)

H2('A6. Divergências e o que não consta')
for t in [
    '**Divergência no Cap. 2:** "três" contratos com cláusula não relida (seção 1.2) contra "dois" (Quadro 5). Seguimos o Quadro 7.',
    '**Divergência no Cap. 2:** dados e contrato anteriores à fundação da empresa em 2022 (Quadros 3 e 7).',
    '**Divergência no Cap. 2:** a acurácia ponderada pelo Quadro 10 dá 87,2%, e o Quadro 9 mostra 87,6%. O campo tem cerca de 323 mil registros por mês, e o Quadro 12 fala em 640 mil decisões por mês.',
    '**Não consta no caso:** se as outras 34 contas fornecem dados para treino; quem consta como responsável pelos dados em cada contrato; se a Prisma é operadora de plano de saúde; se o fim do contrato obriga a retirar os dados do treino e quanto custa retreinar.',
    '**Não consta no caso:** quem apurou a validação de 2023 e a linha de campo; a proporção de casos que precisam de prioridade; o número de pessoas únicas; quem executa a revisão de 2%; quem reclamou; o desempenho por subgrupo em seguradoras e bancos; a carga de cada hospital e a receita afetada pela restrição.',
]:
    B(t)

d.save(OUT)
print('ok')
