# Fase 3 · O Motor 🟡

**Enunciado:** [_Enunciado/Cap03_O_Motor.pdf](_Enunciado/Cap03_O_Motor.pdf) (título do PDF: *AI in Action: Business Models, Algorithms and Ethics That Matter*) · **Dados:** Anexo A do mesmo PDF, Quadros 3 a 13 (no texto, A.1 a A.11). Transcrição do enunciado e do Anexo A feita pela equipe em 09/11/2026: [_Enunciado/Cap03_Enunciado_e_Anexo_A.md](_Enunciado/Cap03_Enunciado_e_Anexo_A.md)
**Prazo no portal:** fase aberta de 15/10/2026 a 11/11/2026; a equipe trabalha com 10/11/2026. As "quatro semanas" até a auditoria são prazo da história.

## A história
O conselho aceitou a recomendação da Fase 2, e o Vetor Capital acrescentou uma condição: antes de qualquer desembolso, uma auditoria técnica independente do Lumis Insight, feita por terceiros, com o Head of AI Management respondendo pelas conclusões. Ela começa em quatro semanas. Paulo Adjaí, o CTO, abre o sistema em uma reunião de seis horas. O que aparece é um sistema competente, cheio de decisões de negócio tomadas pelo time técnico porque não havia mais ninguém na sala para tomá-las. [fonte: Cap. 3, 1.1]

**O que a auditoria vai examinar:** lógica de decisão, escolhas de negócio embutidas, modelo de receita e economia por decisão, métricas de acompanhamento e prontidão organizacional. [fonte: Cap. 3, 1.1]

**As cinco anotações do caderno** [fonte: Cap. 3, 1.2]
1. É uma caixa que ninguém abriu: modelo estatístico mais cerca de 40 regras escritas à mão, legíveis, que ninguém fora do time técnico leu. (O Anexo A diz 41 regras ativas.)
2. O limiar de corte foi fixado em uma reunião de 2023 para a fila de um cliente e nunca foi revisto.
3. Dado faltante vira zero.
4. O preço não acompanha o custo: contrato anual fixo, custo por decisão processada.
5. A empresa inova por impulso: não há caminho definido entre a ideia e a produção.

## As oito entregas

| Código | Entrega | Quadros do Anexo A | Disciplina | Teste do enunciado |
|---|---|---|---|---|
| [F3-E1](F3-E1_Traducao_da_Logica/) | Tradução da Lógica de Decisão | A.1, A.2, A.3 | Computational Thinking | Alguém do comercial consegue explicar o sistema a um cliente sem errar? |
| [F3-E2](F3-E2_Decisoes_Escondidas/) | As Decisões de Negócio Escondidas no Sistema | A.2, A.3, A.4 | AI Governance | Um parâmetro sem dono é um risco sem responsável |
| [F3-E3](F3-E3_Modelo_de_Negocio/) | Modelo de Negócio e Economia por Decisão | A.5, A.6 | AI Strategy | Mostrar em números o risco de volume que fica com a Lumis |
| [F3-E4](F3-E4_Arvore_de_Metricas/) | Árvore de Métricas: da Estratégia à Operação | A.6, A.7 | Data-Driven Business | Se a métrica variar 20%, o que a empresa passa a fazer de diferente? |
| [F3-E5](F3-E5_Deliberacao_Etica/) | Deliberação Ética Estruturada (2 dos 3 dilemas) | A.2, A.3, A.8 | AI Governance | Deixar o custo explícito |
| [F3-E6](F3-E6_Biblioteca_de_Prompts/) | Biblioteca de Prompts para Análise de Sistemas | A.1 a A.4 | Prompt Engineering | Prompt cujo resultado ninguém sabe avaliar é risco |
| [F3-E7](F3-E7_Prontidao_e_Funil/) | Diagnóstico de Prontidão e Funil de Inovação | A.9, A.10 | Leadership & Change · AI Product & Innovation | O funil precisa saber matar projeto |
| [F3-E8](F3-E8_Nota_CTS/) | Nota de Ciência, Tecnologia e Sociedade (2 a 3 páginas) | A.3, A.8, A.11 | Formação Social e Sustentabilidade | Densidade importa mais que extensão |
| [F3-D](F3-D_Documento_Integrado/) | Documento único e peças anexas | todos | | |

[fonte: Cap. 3, seção 4 e Quadro 2]

## Formato da entrega [fonte: Cap. 3, 4.2]
- Um documento único, com identificação da equipe, reunindo as oito entregas de forma articulada.
- O fluxograma da lógica de decisão em arquivo próprio, legível e apresentável a terceiros (sai da F3-E1).
- A biblioteca de prompts em apêndice, com resultados e verificação (sai da F3-E6).
- As planilhas de margem por conta (F3-E3) e a árvore de métricas (F3-E4).
- Envio pelo portal, dentro do prazo.

