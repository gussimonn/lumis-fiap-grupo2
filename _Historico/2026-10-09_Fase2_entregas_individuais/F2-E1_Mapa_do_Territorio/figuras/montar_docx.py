"""F2-E1 v2 enxuta: parte da versão ajustada pela equipe (capa só com título e subtítulo)."""
import re, sys, docx
from docx.shared import Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE = 'C:/Users/gusta/Downloads/LumisOS/'
EQUIPE = BASE + '_Historico/2026-10-06_F2-E1_Mapa_do_Territorio_v2_ajustes-equipe.docx'
FIG = BASE + '02_Fase2_O_Mercado/F2-E1_Mapa_do_Territorio/figuras/'
OUT = sys.argv[1]

d = docx.Document(EQUIPE)
st = d.styles
body = d.element.body

# textos do apêndice, lidos da versão da equipe antes de limpar o corpo
textos = [p.text for p in d.paragraphs]
prompts = [[p.text for p in t.cell(0, 0).paragraphs] for t in d.tables if len(t.rows) == 1]
res = [t for t in textos if t.startswith('Resultado obtido')]
ver = [t for t in textos if t.startswith('Verificação:')]
mudou = next(t for t in textos if t.startswith('O que a verificação mudou'))
ver[0] = ver[0].replace('as fontes 2 a 7 das referências foram reabertas', 'as fontes externas citadas foram reabertas')

# mantém título e subtítulo da equipe; apaga o resto do corpo
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
                runs(p, txt)
                if i % 2 == 0:
                    shade(c, 'F1F6F4')
    P(legenda, 'Caption')


def CAIXA(linhas):
    tb = d.add_table(rows=1, cols=1); tb.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = tb.cell(0, 0); shade(c, 'F1F6F4')
    c.paragraphs[0].style = st['Lumis Tabela']; c.paragraphs[0].add_run(linhas[0])
    for l in linhas[1:]:
        c.add_paragraph(l, style='Lumis Tabela')
    d.add_paragraph(style='Lumis Nota')


# ---------------- corpo ----------------
P('O que faz o Lumis Insight funcionar é alugado, e o único ativo que poderia ser da Lumis, a base de dados, ainda não é dela. Por isso, a tese de crescimento precisa partir do que ainda vai ser construído.', 'Lumis Destaque')
B('**Custo:** nuvem e modelo fundacional somam 72,2% do custo direto, em dólar, e a Lumis não tem alternativa pronta a nenhum dos dois.')
B('**Controle:** a única camada da Lumis é a aplicação, e ela roda dentro do sistema do hospital.')
B('**Ativo:** a base de dados depende de contratos pendentes de revisão jurídica.')

H1('1. Onde a Lumis está')
P('A Lumis só controla a camada de cima. Nas outras três, aluga ou depende da autorização de terceiros.')
FIGURA('fig1_camadas.png', 'Figura 1. O que a Lumis controla em cada camada. Fonte: Cap. 2, Anexo A.')
B('**Nuvem:** renova em 04/2027 e a migração leva 7 meses, então a Lumis chega à renovação sem alternativa.')
B('**Modelo:** fornecedor único, sem preço garantido. O preço em queda alivia o custo, mas também barateia a entrada de concorrentes.')
B('**Dados:** mais de um terço dos dados de clientes não tem autorização clara para treinamento.')
B('**Aplicação:** é da Lumis, mas quem decide o que entra no fluxo do hospital é o dono do prontuário.')
B('**Integração e operação:** atravessam todas as camadas. A implementação e o treinamento junto ao cliente sustentam o valor percebido do produto.')
P('Para Shapiro e Varian (1999), o valor fica com quem controla o gargalo. Aqui os gargalos são a distribuição dentro do hospital e o direito de usar o dado de desfecho, e nenhum dos dois está com a Lumis.')

