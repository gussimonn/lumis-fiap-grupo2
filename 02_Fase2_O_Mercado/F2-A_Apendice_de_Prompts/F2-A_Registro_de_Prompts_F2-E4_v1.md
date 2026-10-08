# F2-A: Registro de Prompts da F2-E4 (Diagnóstico de Cultura e Funil de Inovação), v1

**Data de execução:** 07/10/2026 · **Ferramenta:** Claude Code (modelo Claude Opus 5.5), com subagentes; três frentes usaram WebSearch e WebFetch
**Exigência do enunciado:** o apêndice de prompts só é obrigatório na Entrega 1 [fonte: Cap. 2, Entrega 1 e 4.2]. A equipe registra também os prompts da F2-E4 pelo mesmo método (D-007), para manter a trilha de auditoria.

## 1. Método

1. **Entender** (sem pesquisa web): antes das frentes, a equipe leu o enunciado da Entrega 4, os Quadros 15 e 16, as entregas já feitas (E1, E2, E3 e E5), o levantamento da E3 e o rascunho do colega no material consolidado. Disso saiu o bloco comum da seção 2.
2. **Pesquisa:** sete frentes em paralelo, cada uma com um subagente, o mesmo bloco comum e uma tarefa própria (seção 3). Três frentes usaram a web (conceitos de cultura, intervenções e funil). As outras quatro trabalharam só com arquivos locais (dados, Schein, portfólio e coerência).
3. **Verificação adversarial:** para cada frente, um subagente independente tentou refutar cada achado. Ele reabriu os quadros e as entregas, refez as contas e abriu de novo as fontes externas. Só seguem os achados "confirmado" e "parcial", estes com a correção do verificador.
4. **Síntese:** um subagente escreveu o levantamento da entrega seguindo a skill humanizer.
5. **Crítica em três lentes:** um subagente leu o levantamento como o professor que corrige, como um conselheiro da Lumis e como um analista do Vetor Capital.
6. **Revisão:** os pontos levantados na crítica foram incorporados ao levantamento.

Dos 306 achados de pesquisa, 242 foram confirmados, 61 saíram como parciais (com correção), 2 foram refutados e 1 ficou sem confirmação. As três frentes com web fizeram 38 buscas.

| Frente | Achados | Confirmados | Parciais | Refutados | Não confirmados | Buscas na web |
|---|---|---|---|---|---|---|
| dados | 37 | 33 | 2 | 2 | 0 | 0 |
| schein | 54 | 48 | 6 | 0 | 0 | 0 |
| conceitos_cultura | 23 | 16 | 7 | 0 | 0 | 17 |
| intervencoes | 34 | 20 | 13 | 0 | 1 | 8 |
| funil | 40 | 25 | 15 | 0 | 0 | 13 |
| portfolio | 47 | 41 | 6 | 0 | 0 | 0 |
| coerencia | 71 | 59 | 12 | 0 | 0 | 0 |
| **Total** | **306** | **242** | **61** | **2** | **1** | **38** |

**Verificação humana (Head of AI Management):** pendente. Antes do .docx, abrir pessoalmente as fontes externas que forem para o corpo e as marcadas como parciais ou não confirmadas.

Material bruto: [apoio/F2-E4_achados_e_verificacoes.json](apoio/F2-E4_achados_e_verificacoes.json) (prompt, achados, buscas, lacunas, veredictos e críticas de cada frente).

## 2. Bloco comum de contexto e regras (incluído em todos os prompts de pesquisa)

Cada prompt de pesquisa começa com a linha "Você é pesquisador da equipe. Siga o bloco de contexto e as regras." e, em seguida, traz o bloco abaixo. Depois vem a tarefa da frente (seção 3).

