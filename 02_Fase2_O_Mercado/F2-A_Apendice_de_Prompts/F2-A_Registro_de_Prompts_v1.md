# F2-A: Registro de Prompts da F2-E1 (Mapa do Território), v1

**Data de execução:** 05/10/2026 · **Ferramenta:** Claude Code (modelo Claude Opus 5.5), com subagentes de pesquisa usando WebSearch e WebFetch
**Exigência do enunciado:** *"Use inteligência artificial generativa como instrumento de pesquisa nesta entrega e documente pelo menos dois prompts utilizados, o resultado obtido e a verificação que você fez das informações antes de incorporá-las. Pesquisa não checada não é pesquisa."* [fonte: Cap. 2, Entrega 1]

## 1. Método

A pesquisa passou por cinco etapas:
1. **Pesquisa.** Cinco frentes rodaram em paralelo, uma para cada tópico do enunciado e mais uma de análise quantitativa. Cada frente teve um subagente próprio e o mesmo bloco de contexto e regras (seção 2).
2. **Verificação adversarial.** Para cada frente, um segundo subagente independente recebeu a instrução de tentar **refutar** cada achado: reabrir as URLs, conferir números e datas e refazer as contas. Só entram no levantamento os achados que ficaram "confirmado" ou "parcial", estes com a correção do verificador.
3. **Síntese.** Os achados verificados foram integrados por tópico do enunciado.
4. **Crítica de completude.** Um agente fez o papel de professor avaliador e analista do fundo e apontou as 3 lacunas mais importantes.
5. **Lacunas e síntese final.** Três subagentes pesquisaram as lacunas, e uma síntese final incorporou o resultado.

Ao todo foram 16 subagentes, 514 chamadas de ferramenta e cerca de 1,4 mi de tokens.

**Verificação humana (Head of AI Management)**, feita depois da execução:
- Quadro 7 conferido contra o PDF do Cap. 2 (fontes, volumes, autorização e vencimentos).
- Contas centrais refeitas: margem com inferência +100% = 39,5%; cenário combinado = 29,6%; crescimento anual do mercado = 17,4%; meta de 5% em 2029 = 60,4% ao ano.

> **Pendente antes da entrega:** abrir pessoalmente as URLs das afirmações que forem para o texto final, no mínimo as citadas na seção 0 do levantamento, e registrar a conferência na coluna "Verificação humana" da seção 5.

## 2. Bloco comum de contexto e regras (incluído em todos os prompts de pesquisa)

```text
Você é analista sênior de estratégia de IA aplicada à saúde, com experiência em due diligence para fundos de venture capital no Brasil.

## Contexto
Você apoia o Head of AI Management da Lumis Intelligence, empresa FICTÍCIA criada para um curso de Gestão em IA (FIAP). A Lumis vende o Lumis Insight, sistema de IA preditiva para priorização clínica (hospitais) e classificação de risco (seguradoras e bancos) no Brasil. Ela opera na camada de aplicação, usando modelos fundacionais de terceiros com ajustes próprios. O fundo Vetor Capital propõe aporte de R$ 120 mi e exige em 60 dias uma tese de crescimento defensável. Uma multinacional fictícia (Aster Health) acaba de anunciar entrada no Brasil com módulo de priorização embutido em sistema hospitalar já instalado. Data de hoje: 05/10/2026.

## Dados oficiais da Lumis (única fonte permitida sobre a empresa)
### Quadro 3 — Porte da empresa (fechamento do 2º tri/2026)
- Fundação: 2022
- Clientes ativos: 38 contas (24 hospitais e clínicas, 9 seguradoras, 5 bancos)
- ARR: R$ 41,2 milhões
- Ticket médio anual por cliente: R$ 1,084 milhão
- Crescimento de receita (12 meses): 62%
- Churn anual de contas: 11%
- Colaboradores: 96 (48 técnicos, 22 comercial e CS, 14 produto e design, 12 administrativo)
- Margem bruta: 58%
- Custo direto mensal: R$ 1,44 milhão
- Queima de caixa mensal: R$ 1,90 milhão
- Caixa disponível: R$ 22,0 milhões
- Runway: 11,6 meses
- Proposta Vetor Capital: R$ 120 milhões por 22% (pré-money R$ 425,5 milhões, cerca de 10,3x o ARR), válida por 60 dias.

### Quadro 4 — Custos e câmbio (custo direto mensal)
| Item | Moeda | Valor mensal | % do custo direto |
| Inferência em modelos fundacionais (fornecedor externo) | USD | US$ 118.000 = R$ 637.200 | 44,3% |
| Infraestrutura de nuvem | USD | US$ 74.400 = R$ 401.760 | 27,9% |
| Equipe técnica dedicada a contas | BRL | R$ 289.000 | 20,1% |
| Licenças de bases clínicas de referência | BRL | R$ 112.040 | 7,8% |
| Total | — | R$ 1.440.000 | 100% |
Câmbio: R$ 5,40/US$. 72,2% do custo direto em moeda estrangeira; 100% da receita em reais.

### Quadro 5 — Cadeia de fornecimento
| Camada | Fornecedor | Situação contratual | Risco identificado |
| Modelos fundacionais | Fornecedor único, contrato de consumo | Sem compromisso de preço; termos revisáveis a qualquer tempo com aviso de 30 dias | Preço caiu 38% em 18 meses, mas o fornecedor anunciou módulo próprio para saúde |
| Infraestrutura de nuvem | Provedor global, plano anual | Renovação em 04/2027, desconto por compromisso de volume | Migração estimada em 7 meses de trabalho técnico |
| Bases clínicas de referência | Consórcio setorial | Licença anual, renovação automática | Reajuste indexado, sem teto contratual |
| Dados de clientes | 38 contratos individuais | Ver Quadro 7 (Composição da base de dados e contratos) | Dois dos maiores contratos têm cláusula frágil ou silente quanto a treinamento |

### Quadro 6 — Participantes e tamanho de mercado (IA aplicada à saúde no Brasil)
| Participante | Origem | Proposta | Presença no Brasil | Preço médio anual |
| Lumis Intelligence | Brasil | Priorização clínica e classificação de risco por IA preditiva | 38 contas | R$ 1,084 mi |
| Aster Health | EUA | Sistema hospitalar completo com módulo de IA embutido | 210 hospitais usam o sistema; módulo de IA lançado em 2026 | Módulo: + R$ 340 mil sobre o contrato existente |
| Núcleo Saúde Analytics | Brasil | Painéis e BI hospitalar, sem IA preditiva | 74 contas | R$ 420 mil |
| Consultorias e integradores | Brasil | Projetos sob medida, entrega por escopo | Presença difusa | R$ 1,5 mi a R$ 4,0 mi por projeto |
| Provedores de modelo fundacional | Global | Capacidade genérica vendida por consumo | Acesso direto por qualquer empresa | Preço por volume processado, em queda |
Mercado endereçável no Brasil (IA aplicada à gestão clínica e de risco): R$ 2,1 bilhões em 2026, projeção de R$ 3,4 bilhões em 2029. A Lumis detém cerca de 2%.

### Contexto narrativo do Cap. 2 (fatos da história)
- O time técnico usa modelos de terceiros com ajustes próprios; o ativo próprio é a base histórica construída em 4 anos com dados de clientes; os contratos que autorizam esse uso foram redigidos quando a empresa tinha 11 pessoas.
- Os provedores de modelos fundacionais reduziram preços novamente: bom para o custo, ruim para a barreira de entrada.
- A Aster Health anunciou entrada no Brasil com módulo de priorização embutido em sistema hospitalar já instalado em boa parte dos clientes que a Lumis pretendia conquistar.

## Regras inegociáveis
1. NÃO invente números sobre a Lumis. Todo dado da Lumis vem dos quadros acima; cite "Quadro N". Se algo não está nos quadros, escreva "informação indisponível".
2. Lumis, Aster Health, Núcleo Saúde Analytics e Vetor Capital são fictícios. NÃO procure por eles na web. Procure ANÁLOGOS REAIS e rotule-os como análogos.
3. Todo fato externo precisa de fonte verificável (título, organização/autor, data, URL) que você efetivamente abriu. Prefira fontes primárias (documento oficial, relatório, página do fornecedor, artigo revisado) e publicações de 2023–2026. Não cite de memória: se não conseguiu abrir a fonte, classifique como "hipotese".
4. Separe explicitamente: fato_externo (com fonte), dado_anexo (dos quadros), calculo (mostre a conta) e hipotese (inferência sua, não comprovada).
5. Use WebSearch e WebFetch. Se não estiverem carregadas, carregue com ToolSearch ("select:WebSearch,WebFetch"). Faça várias buscas, inclusive em português.
6. Responda em português do Brasil. Seja específico e conciso; nada de generalidades.
```

