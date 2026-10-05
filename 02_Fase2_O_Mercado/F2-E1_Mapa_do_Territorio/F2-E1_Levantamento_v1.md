# F2-E1: Levantamento do Mapa do Território (v1)

> **Status:** levantamento de pesquisa. Ainda não é o documento final da entrega. Data: 05/10/2026.
> **Escopo de dados:** o enunciado lista os Quadros 3, 4, 5 e 6 do Cap. 2 e a narrativa do Cap. 2. Esta versão também usa os Quadros 7, 8, 9, 10, 11 e 14, porque sem eles não dá para responder com honestidade à pergunta central. Esses quadros estão fora da lista do enunciado, e usá-los na entrega final depende de **decisão sua** (ver seções 6.5 e 9).
> **Empresas fictícias:** Lumis, Aster Health, Núcleo Saúde Analytics e Vetor Capital. Os clientes Hospital Vila Ipê, Rede Sanare, Seguradora Prisma e Banco Meridiano também são fictícios, todos do Cap. 2. Toda empresa real citada aqui é um **análogo** e não aparece na história da Lumis.
> **Marcações:**
> - Origem: [Quadro N], [cálculo], [fonte: Org, ano], [hipótese].
> - Verificação: [parcial] quando o verificador corrigiu o achado, [não verificado] quando não houve URL aberta, [informação indisponível] quando o dado não existe nos quadros.
> - Rastreio: [LACx-NN] é o ID do achado nos complementos.

---

## 0. Síntese executiva

1. **Camadas.** Das quatro, a Lumis controla de fato só a **aplicação**: o fluxo de priorização e classificação, as 38 contas e a equipe dedicada [Quadro 3; Quadro 4]. Na camada de **dados** o controle é condicional, e agora tem número. A base soma 22,0 mi de registros, assim divididos:
   - 14,0 mi (63,6%) vêm do DATASUS, que é público.
   - 5,9 mi são dados de clientes. Desses, só **3,81 mi (17,3% da base)** têm autorização explícita, e mesmo essa autorização vem com condições.
   - Nenhum dos 6 instrumentos contratuais passou por revisão jurídica.
   [Quadro 7; cálculo; LAC1-01/02]
2. **Infraestrutura e modelo são alugados** em camadas concentradas. Somam 72,2% do custo direto, todo em dólar, contra receita 100% em reais [Quadro 4]. Na nuvem, AWS, Microsoft e Google têm 63% do mercado global [fonte: Synergy, 2026]. Em APIs de LLM, Anthropic, OpenAI e Google têm 88% do uso corporativo nos EUA [fonte: Menlo, 2025].
3. **Fornecedor único de modelo.** É a dependência mais **rápida**: termos revisáveis com 30 dias de aviso e 44,3% do custo direto [Quadro 4; Quadro 5]. Se o preço dobrar, a margem bruta cai para 39,5% e o runway para cerca de 8,7 meses [cálculo]. Mesmo assim, ela **parece contornável em até 6 meses**, se o núcleo do Lumis Insight for preditivo e tabular. Com volume de dados, modelos convencionais treinados superam LLMs [fonte: Zhu et al., npj Digit Med, 2026] [hipótese; LAC2-01/13]. O contrato atual não usa nenhum dos instrumentos de barganha que o mercado oferece: capacidade reservada, versão fixada e aviso de 60 dias [LAC2-05/06/08]. O efeito já apareceu dentro da empresa: em 09/2025 o desempenho caiu depois de uma atualização do fornecedor [Quadro 14].
4. **O fornecedor pode virar concorrente.** OpenAI e Anthropic lançaram linhas para saúde em jan/2026 [fonte: Anthropic, 2026; TestingCatalog, 2026] [parcial]. Os provedores também aposentam modelos com aviso de 2 semanas a 6 meses e já subiram preço em 4x [fonte: OpenAI, 2026; TechCrunch, 2024].
5. **Calendário apertado.** A migração de nuvem leva 7 meses e a renovação é em 04/2027, daqui a 5,9 a 6,8 meses [Quadro 5; cálculo]. Antes disso vencem os **dois contratos de dados com autorização frágil**: Prisma em 12/2026 e Vila Ipê em 03/2027. Juntos, são 35,4% dos dados de clientes [Quadro 7; cálculo; LAC1-04]. Os próximos 6 meses são a janela para regularizar esses contratos e também o período de maior risco de perdê-los [hipótese].
6. **A ameaça mais forte é a distribuição embutida no prontuário.** A Aster cobra +R$ 340 mil sobre um contrato que o cliente já tem, cerca de 31% do ticket da Lumis [Quadro 6; cálculo]. O mecanismo já existe com empresas reais:
   - Na América Latina, a MV está em 894 hospitais e o Tasy em 500 [fonte: MV citando KLAS, 2025].
   - A Rede D'Or está ampliando o Tasy de 50 para 60 hospitais [fonte: Philips, 2025].
   - A MV já embute IA no prontuário (MaVi, SOUL Agents) [fonte: MV, 2025].
7. **Contraevidência e limite.** O modelo de sepse da Epic, embutido no prontuário, teve AUC de 0,63 e mesmo assim foi adotado em massa [fonte: JAMA Intern Med, 2021]. Isso abriria espaço para competir por validação. Só que a Lumis **também** tem esse problema:
   - O falso negativo foi de 7,4% na validação e de 17,7% em campo.
   - No subgrupo 60+ D/E ele chega a 31,8%.
   - O material comercial ainda diz "94% de acurácia".
   [Quadros 9, 10 e 11; LAC1-05/06]
8. **Novo: clientes que podem virar concorrentes.** Os compradores mais valiosos são os mais capazes de dispensar a Lumis:
   - Einstein: cerca de 120 algoritmos próprios.
   - Hapvida NDI: 115 soluções de IA.
   - Itaú: mais de 1,3 mil modelos.
   - Bradesco: mais de 600 casos de GenAI.
   - Porto: IA em precificação há mais de 15 anos.

   As 6 maiores operadoras de saúde somam cerca de 42% dos beneficiários [cálculo; LAC3-01 a 13]. O poder do comprador cresce com o porte, e é desse porte que o ticket da Lumis precisa para escalar [hipótese].
9. **Câmbio.** Cada R$ 0,10 de alta no dólar custa R$ 19.240 por mês. No pico da PTAX dos últimos 5 anos, a margem bruta cai para 53,5% [cálculo; fonte: BCB, 2026].
10. **Mercado.** Cresce cerca de 17,4% ao ano, e a Lumis 62%. Chegar a 5% de participação em 2029 exige crescer 60,4% ao ano por 3 anos [cálculo].
11. **Resposta honesta.** Hoje quase nada na Lumis é difícil de copiar, e a base histórica é **passivo líquido**, não fosso [hipótese; LAC1-14]. O que poderia vir a ser difícil de copiar ainda precisa ser construído: dado de desfecho brasileiro com direito de uso limpo, somado à prova auditável de desempenho por subgrupo.

---

## 1. Camadas do mercado de IA e o que a Lumis controla