```text
## Contexto
Trabalho acadêmico de Gestão em IA (FIAP). A Lumis Intelligence é empresa FICTÍCIA. A equipe atua como Head of AI Management. Estamos na Fase 2 (O Mercado): o fundo Vetor Capital propõe R$ 120 mi por 22% e dá 60 dias para uma tese de crescimento defensável. Agora fazemos a ENTREGA 4 (F2-E4) — Diagnóstico de cultura e funil de inovação.

Enunciado da Entrega 4 (Cap. 2, seção 4), literal:
"A fratura interna e o excesso de oportunidades são o mesmo problema visto de dois ângulos: falta de critério compartilhado. Ataque os dois.
• Diagnóstico da cultura atual da Lumis nas três camadas de Schein, com identificação do pressuposto profundo que sustenta o conflito entre as áreas técnica e comercial.
• Duas intervenções concretas para tratar esse conflito, com responsável, prazo e sinal observável de que funcionou.
• Funil de inovação com critérios explícitos de entrada, avanço e encerramento de iniciativas.
• Distribuição proposta dos recursos entre melhoria do produto atual, expansão adjacente e aposta de transformação, com a justificativa da proporção escolhida.
Dados para esta entrega: quadros 'Pesquisa de clima e rotatividade' e 'Backlog de iniciativas, esforço e capacidade disponível'.
Inclua ao menos uma iniciativa que você recomenda recusar, e explique por quê. Estratégia sem recusa não é estratégia."
Critérios de avaliação ligados: "Diagnóstico cultural: profundidade na identificação dos pressupostos que sustentam o conflito, e viabilidade das intervenções propostas" e "Disciplina estratégica: qualidade dos critérios de decisão e coragem para recusar iniciativas". Também "Integração e defesa: coerência entre as cinco entregas".
Disciplinas: Leadership, Change Management & Organizational Culture; AI Product & Innovation Management.

## Arquivos de contexto (texto puro, leia o que precisar)
- Cap. 2 (enunciado + Anexo A com Quadros 3–17): C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/cap02_raw.txt (modo raw, tabelas linha a linha; Quadros 15 e 16 nas seções 5.12 e 5.13) e C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/cap02_layout.txt. Seções-chave: 1.1, 1.2, 2.3, 2.5 (cultura/Schein), 2.6 (inovar com governança), 4 (missão), 4.3 (critérios).
- Cap. 1: C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/cap01_raw.txt
- Fase 1: C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/F1-E1_Mapa_da_Situacao_revisada.txt, C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/F1-E2_Mapa_de_Stakeholders_revisada.txt, C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/F1-E3_Declaracao_de_Intencao_revisada.txt (compromissos C1–C5)
- Entregas já feitas na Fase 2: C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/F2-E1_v2.txt (Mapa do Território), C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/F2-E2_v2.txt (Auditoria do Ativo), C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/F2-E3_v1.txt (Linha de Responsabilidade), C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/F2-E5_v1.txt (Due Diligence ESG)
- Base da empresa: C:/Users/gusta/Downloads/LumisOS/00_Lumis/Empresa_e_Contexto.md, C:/Users/gusta/Downloads/LumisOS/00_Lumis/Pessoas_e_Cargos.md, C:/Users/gusta/Downloads/LumisOS/00_Lumis/Compromissos_Vigentes.md
- Decisões: C:/Users/gusta/Downloads/LumisOS/DECISOES.md (atenção: D-027, D-028 e D-029 aparecem duplicados)
- Levantamento da E3 (deixou ganchos explícitos para a E4, procure "E4", "funil", "veterin", "fundador"): C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E3_Linha_de_Responsabilidade/F2-E3_Levantamento_v1.md
- Rascunho do colega Bruno para a E4 (seção 4, linhas ~226–487, e seções 6, 9, 12): C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-Material_apoio_consolidado.md

## Dados oficiais (Quadros 15 e 16, conferidos no PDF; confira de novo no cap02_raw.txt)
Quadro 15 — Pesquisa de clima, julho de 2026 (81 respostas de 96). Concordância: Técnico (n=41) / Comercial (n=19) / Demais (n=21)
- "Prometemos ao cliente aquilo que o produto de fato entrega": 22% / 79% / 41%
- "Temos tempo adequado de validação antes de subir para produção": 17% / 68% / 38%
- "Sei a quem escalar um problema ético do produto": 29% / 21% / 24%
- "Minha área é ouvida nas decisões de produto": 34% / 63% / 29%
- eNPS: -31 / +16 / -4. eNPS geral -12. Rotatividade 12 meses: 19% total, 27% time de dados.
Quadro 16 — Backlog (iniciativa | quem pediu | esforço meses-pessoa | receita potencial 12 meses)
- Módulo de risco de crédito para bancos | Comercial | 14 | R$ 8,4 mi
- Expansão da operação para o México | Investidor | 22 | R$ 6,0 mi
- Reescrita do pipeline de dados | Time técnico | 18 | Nenhuma receita direta
- Explicabilidade das decisões do modelo | Regulador e clientes | 9 | Nenhuma receita direta; retenção
- Agente conversacional de triagem | Comercial | 11 | R$ 3,2 mi
- Certificação ISO/IEC 42001 | Jurídico | 7 | Nenhuma receita direta; acesso a contas públicas
- Módulo veterinário | Sócio-fundador | 16 | R$ 2,1 mi
- Total 97 | R$ 19,7 mi. Capacidade de produto e engenharia para novas iniciativas nos próximos 6 meses: 30 meses-pessoa.
Quadro 3: 96 colaboradores (48 técnicos, 22 comercial e CS, 14 produto e design, 12 administrativo). Runway 11,6 meses; queima R$ 1,90 mi/mês; caixa R$ 22,0 mi; ARR R$ 41,2 mi; crescimento 62%; churn 11%.

## Regras inegociáveis
- Não inventar números sobre a Lumis. O que não está no Anexo A ou nas entregas é [não consta]. Conclusão sem quadro que a sustente é [hipótese]. Desenho da equipe é [proposta].
- Citar a origem: [fonte: Cap. 2, Quadro N], [fonte: Cap. 2, seção X], [fonte: F2-E3], [fonte: conta da equipe sobre o Quadro N].
- Pesquisa externa entra só como contexto conceitual ou de mercado, com referência completa (autor, título, veículo, ano, URL quando houver) e rotulada como externa. NÃO pesquisar a Lumis nem as empresas fictícias (Aster Health, Núcleo Saúde Analytics, Vetor Capital, Hospital Vila Ipê, Rede Sanare etc.).
- Toda responsabilidade termina em um CARGO (CEO, CTO, Head of AI Management, Responsável por Dados, Responsável Comercial, Responsável por Produto, DPO), não em área. As entregas da Fase 2 usam cargos sem nome de pessoa no texto final.
- Descrever pessoas e áreas por conduta e fato, sem atribuir intenção ou caráter. Não culpar o comercial nem o técnico.
- Não reproduzir dados pessoais de marca d'água dos PDFs.
- Escreva em português do Brasil.
```

## 3. Prompts de pesquisa, resultados e verificação

### Prompt 1: Transcrição e contas dos Quadros 15 e 16 (frente "dados")

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: transcrição e contas dos Quadros 15 e 16 (sem pesquisa web)
1. Transcreva os Quadros 15 e 16 e as notas abaixo deles a partir do C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/cap02_raw.txt, palavra por palavra, e diga se batem com os dados do bloco de contexto. Registre página/seção.
2. Faça e mostre a memória de cálculo de TODAS as contas úteis, cada uma como achado tipo "calculo":
 - Q15: diferença técnico × comercial em pontos percentuais em cada afirmação; média ponderada da empresa por afirmação (pesos n=41/19/21); taxa de resposta total (81/96) e por grupo, cruzando com o Quadro 3 (técnicos 48; comercial e CS 22; 'demais' = produto e design 14 + administrativo 12 = 26 — verificar se essa correspondência é dada pelo caso ou é inferência); conferir se o eNPS geral -12 é coerente com a média ponderada (-31·41 + 16·19 - 4·21)/81 e dizer se a diferença indica algo; o que a rotatividade de 27% em dados significa em pessoas [não consta o tamanho do time de dados: verificar].
 - Q16: soma de esforço e receita; razão backlog/capacidade; % da capacidade de cada iniciativa; receita por mês-pessoa de cada iniciativa com receita; esforço e receita por quem pediu; esforço das iniciativas sem receita direta; TODAS as combinações de iniciativas inteiras que cabem em 30 meses-pessoa (liste as maximais) com receita somada; impacto de financiar só fatias (descoberta) — diga que o tamanho das fatias [não consta].
 - Ligação com o caixa: runway 11,6 meses e a janela de 6 meses da capacidade; receita potencial 12 meses vs. ARR. Não invente prazo de realização de receita.
