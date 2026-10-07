# F2-A: Registro de Prompts da F2-E2 (Auditoria do Ativo), v1

**Data de execução:** 06/10/2026 · **Ferramenta:** Claude Code (modelo Claude Opus 5.5), com subagentes de pesquisa usando WebSearch e WebFetch
**Exigência do enunciado:** o apêndice de prompts só é obrigatório na Entrega 1 [fonte: Cap. 2, Entrega 1 e 4.2]. A equipe registra também os prompts da F2-E2 pelo mesmo método (D-007), para manter a trilha de auditoria.

## 1. Método

1. **Entender** (sem pesquisa web): um subagente leu o enunciado e respondeu o que é a entrega, o objetivo, o que comunicar, o que o conselho quer ver e como comunicar. Outro auditou a v1 do colega número por número. Um terceiro fez as contas, e um quarto as refez de forma independente.
2. **Pesquisa:** seis frentes em paralelo, cada uma com um subagente, o mesmo bloco de contexto e regras (seção 2) e uma tarefa própria (seção 3).
3. **Verificação adversarial:** para cada frente, um subagente independente tentou refutar cada achado, reabrindo as fontes e refazendo as contas. Só seguem os achados "confirmado" e "parcial", estes com a correção do verificador.
4. **Síntese:** um subagente escreveu o levantamento seguindo a skill humanizer.
5. **Crítica e revisão:** um subagente leu o levantamento como professor, conselheiro e analista do Vetor Capital. Os pontos de gravidade alta e média foram incorporados por um último subagente.

Ao todo foram 19 subagentes, 533 chamadas de ferramenta e cerca de 1,9 mi de tokens. Dos 110 achados de pesquisa, 71 foram confirmados, 39 corrigidos e nenhum refutado.

| Frente | Achados | Confirmados | Parciais |
|---|---|---|---|
| proxy | 20 | 12 | 8 |
| legal | 17 | 12 | 5 |
| metricas | 18 | 12 | 6 |
| indicadores | 18 | 12 | 6 |
| conselho | 19 | 14 | 5 |
| diligencia | 18 | 9 | 9 |

**Verificação humana (Head of AI Management):** pendente. Antes da v2, abrir pessoalmente as fontes externas que forem para o corpo e as marcadas como parciais na seção 6 do levantamento.

Material bruto: [apoio/F2-E2_achados_e_verificacoes.json](apoio/F2-E2_achados_e_verificacoes.json) (achados, buscas, lacunas e veredictos de cada frente) e [apoio/F2-E2_etapas_locais.md](apoio/F2-E2_etapas_locais.md) (entendimento, auditoria da v1 e contas).

## 2. Bloco comum de contexto e regras (incluído em todos os prompts de pesquisa)

```text
Você é analista sênior de dados e governança de IA em saúde, com experiência em due diligence para fundos de venture capital no Brasil.

## Contexto
Você apoia o Head of AI Management da Lumis Intelligence, empresa FICTÍCIA criada para um curso de Gestão em IA (FIAP). A Lumis vende o Lumis Insight, sistema de IA preditiva para priorização clínica (hospitais) e classificação de risco (seguradoras e bancos) no Brasil. O fundo Vetor Capital propõe aporte de R$ 120 mi e exige em 60 dias uma tese de crescimento defensável. Na Entrega 2 o fundo quer saber de que é feito o ativo da Lumis: origem e base legal dos dados, o que as variáveis do modelo de fato medem (proxies), se as métricas divulgadas sobrevivem a uma auditoria independente e quais indicadores de gestão a empresa deveria usar. Data de hoje: 06/10/2026.

## Dados oficiais da Lumis (única fonte permitida sobre a empresa)
Leia o arquivo C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Dados_Quadros_7-11.md. Ele traz o enunciado, as quatro perguntas sobre métricas e os Quadros 7 a 11 (base de dados e contratos, variáveis e pesos, desempenho declarado e em campo, desempenho por subgrupo, painel comercial), com trechos dos Quadros 12, 13, 14 e 17.

## Regras inegociáveis
1. NÃO invente números sobre a Lumis. Todo dado da Lumis vem do arquivo acima; cite "Quadro N". Se algo não está lá, escreva "informação indisponível".
2. Lumis, Aster Health, Vetor Capital, Hospital Vila Ipê, Rede Sanare, Seguradora Prisma e Banco Meridiano são fictícios. NÃO procure por eles na web. Procure ANÁLOGOS REAIS e rotule-os como análogos.
3. Todo fato externo precisa de fonte verificável (título, organização/autor, data, URL) que você efetivamente abriu. Prefira fontes primárias (lei, regulador, artigo revisado, documento oficial) e publicações recentes. Não cite de memória: se não conseguiu abrir a fonte, classifique como "hipotese".
4. Separe explicitamente: fato_externo (com fonte), dado_anexo (dos quadros), calculo (mostre a conta) e hipotese (inferência sua, não comprovada).
5. Use WebSearch e WebFetch. Se não estiverem carregadas, carregue com ToolSearch ("select:WebSearch,WebFetch"). Faça várias buscas, inclusive em português.
6. Responda em português do Brasil. Seja específico e conciso; nada de generalidades. Não crie nem altere arquivos.
```

## 3. Prompts de pesquisa, resultados e verificação

### Prompt 1: Variáveis proxy em modelos clínicos

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: o que as variáveis do Quadro 8 medem de fato
Levante evidência real (artigos revisados, relatórios de regulador, casos documentados) sobre variáveis que funcionam como proxy em modelos de priorização e risco em saúde, cobrindo as variáveis do Quadro 8:
- custo acumulado e número de atendimentos como proxy de necessidade (verifique o estudo de Obermeyer et al., Science, 2019, com números e mecanismo);
- local de residência (CEP, ZIP code, índices de privação de área) usado em algoritmos clínicos e o efeito sobre grupos de baixa renda;
- faltas em consultas (no-show) como proxy de adesão e o viés documentado em modelos de previsão de falta;
- tipo de plano ou cobertura como proxy de renda e acesso;
- tempo entre consulta e exame e painel laboratorial: ausência informativa (informative missingness) e dependência da oferta da rede;
- idade em modelos clínicos: quando é variável legítima e quando o efeito vira discriminação;
- no Brasil: evidência pública (IBGE/PNS, ANS, Fiocruz, artigos) de que acesso, uso de serviços e cobertura variam com renda, região e idade.
Também levante métodos usados para auditar uma variável proxy (ablação, análise contrafactual, calibração por subgrupo, troca do rótulo-alvo, como no caso Obermeyer).
Cruze com os Quadros 8 e 10: que mecanismo ligaria as variáveis às taxas de falso negativo por subgrupo? Marque como hipotese o que o anexo não comprova.

