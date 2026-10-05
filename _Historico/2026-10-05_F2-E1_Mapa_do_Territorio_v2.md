# Fase 2 · Entrega 1 — Mapa do Território (v2)

**Lumis Intelligence** · Outubro de 2026  
**Equipe:** Bruno Müller · Diego Franca Evangelista · Felipe Alef · Gustavo Halfen Simon · Maria Fernanda Barros

## 1. Síntese executiva do mapa do território

- **Camadas.** A Lumis controla de fato apenas a camada de **aplicação**, com o Lumis Insight. Nos **dados**, o controle é condicional. **Nuvem** e **modelo fundacional** são alugados e somam **72,2% do custo direto**, todo em dólar, enquanto a receita é 100% em reais.
- **Concorrência.** A ameaça mais forte é de **distribuição**, não de tecnologia. A Aster Health já está instalada em 210 hospitais, 8,75 vezes as 24 contas de saúde da Lumis, e vende a IA como adicional de R$ 340 mil sobre um contrato que o hospital já tem. A segunda ameaça vem dos **grandes compradores**, que conseguem desenvolver IA própria.
- **Dependências.** A dependência mais crítica é a de **dados de clientes**. É a única estrutural, e dois contratos com autorização frágil vencem entre 12/2026 e 03/2027. A mais **rápida** é a do fornecedor de modelo, com 30 dias de aviso. Se o preço desse fornecedor dobrar, a margem bruta cai de 58% para 39,5%.
- **O que é difícil de copiar.** Concordamos que o diferencial não está em uma tecnologia isolada, e sim na combinação de produto especializado, integração e conhecimento. Mas, testada contra os dados, essa combinação **hoje é frágil**: o único ativo próprio, a base histórica, é mais passivo do que fosso. O que pode vir a ser difícil de copiar ainda precisa ser construído.

## 2. Camadas do mercado de IA relevantes para a Lumis

| Camada | O que a Lumis controla | Dependência e poder de negociação | Leitura |
|---|---|---|---|
| **Infraestrutura / nuvem** | Nada; aluga. Provedor global, plano anual, desconto por volume e renovação em 04/2027. Custo de R$ 401.760 por mês (27,9% do custo direto). | Alta. Três provedores concentram 63% do mercado global (AWS 28%, Microsoft 20%, Google 15%)¹. A migração leva 7 meses. | Faltam cerca de 6 meses para a renovação e a migração leva 7. A Lumis vai renegociar sem alternativa pronta, com pouco poder de barganha. |
| **Modelos fundacionais** | Aluga de um fornecedor único, por consumo, sem compromisso de preço. Controla apenas os "ajustes próprios". Custo de R$ 637.200 por mês (44,3%), o maior item. | Muito alta. Os termos podem mudar com 30 dias de aviso. O fornecedor anunciou um módulo próprio para saúde. | O preço caiu 38% em 18 meses, o que é bom para o custo e ruim para a barreira de entrada, porque qualquer concorrente compra a mesma capacidade. O fornecedor já é concorrente potencial. |
| **Dados** | Parcial e condicionado. A base tem 22,0 mi de registros: 63,6% do DATASUS (público), 9,5% sintéticos e 26,8% de clientes. Dos dados de clientes, 35,4% não têm autorização clara para treinamento. As bases clínicas de referência são licenciadas de um consórcio. | Média a alta. O acesso é jurídico, e não só técnico: 38 contratos individuais, nenhum revisado desde a assinatura. | O único insumo que poderia ser exclusivo é também o mais frágil juridicamente. |
| **Aplicação** | Alto. O Lumis Insight é o fluxo de priorização e classificação de risco que atende 38 contas, com equipe dedicada (R$ 289 mil por mês). | Menor. Mesmo assim, o fluxo roda dentro do sistema hospitalar do cliente, que a Lumis não controla. | É onde a Lumis tem mais controle. Mas é o dono do prontuário quem decide o que entra no fluxo do hospital. |

**Leitura estrutural.** Em economias de informação, o valor migra para quem controla o gargalo (Shapiro; Varian, 1999). No caso da Lumis, os gargalos são dois: a **distribuição dentro do fluxo hospitalar**, que pertence ao dono do prontuário, e o **direito de usar dado de desfecho**, que pertence ao cliente. Nenhum dos dois é controlado pela Lumis. Ela opera espremida entre fornecedores concentrados em cima e compradores com alternativas embaixo.