3. Liste o que NÃO consta e que a entrega precisa dizer (ex.: quem dos 'Demais' é de produto; tamanho do time de dados; como a capacidade de 30 foi calculada; se a capacidade já desconta o trabalho de governança assumido na E2/E3/E5; quanto custa em meses-pessoa medir erro por grupo, testar suspensão etc.; pesquisa de clima anterior para tendência; rotatividade por área além de dados).
4. Aponte divergências entre capítulos ou entre entregas sobre esses números (ex.: a E3 diz "cerca de uma em cada quatro pessoas sabe a quem escalar" — confira).

Não faça pesquisa web. Use só os arquivos locais.
Não crie nem altere arquivos. Devolva achados atômicos (uma afirmação verificável por achado), com id no formato DADOS-01, DADOS-02...
```

**Resultado obtido:** 37 achados, sem pesquisa web.

Os Quadros 15 e 16 conferem com o PDF em todos os valores. A única diferença é de nome: o enunciado chama o Quadro 16 de "Backlog de iniciativas, esforço e capacidade disponível", e a legenda diz "Backlog de iniciativas acumuladas". No Quadro 15, o técnico fica 57 p.p. abaixo do comercial em "prometemos o que entregamos", 51 p.p. em "tempo de validação" e 29 p.p. em "minha área é ouvida", e o eNPS separa as duas áreas em 47 pontos. "Sei a quem escalar" é baixo nos três grupos (25,8% na média ponderada). O backlog de 97 meses-pessoa é 3,23 vezes a capacidade de 30, e só as três iniciativas sem receita direta já somam 34. A frente listou as 11 combinações maximais de iniciativas inteiras que cabem em 30 meses-pessoa e o que não consta no caso (tamanho do time de dados, composição dos "Demais", origem dos 30 meses-pessoa, tamanho das fatias de descoberta).

**Verificação:** 33 confirmados, 2 parciais e 2 refutados. Os dois refutados mudaram o texto do levantamento. No DADOS-27, a frente dizia que só crédito + explicabilidade + ISO juntava receita e as duas peças de governança; o verificador mostrou que triagem + explicabilidade + ISO (27 meses-pessoa, R$ 3,2 mi) também junta. No DADOS-29, a ISO/IEC 42001 (7) também cabe na faixa de 9 meses-pessoa do 55/30/15, e não só a explicabilidade. Os parciais pediram marcar como [proposta] a classificação "mercado novo" do crédito (DADOS-24) e corrigir uma citação de linha da E5 (DADOS-35). O verificador também apontou que a frente deixou de usar duas frases do Cap. 2 que sustentam a recusa e o pressuposto (seção 2.6, "replicação de um problema em escala maior"; seção 2.5, "sem que ninguém tenha mentido").

### Prompt 2: Diagnóstico nas três camadas de Schein (frente "schein")

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: diagnóstico nas três camadas de Schein com evidência do caso (sem pesquisa web)
Monte o diagnóstico da cultura da Lumis com evidência de TODO o caso (Cap. 1, Cap. 2 inteiro e todos os quadros, Fase 1 e entregas da Fase 2), não só do Quadro 15.
1. ARTEFATOS (o que se vê): processos, estruturas, documentos, números e comportamentos registrados. Ex. a examinar: o painel comercial e o 94% (Q9, Q11); o incidente de 01/2026 'corrigido no sistema; não corrigido no material comercial' (Q14); reclamações mantidas pelo CS e nunca cruzadas com desempenho (Q17); liberação de versão exclusiva do CTO e ausência de comitê (nota do Q12); priorização autorizada pela diretoria comercial do cliente sem aprovação interna (Q12); contratos redigidos com 11 pessoas e não relidos (1.2); backlog com 'quem pediu' por área e pedido do sócio-fundador (Q16); fundadores ex-pesquisadores e decoração com quadros negros de equação (Cap. 1, 1.1–1.2); a própria pesquisa de clima; política de privacidade em elaboração desde 2024 (Q17). Para cada um: o que mostra e a fonte.
2. VALORES DECLARADOS: o que a empresa e cada área dizem valorizar (Declaração de Intenção da Fase 1, C1–C5; discursos do caderno: 'o comercial promete o que o produto não entrega' / 'o técnico atrasa tudo em nome de um rigor que o cliente não pede' (1.2); 2.5). Mostre onde artefato e valor declarado se contradizem (é aí que Schein manda procurar o pressuposto).
3. PRESSUPOSTOS PROFUNDOS: gere pelo menos 4 candidatos, incluindo (a) a leitura literal do capítulo (confiabilidade × velocidade, seção 2.5), (b) um pressuposto COMPARTILHADO pelas duas áreas (ex.: 'a verdade sobre o produto pertence a uma área; ninguém é dono da distância entre o número validado e o desempenho em campo' ou 'qualidade é atributo do modelo verificado uma vez antes de ir a campo'), (c) um ligado a poder/voz ('quem traz receita decide' — Q15 'minha área é ouvida' 34% × 63%; Q12), (d) um ligado à origem acadêmica/fundadores ou ao crescimento rápido (62%) — e outros que achar. Para cada candidato: enunciado em uma frase, evidências a favor (com fonte), evidências contra, o que ele explica que os outros não explicam, e se é [hipótese]. Recomende UM pressuposto profundo central (pode ser composto: um par de crenças de superfície que se apoiam num pressuposto comum), justificando por que é mais profundo que a leitura literal do capítulo, sem contradizê-la.
4. Explique a CADEIA causal (como hipótese marcada): pressuposto → comportamento → artefato → custo (ex.: como o 94% de 2023 virou promessa comercial 'sem que ninguém tenha mentido', 2.5 e 2.3/Goodhart; como isso gerou os 31,8% não detectados pela Lumis). Ligue aos achados das E1 e E2 sem repetir os números deles além do necessário.
5. Diga o que os dados NÃO permitem afirmar (ex.: n=19 do comercial; 'Demais' mistura produto e administrativo; percepção não é fato; correlação ≠ causa).

Não faça pesquisa web. Use só os arquivos locais.
Não crie nem altere arquivos. Devolva achados atômicos (uma afirmação verificável por achado), com id no formato SCHEIN-01, SCHEIN-02...
```