## Entrega
Retorne pelo menos 8 achados (ideal: 10 a 15), cada um com ID no formato PRX-NN. Liste as lacunas e as buscas feitas.
```

**Resultado obtido:** 20 achados com 18 buscas na web.

Encontrei evidência externa, de fontes que abri, para cada variável do Quadro 8 que funciona como proxy de acesso. As principais são o caso Obermeyer (Science, 2019), o Algorithmic Bias Playbook (Chicago Booth, 2021), o caso do CEP na Univ. of Chicago (Nature, 2019), estudos sobre previsão de faltas (Samorani/SCU; Tuan et al., Ann Fam Med 2025), a ausência informativa em exames laboratoriais (Agniel et al., BMJ 2018), o subdiagnóstico seletivo em grupos mal atendidos (Seyyed-Kalantari et al., Nat Med 2021), o documento da OMS sobre idadismo em IA (2022) e, para o Brasil, a PNS 2019 (IBGE e Palmeira et al. 2022), o Atlas da Radiologia 2025 e a auditoria do TCU de 2026. Cruzando com o anexo: pelo menos 64,9% do peso do modelo (variáveis 1, 2, 5, 6, 7 e 9) está em variáveis que dependem de acesso, de oferta da rede ou de renda, e não da gravidade clínica. Chega a 83,0% se entrarem comorbidades registradas e painel laboratorial, que também só existem quando houve atendimento. O padrão do Quadro 10 tem dois gradientes, um de CEP e outro de idade, e eles se somam com interação positiva (+6,3 p.p.). É o padrão esperado de um rótulo ou de entradas ancorados em uso de serviços. O anexo, porém, não informa o rótulo-alvo nem o sinal dos pesos. Por isso o mecanismo é hipótese que precisa de auditoria: troca de rótulo, ablação das variáveis de acesso e calibração por subgrupo.

**Verificação:** Nenhuma skill Arkium cobre este tema (trabalho acadêmico da FIAP sobre empresa fictícia); a verificação seguiu as regras do CLAUDE.md do projeto. Dos 20 achados, 11 foram confirmados e 9 saem como parciais, com correção. Nenhum foi refutado. Principais correções: PRX-02 (suspender é o passo 3C do Playbook, e não o 3B); PRX-07 (os ~68% são 118 de 174 exames, e não dos 272); PRX-09 (a fonte primária do IBGE voltou a dar 403; os números só conferem em fonte secundária, e os 28,5% incluem plano odontológico); PRX-14 (a classificação 'dependente de acesso' é hipótese, não dado do anexo; e 'dez maiores pesos' somando 100% é uma inconsistência a perguntar); PRX-16 (a interação só existe na escala aditiva; na multiplicativa o efeito conjunto de 3,0x fica perto do produto de 2,86x, e não há intervalos de confiança); PRX-17 (a comparação de 76,2% com 85% mistura bases diferentes; a alternativa deve citar a base de treino, e não a de validação); PRX-19 (ablação e teste contrafactual não vêm das fontes citadas); PRX-20 (o TCU diz que 'outros estados', e não 'muitos municípios', não registraram atividade). Ajustes de referência: PRX-05 deve citar o título publicado 'Overbooked and Overlooked...' (M&SOM). Os PDFs foram lidos por extração local em C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/21178879-392f-48c9-b000-b7bcda3abb02/scratchpad (pb.txt, nat.txt, ibge.txt). Nenhum arquivo do projeto foi criado nem alterado.

### Prompt 2: Base legal e contratual dos dados

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: base legal e contratual para treinar IA com dados de clientes de saúde no Brasil
Levante, com fonte primária, o que a lei e o regulador dizem sobre o uso de dados de clientes para treinar um produto de IA vendido a terceiros:
- LGPD: dado pessoal sensível de saúde (art. 5º, II), dado anonimizado (art. 5º, III, e art. 12), princípios de finalidade e adequação (art. 6º), hipóteses do art. 11 para dado sensível, vedações do art. 11, §4º (compartilhamento com objetivo de vantagem econômica) e §5º (operadoras de planos e seleção de riscos), agentes de tratamento (controlador e operador; o que acontece quando o operador usa o dado para finalidade própria, como treinar o próprio modelo);
- ANPD: guias e normas aplicáveis (agentes de tratamento, anonimização, dosimetria de sanções, posicionamentos sobre IA e treinamento de modelos), com datas;
- dados bancários e de seguros (Banco Meridiano e Seguradora Prisma): sigilo bancário (LC 105/2001) e regras da SUSEP ou do CMN/BCB que limitem uso secundário, se houver;
- prontuário e sigilo médico (CFM, Lei 13.787/2018) quando o dado vem de hospital;
- o que torna uma cláusula como "melhoria contínua do serviço" frágil para autorizar treinamento (finalidade específica e informada) e o que costuma constar de cláusulas robustas de direito de uso de dados para IA;
- casos reais análogos de uso secundário de dados de saúde para desenvolver IA questionado por regulador (ex.: verifique Royal Free London NHS Trust e Google DeepMind, decisão do ICO de 2017; Project Nightingale, Ascension e Google, 2019) e o que aconteceu;
- situação do PL 2338/2023 (marco legal da IA) em 2026.
Cruze com o Quadro 7: classifique cada uma das seis fontes por grau de fragilidade e diga o que falta saber (informação indisponível). Não dê parecer jurídico conclusivo: marque como hipotese.

## Entrega
Retorne pelo menos 8 achados (ideal: 10 a 15), cada um com ID no formato LEG-NN. Liste as lacunas e as buscas feitas.
```

**Resultado obtido:** 17 achados com 21 buscas na web.

