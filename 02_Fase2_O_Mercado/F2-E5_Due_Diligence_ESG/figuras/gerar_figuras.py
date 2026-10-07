"""Figuras da F2-E5 v1 no padrão do design system (00_Lumis/Design_System).
Figura 1: matriz de materialidade dupla (F2-E5_Materialidade_v1.md, seção 2)."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

os.chdir(os.path.dirname(os.path.abspath(__file__)))

VITAL, VITAL_ESC, PROFUNDO, PULSO = '#3DBE93', '#1E8C6B', '#0F2D3A', '#2BA6C9'
TINTA, NEVOA, BORDA, PAPEL, PAPEL_FRIO = '#18252C', '#6B7C85', '#D3DEDB', '#EEF7F3', '#F1F6F4'
plt.rcParams.update({'font.family': 'Calibri', 'font.size': 10, 'text.color': TINTA})
W = 16 / 2.54  # 16 cm, largura útil da página do modelo


def save(fig, name):
    fig.savefig(name, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def fig_materialidade():
    # (coluna = impacto no negócio, linha = impacto do negócio): 0 baixo, 1 médio, 2 alto
    temas = {
        (2, 2): ['T1 Equidade no acesso', 'T2 Privacidade e dados',
                 'T3 Transparência', 'T4 Governança da IA'],
        (2, 1): ['T5 Clima e retenção'],
        (1, 1): ['T6 Diversidade'],
        (0, 0): ['T7 Energia'],
    }
    fig, ax = plt.subplots(figsize=(W, 4.3))
    for c in range(3):
        for r in range(3):
            material = c == 2 or r == 2
            ax.add_patch(Rectangle((c, r), 1, 1, facecolor='#D4EFE6' if material else PAPEL_FRIO,  # Vital a 22% sobre branco
                                   edgecolor='white', linewidth=3))
    for (c, r), itens in temas.items():
        alto = c == 2 or r == 2
        n = len(itens)
        for i, t in enumerate(itens):
            y = r + 0.5 + (n - 1) * 0.11 - i * 0.22
            ax.add_patch(FancyBboxPatch((c + 0.06, y - 0.085), 0.88, 0.17,
                                        boxstyle='round,pad=0,rounding_size=0.04',
                                        facecolor=PROFUNDO if alto else 'white',
                                        edgecolor=PROFUNDO, linewidth=0.8))
            ax.text(c + 0.5, y, t, ha='center', va='center', fontsize=8.6,
                    color='white' if alto else PROFUNDO, fontweight='bold')
    ax.set_xlim(0, 3); ax.set_ylim(0, 3)
    ax.set_xticks([0.5, 1.5, 2.5]); ax.set_xticklabels(['Baixo', 'Médio', 'Alto'], fontsize=9)
    ax.set_yticks([0.5, 1.5, 2.5]); ax.set_yticklabels(['Baixo', 'Médio', 'Alto'], fontsize=9)
    ax.tick_params(length=0, colors=TINTA)
    ax.set_xlabel('Impacto no negócio (risco financeiro para a Lumis)', fontsize=9, color=NEVOA, labelpad=6)
    ax.set_ylabel('Impacto do negócio\n(sobre pessoas e ambiente)', fontsize=9, color=NEVOA, labelpad=6)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.text(3, 3.06, 'Fundo verde: tema material (nota Alta em pelo menos um eixo)',
            ha='right', va='bottom', fontsize=8, color=VITAL_ESC)
    save(fig, 'fig1_materialidade.png')


if __name__ == '__main__':
    fig_materialidade()
    print('ok')