**Resultado obtido:** 54 achados, sem pesquisa web.

A frente reuniu pelo menos 14 artefatos do caso. O padrão comum é um número medido uma vez, em condição favorável, que segue em uso sem nova medição (94% de 2023, NPS com 9 respondentes, piloto sem grupo de controle), e uma correção que para no sistema e não chega ao material comercial (incidente de 01/2026). Avaliou 8 candidatos a pressuposto e recomendou um pressuposto composto e compartilhado pelas duas áreas: o desempenho é tratado como atributo do modelo, provado no conjunto de validação, e ninguém é dono da distância entre esse número e o desempenho em campo, por grupo. A cadeia que vai do pressuposto ao custo ficou marcada como hipótese.

**Verificação:** 48 confirmados e 6 parciais. As correções mais importantes atingiram a formulação central. O incidente de 09/2025 foi detectado pela equipe interna em 6 dias, então existe monitoramento em produção, só que no agregado. Por isso "provado uma vez" virou "provado na média" (SCHEIN-26, SCHEIN-38). Como só 22% do técnico concorda que a promessa corresponde à entrega, o que as áreas compartilham é a falta de dono e de fórum para o erro por grupo, e não a crença no número. Os compromissos da Declaração de Intenção saíram da camada de valores declarados, porque foram escritos pela própria equipe semanas antes e usá-los ali seria circular (SCHEIN-25, SCHEIN-28). O verificador também tirou o Quadro 12 como evidência de poder do comercial da Lumis (SCHEIN-33) e confirmou que as decisões D-027 a D-029 já tinham sido renumeradas pela D-033.

### Prompt 3: Base conceitual e casos reais sobre cultura (frente "conceitos_cultura")

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: base conceitual e casos reais sobre cultura e conflito técnico × comercial (COM pesquisa web)
Levante referências verificáveis (abra as páginas; prefira fontes primárias, editoras, periódicos, HBR, MIT Sloan, sites oficiais):
1. Edgar Schein, Organizational Culture and Leadership (5. ed., 2016/2017, Wiley; com Peter Schein): definição das três camadas (artifacts, espoused beliefs and values, basic underlying assumptions); a ideia de que a mudança cultural não vem de comunicados; os 'primary embedding mechanisms' (o que os líderes prestam atenção, medem e controlam; reação a incidentes críticos; alocação de recursos; recompensas e status; recrutamento/promoção) e 'secondary articulation and reinforcement mechanisms' (estrutura, sistemas e procedimentos, rituais, espaço, histórias, declarações formais). Confirme a lista exata e onde aparece (capítulo/edição) com fonte acessível. Também o conceito de subculturas ocupacionais (operator/engineering/executive), do artigo Schein (1996) 'Three Cultures of Management: The Key to Organizational Learning', MIT Sloan Management Review — confirme dados bibliográficos e o conteúdo.
2. Goodhart e a 'lei de Campbell' sobre metas e indicadores (o capítulo já cita Goodhart 1975): referência correta da formulação 'when a measure becomes a target...' (Strathern 1997) — confirme.
3. Segurança psicológica (Amy Edmondson, 1999, Administrative Science Quarterly, 'Psychological Safety and Learning Behavior in Work Teams'; e/ou The Fearless Organization, 2018): o que diz e por que importa para a afirmação 'sei a quem escalar um problema ético' — confirme.
4. Evidência sobre o conflito entre vendas/marketing e engenharia/produto: ex. Kotler, Rackham & Krishnaswamy (2006) 'Ending the War Between Sales and Marketing', HBR; literatura sobre conflito marketing–P&D (ex.: Gupta, Raj & Wilemon 1986, Journal of Marketing); confirme.
5. Casos REAIS de IA em saúde em que a promessa comercial/divulgação passou à frente da validação em campo, para usar como análogo rotulado: ex. Epic Sepsis Model (Wong et al. 2021, JAMA Intern Med — já usado na F1 e E1); IBM Watson for Oncology (reportagens STAT 2017/2018 sobre recomendações inseguras e marketing); Babylon Health (alegações sobre o chatbot e críticas na The Lancet 2018); FTC e alegações de IA ('Operation AI Comply', 2024; orientações da FTC sobre 'keep your AI claims in check', 2023). Para cada um: o que aconteceu, fonte, data, e qual paralelo com a Lumis (cultural, não técnico). Não force paralelos.
6. Se achar, evidência sobre mecanismos que reduzem esse conflito em empresas de tecnologia (ex.: 'claims review'/revisão de alegações por jurídico e produto; model cards — Mitchell et al. 2019, FAT*; 'go/no-go' conjunto; métricas compartilhadas).
Cada referência: autor, título, veículo, ano, URL aberta, e o trecho/afirmação exata que sustenta. Marque como fato_externo ou conceito. Se não conseguir abrir a fonte, diga.