## 3. Prompts de pesquisa, resultados e verificação

### Prompt 1: Camadas do mercado de IA

**Prompt** (precedido do papel *"Você é analista sênior de estratégia de IA aplicada à saúde, com experiência em due diligence para fundos de venture capital no Brasil"* e do bloco comum da seção 2):

```text
## Tarefa: camadas do mercado de IA e o que a Lumis controla em cada uma
Mapeie, com evidência pública recente, as quatro camadas da cadeia de IA relevantes para uma empresa de aplicação em saúde: (a) infraestrutura de computação e nuvem, (b) modelos fundacionais, (c) aplicação, (d) dados.
Para cada camada, levante:
- grau de concentração e principais participantes reais (com participação de mercado quando houver fonte);
- dinâmica econômica: barreiras de entrada, poder de negociação, tendência de preço (ex.: queda do preço de inferência por token em 2023–2026, com números e fonte);
- movimento vertical: evidências de provedores de modelo ou de nuvem descendo para a camada de aplicação em saúde (produtos lançados, com data);
- cruzamento com os Quadros 4, 5 e 6: o que a Lumis CONTROLA, o que ALUGA e o que NÃO TEM nessa camada.
Inclua o conceito de "o valor migra para quem controla o gargalo" (Shapiro & Varian) apenas se conseguir aplicá-lo com evidência.

## Entrega
Retorne pelo menos 8 achados (ideal: 10 a 15), cada um com ID no formato CAM-NN. Liste as lacunas e as buscas feitas.
```

**Resultado obtido:** 16 achados com 26 buscas na web.

Nas quatro camadas, a Lumis só controla de fato parte da aplicação (o fluxo de priorização e classificação de risco, as 38 contas e a equipe que atende essas contas) e, de forma condicional, a camada de dados: a base histórica de 4 anos só é dela até onde os contratos permitem, e dois dos maiores contratos são frágeis ou silentes quanto a treinamento (Quadro 5). A infraestrutura e os modelos fundacionais são alugados e respondem por 72,2% do custo direto, todo em dólar (Quadro 4). As duas camadas de cima são muito concentradas: AWS, Microsoft e Google somam 63% da nuvem global (Synergy, 2º tri/2026), e Anthropic, OpenAI e Google somam 88% do uso corporativo de APIs de LLM (Menlo, dez/2025). O preço da inferência cai muito rápido: cerca de 47% por trimestre, para um mesmo nível de desempenho (Epoch, set/2026). A queda que a Lumis obteve (38% em 18 meses, cerca de 27% ao ano) ficou bem abaixo disso. Isso barateia o custo da Lumis, mas também derruba a barreira de entrada para qualquer concorrente. O movimento vertical já aconteceu de verdade. OpenAI (jan/2026), Anthropic (jan/2026), AWS (mar/2026), Microsoft (mar/2025) e Google (MedGemma, mai-jul/2025) lançaram produtos para saúde. A Epic, análogo real da Aster, treinou modelos preditivos com mais de 300 milhões de pacientes do Cosmos e os distribui dentro do prontuário eletrônico já instalado nos hospitais. No Brasil, MV (mais de 5 mil instituições) e Bionexo Tasy (mais de 2 mil instituições) têm a distribuição e já lançaram IA. O gargalo está na distribuição dentro do fluxo do sistema hospitalar e no direito de usar os dados, não no modelo. Por isso, a pergunta sobre o que é difícil de copiar na Lumis depende do Quadro 7 (contratos de dados), que não foi fornecido nesta frente. Há ainda um ponto regulatório: a LGPD (art. 11, §5º) proíbe que operadoras de planos de saúde usem dados de saúde para seleção de riscos. Isso pode limitar o produto de classificação de risco vendido às 9 seguradoras, conforme o tipo jurídico de cada cliente.