**Integração e operação** funcionam como uma capacidade transversal às quatro camadas. O Lumis Insight só gera valor quando é bem implementado, compreendido e incorporado à rotina real do cliente, com suporte e treinamento adequados.

## 3. Participantes, mercado e posicionamento competitivo

O mercado endereçável no Brasil para IA aplicada à gestão clínica e de risco é estimado em R$ 2,1 bilhões em 2026, com projeção de R$ 3,4 bilhões em 2029. Isso equivale a um crescimento de cerca de **17,4% ao ano**. A Lumis tem cerca de 2% (ARR de R$ 41,2 mi) e cresce 62% ao ano. Manter os 2% em 2029 significa chegar a R$ 68 mi. Chegar a 5% exigiria crescer cerca de **60% ao ano por três anos seguidos**.

| Participante | Classificação | Mecanismo de ameaça |
|---|---|---|
| **Aster Health** | Direto atual | **Distribuição embutida.** O sistema já está em 210 hospitais, e o módulo de IA custa R$ 340 mil sobre o contrato existente. Esse valor não deve ser comparado ao ticket total da Lumis (R$ 1,084 mi). A comparação que pesa é a decisão do hospital: ativar um módulo do fornecedor que já usa ou contratar um fornecedor novo. Há análogos reais desse padrão no Brasil: a MV está em 894 hospitais na América Latina e o Tasy em 500 (KLAS, 2025)², e a Rede D'Or está ampliando o Tasy de 50 para 60 hospitais³. |
| **Núcleo Saúde Analytics** | Indireto, com potencial de virar direto | Tem 74 contas de BI hospitalar, quase o dobro da Lumis. Já está no hospital e já tem os dados e o relacionamento. Falta só a camada preditiva, que fica mais barata a cada ano. |
| **Consultorias e integradores** | Indireto atual | Já vendem projetos sob medida, de R$ 1,5 a 4,0 mi, sobre a mesma infraestrutura e os mesmos modelos. Disputam principalmente os clientes grandes. |
| **Provedores de modelo fundacional** | Fornecedor e concorrente potencial | O fornecedor da Lumis anunciou um módulo próprio para saúde. O movimento é real no mercado: a OpenAI lançou o OpenAI for Healthcare em 08/01/2026⁴, e a Anthropic lançou o Claude for Healthcare em 11/01/2026⁵ (análogos). |
| **Grandes clientes** (redes, operadoras, bancos) | Potencial, por internalização | Os compradores mais valiosos são os que mais conseguem dispensar a Lumis. Análogos: o Einstein tem perto de 120 algoritmos próprios em uso⁶, e o Itaú opera mais de 1,3 mil modelos de IA⁷. Eles são concorrentes que já "têm distribuição junto aos mesmos clientes", porque são os próprios clientes. |

**Fora da saúde.** 14 das 38 contas (36,8%) são seguradoras e bancos. A Aster não chega a esses clientes, mas os grandes compradores desses setores tendem a desenvolver IA internamente ou a comprar de birôs de dados. Isso torna a presença em três segmentos um diferencial contra a Aster, mas não contra a internalização.

**Contraevidência: distribuição não garante qualidade.** O modelo de sepse da Epic, embutido no prontuário e adotado em larga escala, teve AUC de 0,63 na validação externa e deixou de identificar 67% dos casos (Wong et al., 2021)⁸. Esse caso já foi usado no nosso Mapa da Situação. Ele abre espaço para competir por **qualidade comprovada**. Só que a Lumis tem o mesmo problema: o "94% de acurácia" vem de uma validação de 2023 com dois hospitais da mesma região. Em campo, a acurácia é de 87,6%, e o falso negativo sobe de 7,4% para 17,7%, chegando a 31,8% em pacientes com 60 anos ou mais de CEP D/E (dados de desempenho do Anexo A). Esse argumento só vale para a Lumis depois que ela corrigir essa distância.

## 4. Dependências críticas: o que acontece se cada fornecedor mudar

A tabela segue a ordem de criticidade. **Dados de clientes** vêm primeiro porque são a única dependência estrutural: sustentam o único ativo próprio e não têm substituto. O **modelo fundacional** vem em seguida porque é a dependência mais rápida, com só 30 dias de aviso. As respostas são recomendações e não práticas que a Lumis já adote.