H1('2. Quem pode tomar esse espaço')
P('A ameaça vem de quatro direções, com pesos diferentes.')
FIGURA('fig2_ameacas.png', 'Figura 2. De onde vem a ameaça. Fonte: Cap. 2, Anexo A; peso de cada ameaça: leitura da equipe.')
TABELA([
    ['Ameaça', 'Por que preocupa', 'O que joga a favor da Lumis'],
    ['**1. Aster Health**', 'Vende a IA como módulo sobre o contrato que o hospital já tem. Para o nosso stakeholder, a pergunta passa a ser ativar o módulo do fornecedor atual ou contratar um novo. O padrão já existe no Brasil com os prontuários MV e Tasy¹.', 'A Aster não chega a seguradoras e bancos, que são 14 das 38 contas.'],
    ['**2. Grandes clientes**', 'São os que mais conseguem fazer a própria IA. O Einstein, por exemplo, já usa perto de 120 algoritmos próprios².', 'Clientes médios, sem time próprio de IA, dependem mais de um fornecedor.'],
    ['**3. Os próprios fornecedores**', 'O fornecedor de modelo anunciou um módulo próprio para saúde e passa a concorrer na aplicação. Nuvem e bases clínicas podem seguir o mesmo caminho [hipótese].', 'Nenhum deles tem hoje o fluxo clínico dentro do hospital [hipótese].'],
    ['**4. Núcleo Saúde Analytics**', 'Já tem 74 contas de BI hospitalar, quase o dobro da Lumis, e só falta a camada preditiva.', 'A Lumis já entrega a camada preditiva que falta à Núcleo.'],
    ['**5. Consultorias e integradores**', 'Vendem projetos sob medida aos clientes grandes, sobre a mesma infraestrutura e os mesmos modelos.', 'Produto pronto, com ticket médio de R$ 1,084 mi, abaixo dos R$ 1,5 a 4,0 mi de um projeto.'],
], [3.4, 7.6, 5.0], 'Tabela 1. As ameaças, da mais forte para a mais fraca. Fonte: Cap. 2, Anexo A; leitura da equipe.')
P('Distribuição não garante qualidade: o modelo de sepse da Epic, embutido no prontuário, deixou de identificar dois terços dos casos³. A Lumis, porém, ainda não pode competir por qualidade, porque os 94% de acurácia caem para 87,6% em campo, com o maior erro entre idosos de CEP D/E.')

H1('3. O que pode mudar sem a Lumis decidir')
P('Duas das cinco dependências pedem atenção agora, e as duas têm prazo.')
B('**Dados de clientes, a mais grave:** é a única dependência sem substituto. Dois clientes, o Hospital Vila Ipê e a Seguradora Prisma, respondem por 35,4% dos dados de clientes, e a autorização deles para treinamento é fraca: uma cláusula genérica e um contrato que não trata do tema. Os contratos vencem em 03/2027 e 12/2026.')
B('**O risco nos dados já existe hoje:** o modelo atual foi treinado com esses dados. Se um cliente ou o regulador questionar o uso, a Lumis pode ter de retirá-los e retreinar antes mesmo dos vencimentos. Além disso, nenhum dos seis instrumentos de dados passou por revisão jurídica, as autorizações da Sanare e do Meridiano dependem de condições (uso anonimizado e auditoria anual) e dado de saúde é sensível na LGPD, o que deixa incerta a base legal para treinar um produto vendido a terceiros [hipótese]. A auditoria completa fica para a Entrega 2.')
B('**Fornecedor de modelo, a mais rápida:** muda preço e termos com 30 dias de aviso. Se o preço dobrar, a margem bruta cai de 58% para 39,5%. Já houve queda de desempenho após uma atualização do fornecedor, em 09/2025, e há precedente de aumento: a Anthropic quadruplicou o preço de um modelo em 2024⁴.')
FIGURA('fig4_margem.png', 'Figura 3. Margem bruta em cada cenário de choque. Fonte: cálculos da equipe a partir do Cap. 2, Anexo A.')
TABELA([
    ['Dependência', 'Prazo', 'O que pode acontecer', 'Resposta recomendada'],
    ['**Dados de clientes**', 'Já hoje; contratos vencem em 12/2026 (Prisma) e 03/2027 (Vila Ipê)', 'Questionamento do uso atual obriga a retirar 35,4% dos dados de clientes e retreinar; renegociação restringe o uso; multa da LGPD de até 2% do faturamento, limitada a R$ 50 mi por infração; clientes grandes levam os dados para a Aster.', 'Revisão jurídica dos seis instrumentos; aditivos de direito de uso antes dos vencimentos; linhagem de dados para isolar os registros frágeis.'],
    ['**Modelo fundacional** (44,3% do custo)', '30 dias de aviso, a qualquer momento', 'Margem de 54,3% com preço +20% e de 39,5% com +100%; descontinuação obriga a revalidar o sistema; fornecedor vira concorrente.', 'Homologar um segundo fornecedor; travar preço e versão; avaliar modelo próprio no núcleo preditivo.'],
    ['**Câmbio** (72,2% do custo em dólar)', 'Contínuo', 'Cada R$ 0,10 a mais no dólar custa R$ 19.240 por mês; a R$ 6,50, a margem vai a 51,9%.', 'Proteção cambial e cláusula de reajuste nos contratos com clientes. Não consta se há hedge.'],
    ['**Nuvem** (27,9% do custo)', 'Renovação em 04/2027; migrar leva 7 meses', 'Renovação sem alternativa; cada 10% de reajuste custa R$ 40.176 por mês.', 'Começar já o plano de portabilidade; negociar cláusulas de saída.'],
    ['**Bases clínicas** (7,8% do custo)', 'Renovação anual automática', 'Reajuste sem teto; a renovação automática dificulta a saída.', 'Negociar teto de reajuste na renovação.'],
], [3.0, 2.8, 5.3, 4.9], 'Tabela 2. As cinco dependências, seus prazos e o que recomendamos. As respostas ainda não são praticadas pela Lumis. Fonte: Cap. 2, Anexo A; cálculos da equipe.')

