"""Figuras da F2-E1 v2 no padrão do design system (00_Lumis/Design_System).
Dados: Cap. 2, Anexo A (Quadros 3 a 7, 9, 10 e 14) e cálculos da equipe a partir do Quadro 4."""
import math
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

os.chdir(os.path.dirname(os.path.abspath(__file__)))

VITAL, VITAL_ESC, PROFUNDO, PULSO = '#3DBE93', '#1E8C6B', '#0F2D3A', '#2BA6C9'
TINTA, NEVOA, PAPEL, PAPEL_FRIO, BORDA = '#18252C', '#6B7C85', '#EEF7F3', '#F1F6F4', '#D3DEDB'
AMBAR, AMBAR_FUNDO = '#B7791F', '#FBF3E6'
plt.rcParams.update({'font.family': 'Calibri', 'font.size': 10, 'text.color': TINTA,
                     'axes.edgecolor': BORDA, 'xtick.color': NEVOA, 'ytick.color': TINTA})
W = 16 / 2.54  # 16 cm, largura útil da página do modelo


def save(fig, name):
    fig.savefig(name, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def box(ax, x, y, w, h, fc, ec=None, lw=0, r=0.02, ls='-'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0,rounding_size={r}',
                                fc=fc, ec=ec or fc, lw=lw, ls=ls))


def fig_camadas():
    fig, ax = plt.subplots(figsize=(W, 3.2))
    ax.set_xlim(-0.03, 1); ax.set_ylim(0, 1); ax.axis('off')
    rows = [  # de cima para baixo
        ('Aplicação', 'CONTROLA', VITAL, 'white', 'Lumis Insight, 38 contas. Roda dentro\ndo sistema hospitalar do cliente.'),
        ('Dados', 'CONDICIONADO', PAPEL, VITAL_ESC, '63,6% da base é pública. 35,4% dos dados\nde clientes sem autorização clara.'),
        ('Modelos', 'ALUGA', PAPEL_FRIO, PROFUNDO, 'Fornecedor único, aviso de 30 dias.\n44,3% do custo direto.'),
        ('Nuvem', 'ALUGA', PAPEL_FRIO, PROFUNDO, 'Renova em 04/2027; migrar leva 7 meses.\n27,9% do custo direto.'),
    ]
    h, gap, top = 0.2, 0.04, 0.96
    for i, (nome, status, fc, tc, fato) in enumerate(rows):
        y = top - (i + 1) * h - i * gap
        box(ax, 0.08, y, 0.92, h, fc, ec=VITAL if status == 'CONDICIONADO' else None, lw=1.2)
        branco = fc == VITAL
        ax.text(0.11, y + h / 2, nome, va='center', fontsize=11, fontweight='bold',
                color='white' if branco else PROFUNDO, family='Georgia')
        ax.text(0.36, y + h / 2, status, va='center', fontsize=8.5, fontweight='bold', color=tc)
        ax.text(0.57, y + h / 2, fato, va='center', fontsize=8.6,
                color='white' if branco else TINTA, linespacing=1.3)
    y0 = top - 4 * h - 3 * gap; y1 = top - 2 * h - 2 * gap
    ax.plot([0.06, 0.05, 0.05, 0.06], [y1, y1, y0, y0], color=PULSO, lw=1.6)
    ax.text(0.022, (y0 + y1) / 2, '72,2% em dólar', rotation=90, ha='center', va='center',
            fontsize=7.5, color=PULSO, fontweight='bold')
    save(fig, 'fig1_camadas.png')


def fig_ameacas():
    fig, ax = plt.subplots(figsize=(W, 4.0))
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.05, 1.05); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Circle((0, 0), 0.34, fc=PROFUNDO))
    ax.add_patch(Circle((0, 0.05), 0.09, fc=VITAL))
    ax.text(0, -0.17, 'Lumis Insight', ha='center', va='center', color='white', fontsize=9, family='Georgia')
    items = [  # texto (x, y), origem da seta, espessura, nº, título, texto, alinhamento, cor
        ((-1.55, 0.6), (-0.95, -0.15), 7.5, '1', 'Dentro do hospital',
         'Aster Health: sistema em 210 hospitais,\nIA como módulo de R$ 340 mil a mais', 'left', VITAL_ESC),
        ((1.55, 0.6), (0.95, -0.15), 5.0, '2', 'O próprio cliente',
         'Redes, operadoras e bancos\nque montam a própria IA', 'right', PULSO),
        ((0, 1.0), (0, 0.66), 3.5, '3', 'De cima',
         'Os próprios fornecedores: o de modelo já\nanunciou módulo para saúde', 'center', PULSO),
        ((0, -0.68), (0, -0.64), 1.6, '4', 'Por fora',
         'Núcleo Saúde Analytics (74 contas, sem IA preditiva)\ne consultorias com projetos sob medida', 'center', NEVOA),
    ]
    for (tx, ty), (ox, oy), lw, n, tit, txt, ha, cor in items:
        ang = math.atan2(oy, ox)
        ex, ey = 0.38 * math.cos(ang), 0.38 * math.sin(ang)
        ax.add_patch(FancyArrowPatch((ox, oy), (ex, ey), arrowstyle='-|>', mutation_scale=10 + lw * 1.5,
                                     lw=lw, color=cor))
        ax.text(tx, ty, f'{n}  {tit}', ha=ha, va='top', fontsize=10.5, fontweight='bold', color=PROFUNDO)
        ax.text(tx, ty - 0.13, txt, ha=ha, va='top', fontsize=8.6, color=TINTA, linespacing=1.3)
    save(fig, 'fig2_ameacas.png')