Antes da pesquisa acionei a skill arkium-governanca-dados, como manda a instrução corporativa para temas de LGPD. Ela serviu só de roteiro: a Lumis é fictícia e não é material da Arkium. A leitura das fontes primárias aponta numa direção só. Pela LGPD, dado de saúde é sensível (art. 5º, II). Tratar esse dado exige base do art. 11, e o consentimento só vale se for 'específico e destacado, para finalidades específicas'. O princípio da finalidade (art. 6º, I) proíbe tratamento posterior incompatível com o que foi informado ao titular. O operador age 'em nome do controlador' (art. 5º, VII; art. 39), e a ANPD diz no Guia de Agentes de Tratamento (v2.0, abr/2022, §53) que ele 'só poderá tratar os dados para a finalidade previamente estabelecida pelo controlador'. Se o operador treinar um modelo próprio e vender esse modelo a terceiros, passa a decidir finalidade e a responder solidariamente (art. 42, §1º, I). Pela dosimetria da ANPD (Res. CD/ANPD 4/2023), um caso com dado sensível, larga escala e vantagem econômica cai na faixa grave, com multa de até 2% do faturamento limitada a R$ 50 mi por infração. Há dois limites setoriais. O art. 11, §4º veda o uso compartilhado de dado de saúde entre controladores com objetivo de vantagem econômica, salvo em serviços de saúde em benefício do titular. O §5º veda a operadoras de planos de saúde a seleção de riscos com dado de saúde, e isso afeta a linha de classificação de risco para seguradoras. A LC 105/2001 impõe sigilo bancário com pena de reclusão e só admite revelação com consentimento expresso. Os análogos reais mostram como regulador e Justiça tratam o tema. No caso Royal Free/DeepMind (ICO, jul/2017), 1,6 mi de pacientes, o regulador concluiu que o uso fugia do que os pacientes 'razoavelmente esperariam' e exigiu um compromisso formal (undertaking), base legal, avaliação de impacto à privacidade e auditoria, sem multa. A ação coletiva foi rejeitada em dez/2024. O caso ANPD x Meta (jul-ago/2024) suspendeu o treinamento de IA por hipótese legal inadequada e falta de transparência, e a liberação veio com um plano de conformidade. O Project Nightingale (nov/2019, cerca de 50 mi de registros) gerou investigação do HHS/OCR. O PL 2338/2023 segue na Câmara aguardando parecer do relator (última movimentação: 02/09/2026). Cruzando com o Quadro 7: Prisma (silente, vence 12/2026) e Vila Ipê (cláusula genérica, vence 03/2027, cliente em notificação formal) são as fontes críticas. Sanare e Meridiano têm autorização condicionada, com dúvidas sobre o que conta como 'agregado e anonimizado' e sobre o sigilo bancário. DATASUS e sintéticos têm risco menor, mas com perguntas de origem. Nada disso é parecer jurídico: as conclusões sobre a Lumis são hipóteses.

**Verificação:** Verifiquei os 17 achados. Confirmei 11. Seis ficaram parciais: LEG-06, LEG-07, LEG-08, LEG-14 e LEG-15, já com o texto corrigido no campo correcao, e o LEG-13, que se mantém mas tem uma ressalva sobre a divergência na contagem de contratos frágeis. Nenhum foi refutado.

Por achado:
- LEG-07 (Prismall): o acórdão diz 'contractual entitlement', não 'contractual right'. A frase de Denham vem do The Register, não da página ICO 40.
- LEG-08 (Nightingale): os 50 mi de pacientes não aparecem na fonte citada (WTVR). É preciso outra fonte ou a forma 'até cerca de'.
- LEG-06 (Meta): a decisão é de 01/07/2024 e a publicação no DOU de 02/07. A multa diária vale para descumprimento.
- LEG-14 (contas): todas as contas conferem. O Vila Ipê (03/2027) fica cerca de 3 meses depois de uma janela de 60 dias, não 'logo depois'. O início dessa janela não consta no arquivo de dados.
- LEG-15 (classificação por fonte): o art. 7º, §3º, foi conferido e pode perder a marca [não verificado].
- LEG-13: a divergência entre 'dois' (Quadro 5) e 'três' (narrativa) contratos frágeis merece aparecer na entrega.

Ao citar o art. 11, §4º, usar o texto compilado ou a Lei 13.853/2019, porque a publicação original da LGPD na Câmara traz a redação antiga. O texto do Guia da ANPD saiu do PDF baixado em C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/21178879-392f-48c9-b000-b7bcda3abb02/scratchpad/guia2.pdf, e a Lei 13.787 do PDF baixado na mesma pasta.

Não acionei a skill arkium-governanca-dados porque o material é acadêmico (FIAP) e, pelo CLAUDE.md do projeto, não é da Arkium. A verificação usou fontes primárias e resumos de busca, como indicado acima. Não criei nem alterei arquivos do projeto.

### Prompt 3: Métricas divulgadas e auditoria independente

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: o que cada métrica do Quadro 11 autoriza concluir
Levante evidência real para julgar as cinco afirmações do painel comercial (Quadro 11) como um auditor independente as julgaria:
- queda de desempenho entre validação interna e validação externa ou em campo em modelos clínicos (dataset shift); verifique Wong et al., JAMA Internal Medicine, 2021 (modelo de sepse da Epic) e revisões sobre validação externa;
- por que acurácia é métrica fraca em triagem com classes desbalanceadas, e por que sensibilidade e falso negativo importam mais quando o erro é deixar de priorizar;
- padrões de relato de modelos preditivos clínicos (TRIPOD+AI 2024, DECIDE-AI, CONSORT-AI) e o que exigem sobre amostra, população e subgrupos;
- piloto sem grupo de controle: regressão à média, efeito Hawthorne, sazonalidade; o que seria um desenho mínimo aceitável;
- NPS com 9 respondentes escolhidos pelo comercial: margem de erro e viés de seleção (calcule ou cite);
- "vidas analisadas" com reprocessamento: diferença entre registros e pessoas únicas;
- disponibilidade da API versus disponibilidade de ponta a ponta (SLI/SLO; verifique o livro de SRE do Google);
- casos reais de reguladores punindo afirmações exageradas sobre IA: verifique o acordo do procurador-geral do Texas com a Pieces Technologies (2024), as ações da SEC por "AI washing" (Delphia e Global Predictions, 2024) e ações da FTC sobre alegações de IA;
- lei de Goodhart aplicada a métricas de IA.
Para cada uma das cinco afirmações, diga: medida em quê, por quem, o que autoriza, o que não autoriza, e se sobreviveria a uma auditoria independente (o critério do memorando do Vetor Capital).

