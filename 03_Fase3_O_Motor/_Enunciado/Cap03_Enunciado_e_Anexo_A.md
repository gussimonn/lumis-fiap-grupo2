# Fase 3 — O Motor: enunciado e Anexo A (transcrição do portal)

> Transcrito do Cap. 1 da Fase 3 ("AI in Action: Business Models, Algorithms and Ethics That Matter") no portal FIAP, em 09/11/2026, por Felipe Alef. Fase aberta de 15/10/2026 a 11/11/2026 no portal.
> Use `[fonte: Cap. 3, Quadro N]` para citar. A numeração "Quadro N" é a do capítulo; "A.x" é a seção do Anexo A.

## Contexto da história

- O conselho aceitou a recomendação da Fase 2. O Vetor Capital manteve a proposta, reduziu o prazo e exige, antes de qualquer desembolso, uma **auditoria técnica independente** do Lumis Insight, feita por terceiros, com "você" respondendo pelas conclusões. Começa em **4 semanas**.
- Paulo Adjaí (CTO) abriu o sistema. Diagnóstico: sistema competente, com decisões de negócio tomadas pelo time técnico "por ausência de interlocutor".
- Escopo da auditoria: (1) lógica de decisão em linguagem de gestor; (2) escolhas de negócio embutidas (quem decidiu, justificativa, autoridade); (3) modelo de receita e economia unitária; (4) métricas de acompanhamento; (5) prontidão organizacional.
- Cinco anotações da sala do Paulo:
  1. Não é caixa-preta, é caixa que ninguém abriu: modelo estatístico + ~40 regras escritas à mão, legíveis, nunca lidas fora do time técnico.
  2. O limiar de corte foi definido em reunião de 2023 e nunca revisto (equilibrar a fila de um cliente).
  3. Dado faltante vira zero.
  4. O preço não acompanha o custo (contrato anual fixo × custo por decisão).
  5. A empresa inova por impulso, não por método.

## Conceitos do capítulo (resumo)

- **Algoritmo** = sequência de passos de entrada a saída; a competência do gestor é exigir que a lógica seja explicitada. Decisões de negócio se escondem em **limiar** (troca entre falso positivo e falso negativo), **dado faltante** (zero, média, recusa ou revisão humana) e **desempate**.
- **Modelos de negócio em IA:** custo marginal não é zero; valor fixo com uso ilimitado vira prejuízo quando o cliente cresce. Modelos: por assento, por volume, fixo com teto, por resultado, híbrido. Cada um põe o risco de volume de um lado.
- **Métricas:** hipótese de valor "se A, então B, o que produz C"; cada elo sugere um indicador; "se ele se mover, o que muda na conduta?". Medir qualidade da decisão, não volume. Separar métricas de saúde (faixa) e de progresso (crescer).
- **Ética aplicada (método em 4 passos):** afetados (inclusive quem não está na sala) → valores legítimos em conflito → alternativas além das duas óbvias → decidir e registrar a justificativa.
- **Prompt avançado:** decomposição em etapas, exemplos (few-shot), papel/restrições/critério de sucesso, pedir o caminho do raciocínio; verificação: perguntar de formas diferentes, pedir contra-argumento, exigir o que não pode ser afirmado.
- **Prontidão:** (a) onde se documenta o que se aprende; (b) caminho ideia → experimento → decisão; (c) tolerância ao questionamento. A Lumis falha nas três.
- **Inovação:** hipótese testável, critério de resposta definido antes, investimento limitado; **critério de encerramento** antes de começar.
- **CTS:** nenhuma tecnologia é neutra; perguntar para quem funciona melhor, quem foi consultado, que alternativas foram descartadas.
- Lembrete: a descrição da lógica de decisão é "a peça mais consultada da Fase 7".

## Missão: as 8 entregas

Regra geral: não inventar dados; o que não está no Anexo A é indisponível e deve ser dito.

