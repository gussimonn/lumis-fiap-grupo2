# Dados da F2-E2: Quadros 7 a 11 (e trechos dos Quadros 14 e 17)

Material de apoio. Transcrição do Anexo A do Cap. 2 ([_Enunciado/Cap02_A_IA_e_o_Mercado.pdf](../_Enunciado/Cap02_A_IA_e_o_Mercado.pdf), p. 23 a 25, 27 e 29), feita em 06/10/2026 a partir do texto extraído do PDF. Os valores são os do PDF, sem arredondamento.

## Enunciado da Entrega 2 [fonte: Cap. 2, seção 4, p. 15]

> O fundo quer saber de que é feito o ativo da Lumis. Você precisa responder com precisão, inclusive quando a resposta for desconfortável.
> - Origem, base contratual e legal dos dados que alimentam o Lumis Insight, com identificação dos pontos frágeis.
> - Análise das principais variáveis do sistema: o que cada uma pretende medir, o que de fato mede e que distorções pode introduzir. Trate explicitamente ao menos um caso de variável proxy.
> - Revisão crítica das métricas hoje apresentadas ao mercado: como foram apuradas, o que autorizam concluir e o que não autorizam.
> - Proposta de um novo conjunto de indicadores de gestão — no máximo cinco — em que cada um esteja associado a uma decisão concreta que ele é capaz de mudar, com abertura por subgrupo quando aplicável.
>
> Dados para esta entrega: quadros "Base de dados e contratos", "Variáveis e pesos", "Desempenho declarado e em campo, com abertura por subgrupo" e "Painel comercial".
>
> Aplique as quatro perguntas sobre métricas apresentadas neste capítulo a cada indicador que você propuser ou descartar.

Disciplinas ligadas [fonte: Cap. 2, Quadro 2]: Computational Thinking & AI for Leaders (leitura crítica de dados, variáveis e representação da informação; análise de proxies e de suas distorções) e Data-Driven Business & Analytics (distinção entre métrica de vaidade e métrica de decisão; construção do conjunto de indicadores de gestão).

Critérios de avaliação mais ligados a esta entrega [fonte: Cap. 2, 4.3]: **Honestidade analítica** (registrar as fragilidades do ativo em vez de contorná-las) e **Rigor sobre dados e métricas** (o que as variáveis representam e a diferença entre número apresentável e número útil). Também conta **Integração e defesa** (coerência entre as cinco entregas e o memorando).

Item do memorando do Vetor Capital [fonte: Cap. 2, p. 5]:
> 2. Fundamento do ativo: de onde vêm os dados que sustentam o produto, sob que base legal são usados, o que essas variáveis efetivamente representam e qual parte disso constitui vantagem defensável.
> 3. Evidência, não narrativa: as métricas apresentadas ao mercado precisam ser reproduzíveis fora do ambiente de demonstração. O fundo será explícito: qualquer número que não sobreviva a uma auditoria independente será tratado como passivo, não como diferencial.

## As quatro perguntas [fonte: Cap. 2, 2.3, p. 9]

- **Medida em quê?** Sobre qual população, em que período e em quais condições esse número foi apurado? Um resultado obtido em ambiente controlado não descreve o comportamento em campo.
- **Medida por quem?** Quem produziu o número tem interesse no resultado dele? A apuração é reproduzível por alguém de fora?
- **Muda alguma decisão?** Se esse indicador variar de forma significativa, o que exatamente a empresa passa a fazer de diferente? Se a resposta for nada, o indicador não é de gestão.
- **Esconde qual distribuição?** Uma média confortável pode ocultar desempenho muito pior em subgrupos específicos. Todo número agregado deve ser aberto por segmento antes de virar argumento.

Conceitos do capítulo usados aqui: dado como testemunho e variável como proxy (2.2: "quando um sistema clínico usa histórico de gastos com saúde como indicador de gravidade, ele não está medindo quem está mais doente — está medindo quem teve mais acesso a atendimento"); métricas de vaidade; lei de Goodhart (2.3).

## Quadro 7. Base de dados e contratos [p. 23]