Use WebSearch e WebFetch (carregue com ToolSearch "select:WebSearch,WebFetch" se necessário). Abra cada fonte antes de citá-la. Registre as buscas.
Não crie nem altere arquivos. Devolva achados atômicos (uma afirmação verificável por achado), com id no formato CONCEITOS_CULTURA-01, CONCEITOS_CULTURA-02...
```

**Resultado obtido:** 23 achados com 17 buscas na web.

A frente conferiu a referência de Schein (5ª ed., Edgar e Peter Schein, Wiley, 2017, enquanto o capítulo cita 2016), as três subculturas de Schein (1996, MIT SMR), a formulação de Strathern (1997) para a lei de Goodhart, a lei de Campbell, a definição de segurança psicológica de Edmondson (1999) e o artigo de Kotler, Rackham e Krishnaswamy (2006). Como análogos externos rotulados, trouxe o modelo de sepse da Epic, o Watson for Oncology, a Babylon e a Operation AI Comply da FTC, e os model cards (Mitchell et al., 2019) como mecanismo. A lista de mecanismos primários e secundários de Schein só foi conferida em fonte secundária.

**Verificação:** 16 confirmados e 7 parciais. A lista dos seis mecanismos primários deve ser citada como Schein (2009, p. 98), via NCSU, e não como 5ª edição. Os números de capítulo da 5ª edição não vieram na página aberta e ficam [não verificado]. Foram corrigidas a citação literal da HBR (CONCEITOS_CULTURA-13), a expressão "hundreds of US hospitals" do caso Epic (-15) e a autoria de Atleson no blog da FTC, cuja página não existe mais (-20). O uso dos model cards foi reclassificado: um documento é mecanismo secundário e só muda cultura se estiver ligado ao que a liderança mede e recompensa (-21). As críticas pediram um pressuposto próprio da equipe, base conceitual para o funil e para a proporção, e um conceito que sustente recusar um pedido do sócio-fundador.

### Prompt 4: Desenho das duas intervenções (frente "intervencoes")

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: desenho das duas intervenções sobre o conflito técnico × comercial (pesquisa web permitida para sustentar mecanismos)
O enunciado exige DUAS intervenções concretas, cada uma com RESPONSÁVEL (cargo), PRAZO e SINAL OBSERVÁVEL de que funcionou. Critério: viabilidade.
1. Gere pelo menos 5 candidatas, cobrindo mecanismos diferentes de Schein (o que se mede/controla, reação a incidentes, alocação de recursos, recompensas, estrutura/rituais/procedimentos). Ideias a avaliar (não se limite): (a) regra única de prova: nenhuma afirmação pública, proposta comercial ou liberação de versão sem número de campo por subgrupo aprovado — liga ao indicador 'afirmações públicas auditáveis' da E2 e à etapa 'Aprovar os números divulgados ao mercado' da E3 (Head of AI Management aprova, Responsável Comercial corrige); (b) revisão conjunta quinzenal técnico+comercial+CS do desempenho por grupo e das reclamações (o C2 já prevê leitura quinzenal; E3/E5 também); (c) metas/variável compartilhada (ex.: parte da remuneração comercial ligada a retenção/erro em campo) — avalie o risco Goodhart; (d) pares técnico-comercial em contas/implementação e participação do técnico nas propostas; (e) rito de revisão pós-incidente sem culpa com as duas áreas; (f) definição pública do 'tempo de validação' como parte do produto com prazo fixo (SLA interno) para tirar o argumento de 'atraso indefinido'; (g) dar voz ao técnico no portão de portfólio (Q15 'minha área é ouvida' 34%).
2. Para cada candidata: qual camada/pressuposto ataca, mecanismo de Schein, responsável (um cargo; coerente com a E3), prazo (proposta, coerente com prazos já assumidos: teste de suspensão em 30 dias na E3; contratos 12/2026 e 03/2027; 60 dias do Vetor; pesquisa de clima de julho 2026), custo em capacidade (o que consome dos 30 meses-pessoa — se não consta, diga), sinal observável com linha de base do Quadro 15/14/11/17 e meta proposta (ex.: diferença técnico×comercial em 'prometemos o que entregamos' de 57 p.p. para X; 'sei a quem escalar' de ~26% para X; zero afirmação pública sem auditoria; reclamações cruzadas com desempenho todo mês), riscos e como pode falhar, evidência externa de que funciona (com URL aberta) ou [hipótese].
3. Recomende as DUAS melhores, de mecanismos diferentes e que se complementem (uma que mude o que se mede/promete e outra que mude quem decide/como se conversa, por exemplo), justificando. Diga por que as outras ficaram de fora. Aponte o que é coerente ou conflita com E2, E3, E5 e C1–C5. Lembre: Schein diz que comunicado interno não resolve pressuposto; o capítulo diz que ninguém leva a conversa 'para uma sala onde ela poderia ser resolvida' (1.2).
4. Sinais observáveis precisam ser medíveis com o que a Lumis tem ou passará a ter; atenção ao tamanho pequeno do comercial (n=19) e à repetição da pesquisa (quando? proposta).

Use WebSearch e WebFetch (carregue com ToolSearch "select:WebSearch,WebFetch" se necessário). Abra cada fonte antes de citá-la. Registre as buscas.
Não crie nem altere arquivos. Devolva achados atômicos (uma afirmação verificável por achado), com id no formato INTERVENCOES-01, INTERVENCOES-02...
```

**Resultado obtido:** 34 achados com 8 buscas na web.

A frente avaliou oito candidatas e recomendou duas. A primeira é a regra única de prova: nenhum número sai para o mercado, para proposta ou para contrato sem o número de campo por grupo aprovado pelo Head of AI Management, com o Responsável Comercial corrigindo o material. A segunda é uma mesa de campo quinzenal com técnico, comercial, CS e produto, dona do Responsável por Produto, que cruza reclamações com desempenho e fixa o prazo de validação. Ficaram de fora a remuneração variável ligada ao erro (risco de Goodhart e de fugir de clientes com pacientes de CEP D/E), os pares técnico-comercial e a mudança de contratação e promoção. Os sinais misturam comportamento contável e uma pesquisa curta em 01/2027.