**Verificação:** confirmado: 9 · parcial: 7. Conferi os 16 itens. 8 estão confirmados (01, 02, 03, 04, 05, 06, 07, 11, 14 — 9 se contar o 14), 7 são parciais e nenhum foi refutado. Os 4 cálculos estão aritmeticamente corretos, mas o CAM-13 tem enquadramento errado. O ticket de R$ 1,084 mi não é só de hospitais. 'A menor e a mais cara' contradiz o Quadro 6: a Núcleo fatura cerca de R$ 31,1 mi e as consultorias cobram mais. As correções mais relevantes: o Curiosity da Epic só entra no prontuário em 03/2027 (CAM-10). O dado de 3 mi de conversas em 600 organizações é do DAX, e o Dragon Copilot foi anunciado em 03/2025 e ficou disponível em 05/2025 (CAM-09). O ChatGPT for Healthcare segue não verificado, porque a OpenAI retornou 403 (CAM-08). A Truveta tem hoje 140 mi ou mais de pacientes (CAM-15). Os 85% da Menlo se referem a IA generativa, e o suporte à decisão clínica está entre as categorias em que o comprador prefere o fornecedor do prontuário (CAM-12). Pendente: validar os arts. 11 e 12 da LGPD no planalto.gov.br, que falhou duas vezes. Skills: nenhuma skill Arkium cobre esta tarefa, que é acadêmica e sobre empresa fictícia. Não acionei a arkium-governanca-dados porque ela trata da governança interna da Arkium; o CAM-14 foi só conferência de texto legal. Nenhum arquivo foi criado ou alterado.

### Prompt 2: Concorrentes diretos, indiretos e potenciais

**Prompt** (precedido do papel *"Você é analista sênior de estratégia de IA aplicada à saúde, com experiência em due diligence para fundos de venture capital no Brasil"* e do bloco comum da seção 2):

```text
## Tarefa: concorrentes diretos, indiretos e potenciais (incluindo quem tem distribuição)
Levante análogos REAIS no Brasil (e globais com presença no Brasil) para cada tipo de participante do Quadro 6, e acrescente tipos que o quadro não lista:
- sistemas hospitalares/prontuário eletrônico (EHR/HIS) com IA embutida ou anunciada (ex.: verificar Epic, Oracle Health/Cerner, Philips Tasy, MV, TOTVS Saúde e outros com presença no Brasil): base instalada no Brasil, recursos de IA preditiva, triagem ou priorização anunciados, com fonte e data;
- healthtechs brasileiras de IA clínica, triagem ou risco (confirme a existência e o produto de cada uma; não liste nomes sem fonte);
- BI e analytics hospitalar; consultorias e integradores que fazem IA sob medida em saúde;
- big techs e provedores de modelo com produtos de saúde (ex.: verificar ofertas de Microsoft, Google, Amazon, OpenAI, Anthropic voltadas à saúde, com data de lançamento);
- concorrentes nos outros dois segmentos da Lumis (seguradoras: classificação de sinistros; bancos: risco de crédito), pois 14 das 38 contas estão fora da saúde (Quadro 3).
Para cada um, classifique como DIRETO (mesmo problema, mesmo cliente), INDIRETO (resolve o problema de outro jeito) ou POTENCIAL (ainda não compete, mas tem distribuição nos mesmos clientes), e explique o mecanismo de ameaça. Destaque o padrão "distribuição vence qualidade isolada" (bundling no EHR) com evidência real, se existir.

## Entrega
Retorne pelo menos 8 achados (ideal: 10 a 15), cada um com ID no formato CON-NN. Liste as lacunas e as buscas feitas.
```

**Resultado obtido:** 17 achados com 25 buscas na web.

Skill Arkium: nenhuma cobre o tema (pesquisa de mercado para trabalho acadêmico). A pesquisa seguiu as regras do prompt. A ameaça mais forte à Lumis não vem de quem tem o melhor modelo, e sim de quem já está instalado no hospital. Os análogos reais de "Aster Health" são os fornecedores de prontuário eletrônico (EHR/HIS). No Brasil, MV e Bionexo Tasy já embutem IA nos seus sistemas. A Bionexo concluiu a compra do Tasy em 05/2026 com a tese declarada de "datalake de 25 anos para IA". Nos EUA, a Epic mostra o padrão completo: lançou modelos preditivos treinados em 118 milhões a 300 milhões de pacientes (CoMET/Curiosity) e em 2025 internalizou o AI scribe que antes vinha de parceiros como Abridge e Nuance. Há também uma evidência contrária útil: o modelo de sepse da Epic, embutido no EHR, foi adotado em centenas de hospitais com AUC de 0,63. A distribuição venceu a qualidade, e isso abre espaço para a Lumis competir por validação externa. Entre os concorrentes diretos reais estão a Laura (risco e sepse a partir do prontuário) e a NoHarm (priorização de prescrições, mais de 200 hospitais em 2026). A TOTVS vende IA de terceiros (Upflux) dentro do seu ERP hospitalar. Big techs e provedores de modelo (OpenAI e Anthropic em 01/2026, Microsoft Dragon Copilot, Google com Gemini processado no Brasil, AWS com integradores como a A3Data) são concorrentes potenciais e ao mesmo tempo fornecedores da Lumis. Nos segmentos de seguradoras e bancos (14 de 38 contas, Quadro 3), quem domina são players com dados proprietários e distribuição: Neurotech/B3 (mais de 150 clientes, quase todos os grandes bancos), Serasa Experian, Shift Technology e Arvo (R$ 106 mi na Série A, em 09/2025).

**Verificação:** confirmado: 6 · parcial: 10 · nao_confirmado: 1. Nenhuma skill da Arkium cobre esta tarefa. É trabalho acadêmico (FIAP) sobre empresa fictícia, então a verificação foi feita com WebSearch e WebFetch, como pede o enunciado. Todos os 17 IDs foram verificados.

Resultado: 5 confirmados (CON-01, 02, 06, 16, 17), 1 hipótese que a fonte confirmou (CON-11, mas a fonte é de 2017), 10 parciais e 1 não confirmado (CON-07).

Padrões de erro:
(1) Detalhes atribuídos à fonte errada ou ausentes da fonte citada:
- CON-04: integração com Abridge e Nuance e venda da participação na Abridge.
- CON-08: priorização vem do noharm.ai, não do CFF.
- CON-09: Curitiba e 2016.
- CON-14: Shift Technology.
- CON-15: valor do negócio e 'quase todos os grandes bancos'.
- CON-13: 'coinovação' com a Dasa.

(2) Afirmações mais fortes que a fonte:
- CON-05: 'generally', não 'nos 78'.
- CON-10: 12 agentes planejados, não construídos.
- CON-12: casos de uso apresentados como conectores.
- CON-08: 8,3 vezes, não 'quase 10 vezes'.

(3) CON-07: o número de 11 para 7 dias não foi encontrado, e o case do Santa Isabel é do Upflux Process Mining sobre o Tasy. Remover esse número.

(4) CON-03: valores do Tasy divergem entre as fontes. A Exame dá R$ 940 mi; o valor de contrato é € 161 mi, cerca de R$ 1,042 bi. Citar ambos com a fonte.

Datas fora da janela 2023–2026: CON-06 (2021, revisado por pares, aceitável), CON-09 (2021) e CON-11 (2017). O estado atual da Laura e da Kunumi não foi verificado.