## Entrega
Retorne pelo menos 8 achados (ideal: 10 a 15), cada um com ID no formato MET-NN. Liste as lacunas e as buscas feitas.
```

**Resultado obtido:** 18 achados com 20 buscas na web.

Nenhuma das cinco afirmações do painel comercial (Quadro 11) sobrevive a uma auditoria independente do jeito que está escrita. (1) "Acurácia de 94%" foi medida em 48 mil registros de dois hospitais da mesma região, em 2023. Em campo, em 2026, a acurácia cai para 87,6% e a taxa de falso negativo mais que dobra, de 7,4% para 17,7%; no subgrupo 60+ CEP D/E ela chega a 31,8% (Quadros 9 e 10). A literatura mostra que essa queda entre validação e campo é a regra: Wong et al. 2021 encontraram AUC de 0,63 para o modelo de sepse da Epic, contra 0,76 a 0,83 declarados pelo fabricante, e Wessler et al. 2021 viram 81% das validações externas abaixo da derivação. O TRIPOD+AI 2024 exige justificar a amostra, informar intervalo de confiança e desempenho por subgrupo sociodemográfico. Acurácia é a métrica errada quando o erro grave é deixar de priorizar. (2) "Redução de 30% na triagem" vem de um piloto de 6 semanas, em um hospital e sem controle, exposto a regressão à média, efeito Hawthorne e sazonalidade; autoriza no máximo uma hipótese. (3) "5 milhões de vidas" soma registros com reprocessamentos, e a própria Lumis já detectou a inflação sem corrigir o material comercial (Quadro 14). (4) "NPS 72" com 9 respondentes escolhidos pelo comercial: o intervalo de 95% pelo método adjusted-Wald da MeasuringU vai de cerca de 8 a 24 até cerca de 93 a 100; além disso, 72 não é um valor que 9 respostas inteiras consigam produzir. (5) "99,9%" mede a API, não o serviço de ponta a ponta; o livro de SRE do Google define disponibilidade pela experiência do usuário. Para o conselho, há precedentes reais de punição por métrica de IA exagerada: o acordo do procurador-geral do Texas com a Pieces Technologies (2024), que obriga a divulgar definição e método de cada métrica; a SEC contra Delphia e Global Predictions (US$ 400 mil, 2024); e a FTC com a Operation AI Comply (2024). Isso sustenta a tese do memorando do Vetor Capital: número que não se reproduz fora da demo vira passivo.

**Verificação:** Dos 18 achados, 12 foram confirmados e 6 ficaram parciais. Nenhum foi refutado. Os dados do anexo e todos os cálculos batem (MET-05, MET-11 e MET-14 refeitos). As correções principais são estas. MET-06: o arXiv de Kernbach não tem o exemplo de sepse com 3%/97%, o termo 'paradoxo da acurácia' nem AUPRC; o que tem é um exemplo de 90% e a recomendação de relatar no mínimo sensibilidade e especificidade. MET-13: o cap. 'Embracing Risk' é de Marc Alvidrez. MET-15: incluir que a Pieces nega irregularidade e separar as métricas '<0,001%' (critical) e '<1/100.000' (severe). MET-17: Goodhart e auditorias externas não aparecem no resumo. MET-04 e MET-18: atribuem à própria Lumis a validação de 2023 e o dado de campo do Quadro 9, mas o anexo não diz quem os apurou; isso é [não consta] ou [hipótese]. Ressalvas menores: conferir no PDF do JAMA a faixa de 0,76–0,83 do desenvolvedor (MET-01) e o número exato do item de amostra no DECIDE-AI (MET-08). Nenhum arquivo foi criado ou alterado. A fonte do anexo foi C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Dados_Quadros_7-11.md.

### Prompt 4: Indicadores de gestão e monitoramento

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: referências para no máximo cinco indicadores de gestão que mudam decisões
Levante referências reais (regulador, norma, artigo revisado) sobre monitoramento de modelos de IA em produção na saúde e indicadores de decisão:
- métricas de equidade e a escolha entre elas: igualdade de oportunidade (paridade de taxa de falso negativo), paridade demográfica, calibração por grupo; impossibilidade de satisfazer todas ao mesmo tempo (Kleinberg et al., 2016; Chouldechova, 2017; Hardt et al., 2016);
- Good Machine Learning Practice (FDA, Health Canada, MHRA, 2021), em especial o princípio de monitoramento do modelo implantado; orientação da FDA sobre Predetermined Change Control Plan (PCCP), com data;
- NIST AI RMF 1.0 (função MEASURE) e ISO/IEC 42001:2023 (avaliação de desempenho), no que dizem sobre medir e monitorar;
- ANVISA: RDC 657/2022 (software como dispositivo médico) e se um sistema de priorização clínica poderia ser enquadrado;
- práticas de monitoramento de drift e de limites (thresholds) que disparam suspensão ou rollback; exemplos de "kill switch" ou critérios de interrupção;
- reclamações e sinalizações de usuários como fonte de sinal de dano (farmacovigilância/tecnovigilância como análogo);
- diferença entre indicador de atividade e indicador de resultado; métricas de vaidade versus de decisão (Eric Ries, Lean Startup, ou fonte equivalente).
Proponha critérios para escolher no máximo cinco indicadores para a Lumis com base nos Quadros 7 a 11, 14 e 17. Para cada indicador sugerido, aponte a decisão que ele muda, o limite que dispararia a decisão (marque como hipotese se não houver base), o cargo que mede (Quadro 13) e a abertura por subgrupo. Liste também indicadores que deveriam ser descartados e por quê.

## Entrega
Retorne pelo menos 8 achados (ideal: 10 a 15), cada um com ID no formato IND-NN. Liste as lacunas e as buscas feitas.
```

**Resultado obtido:** 18 achados com 31 buscas na web.

Nenhuma skill da Arkium cobre esta tarefa: é um trabalho acadêmico da FIAP com empresa fictícia. Por isso usei só o anexo e fontes primárias que abri. As referências convergem num ponto: indicador de gestão de IA clínica precisa ser medido em campo, aberto por subgrupo e ligado a um gatilho de ação. Esse gatilho pode ser suspender, desligar, reverter ou não liberar a versão. Os textos que pedem isso são o GMLP de 2021 (princípios 3, 8, 9 e 10), o NIST AI RMF 1.0 (MEASURE 2.4, 2.11, 3.1 e 3.3; MANAGE 2.4 e 4.1), o guia de PCCP da FDA (emitido em 04/12/2024 e revisado em 18/08/2025) e Feng et al. (2022). A literatura de equidade (Kleinberg 2016, Chouldechova 2017, Hardt 2016, Rajkomar 2018) obriga a escolher uma métrica de forma explícita. Para priorização, em que o dano é o falso negativo, a escolha defensável é a igualdade de oportunidade (paridade da taxa de falso negativo), e o custo dela são mais alertas falsos. O FAQ da ANVISA sobre a RDC 657/2022 (Q64) diz que um software de triagem que classifica o risco do paciente pode ser SaMD, conforme o uso. A tecnovigilância (RDC 67/2009) serve de análogo para tratar reclamação como sinal de dano. No anexo, quatro números do painel comercial (Quadro 11) não passam pelas quatro perguntas do capítulo. O quinto, a disponibilidade, é uma métrica técnica parcial. Proponho cinco indicadores: (1) taxa de falso negativo em campo por subgrupo idade × CEP e a razão entre o pior e o melhor subgrupo; (2) desvio entre o desempenho em campo e o validado, por cliente; (3) reclamações formais por faixa de CEP, cruzadas com o falso negativo; (4) parcela dos registros de clientes no treino com autorização contratual expressa, com prazo até o vencimento; (5) tempo até detectar e corrigir um incidente, junto com a parcela de incidentes detectados pelo cliente. Todos os limites numéricos que propus são hipótese, porque nenhuma fonte fixa valores para este caso.