| Dependência | Se mudar PREÇO | Se mudar TERMOS | Se mudar ESCOPO | Resposta possível |
|---|---|---|---|---|
| **1. Dados de clientes** (38 contratos). Hospital Vila Ipê: cláusula genérica, vence em 03/2027. Seguradora Prisma: contrato silente, vence em 12/2026. | Clientes podem passar a cobrar pelo dado ou exigir contrapartida. | Uma renegociação pode restringir o treinamento ou exigir a retirada de 35,4% dos dados de clientes, o que forçaria retreinar o modelo. | Clientes grandes podem levar os próprios dados para a Aster ou para o fornecedor de modelo. | Assinar aditivos de direito de uso antes dos vencimentos. Montar a linhagem de dados para isolar os registros frágeis. (A auditoria completa fica na Entrega 2.) |
| **2. Modelo fundacional** (fornecedor único, 44,3% do custo direto, 30 dias de aviso). | Com +20%, a margem bruta cai para 54,3%. Com +100%, cai para 39,5%, a queima vai a R$ 2,54 mi por mês e o runway cai de 11,6 para 8,7 meses. Há precedente: a Anthropic quadruplicou o preço do Haiku em 2024⁹. | A descontinuação de um modelo obriga a revalidar o sistema clínico. Já houve queda de desempenho depois de uma atualização do fornecedor (09/2025, registro de incidentes). | O módulo próprio de saúde transforma o fornecedor em concorrente na camada de aplicação. | Homologar um segundo fornecedor. Negociar preço e versão travados. Avaliar se o núcleo preditivo pode rodar em modelo próprio [hipótese: viável se a predição for sobre dados tabulares]. |
| **3. Câmbio** (72,2% do custo em US$, receita em R$). | Cada R$ 0,10 a mais no dólar custa R$ 19.240 por mês. Com dólar a R$ 6,00, a margem bruta é de 54,7%; a R$ 6,50, de 51,9%. | — | — | Avaliar proteção cambial e cláusula de reajuste nos contratos com clientes. Hoje, a existência de hedge não consta. |
| **4. Nuvem** (provedor global, 27,9% do custo, renovação em 04/2027). | Cada 10% de reajuste custa R$ 40.176 por mês. Como a migração leva 7 meses, a Lumis aceita a renovação praticamente sem alternativa. | Uma mudança de região ou de condições técnicas pode trazer exigências de transferência internacional de dados de saúde [hipótese]. | Os provedores de nuvem também vendem IA para saúde [hipótese de sobreposição]. | Começar já um plano de portabilidade e negociar a renovação com cláusulas de saída. |
| **5. Bases clínicas** (consórcio, 7,8% do custo). | O reajuste é indexado e não tem teto. Cada 10% custa R$ 11.204 por mês. | A renovação automática pode travar a saída. | — | Negociar teto de reajuste na renovação. |

**Cenário combinado.** Com o preço do modelo dobrado e o dólar a R$ 6,50, a margem bruta cai para **29,6%**. Isso mostra que o risco de margem se concentra em duas variáveis que a Lumis não controla. **Poder de negociação:** a Lumis é tomadora de preço nas três dependências de cima (modelo, nuvem e bases) e enfrenta, embaixo, compradores grandes que conseguem internalizar. O poder dela é maior nos clientes médios, sem time próprio de IA.

**Risco operacional transversal.** Uma implementação fraca, treinamento insuficiente ou pouca incorporação à rotina reduzem a adoção e o valor percebido do produto, mesmo com tecnologia, nuvem e dados disponíveis.

## 5. O que, exatamente, é difícil de copiar na Lumis?

Partimos da leitura de que o diferencial não está em uma tecnologia isolada, mas na combinação de produto, integração e conhecimento. Testamos cada elemento dessa combinação contra os dados:

| Elemento | Veredito hoje | Por quê |
|---|---|---|
| Modelo e tecnologia de IA | Copiável | É de terceiro e está disponível para qualquer empresa por consumo, com preço em queda. |
| Produto especializado (priorização e risco em 3 segmentos) | Parcialmente difícil | O foco é real. Mas a Aster entrega priorização embutida no hospital, e em bancos e seguradoras os grandes compradores internalizam. |
| Integração e relacionamento com 38 contas | Parcialmente difícil | O churn é de 11% ao ano: cerca de 4 contas e R$ 4,5 mi de ARR. A retenção ainda não foi testada contra um concorrente embutido no prontuário. |
| Conhecimento acumulado e equipe | Moderadamente difícil | São 48 técnicos e 4 anos de domínio, mas o conhecimento vai embora com as pessoas. |
| Base histórica de dados | **Hoje é passivo** | 63,6% é dado público. Dos dados de clientes, 35,4% não têm autorização clara para treinamento, e nenhum contrato foi revisado. Só 2 clientes da saúde fornecem dados clínicos (Quadro 7). |
| Validação clínica | **Hoje é passivo** | O "94%" não se reproduz em campo. A diferença entre validação e campo é maior justamente no grupo que originou a reclamação do hospital. |