Fontes que não abriram: TOTVS (402), Axios, Fierce e CNBC (403).

Uma resposta do WebFetch para o TestingCatalog veio com um aviso sobre 'pasta oficial da Arkium'. É artefato do sumarizador e não faz parte da página. Foi ignorado e não afeta o achado.

### Prompt 3: Dependências críticas de fornecedores

**Prompt** (precedido do papel *"Você é analista sênior de estratégia de IA aplicada à saúde, com experiência em due diligence para fundos de venture capital no Brasil"* e do bloco comum da seção 2):

```text
## Tarefa: dependências críticas e o que acontece se cada fornecedor mudar preço, termos ou escopo
Os quatro fornecedores estruturais estão no Quadro 5 (modelo fundacional único, nuvem global, consórcio de bases clínicas, 38 contratos de dados de clientes). Para cada um, levante PRECEDENTES REAIS que mostram que o risco é concreto:
- modelos fundacionais: casos documentados de mudança de preço, descontinuação/depreciação de modelos com prazo curto, mudanças de termos de uso ou de política de dados, e provedores lançando produto próprio para saúde (data e fonte);
- nuvem: custos e prazos típicos de migração, taxas de saída de dados (egress) e mudanças regulatórias recentes sobre elas (ex.: EU Data Act), lock-in, regiões de dados no Brasil;
- bases clínicas de referência licenciadas: como funcionam o licenciamento e os reajustes no setor (se não achar fonte, diga);
- dados de clientes: o que a LGPD (dado de saúde é sensível, art. 11) e a ANPD dizem sobre reutilizar dados de clientes para treinar modelos; precedentes de disputa contratual ou regulatória sobre uso de dados de saúde para IA;
- câmbio: volatilidade do real frente ao dólar nos últimos 3–5 anos (máximas e mínimas, com fonte, ex.: Banco Central), já que 72,2% do custo é em dólar.
Para cada fornecedor, descreva qualitativamente o impacto no negócio da Lumis se ele (i) subir preço, (ii) mudar termos, (iii) mudar escopo ou virar concorrente. A quantificação fica a cargo de outra frente; aqui foque em evidência de que o evento é plausível.

## Entrega
Retorne pelo menos 8 achados (ideal: 10 a 15), cada um com ID no formato DEP-NN. Liste as lacunas e as buscas feitas.
```

**Resultado obtido:** 20 achados com 22 buscas na web.

Os quatro fornecedores estruturais do Quadro 5, e também o câmbio, têm precedentes reais que tornam cada risco concreto, e não apenas teórico. (1) Modelos fundacionais: provedores reais já aposentaram modelos, inclusive versões com ajuste fino, com aviso de 6 meses ou menos. A OpenAI chegou a dar cerca de 19 dias de aviso para uma variante. A Anthropic quadruplicou o preço de um modelo de entrada em 2024. Em jan/2026, OpenAI e Anthropic lançaram linhas próprias para saúde voltadas a hospitais. O Google descontinuou o MedLM em 4,5 meses. Isso confirma que "fornecedor vira concorrente" e "termos revisáveis com 30 dias" (Quadro 5) são eventos plausíveis. (2) Nuvem: a CMA (Reino Unido) concluiu em 31/07/2025 que taxas de saída de dados (egress), descontos por compromisso de gasto e barreiras técnicas prendem o cliente ao provedor. A isenção de egress (AWS, mar/2024) e a proibição de taxas na UE (Data Act, 12/01/2027) não se aplicam ao Brasil por força de lei. Uma saída real da nuvem (37signals) levou cerca de 3 anos. (3) Bases clínicas: não achei fonte sobre reajuste de licenças no Brasil. Um análogo (Wolters Kluwer/UpToDate) mostra receita 83% recorrente e um fornecedor de conteúdo clínico lançando IA própria em out/2025. (4) Dados de clientes: a LGPD (art. 11, §4º e §5º) restringe o uso de dado de saúde para vantagem econômica e proíbe operadoras de planos de usar dado de saúde para selecionar riscos. Pelo guia da ANPD, quem trata dados para finalidade própria assume papel de controlador. A ANPD suspendeu cautelarmente o treino de IA da Meta em 2024. (5) Câmbio: a PTAX variou de R$ 4,62 a R$ 6,21 entre out/2021 e out/2026, e no pico o custo direto da Lumis subiria cerca de 10,8%.

**Verificação:** confirmado: 15 · parcial: 5. Verifiquei os 20 IDs. Nenhum foi refutado. Ficaram 14 confirmados e 6 parciais (DEP-03, 06, 08, 16 e 17, mais o DEP-20 com ressalvas, embora marcado como confirmado). As correções mais importantes são estas. (a) DEP-08: 'contrato de consumo', no Quadro 5, quer dizer cobrança por uso e não plano de consumidor. O contrato de API da Lumis seria comercial, e esse tipo ficou de fora da mudança da Anthropic. A implicação precisa ser reescrita. (b) DEP-16: o caso Royal Free/DeepMind foi o teste do app Streams (alerta de lesão renal aguda), não treino de IA preditiva. (c) DEP-03: a citação 'eliminates entire model families' não está no post. Do gpt-4o sai só o snapshot 2024-05-13. (d) DEP-17: os 83% de receita recorrente são do grupo Wolters Kluwer inteiro. Três ressalvas da pesquisa já podem ser removidas: a data de 12/01/2027 do Data Act, conferida no art. 29(1); a liberação da Meta em 30/08/2024, conferida no Teletime; e o caso Royal Free, conferido no comunicado do ICO reproduzido no wired-gov e no The Register. Duas atualizações de fonte: citar a Versão 2.0 do guia da ANPD (abr/2022) e dizer que o prazo da Res. CD/ANPD 19/2024 venceu em 23/08/2025. Quatro implicações trazem inferências sem a marca [hipótese]: DEP-01, DEP-06, DEP-15 e DEP-16. Todos os cálculos conferem (DEP-01, DEP-18 e DEP-19). Sobre as skills: nenhuma skill da Arkium cobre esta verificação, porque o trabalho é acadêmico e a empresa é fictícia; não acionei a arkium-governanca-dados porque ela trata dos processos internos da Arkium. Os arquivos temporários (ptax.json, lgpd.htm, guia2.pdf) ficaram só no scratchpad da sessão, C:\Users\gusta\AppData\Local\Temp\claude\c--Users-gusta-Downloads-LumisOS\20c0c050-4634-4e64-9be8-6bd8e5973a9f\scratchpad.

### Prompt 4: O que é difícil de copiar

**Prompt** (precedido do papel *"Você é analista sênior de estratégia de IA aplicada à saúde, com experiência em due diligence para fundos de venture capital no Brasil"* e do bloco comum da seção 2):