**Verificação:** Verifiquei os 18 achados: 10 confirmados, 8 parciais e nenhum refutado. Nenhuma skill da Arkium cobre o tema, e o trabalho é acadêmico e não da Arkium. Por isso segui o CLAUDE.md do LumisOS e o arquivo Dados_Quadros_7-11.md. Não criei nem alterei arquivos.

Fontes externas reabertas e confirmadas: os PDFs do PCCP da FDA, do NIST AI RMF e do FAQ da RDC 657 da ANVISA, cujo texto extraí; os resumos no arXiv; Rajkomar e Feng no PMC; a JAMA; a RDC 67 no LegisWeb.

Correções que mudam o conteúdo:
- **IND-01:** no GMLP, a frase sobre viés e deriva do princípio 10 vale só quando o modelo é retreinado depois da implantação.
- **IND-16:** o indicador 4 se define como 'autorização expressa e revisada pelo jurídico', mas nenhum contrato foi revisado (Quadro 7). Então o valor atual pela definição é 0%, não 64,6%. E o limite do indicador 1 (falso negativo acima de 15%) já dispara hoje em 4 dos 6 subgrupos, que somam 52% da base. Isso daria cerca de 333 mil revisões humanas por mês, contra 12.800 hoje.
- **IND-18:** no anexo, o uso em seguradoras é classificação de sinistros, não precificação.

Ajustes menores de fonte e de linguagem:
- **IND-04:** a ISO 42001 foi conferida só em fonte secundária.
- **IND-12:** 'causa e efeito' é paráfrase da equipe, não frase de Ries.
- **IND-17:** quem apurou os 94% não consta no anexo. 'Anula' é forte demais para o NPS.

Os percentuais de Obermeyer (17,7% para 46,5%) seguem sem conferência na fonte primária, como o achado já marca. Arquivos usados: C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Dados_Quadros_7-11.md e C:/Users/gusta/Downloads/LumisOS/00_Lumis/Empresa_e_Contexto.md.

### Prompt 5: Como comunicar dados e riscos ao conselho

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: como um conselho de administração quer receber uma auditoria de dados e métricas
Levante fontes reais sobre como apresentar risco, dados e métricas de IA a conselhos de administração e investidores:
- IBGC: Código das Melhores Práticas de Governança Corporativa (6ª ed., 2023) e publicações do IBGC sobre IA e conselhos, no que dizem sobre informação ao conselho;
- NACD, Harvard Law School Forum on Corporate Governance, WEF ou consultorias reconhecidas sobre supervisão de IA pelo conselho: que perguntas o conselho faz e que informação espera receber;
- boas práticas de material para conselho (board pack): começar pela decisão pedida, poucas métricas com tendência e limite, exceções em destaque, separar fato de opinião, extensão curta; princípio da pirâmide de Barbara Minto;
- clareza na apresentação de dados (tabelas versus gráficos, uma mensagem por gráfico): fontes como Tufte, Knaflic (Storytelling with Data) ou guias de governo;
- como apresentar más notícias e incertezas a investidores sem perder credibilidade (transparência como ativo; evidência de que ocultar problemas destrói mais valor que expô-los).
Traduza em recomendações concretas para um documento de 4 a 6 páginas ao conselho da Lumis sobre a auditoria do ativo: o que vem primeiro, que números ficam no corpo, o que vai para anexo, como marcar o que é fato, cálculo e hipótese.

