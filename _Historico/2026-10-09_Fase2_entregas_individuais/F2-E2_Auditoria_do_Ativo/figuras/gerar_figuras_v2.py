"""Figuras da F2-E2 v2 enxuta (design system em 00_Lumis/Design_System).
Dados: Cap. 2, Anexo A (Quadros 7 a 11, 14 e 17). Respostas curtas das quatro perguntas: leitura da equipe."""
import os
import textwrap
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


def fig_base():
    """Composição da base: o que é exclusivo e o que está frágil (Quadro 7)."""
    partes = [('DATASUS', 14.0, BORDA), ('Sintéticos', 2.1, '#E4ECE9'),
              ('Sanare e Meridiano', 3.81, VITAL), ('Vila Ipê e Prisma', 2.09, AMBAR)]
    tot = sum(p[1] for p in partes)
    fig, ax = plt.subplots(figsize=(W, 1.75))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
    x, meio = 0, []
    for rot, v, cor in partes:
        w = v / tot
        ax.add_patch(plt.Rectangle((x, 0.45), w, 0.24, fc=cor, ec='white', lw=1.5))
        meio.append(x + w / 2); x += w
    ax.text(meio[0], 0.57, 'DATASUS: público, aberto a qualquer concorrente', ha='center', va='center', fontsize=8.5)
    ax.text(meio[1], 0.40, 'Sintéticos', ha='center', va='top', fontsize=8, color=NEVOA)
    for k, (cor, txt) in enumerate(((VITAL, 'Sanare e Meridiano: autorizam o treino com condição'),
                                    (AMBAR, 'Vila Ipê e Prisma: sem autorização clara; vencem em 12/2026 e 03/2027'))):
        yy = 0.30 - k * 0.15
        ax.add_patch(plt.Rectangle((0, yy - 0.045), 0.012, 0.09, fc=cor, ec='none'))
        ax.text(0.02, yy, txt, ha='left', va='center', fontsize=8.5, color=TINTA)
    x0 = (14.0 + 2.1) / tot
    ax.plot([x0, x0, 1, 1], [0.74, 0.80, 0.80, 0.74], color=PROFUNDO, lw=1.2)
    ax.text(1, 0.86, 'Só da Lumis: os dados de clientes', ha='right', va='bottom', fontsize=9,
            color=PROFUNDO, fontweight='bold')
    ax.text(0, 0.86, '22 milhões de registros', ha='left', va='bottom', fontsize=9, color=NEVOA)
    save(fig, 'v2_fig1_base.png')


def fig_proxy():
    """O que cada variável diz medir e o que mede de fato (Quadro 8)."""
    linhas = [('Nº de atendimentos', '18,4%', 'Necessidade de cuidado', 'Quem conseguiu ser atendido'),
              ('Custo acumulado', '15,1%', 'Gravidade', 'Quem teve acesso a exames e procedimentos'),
              ('Faixa de CEP', '8,9%', 'Região de residência', 'Renda e oferta de serviços perto de casa'),
              ('Tipo de plano', '7,4%', 'Cobertura contratada', 'Renda')]
    fig, ax = plt.subplots(figsize=(W, 2.3))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
    for x, t in ((0.0, 'Variável e peso no modelo'), (0.27, 'A empresa diz que mede'), (0.58, 'O que mede de fato')):
        ax.text(x, 0.99, t, fontsize=8, color=NEVOA, va='top')
    h, gap = 0.18, 0.035
    for i, (var, peso, diz, mede) in enumerate(linhas):
        top = 0.88 - i * (h + gap); yc = top - h / 2
        ax.text(0.0, yc + 0.035, var, fontsize=9, fontweight='bold', color=PROFUNDO, va='center')
        ax.text(0.0, yc - 0.045, peso, fontsize=8, color=NEVOA, va='center')
        box(ax, 0.27, top - h, 0.25, h, PAPEL_FRIO)
        ax.text(0.283, yc, diz, fontsize=8.5, va='center')
        ax.add_patch(FancyArrowPatch((0.525, yc), (0.572, yc), arrowstyle='-|>', mutation_scale=9, lw=1.3, color=AMBAR))
        box(ax, 0.58, top - h, 0.42, h, AMBAR_FUNDO)
        ax.text(0.593, yc, mede, fontsize=8.5, va='center', fontweight='bold')
    save(fig, 'v2_fig2_proxy.png')