**E1 — Tradução da Lógica de Decisão** (Quadros A.1, A.2, A.3)
- Caminho completo entrada → saída em etapas numeradas; regras de cada etapa e ordem; limiares e o que muda acima/abaixo; **fluxograma**; **dois exemplos completos** (um alta, um baixa), com o motivo em cada etapa.
- Teste: alguém do comercial consegue explicar o sistema a um cliente sem errar?

**E2 — Decisões de Negócio Escondidas** (A.2, A.3, A.4)
- Parâmetros que são decisão de negócio; para cada um: quem decidiu, quando, justificativa, autoridade; efeito sobre grupos; a quem deve caber e periodicidade de revisão; o parâmetro mais urgente, com justificativa.

**E3 — Modelo de Negócio e Economia por Decisão** (A.5, A.6)
- Receita × custo lado a lado; margem por conta pelo volume efetivo; contas que pioram ao crescer, com números; ≥3 modelos alternativos e quem absorve o risco de volume; recomendação com transição dos contratos existentes.

**E4 — Árvore de Métricas** (A.6, A.7)
- Hipótese "se A, B, o que produz C"; árvore do estratégico ao operacional; progresso × saúde; indicadores atuais sem hipótese (manter/descartar); ≥1 indicador de qualidade da decisão; quem revisa e com que frequência. Para cada métrica: "se variar 20%, o que a empresa faz de diferente?".

**E5 — Deliberação Ética Estruturada** (A.2, A.3, A.8) — escolher 2 dos 3 dilemas
- Todos os afetados; valores legítimos em conflito; ≥4 alternativas; decisão com justificativa registrada; custo (financeiro, operacional, relacionamento); quem deveria ter autoridade.

**E6 — Biblioteca de Prompts** (A.1 a A.4)
- 5 prompts: traduzir lógica técnica; encontrar decisões implícitas; gerar cenários de teste; revisar texto como auditor; argumentar contra a própria conclusão. Cada um com papel, contexto, restrições, formato de saída e critério de sucesso. Resultado em ≥2 aplicados ao Anexo A; análise crítica (útil, errado, como verificou); técnica avançada e motivo.

**E7 — Prontidão e Funil de Inovação** (A.9, A.10)
- Diagnóstico nas 3 dimensões; dependências críticas de pessoas e risco; funil (quem propõe, evidência mínima por etapa, quem decide, recurso liberado por vez); critério de encerramento aplicado a ≥2 iniciativas atuais; 2 intervenções com responsável, prazo e sinal observável.

**E8 — Nota de Ciência, Tecnologia e Sociedade** (A.3, A.8, A.11) — **2 a 3 páginas**
- Efeito desigual das decisões da E2; prioridades embutidas no que o sistema otimiza e quem as definiu; quem deveria ter sido consultado; ferramenta que reduz × que automatiza desigualdade; posicionamento público da Lumis.

## Formato da entrega

- Documento único, com identificação da equipe, reunindo as 8 entregas de forma articulada.
- Fluxograma da lógica de decisão **em arquivo próprio**, apresentável.
- Biblioteca de prompts **em apêndice**, com resultados e verificação.
- **Planilhas** de margem por conta e a árvore de métricas.
- Envio pelo portal, no prazo.

## Critérios de avaliação

Clareza da tradução · identificação de decisões implícitas · consistência econômica (margem e modelo de cobrança) · qualidade da árvore de métricas · método na deliberação ética · domínio de prompt avançado · realismo do funil (inclusive encerramento) · consciência sociotécnica.

## Disciplinas × entregas

| Disciplina | Entrega |
|---|---|
| Computational Thinking & AI for Leaders | E1 |
| AI Governance & Responsible AI Management | E2, E5 |
| AI Strategy & Market Dynamics | E3 |
| Data-Driven Business & Analytics | E4 |
| Prompt Engineering & Intelligent Automation | E6 |
| Leadership, Change Management & Org. Culture | E7 |
| AI Product & Innovation Management | E7 |
| Formação Social e Sustentabilidade | E8 |