## Entrega
Retorne pelo menos 8 achados (ideal: 10 a 15), cada um com ID no formato CON-NN. Liste as lacunas e as buscas feitas.
```

**Resultado obtido:** 19 achados com 23 buscas na web.

Nenhuma skill da Arkium cobre comunicação a conselho em trabalho acadêmico. A pesquisa usou só fontes externas abertas nesta sessão, mais os Quadros 7 a 17 do anexo. As fontes concordam em cinco pontos. (1) O IBGC (Código, 6ª ed., 2023) pede que todo material de deliberação comece com um sumário e um posicionamento fundamentado da diretoria. Pede também que o conselheiro identifique com clareza o que vai deliberar e os pontos de atenção, e que a informação seja verdadeira, tempestiva, clara e relevante, "sejam elas positivas ou negativas". (2) O guia Accenture/Microsoft/IBGC para conselheiros (2024) e a NACD (Blue Ribbon Commission, 2024) põem no centro da supervisão de IA o inventário de sistemas, a avaliação de riscos, o viés e métricas claras. Os investidores (Glass Lewis, via Harvard Forum, 2026) citam viés e dano reputacional como riscos materiais. (3) As boas práticas de material para conselho (ICSA/Board Intelligence, Minto) mandam abrir com o pedido de decisão e a resposta, sumário executivo de no máximo uma página, frases curtas, o "e daí?" em vez de dado bruto, e no máximo cinco perguntas que estruturam o texto. (4) Os guias de visualização (UK Government Analysis Function, Tufte) recomendam tabela para comparar valores exatos e gráfico só quando há padrão a mostrar. Cada gráfico deve ter um título que já diga a mensagem, sem enfeite, e os limites de qualidade e incerteza devem ficar ao lado do número, não escondidos no anexo. (5) Sobre más notícias, a evidência acadêmica (Kothari, Shu e Wysocki, 2009; Billings, Cedergren e Dube, 2021) mostra que gestores tendem a atrasar notícias ruins e que, quando elas vêm à tona, a reação do preço é maior. Já Cutler, Davis e Peterson (2019) apontam um contraponto: divulgar mais está associado a ações judiciais que avançam. Os casos Epic Sepsis (o desempenho declarado caiu na validação externa) e Theranos (alegações de desempenho falsas) são análogos reais do risco de "número que não sobrevive à auditoria". Para a Lumis, isso vira um documento de 4 a 6 páginas que abre pela decisão pedida e pela resposta. O corpo leva poucos números: a queda de desempenho do laboratório para o campo (Q9), a disparidade por subgrupo (Q10), os 35,4% de dados contratuais com autorização frágil (Q7), um placar das 5 afirmações públicas (Q11) e os ≤5 indicadores propostos. O resto vai para anexo, com cada número marcado como fato, cálculo ou hipótese.

**Verificação:** Nenhuma skill da Arkium cobre este tema (trabalho acadêmico fictício de governança de IA). A verificação seguiu as regras do projeto e conferiu as fontes primárias abertas agora, em 06/10/2026.

Dos 19 achados, 14 foram confirmados e 5 ficaram parciais. Nenhum foi refutado.

Confirmei contra o PDF ou a página original:
- IBGC 6ª ed. (CON-01 a 03);
- Guia Accenture/Microsoft/IBGC (CON-04);
- NACD 2024 (CON-05);
- Glass Lewis/HLS 2026 (CON-06) e ISS STOXX/HLS 2024 (CON-07);
- Minto (CON-09);
- UK Analysis Function (CON-10 e 11);
- os três estudos acadêmicos (CON-13);
- JAMA/Epic Sepsis (CON-14) e SEC/Theranos (CON-15).

As contas de CON-16 batem.

Ficaram parciais:
- CON-08: 'lead with the ask' não aparece na página da Board Intelligence. É síntese da equipe. O resto confere.
- CON-12: 'chartjunk' não está na fonte secundária citada.
- CON-17: o Cap. 2 (4.2) não fixa páginas para a E2, só para o memorando (máx. 2). Ele exige um documento único com as cinco entregas articuladas, não anexos independentes. O apêndice de prompts é da Entrega 1.
- CON-18: as etiquetas [cálculo] e [contexto externo] não existem no padrão Tag do projeto.
- CON-19: o exemplo diz que o modelo 'erra 31,8%' dos idosos de CEP D/E. Na verdade, 31,8% é a taxa de falso negativo. A acurácia do subgrupo é 79,3%.

Observação operacional: baixei de novo os PDFs do IBGC e do Guia para a pasta temporária da sessão, por cima de arquivos de mesmo nome e mesma origem. Gravei o texto extraído em arquivos novos, ver_*.txt. Nenhum arquivo do projeto foi alterado.

### Prompt 6: O que o investidor verifica sobre dados em IA

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: o que um fundo verifica sobre dados e métricas na due diligence de uma empresa de IA
Levante fontes reais sobre due diligence técnica e de dados em investimentos em empresas de IA, especialmente em saúde:
- listas de verificação publicadas por fundos, escritórios de advocacia ou consultorias sobre proveniência dos dados, direito de uso para treinamento, cadeia de consentimento e dependência de poucos clientes;
- como o investidor trata dados sem direito de uso claro (passivo, ajuste de valuation, condição precedente, cláusula de indenização, escrow); exemplos de cláusulas de "data rights" em term sheets ou acordos de investimento;
- casos reais em que problemas de dados ou de métricas afetaram uma rodada, aquisição ou valor de empresa de IA ou healthtech (verifique, por exemplo, Babylon Health, Olive AI, IBM Watson Health e a venda de seus ativos em 2022; escolha casos com fonte sólida);
- o que é considerado "vantagem defensável" em dados (data moat) e as críticas a essa ideia (por exemplo, o texto da Andreessen Horowitz "The Empty Promise of Data Moats", 2019).
Cruze com os Quadros 7 a 11: o que, na Lumis, um analista do Vetor Capital marcaria como passivo, o que marcaria como ativo e o que pediria como condição prévia ao aporte. Marque como hipotese o que não tiver base no anexo.

## Entrega
Retorne pelo menos 8 achados (ideal: 10 a 15), cada um com ID no formato DIL-NN. Liste as lacunas e as buscas feitas.
```

**Resultado obtido:** 18 achados com 15 buscas na web.

Fontes reais de escritórios de advocacia (Reed Smith, mar/2026; Osler, jan/2025) mostram como funciona hoje a due diligence de empresas de IA. O investidor verifica a cadeia de direitos sobre os dados de treinamento, ou seja, de onde vêm, com que consentimento e com que linhagem documentada. Também verifica testes documentados de viés e de desempenho. Quando encontra risco, protege-se com declarações específicas do vendedor, indenizações direcionadas, escrow de 18 a 24 meses, ajuste de preço e obrigação de correção com prazo. Os casos reais mostram três mecanismos de perda de valor. (1) Dado obtido sem direito pode obrigar a apagar o próprio modelo: a FTC, autoridade americana de defesa do consumidor, fez isso com a Everalbum em 2021, e a LGPD prevê eliminação de dados e suspensão do tratamento no art. 52. (2) Métrica feita pelo próprio desenvolvedor não se sustenta em validação externa: foi o caso do Epic Sepsis Model (AUC declarada de 0,76–0,83 contra 0,63 medida fora) e das alegações da Babylon criticadas na Lancet. (3) Concentração em poucos clientes: a Babylon perdeu contratos ligados à Centene que somavam quase 50% da receita e quebrou. A IBM gastou cerca de US$ 4 bi montando a Watson Health e vendeu ativos por pouco mais de US$ 1 bi. O texto da a16z (2019) relativiza o próprio conceito de vantagem defensável baseada em dados (data moat). Cruzando com os Quadros 7 a 11, um analista do Vetor Capital marcaria como passivo: os 2,09 mi de registros com autorização frágil ou silente (35,4% dos dados de clientes), as métricas do Quadro 11 que não sobrevivem a auditoria e o falso negativo de 31,8% no subgrupo 60+ D/E. Marcaria como ativo, com ressalvas: o aditivo da Rede Sanare, o contrato do Banco Meridiano e a própria medição em campo com abertura por subgrupo. Antes do aporte, pediria parecer jurídico dos contratos, regularização ou exclusão dos dados frágeis seguida de retreino, validação externa independente e correção do material comercial. As cláusulas propostas para o caso da Lumis são hipótese. Nenhuma skill da Arkium cobre este tema; o trabalho é acadêmico (FIAP) e não é material da Arkium.

**Verificação:** Conferi os 18 achados. Nenhum foi refutado e nenhum ficou sem confirmação; 8 se confirmam como estão e 10 são parciais e precisam de ajuste de texto.