**Resposta.** Hoje, pouco na Lumis é difícil de copiar. A combinação de produto especializado, integração e conhecimento existe, mas se apoia em um ativo de dados com direito de uso incerto e em métricas que não se reproduzem fora do ambiente de validação. Um concorrente com mais capital consegue replicar a tecnologia em meses. O dono do prontuário consegue replicar a distribuição imediatamente.

**O que pode vir a ser difícil de copiar** é o **dado de desfecho da priorização clínica em fluxo brasileiro, com direito de uso limpo, somado à prova auditável de desempenho por subgrupo**. Hoje, nem o dono do prontuário nem o provedor de modelo têm isso. Para chegar lá, três condições precisam se cumprir:

- **Regularizar os contratos de dados** antes dos vencimentos (Prisma em 12/2026 e Vila Ipê em 03/2027) e estender o direito de uso aos clientes que hoje não contribuem dados.
- **Substituir o "94%" por validação em campo, estratificada e publicada.** Isso também cumpre o nosso compromisso de Não Amplificação de Danos (Declaração de Intenção, Fase 1).
- **Concentrar a operação em hospitais e seguradoras médios**, sem time próprio de IA, onde a integração vale mais e o comprador não internaliza.

## 6. Síntese consolidada

A Lumis é uma empresa de aplicação que aluga as duas camadas de baixo, que são concentradas e cobram em dólar, e tem controle apenas condicional sobre a camada que poderia diferenciá-la, a de dados. A competição se decide menos pela qualidade do modelo e mais por quem está dentro do fluxo hospitalar e por quem tem direito de usar o dado. Nos dois casos, a Lumis está em desvantagem. As dependências mais críticas são, nesta ordem: os dados de clientes (estrutural), o modelo fundacional (rápida), o câmbio, a nuvem e as bases clínicas. A tese de crescimento a ser apresentada ao Vetor Capital precisa começar pelo que a Lumis tem de **construir** para merecer o múltiplo de 10,3 vezes o ARR, e não pelo que ela já teria de exclusivo.

## 7. Desdobramentos para as próximas entregas

- **Entrega 2 (auditoria do ativo):** contratos e direito de uso dos dados, variáveis e a distância entre as métricas comerciais e o desempenho em campo.
- **Entrega 3 (linha de responsabilidade):** quem decide trocar de fornecedor, quem aprova uma nova versão de modelo depois de mudança do fornecedor e quem pode suspender o sistema.
- **Entrega 4 (cultura e inovação):** priorizar iniciativas que reduzam dependência (dados, segundo fornecedor) antes de iniciativas de expansão.
- **Entrega 5 (ESG):** a validação por subgrupo como métrica pública de equidade.

### Referências (contexto externo, análogos reais)

1. SYNERGY RESEARCH GROUP. Q2 Cloud Market Passes $143 Billion. 30 jul. 2026. Disponível em: https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years.
2. MV. MV se torna a 5ª maior fornecedora global de prontuário eletrônico hospitalar (dados KLAS 2025). 4 ago. 2025. Disponível em: https://mv.com.br/imprensa/mv-se-torna-a-5a-maior-fornecedora-global-de-prontuario-eletronico-hospitalar.
3. PHILIPS. Philips expande acesso ao Tasy EMR na Rede D'Or. 19 ago. 2025. Disponível em: https://www.philips.com.br/a-w/about/news/archive/standard/news/press/2025/20250819-philips-expands-access-to-tasy-emr-in-rede-d-or-improving-patient-care.html.
4. TESTINGCATALOG. OpenAI launches ChatGPT for Healthcare with US hospitals. 8 jan. 2026. Disponível em: https://www.testingcatalog.com/openai-launches-chatgpt-for-healthcare-with-us-hospitals/.
5. ANTHROPIC. Advancing Claude in healthcare and the life sciences. 11 jan. 2026. Disponível em: https://www.anthropic.com/news/healthcare-life-sciences.
6. CONVERGÊNCIA DIGITAL. Hospital Israelita Albert Einstein: algoritmos, IA e inovação salvam vidas. 8 jan. 2025. Disponível em: https://convergenciadigital.com.br/mercado/hospital-israelita-albert-einstein-algoritmos-ia-e-inovacao-salvam-vidas/.
7. LET'S MONEY. Itaú usa mais de 1,3 mil modelos de IA. 2026. Disponível em: https://www.letsmoney.com.br/noticias/itau-usa-mais-de-mil-modelos-ia/.
8. WONG, A. et al. External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients. JAMA Internal Medicine, v. 181, n. 8, p. 1065-1070, 2021.
9. TECHCRUNCH. Anthropic hikes the price of its Haiku model. 4 nov. 2024. Disponível em: https://techcrunch.com/2024/11/04/anthropic-hikes-the-price-of-its-haiku-model.
10. SHAPIRO, C.; VARIAN, H. R. Information Rules: A Strategic Guide to the Network Economy. Boston: Harvard Business School Press, 1999.