---

# Anexo A — Dossiê técnico do Lumis Insight

> Dados fictícios e didáticos. Dão continuidade à Fase 2 (porte, contratos e custo iguais). Se faltar algo, registrar a lacuna.

## A.1 Arquitetura (Quadro 3)

Duas camadas: modelo estatístico (pontuação 0–100) + regras manuais que ajustam a pontuação e definem a classificação. Regras avaliadas na ordem; **a primeira que se aplica encerra a avaliação daquele bloco**.

| Etapa | O que acontece | Responsável pela regra |
|---|---|---|
| 1. Recepção | Recebe o registro do paciente com até 34 campos preenchidos pelo cliente | Integração — time técnico |
| 2. Completude | Verifica campos ausentes e aplica a regra do A.3 | Time de dados |
| 3. Pontuação | Modelo atribui 0 a 100 com base nas variáveis do Quadro A.6 da Fase 2 | Time de dados |
| 4. Ajustes por regra | Aplica as regras do A.2 (somam ou subtraem pontos) | Time técnico |
| 5. Classificação | Compara a pontuação ajustada aos limiares do A.2 e atribui a faixa | Definido em 2023, sem revisão |
| 6. Desempate | Mesma pontuação e mesma faixa → regra do A.3 | Não documentado |
| 7. Entrega | Devolve ao cliente a faixa e os 3 fatores de maior peso | Integração — time técnico |

O sistema **não devolve a pontuação numérica**, só a faixa. Decidido em 2023 para evitar que hospitais calibrassem registros. Nunca comunicado formalmente a nenhum cliente.

## A.2 Regras de ajuste e limiares

Amostra de 8 das **41** regras ativas (Quadro 4):

| Nº | Regra | Efeito | Criada em |
|---|---|---|---|
| R-04 | Internação nos últimos 90 dias | +12 | 2022 |
| R-07 | Registro de comorbidade crônica | +9 | 2022 |
| R-11 | Mais de 2 faltas em consultas agendadas | −7 | 2023 |
| R-15 | Encaminhamento de pronto-socorro | +15 | 2022 |
| R-19 | Custo acumulado de procedimentos no quartil superior | +11 | 2023 |
| R-23 | Plano da categoria básica → não aplicar o bônus da R-19 | anula +11 | 2024 |
| R-31 | 75 anos ou mais e nenhuma internação recente | −6 | 2023 |
| R-38 | Cliente é conta estratégica → elevar em uma faixa todos os casos limítrofes | +1 faixa | 2025 |

Limiares sobre a pontuação ajustada (Quadro 5):

| Faixa | Pontuação ajustada | % dos casos em 2026 | Definida em |
|---|---|---|---|
| Alta | 72 ou mais | 18% | mar/2023 |
| Média | 45 a 71 | 44% | mar/2023 |
| Baixa | abaixo de 45 | 38% | mar/2023 |

**Origem do 72:** calibrado em mar/2023 para a fila de alta prioridade do Hospital Vila Ipê caber na capacidade daquela unidade. Objetivo operacional, não clínico. Replicado para todos os clientes e nunca recalibrado; hoje governa 38 contas.

## A.3 Dados faltantes e desempate (Quadro 6)

11 dos 34 campos são frequentemente enviados vazios.

| Campo ausente | Frequência | Comportamento atual | Efeito prático |
|---|---|---|---|
| Histórico de internações | 23% | Assume zero internações | Sem histórico = sem necessidade |
| Custo acumulado de procedimentos | 31% | Assume zero | Anula a R-19 e reduz a pontuação |
| Comorbidades | 19% | Assume nenhuma | Anula a R-07 |
| Resultado de exames | 42% | Assume a média da base | Achata extremos |
| Tipo de plano | 8% | Assume categoria básica | Aciona a R-23 e anula bônus |

Unidades públicas e clientes com sistemas antigos têm, em média, **2,4 vezes** mais campos vazios que unidades privadas de grande porte.