| Camada | Quem domina (real) | Dinâmica econômica | O que a Lumis controla / aluga / não tem | Evidência |
|---|---|---|---|---|
| **Infraestrutura (nuvem)** | AWS 28%, Microsoft 20% e Google 15%: 63% do mercado global no 2º tri/2026 (67% em IaaS/PaaS). O mercado cresceu 43% a/a, e os serviços de GenAI 165% a/a. | Oligopólio com demanda aquecida. A tarifa de saída (egress) deixou de ser a barreira principal: Google (jan/2024) e AWS (mar/2024) isentam quem sai totalmente. A barreira agora é de engenharia. A CMA (31/07/2025) aponta egress, descontos por compromisso e barreiras técnicas como fontes de aprisionamento. | **Aluga.** Provedor global, plano anual, desconto por volume, renovação em 04/2027 e migração de 7 meses [Quadro 5]. Custa R$ 401.760 por mês: 27,9% do custo direto e cerca de 11,7% da receita [Quadro 4; cálculo]. | [fonte: Synergy, 2026]; [fonte: SiliconANGLE, 2024]; [fonte: CMA, 2025] |
| **Modelos fundacionais** | Anthropic 40%, OpenAI 27% e Google 21%: 88% do uso corporativo de APIs nos EUA (Brasil: [informação indisponível]). Gasto com APIs: US$ 12,5 bi em 2025. | Para o mesmo desempenho, o preço cai cerca de 47% por trimestre. Os provedores **desceram para a aplicação em saúde**: Anthropic (jan/2026), OpenAI (jan/2026) [parcial], AWS (mar/2026), Microsoft (Dragon Copilot, 2025) e Google (MedGemma, 2025). O ciclo de vida está ficando padronizado: Azure aposenta modelos GA em 18 meses (12 meses para terceiros) com aviso mínimo de 60 dias, e a Anthropic dá aviso mínimo de 60 dias [LAC2-05/06]. | **Aluga** de fornecedor único, por consumo, sem compromisso de preço e com 30 dias de aviso [Quadro 5]. Controla os "ajustes próprios" (Cap. 2), cujo tamanho é [informação indisponível]. Queda de preço obtida: cerca de 27% ao ano, contra cerca de 92% ao ano no mercado. As métricas são diferentes [cálculo]. **Novo:** em predição tabular com volume de dados, LLM provavelmente é escolha de arquitetura, não necessidade [hipótese; LAC2-01/02]. A arquitetura real do Lumis Insight é [informação indisponível]. | [fonte: Menlo, 2025]; [fonte: Epoch AI, 2026]; [fonte: Microsoft Learn, 2026]; [fonte: Anthropic, 2026]; [fonte: Zhu et al., 2026] |
| **Aplicação** | Hospitais: os donos do prontuário, como Epic nos EUA (análogo da Aster), MV (894 hospitais na AL) e Philips/Tasy, hoje Bionexo (500 hospitais na AL) [fonte: MV citando KLAS, 2025]. Seguradoras e bancos: players com dados próprios (Neurotech/B3, Arvo, Serasa) e **times internos** (Itaú, Bradesco, Porto). | Quem é dono do sistema de registro embute IA na base instalada. Nos EUA, os compradores preferem o fornecedor do prontuário inclusive em suporte à decisão clínica [parcial]. **Novo:** os grandes compradores brasileiros já internalizaram IA preditiva (seção 2.2). | **Controla** o fluxo de priorização e classificação, as 38 contas e a equipe dedicada de R$ 289 mil por mês [Quadro 3; Quadro 4]. **Não tem** o sistema de registro hospitalar [hipótese]. | [fonte: Menlo, 2025]; [fonte: MV, 2025]; [fonte: Exame, 2026]; LAC3 |
| **Dados** | Bases nacionais e de consórcio: RNDS/SUS (mais de 2,8 bi de registros, instituída em 23/07/2025); Epic Cosmos (mais de 300 mi de pacientes e 16,3 bi de encontros, de 310 sistemas de saúde); Truveta (mais de 120 mi de pacientes de 30 sistemas, 900+ hospitais, em 02/2025; o site atual diz mais de 140 mi). | Dado clínico agregado tende a virar insumo comum ou de consórcio [hipótese]. A LGPD impõe teto legal: o art. 11 não prevê legítimo interesse para dado sensível; o §4º limita o compartilhamento para vantagem econômica; o §5º impede seleção de risco por operadoras; e o art. 12 só tira da lei o dado anonimizado de forma irreversível. | **Controla de forma condicional:** <br>• Base: 22,0 mi de registros. DATASUS 14,0 mi (63,6%), sintéticos 2,1 mi, clientes 5,9 mi (26,8%). <br>• Dados de clientes com autorização explícita: 3,81 mi, todos com condição (Sanare: uso agregado e anonimizado; Meridiano: auditoria anual do cliente). <br>• Autorização frágil ou silente: 2,09 mi (35,4%), do Vila Ipê (cláusula genérica) e da Prisma (contrato silente). <br>• Nenhum dos 6 instrumentos foi revisado. <br>• Só 2 dos 24 hospitais e clínicas contribuem dados [Quadro 7; Quadro 3; cálculo]. <br>**Licencia** as bases clínicas de um consórcio, com reajuste sem teto [Quadro 5]. | [fonte: Mobile Time, 2025]; [fonte: Waxler et al., 2025]; [fonte: Truveta, 2025]; [fonte: Planalto, LGPD]; LAC1-01/02/03/13 |

**Leitura da camada [hipótese].** O gargalo de valor está na **distribuição dentro do fluxo hospitalar** e no **direito de usar dado de desfecho**, não no modelo. O poder de impor custo de troca está nas duas pontas. Em cima ficam o fornecedor de modelo (poder contratual) e a nuvem (7 meses de migração). Embaixo ficam o dono do prontuário e o comprador grande, que pode internalizar. A Lumis fica no meio. Mais uma ponta mudou de leitura: na camada de dados, o "ativo" da Lumis é em 63,6% dado público, acessível a qualquer concorrente [Quadro 7; cálculo]. Sobre a lógica de lock-in de Shapiro e Varian: [não verificado no texto do livro].

---

## 2. Concorrentes diretos, indiretos e potenciais

### 2.1 Mapa de concorrentes

| Participante | Tipo | Mecanismo de ameaça | Evidência |
|---|---|---|---|
| **Aster Health** (fictício) | Potencial que vira direto | Módulo embutido em sistema usado por 210 hospitais, por +R$ 340 mil. Teto teórico de R$ 71,4 mi, 1,73x o ARR da Lumis. A taxa de adoção é [informação indisponível]. | [Quadro 6; cálculo] |
| **Núcleo Saúde Analytics** (fictício) | Indireto | BI sem IA preditiva, 74 contas, cerca de R$ 31,1 mi de receita estimada. Pode acrescentar predição [hipótese]. | [Quadro 6; cálculo] |
| **Consultorias e integradores** (Quadro 6) | Indireto | Projetos de R$ 1,5 a 4,0 mi sobre a mesma infraestrutura. | [Quadro 6] |
| **Provedores de modelo fundacional** (Quadro 6) | Potencial e, ao mesmo tempo, fornecedor | Acesso direto e preço em queda. O fornecedor da Lumis anunciou módulo para saúde. | [Quadro 5; Quadro 6] |
| Epic (EUA), **análogo da Aster** | Padrão de referência | Família Curiosity, treinada no Cosmos (mais de 300 mi de pacientes). Anunciada em 2026, com lançamento no prontuário previsto para 03/2027 [parcial]. O preprint CoMET (118 mi de pacientes) igualou ou superou modelos específicos na maioria das 78 tarefas [parcial; preprint]. AI Charting lançado em 08/2025. | [fonte: Epic, 2026]; [fonte: Waxler et al., 2025; autoria principal [não verificado]]; [fonte: Galen Growth, 2025] |
| MV, **análogo brasileiro da Aster** | Potencial, que vira direto se lançar predição | Líder em prontuário na AL: 894 hospitais (KLAS 2025, dado divulgado pela própria MV). Mais de 5 mil instituições somando todos os tipos. Faturou R$ 638 mi em 2024. Embute IA (MaVi, integrada ao prontuário; SOUL Agents na Hospitalar 2026). A predição de sepse "6 a 12 horas antes" está [não verificado]. Seria um passo incremental [hipótese]. | [fonte: MV, 2025]; [fonte: MV Blog, 16/05/2025]; [fonte: Baguete, 2025]; LAC3-07/08 |
| Bionexo Tasy, **análogo** | Potencial | Comprou o Tasy da Philips, com aprovação do CADE. Valor: € 161 mi; R$ 940 mi segundo a Exame; cerca de R$ 1 bi segundo outras fontes [parcial]. O Tasy está em 500 hospitais na AL (KLAS) e **em 50 a 60 hospitais da Rede D'Or** [fonte: Philips, 19/08/2025]. A tese declarada é usar um datalake de 25 anos para IA. Divergência: o complemento LAC3 marcou a venda como [não verificado], porque se apoiava numa matéria de 07/2025, anterior ao negócio. As fontes de 05/2026 confirmam a venda e prevalecem. | [fonte: Exame, 2026]; [fonte: Baguete, 2026]; [fonte: Philips, 2025] |
| Laura, **análogo** | Direto (hospital) | IA de risco e sepse sobre o prontuário. Mais de 40 instituições e seed de R$ 10 mi em 2021. Situação em 2026: [não verificado]. | [fonte: InfoMoney, 2021] |
| NoHarm, **análogo** | Direto em nicho adjacente | Priorização de prescrições em mais de 200 hospitais e serviços (Brasil e Argentina) [parcial]. É cerca de 8,3x as 24 contas de saúde da Lumis, mas as bases não se comparam. | [fonte: CFF, 2026] |
| A3Data com AWS (Mater Dei), **análogo** de integrador | Indireto | 12 agentes no ciclo de receita. ROI declarado de 517% [parcial]. | [fonte: AWS Blog Brasil, 2026] |
| Kunumi, **análogo** de integrador | Indireto | Óbito em UTI no Sírio-Libanês. Dados de 2017; situação atual [não verificado]. | [fonte: Exame, 2017; URL não registrada] |
| OpenAI e Anthropic, **análogos** do fornecedor | Potencial | Claude for Healthcare (11/01/2026) e ChatGPT for Healthcare (01/2026) [parcial]. Foco em IA generativa administrativa [hipótese]. Oferta no Brasil: [informação indisponível]. | [fonte: Anthropic, 2026]; [fonte: TestingCatalog, 2026] |
| Google Cloud e Microsoft, **análogos** | Potencial | Rede Américas usa o Agentspace; Gemini 2.5 Flash processado no Brasil. O Dragon Copilot não está no Brasil. | [fonte: TI Inside, 2025]; [fonte: Microsoft, 2025] |
| Planisa, **análogo do Núcleo** | Indireto | Base financeira da saúde, sem IA preditiva. | [fonte: Planisa, 2026] |
| Arvo, **análogo** em seguradoras | Direto, se as seguradoras da Lumis forem de saúde | Série A de R$ 106 mi. Mais de R$ 130 bi em sinistros processados. Identificou R$ 1,8 bi em pagamentos indevidos em 2025. O orçamento de IA das operadoras vai primeiro para fraude e auditoria [hipótese]. | [fonte: Startupi, 2025]; [fonte: Exame, data [não verificado]]; LAC3-14 |
| Neurotech/B3, **análogo** em bancos e seguros | Direto | Compra por R$ 620 mi mais earn-out de até R$ 523 mi (total até cerca de R$ 1,14 bi). Mais de 320 funcionários e mais de 150 clientes, cerca de 3,9x as 38 contas da Lumis. | [fonte: InvestNews, 2023]; [fonte: Finsiders, 2025]; [cálculo] |
| Serasa Experian, **análogo** em crédito | Indireto ou direto em bancos | **Confirmado:** nova versão do Serasa Score em jan/2025, em tempo real e "processado por IA". É atualização de versão, não produto novo. Tem escala de dados de birô, que a Lumis não tem. | [fonte: Serasa, 29/05/2025]; LAC3-11 |
| Wolters Kluwer/UpToDate, **análogo** de fornecedor de conteúdo | Potencial | UpToDate Expert AI (10/2025). | [fonte: Wolters Kluwer, 2026] |