def matriz(cab, linhas, larg, nome, col_decisao=None, alt_cab=0.075):
    """Matriz curta: uma linha por item, respostas de poucas palavras."""
    wraps = [max(8, int(w * 86)) for w in larg]  # caracteres por linha em cada coluna (Calibri 8)
    linhas_q = [[textwrap.wrap(c, int(wr * (0.92 if j in (0, col_decisao) else 1)), break_long_words=False) or [''] for j, (c, wr) in enumerate(zip(l, wraps))] for l in linhas]
    nl = [max(len(c) for c in l) for l in linhas_q]
    unid = 0.026
    alts = [n * unid + 0.014 for n in nl]
    total = alt_cab + sum(alts)
    fig, ax = plt.subplots(figsize=(W, total * 6.2))
    ax.set_xlim(0, 1); ax.set_ylim(0, total); ax.axis('off')
    xs = [sum(larg[:i]) for i in range(len(larg))]
    y = total
    ax.add_patch(plt.Rectangle((0, y - alt_cab), 1, alt_cab, fc=PROFUNDO, ec='none'))
    for x, w, c in zip(xs, larg, cab):
        ax.text(x + 0.008, y - alt_cab / 2, '\n'.join(textwrap.wrap(c, max(7, int(w * 72)), break_long_words=False)), fontsize=8,
                color='white', fontweight='bold', va='center', linespacing=1.1)
    y -= alt_cab
    for k, (l, h) in enumerate(zip(linhas_q, alts)):
        if k % 2:
            ax.add_patch(plt.Rectangle((0, y - h), 1, h, fc=PAPEL_FRIO, ec='none'))
        ax.plot([0, 1], [y - h, y - h], color=BORDA, lw=0.6)
        for j, (x, w, cel) in enumerate(zip(xs, larg, l)):
            txt = '\n'.join(cel)
            cor, peso = TINTA, 'normal'
            if j == 0:
                cor, peso = PROFUNDO, 'bold'
            if col_decisao is not None and j == col_decisao:
                cor = VITAL_ESC if txt.startswith('Sim') else AMBAR
                peso = 'bold'
            if txt.startswith('não consta'):
                cor = NEVOA
            ax.text(x + 0.008, y - 0.007, txt, fontsize=8, color=cor, fontweight=peso, va='top', linespacing=1.15)
        y -= h
    save(fig, nome)


def fig_metricas():
    cab = ['Métrica', 'Medida em quê?', 'Medida por quem?', 'Muda alguma decisão?', 'Esconde qual distribuição?', 'Destino']
    linhas = [
        ['"Acurácia de 94%"', '2 hospitais, em 2023', 'não consta', 'Não', 'O erro por grupo', 'Trocar pelo indicador 1'],
        ['"Triagem 30% mais rápida"', '1 hospital, 6 semanas, sem comparação', 'não consta', 'Não', 'Se foi o produto', 'Retirar'],
        ['"5 milhões de vidas"', 'Registros repetidos', 'Auditoria interna achou a repetição', 'Não', 'Quantas pessoas são', 'Retirar já'],
        ['"NPS 72"', '9 clientes', 'Escolhidos pelo comercial', 'Não', 'As reclamações', 'Trocar pelo indicador 3'],
        ['"Disponibilidade de 99,9%"', 'Só a interface técnica', 'não consta', 'Pouco', 'O serviço completo', 'Tirar do material comercial'],
        ['Auditorias de contrato concluídas', 'Número de auditorias', 'DPO', 'Não', 'Os registros afetados', 'Trocar pelo indicador 2'],
    ]
    matriz(cab, linhas, [0.21, 0.18, 0.16, 0.13, 0.16, 0.16], 'v2_fig4_metricas.png', col_decisao=3)


def fig_indicadores():
    cab = ['Indicador (abertura)', 'Hoje', 'Medida em quê?', 'Medida por quem?', 'Muda alguma decisão?', 'Esconde qual distribuição?']
    linhas = [
        ['1. Erro em campo por grupo (idade, CEP, cliente)', 'Pior grupo: 3 vezes o melhor', 'Revisão humana de 10% nos grupos críticos',
         'Lumis; cliente e auditor refazem', 'Sim: com o dobro do erro do melhor, suspende no grupo', 'Grupos que o caso não abre'],
        ['2. Direito de uso dos dados (por contrato)', 'Nenhum contrato com parecer', 'Contratos contra a base de treino',
         'DPO; parecer externo confere', 'Sim: sem parecer, fica fora do treino', 'A concentração na Sanare'],
        ['3. Reclamações (CEP e idade)', 'CEP D/E: 2,5 vezes o seu peso', 'Registro dos últimos 90 dias',
         'Sucesso do cliente; o cliente confere', 'Sim: com 1,5 vez o peso, revisão clínica', 'Quem não reclama'],
        ['4. Incidentes vistos antes do cliente', '2 de 4 vistos pelo cliente', 'Registro de incidentes',
         'Head of AI; a DPO confere', 'Sim: se o cliente vê antes, vai ao conselho', 'A gravidade'],
        ['5. Afirmações públicas auditáveis', '0 de 5', 'Material de divulgação',
         'Quem não vende; auditor refaz', 'Sim: o que ninguém refaz, sai', 'O grupo fora do recorte'],
    ]
    matriz(cab, linhas, [0.19, 0.14, 0.16, 0.17, 0.19, 0.15], 'v2_fig5_indicadores.png', col_decisao=4)


if __name__ == '__main__':
    fig_base(); fig_proxy(); fig_metricas(); fig_indicadores()
    print('ok')