**Desempate:** mesma pontuação e mesma faixa → ordem de entrada no sistema (mais antigo primeiro). Não documentado; descoberto por leitura do código.

## A.4 Histórico de alterações de parâmetro (Quadro 7)

| Data | Alteração | Motivo registrado | Quem autorizou |
|---|---|---|---|
| mar/2023 | Limiar de alta em 72 | Ajuste de capacidade de fila | Time técnico |
| set/2023 | Criação da R-11 | Sugestão de cliente em reunião | Time técnico |
| set/2023 | Criação da R-31 | Não registrado | Não registrado |
| fev/2024 | Criação da R-23 | Reclamação de cliente sobre distorção | Time técnico |
| nov/2025 | Criação da R-38 | Pedido comercial | Diretoria comercial |

Nenhuma passou por avaliação de impacto sobre grupos, nenhuma foi comunicada aos clientes, não há processo formal de aprovação.

## A.5 Contratos e cobrança (Quadro 8)

| Segmento | Contas | Modelo | Ticket médio anual | Reajuste |
|---|---|---|---|---|
| Hospitais e clínicas | 24 | Fixo anual, uso ilimitado | R$ 1,18 mi | Inflação |
| Seguradoras | 9 | Fixo anual, teto de 400 mil decisões | R$ 1,04 mi | Inflação |
| Bancos | 5 | Fixo anual, teto de 250 mil decisões | R$ 0,72 mi | Inflação |
| Total | 38 | — | R$ 1,084 mi | — |

24 contas sem teto; nenhum contrato prevê revisão de preço por volume.

## A.6 Custo por decisão e rentabilidade (Quadro 9)

Custo direto mensal R$ 1,44 mi, dos quais **R$ 1.039 mil** variáveis (inferência e infraestrutura). **1.050.000 decisões/mês** → **R$ 0,99 por decisão**.

| Conta | Segmento | Decisões/mês | Receita mensal | Custo variável | Margem |
|---|---|---|---|---|---|
| Rede Sanare | Hospitalar | 214.000 | R$ 145.000 | R$ 211.860 | −R$ 66.860 |
| Hospital Vila Ipê | Hospitalar | 96.000 | R$ 98.000 | R$ 95.040 | R$ 2.960 |
| Hospital Aurora | Hospitalar | 61.000 | R$ 92.000 | R$ 60.390 | R$ 31.610 |
| Seguradora Prisma | Seguradora | 58.000 | R$ 87.000 | R$ 57.420 | R$ 29.580 |
| Banco Meridiano | Banco | 24.000 | R$ 60.000 | R$ 23.760 | R$ 36.240 |
| Demais 33 contas | Diversos | 597.000 | R$ 2.951.000 | R$ 591.030 | R$ 2.359.970 |
| Total | — | 1.050.000 | R$ 3.433.000 | R$ 1.039.500 | R$ 2.393.500 |

**Sanare:** contrato de 2020 (3 unidades), hoje 7 unidades; valor igual, consumo 2,9×; sem teto nem revisão. Apresentada como principal referência comercial; ninguém tinha calculado a margem.

## A.7 Indicadores hoje acompanhados (Quadro 10)

| Indicador | Frequência | Quem acompanha | Deriva de hipótese de valor? |
|---|---|---|---|
| Decisões processadas por mês | Diária | Time técnico | Não — atividade |
| Disponibilidade da interface | Diária | Time técnico | Sim — confiabilidade |
| Tempo médio de resposta | Diária | Time técnico | Sim — experiência de uso |
| Receita recorrente anual | Mensal | Diretoria | Sim — sustentabilidade |
| Número de contas ativas | Mensal | Comercial | Parcialmente — não distingue conta rentável |
| Vidas analisadas acumuladas | Mensal | Comercial | Não — divulgação |
| Acurácia do modelo | Anual | Time de dados | Sim, mas só na base de 2023 |
| Reclamações formais | Sem periodicidade | Sucesso do cliente | Não é tratado como indicador |