H1('4. O que é difícil de copiar')
P('Partimos da leitura de que o diferencial está na combinação de produto, integração e conhecimento. Testada contra os dados, nenhuma parte dela é hoje difícil de copiar. As duas que mais valem, a base histórica e a validação clínica, estão travadas.')
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT as VA


def TABELA_NIVEIS(grupos, larguras, legenda):
    """Tabela agrupada por nível: célula do nível mesclada, cor de fundo por grupo e nota 'destrava' em itálico."""
    n = 1 + sum(len(g[3]) for g in grupos)
    tb = d.add_table(rows=n, cols=3); tb.alignment = WD_TABLE_ALIGNMENT.CENTER
    bd = OxmlElement('w:tblBorders')
    for side in ('top', 'bottom', 'insideH'):
        e = OxmlElement(f'w:{side}'); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '4'); e.set(qn('w:color'), 'D3DEDB')
        bd.append(e)
    tb._tbl.tblPr.append(bd); tb.autofit = False
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tb._tbl.tblPr.append(lay)
    for gc, w in zip(tb._tbl.tblGrid.findall(qn('w:gridCol')), larguras):
        gc.set(qn('w:w'), str(int(w * 567)))
    for r in tb.rows:
        r._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
    th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), 'true'); tb.rows[0]._tr.get_or_add_trPr().append(th)
    for j, txt in enumerate(['Hoje', 'Elemento', 'Por quê']):
        c = tb.cell(0, j); c.width = Cm(larguras[j]); p = c.paragraphs[0]; p.style = st['Lumis Tabela']
        p.paragraph_format.keep_with_next = True
        r = p.add_run(txt); r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); shade(c, '0F2D3A')
    i = 1
    for nivel, cor, fundo, itens in grupos:
        first = i
        for elemento, porque, destrava in itens:
            for j in range(3):
                c = tb.cell(i, j); c.width = Cm(larguras[j]); c.vertical_alignment = VA.CENTER
                c.paragraphs[0].style = st['Lumis Tabela']
                if fundo:
                    shade(c, fundo)
            tb.cell(i, 1).paragraphs[0].add_run(elemento).bold = True
            tb.cell(i, 2).paragraphs[0].add_run(porque)
            if destrava:
                q = tb.cell(i, 2).add_paragraph(style='Lumis Tabela')
                rr = q.add_run(destrava); rr.italic = True; rr.font.color.rgb = RGBColor.from_string('1E8C6B')
            if len(itens) > 1 and i < first + len(itens) - 1:  # mantém o grupo junto
                for cc in tb.rows[i].cells:
                    cc.paragraphs[0].paragraph_format.keep_with_next = True
            i += 1
        cel = tb.cell(first, 0)
        if i - 1 > first:
            cel = cel.merge(tb.cell(i - 1, 0))
            for extra in cel.paragraphs[1:]:
                extra._p.getparent().remove(extra._p)
        p0 = cel.paragraphs[0]; p0.style = st['Lumis Tabela']
        rn = p0.add_run(nivel); rn.bold = True; rn.font.color.rgb = RGBColor.from_string(cor)
        cel.vertical_alignment = VA.CENTER
    P(legenda, 'Caption')