Nesta fase não há memorando ao conselho.

## Critérios de avaliação [fonte: Cap. 3, 4.3]
Clareza da tradução · Identificação de decisões implícitas · Consistência econômica · Qualidade da árvore de métricas · Método na deliberação ética · Domínio de prompt avançado · Realismo do funil de inovação · Consciência sociotécnica.

## Regras do enunciado
- Não inventar informação sobre a Lumis. O que não está no Anexo A é indisponível e deve ser dito; apontar o que falta também é resultado. [fonte: Cap. 3, seção 4]
- O trabalho é traduzir e assumir a responsabilidade, sem consertar o código.
- A descrição da lógica de decisão é a peça mais consultada na Fase 7: escrever para quem vai ler sob pressão daqui a quatro fases. [fonte: Cap. 3, seção 3]

## Pontes com as fases anteriores (coerência cobrada na Fase 7)
- **F2-E2:** a regra R-19 dá pontos por custo acumulado alto, e custo mede acesso, não necessidade. É o mecanismo de proxy que a F2-E2 já apontou. A F2-E2 também decidiu restringir a recomendação automática para idosos de CEP C e D/E; a R-31 tira pontos de pacientes com 75 anos ou mais sem internação recente.
- **F2-E3:** a linha de responsabilidade por cargo serve de base para dizer, na F3-E2 e na F3-E5, a quem cada parâmetro deve caber.
- **F2-E4:** a Fase 2 já desenhou um funil e recusou o agente de triagem. No Cap. 3 ele aparece em protótipo há 7 meses (Quadro 12). A F3-E7 parte do funil da F2-E4 e precisa dizer o que acontece com essa iniciativa.
- **F2-E5 e memorando:** a métrica pública (falso negativo por grupo, trimestral) e o painel por subgrupo. O Quadro 12 mostra o painel "não iniciado".
- **Compromissos C1 a C5:** o Dilema 3 (transparência do limiar) testa o C1; o Quadro 13 e os indicadores sem recorte por grupo testam o C2; o C4 exige que cada decisão termine em um cargo. Ver [Compromissos_Vigentes](../00_Lumis/Compromissos_Vigentes.md).

## Divergências e lacunas já vistas na primeira leitura
- **Origem do agente de triagem:** o Cap. 2 lista o pedido como do comercial; o Cap. 3 (Quadro 12) diz "ideia de sócio-fundador". Vale o Cap. 3, com a divergência sinalizada (D-003).
- **CTO:** o Cap. 3 confirma Paulo Adjaí, como no Cap. 2 (o Cap. 1 citava Rafael Campos).
- **Número de regras:** "cerca de 40" no texto e 41 no Anexo A. Só 8 das 41 estão no Quadro 4; as outras 33 [não consta].
- **Teto de consumo:** o Quadro 8 não diz se o teto de 400 mil (seguradoras) e de 250 mil decisões (bancos) é anual. Se for, a Seguradora Prisma (58 mil por mês) e o Banco Meridiano (24 mil por mês) já passariam do teto [hipótese a conferir: o período do teto não consta].
- **Margem por conta:** o Quadro 9 detalha 5 contas e agrega as outras 33. A margem do quadro é receita menos custo variável (R$ 0,99 por decisão); a parte fixa do custo direto (R$ 1,44 mi menos R$ 1,039 mi por mês) não está distribuída por conta. As contas do Quadro 9 fecham.
- **Dados faltantes:** o Quadro 6 descreve 5 dos 11 campos que costumam chegar vazios; os outros 6 [não consta].

## Ordem de trabalho proposta
Guia da equipe, com contexto de cada entrega: [_Plano_de_Trabalho/F3_Guia_da_Equipe.pdf](_Plano_de_Trabalho/F3_Guia_da_Equipe.pdf) (fonte em `guia.html`). Quadro-resumo em imagem: [_Plano_de_Trabalho/F3_Plano_de_Trabalho.png](_Plano_de_Trabalho/F3_Plano_de_Trabalho.png) (fonte em `plano.html`).

0. Transcrever e conferir os Quadros 3 a 13 em um arquivo de dados único da fase (a extração do PDF sai embaralhada nas tabelas).
1. F3-E1, que é a base de tudo.
2. F3-E2, que alimenta a E5 e a E8.
3. F3-E3 e F3-E4 (a E4 usa o Quadro 9 da E3).
4. F3-E5 e F3-E8.
5. F3-E7, partindo do funil da F2-E4.
6. F3-E6 ao longo do caminho: registrar os prompts usados em cada entrega, como na Fase 2.
7. F3-D: documento único, fluxograma em arquivo próprio e planilhas.