Nenhum mede a qualidade da decisão entregue; nenhum é aberto por subgrupo; o desempenho por subgrupo da Fase 2 foi pontual.

## A.8 Dilemas em aberto

1. **R-38:** eleva casos limítrofes de contas estratégicas (pedido comercial). Dois pacientes com o mesmo quadro recebem prioridades diferentes conforme o hospital. Remover = conversas difíceis com **5 clientes que são 31% da receita**.
2. **Dado faltante:** zero prejudica unidades com sistemas menos completos (públicas, menores). Alternativa — revisão humana de todos esses casos — aumenta em **~31%** as revisões manuais dos clientes, que muitos não conseguem absorver nem são obrigados por contrato.
3. **Transparência do limiar:** a Lumis nunca informou que a pontuação existe nem o corte. Divulgar aumenta transparência e questionamento qualificado, e permite que clientes ajustem registros para subir de faixa.

## A.9 Documentação e dependência de pessoas (Quadro 11)

| Ativo de conhecimento | Onde está | Pessoas que dominam |
|---|---|---|
| Lógica das 41 regras | No código, sem documentação externa | 2 |
| Racional dos limiares | Não documentado — memória de reunião | 1 |
| Pipeline de dados e integrações | Documentação parcial, desatualizada desde 2024 | 3 |
| Critérios de retreinamento | Não documentado | 2 |
| Histórico de incidentes e correções | Planilha individual | 1 |
| Contratos e cláusulas de uso de dados | Pasta jurídica, sem índice | 2 |

Duas pessoas do time de dados concentram 4 dos 6 ativos. Rotatividade do time de dados em 12 meses: 27%.

## A.10 Iniciativas em andamento (Quadro 12)

| Iniciativa | Como entrou | Status | Tempo | Critério de encerramento |
|---|---|---|---|---|
| Explicabilidade das decisões | Pedido de cliente após incidente | Em desenvolvimento | 5 meses | Não definido |
| Módulo de risco de crédito | Pedido comercial | Em especificação | 3 meses | Não definido |
| Reescrita do pipeline de dados | Proposta do time técnico | Parado | 11 meses | Não definido |
| Agente conversacional de triagem | Ideia de sócio-fundador | Protótipo | 7 meses | Não definido |
| Painel de desempenho por subgrupo | Consequência da Fase 2 | Não iniciado | — | Não definido |

Nenhuma com critério de encerramento ou avaliação formal de prioridade. A parada há 11 meses ainda consome reuniões semanais.

## A.11 Efeito das escolhas de projeto sobre grupos (Quadro 13)

| Grupo | % da base | Campos vazios (média) | Efeito acumulado das regras | Faixa alta (%) |
|---|---|---|---|---|
| Privadas de grande porte | 38% | 1,9 | Neutro a positivo | 24% |
| Privadas de médio porte | 29% | 3,1 | Levemente negativo | 18% |
| Públicas conveniadas | 22% | 4,6 | Negativo — R-11, R-23 e dado zero | 11% |
| Regiões remotas | 11% | 5,2 | Negativo — acúmulo de todos os efeitos | 9% |

A faixa alta varia de 24% a 9%. Parte pode ser perfil clínico; parte vem das escolhas dos A.2 e A.3. Separar as duas causas é o que a auditoria vai exigir.

## Referências do capítulo

Brasil, Marco Legal da IA (PL, 2024) · Christensen, *O dilema da inovação* (2012) · Crawford, *Atlas of AI* (2021) · Eubanks, *Automating Inequality* (2018) · UE, AI Act, Reg. 2024/1689 · ISO/IEC 42001:2023 · Osterwalder e Pigneur, *Business Model Generation* (2010) · Ries, *The Lean Startup* (2011) · Russell e Norvig, *AI: A Modern Approach*, 4. ed. (2020) · Winner, "Do Artifacts Have Politics?", *Daedalus* 109(1), 1980.