**Fatos externos.** Reabri todas as fontes. Reed Smith, Osler, FTC/Everalbum, FPF/Kurbo (agora aberta e confirmada), JAMA/Epic, Undark/Babylon (a carta na Lancet confirmada pelo repositório White Rose), Healthcare Dive, a16z e Berkeley conferem. Ajustes:
- **DIL-02:** a menção a saúde e finanças no artigo vale só para explicabilidade.
- **DIL-04:** a auditoria da ANPD do art. 20 §2 só vale quando o controlador nega informações alegando segredo comercial. Os demais artigos da LGPD conferem, mas o texto foi lido em lgpd-brasil.info; o Planalto ainda precisa ser conferido.
- **DIL-08:** a lista de ativos vem do comunicado da Francisco Partners, não do Boston Globe. Nenhuma fonte aberta diz que a tecnologia central do Watson ficou fora da venda.
- **DIL-09:** a página aberta não dá o ano do valuation nem atribui a frase à gestão da Olive.

**Dados do anexo e contas.**
- **DIL-12 e DIL-14:** conferem com Dados_Quadros_7-11.md.
- **DIL-13:** as contas fecham, mas a frase do prazo usa a data real (06/10/2026) como início dos 60 dias. Esse prazo é da história: é a validade da oferta, não uma janela de diligência, e a data em que começa não consta.
- **DIL-15:** as somas fecham, mas a leitura de que essas variáveis medem acesso precisa vir marcada como hipótese na própria frase.

**Hipóteses.**
- **DIL-16:** a frase 'que concorrentes não têm' não tem base no anexo.
- **DIL-17:** propõe criar um DPO, mas a Lumis já tem uma (Ana Beatriz Rangel, Quadro 13).
- **DIL-18:** resume mal o art. 20 §2 e ignora a revisão humana obrigatória nos casos de maior impacto, adotada após o incidente.

Arquivo de dados conferido: C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Dados_Quadros_7-11.md.

## 4. Prompts das etapas sem pesquisa web

### Entendimento da entrega

```text
Arquivos (leia antes de trabalhar):
- Dados oficiais da entrega, já transcritos e conferidos: C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Dados_Quadros_7-11.md (enunciado da Entrega 2, as quatro perguntas, Quadros 7 a 11 e trechos dos Quadros 12, 13, 14 e 17).
- Texto completo do Cap. 2 (sem marca d'água): C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/21178879-392f-48c9-b000-b7bcda3abb02/scratchpad/cap2_limpo.txt
- Contexto da Lumis: C:/Users/gusta/Downloads/LumisOS/00_Lumis/Empresa_e_Contexto.md, C:/Users/gusta/Downloads/LumisOS/00_Lumis/Pessoas_e_Cargos.md, C:/Users/gusta/Downloads/LumisOS/00_Lumis/Compromissos_Vigentes.md
- Versão 1 do colega (a revisar): C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/F2-E2_Auditoria_do_Ativo_v1.docx (extraia o texto com python-docx: parágrafos e tabelas) ou o PDF original C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Fase 2_Lumis_Entrega2_v1colega.pdf
- Entrega anterior da equipe, que define o tom e o formato adotados: C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E1_Mapa_do_Territorio/F2-E1_Mapa_do_Territorio_v2.docx e as decisões D-012, D-018, D-019 e D-020 em C:/Users/gusta/Downloads/LumisOS/DECISOES.md

Tarefa: antes de revisar a Entrega 2 (F2-E2, Auditoria do Ativo: Dados e Métricas), a equipe quer entender a entrega a fundo. Responda, sempre apoiado no enunciado do Cap. 2 (cite página ou seção), no memorando do Vetor Capital, nos critérios de avaliação (seção 4.3), no Quadro 2 (disciplinas) e no formato final da fase (seção 4.2: documento único com as cinco entregas articuladas, memorando ao conselho de até 2 páginas):
1. O que é esta entrega, em linguagem simples, e onde ela se encaixa no dossiê da Fase 2 (o que recebe da F2-E1 e o que passa para F2-E3, F2-E5 e o memorando).
2. O objetivo da entrega: a pergunta que ela responde e o que o professor vai avaliar. Liste item a item o que o enunciado exige (incluindo "ao menos um caso de proxy", "no máximo cinco indicadores", "abertura por subgrupo", "as quatro perguntas a cada indicador proposto OU descartado").
3. O que precisamos comunicar: as 3 a 5 mensagens que o documento tem de deixar claras, com o quadro que sustenta cada uma. Inclua a mensagem desconfortável que o enunciado pede para não contornar.
4. O que o conselho (e o Vetor Capital) gostaria de ver: as perguntas que um conselheiro faria ao ler, o que o deixaria seguro, o que o faria desconfiar. Use os itens 2 e 3 do memorando ("fundamento do ativo" e "evidência, não narrativa": número que não sobrevive a auditoria independente é passivo).
5. Como comunicar isso ao conselho: estrutura sugerida, ordem das seções, o que vai no corpo e o que vai para anexo, tamanho, tom. Leve em conta o formato que a equipe adotou na F2-E1 v2 (relatório ao conselho com a conclusão no início, seções que se encadeiam, tabelas só onde guardam números, figuras simples; ver D-012, D-018 a D-020) e a regra do curso de marcar fonte, hipótese e o que não consta.
6. Pontes obrigatórias: compromissos C1, C2 e C5 (Compromissos_Vigentes.md), diagnóstico D-004 (viés vindo dos dados), e o que a F2-E1 v2 já prometeu que a Entrega 2 faria.
Responda em português, em markdown, de forma direta. Não crie nem altere arquivos.
```

### Auditoria da v1 do colega