TABELA_NIVEIS([
    ('Copiável', '6B7C85', None, [
        ('Modelo e tecnologia de IA', 'É de terceiro, à venda por consumo, com preço em queda.', None)]),
    ('Parcialmente difícil', '0F2D3A', 'F1F6F4', [
        ('Produto especializado', 'A Aster embute priorização no hospital, e os grandes clientes internalizam.', None),
        ('Integração e relacionamento', 'Churn de 11% ao ano; a retenção não foi testada contra a Aster.', None)]),
    ('Moderadamente difícil', '0F2D3A', None, [
        ('Conhecimento e equipe', '48 técnicos e 4 anos de domínio, que saem da empresa com as pessoas.', None)]),
    ('Valioso, mas travado', 'B7791F', 'FBF3E6', [
        ('Base histórica', 'Dados de clientes com autorização fraca e viés.', 'Destrava com contratos regularizados e viés corrigido.'),
        ('Validação clínica', 'Os 94% caem para 87,6% em campo.', 'Destrava com validação em campo por subgrupo.')]),
    ('Difícil de copiar', '1E8C6B', 'EEF7F3', [
        ('Nada hoje', 'A construir: dado de desfecho com direito de uso limpo e prova auditável de desempenho por subgrupo.', None)]),
], [3.6, 4.2, 8.2], 'Tabela 3. Cada elemento da combinação testado contra os dados, do mais fácil ao mais difícil de copiar. Fonte: Cap. 2, Anexo A; classificação da equipe.')
P('A base histórica parece o ativo mais forte, mas a maior parte dela não é exclusiva:').paragraph_format.keep_with_next = True
TABELA([
    ['Parte da base (22 mi de registros)', 'Peso', 'É exclusiva da Lumis?'],
    ['DATASUS', '63,6%', 'Não. É pública, e qualquer concorrente pode usar.'],
    ['Dados sintéticos', '9,5%', 'Não. Foram gerados internamente, e outro consegue gerar também.'],
    ['Dados de clientes', '26,8%', 'Sim. É aqui que está o valor possível, mas com as travas abaixo.'],
], [5.0, 2.0, 9.0], 'Tabela 4. Composição da base de treinamento. Fonte: Cap. 2, Quadro 7.')
P('Os dados de clientes têm quatro travas:')
B('**Autorização:** 35,4% deles têm autorização fraca, e nenhum dos seis contratos de dados passou por revisão jurídica. Um dado que talvez não possa ser usado não protege a Lumis.')
B('**Concentração:** só 2 dos 24 clientes de saúde fornecem dados, e cerca de três quartos do dado clínico de clientes vêm de um único cliente, a Rede Sanare.')
B('**Escala:** quem é dono do prontuário, como a Aster com 210 hospitais, tem acesso a muito mais dados.')
B('**Viés:** é dessa base que vem o viés identificado na Fase 1. Usada como está, ela repete os 31,8% de falso negativo em idosos de CEP D/E.')
P('Os 4 anos de operação contam na experiência da equipe, que é moderadamente difícil de copiar, mas sai da empresa com as pessoas. O que pode ter mais valor é o histórico dos dados de clientes, de 2019 a 2026, porque pode registrar a priorização clínica brasileira junto com o desfecho, algo que nenhum fornecedor de modelo tem [hipótese]. Esse histórico só vira barreira com direito de uso limpo e prova auditável de desempenho por subgrupo. Para chegar lá:')
B('**Regularizar os contratos de dados** antes de 12/2026 e 03/2027 e estender o direito de uso aos demais clientes.')
B('**Trocar os 94% por validação em campo**, por subgrupo e publicada, o que também cumpre nosso compromisso de Não Amplificação de Danos (Fase 1).')
B('**Focar em hospitais e seguradoras médios**, onde a integração vale mais e o cliente não faz a própria IA.')