| Fonte | Volume | Período | Instrumento | Autoriza treinamento? | Vencimento |
|---|---|---|---|---|---|
| Hospital Vila Ipê | 1,2 mi de atendimentos | 2019–2026 | Contrato de 2022 | Cláusula genérica: "melhoria contínua do serviço" | 03/2027 |
| Rede Sanare (7 unidades) | 3,4 mi de atendimentos | 2020–2026 | Aditivo de 2024 | Sim, para uso agregado e anonimizado | 08/2028 |
| Seguradora Prisma | 890 mil sinistros | 2021–2026 | Contrato de 2021 | Silente | 12/2026 |
| Banco Meridiano | 410 mil operações | 2023–2026 | Contrato de 2023 | Sim, com auditoria anual do cliente | 05/2028 |
| DATASUS (base pública) | 14,0 mi de registros | 2015–2024 | Uso público | Sim | — |
| Dados sintéticos internos | 2,1 mi de registros | 2024–2026 | Geração própria | Sim | — |

Texto após o quadro: a base de treinamento soma 22,0 milhões de registros. Destes, 5,9 milhões (26,8%) são dados de clientes; o restante vem de fonte pública e de geração sintética interna. Entre os dados de clientes, 2,09 milhões de registros (35,4% do total de origem contratual) provêm de fontes cuja autorização para uso em treinamento é frágil ou inexistente: o Hospital Vila Ipê, com cláusula genérica, e a Seguradora Prisma, cujo contrato é silente sobre o tema e vence em dezembro de 2026. Nenhum dos seis instrumentos passou por revisão jurídica desde a assinatura.

Outros trechos do Cap. 2 sobre o tema:
- Quadro 5: dados de clientes vêm de "38 contratos individuais"; "dois dos maiores contratos têm cláusula frágil ou silente quanto a treinamento".
- Narrativa (1.2, p. 6): "os contratos que autorizam esse uso foram redigidos quando a empresa tinha onze pessoas, e **três** dos maiores clientes têm cláusulas que ninguém releu desde então". Divergência com o Quadro 5 ("dois"); o Quadro 7 lista quatro fontes de clientes.
- Só 4 dos 38 clientes aparecem como fonte de dados no Quadro 7. [não consta] se os outros 34 contratos tratam de dados.

## Quadro 8. Variáveis e pesos (dez maiores pesos no modelo de priorização) [p. 24]

| # | Variável | O que a empresa diz que ela mede | Peso |
|---|---|---|---|
| 1 | Nº de atendimentos nos últimos 24 meses | Histórico de necessidade de cuidado | 18,4% |
| 2 | Custo acumulado de procedimentos | Gravidade do quadro clínico | 15,1% |
| 3 | Idade do paciente | Idade | 12,7% |
| 4 | Nº de comorbidades registradas | Carga de doença | 11,2% |
| 5 | Tempo médio entre consulta e exame | Urgência percebida pelo médico | 9,8% |
| 6 | Faixa de CEP agrupada | Região de residência | 8,9% |
| 7 | Tipo de plano ou cobertura | Nível de cobertura contratada | 7,4% |
| 8 | Painel de exames laboratoriais | Estado clínico atual | 6,9% |
| 9 | Nº de faltas em consultas agendadas | Adesão ao tratamento | 5,3% |
| 10 | Especialidade de origem do encaminhamento | Via de entrada no sistema | 4,3% |

Os dez somam 100,0%. [não consta] a definição técnica de "peso" (importância de atributo, coeficiente etc.).

## Quadro 9. Desempenho declarado e em campo [p. 24]

| Recorte | Amostra | Acurácia | Sensibilidade | Taxa de falso negativo |
|---|---|---|---|---|
| Conjunto de validação de 2023 (dois hospitais da mesma região) | 48.000 | 94,1% | 92,6% | 7,4% |
| Campo, base completa, 1º semestre de 2026 | 1.940.000 | 87,6% | 82,3% | 17,7% |

Falso negativo: paciente que deveria ter sido priorizado e foi classificado como baixa prioridade.

## Quadro 10. Desempenho em campo por subgrupo, 1º semestre de 2026 [p. 25]

| Subgrupo | Participação na base | Acurácia | Sensibilidade | Falso negativo |
|---|---|---|---|---|
| 18 a 59 anos, CEP A/B | 21% | 91,2% | 89,4% | 10,6% |
| 18 a 59 anos, CEP C | 27% | 88,9% | 85,7% | 14,3% |
| 18 a 59 anos, CEP D/E | 15% | 85,1% | 79,8% | 20,2% |
| 60 anos ou mais, CEP A/B | 13% | 88,7% | 84,1% | 15,9% |
| 60 anos ou mais, CEP C | 14% | 84,2% | 76,5% | 23,5% |
| 60 anos ou mais, CEP D/E | 10% | 79,3% | 68,2% | 31,8% |

