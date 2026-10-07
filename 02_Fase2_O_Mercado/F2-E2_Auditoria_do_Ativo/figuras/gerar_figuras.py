"""Figuras da F2-E2 v1 no padrão do design system (00_Lumis/Design_System).
Transposição fiel da v1 do colega: mesmos valores do gráfico original (desempenho em campo por subgrupo)."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))

VITAL, VITAL_ESC, PROFUNDO, PULSO = '#3DBE93', '#1E8C6B', '#0F2D3A', '#2BA6C9'
TINTA, NEVOA, BORDA = '#18252C', '#6B7C85', '#D3DEDB'
plt.rcParams.update({'font.family': 'Calibri', 'font.size': 10, 'text.color': TINTA,
                     'axes.edgecolor': BORDA, 'xtick.color': NEVOA, 'ytick.color': TINTA})
W = 16 / 2.54  # 16 cm, largura útil da página do modelo


def save(fig, name):
    fig.savefig(name, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def fig_subgrupo():
    dados = [('18–59 A/B', 10.6), ('18–59 C', 14.3), ('18–59 D/E', 20.2),
             ('60+ A/B', 15.9), ('60+ C', 23.5), ('60+ D/E', 31.8)]
    fig, ax = plt.subplots(figsize=(W, 2.6))
    ys = list(range(len(dados)))[::-1]
    for y, (rot, v) in zip(ys, dados):
        ax.barh(y, v, color=PROFUNDO, height=0.62)
        ax.text(v + 0.5, y, f'{v:.1f}%'.replace('.', ','), va='center', fontsize=9, color=TINTA, fontweight='bold')
    ax.set_yticks(ys); ax.set_yticklabels([d[0] for d in dados], fontsize=9)
    ax.tick_params(axis='y', length=0)
    ax.set_xlim(0, 35); ax.set_xticks([0, 5, 10, 15, 20, 25, 30, 35])
    ax.tick_params(axis='x', labelsize=8)
    ax.set_xlabel('Taxa de falso negativo (%)', fontsize=8.5, color=NEVOA)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    save(fig, 'fig1_subgrupo.png')


def fig_subgrupo_v2():
    """v2: o pior subgrupo em destaque e a média de campo como referência (Quadros 9 e 10)."""
    dados = [('18 a 59, CEP A/B', 10.6), ('18 a 59, CEP C', 14.3), ('18 a 59, CEP D/E', 20.2),
             ('60+, CEP A/B', 15.9), ('60+, CEP C', 23.5), ('60+, CEP D/E', 31.8)]
    fig, ax = plt.subplots(figsize=(W, 2.6))
    ys = list(range(len(dados)))[::-1]
    for y, (rot, v) in zip(ys, dados):
        cor = PROFUNDO if v == 31.8 else PULSO
        ax.barh(y, v, color=cor, height=0.62, zorder=2)
        ax.text(v + 0.5, y, f'{v:.1f}%'.replace('.', ','), va='center', fontsize=9, color=TINTA, fontweight='bold',
                zorder=3, bbox=dict(fc='white', ec='none', pad=1))
    ax.axvline(17.7, color=NEVOA, lw=1, ls=(0, (3, 3)), zorder=1)
    ax.text(17.9, 5.45, 'média em campo: 17,7%', fontsize=8, color=NEVOA, va='center')
    ax.set_yticks(ys); ax.set_yticklabels([d[0] for d in dados], fontsize=9)
    ax.tick_params(axis='y', length=0)
    ax.set_xlim(0, 36); ax.set_xticks([])
    for s in ('top', 'right', 'bottom'):
        ax.spines[s].set_visible(False)
    save(fig, 'fig1_subgrupo_v2.png')


if __name__ == '__main__':
    fig_subgrupo()
    fig_subgrupo_v2()
    print('ok')