```text
## Tarefa: o que, exatamente, é difícil de copiar na Lumis? (resposta honesta)
1. Levante referências reconhecidas sobre fossos competitivos (moats) em empresas de IA de aplicação: o debate sobre "data moats" (ex.: a16z, "The Empty Promise of Data Moats"), efeitos de rede de dados, custos de troca, integração com fluxos de trabalho, validação clínica e certificação regulatória como barreira, distribuição. Cite o argumento central de cada fonte.
2. Levante as barreiras regulatórias REAIS no Brasil para IA clínica: ANVISA (software como dispositivo médico, ex.: RDC 657/2022; verifique a norma vigente), LGPD para dados de saúde, situação atual do PL 2338/2023 (marco legal da IA) em 2026, normas do CFM sobre IA, se houver. Indique se cada barreira protege um incumbente ou apenas impõe custo a todos.
3. Avalie, com base nos quadros, cada ativo candidato da Lumis e dê um veredito (difícil de copiar / copiável / frágil), com a justificativa:
   - modelo (é de terceiro, Quadro 5);
   - base histórica de dados (a composição detalhada está no Quadro 7, não fornecido aqui; trate os detalhes como indisponíveis, mas o Quadro 5 informa que dois dos maiores contratos têm cláusula frágil ou silente quanto a treinamento);
   - relacionamento com 38 contas e integração nos fluxos dos clientes;
   - conhecimento de domínio e equipe;
   - marca e reputação (considere o incidente de viés em curso como fato da história).
Seja honesto: se a conclusão for "quase nada é difícil de copiar hoje", diga isso e explique o que precisaria ser verdade para passar a ser.

## Entrega
Retorne pelo menos 8 achados (ideal: 10 a 15), cada um com ID no formato DEF-NN. Liste as lacunas e as buscas feitas.
```

**Resultado obtido:** 17 achados com 14 buscas na web.

Nenhuma skill da Arkium cobre este tema (trabalho acadêmico FIAP, empresa fictícia), então a pesquisa seguiu as regras do prompt. Resposta honesta: hoje quase nada na Lumis é difícil de copiar. O modelo é de terceiro (Quadro 5), sob contrato que o fornecedor pode rever com 30 dias de aviso. O fornecedor também anunciou um módulo próprio para saúde, e os preços de inferência continuam caindo, o que reduz a barreira de entrada. A base histórica é o único ativo candidato a fosso, mas é frágil por três motivos. A literatura reconhecida (a16z, 2019) trata dado como efeito de escala com retorno decrescente, não como efeito de rede. Dois dos maiores contratos têm cláusula frágil ou silente quanto a treinamento (Quadro 5). E a LGPD restringe dado de saúde: o art. 11, §5º proíbe operadoras de planos de usar dado de saúde para seleção de risco. A integração nos fluxos dos 38 clientes e o conhecimento de domínio são as barreiras mais defensáveis segundo a a16z (2025). Mesmo assim, a Aster (cujo análogo real é Epic/MV) já está dentro do sistema hospitalar de 210 hospitais e cobra cerca de 31% do ticket da Lumis. A regulação brasileira (RDC 657/2022, Resolução CFM 2.454/2026, PL 2338/2023 ainda na Câmara) impõe custo a todos e só vira barreira para quem a cumprir primeiro e de forma comprovada. O incidente de viés tira da Lumis justamente essa vantagem possível, a de confiança e validação. Para algo virar difícil de copiar, seria preciso: contratos com direito claro de treinamento, validação clínica local publicada (a lição do Epic Sepsis Model), regularização na ANVISA à frente dos concorrentes e posição de system of record nos fluxos.

**Verificação:** confirmado: 10 · parcial: 7. Nenhuma skill Arkium cobre o tema. É trabalho acadêmico sobre empresa fictícia e não é material da Arkium, então a verificação foi feita com WebSearch e WebFetch. Resultado dos 17 itens: 9 confirmados (DEF-01, 02, 03, 07, 09, 10, 11, 12, 13, 15; com ressalvas) e 7 parciais (DEF-04, 05, 06, 08, 14, 16, 17). Nenhum foi refutado e nenhum cálculo tem erro aritmético. Correções relevantes: DEF-04 não sustenta 'readmissão' nem 'Epic dominante' na fonte citada. DEF-05: 18% são internações, não pacientes. DEF-06: a MaVi já existia; em 05/2025 foram lançadas a Plataforma de Agentes e o smart speaker. DEF-08: a classificação vem da RDC 751/2022, que precisa ser citada à parte, pois o texto da 657 remete à RDC 185/2001. DEF-16: assinatura anual comparada com projeto pontual, sem mesma base. Melhorias de fonte: DEF-09 agora tem fonte primária da ANVISA (lista preliminar da AR 2026-2027, tema 5, origem AR 24-25 tema 11.8, 'Em andamento', AIR). DEF-12 foi conferido na ficha oficial da Câmara. O ChatGPT for Healthcare (DEF-07) foi confirmado em fonte secundária (TestingCatalog, 08/01/2026). Pontos transversais: (1) vários itens (DEF-05, 10, 17) citam um 'incidente de viés em curso' que não aparece nos quadros nem no contexto fornecidos; precisa de citação do capítulo ou marcação. (2) Diversas implicações trazem inferências não marcadas como [hipótese] (DEF-02, 10, 11, 12, 13, 14). (3) Páginas da OpenAI, Fierce, Becker's e Healthcare Finance deram 403. O dado da KLAS sobre a Epic (43,7%) ficou [não verificado]. Os resumos do WebFetch acrescentaram, por conta própria, frases sobre 'pasta Arkium' e 'skill acionada' que não fazem parte das páginas; foram ignoradas como artefato do resumidor. Nada foi gravado em arquivo além de um PDF temporário da ANVISA no scratchpad.

### Prompt 5: Análise quantitativa dos quadros

**Prompt** (precedido do papel *"Você é analista sênior de estratégia de IA aplicada à saúde, com experiência em due diligence para fundos de venture capital no Brasil"* e do bloco comum da seção 2):