**Verificação:** 20 confirmados, 13 parciais e 1 não confirmado. O não confirmado é a lista completa de mecanismos de Schein (INTERVENCOES-09), que não foi lida em fonte aberta. As correções principais: a pesquisa de clima é quase um censo, então a margem de ±18 p.p. no comercial não se sustenta, e o argumento que fica é "uma pessoa vale cerca de 5,3 p.p." (-04). A Prisma é fornecedora de dados, e não cliente da triagem (-10). A meta sobre a diferença técnico × comercial poderia ser cumprida com a cultura piorando, então passou a mirar a subida do técnico (-11). A mesa e o Head of AI Management apareciam como donos da mesma decisão sobre o que se promete, e o verificador pediu separar quem propõe, quem decide e quem confere (-15, -28). O caso Workado é ordem proposta, e não final (-13); a frase do DORA é de John Shook (-19). O item P-1 sobre a E5 estava superado (-31).

### Prompt 5: Funil de inovação e critérios (frente "funil")

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: funil de inovação e critérios de entrada, avanço e encerramento (COM pesquisa web para a base conceitual)
1. Base conceitual verificável (abra as fontes): Stage-Gate de Robert G. Cooper (ex.: 'Stage-Gate Systems: A New Tool for Managing New Products', Business Horizons, 1990; critérios must-meet × should-meet; 'kill' em cada portão); 'Three Horizons' (Baghai, Coley & White, The Alchemy of Growth, 1999, McKinsey) e 'Managing Your Innovation Portfolio' (Nagji & Tuff, HBR, maio 2012, proporção 70-20-10 e o retorno observado); critérios de encerramento/kill criteria (ex.: Annie Duke, Quit, 2022, 'kill criteria'; ou literatura de portfólio); financiamento por etapa ('metered funding', ex.: Ries, The Lean Startup / The Startup Way, ou Intuit/Amazon); e gestão de risco de IA no ciclo de vida (NIST AI RMF 1.0, 2023, funções Govern/Map/Measure/Manage; ISO/IEC 42001:2023 e avaliação de impacto). Para cada uma: referência completa, URL aberta e o que sustenta.
2. Proponha o funil da Lumis [proposta] com 4 ou 5 etapas (ex.: entrada/triagem → descoberta → piloto em modo sombra → produção limitada → escala), e para CADA etapa: critério de ENTRADA, critério de AVANÇO e critério de ENCERRAMENTO explícitos e verificáveis, quem decide (cargo; coerente com o 'portão de entrada' da E3: Responsável por Produto leva o pedido, CEO decide, Head of AI Management e DPO dão parecer obrigatório; modo sombra; responsável do domínio; suspensão testada antes de entrar), e quanto de capacidade a etapa pode consumir antes de nova decisão (orçamento por etapa — o tamanho [não consta], proponha regra).
3. Os critérios devem embutir as condições já assumidas: E1 (foco em hospitais e seguradoras médios; o fosso a construir é dado com direito de uso limpo e prova auditável de desempenho por subgrupo; dependências de fornecedor), E2 (indicadores; nada de métrica que não sobrevive a auditoria; erro por grupo), E3 (portão, modo sombra, responsável de domínio, revisão humana), E5 (seis condições para expansão; indicador E4 de representatividade; dado de saúde fora do crédito; métrica pública), C1–C5. Inclua critério de 'quem pediu não decide' (o pedido do sócio-fundador, do investidor e do comercial passam pelo mesmo portão).
4. Inclua critérios de encerramento duros (ex.: estourou o orçamento da etapa sem evidência nova; erro por grupo acima do limite no modo sombra por N ciclos; direito de uso do dado não obtido até data X; responsável de domínio não nomeado; dependência nova de fornecedor sem alternativa) e regra para reabrir.
5. Ligue o funil ao conflito cultural: mostre como o MESMO critério de prova serve para o que o comercial pode prometer e para o que avança no funil (tese 'critério compartilhado' do enunciado).
6. Diga o que é [proposta], [hipótese] e [não consta]. Evite pontuação numérica (scores) sem memória de cálculo — o rascunho do Bruno alerta para isso.

