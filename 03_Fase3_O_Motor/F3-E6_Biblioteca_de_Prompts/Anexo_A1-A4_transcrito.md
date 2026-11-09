# Anexo A, Quadros A.1 a A.4 (transcrição)

Material de apoio. Transcrito do Cap. 3 (`_Enunciado/Cap03_O_Motor.pdf`, seções 5.1 a 5.4, Quadros 3 a 7) em 08/11/2026 e conferido contra o PDF. É o [ANEXO] usado nas execuções dos prompts da biblioteca. Sem dado pessoal.

## A.1 Arquitetura do Lumis Insight: o caminho de uma decisão

O sistema combina duas camadas. A primeira é um modelo estatístico que atribui a cada caso uma pontuação de 0 a 100. A segunda é um conjunto de regras escritas manualmente que ajusta essa pontuação e define a classificação final. As regras são avaliadas na ordem apresentada e a primeira que se aplica encerra a avaliação daquele bloco.

| Etapa | O que acontece | Responsável pela regra |
|---|---|---|
| 1. Recepção | O sistema recebe o registro do paciente com até 34 campos preenchidos pelo cliente. | Integração, time técnico |
| 2. Completude | Verifica quais campos estão ausentes e aplica a regra de preenchimento do Quadro A.3. | Time de dados |
| 3. Pontuação | O modelo estatístico atribui pontuação de 0 a 100 com base nas variáveis do Quadro A.6 da Fase 2. | Time de dados |
| 4. Ajustes por regra | Aplica as regras do Quadro A.2, que somam ou subtraem pontos. | Time técnico |
| 5. Classificação | Compara a pontuação ajustada aos limiares do Quadro A.2 e atribui a faixa de prioridade. | Definido em 2023, sem revisão |
| 6. Desempate | Se dois casos ficam na mesma pontuação e na mesma faixa, aplica a regra do Quadro A.3. | Não documentado |
| 7. Entrega | Devolve ao sistema do cliente a faixa de prioridade e os três fatores de maior peso. | Integração, time técnico |

O sistema não devolve a pontuação numérica ao cliente, apenas a faixa. Essa decisão foi tomada em 2023 para evitar que hospitais tentassem calibrar registros para obter pontuações mais altas. Nunca foi comunicada formalmente a nenhum cliente.

## A.2 Regras de ajuste e limiares de classificação

Amostra representativa de 8 das 41 regras hoje ativas. As demais seguem a mesma estrutura e estão disponíveis no repositório interno.

| Nº | Regra (em linguagem natural) | Efeito | Criada em |
|---|---|---|---|
| R-04 | Se o paciente teve internação nos últimos 90 dias, somar pontos. | +12 pontos | 2022 |
| R-07 | Se há registro de comorbidade crônica, somar pontos. | +9 pontos | 2022 |
| R-11 | Se o número de faltas em consultas agendadas for maior que 2, subtrair pontos. | −7 pontos | 2023 |
| R-15 | Se o encaminhamento veio de pronto-socorro, somar pontos. | +15 pontos | 2022 |
| R-19 | Se o custo acumulado de procedimentos está no quartil superior, somar pontos. | +11 pontos | 2023 |
| R-23 | Se o plano contratado é da categoria básica, não aplicar o bônus da R-19. | anula +11 | 2024 |
| R-31 | Se o paciente tem 75 anos ou mais e nenhuma internação recente, subtrair pontos. | −6 pontos | 2023 |
| R-38 | Se o cliente é conta estratégica, elevar em uma faixa todos os casos limítrofes. | +1 faixa | 2025 |

Limiares de classificação vigentes, aplicados sobre a pontuação já ajustada:

| Faixa | Pontuação ajustada | % dos casos em 2026 | Definida em |
|---|---|---|---|
| Alta prioridade | 72 ou mais | 18% | mar/2023 |
| Média prioridade | de 45 a 71 | 44% | mar/2023 |
| Baixa prioridade | abaixo de 45 | 38% | mar/2023 |

Origem do limiar de 72 pontos: o corte de 72 foi calibrado em março de 2023 para que a fila de alta prioridade de um cliente específico, o Hospital Vila Ipê, coubesse na capacidade de atendimento daquela unidade naquele momento. O objetivo era operacional, não clínico. O parâmetro foi replicado para todos os clientes seguintes e nunca foi recalibrado. Hoje ele governa a priorização em 38 contas com capacidades instaladas, perfis de pacientes e realidades regionais completamente diferentes.

## A.3 Dados faltantes e regras de desempate

Dos 34 campos que o sistema recebe, 11 são frequentemente enviados vazios. O comportamento atual para cada situação:

| Campo ausente | Frequência de ausência | Comportamento atual | Efeito prático |
|---|---|---|---|
| Histórico de internações | 23% dos registros | Assume zero internações | Paciente sem histórico registrado é tratado como paciente sem necessidade |
| Custo acumulado de procedimentos | 31% dos registros | Assume zero | Anula a regra R-19 e reduz a pontuação |
| Comorbidades | 19% dos registros | Assume nenhuma | Anula a regra R-07 |
| Resultado de exames | 42% dos registros | Assume a média da base | Aproxima o caso do comportamento médio, achatando extremos |
| Tipo de plano | 8% dos registros | Assume categoria básica | Aciona a regra R-23 e anula bônus |

A ausência de dados não é distribuída de forma homogênea. Registros oriundos de unidades públicas e de clientes com sistemas mais antigos apresentam, em média, 2,4 vezes mais campos vazios do que os de unidades privadas de grande porte.

Regra de desempate: quando dois casos apresentam a mesma pontuação ajustada e a mesma faixa, o sistema ordena por data de entrada do registro no sistema, o mais antigo primeiro. Essa regra não está documentada em lugar nenhum; foi identificada por leitura do código durante a preparação deste dossiê.

## A.4 Histórico de alterações de parâmetro

| Data | Alteração | Motivo registrado | Quem autorizou |
|---|---|---|---|
| mar/2023 | Definição do limiar de alta prioridade em 72 | Ajuste de capacidade de fila | Time técnico |
| set/2023 | Criação da regra R-11 (desconto por faltas) | Sugestão de cliente em reunião de acompanhamento | Time técnico |
| set/2023 | Criação da regra R-31 (desconto para 75+ sem internação) | Não registrado | Não registrado |
| fev/2024 | Criação da regra R-23 (anulação de bônus por categoria de plano) | Reclamação de cliente sobre distorção | Time técnico |
| nov/2025 | Criação da regra R-38 (elevação de faixa para conta estratégica) | Pedido comercial | Diretoria comercial |

Nenhuma dessas alterações passou por avaliação de impacto sobre grupos de pacientes. Nenhuma foi comunicada aos clientes afetados. Não existe processo formal de aprovação para mudança de parâmetro.