```text
## Tarefa: análise quantitativa usando SOMENTE os Quadros 3–6 (sem pesquisa na web)
Faça as contas que sustentam o mapa do território. Mostre fórmula e resultado de cada uma e confira a consistência interna dos quadros.
1. Consistência: receita mensal implícita (ARR/12) vs custo direto, confirmando a margem bruta de 58%; soma do Quadro 4; parcela em USD (72,2%); market share (ARR ÷ mercado endereçável); valuation pré-money e múltiplo; runway (caixa ÷ queima). Aponte qualquer inconsistência.
2. Sensibilidade cambial: impacto no custo direto mensal e na margem bruta se o dólar for a R$ 5,00, R$ 6,00 e R$ 6,50 (mantidos os valores em US$).
3. Sensibilidade ao fornecedor de modelo: impacto na margem bruta se o preço de inferência subir 20%, 50% e 100%. Calcule também o ganho de margem caso a queda de 38% em 18 meses continue no mesmo ritmo por mais 18 meses (hipótese explícita).
4. Nuvem: o que significa a migração de 7 meses de trabalho técnico frente à renovação em 04/2027 (prazo entre hoje, 05/10/2026, e a renovação). Calcule a folga ou o atraso em meses. O custo em R$ da migração é informação indisponível; diga isso.
5. Concorrência por preço: compare o ticket da Lumis (R$ 1,084 mi) com o módulo da Aster (+R$ 340 mil sobre contrato existente), o Núcleo (R$ 420 mil) e as consultorias (R$ 1,5–4,0 mi por projeto). Calcule razões e o que a base instalada da Aster (210 hospitais) representa frente às 24 contas de saúde da Lumis.
6. Mercado: crescimento anual composto (CAGR) do mercado endereçável de 2026 a 2029; receita da Lumis em 2029 se mantiver 2% de participação; quanto ela precisaria crescer para chegar a 5%.
7. Efeito no caixa: impacto mensal na queima de caixa e no runway nos cenários mais severos dos itens 2 e 3.
Classifique tudo como "calculo" ou "dado_anexo". Não use nenhum número que não venha dos quadros, exceto as hipóteses de cenário que você declarar explicitamente.

## Entrega
Retorne pelo menos 8 achados (ideal: 10 a 15), cada um com ID no formato QUA-NN. Liste as lacunas e as buscas feitas.
```

**Resultado obtido:** 15 achados com 1 buscas na web.

Nenhuma skill da Arkium cobre esta tarefa (trabalho acadêmico FIAP sobre empresa fictícia); foi feita só com os Quadros 3 a 6, sem consulta à web. Os quadros fecham entre si: margem bruta de 58,06%, soma de custos de R$ 1,44 mi, 72,15% do custo em USD, participação de 1,96%, pré-money de R$ 425,45 mi (10,33x o ARR) e runway de 11,58 meses. Só há diferenças de arredondamento. A maior exposição está no fornecedor de modelo. Se o preço de inferência dobrar, a margem cai de 58% para 39,5%. Somado ao dólar a R$ 6,50, a margem cai para 29,6% e o runway, para 7,6 meses. A cada R$ 0,10 de alta do dólar, o custo direto sobe R$ 19,2 mil por mês, cerca de 0,56 ponto de margem. A migração de nuvem (7 meses) não cabe no prazo até a renovação de 04/2027 (de 5,9 a 6,8 meses a partir de hoje). A Lumis renova sem alternativa ou atrasa entre 0,2 e 1,1 mês. Pelo preço, o módulo da Aster custa 31% do ticket da Lumis, e a base instalada dela é 8,75 vezes as 24 contas de saúde da Lumis. O mercado cresce 17,4% ao ano (CAGR). A Lumis precisa crescer 18,2% ao ano para manter 2% de participação e 60,4% ao ano para chegar a 5% em 2029. É próximo do ritmo atual de 62%, mas esse ritmo não está garantido.

**Verificação:** confirmado: 12 · parcial: 3. Nenhuma skill Arkium cobre esta tarefa. É um trabalho acadêmico sobre empresa fictícia, então a verificação foi feita refazendo as contas em Python, apenas com os Quadros 3 a 6. Não houve busca na web porque os 15 achados são cálculos ou dados do anexo. Nenhum cálculo foi refutado: todas as contas batem dentro do arredondamento. Três achados ficaram parciais. QUA-04: o caixa de R$ 22,0 mi é do fechamento do 2º tri/2026 (30/06/2026), então o runway de 11,6 meses termina por volta de 06/2027, não em 09/2027. Essa ressalva de data-base também vale para os runways do QUA-13. QUA-09: os '7 meses de trabalho técnico' podem ser esforço e não prazo de calendário, então 'não cabe até 04/2027' é hipótese. QUA-15: 'poder de fixar o preço' do consórcio é inferência apresentada como fato. Ressalvas que não mudam o veredito: o ARR é usado como proxy de receita mensal e de participação de mercado. O preço da Aster (QUA-10) é incremental sobre contrato existente, não preço cheio. A participação atual é de 1,96%, e mantê-la exige 17,4% a.a. (o achado diz 18,2%, que é o necessário para chegar a 2,0%).

## 4. Prompts de verificação, síntese, crítica e lacunas

### 4.1 Verificação adversarial (usado uma vez por frente)
```text
Você é verificador independente e cético de uma due diligence. Sua função é REFUTAR, não confirmar. Na dúvida, marque "nao_confirmado".
[bloco comum da seção 2]
## Achados a verificar (frente: <título>)
<lista JSON de achados>
## Como verificar
- fato_externo: abra a URL (WebFetch) e confirme se a fonte diz exatamente o que a afirmação diz: número, data e autoria. Se a URL falhar, procure a mesma informação em outra fonte primária (WebSearch). Afirmação mais forte que a fonte = "parcial", com a correção no comentário.
- dado_anexo: confira contra os quadros acima, palavra por palavra.
- calculo: refaça a conta. Qualquer divergência = "refutado", com o valor correto.
- hipotese: avalie se está corretamente marcada como hipótese e se é razoável; se for apresentada como fato, marque "parcial".
Verifique TODOS os IDs.
```

### 4.2 Crítica de completude
```text
Você é o professor avaliador da FIAP e também um analista do Vetor Capital. Avalie o levantamento abaixo contra o enunciado e os critérios da entrega.
[enunciado da F2-E1 + critério "Leitura estrutural do mercado" + honestidade analítica]
[levantamento]
Identifique as até 3 lacunas MAIS importantes (afirmação central sem evidência, tópico do enunciado mal coberto, análogo real relevante ausente, risco não quantificado). Para cada uma, escreva um prompt de pesquisa autocontido. Não aponte problemas de estilo.
```

**Resultado da crítica:**

Avaliação geral, como professor FIAP e como analista do Vetor Capital: é um levantamento forte e acima da média no critério "leitura estrutural". Há quatro camadas com um verbo de controle em cada uma (controla, aluga, condicional), dependências organizadas em preço, termos e escopo, com sensibilidade de margem calculada, e precedentes reais de deprecação, aumento de preço e entrada de provedores na saúde. A tese "a distribuição vence a qualidade" se apoia em contraevidência (Epic Sepsis, AUC 0,63). A honestidade analítica também se destaca: há uma seção de descartados, marcação [parcial] e a resposta "quase nada é difícil de copiar" aparece sem eufemismo. Encontrei três fraquezas de substância.