def fig_relogio():
    fig, ax = plt.subplots(figsize=(W, 2.5))
    m = lambda y, mo: y * 12 + mo
    start, end = m(2026, 10), m(2027, 7)
    ax.set_xlim(start - 0.3, end); ax.set_ylim(-1.6, 1.9); ax.axis('off')
    ax.plot([start, end], [0, 0], color=PROFUNDO, lw=1.5)
    meses = ['out', 'nov', 'dez', 'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul']
    for i, nome in enumerate(meses):
        x = start + i
        ax.plot([x, x], [-0.07, 0.07], color=PROFUNDO, lw=1)
        ano = ' 2026' if i == 0 else ' 2027' if nome == 'jan' else ''
        ax.text(x, -0.17, nome + ano, ha='center', va='top', fontsize=8, color=NEVOA)
    box(ax, start, -0.95, 1, 0.3, PULSO, r=0.08)
    ax.text(start + 1.15, -0.8, 'Modelo: preço e termos mudam com 30 dias de aviso, a qualquer momento',
            va='center', fontsize=8, color=PROFUNDO)
    box(ax, start, -1.45, 7, 0.3, PAPEL_FRIO, ec=NEVOA, lw=0.8, r=0.08, ls='--')
    ax.text(start + 0.15, -1.3, 'Migração de nuvem, se começasse hoje: 7 meses (termina depois da renovação)',
            va='center', fontsize=8, color=NEVOA)
    eventos = [(m(2026, 12), 'Prisma: contrato\nde dados vence', VITAL_ESC),
               (m(2027, 3), 'Vila Ipê: contrato\nde dados vence', VITAL_ESC),
               (m(2027, 4), 'Nuvem:\nrenovação', PROFUNDO)]
    for k, (x, txt, c) in enumerate(eventos):
        yt = 1.0 if k < 2 else 0.45
        ax.plot([x, x], [0, yt - 0.08], color=c, lw=1, ls=':')
        ax.scatter([x], [0], s=70, color=c, edgecolors='white', linewidths=1, zorder=3)
        ax.text(x + (0.12 if k == 2 else 0), yt, txt, ha='left' if k == 2 else 'center', va='bottom',
                fontsize=8.5, color=c, fontweight='bold', linespacing=1.2)
    save(fig, 'fig3_relogio.png')


def fig_margem():
    dados = [('Hoje', 58.0, VITAL),
             ('Dólar a R$ 6,00', 54.7, PULSO),
             ('Modelo +20%', 54.3, PULSO),
             ('Dólar a R$ 6,50', 51.9, PULSO),
             ('Modelo +100%', 39.5, PROFUNDO),
             ('Modelo +100% e dólar a R$ 6,50', 29.6, PROFUNDO)]
    fig, ax = plt.subplots(figsize=(W, 2.5))
    ys = list(range(len(dados)))[::-1]
    for y, (rot, v, c) in zip(ys, dados):
        ax.barh(y, v, color=c, height=0.62)
        ax.text(v + 0.8, y, f'{v:.1f}%'.replace('.', ','), va='center', fontsize=9, color=TINTA, fontweight='bold')
    ax.set_yticks(ys); ax.set_yticklabels([d[0] for d in dados], fontsize=9)
    ax.tick_params(axis='y', length=0)
    ax.set_xlim(0, 75); ax.set_xticks([])
    for s in ('top', 'right', 'bottom'):
        ax.spines[s].set_visible(False)
    ax.text(47, 1, 'o caixa passa a durar 8,7 meses (hoje: 11,6)', va='center', fontsize=8, color=NEVOA)
    save(fig, 'fig4_margem.png')


