# Design System do Lumis Insight

Padrão visual dos documentos da equipe: entregas, memorandos e anexos. Vale a partir da F2-E2. O que já foi entregue não precisa ser refeito (D-013, cores revistas em D-014).

O material do curso não traz logo, cores nem fontes da Lumis. Procuramos nos textos do Cap. 1 e do Cap. 2 e não encontramos nada sobre identidade visual. Tudo aqui foi criado pela equipe para o trabalho.

## A ideia

O Lumis Insight trabalha onde saúde e dados se encontram: recomenda diagnóstico, prioriza atendimento e aprende com o uso [fonte: Cap. 1, Dossiê]. A identidade junta três vozes. O verde Vital é a saúde e fica com o ponto central do logo. O Profundo, um azul-petróleo escuro, é o dado e dá a base séria de relatório ao conselho. O Pulso, um ciano, é a inovação e aparece onde o sinal vira dado. O verde se inspira no tom de saúde usado pela Arkium, mas a Lumis tem paleta própria, e os dois tons não são iguais.

## Logo

| Arquivo | Uso |
|---|---|
| [logo/lumis-insight_horizontal.svg](logo/lumis-insight_horizontal.svg) (.png) | Capa, cabeçalho, slides |
| [logo/lumis-insight_horizontal_negativo.svg](logo/lumis-insight_horizontal_negativo.svg) (.png) | Sobre o Profundo |
| [logo/lumis-insight_simbolo.svg](logo/lumis-insight_simbolo.svg) (.png) | Ícone, avatar, espaço pequeno |

![Logo](logo/lumis-insight_horizontal.png)

O símbolo é uma abertura: um anel Profundo aberto à direita, o ponto Vital no centro e um ponto Pulso menor saindo pela abertura. O anel é o sistema, o ponto verde é o paciente e o ponto ciano é a recomendação que sai. Ela sai do sistema e passa por uma pessoa antes de virar decisão, como diz o princípio-base da Declaração de Intenção [fonte: F1-E3].

Regras:
- Área de respiro em volta do logo igual ao diâmetro do ponto verde.
- Largura mínima de 3 cm no impresso. Abaixo disso, usar só o símbolo.
- Não mudar as cores, não girar, não aplicar sombra e não colocar sobre foto.
- "lumis" em minúsculas, Georgia, cor Profundo. "insight" em Calibri, Vital escuro. Em texto corrido, o nome do produto continua sendo Lumis Insight, com maiúsculas.

## Cores

| Nome | Hex | Voz | Uso |
|---|---|---|---|
| Vital | `#3DBE93` | Saúde | Ponto do logo, filete dos títulos, barra do destaque, linha de pulso |
| Vital escuro | `#1E8C6B` | Saúde | Rótulos e "insight" no logo; é o verde que tem contraste para texto |
| Profundo | `#0F2D3A` | Dados | Títulos, anel do logo, cabeçalho de tabela, fundo da capa |
| Pulso | `#2BA6C9` | Inovação | Ponto de dado do logo, pontos do Feixe, ponta do degradê |
| Tinta | `#18252C` | | Texto corrido |
| Névoa | `#6B7C85` | | Legendas, notas, rodapé |
| Papel | `#EEF7F3` | | Fundo do destaque |
| Papel frio | `#F1F6F4` | | Linhas alternadas de tabela |
| Borda | `#D3DEDB` | | Linhas finas de tabela |

O degradê Vital → Pulso (`#3DBE93` → `#2BA6C9`) marca a passagem de saúde para dado. Ele aparece só em elementos gráficos (um arco do Feixe e a linha de luz), nunca em texto.

### Marcadores de origem

Os marcadores que o CLAUDE.md exige ganham uma cor cada um, em Calibri 9 negrito, para que o leitor veja de longe o que é dado e o que é leitura nossa.