Use WebSearch e WebFetch (carregue com ToolSearch "select:WebSearch,WebFetch" se necessário). Abra cada fonte antes de citá-la. Registre as buscas.
Não crie nem altere arquivos. Devolva achados atômicos (uma afirmação verificável por achado), com id no formato FUNIL-01, FUNIL-02...
```

**Resultado obtido:** 40 achados com 13 buscas na web.

A frente conferiu Cooper (1990), Nagji e Tuff (HBR, 2012), o NIST AI RMF 1.0 e, por fontes secundárias, Duke (2022), Ries (2017), os Três Horizontes e a ISO/IEC 42001. Propôs um funil de cinco etapas (Entrada, Descoberta, Modo sombra, Produção limitada, Escala), cada uma com critério de entrada, avanço e encerramento e decisor com cargo, usando o portão da E3. O financiamento é por etapa (até 10% do esforço na Descoberta e mais 30% no Modo sombra, valores [proposta]). Duas regras novas: quem pediu não decide, e o que o comercial pode prometer fica amarrado à etapa em que a iniciativa está.

**Verificação:** 25 confirmados e 15 parciais. Nas fontes, o verificador corrigiu atribuições: o go/no-go explícito do NIST está na lista de benefícios esperados, e não no GOVERN (FUNIL-17); "estado e data" é síntese de fonte secundária, e não de Duke (-15); must-meet e should-meet não vêm de Cooper (-11); os Três Horizontes devem ser citados pelo livro (-14). No desenho, a regra "quem pediu não decide" conflitava com a E3, porque a DPO (Jurídico, que pediu a ISO) e o CTO têm papel obrigatório no portão (-23). A escada de promessa invertia o papel da E3: quem aprova é o Head of AI Management (-31). O avanço do modo sombra passou a exigir razão de até 1,5 e dado de desfecho disponível (-25), e a produção limitada ganhou a autorização da CEO por cliente e a condição 1 da E5 (-26). A crítica principal: travar no funil é adiar, e o enunciado pede uma recusa explícita (-35).

### Prompt 6: Classificação do backlog, distribuição e recusa (frente "portfolio")

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: classificação do backlog por horizonte, distribuição dos 30 meses-pessoa e recusa (sem pesquisa web)
1. Classifique as 7 iniciativas do Quadro 16 em melhoria do produto atual / expansão adjacente / aposta de transformação, com justificativa e grau de certeza; aponte as ambíguas (ex.: ISO/IEC 42001 é melhoria de governança ou acesso a contas públicas = adjacente? crédito é segmento já atendido — 5 bancos, 31 mil decisões/mês, Q3 e Q12 — então é melhoria ou adjacência? agente conversacional de triagem é nova decisão automatizada de alto impacto na mesma área em que o falso negativo chega a 31,8%; o México é mesmo produto em geografia nova; o veterinário é domínio novo; a 'plataforma' que o Vetor propõe (1.1) NÃO está no backlog — diga isso).
2. Avalie cada iniciativa contra os critérios das entregas anteriores: E1 (foco em clientes médios; fosso = dado com direito de uso limpo + prova por subgrupo; dependência de fornecedor; Aster), E2 (contratos frágeis Vila Ipê/Prisma; indicadores; restrição para 60+ CEP C e D/E; revisão 10%), E3 (portão; modo sombra; responsável de domínio; 'o portão precisa conseguir recusar até um pedido do fundador'; explicabilidade dá conteúdo à revisão humana — ver levantamento da E3), E5 (seis condições; dado de saúde fora do crédito; México e crédito analisados; E4 de representatividade). Para cada: decisão recomendada (financiar inteira / financiar só a descoberta / condicionar / adiar / recusar), com motivo e fonte.
3. Monte 3 cenários de distribuição dos 30 meses-pessoa em 6 meses, com as contas: (A) 'consertar primeiro' (melhoria máxima), (B) 'equilíbrio com receita' e (C) um cenário que respeite uma proporção de referência externa (ex.: 70-20-10 de Nagji & Tuff, citada só como referência, ou 55/30/15 do rascunho do Bruno). Mostre que proporções fixas esbarram na granularidade das iniciativas (ex.: 30% = 9 MP e a menor adjacente pede 11) e proponha a saída: financiar por etapa (descoberta/fatia) — o tamanho das fatias [não consta], então trate como [proposta]. Para cada cenário: receita potencial em 12 meses que fica em jogo, risco que resolve e que deixa aberto, efeito no runway de 11,6 meses (sem inventar), e coerência com as condições do Vetor. Recomende um, com a proporção final e justificativa em 3–4 frases.
4. Recusa: avalie candidatos a recusar (veterinário; agente de triagem; México nas condições atuais; outros) com argumentos a favor e contra, incluindo o custo político (sócio-fundador; investidor; comercial) e o que mostraria coragem e disciplina sem parecer arbitrário. Recomende pelo menos uma recusa firme e diga o que precisaria mudar para reabrir. Diferencie 'recusar' de 'adiar' e de 'condicionar'.
5. Aponte o que a entrega deve declarar como [não consta] (ex.: se a capacidade inclui a restrição e os indicadores já assumidos; prazo para a receita; custo de oportunidade).

Não faça pesquisa web. Use só os arquivos locais.
Não crie nem altere arquivos. Devolva achados atômicos (uma afirmação verificável por achado), com id no formato PORTFOLIO-01, PORTFOLIO-02...
```

**Resultado obtido:** 47 achados, sem pesquisa web.

A frente classificou as sete iniciativas por horizonte e apontou as ambíguas (ISO/IEC 42001, crédito, agente de triagem). Mostrou que proporções fixas não fecham com iniciativas inteiras e que o backlog não tem nenhuma linha para corrigir o viés nem para cumprir os compromissos já assumidos. Montou três cenários (consertar primeiro; equilíbrio com receita, com 30 meses-pessoa exatos e R$ 8,4 mi em jogo; e o 55/30/15 do rascunho). Recomendou cerca de 2/3 em melhoria, 1/3 em adjacência financiada por etapa e zero em transformação neste ciclo, com recusa firme do módulo veterinário, adiamento do agente de triagem e o México condicionado às condições da E5.

**Verificação:** 41 confirmados e 6 parciais. O verificador corrigiu a leitura do rascunho do colega: os 15% de transformação iam para "plataforma e governança", e não para o veterinário (PORTFOLIO-23, -46). A regra da ISO estava incoerente entre melhoria e adjacência e precisa ser fixada numa tabela só (-25). O número de 30% de redução no tempo de triagem não é citado na E2 e deve ser atribuído ao Quadro 11 (-31). O condicionamento do México passou a ser justificado por critério, e não por evitar atrito com o investidor (-37). A referência a Nagji e Tuff ficou como contexto externo sem citação literal (-45). As críticas pediram critérios de encerramento por iniciativa, a ligação da distribuição com o pressuposto cultural e o que o comercial ganha com a proposta.

### Prompt 7: Coerência com a história, as entregas e os compromissos (frente "coerencia")

**Prompt** (precedido do bloco comum da seção 2):