def fig_copiar():
    cols = ['Passivo\nhoje', 'Copiável', 'Parcial', 'Moderado', 'Difícil\nde copiar']
    linhas = [('Modelo e tecnologia de IA', 'de terceiro, à venda por consumo, preço em queda', 1),
              ('Produto especializado', 'a Aster embute priorização; grandes clientes internalizam', 2),
              ('Integração e relacionamento', 'churn de 11% ao ano; retenção não testada contra a Aster', 2),
              ('Conhecimento e equipe', '48 técnicos e 4 anos de domínio, que saem com as pessoas', 3),
              ('Base histórica de dados', '63,6% pública; 35,4% sem autorização clara', 0),
              ('Validação clínica', 'os 94% não se repetem em campo (87,6%)', 0)]
    fig, ax = plt.subplots(figsize=(W, 3.6))
    x0, dx = 0.56, 0.098
    n = len(linhas)
    ax.set_xlim(0, 1); ax.set_ylim(-0.7, n + 0.8); ax.axis('off')
    for j, c in enumerate(cols):
        x = x0 + j * dx
        if j in (0, 4):
            box(ax, x - dx / 2 + 0.004, -0.55, dx - 0.008, n + 0.1, AMBAR_FUNDO if j == 0 else PAPEL, r=0.01)
        ax.text(x, n + 0.05, c, ha='center', va='bottom', fontsize=8, color=NEVOA, linespacing=1.1)
    for i, (nome, porque, k) in enumerate(linhas):
        y = n - 1 - i
        ax.text(0.0, y + 0.13, nome, va='center', fontsize=9.5, fontweight='bold', color=PROFUNDO)
        ax.text(0.0, y - 0.23, porque, va='center', fontsize=7.6, color=NEVOA)
        ax.plot([x0 + dx, x0 + 4 * dx], [y, y], color=BORDA, lw=0.8, zorder=1)
        ax.scatter([x0 + k * dx], [y], s=90, color=AMBAR if k == 0 else PROFUNDO,
                   edgecolors='white', linewidths=1, zorder=3)
    xd = x0 + 4 * dx
    ax.text(xd, 2.35, 'vazio\nhoje', ha='center', va='center', fontsize=8, color=VITAL_ESC, style='italic')
    ax.text(xd, 1.6, 'a construir:\ndado de\ndesfecho e\nprova por\nsubgrupo', ha='center', va='top',
            fontsize=7.2, color=VITAL_ESC, linespacing=1.15)
    save(fig, 'fig5_copiar.png')


def fig_copiar_simples():
    """Versão simples da Figura 5: três faixas, no mesmo desenho da Figura 1."""
    fig, ax = plt.subplots(figsize=(W, 2.9))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
    rows = [  # de cima para baixo: (faixa, fundo, borda, cor do título, itens)
        ('Difícil de copiar', 'white', VITAL, VITAL_ESC,
         'Nada hoje. A construir: dado de desfecho com direito de uso\nlimpo e prova auditável de desempenho por subgrupo.'),
        ('Copiável ou\nparcialmente difícil', PAPEL_FRIO, None, PROFUNDO,
         'Modelo e tecnologia de IA · Produto especializado\nIntegração e relacionamento · Conhecimento e equipe'),
        ('Valioso, mas\ntravado hoje', AMBAR_FUNDO, None, AMBAR,
         'Base histórica (dados de clientes com autorização fraca e viés)\nValidação clínica (os 94% caem para 87,6% em campo)'),
    ]
    h, gap, top = 0.29, 0.04, 0.98
    for i, (nome, fc, ec, tc, itens) in enumerate(rows):
        y = top - (i + 1) * h - i * gap
        box(ax, 0.0, y, 1.0, h, fc, ec=ec, lw=1.4 if ec else 0, ls='--' if ec else '-')
        ax.text(0.03, y + h / 2, nome, va='center', fontsize=10, fontweight='bold', color=tc,
                family='Georgia', linespacing=1.15)
        dy = 0.035 if i == 2 else 0
        ax.text(0.37, y + h / 2 + dy, itens, va='center', fontsize=8.8, color=TINTA, linespacing=1.35)
        if i == 2:
            ax.text(0.37, y + 0.045, 'Destrava com contratos regularizados e desempenho corrigido',
                    va='center', fontsize=8.4, color=VITAL_ESC, style='italic')
    save(fig, 'fig5_copiar_simples.png')


if __name__ == '__main__':
    fig_camadas(); fig_ameacas(); fig_relogio(); fig_margem(); fig_copiar(); fig_copiar_simples()
    print('ok')
