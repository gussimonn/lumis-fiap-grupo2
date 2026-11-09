"""Fluxograma da lógica de decisão do Lumis Insight (Entrega 1 da Fase 3).

Gera, na pasta da entrega:
  - figuras/fluxograma_logica.png (usada no documento único)
  - F3-E1_Fluxograma_Logica_de_Decisao.pdf e .png (arquivo próprio pedido no item 4.2 do enunciado)
Fonte de todo o conteúdo: Cap. 3, Anexo A, Quadros A.1 a A.3 (Quadros 3 a 6 do PDF).
Cores e fontes do design system (00_Lumis/Design_System).
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

AQUI = os.path.dirname(os.path.abspath(__file__))
ENTREGA = os.path.dirname(AQUI)

PROF, VITAL, VITAL_E, PULSO = '#0F2D3A', '#3DBE93', '#1E8C6B', '#2BA6C9'
PAPEL, PAPEL_F, BORDA, NEVOA, AMBAR, TINTA = '#EEF7F3', '#F1F6F4', '#D3DEDB', '#6B7C85', '#B7791F', '#18252C'
plt.rcParams['font.family'] = 'Calibri'

W, H = 6.3, 9.0  # polegadas: 16 cm de largura, tamanho real no documento
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 100); ax.set_ylim(0, 143); ax.axis('off')


def caixa(x, y, w, h, titulo, texto, cor=PROF, fundo=PAPEL, tam=7.6):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0.4,rounding_size=1.6',
                                fc=fundo, ec=cor, lw=1.1))
    if titulo:
        ax.text(x, y + h / 2 - 2.6, titulo, ha='center', va='center', fontsize=tam + 0.6, color=cor, weight='bold')
        ax.text(x, y - 1.4, texto, ha='center', va='center', fontsize=tam, color=TINTA, linespacing=1.25)
    else:
        ax.text(x, y, texto, ha='center', va='center', fontsize=tam, color=TINTA, linespacing=1.25)


def losango(x, y, w, h, texto, tam=7.6):
    ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y), (x, y - h / 2), (x - w / 2, y)], closed=True,
                         fc='white', ec=PULSO, lw=1.3))
    ax.text(x, y, texto, ha='center', va='center', fontsize=tam, color=PROF, weight='bold', linespacing=1.2)


def seta(x1, y1, x2, y2, rot=None, lado='right'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='-|>', color=PROF, lw=0.9,
                                                                  shrinkA=0, shrinkB=0, mutation_scale=8))
    if rot and y1 == y2:  # seta horizontal: rótulo acima da linha
        ax.text((x1 + x2) / 2, y1 + 1.5, rot, fontsize=7, color=VITAL_E, weight='bold', ha='center', va='bottom')
    elif rot:
        dx = 1.2 if lado == 'right' else -1.2
        ax.text((x1 + x2) / 2 + dx, (y1 + y2) / 2, rot, fontsize=7, color=VITAL_E, weight='bold',
                ha='left' if lado == 'right' else 'right', va='center')


def etapa(y, n, quem):
    ax.text(2, y + 1.2, f'Etapa {n}', fontsize=7.2, color=VITAL_E, weight='bold', va='center')
    ax.text(2, y - 1.8, quem, fontsize=6.4, color=NEVOA, va='center', linespacing=1.1)


ax.text(50, 140, 'Como o Lumis Insight chega a uma faixa de prioridade', ha='center', va='center',
        fontsize=11.5, color=PROF, family='Georgia')
ax.text(50, 136.2, 'Caminho documentado nos Quadros A.1 a A.3 do Anexo A. Em âmbar, o que o Anexo A não informa.',
        ha='center', va='center', fontsize=7.2, color=NEVOA)

X = 46  # eixo principal
# 1 Recepção
caixa(X, 128, 40, 6.5, '', 'O cliente envia o registro do paciente\ncom até 34 campos')
etapa(128, 1, 'Integração,\ntime técnico')
seta(X, 124.6, X, 120.6)
# 2 Completude
losango(X, 116, 30, 9, 'Falta algum dos\ncampos?')
etapa(116, 2, 'Time de dados')
caixa(83, 116, 30, 15, 'Preenche por regra', 'internação ausente: zero\ncusto ausente: zero\ncomorbidade ausente: nenhuma\nexames ausentes: média da base\nplano ausente: básico', cor=AMBAR, fundo='#FBF3E6', tam=6.9)
seta(X + 15, 116, 68, 116, 'sim')
ax.plot([83, 83, X], [108.4, 104.5, 104.5], color=PROF, lw=0.9)
seta(X, 111.5, X, 103.3, 'não', lado='left')
# 3 Pontuação
caixa(X, 99, 40, 7.5, '', 'O modelo estatístico dá uma pontuação de 0 a 100\n(fórmula e pesos não constam do Anexo A)')
etapa(99, 3, 'Time de dados')
seta(X, 95.2, X, 91.4)
# 4 Regras
caixa(X, 83.5, 52, 15, 'Regras manuais: 41 ativas, 8 divulgadas',
      'Avaliadas na ordem; a primeira que se aplica encerra o bloco\nR-04 internação em 90 dias +12 · R-07 comorbidade +9\nR-11 mais de 2 faltas −7 · R-15 pronto-socorro +15\nR-19 custo no quartil superior +11 (R-23: plano básico anula)\nR-31 75 anos ou mais sem internação recente −6',
      tam=6.9)
etapa(83.5, 4, 'Time técnico')
ax.text(83.5, 83.5, '33 regras e a\ndivisão dos blocos\nnão constam', fontsize=6.6, color=AMBAR, ha='center', va='center', weight='bold')
seta(X, 76, X, 72.3)
# 5 Classificação
losango(X, 67.5, 30, 9, 'Pontuação ajustada\né 72 ou mais?')
etapa(67.5, 5, 'Definido em 2023,\nsem revisão')
caixa(83, 67.5, 18, 5.5, '', 'Alta', cor=VITAL_E, fundo=PAPEL, tam=8.4)
seta(X + 15, 67.5, 74, 67.5, 'sim')
seta(X, 63, X, 59.8, 'não', lado='left')
losango(X, 55.3, 30, 9, 'É 45 ou mais?')
caixa(83, 55.3, 18, 5.5, '', 'Média', cor=VITAL_E, fundo=PAPEL, tam=8.4)
seta(X + 15, 55.3, 74, 55.3, 'sim')
caixa(16, 55.3, 14, 5.5, '', 'Baixa', cor=VITAL_E, fundo=PAPEL, tam=8.4)
seta(X - 15, 55.3, 23, 55.3, 'não', lado='left')
# junção das faixas
ax.plot([92.4, 96.5, 96.5], [67.5, 67.5, 46], color=PROF, lw=0.9); ax.plot([92.4, 96.5], [55.3, 55.3], color=PROF, lw=0.9)
ax.plot([16, 16], [52.15, 46], color=PROF, lw=0.9); ax.plot([16, 96.5], [46, 46], color=PROF, lw=0.9)
seta(X, 46, X, 43.3)
# R-38
losango(X, 38.5, 34, 9.6, 'Conta estratégica e\ncaso limítrofe? (R-38)')
caixa(83, 38.5, 22, 8.6, '', 'Sobe uma faixa\n"limítrofe" não está\ndefinido', cor=AMBAR, fundo='#FBF3E6', tam=6.9)
seta(X + 17, 38.5, 72, 38.5, 'sim')
ax.plot([83, 83], [34.2, 30.5], color=PROF, lw=0.9); ax.plot([83, X], [30.5, 30.5], color=PROF, lw=0.9)
seta(X, 33.7, X, 27.8, 'não', lado='left')
ax.text(2, 38.5, 'Posição exata\nda R-38 na ordem\nnão consta', fontsize=6.4, color=AMBAR, va='center')
# 6 Desempate
losango(X, 23.3, 32, 9, 'Empate na mesma\npontuação e faixa?')
etapa(23.3, 6, 'Não documentado')
caixa(83, 23.3, 22, 7.5, '', 'Passa na frente o\nregistro mais antigo\n(achado no código)', cor=PROF, fundo=PAPEL_F, tam=6.9)
seta(X + 16, 23.3, 72, 23.3, 'sim')
ax.plot([83, 83], [19.55, 16], color=PROF, lw=0.9); ax.plot([83, X], [16, 16], color=PROF, lw=0.9)
seta(X, 18.8, X, 13.3, 'não', lado='left')
# 7 Entrega
caixa(X, 8.5, 52, 8.6, 'O cliente recebe a faixa e os três fatores de maior peso',
      'A pontuação não é enviada (decisão de 2023, nunca comunicada aos clientes)', cor=PROF, fundo='#E6F4F8', tam=6.9)
etapa(8.5, 7, 'Integração,\ntime técnico')
ax.text(50, 1.6, 'Fonte: Cap. 3, Anexo A, Quadros A.1, A.2 e A.3. A recomendação apoia a decisão clínica e não a substitui.',
        ha='center', fontsize=6.4, color=NEVOA)

fig.savefig(os.path.join(AQUI, 'fluxograma_logica.png'), dpi=220)
fig.savefig(os.path.join(ENTREGA, 'F3-E1_Fluxograma_Logica_de_Decisao.png'), dpi=220)
fig.savefig(os.path.join(ENTREGA, 'F3-E1_Fluxograma_Logica_de_Decisao.pdf'))
print('ok')
