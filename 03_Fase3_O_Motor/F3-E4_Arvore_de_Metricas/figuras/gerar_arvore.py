"""Árvore de métricas da Entrega 4 (Fase 3): da hipótese de valor aos indicadores operacionais.

Gera figuras/arvore_metricas.png (documento único) e F3-E4_Arvore_de_Metricas.pdf e .png (arquivo próprio, item 4.2).
Indicadores propostos pela equipe; valores de hoje dos Quadros A.3, A.6, A.7 e A.11 do Cap. 3.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

AQUI = os.path.dirname(os.path.abspath(__file__))
ENTREGA = os.path.dirname(AQUI)
PROF, VITAL, VITAL_E, PULSO = '#0F2D3A', '#3DBE93', '#1E8C6B', '#2BA6C9'
PAPEL, NEVOA, AMBAR, TINTA = '#EEF7F3', '#6B7C85', '#B7791F', '#18252C'
plt.rcParams['font.family'] = 'Calibri'

fig = plt.figure(figsize=(6.3, 5.9))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(11, 105); ax.axis('off')


def box(x, y, w, h, txt, ec=PROF, fc='white', cor=TINTA, tam=7.2, bold=False):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0.3,rounding_size=1.2', fc=fc, ec=ec, lw=1))
    ax.text(x, y, txt, ha='center', va='center', fontsize=tam, color=cor, weight='bold' if bold else 'normal', linespacing=1.2)


def linha(x1, y1, x2, y2):
    ax.plot([x1, x1, x2, x2], [y1, (y1 + y2) / 2, (y1 + y2) / 2, y2], color=NEVOA, lw=0.8)


ax.text(50, 102, 'Árvore de métricas do Lumis Insight', ha='center', fontsize=11.5, color=PROF, family='Georgia')
ax.text(50, 98.6, 'P = progresso (deve melhorar)   ·   S = saúde (deve ficar dentro da faixa)', ha='center', fontsize=7, color=NEVOA)

box(50, 91, 70, 7.5, 'Indicador estratégico (C)\nParcela da receita vinda de contas com margem positiva e erro por grupo dentro do limite',
    ec=PROF, fc=PROF, cor='white', tam=7.4, bold=True)

ramos = [
    (11, 'Quem precisa\nrecebe prioridade'),
    (30.5, 'A origem do registro\nnão decide a fila'),
    (50, 'Erro pode ser\ncontestado e corrigido'),
    (69.5, 'O sistema\nentrega a faixa'),
    (89, 'Cada conta paga\no que consome'),
]
folhas = {
    11: [('P', 'Falso negativo por\ngrupo entre quem\nprecisava de prioridade'), ('S', 'Razão entre o pior\ne o melhor grupo\n(alerta 1,5; limite 2)')],
    30.5: [('S', 'Parcela marcada como\nalta por tipo de\nunidade (hoje 24% a 9%)'), ('S', 'Campos críticos\nvazios por origem\n(hoje 1,9 a 5,2)'), ('S', 'Casos com avaliação\nde referência por\ngrupo (amostra)')],
    50: [('S', 'Contestações\nrevistas no prazo\n(urgência e 48 h)'), ('S', 'Reclamações por\ngrupo cruzadas\ncom o erro')],
    69.5: [('S', 'Disponibilidade de\nponta a ponta, até\no sistema do cliente')],
    89: [('P', 'Margem de\ncontribuição\npor conta'), ('S', 'Custo variável\npor decisão\n(hoje R$ 0,99)')],
}
for x, t in ramos:
    linha(50, 87.2, x, 80.6)
    box(x, 77, 17.5, 7, t, ec=VITAL_E, fc=PAPEL, cor=PROF, tam=7, bold=True)
    for i, (tipo, txt) in enumerate(folhas[x]):
        y = 63 - i * 15.5
        ax.plot([x, x], [73.5 if i == 0 else y + 15.5 - 6.4, y + 6.4], color=NEVOA, lw=0.8)
        cor = VITAL_E if tipo == 'P' else PULSO
        box(x, y, 17.5, 12.2, txt, ec=cor, tam=6.6)
        ax.text(x - 8.3, y + 5.1, tipo, fontsize=6.8, color='white', weight='bold', ha='center', va='center',
                bbox=dict(boxstyle='circle,pad=0.18', fc=cor, ec='none'))

ax.text(50, 20, 'Hipótese de valor: se priorizarmos com dados suficientes, regras com dono e erro medido por grupo (A),\n'
        'os clientes atendem antes quem precisa, sem que a origem do registro decida a fila (B), o que sustenta\n'
        'contratos com margem positiva e a confiança de quem audita (C).', ha='center', va='center', fontsize=6.8,
        color=TINTA, linespacing=1.3)
ax.text(50, 13, 'Fonte: proposta da equipe; valores de hoje dos Quadros A.3, A.6 e A.11 do Cap. 3. Limites de erro: propostos na Fase 2.',
        ha='center', fontsize=6, color=NEVOA)

fig.savefig(os.path.join(AQUI, 'arvore_metricas.png'), dpi=220)
fig.savefig(os.path.join(ENTREGA, 'F3-E4_Arvore_de_Metricas.png'), dpi=220)
fig.savefig(os.path.join(ENTREGA, 'F3-E4_Arvore_de_Metricas.pdf'))
print('ok')