*Dados da Lumis: Anexo A do Cap. 2 (Quadros 3 a 6; para dados e desempenho, Quadros 7, 9, 10 e 14). Os números calculados (margens, cenários, crescimento) partem do Quadro 4 e estão detalhados no material de apoio da equipe. As empresas reais citadas são análogos e não fazem parte do caso Lumis.*

---

## APÊNDICE A: Uso de IA generativa como instrumento de pesquisa

**Ferramenta e data:** Claude Code (Anthropic), em 05/10/2026, com subagentes autorizados a buscar e abrir páginas na web.

**Método.** A IA foi usada para **pesquisar**, não para redigir. Cinco frentes de pesquisa rodaram em paralelo: camadas, concorrência, dependências, defensabilidade e cálculos. Todas receberam o mesmo bloco de contexto, com os Quadros 3 a 6 transcritos e regras explícitas:

- não inventar números sobre a Lumis;
- não pesquisar as empresas fictícias, e sim buscar análogos reais rotulados como tal;
- citar fonte aberta para todo fato externo;
- separar fato, dado do caso, cálculo e hipótese.

Cada frente passou por um **segundo agente verificador**, instruído a tentar refutar cada achado: reabrir a fonte e refazer as contas. Dos 85 achados, 52 foram confirmados, 32 corrigidos ("parcial") e 1 descartado. Os não confirmados não entraram no texto. Abaixo estão os dois prompts de pesquisa mais usados e o prompt de verificação. Os demais estão no registro completo da equipe.

**Bloco de contexto comum (resumido):** papel de analista sênior de estratégia de IA em saúde, com experiência em due diligence de venture capital no Brasil; contexto da Lumis e do Vetor Capital; Quadros 3 a 6 na íntegra; as seis regras acima.

### Prompt 1: Concorrentes diretos, indiretos e potenciais

```text
## Tarefa: concorrentes diretos, indiretos e potenciais (incluindo quem tem distribuição)
Levante análogos REAIS no Brasil (e globais com presença no Brasil) para cada tipo de participante do Quadro 6, e acrescente tipos que o quadro não lista:
- sistemas hospitalares/prontuário eletrônico (EHR/HIS) com IA embutida ou anunciada (ex.: verificar Epic, Oracle Health/Cerner, Philips Tasy, MV, TOTVS Saúde e outros com presença no Brasil): base instalada no Brasil, recursos de IA preditiva, triagem ou priorização anunciados, com fonte e data;
- healthtechs brasileiras de IA clínica, triagem ou risco (confirme a existência e o produto de cada uma; não liste nomes sem fonte);
- BI e analytics hospitalar; consultorias e integradores que fazem IA sob medida em saúde;
- big techs e provedores de modelo com produtos de saúde (ex.: verificar ofertas de Microsoft, Google, Amazon, OpenAI, Anthropic voltadas à saúde, com data de lançamento);
- concorrentes nos outros dois segmentos da Lumis (seguradoras: classificação de sinistros; bancos: risco de crédito), pois 14 das 38 contas estão fora da saúde (Quadro 3).
Para cada um, classifique como DIRETO (mesmo problema, mesmo cliente), INDIRETO (resolve o problema de outro jeito) ou POTENCIAL (ainda não compete, mas tem distribuição nos mesmos clientes), e explique o mecanismo de ameaça. Destaque o padrão "distribuição vence qualidade isolada" (bundling no EHR) com evidência real, se existir.
```