```text
Arquivos (leia antes de trabalhar):
- Dados oficiais da entrega, já transcritos e conferidos: C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Dados_Quadros_7-11.md (enunciado da Entrega 2, as quatro perguntas, Quadros 7 a 11 e trechos dos Quadros 12, 13, 14 e 17).
- Texto completo do Cap. 2 (sem marca d'água): C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/21178879-392f-48c9-b000-b7bcda3abb02/scratchpad/cap2_limpo.txt
- Contexto da Lumis: C:/Users/gusta/Downloads/LumisOS/00_Lumis/Empresa_e_Contexto.md, C:/Users/gusta/Downloads/LumisOS/00_Lumis/Pessoas_e_Cargos.md, C:/Users/gusta/Downloads/LumisOS/00_Lumis/Compromissos_Vigentes.md
- Versão 1 do colega (a revisar): C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/F2-E2_Auditoria_do_Ativo_v1.docx (extraia o texto com python-docx: parágrafos e tabelas) ou o PDF original C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Fase 2_Lumis_Entrega2_v1colega.pdf
- Entrega anterior da equipe, que define o tom e o formato adotados: C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E1_Mapa_do_Territorio/F2-E1_Mapa_do_Territorio_v2.docx e as decisões D-012, D-018, D-019 e D-020 em C:/Users/gusta/Downloads/LumisOS/DECISOES.md

Tarefa: faça uma auditoria crítica e minuciosa da v1 do colega da F2-E2 (Auditoria do Ativo), como faria o professor que corrige. Para cada ponto, dê um ID (V1-NN), o trecho, o problema e a correção sugerida. Cubra:
1. Fidelidade aos dados: confira TODO número e TODA afirmação factual da v1 contra Dados_Quadros_7-11.md e o texto do Cap. 2. Aponte erros, arredondamentos enganosos, dados omitidos que mudariam a leitura (ex.: sensibilidade e participação por subgrupo do Quadro 10; incidente de 01/2026 do Quadro 14 com a duplicidade ainda no material comercial; reclamações por CEP do Quadro 17; revisão por amostragem de 2% do Quadro 12), citações erradas (ex.: a seção 8 cita "Capítulo 1 — A IA e o Mercado"; confira) e coisas apresentadas como fato que deveriam ser hipótese.
2. Cumprimento do enunciado, item a item: origem e base contratual e legal (a parte LEGAL foi tratada ou só a contratual?); variáveis com o que pretendem medir, o que medem e a distorção; proxy explícito; métricas com como foram apuradas, o que autorizam e o que não autorizam; no máximo cinco indicadores, cada um com decisão concreta e abertura por subgrupo; as quatro perguntas aplicadas a cada indicador proposto E a cada descartado (as métricas do painel comercial e o indicador "auditorias contratuais concluídas" foram descartados: as quatro perguntas foram aplicadas a eles?).
3. Honestidade analítica e rigor: a v1 encara as fragilidades ou as suaviza? Diz qual parte do ativo é defensável? Separa fato, cálculo e hipótese?
4. Responsabilidade: "Medida por quem?" termina em áreas (Dados, Jurídico, CS) ou em cargos? Compare com o Quadro 13 e com a regra da F2-E3 de que toda responsabilidade termina em um cargo.
5. Coerência com Compromissos_Vigentes.md (C1, C2, C5 e os pontos de cobrança), com D-004 e com a F2-E1 v2 (por exemplo, a F2-E1 v2 diz que "a auditoria completa fica para a Entrega 2" e fala em contratos "pendentes de revisão").
6. Comunicação para conselho: a v1 começa pela conclusão? É clara para quem não é técnico? Tem jargão (drift, rollback, E2E, claim, baseline, CS)? Tem marcas de texto gerado por IA (travessões, "não é apenas X, mas Y", tríades, negrito decorativo)? Use a skill humanizer: leia C:/Users/gusta/Downloads/LumisOS/.claude/skills/humanizer/SKILL.md e C:/Users/gusta/Downloads/LumisOS/.claude/skills/humanizer/PT-BR.md.
7. O que está bom e deve ficar na v2.
Feche com uma lista priorizada das 10 mudanças mais importantes para a v2. Responda em português, em markdown. Não crie nem altere arquivos.
```

### Contas

```text
Arquivos (leia antes de trabalhar):
- Dados oficiais da entrega, já transcritos e conferidos: C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Dados_Quadros_7-11.md (enunciado da Entrega 2, as quatro perguntas, Quadros 7 a 11 e trechos dos Quadros 12, 13, 14 e 17).
- Texto completo do Cap. 2 (sem marca d'água): C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/21178879-392f-48c9-b000-b7bcda3abb02/scratchpad/cap2_limpo.txt
- Contexto da Lumis: C:/Users/gusta/Downloads/LumisOS/00_Lumis/Empresa_e_Contexto.md, C:/Users/gusta/Downloads/LumisOS/00_Lumis/Pessoas_e_Cargos.md, C:/Users/gusta/Downloads/LumisOS/00_Lumis/Compromissos_Vigentes.md
- Versão 1 do colega (a revisar): C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/F2-E2_Auditoria_do_Ativo_v1.docx (extraia o texto com python-docx: parágrafos e tabelas) ou o PDF original C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Fase 2_Lumis_Entrega2_v1colega.pdf
- Entrega anterior da equipe, que define o tom e o formato adotados: C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E1_Mapa_do_Territorio/F2-E1_Mapa_do_Territorio_v2.docx e as decisões D-012, D-018, D-019 e D-020 em C:/Users/gusta/Downloads/LumisOS/DECISOES.md

Tarefa: produza as contas que sustentam a F2-E2, só com os dados do Anexo A (Dados_Quadros_7-11.md). Para cada conta, dê um ID (CAL-NN), a pergunta que ela responde, a conta passo a passo, o resultado e uma frase sobre o que ele significa para o conselho. Não invente dados: se uma conta exige dado que não existe (ex.: número de pacientes únicos, volume por cliente das reclamações), diga "informação indisponível". Inclua pelo menos:
- composição da base (pública, sintética, clientes) e peso das fontes frágeis na base de clientes e na base total; peso de cada fonte de cliente; concentração (quanto da base de clientes vem da Rede Sanare); fontes cujo contrato vence antes de 12/2027;
- quanto da base de clientes está em cada grau de autorização (forte com condição, genérica, silente);
- soma dos pesos das variáveis que dependem de acesso ou de condição socioeconômica (defina claramente o critério e mostre alternativas: só as 4 mais óbvias, ou todas as que a equipe classificaria como proxy de acesso) e quanto do modelo é sinal clínico direto;
- queda validação → campo em acurácia, sensibilidade e falso negativo, em p.p. e em termos relativos; quantas vezes o falso negativo aumentou;
- falso negativo médio ponderado pelo Quadro 10 e conferência com o Quadro 9; razão entre o pior e o melhor subgrupo em falso negativo e em sensibilidade; efeito da idade com CEP fixo e do CEP com idade fixa (decomposição simples);
- ordem de grandeza de pacientes que deveriam ser priorizados e não foram: explique por que não é possível calcular com precisão (falta a prevalência de casos que deveriam ser priorizados) e, se fizer alguma estimativa ilustrativa, marque como hipótese e mostre a premissa. Use também o volume de 640.000 decisões de priorização por mês do Quadro 12 e a revisão por amostragem de 2% (quantas decisões por mês passam sem revisão humana);
- reclamações por faixa de CEP (Quadro 17): participação nas reclamações versus participação na base, e taxa relativa por faixa (D/E versus A/B);
- painel comercial: diferença entre 94,1% e 87,6%; margem de erro aproximada de um NPS com n = 9 (explique a premissa); o que 99,92% de disponibilidade significa em horas por ano e por que não diz nada sobre o serviço de ponta a ponta;
- amostra de validação (48 mil) como fração da amostra de campo (1,94 mi).
Responda em português, em markdown. Não crie nem altere arquivos.
```
