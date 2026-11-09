"""Planilha de margem por conta (Entrega 3 da Fase 3): F3-E3_Margem_por_Conta.xlsx, com fórmulas.

Entradas: Cap. 3, Anexo A, Quadros A.5 e A.6 (Quadros 8 e 9 do PDF). Células azuis são entradas; as demais, fórmulas.
Cenários de preço da Sanare e tetos anuais são propostas ou hipóteses da equipe, marcadas na própria planilha.
Ao final, o script confere em Python os valores que as fórmulas devem dar.
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, 'F3-E3_Margem_por_Conta.xlsx')

PROF, VITAL_E, PAPEL, NEVOA = '0F2D3A', '1E8C6B', 'EEF7F3', '6B7C85'
CAB = Font(name='Calibri', bold=True, color='FFFFFF'); FCAB = PatternFill('solid', fgColor=PROF)
ENT = Font(name='Calibri', color='1F4E9E'); FENT = PatternFill('solid', fgColor='E8F0FB')
TIT = Font(name='Georgia', size=14, color=PROF); NOTA = Font(name='Calibri', size=9, italic=True, color=NEVOA)
BOLD = Font(name='Calibri', bold=True); BRD = Border(bottom=Side(style='thin', color='D3DEDB'))
R = '"R$" #,##0;[Red]-"R$" #,##0'; R2 = '"R$" #,##0.00'; PCT = '0.0%;[Red]-0.0%'; N = '#,##0'

wb = Workbook()


def cabecalho(ws, linha, nomes, larguras):
    for j, (n, w) in enumerate(zip(nomes, larguras), 1):
        c = ws.cell(linha, j, n); c.font = CAB; c.fill = FCAB; c.alignment = Alignment(wrap_text=True, vertical='center')
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.row_dimensions[linha].height = 32


# ---------------------------------------------------------------- Aba 1: margem por conta
ws = wb.active; ws.title = 'Margem por conta'
ws['A1'] = 'Margem de contribuição por conta'; ws['A1'].font = TIT
ws['A2'] = 'Fonte: Cap. 3, Anexo A, Quadro A.6 (Quadro 9). Azul = entrada do caso; preto = fórmula. Margem de contribuição = receita menos custo variável.'; ws['A2'].font = NOTA
ws['A4'] = 'Custo variável por decisão (R$)'; ws['B4'] = 0.99; ws['B4'].number_format = R2
ws['A5'] = 'Custo direto total por mês (R$)'; ws['B5'] = 1440000; ws['B5'].number_format = R
for c in ('B4', 'B5'):
    ws[c].font = ENT; ws[c].fill = FENT
cabecalho(ws, 7, ['Conta', 'Segmento', 'Decisões/mês', 'Receita/mês', 'Custo variável/mês', 'Margem/mês', 'Margem %',
                  'Receita por decisão', 'Volume de margem zero', 'Folga até margem zero (decisões)'],
          [24, 13, 13, 14, 16, 14, 10, 13, 15, 17])
contas = [('Rede Sanare', 'Hospitalar', 214000, 145000), ('Hospital Vila Ipê', 'Hospitalar', 96000, 98000),
          ('Hospital Aurora', 'Hospitalar', 61000, 92000), ('Seguradora Prisma', 'Seguradora', 58000, 87000),
          ('Banco Meridiano', 'Banco', 24000, 60000), ('Demais 33 contas (agregado)', 'Diversos', 597000, 2951000)]
for i, (nome, seg, vol, rec) in enumerate(contas, 8):
    ws.cell(i, 1, nome); ws.cell(i, 2, seg)
    for col, v in ((3, vol), (4, rec)):
        c = ws.cell(i, col, v); c.font = ENT; c.fill = FENT
    ws.cell(i, 5, f'=C{i}*$B$4'); ws.cell(i, 6, f'=D{i}-E{i}'); ws.cell(i, 7, f'=F{i}/D{i}')
    ws.cell(i, 8, f'=D{i}/C{i}'); ws.cell(i, 9, f'=D{i}/$B$4'); ws.cell(i, 10, f'=I{i}-C{i}')
t = 14
ws.cell(t, 1, 'Total (38 contas)').font = BOLD
for col in (3, 4, 5, 6):
    L = get_column_letter(col); ws.cell(t, col, f'=SUM({L}8:{L}13)').font = BOLD
ws.cell(t, 7, f'=F{t}/D{t}').font = BOLD; ws.cell(t, 8, f'=D{t}/C{t}').font = BOLD
for i in range(8, t + 1):
    for col, fmt in ((3, N), (4, R), (5, R), (6, R), (7, PCT), (8, R2), (9, N), (10, N)):
        ws.cell(i, col).number_format = fmt
        ws.cell(i, col).border = BRD
ws.cell(16, 1, 'Conferência com o Anexo A').font = BOLD
ws.cell(17, 1, 'Custo variável do texto do Quadro A.6 (R$ 1.039 mil)'); ws.cell(17, 5, 1039000).number_format = R
ws.cell(18, 1, 'Diferença entre a tabela e o texto'); ws.cell(18, 5, f'=E{t}-E17').number_format = R
ws.cell(19, 1, 'Custo direto que não varia com o volume (não distribuído por conta)'); ws.cell(19, 5, f'=$B$5-E{t}').number_format = R
ws.cell(20, 1, 'Margem depois de todo o custo direto (só no agregado)'); ws.cell(20, 5, f'=(D{t}-$B$5)/D{t}').number_format = PCT
ws.cell(21, 1, 'Receita anual pela tabela (receita mensal x 12)'); ws.cell(21, 5, f'=D{t}*12').number_format = R
ws.cell(22, 1, 'Receita anual pelos tickets médios do Quadro A.5 (24 x 1,18 + 9 x 1,04 + 5 x 0,72 mi)'); ws.cell(22, 5, '=24*1180000+9*1040000+5*720000').number_format = R
ws.cell(23, 1, 'Diferença (arredondamento dos tickets; causa não consta)'); ws.cell(23, 5, '=E22-E21').number_format = R
ws.cell(25, 1, 'As 33 contas agregadas não podem ser abertas sem inventar dados: o Quadro A.6 só detalha cinco contas.').font = NOTA

# ---------------------------------------------------------------- Aba 2: crescimento e sensibilidade
w2 = wb.create_sheet('Crescimento')
w2['A1'] = 'O que acontece quando a conta cresce sem mudar o preço'; w2['A1'].font = TIT
w2['A2'] = 'Contas de valor fixo: a receita não muda e o custo variável sobe R$ 0,99 por decisão a mais. Azul = entrada.'; w2['A2'].font = NOTA
cabecalho(w2, 4, ['Conta', 'Decisões/mês hoje', 'Receita/mês', 'Crescimento do volume', 'Decisões/mês depois', 'Margem/mês depois', 'Margem % depois', 'Margem anual depois'],
          [24, 15, 14, 14, 16, 16, 13, 16])
for i, linha_conta in enumerate(range(8, 13), 5):
    w2.cell(i, 1, f"='Margem por conta'!A{linha_conta}"); w2.cell(i, 2, f"='Margem por conta'!C{linha_conta}")
    w2.cell(i, 3, f"='Margem por conta'!D{linha_conta}")
    c = w2.cell(i, 4, 0.10); c.font = ENT; c.fill = FENT; c.number_format = PCT
    w2.cell(i, 5, f'=B{i}*(1+D{i})'); w2.cell(i, 6, f"=C{i}-E{i}*'Margem por conta'!$B$4"); w2.cell(i, 7, f'=F{i}/C{i}')
    w2.cell(i, 8, f'=F{i}*12')
    for col, fmt in ((2, N), (3, R), (5, N), (6, R), (7, PCT), (8, R)):
        w2.cell(i, col).number_format = fmt
w2['A11'] = 'Cada 1.000 decisões a mais numa conta de valor fixo reduzem a margem em (R$):'; w2['F11'] = "=1000*'Margem por conta'!B4"; w2['F11'].number_format = R
w2['A12'] = 'Sanare: o contrato de 2020 cobria 3 unidades; hoje são 7, e o consumo cresceu 2,9 vezes sem mudança no valor pago (Quadro A.6).'; w2['A12'].font = NOTA
w2['A14'] = 'Tetos de seguradoras e bancos [hipótese: o período do teto não consta no Quadro A.5; aqui, teto anual]'; w2['A14'].font = BOLD
cabecalho(w2, 15, ['Conta', 'Decisões/mês', 'Teto do contrato', 'Meses até o teto', '', '', '', ''], [24, 15, 14, 14, 16, 16, 13, 16])
for i, (nome, ref, teto) in enumerate((('Seguradora Prisma', 11, 400000), ('Banco Meridiano', 12, 250000)), 16):
    w2.cell(i, 1, nome); w2.cell(i, 2, f"='Margem por conta'!C{ref}").number_format = N
    c = w2.cell(i, 3, teto); c.font = ENT; c.fill = FENT; c.number_format = N
    w2.cell(i, 4, f'=C{i}/B{i}').number_format = '0.0'
w2['A19'] = 'O Quadro A.5 também não diz o que acontece quando o teto é ultrapassado (cobrança extra, bloqueio ou nada).'; w2['A19'].font = NOTA

# ---------------------------------------------------------------- Aba 3: cenários Sanare
w3 = wb.create_sheet('Cenários Sanare')
w3['A1'] = 'Rede Sanare: quatro formas de cobrar no volume de hoje'; w3['A1'].font = TIT
w3['A2'] = 'Preços, franquia e faixas são cenários da equipe para negociar, e não preço de mercado nem valor do caso. Azul = entrada.'; w3['A2'].font = NOTA
entradas = [('Decisões/mês da Sanare', "='Margem por conta'!C8", N), ('Mensalidade atual (R$)', "='Margem por conta'!D8", R),
            ('Custo variável por decisão (R$)', "='Margem por conta'!B4", R2), ('Preço por decisão no modelo 100% variável (R$)', 1.50, R2),
            ('Franquia incluída na mensalidade (decisões)', 100000, N), ('Preço do excedente (R$)', 1.50, R2),
            ('Faixas: preço de 100 mil a 200 mil decisões (R$)', 1.30, R2), ('Faixas: preço acima de 200 mil decisões (R$)', 1.50, R2)]
for i, (rot, v, fmt) in enumerate(entradas, 4):
    w3.cell(i, 1, rot); c = w3.cell(i, 2, v); c.number_format = fmt
    if not isinstance(v, str):
        c.font = ENT; c.fill = FENT
w3.column_dimensions['A'].width = 46; w3.column_dimensions['B'].width = 16
cabecalho(w3, 13, ['Modelo', 'Receita/mês', 'Custo variável/mês', 'Margem/mês', 'Margem %', 'Quem absorve o risco de volume'], [46, 16, 18, 15, 11, 44])
modelos = [
    ('A. Valor fixo, uso ilimitado (atual)', '=B5', 'Lumis, sozinha'),
    ('B. 100% por decisão', '=B4*B7', 'Cliente no volume; Lumis no custo unitário'),
    ('C. Híbrido: franquia + excedente (recomendado)', '=B5+MAX(0,B4-B8)*B9', 'Lumis até a franquia; cliente acima dela'),
    ('D. Faixas de volume', '=B5+MIN(MAX(0,B4-100000),100000)*B10+MAX(0,B4-200000)*B11', 'Dividido, em degraus'),
]
for i, (nome, rec, quem) in enumerate(modelos, 14):
    w3.cell(i, 1, nome); w3.cell(i, 2, rec).number_format = R; w3.cell(i, 3, '=$B$4*$B$6').number_format = R
    w3.cell(i, 4, f'=B{i}-C{i}').number_format = R; w3.cell(i, 5, f'=D{i}/B{i}').number_format = PCT; w3.cell(i, 6, quem)
w3['A19'] = 'Mensalidade que daria 30% de margem no volume de hoje (R$)'; w3['B19'] = '=B4*B6/0.7'; w3['B19'].number_format = R
w3['A20'] = 'Quanto a conta da Sanare subiria no modelo C (vezes a mensalidade atual)'; w3['B20'] = '=B16/B5'; w3['B20'].number_format = '0.00'
w3['A22'] = 'Nenhum modelo inclui os cerca de R$ 400,5 mil por mês de custo direto que não varia com o volume, porque o caso não diz como distribuí-lo por conta.'; w3['A22'].font = NOTA
w3['A23'] = 'Referência de preço: Hospital Aurora e Seguradora Prisma já pagam cerca de R$ 1,50 por decisão (aba Margem por conta, coluna H).'; w3['A23'].font = NOTA

wb.save(SAIDA)

# ---------------------------------------------------------------- conferência em Python dos valores esperados
cv = 0.99
esperado = {'Sanare': 145000 - 214000 * cv, 'Vila Ipê': 98000 - 96000 * cv, 'Total': 3433000 - 1050000 * cv}
assert round(esperado['Sanare']) == -66860 and round(esperado['Vila Ipê']) == 2960 and round(esperado['Total']) == 2393500
assert round(145000 / cv) == 146465 and round((3433000 - 1440000) / 3433000, 4) == 0.5805
assert 214000 * 1.5 == 321000 and 145000 + 114000 * 1.5 == 316000 and 145000 + 100000 * 1.3 + 14000 * 1.5 == 296000
assert round(214000 * cv / 0.7) == 302657 and 24 * 1180000 + 9 * 1040000 + 5 * 720000 - 3433000 * 12 == 84000
print('planilha gerada e valores conferidos:', SAIDA)