### 2.2 Clientes que podem virar concorrentes (novo)

| Comprador (análogo real) | Mecanismo | Evidência | Probabilidade [hipótese] |
|---|---|---|---|
| Rede hospitalar de ponta (Einstein) | Constrói internamente e pode licenciar. Tem cerca de 120 algoritmos, entre eles modelos de risco. Mantém central de monitoramento com mais de 100 gatilhos desde 2018. O projeto Watcher detecta piora clínica com meta de −50% em transferências tardias para UTI (piloto de 04/2024 a 10/2026). Os 250 profissionais de dados estão [não verificado]. | [fonte: Convergência Digital, 08/01/2025]; [fonte: Medicina S/A, 30/09/2024] | ALTA de não comprar; MÉDIA de competir |
| Operadora verticalizada (Hapvida NDI) | Rede e operadora com dado integrado. 115 soluções de IA, 30 em produção. 8,869 mi de beneficiários (3T25). | [fonte: Diário Indústria & Comércio, 14/11/2025] | ALTA |
| Grupo verticalizado (Rede D'Or + SulAmérica) | 76 hospitais e 10.351 leitos. Comprou a SulAmérica em 2022 (6 mi de beneficiários). Compra insumos até 25% abaixo da média do mercado. Usa o Tasy em 50 a 60 hospitais. O modelo oncológico com recall de 69% está [não verificado]. | [fonte: Exame, 2026]; [fonte: Philips, 2025] | ALTA (impõe preço ou internaliza) |
| Fornecedor de prontuário (MV, Tasy) | Embute módulo na base instalada. | LAC3-06/07/08 | ALTA |
| Grande banco (Itaú, Bradesco) | Itaú: mais de 1,3 mil modelos, inclusive de risco de crédito, e R$ 11,7 bi em tecnologia em 2025. Bradesco: mais de 600 casos de GenAI com barramento próprio. | [fonte: Let's Money, 10/03/2026 e 12/09/2026] | ALTA de internalizar |
| Birô ou plataforma de dados (Serasa, Neurotech/B3) | Vende score e IA a bancos e seguradoras com escala de dados. | LAC3-11/12 | MÉDIA-ALTA |
| Grande seguradora (Porto) | IA em precificação há mais de 15 anos. 4 dos 7 processos de sinistro auto já usam IA; a análise caiu de 4 a 7 dias para 1 a 2 dias. | [fonte: Mobile Time, 24/04/2026] | ALTA |

Não pesquisados ou sem fonte primária: Sírio-Libanês, Dasa (a venda de IA a terceiros está [não verificado]), Unimed, Amil, Bradesco Saúde, SulAmérica, Banco do Brasil, Santander, Nubank, Bradesco Seguros e Allianz.

### 2.3 Poder de barganha dos compradores por segmento [hipótese; LAC3-17]

- **Hospital:** poder alto nas redes grandes, verticalizadas e com time de dados, que podem trocar a Lumis por um módulo do prontuário instalado. Poder médio-baixo nos hospitais médios sem time de dados, que é onde fica o espaço da Lumis.
- **Seguradora de saúde:** poder alto. As 6 maiores somam cerca de 42% dos beneficiários [cálculo; fonte: SindiPlanos com dados da ANS, mar/2025, fonte secundária]. A verticalização transforma operadora em rede, e o orçamento de IA disputa com fraude e auditoria.
- **Banco:** poder muito alto nos grandes, com centenas ou milhares de modelos internos. Nos médios, a alternativa natural é o birô, não a Lumis.
- **Exposição por conta:** cada conta média vale 2,63% do ARR. A distribuição real de receita entre as contas é [informação indisponível] [Quadro 3; cálculo].
- **Conclusão:** a tese para a Vetor precisa dizer em que porte de cliente a Lumis é insubstituível. Disputar contas âncora contra a internalização pressiona o preço.

### 2.4 Distribuição e bundling

- **Padrão real:** o dono do prontuário primeiro integra parceiros e depois internaliza o produto. Exemplo: Epic AI Charting em 08/2025 [fonte: Galen Growth, 2025]. A venda da participação na Abridge está [não verificado].
- **Preferência do comprador:** nos EUA, a maioria prefere o fornecedor do prontuário, inclusive em suporte à decisão clínica. Startups ficam com 85% do gasto em IA **generativa** em saúde [fonte: Menlo, 2025] [parcial].
- **Alcance:** a MV tem 894 hospitais na AL, cerca de 37x as 24 contas hospitalares da Lumis. MV e Tasy somados chegam a 1.394. As bases não são equivalentes, porque uma conta é de hospitais na América Latina e a outra de "hospitais e clínicas" no Brasil [cálculo; LAC3-07].
- **Brecha:** o Epic Sepsis Model teve AUC de 0,63, contra 0,76 a 0,83 declarados, e deixou de detectar 67% dos casos [fonte: JAMA Intern Med, 2021] [parcial]. Para a Lumis aproveitar essa brecha, ela precisa antes resolver a própria distância entre validação e campo (seção 4).
- **Fora do hospital:** 14 das 38 contas (36,8%) estão em seguradoras e bancos [Quadro 3; cálculo]. A Aster não alcança esses clientes, mas os grandes compradores ali internalizam ou compram de birôs (seção 2.2).

---

## 3. Dependências críticas

| Dependência | Situação | Se mudar PREÇO | Se mudar TERMOS | Se mudar ESCOPO | Impacto quantificado [cálculo] | Precedente real (análogo) |
|---|---|---|---|---|---|---|
| **Modelo fundacional** | Fornecedor único, contrato de consumo (pago por volume), sem compromisso de preço, termos revisáveis com 30 dias de aviso. Preço caiu 38% em 18 meses. Módulo próprio de saúde anunciado [Quadro 5]. | Comprime a margem na hora: são 44,3% do custo direto e 18,6% da receita. Com 30 dias de aviso, não há tempo de reagir [hipótese]. | A aposentadoria de um modelo obriga a revalidar o modelo clínico. Se o Lumis Insight for SaMD, pode exigir peticionamento (RDC 657/2022, art. 16) [fonte: ANVISA, 2022; hipótese]. **Evidência interna:** em 09/2025 o desempenho caiu após atualização do fornecedor; correção em 6 dias [Quadro 14]. | O fornecedor vira concorrente na aplicação. OpenAI e Anthropic não usam por padrão os dados de API para treino; o contrato da Lumis é [informação indisponível] [LAC2-07]. | +10%: MB 56,2%. +20%: 54,3%. +50%: 48,8%. +100%: 39,5%, com queima de R$ 2,54 mi por mês e runway de 8,7 meses (−2,9) [LAC2-11]. −38%: MB 65,1% (vale para todos). | OpenAI: aviso de 2 semanas a 6 meses [fonte: OpenAI, 2026]. Anthropic: mínimo de 60 dias [fonte: Anthropic, 2026]; compromisso de preservar pesos [não verificado, post de 04/11/2025 sem URL]. Azure: ciclo de 18 meses, 60 dias de aviso, deployments provisionados sem upgrade automático [fonte: Microsoft Learn, 2026]. Haiku 4x mais caro [fonte: TechCrunch, 2024]. MedLM descontinuado em cerca de 4,5 meses [fonte: Google Cloud, 2025]. |
| **Nuvem** | Plano anual, desconto por volume, renovação em 04/2027, migração de 7 meses [Quadro 5]. | Renovação com pouco poder de barganha [hipótese]. | Mudança de região traz risco de transferência internacional. A região usada hoje é [informação indisponível]. | Sobreposição parcial com a IA em saúde dos hiperescaladores [hipótese]. | R$ 401.760 por mês (27,9%). Faltam 5,9 a 6,8 meses contra 7 de migração [hipótese de leitura]. **Atenção:** levar o modelo para pesos abertos (seção 3.1) **aumenta** a dependência da nuvem. | CMA (31/07/2025). Isenção de egress da AWS (2024). Data Act da UE, art. 29 (não alcança o Brasil). 37signals (não comparável). Região AWS em São Paulo. |
| **Bases clínicas** | Consórcio, licença anual, renovação automática, reajuste sem teto [Quadro 5]. | Cada 10% de reajuste: +R$ 11.204 por mês (cerca de 0,33 ponto de margem). | A renovação automática pode travar a saída [hipótese]. | O fornecedor de conteúdo lança IA própria [hipótese com análogo]. | R$ 112.040 por mês (7,8%). Índice de reajuste: [informação indisponível]. | Wolters Kluwer, UpToDate Expert AI [parcial]. |
| **Dados de clientes** | Quadro 7: <br>• Vila Ipê: 1,2 mi, cláusula genérica ("melhoria contínua do serviço"), vence em 03/2027. <br>• Sanare: 3,4 mi, aditivo de 2024 que permite uso agregado e anonimizado, vence em 08/2028. <br>• Prisma: 0,89 mi, contrato silente, vence em 12/2026. <br>• Meridiano: 0,41 mi, permite uso com auditoria anual, vence em 05/2028. <br>Nenhum dos instrumentos foi revisado. | Os clientes podem passar a cobrar pelo dado [hipótese]. | Renegociar pode restringir o treino ou forçar a retirada de dados. O Vila Ipê, dono da cláusula mais fraca, é **o mesmo cliente que notificou o viés** [Quadro 10; Quadro 14] [hipótese sobre o efeito]. | Clientes grandes podem levar os dados para a Aster ou para o fornecedor [hipótese]. | 35,4% dos dados de clientes vencem antes de 04/2027. 73,9% do dado clínico com autorização explícita vem de um único cliente, a Sanare. A multa da LGPD vai até 2% do faturamento, limitada a R$ 50 mi por infração (art. 52, II). | LGPD, art. 11 (sem legítimo interesse para dado sensível), §§4º e 5º, e art. 12 [fonte: Planalto]. Guia ANPD v2.0 (2022), §53: o operador só trata dados para a finalidade do controlador. Para treinar um modelo vendido a terceiros, a Lumis tende a ser controladora [hipótese/interpretação]. Nota Técnica ANPD 12/2025: tema não pacificado [fonte: Lefosse, 2025; não verificado na fonte primária]. FTC (Everalbum 2021, WW/Kurbo 2022, Rite Aid 2023): ordens de **destruir algoritmos**; Rite Aid junta direito de uso e viés por grupo. Royal Free/DeepMind, ICO 2017: a sanção recaiu sobre o hospital [fonte: The Register, 2017]. ANPD × Meta, 2024 [fonte: Conjur, 2024]. Nenhum caso brasileiro de retreino forçado foi encontrado. |
| **Câmbio** | 72,2% do custo em USD e 100% da receita em BRL [Quadro 4]. | +R$ 19.240 por mês a cada R$ 0,10. Câmbio +10%: +R$ 103.896 por mês. | Hedge ou indexação: [informação indisponível]. | — | R$ 5,94: MB 55,0%. R$ 6,2086: 53,5%. R$ 6,50: 51,9%. | PTAX de 5 anos entre R$ 4,6175 e R$ 6,2086. PTAX em 02/10/2026: R$ 5,2238 [fonte: BCB, 2026]. |

### 3.1 Poder de barganha com o fornecedor de modelo: opções de mitigação (novo) [hipótese/cálculo; LAC2-13]

| Opção | Prazo | Custo estimado | Efeito na barganha | Ressalva |
|---|---|---|---|---|
| Multi-provedor via gateway (padrão LiteLLM/AWS) | 1 a 3 meses (o gateway sai em semanas, e o resto é revalidar um segundo modelo) | Engenharia [informação indisponível]; inferência neutra | Alto: a ameaça de troca fica crível | Revalidação clínica de cada modelo [fonte: AWS Solutions Library; LAC2-12] |
| Modelo aberto hospedado (Llama, Qwen, Gemma/MedGemma) | 3 a 6 meses | Os US$ 118 mil por mês pagam cerca de 40 H100 on-demand; hardware perto de US$ 0,60 por milhão de tokens a 100% de uso [cálculo; throughput [não verificado]]. Mais MLOps. | Alto | Troca a dependência do modelo pela dependência da nuvem (7 meses de migração). O volume de tokens da Lumis é [informação indisponível]. |
| Contrato com preço e capacidade travados, mais cláusula de não treino e aviso de 60 dias ou mais | 1 a 2 meses de negociação | Bedrock com 6 meses: cerca de 40% abaixo do preço sem compromisso (ex.: US$ 23,77 contra 39,60/h) [fonte: AWS, 2026]. Azure PTU: até 64 a 70% [não verificado]. OpenAI Scale Tier [não verificado]. | Médio: protege preço e versão, mas aprofunda o lock-in | Cria compromisso de caixa com runway de 11,6 meses [Quadro 3] |
| Núcleo preditivo em modelo clássico próprio (GBM, regressão, TabPFN), com o LLM só em texto | 4 a 6 meses, incluindo revalidação e eventual peticionamento à ANVISA | Inferência muito menor [hipótese] | O mais alto: o score deixa de depender do fornecedor | Depende de base contratual limpa para treino (seção 4) [fonte: Zhu et al., 2026; Univ. Freiburg, 2025] |

**Frase-resposta [hipótese].** A dependência do fornecedor de modelo é contornável em até 6 meses, e não estrutural, com duas condições: o núcleo do Lumis Insight ser tabular e haver um protocolo de revalidação. Para a Vetor, ela é risco de margem. Só vira risco de caixa num choque grande de preço com 30 dias de aviso.

**Ordem de criticidade, revisada [hipótese].** A versão anterior punha o modelo em primeiro lugar. Com os complementos, a ordem fica assim:
1. **Dados de clientes.** É a única dependência estrutural: sustenta o único ativo próprio, tem prazo de 12/2026 a 03/2027 e pode exigir retreino.
2. **Modelo fundacional.** É a mais rápida (30 dias), mas é contornável.
3. **Câmbio.**
4. **Nuvem.** O prazo aperta em 04/2027, e a pressão cresce se o modelo for para pesos abertos.
5. **Bases clínicas.**

---

## 4. O que é difícil de copiar: resposta honesta

| Ativo | Veredito | Por quê | Origem |
|---|---|---|---|
| Modelo e ajustes próprios | **Copiável** | Modelo de terceiro, de fornecedor único, com termos de 30 dias. O preço de inferência cai cerca de 13x ao ano. Em predição tabular, modelos abertos e clássicos são alternativas viáveis, o que torna o modelo ainda mais replicável por concorrentes. | [Quadro 5]; [fonte: Epoch AI, 2026]; [fonte: Zhu et al., 2026]; [hipótese] |
| Base histórica (22,0 mi de registros) | **Passivo líquido hoje** | 63,6% é DATASUS público. Dos dados de clientes, só 3,81 mi (17,3% da base) têm autorização explícita, e ela é condicionada. 2,09 mi são frágeis ou silentes, e nenhum instrumento foi revisado. O modelo atual pode estar "contaminado" por esses dados (análogos da FTC). 73,9% do dado clínico limpo vem de 1 cliente. Só 2 de 24 hospitais contribuem. A escala é irrelevante diante de Cosmos (mais de 300 mi), Truveta e RNDS (2,8 bi). O que tem valor: o histórico de fluxo clínico brasileiro de 2019 a 2026 e o dado de priorização com desfecho, que nenhum provedor de modelo tem [hipótese]. | [Quadro 7; Quadro 3; cálculo]; LAC1-02/03/11/13/14 |
| Integração e relacionamento com 38 contas | **Parcialmente difícil** | Churn de 11% ao ano (cerca de 4,2 contas e R$ 4,5 mi). A retenção ainda não enfrentou concorrente embutido no prontuário. Os compradores com mais poder são os que internalizam (seção 2.2). Profundidade da integração: [informação indisponível]. | [Quadro 3; Quadro 4]; [fonte: a16z, 2025]; [hipótese] |
| Conhecimento de domínio e equipe | **Moderadamente difícil** | 48 técnicos e 14 pessoas de produto e design. Pessoas saem. Einstein, Itaú e Bradesco têm times maiores. | [Quadro 3]; LAC3; [hipótese] |
| Validação clínica | **Hoje é passivo** | A validação de 2023 usou 48 mil casos (2,5% do volume de campo), de 2 hospitais da mesma região. Em campo: acurácia −6,5 pp, falso negativo 2,4x maior (17,7%) e 31,8% no subgrupo 60+ D/E. O material comercial ainda diz 94% [Quadro 11]. Viés etário e regional notificado pelo Vila Ipê, ainda em tratamento [Quadro 14]. Pesos de 8,9% para "faixa de CEP" e 15,1% para "custo acumulado" [Quadro 8, via LAC1-14; não transcrito nesta rodada]; a relação causal com o viés não está demonstrada [hipótese]. A Resolução CFM 2.454/2026 exige governança. | [Quadros 8, 9, 10, 11 e 14; cálculo]; [fonte: CFM, 2026] |
| Monitoramento próprio | **Fraco** | 2 dos 4 incidentes foram detectados pelo cliente. A duplicidade de registros foi corrigida no sistema, mas não no material comercial. | [Quadro 14] |
| Conformidade regulatória | **Ainda não é barreira** | RDC 657/2022: a priorização tende a ser SaMD, e mudança significativa de desempenho exige peticionamento (art. 16). Revisão para IA/ML na Agenda ANVISA 2026-2027. PL 2338/2023 parado. Situação da Lumis na ANVISA: [informação indisponível]. | [fonte: ANVISA, 2022 e 2026]; [fonte: LCF, 2026] |
| Preço e posição | **Não protege** | O ticket é 3,19x o módulo da Aster e 2,58x o Núcleo. Fica mais barato que um projeto de consultoria só num horizonte de até cerca de 1,4 ano. | [Quadro 6; cálculo] |
| Presença em três segmentos | **Diferencial possível contra a Aster, fraco contra a internalização** | A Aster não alcança seguradoras e bancos. Mas ali os grandes compradores internalizam (Itaú, Bradesco, Porto) ou compram de birôs (Serasa, Neurotech/B3). O §5º da LGPD pode limitar o uso com operadoras. | [Quadro 3]; LAC3; [hipótese] |

**Resposta direta [hipótese].** Hoje quase nada na Lumis é difícil de copiar:
- O modelo é alugado e fica mais barato para todos.
- A distribuição hospitalar pertence ao dono do prontuário (Aster e seus análogos MV, Tasy e Epic).
- Os maiores compradores conseguem internalizar.
- A base histórica, único ativo próprio, é hoje **passivo líquido**: 63,6% é dado público, só 17,3% é dado de cliente com autorização explícita, e a validação clínica que deveria provar o valor da base está desatualizada e mostra viés.

O que poderia vir a ser difícil de copiar **não é o dado bruto**. É o dado de desfecho da priorização em fluxo brasileiro, com direito de uso limpo, somado à prova auditável de desempenho por subgrupo. Para chegar lá, quatro condições teriam de se cumprir em 6 a 12 meses:
1. Aditivos de direito de uso com a Prisma (até 12/2026) e com o Vila Ipê (até 03/2027), estendidos depois aos 22 hospitais que hoje não contribuem dados, com papel jurídico definido.
2. Retreino ou linhagem de dados que isole os registros frágeis.
3. Validação em campo estratificada e publicada, que substitua o "94%".
4. Integração profunda no fluxo de priorização, mirando hospitais e seguradoras médios, onde o comprador não internaliza.

Um fundo que paga 10,3x o ARR estaria pagando por esse fosso futuro e assumindo o passivo atual. Esse texto precisa ser checado contra `00_Lumis/Compromissos_Vigentes.md`, em especial o compromisso de não amplificar danos.

---

## 5. Números de apoio (cálculos)

| # | Indicador | Conta | Resultado |
|---|---|---|---|
| 1 | Receita mensal (proxy) | 41,2 mi / 12 | R$ 3,433 mi |
| 2 | Margem bruta | 1 − 1,44 / 3,433 | 58,06% |
| 3 | Custo em USD | (118.000 + 74.400) × 5,40 | R$ 1.038.960 (72,15%) |
| 4 | Pré-money e múltiplo | 120/0,22 − 120; ÷ 41,2 | R$ 425,45 mi; 10,33x |
| 5 | Runway | 22,0 / 1,90 | 11,58 meses a partir de 30/06/2026, caixa até cerca de 06/2027 [parcial]. Em 05/10/2026 restariam cerca de R$ 16,3 mi, ou 8,6 meses [hipótese] |
| 6 | Participação de mercado | 41,2 / 2.100 | 1,96% |
| 7 | Câmbio | 192.400 × Δ | R$ 19.240 por mês a cada R$ 0,10. MB 60,3% / 55,0% / 53,5% / 51,9% |
| 8 | Choque no modelo | 1.440.000 + 637.200 × Δ | MB 54,3% (+20%), 48,8% (+50%), 39,5% (+100%) |
| 9 | Cenário combinado | (236.000 + 74.400) × 6,5 + 401.040 | Custo de R$ 2,419 mi; MB 29,6%; runway 7,6 meses |
| 10 | Queda de preço, Lumis vs. mercado | 0,62^(12/18) vs. 0,53^4 | −27,3% contra −92,1% ao ano (métricas diferentes) |
| 11 | Prazo da nuvem | 05/10/2026 → 04/2027 | 5,9 a 6,8 meses contra 7 de migração |
| 12 | Aster vs. Lumis | 340/1.084; 210/24; 210 × 0,34 | 31%; 8,75x; teto de R$ 71,4 mi |
| 13 | Diferença de ticket | 1.084 − 340 | R$ 744 mil |
| 14 | Crescimento do mercado | (3,4/2,1)^(1/3) − 1 | 17,4% ao ano |
| 15 | Metas para 2029 | 2% e 5% de 3,4 bi | R$ 68 mi (18,2% ao ano); R$ 170 mi (60,4% ao ano) |
| 16 | Churn | 0,11 × 38; × 41,2 | 4,2 contas; R$ 4,5 mi |
| 17 | Contas fora da saúde | 14/38 | 36,8% |
| 18 | Peso de cada fornecedor na receita | ÷ 3,433 | Inferência 18,6%; nuvem 11,7% |
| 19 | Ativo limpo de clientes | 5,9 − (1,2 + 0,89) | 3,81 mi; 64,6% dos dados de clientes; 17,3% da base |
| 20 | Composição da base | (3,81 + 2,1)/22; 14/22 | Próprio limpo 26,9%; DATASUS 63,6% |
| 21 | Concentração clínica | 3,4/(1,2 + 3,4) | 73,9% vem da Sanare; 2 de 24 hospitais contribuem |
| 22 | Dados que vencem antes de 04/2027 | (0,89 + 1,2)/5,9 | 35,4% (Prisma 12/2026, cerca de 2 a 3 meses; Vila Ipê 03/2027, cerca de 4,9 a 5,9 meses) |
| 23 | Validação vs. campo | 94,1 − 87,6; 17,7/7,4; 31,8/7,4; 31,8/10,6; 48.000/1.940.000 | −6,5 pp; FN 2,39x; 60+ D/E 4,30x; 3,0x o melhor subgrupo; amostra de 2,47% |
| 24 | Consistência do Quadro 10 | Médias ponderadas | FN 17,65% (confere); acurácia 87,2% contra 87,6% no Quadro 9 (0,4 pp; arredondamento [hipótese]) |
| 25 | Inferência +10% | 0,1 × 637.200 / 3,433 mi | −1,86 pp; MB 56,2% |
| 26 | Inferência +100%, runway | 22,0 / (1,90 + 0,637) | 8,7 meses (−2,9) |
| 27 | Câmbio +10% | 0,10 × 1.038.960 | +R$ 103.896 por mês |
| 28 | Equivalência em GPU | 118.000 / (3,99 × 730); 3,99 / (1.850 × 3.600/10⁶) | 40,5 H100 (5,1 nós); cerca de US$ 0,60/Mtok [throughput não verificado] |
| 29 | Concentração de planos de saúde | 21,9 / 52,1 | 6 maiores cerca de 42,0% |
| 30 | MV vs. Lumis | 894/24; 894 + 500 | 37,3x; 1.394 hospitais MV + Tasy (bases diferentes) |
| 31 | Peso de uma conta média | 1,084 / 41,2 | 2,63% do ARR |
| 32 | Neurotech vs. Lumis | 150 / 38 | cerca de 3,9x em número de clientes |

Premissas: o custo direto do Quadro 4 é todo o custo considerado na margem bruta. Volumes em dólar constantes. Receita constante nos choques.

---

## 6. Lacunas e informação indisponível

### 6.1 Resolvidas nesta rodada
- **Quadro 7** transcrito, com 6 fontes, volumes, cláusulas e vencimentos [LAC1-01].
- **"Incidente de viés"**: consta nos Quadros 10 e 14 (07/2026, Vila Ipê, em tratamento).
- **Serasa, score com IA em 01/2025**: confirmado [LAC3-11].
- **Guia ANPD v2.0 (2022)**: aberto e lido [LAC1-09].
- **Truveta "30 sistemas"**: confirmado no press release de 13/02/2025, com 120 mi de pacientes. O site atual informa mais de 140 mi. Vale o mais recente, com a divergência sinalizada.
- **Royal Free/DeepMind**: agora com URL (The Register).

### 6.2 Dados da Lumis ainda indisponíveis
- Volume de tokens, modelo usado e arquitetura do Lumis Insight (quanto do score depende do LLM). Identidade do fornecedor de modelo e de nuvem. Região de processamento. Custo da migração de nuvem em R$.
- Texto do contrato com o fornecedor de modelo (cláusula de treino e retenção).
- Classificação do produto na ANVISA e se ele é SaMD regularizado.
- Se o modelo atual foi treinado com os dados do Vila Ipê e da Prisma, se existe linhagem de dados e se os dados da Sanare estão de fato anonimizados.
- Data de revisão jurídica por instrumento. O Quadro 7 não tem essa coluna; só o texto do capítulo diz que nenhum foi revisado.
- Tipo da Seguradora Prisma e das outras 8 seguradoras: se forem operadoras de plano, aplica-se o art. 11, §5º, da LGPD.
- ARR, churn e margem por segmento. Maiores contas e concentração de receita. Porte dos clientes.
- Papel jurídico da Lumis (controladora ou operadora) por operação. Hedge. Indexação dos contratos com clientes. Índice de reajuste das bases clínicas.
- Adoção do módulo da Aster e sobreposição dos 210 hospitais com a carteira ou o pipeline da Lumis.
- Quadro 8: os pesos foram citados via LAC1-14, mas o quadro não foi transcrito nesta rodada.
- Definição de "queima de caixa" e caixa em 05/10/2026.

### 6.3 Fontes externas não abertas ou não verificadas
- openai.com (Scale Tier e enterprise privacy), Azure Tech Community (PTU), Ropes & Gray, Fierce Healthcare, Becker's, Healthcare IT News, Axios e CNBC retornaram 403. A guidance de PCCP no fda.gov retornou 404. A Nota Técnica ANPD 12/2025 retornou 401 e foi lida só via Lefosse. A decisão original do ICO e a ordem final do Everalbum (PDF) não foram abertas.
- Google Vertex (Provisioned Throughput e governança de dados): não confirmado.
- Throughput do Llama 3.3 70B em H100 (markaicode, [não verificado]). TechTarget (14/05/2026) sobre o custo total de MLOps, sem URL [não verificado].
- Nenhum caso em fonte primária de empresa de saúde que trocou de provedor de LLM, com prazo e custo.
- Nenhuma evidência quantitativa do valor de um dataset clínico proprietário como barreira. Há só dados de escala.
- Nenhum caso brasileiro (ANPD ou Judiciário) de retreino ou destruição de modelo. Nenhuma manifestação da ANPD sobre o papel do fornecedor de IA B2B.
- Participação das maiores redes em leitos privados (ANAHP/CNSaúde). Dados da ANS em fonte primária (exigiu autenticação). TIC Saúde/CETIC.br. Relatório KLAS original (o dado veio via comunicado da MV).
- Participação de nuvem e de LLM no Brasil. Base instalada da Epic e da Oracle no Brasil. Preço de módulos de IA embutidos. Reajuste de bases clínicas no Brasil. Sobrepreço da região de São Paulo.
- Situação atual da Laura e da Kunumi. Estudo da PwC (403). Shapiro e Varian sem leitura da fonte.
- Einstein com 250 profissionais de dados, IA de sepse da MV, recall de 69% da Rede D'Or e Dasa vendendo IA: todos [não verificado].
- Não pesquisados: Sírio-Libanês, Unimed, Amil, Bradesco Saúde, SulAmérica, BB, Santander, Nubank, Bradesco Seguros, Allianz. Estudos de CoMET e eICU contra GBM.

### 6.4 Divergências sinalizadas
- **Valor da compra do Tasy:** € 161 mi; R$ 940 mi; cerca de R$ 1 bi. A venda à Bionexo foi confirmada por fontes de 05/2026, que prevalecem sobre a matéria de 07/2025 usada no LAC3.
- **Earn-out da Neurotech:** "até R$ 1,1 bi" (InvestNews) e "R$ 523 mi de earn-out" (Finsiders) são compatíveis se o primeiro for o total (620 + 523 = R$ 1,143 bi) [hipótese de leitura].
- **Período do Meridiano:** a extração em layout mostra 2021, e a extração bruta mostra 2023-2026, com contrato de 2023. Adotada a extração bruta; conferir no PDF.
- **Período do Vila Ipê:** os dados vão de 2019 a 2026, antes da fundação (2022) e do contrato (2022). Pode ser carga histórica retroativa [hipótese]; isso não consta no capítulo.
- **Acurácia:** a ponderada pelo Quadro 10 (87,2%) difere da do Quadro 9 (87,6%).
- **Câmbio:** a PTAX atual (R$ 5,22) difere do Quadro 4 (R$ 5,40). Os cálculos usam o Quadro 4.
- **Margem com inferência +10%:** o LAC2-11 diz 56,1%, e o recálculo sobre a base de 58,06% dá 56,2%. Adotado 56,2%.

### 6.5 Decisão pendente (sua)
- Usar ou não os Quadros 7, 8, 9, 10, 11 e 14 na entrega final, que estão fora da lista do enunciado. Se usar, registrar em `DECISOES.md` e checar contra `Compromissos_Vigentes.md`.

---

## 7. Descartados na verificação

| Item | Motivo |
|---|---|
| CON-07: TOTVS/Upflux, tempo de internação de 11 para 7 dias | Não confirmado. O case é do Upflux sobre o Tasy. |
| CAM-13: "a Lumis é a menor e a mais cara" | Refutado pelo Quadro 6. |
| CAM-13: "a Aster é 3,2x mais barata em hospital" | O ticket só de hospitais não consta. |
| CON-14: Shift Technology no Brasil | Sem fonte aberta. Confirmado de novo no LAC3. |
| CON-15: Neurotech "parceira de quase todos os grandes bancos" | Sem fonte aberta. |
| CON-04: Epic e a participação na Abridge | Só aparece em snippets [não verificado]. |
| CAM-10: Curiosity "já distribuído"; Agent Factory em 2026 | O lançamento é previsto para 03/2027. |
| DEF-04: "readmissão" na Healthcare IT Today | Não consta nessa fonte; consta no preprint. |
| DEF-06/CAM-11: "MaVi lançada em 05/2025" | A MaVi já existia. |
| CAM-09: 3 mi de conversas atribuídas ao Dragon Copilot | O número é do DAX. |
| CAM-15: Truveta "120 mi e 30 sistemas" como dado atual | O dado é de 02/2025 (agora com fonte). O dado atual é de mais de 140 mi. |
| DEP-16: Royal Free como caso de "treino de IA" | Foi teste do app Streams. |
| DEP-08: "contrato de consumo exposto a termos de consumidor" | Leitura errada. |
| CON-13: "coinovação" Google-Dasa; "residência de dados tira barreira LGPD" | A fonte só diz que a Dasa usa Gemini. O segundo ponto foi rebaixado a hipótese. |
| CON-12: "conectores para glosa" | São casos de uso (claims appeals). |
| CON-08: "quase 10x" | O correto é 8,3x. |
| DEF-16: Lumis mais barata que consultoria, sem horizonte | Só vale até cerca de 1,4 ano. |
| QUA-04: "o caixa acaba em 09/2027" | Corrigido para cerca de 06/2027. |
| DEP-17/DEF-14: 83% de receita recorrente "do UpToDate" | O número é do grupo. |
| CAM-12: 85% de "todo" o gasto | O número é de IA generativa. |
| LAC2: migrações de LLM com −73% em 12 semanas e economia de 91% | Blogs de fornecedor (swfte.com, aipricingmaster.com) não abertos. Descartados como evidência. |
| LAC3: "venda do Tasy à Bionexo não verificada" | Superado pelas fontes de 05/2026 (n.º 37 e 38). |
| LAC3: IA de sepse da MV "6 a 12 h antes"; 250 profissionais de dados no Einstein; recall de 69% na Rede D'Or; Dasa vendendo IA | Só apareceram em snippets ou em página não aberta [não verificado]. Não usar como fato. |

---

## 8. Fontes externas verificadas

*Infraestrutura e modelos*
1. Synergy Research Group, "Q2 Cloud Market Passes $143 Billion...", 30/07/2026. https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years
2. SiliconANGLE, "AWS follows Google Cloud in canceling egress fees", 05/03/2024. https://siliconangle.com/2024/03/05/aws-follows-google-cloud-canceling-egress-fees-allowing-customers-leave-cloud-platform-free/
3. TechCrunch, "Amazon follows Google in announcing free data transfers out of AWS", 05/03/2024. https://techcrunch.com/2024/03/05/amazon-follows-google-in-announcing-free-data-transfers-out-of-aws
4. UK CMA, "Cloud services market investigation", 31/07/2025. https://www.gov.uk/cma-cases/cloud-services-market-investigation
5. Comissão Europeia, "Data Act". https://digital-strategy.ec.europa.eu/en/policies/data-act (art. 29 conferido em data-act-text.com, URL exata não registrada)
6. The Register, "37signals is completing its on-prem move", 09/05/2025. https://www.theregister.com/2025/05/09/37signals_cloud_repatriation_storage_savings
7. AWS, "AWS Regions" (consulta em 05/10/2026). https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
8. Menlo Ventures, "2025: The State of Generative AI in the Enterprise", 09/12/2025. https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
9. Epoch AI, "The Plunging Price of Thought", 22/09/2026. https://epoch.ai/publications/the-plunging-price-of-thought
10. Epoch AI, "LLM inference prices have fallen rapidly but unequally across tasks", 12/03/2025. https://epoch.ai/data-insights/llm-inference-price-trends
11. OpenAI, "Deprecations" (consulta em 05/10/2026). https://developers.openai.com/api/docs/deprecations
12. OpenAI Developer Community, "Deprecation notice: upcoming model shutdowns in 2026", 22/04/2026. https://community.openai.com/t/deprecation-notice-upcoming-model-shutdowns-in-2026/1379553
13. TechCrunch, "Anthropic hikes the price of its Haiku model", 04/11/2024. https://techcrunch.com/2024/11/04/anthropic-hikes-the-price-of-its-haiku-model
14. Google Cloud, "Vertex AI (Generative AI) release notes", entrada de 14/05/2025. https://docs.cloud.google.com/vertex-ai/generative-ai/docs/release-notes
15. Anthropic, "Updates to Consumer Terms and Privacy Policy", 28/08/2025. https://www.anthropic.com/news/updates-to-our-consumer-terms

*Entrada de provedores na saúde*
16. TechCrunch, "Anthropic announces Claude for Healthcare...", 12/01/2026. https://techcrunch.com/2026/01/12/anthropic-announces-claude-for-healthcare-following-openais-chatgpt-health-reveal/
17. Anthropic, "Advancing Claude in healthcare and the life sciences", 11/01/2026. https://www.anthropic.com/news/healthcare-life-sciences
18. TestingCatalog, "OpenAI launches ChatGPT for Healthcare with US hospitals", 08/01/2026. https://www.testingcatalog.com/openai-launches-chatgpt-for-healthcare-with-us-hospitals/
19. The Decoder, "OpenAI launches healthcare product line...", 09/01/2026. https://the-decoder.com/openai-launches-healthcare-product-line-signs-up-major-us-hospitals/
20. Silicon Republic, "After OpenAI, Anthropic launches Claude for Healthcare", 12/01/2026. https://www.siliconrepublic.com/machines/anthropic-claude-healthcare-tools-ai-openai-data-privacy
21. Medical Economics, "OpenAI launches ChatGPT Health...", 08/01/2026. https://www.medicaleconomics.com/view/openai-launches-chatgpt-health-directly-linking-patient-portals-to-the-ai-chatbot
22. Microsoft Source, comunicado do Dragon Copilot, 03/03/2025. https://news.microsoft.com/source/2025/03/03/microsoft-dragon-copilot-provides-the-healthcare-industrys-first-unified-voice-ai-assistant-that-enables-clinicians-to-streamline-clinical-documentation-surface-information-and-automate-task/
23. Microsoft Cloud Blog, "Extending AI impact at HLTH 2025", 16/10/2025. https://www.microsoft.com/en-us/microsoft-cloud/blog/healthcare/2025/10/16/extending-ai-impact-at-hlth-2025-dragon-copilot-scales-across-care-teams-partners-and-geographies/
24. Healthcare Dive, "Amazon launches suite of healthcare AI agents", 05/03/2026. https://www.healthcaredive.com/news/amazon-web-services-launch-amazon-connect-health-ai-agent/813796/
25. Google Research, "MedGemma...", 09/07/2025. https://research.google/blog/medgemma-our-most-capable-open-models-for-health-ai-development/
26. TI Inside, "Google Cloud traz uma nova era de inovação em IA para o Brasil", 10/09/2025. https://tiinside.com.br/10/09/2025/google-cloud-traz-uma-nova-era-de-inovacao-em-ia-para-o-brasil/

*Prontuário, bundling e concorrentes*
27. Epic, "The Rise of AI-Powered Health Prediction, Featuring Epic's Curiosity", 06/03/2026. https://www.epic.com/epic/post/the-rise-of-ai-powered-health-prediction-featuring-epics-curiosity/
28. Waxler et al. (autoria principal [não verificado]), "Generative Medical Event Models Improve with Scale", arXiv:2508.12104, 16/08/2025. https://arxiv.org/html/2508.12104v1
29. Healthcare IT Today, "A Deep Dive Into the Announcements at Epic UGM 2025", 21/08/2025. https://www.healthcareittoday.com/2025/08/21/a-deep-dive-into-the-announcements-at-epic-ugm-2025/
30. Galen Growth, "Epic Joins the AI Scribe Race...", 21/08/2025 (atualizado em 05/05/2026). https://www.galengrowth.com/epic-joins-the-ai-scribe-race-can-startups-still-win/
31. Wong A. et al., JAMA Internal Medicine 181(8), 21/06/2021. https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307
32. Menlo Ventures, "2025: The State of AI in Healthcare", 21/10/2025. https://menlovc.com/perspective/2025-the-state-of-ai-in-healthcare/
33. MV, "MV se torna a 5ª maior fornecedora global de prontuário eletrônico hospitalar" (cita KLAS 2025), 04/08/2025. https://mv.com.br/imprensa/mv-se-torna-a-5a-maior-fornecedora-global-de-prontuario-eletronico-hospitalar
34. MV Blog, "MaVi: saiba mais sobre a IA da MV", 11/07/2025. https://mv.com.br/blog/mavi-saiba-mais-sobre-a-ia-da-mv
35. MV Imprensa, "MV na Hospitalar 2025...", 19/05/2025. https://mv.com.br/imprensa/mv-na-hospitalar-2025-lider-na-transformacao-digital-apresenta-o-proximo-nivel-do-uso-de-ia-na-saude
36. Baguete, "MV fatura R$ 638 milhões, alta de 27%", 24/04/2025. https://www.baguete.com.br/noticias/mv-fatura-r-638-milhoes-alta-de-27
37. Baguete, "Bionexo compra Tasy por quase R$ 1 bi", 07/05/2026. https://www.baguete.com.br/noticias/bionexo-compra-tasy-por-quase-r-1-bi
38. Exame, "Brasileira Bionexo compra plataforma da Philips por R$ 940 milhões...", 04/05/2026. https://exame.com/negocios/brasileira-bionexo-compra-plataforma-da-philips-por-r-940-milhoes-para-dominar-dados-de-saude/
39. CFF, "Farmacêutica brasileira desenvolve IA...", 05/08/2026. https://site.cff.org.br/noticia/Noticias-gerais/05/08/2026/farmaceutica-brasileira-desenvolve-ia-que-reforca-a-seguranca-das-prescricoes
40. NoHarm, site institucional. https://noharm.ai
41. InfoMoney, Laura, 20/05/2021. https://www.infomoney.com.br/negocios/como-esta-startup-reduz-internacoes-e-mortalidade-em-hospitais-e-recebeu-r-10-milhoes/
42. Exame, Laura, 20/05/2021. https://exame.com/insight/laura-startup-inteligencia-artificial-saude-10-milhoes/p
43. AWS Blog Brasil, Rede Mater Dei, 28/05/2026. https://aws.amazon.com/pt/blogs/aws-brasil/rede-mater-dei-de-saude-monitoramento-de-multiagentes-de-ia-no-ciclo-de-receita-com-amazon-bedrock-agentcore/
44. Startupi, "Arvo capta R$ 106 milhões em série A", 17/09/2025. https://startupi.com.br/arvo-capta-106-milhoes-em-serie-a/
45. InvestNews, "B3 conclui compra da Neurotech...", 15/05/2023. https://investnews.com.br/negocios/b3-conclui-compra-da-neurotech-apos-aprovacao-pelo-cade-e-cvm/
46. Planisa, site institucional (consulta em 05/10/2026). https://planisa.com.br/site/
47. Wolters Kluwer, "2025 Full-Year Report", 25/02/2026. https://www.globenewswire.com/news-release/2026/02/25/3244280/0/en/wolters-kluwer-2025-full-year-report.html
48. Mobile Time, "Rede Nacional de Dados em Saúde é instituída pelo governo", 23/07/2025. https://www.mobiletime.com.br/noticias/23/07/2025/rede-nacional-dados-saude/

*Regulação e dados*
49. Lei 13.709/2018 (LGPD), texto compilado no Planalto (consulta em 05/10/2026). https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
50. ANPD, Guia Orientativo de Agentes de Tratamento, v1, maio/2021. https://www.gov.br/anpd/pt-br/assuntos/noticias/inclusao-de-arquivos-para-link-nas-noticias/2021-05-27-guia-agentes-de-tratamento_final.pdf/@@display-file/file
51. Conjur, "Meta não pode usar dados de brasileiros para treinar IAs, diz ANPD", 02/07/2024. https://www.conjur.com.br/2024-jul-02/meta-nao-pode-usar-dados-de-brasileiros-para-treinar-ias-diz-anpd/
52. CNB/SP, análise da Resolução CD/ANPD nº 19, 30/08/2024. https://cnbsp.org.br/2024/08/30/artigo-breve-analise-sobre-a-transferencia-internacional-de-dados-resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024-por-cintia-rosa-pereira-de-lima-e-juliana-roman/
53. HIPAA Journal, Dinerstein v. UChicago/Google, 09/09/2020. https://www.hipaajournal.com/privacy-lawsuit-against-uchicago-and-google-dismissed-by-federal-judge/
54. ANVISA, RDC nº 657/2022, art. 16 (AnvisaLegis, consulta em 05/10/2026). https://anvisalegis.datalegis.net/action/ActionDatalegis.php?acao=abrirTextoAto&tipo=RDC&numeroAto=00000657&seqAto=000&valorAno=2022&orgao=RDC%2FDC%2FANVISA%2FMS&codTipo=&desItem=&desItemFim=&cod_menu=9434&cod_modulo=310&pesquisa=true
55. INOVAMED, "IA que Muda Depois de Aprovada: o Vão CFM-ANVISA", 22/08/2026. https://inovamed.pro/software-que-muda-depois-de-aprovado-cfm-anvisa/
56. CFM, Resolução 2.454/2026, 27/02/2026. https://portal.cfm.org.br/noticias/cfm-normatiza-uso-da-ia-na-medicina/
57. LCF Consulting, monitor do PL 2338/2023 (consulta em 05/10/2026). https://monitor.lcfconsulting.com.br/proposicoes/pl-2338-2023/
58. Banco Central do Brasil, SGS série 1 (PTAX), de 01/10/2021 a 05/10/2026. https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json&dataInicial=01/10/2021&dataFinal=05/10/2026

*Defensabilidade*
59. a16z, "The Empty Promise of Data Moats", 09/05/2019. https://a16z.com/the-empty-promise-of-data-moats/
60. a16z, "Context is King", 18/08/2025. https://a16z.com/context-is-king/
61. a16z, "Trading Margin for Moat", 04/06/2025. https://a16z.com/services-led-growth/
62. Shapiro e Varian, "Recognizing Lock-In" [não verificado]. https://www.inforules.com/powerpt/lockin1.pdf

*Novas: complemento 1 (base de dados e LGPD)*
63. ANPD, Guia Orientativo de Agentes de Tratamento e do Encarregado, v2.0, abr/2022, §§51-57 e 62 (lido em 05/10/2026). https://www.gov.br/anpd/pt-br/documentos-e-publicacoes/Segunda_Versao_do_Guia_de_Agentes_de_Tratamento_retificada.pdf
64. Lefosse Advogados, "ANPD publica nota técnica sobre decisões automatizadas", 23/05/2025 (fonte secundária da NT 12/2025). https://lefosse.com/noticias/inteligencia-artificial-anpd-publica-nota-tecnica-sobre-decisoes-automatizadas/
65. FTC, "FTC Finalizes Settlement with Photo App Developer..." (Everalbum), 05/2021; data exata da ordem final [não verificado]. https://www.ftc.gov/news-events/news/press-releases/2021/05/ftc-finalizes-settlement-photo-app-developer-related-misuse-facial-recognition-technology
66. FTC, "FTC Takes Action Against Company Formerly Known as Weight Watchers...", 04/03/2022. https://www.ftc.gov/news-events/news/press-releases/2022/03/ftc-takes-action-against-company-formerly-known-weight-watchers-illegally-collecting-kids-sensitive
67. FTC, "Rite Aid Banned from Using AI Facial Recognition...", 19/12/2023. https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without
68. The Register, "Google DeepMind trial failed to comply with data protection law", 03/07/2017. https://www.theregister.com/2017/07/03/google_deepmind_trial_failed_to_comply_with_data_protection_law/
69. Truveta, press release (GlobeNewswire), 13/02/2025. https://www.globenewswire.com/news-release/2025/02/13/3025934/0/en/Truveta-Data-expands-beyond-EHR-data-with-linked-closed-claims-for-more-than-200-million-patients.html

*Novas: complemento 2 (fornecedor de modelo)*
70. Zhu et al., "ClinicRealm...", npj Digital Medicine, abr/2026 (PMC13079879). https://pmc.ncbi.nlm.nih.gov/articles/PMC13079879/
71. Universidade de Freiburg, "New AI model TabPFN...", 09/01/2025 (Hollmann et al., Nature, DOI 10.1038/s41586-024-08328-6). https://uni-freiburg.de/en/new-ai-model-tabpfn-enables-faster-and-more-accurate-predictions-on-small-tabular-data-sets/
72. FDA, "FDA Roundup: December 3, 2024" (guidance PCCP final de 04/12/2024; texto integral [não verificado]). https://www.fda.gov/news-events/press-announcements/fda-roundup-december-3-2024
73. Microsoft Learn, "Foundry Models lifecycle and support policy", atualizado em 24/07/2026. https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-retirements
74. Anthropic, "Model deprecations" (consulta em 05/10/2026). https://platform.claude.com/docs/en/about-claude/model-deprecations
75. OpenAI, "Data controls in the OpenAI platform" (consulta em 05/10/2026). https://developers.openai.com/api/docs/guides/your-data
76. Anthropic Privacy Center, "Is my data used for model training?", 18/08/2026. https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
77. AWS, "Amazon Bedrock Pricing" (consulta em 05/10/2026). https://aws.amazon.com/bedrock/pricing/
78. Lambda, página de preços (consulta em 05/10/2026). https://lambda.ai/pricing
79. SemiAnalysis InferenceX, "H100 vs H200: Llama 3.3 70B" (2026). https://inferencex.semianalysis.com/compare/llama-3-3-70b-h100-vs-h200
80. AWS Solutions Library, "Guidance for Multi-Provider Generative AI Gateway on AWS" (GitHub, consulta em 05/10/2026). https://github.com/aws-solutions-library-samples/guidance-for-multi-provider-generative-ai-gateway-on-aws

*Novas: complemento 3 (compradores e internalização)*
81. Convergência Digital, "Hospital Israelita Albert Einstein: algoritmos, IA e inovação salvam vidas", 08/01/2025. https://convergenciadigital.com.br/mercado/hospital-israelita-albert-einstein-algoritmos-ia-e-inovacao-salvam-vidas/
82. Medicina S/A, "Einstein investe em uso de dados e IA...", 30/09/2024. https://medicinasa.com.br/ia-pacientes-hospitalizados/
83. Diário Indústria & Comércio, Hapvida 3T25, 14/11/2025. https://www.diarioinduscom.com.br/Noticias/872730/hapvida_mantem_trajetoria_de_crescimento_e_reforca_investimentos_em_rede_propria__inovacao_e_cuidado_coordenado_no_3t25
84. SindiPlanos, "Ranking dos maiores planos de saúde do Brasil", ref. mar/2025 (dados da ANS; fonte secundária). https://sindiplanos.org.br/ranking-dos-maiores-planos-de-saude-do-brasil/
85. Exame, "Saúde de ponta a ponta: como a Rede D'Or construiu uma gigante de 76 hospitais" (Melhores e Maiores 2026). https://exame.com/revista-exame/saude-de-ponta-a-ponta/
86. Philips, "Philips expande acesso ao Tasy EMR na Rede D'Or", 19/08/2025. https://www.philips.com.br/a-w/about/news/archive/standard/news/press/2025/20250819-philips-expands-access-to-tasy-emr-in-rede-d-or-improving-patient-care.html
87. MV Blog, "MV na Hospitalar 2025: inovação hospitalar e IA...", 16/05/2025. https://mv.com.br/blog/mv-na-hospitalar-2025-inovacao-hospitalar-e-inteligencia-artificial-redefinem-o-futuro-da-saude
88. Let's Money, "Itaú usa mais de 1,3 mil modelos de IA", 10/03/2026. https://www.letsmoney.com.br/noticias/itau-usa-mais-de-mil-modelos-ia/
89. Let's Money, "Bradesco atinge 600 casos de IA com barramento próprio", 12/09/2026. https://www.letsmoney.com.br/ia/bradesco-600-casos-ia-barramento-proprio/
90. Serasa, "Cálculo do score: entenda como é feito", 29/05/2025. https://www.serasa.com.br/score/blog/calculo-score/
91. Finsiders Brasil, "Para avançar em IA e dados, B3 compra Neurotech" (página de 23/04/2025). https://finsidersbrasil.com.br/ia/para-avancar-em-ia-e-dados-b3-compra-neurotech/
92. Mobile Time, "Porto Seguro otimiza processos de sinistro com IA", 24/04/2026. https://www.mobiletime.com.br/noticias/24/04/2026/porto-seguro-otimiza/
93. Exame, "Como essa startup encontrou R$ 1,8 bilhão em fraudes e erros nos planos de saúde" (data [não verificado]). https://exame.com/negocios/como-essa-startup-encontrou-r-18-bilhao-em-fraudes-e-erros-nos-planos-de-saude/

*Fontes internas:* Cap. 2 (PDF em `02_Fase2_O_Mercado/_Enunciado/`), Quadros 3, 4, 5, 6, 7, 9, 10 e 14 (transcritos), mais Quadros 8 e 11 (citados via complemento); `00_Lumis/Empresa_e_Contexto.md`.

*Sem URL, [não verificado]:* Anthropic, "Commitments on model deprecation and preservation" (04/11/2025); TechTarget sobre TCO de MLOps (14/05/2026); markaicode, benchmark vLLM em H100 (URL conhecida, não aberta); Azure Tech Community, PTU (403); OpenAI Scale Tier (403).

*Abertas pelo verificador, mas sem URL registrada (localizar antes de citar na entrega final):* Startupi/Bionexo (04/05/2026); Futuro da Saúde/Tasy (23/07/2025); HealthTech HotSpot/UGM 2026; Times Brasil/Epic; Exame/Kunumi (2017); Revista Apólice (08/07/2026); Forbes Brasil/Neurotech (2022); Teletime/ANPD-Meta (30/08/2024); site da Truveta; RDC 751/2022; Agenda Regulatória ANVISA 2026-2027; ficha do PL 2338/2023.

---

## 9. Notas da crítica

**Avaliação do crítico (resumo).** O crítico avaliou como professor FIAP e como analista do Vetor Capital. Considerou o levantamento forte em leitura estrutural e em honestidade analítica: tem seção de descartados, marcação [parcial] e uma resposta central sem eufemismo. Apontou três fraquezas de substância e dois pontos menores.

**Como cada lacuna foi tratada:**

1. **A resposta central dependia do Quadro 7, que estava disponível no projeto.**
   - **Tratada.** Os Quadros 7, 9, 10 e 14 foram transcritos do PDF (extração em modo bruto, células legíveis, marca d'água descartada) e incorporados às seções 0, 1, 3, 4 e 5.
   - **O veredito mudou:** a base histórica deixou de ser "único candidato a fosso" e passou a "passivo líquido hoje". A validação clínica deixou de ser "possível diferencial" e passou a "hoje é passivo".
   - **Ainda em aberto:** a linhagem de dados do modelo, a anonimização real da Sanare, o tipo da Prisma e a transcrição do Quadro 8.
   - **Pendente com você:** esses quadros estão fora da lista do enunciado, e usá-los na entrega final exige decisão sua e registro em `DECISOES.md` (seção 6.5).
2. **O poder de negociação com o fornecedor de modelo só era tratado num sentido e sem custo de troca.**
   - **Tratada.** Entraram a seção 3.1 (quatro opções com prazo, custo e efeito), a evidência de que predição tabular não exige LLM proprietário (ClinicRealm e TabPFN), os instrumentos contratuais disponíveis no mercado e a regra de revalidação da RDC 657, art. 16.
   - **Ordem de criticidade revisada:** dados de clientes passam à frente do modelo.
   - **Ainda em aberto:** volume de tokens e arquitetura da Lumis, texto do contrato, caso de migração em fonte primária e páginas da OpenAI, Azure e FDA (403/404).
3. **Faltavam o poder de barganha dos clientes e o risco de internalização.**
   - **Tratada.** Entraram as seções 2.2 e 2.3, com Einstein, Hapvida, Rede D'Or com SulAmérica, Itaú, Bradesco, Porto, Serasa e Neurotech, além da concentração da saúde suplementar.
   - **Ainda em aberto:** participação de leitos privados, TIC Saúde, Sírio-Libanês, Dasa, Unimed, Amil, BB, Santander e Nubank.
- **Pontos menores:**
  - A sobreposição Aster, MV e Tasy foi tratada **em parte**: entraram os números KLAS para a América Latina e o Tasy na Rede D'Or. Os dados só do Brasil continuam pendentes.
  - O segmento de bancos foi **ampliado**: Itaú, Bradesco, Serasa confirmada e Neurotech. Os demais bancos não foram pesquisados.

**Notas do redator:**
- **Regra de [não verificado]:** foi aplicada aos achados *externos* sem URL aberta. Os achados do tipo `dado_anexo` e `calculo` vêm do PDF do Cap. 2, que é fonte interna aberta, e por isso ficaram marcados com [Quadro N] ou [cálculo].
- **Divergências encontradas na incorporação:**
  - O LAC3 tratava a venda do Tasy à Bionexo como não verificada, mas as fontes de 05/2026 já a confirmam.
  - O earn-out da Neurotech é compatível entre as fontes se "até R$ 1,1 bi" for lido como total.
  - Truveta: 120 mi de pacientes (02/2025) contra mais de 140 mi (site atual).
  - Período dos dados do Vila Ipê anterior à fundação da empresa.
  - Margem com inferência +10% recalculada para 56,2%.
- **Para você conferir:** o complemento 3 relatou que o resumidor do WebFetch inseriu, em duas respostas sobre páginas da MV, frases sobre "skill da Arkium" que não vinham das páginas. As frases foram desconsideradas e nenhuma instrução de terceiro foi seguida. O texto exato desses trechos não foi registrado, e as afirmações tiradas dessas duas páginas (LAC3-07 e LAC3-08) devem ser conferidas na fonte antes da entrega final. Quer que essas páginas sejam reabertas para conferência?
- **Coerência não checada nesta rodada:** a seção 4 e a ordem de criticidade não foram comparadas com `00_Lumis/Compromissos_Vigentes.md`. Isso deve ser feito antes da redação final, em especial no ponto da validação, do viés e do material comercial ("94%").
- **Skills:** nenhuma skill da Arkium cobre o tema. A `arkium-governanca-dados` foi acionada por causa da LGPD, mas cobre só os manuais internos da Arkium. Nada foi gravado em arquivo nesta etapa.