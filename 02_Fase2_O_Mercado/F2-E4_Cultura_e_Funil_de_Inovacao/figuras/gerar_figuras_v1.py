"""Figuras da F2-E4 v1 (design system em 00_Lumis/Design_System).
Dados: Cap. 2, Anexo A (Quadros 15 e 16). Funil, escada de promessa e distribuição: proposta da equipe
(F2-E4_Levantamento_v1.md, §6 e §7)."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

os.chdir(os.path.dirname(os.path.abspath(__file__)))

VITAL, VITAL_ESC, PROFUNDO, PULSO = '#3DBE93', '#1E8C6B', '#0F2D3A', '#2BA6C9'
TINTA, NEVOA, PAPEL, PAPEL_FRIO, BORDA = '#18252C', '#6B7C85', '#EEF7F3', '#F1F6F4', '#D3DEDB'
AMBAR, AMBAR_FUNDO, TIJOLO = '#B7791F', '#FBF3E6', '#B4442F'
plt.rcParams.update({'font.family': 'Calibri', 'font.size': 9, 'text.color': TINTA})
W = 16 / 2.54  # largura útil da página


def save(fig, name):
    fig.savefig(name, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def box(ax, x, y, w, h, fc, ec=None, lw=0, r=0.012):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0,rounding_size={r}', fc=fc, ec=ec or fc, lw=lw))


def fig_clima():
    """Quadro 15: concordância por grupo nas quatro afirmações, com o eNPS."""
    afirm = ['"Prometemos ao cliente o que\no produto de fato entrega"',
             '"Temos tempo adequado de\nvalidação antes de subir"',
             '"Sei a quem escalar um\nproblema ético do produto"',
             '"Minha área é ouvida nas\ndecisões de produto"']
    grupos = [('Técnico (n=41)', [22, 17, 29, 34], PROFUNDO),
              ('Comercial (n=19)', [79, 68, 21, 63], VITAL),
              ('Demais (n=21)', [41, 38, 24, 29], '#B9C7C3')]
    fig, ax = plt.subplots(figsize=(W, 2.55))
    h = 0.24
    for g, (nome, vals, cor) in enumerate(grupos):
        ys = [i + (g - 1) * h for i in range(len(afirm))]
        ax.barh(ys, vals, height=h * 0.92, color=cor, label=nome)
        for y, v in zip(ys, vals):
            ax.text(v + 1, y, f'{v}%', va='center', fontsize=8, color=TINTA)
    ax.set_yticks(range(len(afirm)))
    ax.set_yticklabels(afirm, fontsize=8.5, color=PROFUNDO)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xticks([])
    for s in ('top', 'right', 'bottom'):
        ax.spines[s].set_visible(False)
    ax.spines['left'].set_color(BORDA)
    ax.tick_params(axis='y', length=0)
    ax.legend(loc='lower right', frameon=False, fontsize=8, ncol=1)
    ax.text(0, 3.75, 'eNPS: técnico −31 · comercial +16 · demais −4 · empresa −12', fontsize=8.5,
            color=NEVOA, va='top', transform=ax.transData)
    save(fig, 'v1_fig1_clima.png')


def fig_funil():
    """Funil em cinco etapas, com o que decide cada portão e a escada de promessa."""
    etapas = [('Entrada', 'Ficha e critérios\neliminatórios', 'CEO decide;\nHead of AI e DPO\ndão parecer', '"Em estudo"'),
              ('Descoberta', 'Até 10%\ndo esforço', 'Cliente, dados\nautorizados e resp.\ndo domínio', '"Em estudo"'),
              ('Modo sombra', 'Até mais 30%;\nnão decide nada', '4 leituras com o\npior grupo até 1,5\nvez o melhor', '"Em teste",\nsem número'),
              ('Produção\nlimitada', 'Condições da\nEntrega 5', 'Leitura sem\npiora em\nnenhum grupo', 'Erro por grupo\nmedido em campo'),
              ('Escala', 'Auditoria\nindependente', 'Indicadores\ncontínuos', 'Erro por grupo\nmedido em campo')]
    fig, ax = plt.subplots(figsize=(W, 2.85))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
    n, gap = len(etapas), 0.022
    w = (1 - gap * (n - 1)) / n
    cores = [PROFUNDO, PROFUNDO, PULSO, VITAL_ESC, VITAL_ESC]
    for i, (nome, recurso, portao, diz) in enumerate(etapas):
        x = i * (w + gap)
        box(ax, x, 0.80, w, 0.18, cores[i])
        ax.text(x + w / 2, 0.89, nome, ha='center', va='center', fontsize=9, color='white', fontweight='bold')
        ax.text(x + w / 2, 0.735, recurso, ha='center', va='center', fontsize=7.5, color=NEVOA)
        box(ax, x, 0.31, w, 0.27, PAPEL_FRIO)
        ax.text(x + w / 2, 0.445, portao, ha='center', va='center', fontsize=7.5, color=TINTA)
        box(ax, x, 0.0, w, 0.18, PAPEL, ec=VITAL, lw=0.6)
        ax.text(x + w / 2, 0.09, diz, ha='center', va='center', fontsize=7.5, color=VITAL_ESC, fontweight='bold')
        if i < n - 1:
            ax.add_patch(FancyArrowPatch((x + w + 0.002, 0.89), (x + w + gap - 0.002, 0.89),
                                         arrowstyle='-|>', mutation_scale=7, lw=1, color=NEVOA))
    ax.text(0, 0.595, 'Para avançar', fontsize=7.5, color=NEVOA, ha='left', va='bottom')
    ax.text(0, 0.195, 'O que o comercial pode dizer', fontsize=7.5, color=VITAL_ESC, ha='left', va='bottom')
    save(fig, 'v1_fig2_funil.png')


def fig_capacidade():
    """Quadro 16: backlog de 97 contra 30 de capacidade, e a distribuição proposta."""
    backlog = [('Pipeline', 18, VITAL, False), ('Explicab.', 9, VITAL, False), ('ISO', 7, VITAL, False),
               ('Crédito', 14, PULSO, False), ('México', 22, PULSO, True), ('Triagem', 11, PULSO, True),
               ('Veterinário', 16, AMBAR, True)]
    prop = [('Melhoria 23,4', 23.4, VITAL), ('', 5.6, PULSO), ('', 1.0, AMBAR)]
    fig, ax = plt.subplots(figsize=(W, 1.9))
    ax.set_xlim(0, 100); ax.set_ylim(-0.2, 2.3); ax.axis('off')
    x = 0
    for nome, v, cor, recusa in backlog:
        ax.barh(1.5, v, left=x, height=0.55, color=cor, edgecolor='white', lw=1.2,
                hatch='////' if recusa else None, alpha=0.55 if recusa else 1)
        ax.text(x + v / 2, 1.5, f'{nome}\n{v}', ha='center', va='center', fontsize=7.5,
                color=TINTA if recusa else 'white', fontweight='bold')
        x += v
    ax.text(0, 1.88, 'Backlog: 97 meses-pessoa', fontsize=8.5, color=PROFUNDO, fontweight='bold', va='bottom')
    x = 0
    for nome, v, cor in prop:
        ax.barh(0.45, v, left=x, height=0.55, color=cor, edgecolor='white', lw=1.2)
        if nome:
            ax.text(x + v / 2, 0.45, nome, ha='center', va='center', fontsize=7.5, color='white', fontweight='bold')
        x += v
    ax.text(31, 0.45, 'Adjacente 5,6', ha='left', va='center', fontsize=7.5, color=PULSO, fontweight='bold')
    ax.text(45.5, 0.45, 'Transformação 1,0', ha='left', va='center', fontsize=7.5, color=AMBAR, fontweight='bold')
    ax.text(0, 0.83, 'Capacidade do semestre: 30 meses-pessoa, distribuição proposta', fontsize=8.5,
            color=PROFUNDO, fontweight='bold', va='bottom')
    for k, (cor, txt) in enumerate(((VITAL, 'Melhoria'), (PULSO, 'Adjacente'), (AMBAR, 'Transformação'))):
        ax.add_patch(plt.Rectangle((k * 15, -0.15), 1.6, 0.22, fc=cor, ec='none'))
        ax.text(2.2 + k * 15, -0.04, txt, fontsize=7.5, va='center')
    ax.add_patch(plt.Rectangle((48, -0.15), 1.6, 0.22, fc='white', ec=NEVOA, hatch='////', lw=0.5))
    ax.text(50.2, -0.04, 'Recusado ou fora desta janela', fontsize=7.5, va='center')
    save(fig, 'v1_fig3_capacidade.png')


fig_clima()
fig_funil()
fig_capacidade()
print('ok')