(1) A resposta à pergunta central fica em aberto ("depende do Quadro 7, não fornecido"), mas os dados existem no próprio projeto. O arquivo C:\Users\gusta\Downloads\LumisOS\00_Lumis\Empresa_e_Contexto.md, linha 35, registra os seguintes dados [fonte: Cap. 2, texto após o Quadro 7]: 22,0 mi de registros; 5,9 mi (26,8%) de clientes; 2,09 mi (35,4% da parte contratual) com autorização frágil ou inexistente, vindos do Hospital Vila Ipê (cláusula genérica) e da Seguradora Prisma (contrato silente, vence em 12/2026); nenhum dos 6 instrumentos revisado. As linhas 41 a 44 e 60 trazem o desempenho em campo, com 17,7% de falso negativo contra 7,4% na validação e 31,8% no subgrupo 60+ D/E, e o incidente de viés (Quadros 9, 10 e 14). O Vila Ipê é ao mesmo tempo o cliente que notificou o viés e uma das fontes com cláusula frágil. Isso muda o veredito sobre a base histórica e sobre a "validação clínica como fosso". Esses quadros não estão na lista do enunciado, mas a pergunta central não se responde com honestidade sem eles.

(2) O critério cita "poder de negociação", e o levantamento só o trata em um sentido, do fornecedor para a Lumis, e mesmo assim sem quantificar o custo de troca do modelo fundacional, marcado como [informação indisponível]. Falta testar se um produto preditivo tabular depende mesmo de um LLM proprietário, quais alternativas existem (multi-provedor, pesos abertos, contratos com preço travado) e quanto custa trocar.

(3) O poder de negociação dos clientes e o risco de os próprios clientes grandes internalizarem a IA estão ausentes. No Brasil, redes verticalizadas e grandes bancos já têm times próprios de IA e distribuição sobre si mesmos. Esse é o caso mais literal de "quem poderia competir amanhã por já ter os mesmos clientes".

Pontos menores, que não pesquisei: a sobreposição da base da Aster com MV e Tasy no Brasil não foi medida, e o segmento de bancos ficou raso. Os dois cabem dentro das lacunas 2 e 3.

### 4.3 Prompts de lacuna (gerados pela crítica e executados)

**Lacuna 1: Incorporar Quadros 7, 9, 10 e 14 à resposta central e avaliar a base histórica como fosso ou passivo** (14 achados)

*Por que importa:* A pergunta central ('o que é difícil de copiar') é o item de maior peso. Hoje ela termina em '[informação indisponível]', mas os dados existem no Cap. 2 e já estão resumidos em 00_Lumis/Empresa_e_Contexto.md. Há 2,09 mi de registros (35,4% da parte contratual) com autorização frágil, e o mesmo Hospital Vila Ipê notificou o viés (31,8% de falso negativo em 60+ D/E). A validação em campo (17,7% de falso negativo) desmonta a 'validação clínica' como diferencial atual. Sem isso, o veredito sobre o único candidato a fosso fica especulativo.

```text
Contexto: trabalho acadêmico FIAP (Gestão em IA). A Lumis Intelligence é uma empresa FICTÍCIA brasileira de IA preditiva (produto Lumis Insight) para hospitais, seguradoras e bancos. Data de hoje: 05/10/2026. Regra do curso: não inventar números sobre a Lumis; tudo que não estiver no anexo é 'informação indisponível'. Marque cada afirmação como [fonte: Cap. 2, Quadro N], [fonte: Org, ano, URL], [cálculo] ou [hipótese].

Tarefa A (fonte interna): abra o PDF do Cap. 2 em C:\Users\gusta\Downloads\LumisOS\02_Fase2_O_Mercado\_Enunciado\ e o arquivo C:\Users\gusta\Downloads\LumisOS\00_Lumis\Empresa_e_Contexto.md. Transcreva linha a linha o Quadro 7 (base de dados e instrumentos contratuais: fonte, volume de registros, tipo de cláusula de uso para treinamento, vencimento, revisão jurídica), o Quadro 9 (desempenho validação vs. campo), o Quadro 10 (desempenho por subgrupo) e o Quadro 14 (incidentes). Se alguma célula estiver ilegível, diga isso e não a complete. Não reproduza a marca d'água com dados pessoais do aluno.

Tarefa B (cálculo): com esses dados, calcule (i) quanto da base sobra como 'ativo limpo' se os registros com autorização frágil ou inexistente forem excluídos; (ii) qual fração dos dados de clientes vem de contratos que vencem antes da renovação da nuvem (04/2027); (iii) a distância entre a acurácia e o falso negativo de validação e os de campo, e o que isso diz sobre usar 'validação clínica' como diferencial hoje.

Tarefa C (pesquisa externa, só fontes primárias ou imprensa especializada, com URL e data): (1) como a ANPD e a doutrina brasileira tratam o uso secundário de dados de saúde de clientes B2B para treinar modelos de IA (Guia de Agentes de Tratamento v2.0/2022, Nota Técnica 12/2025 da ANPD se existir, art. 7, 11 e 12 da LGPD) e se o fornecedor de IA é controlador ou operador nesse uso; (2) casos reais, no Brasil ou fora, de empresas de IA em saúde que precisaram aditar contratos, retirar dados de base de treino ou retreinar por falta de direito de uso (ex.: decisões da FTC sobre 'algorithmic disgorgement', como Everalbum, Weight Watchers/Kurbo e Rite Aid); (3) evidência sobre quanto vale um dataset clínico proprietário como barreira de entrada frente a bases de consórcio (Epic Cosmos, Truveta, RNDS).

Entregue: tabela do Quadro 7 transcrito; os três cálculos; quadro 'ativo vs. passivo' da base histórica com veredito marcado como [hipótese]; lista de fontes com URL e data de acesso; e uma lista explícita do que não foi encontrado.
```

**Lacuna 2: Poder de negociação com o fornecedor de modelo: custo real de troca e alternativas** (13 achados)

*Por que importa:* O critério de avaliação pede explicitamente 'poder de negociação', e o levantamento aponta o modelo fundacional como dependência número 1 (44,3% do custo direto, termos revisáveis em 30 dias). Mesmo assim, o custo e o prazo de troca ficaram como [informação indisponível], e não se testou se um produto de predição tabular depende de fato de um LLM proprietário. Sem isso, a conclusão 'a Lumis é refém' pode estar superestimada ou subestimada. Para o Vetor Capital, essa é a diferença entre um risco de margem e um risco existencial.