Destaque após o quadro: um paciente com 60 anos ou mais residente em CEP de faixa D/E tem 31,8% de chance de ser incorretamente classificado como baixa prioridade, três vezes a taxa observada no subgrupo de melhor desempenho. Esse é o dado que o Hospital Vila Ipê apurou por conta própria e enviou junto à notificação formal.

## Quadro 11. Painel comercial: o que a Lumis afirma publicamente hoje [p. 25]

| Afirmação divulgada | Valor | Como foi apurada |
|---|---|---|
| "Acurácia de 94%" | 94,1% | Conjunto de validação de 2023, dois hospitais da mesma região, 48 mil registros |
| "Redução de 30% no tempo de triagem" | 30,4% | Piloto de seis semanas em um único hospital, sem grupo de controle |
| "Mais de 5 milhões de vidas analisadas" | 5,2 milhões | Soma de registros processados; inclui reprocessamentos do mesmo paciente |
| "NPS 72" | 72 | Pesquisa com 9 respondentes, todos indicados pelo time comercial |
| "Disponibilidade de 99,9%" | 99,92% | Disponibilidade da interface de programação, não do serviço de ponta a ponta |

## Trechos de outros quadros ligados à F2-E2

**Quadro 14. Registro de incidentes, últimos 24 meses [p. 27]**

| Data | Ocorrência | Detectado por | Tempo até a correção |
|---|---|---|---|
| 03/2025 | Modelo passou a descartar exames de laboratório recém-credenciado | Cliente | 22 dias |
| 09/2025 | Queda de desempenho após atualização do fornecedor de modelo | Equipe interna | 6 dias |
| 01/2026 | Duplicidade de registros inflou o número de "vidas analisadas" | Auditoria interna | Corrigido no sistema; não corrigido no material comercial |
| 07/2026 | Viés etário e regional na priorização de atendimento | Cliente (Hospital Vila Ipê) | Em tratamento |

**Quadro 17. Indicadores socioambientais e de equidade [p. 29]** (linhas ligadas à F2-E2)
- Distribuição dos pacientes processados por faixa de CEP: A/B 34%, C 41%, D/E 25%.
- Reclamações formais nos últimos 12 meses, por faixa de CEP: A/B 8, C 19, D/E 47 (total 74).
- Métricas de impacto reportadas publicamente: nenhuma.
- Política de privacidade específica para dados sensíveis de saúde: em elaboração desde 2024, sem versão aprovada.
- Observação: pacientes de CEP D/E são 25% da base processada e concentram 64% das reclamações formais. O registro de reclamações é mantido pelo time de sucesso do cliente e nunca foi cruzado com os dados de desempenho do modelo.

**Quadro 12 e texto [p. 26]:** a priorização da fila de atendimento tem 640.000 decisões por mês, revisão humana por amostragem de 2%, uso autorizado pela diretoria comercial do cliente sem aprovação interna formal. A Lumis não tem comitê de ética nem de risco; colocar nova versão em produção é decisão exclusiva do diretor de tecnologia.

**Quadro 13 [p. 26]:** Renata Souza (CEO), Paulo Adjaí (CTO), Yuri Nakamura (Dados), Head of AI Management (nós), Camila Torres (Comercial), Marcos Villela (Produto), Ana Beatriz Rangel (DPO, jurídico e proteção de dados).

## Contas de conferência (equipe)

- 2,09 mi ÷ 5,9 mi = 35,4%. Vila Ipê 1,2 mi + Prisma 0,89 mi = 2,09 mi. 2,09 ÷ 22,0 = 9,5% da base total.
- Clientes: 1,2 + 3,4 + 0,89 + 0,41 = 5,9 mi. Total: 5,9 + 14,0 + 2,1 = 22,0 mi.
- O falso negativo médio ponderado pela participação no Quadro 10 dá 17,65%, coerente com os 17,7% do Quadro 9.
- A participação por faixa de CEP no Quadro 10 (A/B 34%, C 41%, D/E 25%) bate com o Quadro 17.
- 31,8 ÷ 10,6 = 3,0.