| Marcador | Cor | Estilo no Word |
|---|---|---|
| `[fonte: Cap. 2, Quadro 9]` | Vital escuro `#1E8C6B` | Tag Fonte |
| `[hipótese]` | Âmbar escuro `#B7791F` | Tag Hipótese |
| `[não consta]` | Névoa `#6B7A8C` | Tag Não consta |
| `[risco: C2]` | Tijolo `#B4442F` | Tag Risco: ponto que tensiona um compromisso de [Compromissos_Vigentes.md](../Compromissos_Vigentes.md) |

## Tipografia

Duas famílias, ambas instaladas com o Office, então o arquivo abre igual em qualquer computador da equipe.

| Elemento | Fonte | Tamanho | Cor |
|---|---|---|---|
| Título da capa | Georgia | 28 pt | Profundo |
| Subtítulo | Calibri | 13 pt | Névoa |
| Título 1 | Georgia | 16 pt, filete Vital embaixo | Profundo |
| Título 2 | Georgia | 12,5 pt | Profundo |
| Título 3 | Calibri negrito | 11 pt | Profundo |
| Corpo | Calibri | 11 pt, entrelinha 1,15 | Tinta |
| Destaque | Georgia itálico | 12 pt, barra Vital à esquerda | Profundo |
| Rótulo | Calibri negrito, caixa alta | 9 pt | Vital escuro |
| Tabela | Calibri | 9,5 pt | Tinta |
| Legenda e nota | Calibri | 9 pt | Névoa |

Georgia fica nos títulos e Calibri no texto. Fora do Office (HTML, slides no navegador), os equivalentes são Source Serif 4 e Source Sans 3, do Google Fonts.

## Artefato visual: o Feixe

![Feixe](artefato/feixe_capa.png)

Sobre o fundo Profundo, arcos concêntricos de sinal saem do ponto Vital. Do mesmo ponto sai uma linha de pulso, como num monitor cardíaco. Depois do batimento, a linha se desfaz em pontos que passam do verde ao ciano e ganham variação: o sinal do paciente vira dado. Um único arco leva o degradê Vital → Pulso. A leitura que propomos é a conversa entre saúde, dados e inovação que dá nome ao produto.

| Arquivo | Uso |
|---|---|
| [artefato/feixe_capa.svg](artefato/feixe_capa.svg) (.png) | Faixa do topo da capa, abertura de slides |
| [artefato/linha_de_luz.svg](artefato/linha_de_luz.svg) (.png) | Divisor: filete Profundo com o ponto Vital e um trecho em degradê, para separar partes de um documento longo ou de um slide |

O Feixe aparece uma vez por documento, na capa. No miolo, o que lembra o artefato é o filete verde sob o Título 1.

## Modelo de entrega

[Modelo_Entrega_Lumis.docx](Modelo_Entrega_Lumis.docx) já traz a capa, o cabeçalho e o rodapé, todos os estilos acima e uma página de exemplo. Para começar uma entrega:

1. Copiar o modelo para a pasta da entrega com o nome padrão (ex.: `F2-E2_Auditoria_do_Ativo_v1.docx`).
2. Trocar na capa o código da fase e da entrega, o título, o subtítulo, a equipe e a data.
3. Trocar o texto do cabeçalho (`FX-EY · Nome da entrega`), que fica em Inserir > Cabeçalho.
4. Escrever usando só os estilos da galeria. A cor e a fonte vêm do estilo, nunca de formatação manual.

Estrutura que o modelo sugere, seguindo o que a equipe adotou na F2-E1 (D-012): rótulo "Em uma frase" com a conclusão no Destaque, seções numeradas, tabelas só onde guardam números, e um fechamento que diz o que muda sem repetir a conclusão.

O modelo é gerado pelo script [_fonte/gerar_modelo.py](_fonte/gerar_modelo.py) (python-docx). Para mudar um estilo de forma permanente, editar o script e gerar de novo, guardando a versão anterior em `_Historico/`.