**Resultado obtido:** 17 achados a partir de 25 buscas. O principal é o padrão de distribuição embutida no prontuário, com análogos brasileiros (MV com 894 hospitais e Tasy com 500 na América Latina, segundo o KLAS; Tasy na Rede D'Or). Também apareceram a entrada de OpenAI e Anthropic na saúde (jan/2026), healthtechs e integradores nacionais e concorrentes em seguros e crédito.

**Verificação:** 6 achados confirmados, 10 corrigidos e 1 descartado (um resultado de caso clínico atribuído à empresa errada). Uma crítica de completude apontou a ausência dos grandes compradores que desenvolvem IA própria, e uma pesquisa complementar trouxe Einstein, Itaú, Bradesco e Porto. Antes de entrarem no texto, as fontes 2 a 7 das referências foram reabertas em 05/10/2026, e os números citados foram confirmados.

### Prompt 2: Dependências críticas de fornecedores

```text
## Tarefa: dependências críticas e o que acontece se cada fornecedor mudar preço, termos ou escopo
Os quatro fornecedores estruturais estão no Quadro 5 (modelo fundacional único, nuvem global, consórcio de bases clínicas, 38 contratos de dados de clientes). Para cada um, levante PRECEDENTES REAIS que mostram que o risco é concreto:
- modelos fundacionais: casos documentados de mudança de preço, descontinuação/depreciação de modelos com prazo curto, mudanças de termos de uso ou de política de dados, e provedores lançando produto próprio para saúde (data e fonte);
- nuvem: custos e prazos típicos de migração, taxas de saída de dados (egress) e mudanças regulatórias recentes sobre elas (ex.: EU Data Act), lock-in, regiões de dados no Brasil;
- bases clínicas de referência licenciadas: como funcionam o licenciamento e os reajustes no setor (se não achar fonte, diga);
- dados de clientes: o que a LGPD (dado de saúde é sensível, art. 11) e a ANPD dizem sobre reutilizar dados de clientes para treinar modelos; precedentes de disputa contratual ou regulatória sobre uso de dados de saúde para IA;
- câmbio: volatilidade do real frente ao dólar nos últimos 3–5 anos (máximas e mínimas, com fonte, ex.: Banco Central), já que 72,2% do custo é em dólar.
Para cada fornecedor, descreva qualitativamente o impacto no negócio da Lumis se ele (i) subir preço, (ii) mudar termos, (iii) mudar escopo ou virar concorrente. A quantificação fica a cargo de outra frente; aqui foque em evidência de que o evento é plausível.
```

**Resultado obtido:** 20 achados a partir de 22 buscas. Os principais precedentes reais: descontinuação de modelos com aviso curto, o aumento de 4 vezes no preço do Haiku em 2024, a concentração da nuvem e os custos de saída, os limites da LGPD para dado de saúde (art. 11) e a volatilidade do câmbio, com PTAX entre R$ 4,62 e R$ 6,21 em cinco anos (Banco Central).

**Verificação:** 15 achados confirmados e 5 corrigidos. Uma pesquisa complementar sobre o poder de negociação com o fornecedor de modelo (alternativas e custo de troca) mudou a ordem de criticidade: os dados de clientes passaram à frente do modelo. Os cálculos de sensibilidade (margem, câmbio, runway) foram refeitos a partir do Quadro 4, e a fonte do aumento de preço do Haiku foi reaberta.

### Prompt 3: Verificação adversarial (usado em todas as frentes)

```text
Você é verificador independente e cético de uma due diligence. Sua função é REFUTAR, não confirmar. Na dúvida, marque "nao_confirmado".
[bloco de contexto comum]
## Achados a verificar: <lista de achados da frente>
## Como verificar
- fato_externo: abra a URL e confirme se a fonte diz exatamente o que a afirmação diz (número, data, autoria). Se a URL falhar, procure a mesma informação em outra fonte primária. Afirmação mais forte que a fonte = "parcial", com correção.
- dado_anexo: confira contra os quadros, palavra por palavra.
- calculo: refaça a conta. Qualquer divergência = "refutado", com o valor correto.
- hipotese: avalie se está marcada como hipótese e se é razoável.
Verifique TODOS os IDs.
```

**O que a verificação mudou:** corrigiu, entre outros, uma data de lançamento antecipada de forma indevida (um produto previsto para 2027), uma comparação "quase 10 vezes" que na verdade era 8,3 vezes, um percentual de mercado aplicado ao total quando valia só para IA generativa e uma data de fim de caixa calculada errado. **Lição:** sem a verificação, quatro erros factuais teriam entrado no texto.
