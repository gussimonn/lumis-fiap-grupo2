# Design System do Lumis Insight

Padrão visual dos documentos da equipe: entregas, memorandos e anexos. Vale a partir da F2-E2. O que já foi entregue não precisa ser refeito (D-013).

O material do curso não traz logo, cores nem fontes da Lumis. Procuramos nos textos do Cap. 1 e do Cap. 2 e não encontramos nada sobre identidade visual. Tudo aqui foi criado pela equipe para o trabalho.

## A ideia

O nome Lumis vem de luz. O Lumis Insight recomenda diagnóstico, avalia crédito e classifica sinistro, e hoje responde a um hospital, a um regulador e a um investidor por causa de um viés que ninguém viu. Por isso a marca é sóbria: um azul-noite de relatório ao conselho e um único ponto de luz âmbar, que aparece onde o leitor deve olhar. O âmbar entra pouco: no logo, no filete dos títulos e na barra do destaque.

## Logo

| Arquivo | Uso |
|---|---|
| [logo/lumis-insight_horizontal.svg](logo/lumis-insight_horizontal.svg) (.png) | Capa, cabeçalho, slides |
| [logo/lumis-insight_horizontal_negativo.svg](logo/lumis-insight_horizontal_negativo.svg) (.png) | Sobre o azul-noite |
| [logo/lumis-insight_simbolo.svg](logo/lumis-insight_simbolo.svg) (.png) | Ícone, avatar, espaço pequeno |

![Logo](logo/lumis-insight_horizontal.png)

O símbolo é uma abertura: um anel azul aberto à direita e um ponto âmbar no centro. O anel é o sistema e o ponto é a recomendação. A abertura indica que a decisão sai do sistema e passa por uma pessoa, como diz o princípio-base da Declaração de Intenção [fonte: F1-E3].

Regras:
- Área de respiro em volta do logo igual ao diâmetro do ponto âmbar.
- Largura mínima de 3 cm no impresso. Abaixo disso, usar só o símbolo.
- Não mudar as cores, não girar, não aplicar sombra e não colocar sobre foto.
- "lumis" em minúsculas, Georgia. "insight" em Calibri cinza. Em texto corrido, o nome do produto continua sendo Lumis Insight, com maiúsculas.

## Cores

| Nome | Hex | Uso |
|---|---|---|
| Noite | `#1F3A5F` | Títulos, cabeçalho de tabela, logo, capa |
| Lúmen | `#E8A33D` | Ponto do logo, filete dos títulos, barra do destaque |
| Tinta | `#1B2430` | Texto corrido |
| Névoa | `#6B7A8C` | Legendas, notas, rodapé, "insight" no logo |
| Papel | `#F3F5F8` | Fundo do destaque e linhas alternadas de tabela |
| Borda | `#D5DCE4` | Linhas finas de tabela |

O Noite já era o azul usado na F2-E1 v2, e os documentos novos continuam nele.

### Marcadores de origem

Os marcadores que o CLAUDE.md exige ganham uma cor cada um, em Calibri 9 negrito, para que o leitor veja de longe o que é dado e o que é leitura nossa.

| Marcador | Cor | Estilo no Word |
|---|---|---|
| `[fonte: Cap. 2, Quadro 9]` | Verde `#2F7D6B` | Tag Fonte |
| `[hipótese]` | Âmbar escuro `#B7791F` | Tag Hipótese |
| `[não consta]` | Névoa `#6B7A8C` | Tag Não consta |
| `[risco: C2]` | Tijolo `#B4442F` | Tag Risco: ponto que tensiona um compromisso de [Compromissos_Vigentes.md](../Compromissos_Vigentes.md) |

## Tipografia

Duas famílias, ambas instaladas com o Office, então o arquivo abre igual em qualquer computador da equipe.

| Elemento | Fonte | Tamanho | Cor |
|---|---|---|---|
| Título da capa | Georgia | 28 pt | Noite |
| Subtítulo | Calibri | 13 pt | Névoa |
| Título 1 | Georgia | 16 pt, filete âmbar embaixo | Noite |
| Título 2 | Georgia | 12,5 pt | Noite |
| Título 3 | Calibri negrito | 11 pt | Noite |
| Corpo | Calibri | 11 pt, entrelinha 1,15 | Tinta |
| Destaque | Georgia itálico | 12 pt, barra âmbar à esquerda | Noite |
| Rótulo | Calibri negrito, caixa alta | 9 pt | Âmbar escuro |
| Tabela | Calibri | 9,5 pt | Tinta |
| Legenda e nota | Calibri | 9 pt | Névoa |

Georgia fica nos títulos e Calibri no texto. Fora do Office (HTML, slides no navegador), os equivalentes são Source Serif 4 e Source Sans 3, do Google Fonts.

## Artefato visual: o Feixe

![Feixe](artefato/feixe_capa.png)

Arcos concêntricos que saem do ponto de luz, em branco sobre o Noite, ficando mais fracos à medida que se afastam. Um só arco é âmbar. A leitura que propomos: uma recomendação alcança longe e perde nitidez com a distância, e o arco âmbar marca até onde a equipe consegue responder por ela.

| Arquivo | Uso |
|---|---|
| [artefato/feixe_capa.svg](artefato/feixe_capa.svg) (.png) | Faixa do topo da capa, abertura de slides |
| [artefato/linha_de_luz.svg](artefato/linha_de_luz.svg) (.png) | Divisor: filete Noite com o ponto âmbar na ponta, para separar partes de um documento longo ou de um slide |

O Feixe aparece uma vez por documento, na capa. No miolo, o que lembra o artefato é o filete âmbar sob o Título 1.

## Modelo de entrega

[Modelo_Entrega_Lumis.docx](Modelo_Entrega_Lumis.docx) já traz a capa, o cabeçalho e o rodapé, todos os estilos acima e uma página de exemplo. Para começar uma entrega:

1. Copiar o modelo para a pasta da entrega com o nome padrão (ex.: `F2-E2_Auditoria_do_Ativo_v1.docx`).
2. Trocar na capa o código da fase e da entrega, o título, o subtítulo, a equipe e a data.
3. Trocar o texto do cabeçalho (`FX-EY · Nome da entrega`), que fica em Inserir > Cabeçalho.
4. Escrever usando só os estilos da galeria. A cor e a fonte vêm do estilo, nunca de formatação manual.

Estrutura que o modelo sugere, seguindo o que a equipe adotou na F2-E1 (D-012): rótulo "Em uma frase" com a conclusão no Destaque, seções numeradas, tabelas só onde guardam números, e um fechamento que diz o que muda sem repetir a conclusão.

O modelo é gerado pelo script [_fonte/gerar_modelo.py](_fonte/gerar_modelo.py) (python-docx). Para mudar um estilo de forma permanente, editar o script e gerar de novo, guardando a versão anterior em `_Historico/`.
