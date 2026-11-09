"""Confere, por conta independente, os casos de teste da execução do P3 e gera F3-E6_Testes_Sinteticos.csv.

Implementa só o que os Quadros A.1 a A.3 do Cap. 3 dizem: cortes 45 e 72, as oito regras divulgadas,
o preenchimento de campos ausentes e o desempate. Cada caso roda com uma única regra visível disparando
(as 33 regras não divulgadas e a divisão dos blocos não constam). Casos que o anexo não permite decidir
ficam marcados como INDETERMINÁVEL e não são calculados.
Uso: python verificar_testes.py   (gera o CSV na mesma pasta e imprime o resultado da conferência)
"""
import csv, os, sys
sys.stdout.reconfigure(encoding="utf-8")

AQUI = os.path.dirname(os.path.abspath(__file__))


def faixa(p):
    return 'Alta' if p >= 72 else ('Média' if p >= 45 else 'Baixa')


def ajustar(p0, internacao_dias=None, historico_vazio=False, comorbidade=False, comorbidade_vazia=False, faltas=0,
            ps=False, custo_q4=False, custo_vazio=False, plano_basico=False, plano_vazio=False, idade=50.5):
    """Pontuação ajustada pelas regras divulgadas, com uma regra disparando por vez."""
    if historico_vazio:      # A.3: assume zero internações
        internacao_dias = None
    if comorbidade_vazia:    # A.3: assume nenhuma
        comorbidade = False
    if custo_vazio:          # A.3: assume zero, logo fora do quartil superior
        custo_q4 = False
    if plano_vazio:          # A.3: assume categoria básica
        plano_basico = True
    p = p0
    if internacao_dias is not None and internacao_dias <= 90: p += 12      # R-04
    if comorbidade: p += 9                                                   # R-07
    if faltas > 2: p -= 7                                                    # R-11
    if ps: p += 15                                                           # R-15
    if custo_q4 and not plano_basico: p += 11                                # R-19, anulada pela R-23
    if idade >= 75 and internacao_dias is None: p -= 6                       # R-31 (sem nenhuma internação)
    return p


CASOS = [
    # id, descrição, kwargs (None = indeterminável), saída esperada pela execução do P3
    ('C01', 'Pontuação 44', dict(p0=44), 'Baixa'),
    ('C02', 'Pontuação 45', dict(p0=45), 'Média'),
    ('C03', 'Pontuação 71', dict(p0=71), 'Média'),
    ('C04', 'Pontuação 72', dict(p0=72), 'Alta'),
    ('C05', 'Pontuação 71,6 ou 44,6', None, 'INDETERMINÁVEL: arredondamento não consta'),
    ('C06', 'Pontuação 78, 2 faltas', dict(p0=78, faltas=2), 'Alta'),
    ('C07', 'Pontuação 78, 3 faltas', dict(p0=78, faltas=3), 'Média'),
    ('C08', 'Pontuação 50, 74 anos, sem internação', dict(p0=50, idade=74.5), 'Média'),
    ('C09', 'Pontuação 50, 75 anos, sem internação', dict(p0=50, idade=75.5), 'Baixa'),
    ('C10', 'Pontuação 60, internação há 89 dias', dict(p0=60, internacao_dias=89), 'Alta'),
    ('C11', 'Pontuação 60, internação há 91 dias', dict(p0=60, internacao_dias=91), 'Média'),
    ('C12', '75 anos, internação há 91 dias', None, 'INDETERMINÁVEL: "internação recente" não definida'),
    ('C13', 'Pontuação 50, 78 anos, histórico vazio', dict(p0=50, idade=78.5, historico_vazio=True), 'Baixa'),
    ('C14', 'Pontuação 62, custo vazio', dict(p0=62, custo_vazio=True), 'Média'),
    ('C14c', 'Controle: pontuação 62, custo no quartil superior', dict(p0=62, custo_q4=True), 'Alta'),
    ('C15', 'Pontuação 66, comorbidade vazia', dict(p0=66, comorbidade_vazia=True), 'Média'),
    ('C15c', 'Controle: pontuação 66, comorbidade registrada', dict(p0=66, comorbidade=True), 'Alta'),
    ('C16', 'Custo no quartil superior e plano básico informado', None, 'INDETERMINÁVEL: divisão dos blocos não consta'),
    ('C17', 'Pontuação 62, custo no quartil superior, plano vazio', dict(p0=62, custo_q4=True, plano_vazio=True), 'Média'),
    ('C18', 'Pontuação 62, plano básico, custo fora do quartil', dict(p0=62, plano_basico=True), 'Média'),
    ('C19', 'Pontuação 71, conta estratégica', None, 'INDETERMINÁVEL: "limítrofe" não definido'),
    ('C20', 'Pontuação 44, conta estratégica', None, 'INDETERMINÁVEL: "limítrofe" não definido'),
    ('C21', 'Pontuação 90, conta estratégica', dict(p0=90), 'Alta'),
    ('C22', 'Empate em 60: A entrou antes de B', None, 'A antes de B'),
    ('C23', 'Empate com a mesma data e hora', None, 'INDETERMINÁVEL: critério após a data não consta'),
    ('C24', 'R-38 com desempate', None, 'INDETERMINÁVEL: "limítrofe" não definido'),
]

linhas, falhas = [], 0
for cid, desc, kw, esperado in CASOS:
    if kw is None:
        obtido, status = esperado, 'não calculado'
    else:
        p = ajustar(**kw)
        obtido = faixa(p)
        status = 'confere' if obtido == esperado else 'DIVERGE'
        falhas += status == 'DIVERGE'
        obtido = f'{p} → {obtido}'
    linhas.append([cid, desc, esperado, obtido, status])
# desempate (C22): ordena por data de entrada, a mais antiga primeiro
fila = sorted([('B', '2026-03-02 09:00'), ('A', '2026-03-01 09:00')], key=lambda x: x[1])
assert [x[0] for x in fila] == ['A', 'B']

with open(os.path.join(AQUI, 'F3-E6_Testes_Sinteticos.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['Caso', 'Dados sintéticos', 'Saída esperada (execução do P3)', 'Conta independente', 'Resultado'])
    w.writerows(linhas)
print(f'{len(linhas)} casos; divergências: {falhas}; desempate confere')
for l in linhas:
    print(' | '.join(l))