```text
## Tarefa: coerência com a história, as entregas e os compromissos (sem pesquisa web)
1. Monte a lista completa de GANCHOS que a E4 precisa honrar, com citação exata: o que E1, E2, E3 e E5 (e seus levantamentos, decisões D-009, D-020, D-023 a D-029 em DECISOES.md) dizem que 'fica para a Entrega 4' ou que a E4 precisa respeitar (ex.: E3: 'Os critérios de entrada e de encerramento ficam no funil da Entrega 4'; levantamento da E3: 'o portão precisa conseguir recusar até um pedido do fundador', Comitê de Risco e Ética 'semente para a E4 e a Fase 4', 'Governança consome capacidade, e o memorando precisa dizer isso', explicabilidade e ISO como 'alavanca de priorização para a E4'; E2 levantamento: 'A explicação estrutural vem de Goodhart e fica para a F2-E4').
2. Liste cargos e papéis já fixados pela E3 (tabela 'Quem responde por cada etapa') que a E4 deve usar sem contradizer, e os prazos/limites já assumidos (48 h, quinzenal, 30 dias para testar suspensão, 10% de revisão, contratos 12/2026 e 03/2027, métrica pública trimestral).
3. Checagem contra C1–C5 (Declaração de Intenção da Fase 1): para cada compromisso, como a E4 o reforça ou poderia contradizê-lo (ex.: financiar receita antes de explicabilidade conflita com C1? recusar a reescrita do pipeline conflita com C2/C5?). E contra D-005 (priorizar a segurança dos afetados).
4. O que o memorando ao conselho (F2-M: direção, riscos assumidos, condições prévias) e o documento integrado (F2-D, cinco entregas 'articuladas entre si') precisam receber da E4. E sementes para as Fases 5 (O Produto: escopo, roadmap, critérios de sucesso), 6 (As Pessoas: metade do time com medo de ser substituída; transformação liderada, não anunciada) e 7 (Julgamento: coerência cobrada).
5. Padrão de formato das entregas da Fase 2 (veja E1/E2/E3/E5): conclusão no início, 4 páginas, seções curtas, figuras e tabelas, sem códigos internos (D-XX, C1–C5, FX-EY) no texto entregue — os compromissos aparecem pelo nome; cargos sem nome de pessoa; referências externas poucas. Proponha a estrutura do .docx da E4 nesse padrão, com figuras sugeridas (ex.: gráfico de barras pareadas do Q15; barra empilhada do backlog vs capacidade; diagrama do funil).
6. Aponte riscos de contradição entre o rascunho do Bruno (seção 4 do material consolidado) e as entregas já feitas, e problemas no rascunho (ex.: scores sem memória de cálculo, 'Gate único' vs. portão da E3, 55/30/15 vs granularidade, crédito 'avançar' vs. cautela da E5).
7. Note problemas de organização que encontrar (ex.: DECISOES com IDs duplicados; ESTADO desatualizado) — só reporte.

Não faça pesquisa web. Use só os arquivos locais.
Não crie nem altere arquivos. Devolva achados atômicos (uma afirmação verificável por achado), com id no formato COERENCIA-01, COERENCIA-02...
```

**Resultado obtido:** 71 achados, sem pesquisa web.

A frente listou os ganchos que a E4 precisa honrar: os critérios de entrada e encerramento que a E3 deixou para o funil, o portão que precisa conseguir recusar um pedido do sócio-fundador, o comitê de risco e ética como semente que só dá parecer, a governança que consome capacidade, a explicação pela lei de Goodhart que a E2 deixou para a E4, as condições da E5 e o que a E1 manda construir. Fixou os cargos e prazos que a E4 não pode contradizer, checou a proposta contra os cinco compromissos e contra a D-005 e apontou problemas numéricos no rascunho do colega (9 meses-pessoa de adjacência contra 47 pedidos; 48 meses-pessoa marcados para avançar contra 30). Também propôs a estrutura do .docx e registrou problemas de organização da pasta.

**Verificação:** 59 confirmados e 12 parciais. A correção mais importante foi no pressuposto: "não existe instância nem critério" descreve uma ausência estrutural, que em Schein é artefato, e não uma crença; o pressuposto precisa ser escrito como crença tácita comum às duas áreas (COERENCIA-30). A primeira condição da E5 foi citada sem a cláusula "com a recomendação automática já restrita nos subgrupos acima dele", o que mudava a leitura sobre quando o crédito e o México podem gerar receita (-11, -13). Outras correções: a D-034 não traz a regra sobre o comitê, que está só no levantamento da E3 (-20); o rascunho do colega não propõe nota ponderada (-28); a ISO cabe nos 9 meses-pessoa se for contada como adjacente (-39); o escopo do agente de triagem é hipótese (-09). O verificador confirmou que o ESTADO.md está desatualizado e que as decisões duplicadas já tinham sido renumeradas.

## 4. Prompts de verificação, síntese e crítica

### Verificação adversarial (modelo)

Cada frente teve um verificador com o prompt abaixo. O bloco comum da seção 2 entra logo depois da primeira linha. A lista de achados da frente entra no lugar de `<lista>`.

```text
Você é verificador independente e cético de uma due diligence acadêmica. Sua função é REFUTAR, não confirmar. Na dúvida, marque "nao_confirmado".

[bloco comum da seção 2]

## Achados da frente "<frente>" a verificar
{
 "achados": "<lista>"
}

## Como verificar
- dado_anexo: confira contra C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/9a5aa094-89af-4f60-a523-15120823ee88/scratchpad/ctx/cap02_raw.txt (e cap01_raw.txt / arquivos das entregas), palavra por palavra e número por número.
- calculo: refaça a conta. Qualquer divergência = "refutado" com o valor correto em "correcao".
- fato_externo e conceito: abra a URL (WebFetch; carregue com ToolSearch "select:WebSearch,WebFetch") e confirme se a fonte diz exatamente isso (autor, ano, veículo, número, trecho). Afirmação mais forte que a fonte = "parcial" com correção. URL que não abre: procure a mesma informação em outra fonte primária; se não achar, "nao_confirmado".
- hipotese e proposta: avalie se está marcada como tal, se é razoável e se contradiz algum dado do caso, alguma entrega anterior (E1, E2, E3, E5) ou os compromissos C1–C5. Proposta incoerente = "parcial" com a correção.
- coerencia e lacuna: confira a citação no arquivo indicado; se o item 'não consta' na verdade consta em algum lugar, "refutado".
Verifique TODOS os ids. Em "criticas_gerais", aponte o que a frente deixou de fora ou tratou de forma rasa, pensando nos critérios do enunciado (profundidade do pressuposto, viabilidade das intervenções, qualidade dos critérios, coragem de recusar, coerência entre entregas). Não crie nem altere arquivos.
```

### Síntese, crítica e revisão (resumidos)

Os textos completos destes três prompts não estão no JSON bruto. Fica aqui só o que cada etapa fez.

- **Síntese:** reuniu os achados confirmados e parciais das sete frentes, com as correções dos verificadores, no levantamento da entrega, seguindo a skill humanizer (SKILL.md e PT-BR.md).
- **Crítica em três lentes:** leu o levantamento como o professor que corrige, como um conselheiro da Lumis e como um analista do Vetor Capital.
- **Revisão:** incorporou ao levantamento os pontos da crítica.