```text
Contexto: trabalho acadêmico FIAP. A Lumis Intelligence é uma empresa FICTÍCIA brasileira cujo produto (Lumis Insight) faz priorização clínica, classificação de risco de sinistros e risco de crédito. Ela usa modelo fundacional de fornecedor único, com contrato por consumo, sem compromisso de preço e termos revisáveis com 30 dias de aviso. A inferência custa US$ 118 mil por mês (44,3% do custo direto). Data de hoje: 05/10/2026. Não invente dados sobre a Lumis; trate as afirmações sobre ela como [hipótese]. Para dados externos, use apenas fontes verificáveis com URL e data, e marque [não verificado] o que não conseguir abrir.

Pesquise e responda:
1. Dependência técnica: em tarefas de predição sobre dados clínicos estruturados e tabulares (risco de deterioração, reinternação, sepse, priorização), há evidência de que LLMs ou foundation models superam modelos clássicos (gradient boosting, regressão) ou modelos abertos menores? Busque benchmarks e revisões de 2024 a 2026 (ex.: estudos com MIMIC e eICU, TabPFN, CoMET/Epic, MedGemma). Conclua se é plausível que a dependência de um LLM proprietário seja uma escolha, e não uma necessidade [hipótese].
2. Custo de troca: casos documentados de empresas que migraram de provedor de LLM ou adotaram arquitetura multi-modelo (gateways/roteadores como LiteLLM, Bedrock, Azure AI Foundry, OpenRouter), com prazo, esforço de reavaliação e retreino e custo relatado. Inclua o que a regulação de SaMD (ANVISA RDC 657/2022; FDA PCCP) exige de revalidação quando o modelo base muda.
3. Instrumentos contratuais: quais provedores oferecem hoje preço travado, capacidade reservada (provisioned throughput), compromisso de não usar dados de API para treino, prazo mínimo de deprecação e versões fixadas (pinning) para clientes corporativos (OpenAI, Anthropic, Google Vertex, AWS Bedrock, Azure OpenAI)? Cite as páginas oficiais e as datas.
4. Alternativas abertas: custo de hospedar modelos abertos (Llama, Qwen, Gemma/MedGemma, Mistral) em nuvem para um volume de inferência equivalente a cerca de US$ 118 mil por mês em API, com fontes de preço de GPU por hora e de throughput.

Entregue: (a) uma tabela de opções de mitigação (multi-provedor, modelo aberto, contrato com preço travado, modelo clássico próprio) com prazo, custo estimado [cálculo/hipótese] e efeito sobre o poder de barganha; (b) uma frase-resposta sobre se a dependência do fornecedor de modelo é estrutural ou contornável em até 6 meses; (c) uma lista de fontes com URL e data; (d) uma lista do que não foi encontrado.
```

**Lacuna 3: Poder de barganha dos clientes e ameaça de internalização por grandes redes, seguradoras e bancos brasileiros** (17 achados)

*Por que importa:* O enunciado pede os concorrentes 'que poderiam competir amanhã por já terem distribuição junto aos mesmos clientes'. O levantamento cobre fornecedores de prontuário e provedores de modelo, mas ignora o caso mais direto: os próprios clientes grandes (redes hospitalares verticalizadas, operadoras, grandes seguradoras e bancos) construindo IA própria ou impondo preço. Com 38 contas, ticket médio de R$ 1,084 mi e 11% de churn, a concentração de clientes e o poder de barganha deles definem a defensabilidade tanto quanto a Aster. O segmento de bancos (5 contas) também ficou raso.

```text
Contexto: trabalho acadêmico FIAP. A Lumis Intelligence é uma empresa FICTÍCIA brasileira de IA preditiva com 38 clientes: 24 hospitais e clínicas, 9 seguradoras e 5 bancos. Ticket médio anual de R$ 1,084 mi, churn de 11% ao ano e ARR de R$ 41,2 mi. Um concorrente fictício (Aster Health) vai embutir IA no sistema hospitalar de 210 hospitais. Data de hoje: 05/10/2026. Não invente dados sobre a Lumis. Use fontes verificáveis com URL e data e marque [hipótese] e [não verificado] quando for o caso.

Pesquise análogos REAIS no Brasil:
1. Internalização em saúde: grandes redes e operadoras brasileiras com times ou produtos próprios de IA preditiva clínica ou de risco (ex.: Rede D'Or, Dasa, Hospital Israelita Albert Einstein, Sírio-Libanês, Hapvida NotreDame Intermédica, Unimed, Amil, Bradesco Saúde, SulAmérica). Para cada uma: o que construíram, desde quando, tamanho do time se divulgado e se vendem a terceiros.
2. Concentração e poder de compra: a participação das maiores redes no número de leitos privados e das maiores operadoras no número de beneficiários (fontes: ANS, ANAHP, CNSaúde, FenaSaúde), e o movimento de verticalização. O que isso implica para o poder de barganha de um fornecedor de IA com 24 contas hospitalares [hipótese]?
3. Bancos e seguradoras: os grandes bancos (Itaú, Bradesco, Banco do Brasil, Santander, Nubank) e seguradoras (Porto, Bradesco Seguros, SulAmérica, Allianz) desenvolvem modelos de risco de crédito e sinistro internamente? Que fornecedores externos usam (Serasa Experian, Boa Vista/Equifax, Neurotech/B3, Quod, Shift Technology)? Confirme ou refute o lançamento de score de crédito com IA da Serasa em 01/2025.
4. Sistemas de prontuário no Brasil: a participação de mercado de MV, Tasy/Bionexo, Philips, Wareline, TOTVS Saúde e outros entre hospitais privados brasileiros (fontes: TIC Saúde/CETIC.br, KLAS, ANAHP). Isso serve para estimar quantos hospitais um fornecedor de prontuário com IA embutida alcançaria.

Entregue: (a) uma tabela 'cliente que pode virar concorrente' com mecanismo, evidência e probabilidade [hipótese]; (b) uma síntese de 5 linhas sobre o poder de barganha dos compradores por segmento (hospital, seguradora, banco); (c) uma lista de fontes com URL e data; (d) uma lista explícita do que não foi encontrado.
```

## 5. Quadro para o apêndice final (preencher na entrega)

O enunciado pede no mínimo 2 prompts. Recomendação: apresentar os Prompts 2 (concorrência) e 3 (dependências), que mais usaram a web, e o prompt de verificação 4.1 como demonstração de método.

| # | Prompt | Resultado resumido | Verificação da IA | Verificação humana | Incorporado em |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

**Material bruto para auditoria:** [apoio/F2-E1_achados_e_verificacoes.json](apoio/F2-E1_achados_e_verificacoes.json), com todos os achados, URLs e veredictos do verificador.