H1('5. O que isso muda na tese')
P('A tese para o Vetor Capital precisa mostrar o que a Lumis vai construir para merecer 10,3 vezes o ARR. A Entrega 2 detalha contratos e métricas, e a Entrega 3 define quem responde por cada decisão sobre fornecedores.')

H2('Referências')
for t in [
    "1. MV. MV se torna a 5ª maior fornecedora global de prontuário eletrônico hospitalar (dados KLAS 2025). 4 ago. 2025. Disponível em: https://mv.com.br/imprensa/mv-se-torna-a-5a-maior-fornecedora-global-de-prontuario-eletronico-hospitalar.",
    "2. CONVERGÊNCIA DIGITAL. Hospital Israelita Albert Einstein: algoritmos, IA e inovação salvam vidas. 8 jan. 2025. Disponível em: https://convergenciadigital.com.br/mercado/hospital-israelita-albert-einstein-algoritmos-ia-e-inovacao-salvam-vidas/.",
    "3. WONG, A. et al. External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients. JAMA Internal Medicine, v. 181, n. 8, p. 1065-1070, 2021.",
    "4. TECHCRUNCH. Anthropic hikes the price of its Haiku model. 4 nov. 2024. Disponível em: https://techcrunch.com/2024/11/04/anthropic-hikes-the-price-of-its-haiku-model.",
    "SHAPIRO, C.; VARIAN, H. R. Information Rules: A Strategic Guide to the Network Economy. Boston: Harvard Business School Press, 1999.",
]:
    P(t, 'Lumis Nota')
P('Dados da Lumis: Cap. 2, Anexo A. Margens e cenários são cálculos da equipe a partir do Quadro 4. As empresas reais citadas são análogos e não fazem parte do caso Lumis.', 'Lumis Nota')

# ---------------- apêndice ----------------
d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
H1('Apêndice A: Uso de IA generativa na pesquisa e na redação')
P('**Ferramenta e data:** Claude Code (Anthropic), em 05 e 06/10/2026, com subagentes autorizados a buscar e abrir páginas na web.')
P('**Método.** A IA foi usada na pesquisa e como apoio à redação, com revisão e reescrita final da equipe. Cinco frentes de pesquisa rodaram em paralelo (camadas, concorrência, dependências, defensabilidade e cálculos), com o mesmo contexto (os Quadros 3 a 6 transcritos) e as mesmas regras:')
for t in ['não inventar números sobre a Lumis;',
          'não pesquisar as empresas fictícias e buscar, no lugar delas, análogos reais rotulados como tal;',
          'citar fonte aberta para todo fato externo;',
          'separar fato, dado do caso, cálculo e hipótese.']:
    B(t)
P('**Verificação.** Um segundo agente tentou refutar cada achado, reabrindo a fonte e refazendo as contas. Dos 85 achados, 52 foram confirmados, 32 corrigidos e 1 descartado; os não confirmados ficaram fora do texto. Seguem os dois prompts de pesquisa mais usados e o de verificação.')


def rotulo(t):
    k = t.index(':') + 1
    return '**' + t[:k] + '**' + t[k:]


H2('Prompt 1: Concorrentes diretos, indiretos e potenciais'); CAIXA(prompts[0])
P(rotulo(res[0])); P(rotulo(ver[0]))
H2('Prompt 2: Dependências críticas de fornecedores'); CAIXA(prompts[1])
P(rotulo(res[1])); P(rotulo(ver[1]))
H2('Prompt 3: Verificação adversarial (usado em todas as frentes)'); CAIXA(prompts[2])
P(rotulo(mudou))

d.save(OUT)
print('ok')
