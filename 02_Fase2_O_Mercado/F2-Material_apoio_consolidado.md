# Lumis Intelligence — Fase 2
## Material consolidado de apoio para continuidade das Entregas 3, 4 e 5

> **Objetivo deste arquivo:** reunir, em um único lugar, os dados do case, análises já realizadas, decisões metodológicas, pontos de atenção, prompts, resultados, verificações e pendências que podem apoiar a continuidade do trabalho.
>
> Este material **não substitui a redação final das Entregas 3, 4 e 5**. A ideia é reduzir retrabalho e dar ao grupo uma base organizada para decidir o que manter, ajustar, aprofundar ou remover.

---

## 1. Como ler este material

Para evitar confusão entre dado e interpretação, usar sempre estas etiquetas mentais:

- **FATO DO CASE** — informação explícita no Anexo A ou nos materiais anteriores da Lumis.
- **CÁLCULO DERIVADO** — número calculado a partir de dados do case; deve ser reproduzível.
- **INFERÊNCIA** — interpretação sustentada pelos dados, mas não declarada literalmente pelo case.
- **PROPOSTA** — decisão, prazo, threshold, estrutura ou alocação sugerida pelo grupo.
- **PESQUISA EXTERNA** — contexto de mercado/concorrentes que não pertence ao universo fictício da Lumis.
- **LACUNA / PENDÊNCIA** — informação não fornecida ou decisão que ainda precisa ser fechada pelo grupo.

### Regra metodológica central

> Primeiro: o que o enunciado pede.  
> Depois: a evidência do case.  
> Só então: interpretação, cálculo e proposta.

Sempre que um número, cargo, prazo, threshold ou arquitetura **não estiver no case**, ele não deve aparecer como se fosse fato.

---

## 2. Tese que integra as cinco entregas

### Direção consolidada sugerida

**GO condicionado**: continuar a negociação do aporte, mas condicionar a expansão ao fortalecimento do core, da governança de dados, da equidade, da responsabilidade sobre decisões de alto impacto e da disciplina de portfólio.

Em termos práticos:

1. fortalecer o produto atual antes de escalar risco;
2. corrigir fragilidades contratuais e de governança dos dados;
3. tratar decisões de alto impacto com supervisão humana e poder real de suspensão;
4. expandir por adjacências validadas, não em todas as direções ao mesmo tempo;
5. usar critérios únicos para portfólio e go-live;
6. transformar equidade, privacidade, supervisão e prestação de contas em capacidades permanentes;
7. não confundir capital disponível com autorização para escalar.

### Evidências que sustentam essa tese

- ARR: **R$ 41,2 milhões**.
- Crescimento de receita em 12 meses: **62%**.
- Participação aproximada no mercado endereçável: **~2%**.
- **72,2%** do custo direto está denominado em USD.
- Existe fornecedor único de modelo fundacional com termos revisáveis.
- Migração de nuvem estimada em **7 meses de trabalho técnico**.
- **2,09 milhões** de registros de clientes possuem autorização para treinamento frágil ou silente.
- A base legal da LGPD por fonte **não é informada pelo case**.
- Validação histórica: acurácia de **94,1%**.
- Produção atual: acurácia de **87,6%**.
- Sensibilidade: **92,6% na validação** versus **82,3% em campo**.
- Falso negativo: **7,4% na validação** versus **17,7% em campo**.
- Pior subgrupo observado: **31,8% de falso negativo**.
- Pesquisa de clima: apenas **22% do time técnico** concorda que a empresa promete o que o produto entrega, contra **79% do Comercial**.
- eNPS técnico: **-31**; Comercial: **+16**; geral: **-12**.
- Backlog de iniciativas: **97 meses-pessoa** para **30 meses-pessoa de capacidade disponível** nos próximos seis meses.

---

# 3. Entrega 3 — A linha de responsabilidade

## 3.1 O que o enunciado exige

A entrega precisa responder:

- quais decisões estão delegadas ao sistema;
- qual o impacto de cada decisão sobre as pessoas;
- para decisões de alto impacto:
  - quem autoriza o uso;
  - quem monitora;
  - quem pode suspender;
  - em quanto tempo a suspensão pode ser executada;
- quando a revisão humana é obrigatória;
- o que muda ao entrar em novo setor/domínio.

**Regra explícita do enunciado:** nenhuma responsabilidade pode terminar em uma área; precisa terminar em um **cargo**.

---

## 3.2 Mapa de decisões já levantado

| Decisão | Volume/mês | Impacto analítico sugerido | Revisão atual | Leitura |
|---|---:|---|---|---|
| Priorização da fila | 640 mil | Alto | Amostragem de 2% | Grande volume + impacto clínico direto. Amostragem isolada é frágil diante do viés observado. |
| Sugestão de protocolo clínico | 210 mil | Alto | Obrigatória por médico | Manter humano antes da adoção clínica. |
| Risco de sinistro | 74 mil | Alto | Exceção acima de R$ 50 mil | Threshold financeiro não elimina impacto sobre pessoas. |
| Sinalização de risco de crédito | 31 mil | Alto | Obrigatória | Manter revisão antes de decisão desfavorável. |
| Roteamento de suporte | 95 mil | Médio | Nenhuma | Pode permanecer automatizado, com revisão por exceção. |

**Atenção:** a classificação “alto/médio impacto” é **proposta analítica**, não classificação oficial do case.

---

## 3.3 Linha de responsabilidade sugerida

### Priorização clínica

- **Autoriza no cliente:** autoridade clínica do hospital.
- **Monitora na Lumis:** Head of AI Management, com apoio de Dados.
- **Suspensão:** Head of AI Management determina; CTO executa tecnicamente.
- **Prazo:** “até 1 hora” deve aparecer somente como **SLA operacional proposto**, não como regra existente.
- **Revisão humana obrigatória sugerida:** redução/negação de prioridade, contestação, alerta de viés, baixa confiança, degradação ou comportamento inesperado.

### Sugestão de protocolo clínico

- **Autoriza no cliente:** Diretor/Comitê Clínico, conforme o ator efetivamente informado no case.
- **Monitora:** Head of AI Management.
- **Suspensão:** mesmo fluxo.
- **Revisão humana:** obrigatória antes da adoção pelo profissional.

### Risco de sinistro

- **Autoriza no cliente:** usar exatamente o ator fornecido pelo case.
- **Monitora:** Head of AI Management.
- **Suspensão:** mesmo fluxo.
- **Revisão humana sugerida:** resultado materialmente desfavorável e contestação.
- **Não inventar:** “Diretor de Sinistros” se esse cargo não existir explicitamente no material.

### Risco de crédito

- **Autoriza no cliente:** Comitê/Diretoria de Crédito, conforme redação exata do case.
- **Monitora:** Head of AI Management.
- **Suspensão:** mesmo fluxo.
- **Revisão humana:** obrigatória antes de uma decisão desfavorável baseada no sinal.

### Responsabilidade interna consolidada

- **Head of AI Management:** dono do gate de governança e da suspensão preventiva.
- **CTO:** execução técnica da suspensão.
- **CEO:** Go/No-Go estratégico de produto, mercado e capital.
- **Operações:** existe uma lacuna; o case não informa claramente um responsável nominal específico. Não inventar cargo.

---

## 3.4 Revisão humana — ponto crítico

Evitar escrever que todas as **640 mil priorizações mensais** serão revistas por humanos. Isso torna a proposta impraticável.

### Critérios mais defensáveis para revisão obrigatória

Revisão humana obrigatória quando houver:

- decisão desfavorável de maior impacto;
- contestação;
- alerta de viés;
- baixa confiança;
- degradação de desempenho;
- comportamento inesperado;
- impacto clínico material;
- entrada em novo domínio ainda sem validação local.

A lógica é **risk-based**, não revisão total.

---

## 3.5 Prazo de 48 horas

O prazo de **até 48 horas** para casos não urgentes contestados já aparece na Declaração de Intenção da Fase 1.

Portanto:

- pode ser mantido por coerência;
- deve ser descrito como compromisso já assumido anteriormente;
- casos urgentes devem permitir revisão humana imediata.

---

## 3.6 Novo setor ou novo país

A recomendação mais consistente não é “proibir qualquer automação”, mas adotar **modo assistido** até que o domínio seja compreendido e validado.

### Gates sugeridos

1. **Conhecimento do domínio**
   - mapa de processos;
   - danos;
   - exceções;
   - erros típicos.

2. **Qualidade dos dados**
   - cobertura;
   - lacunas;
   - representatividade;
   - mudança de distribuição.

3. **Validação local**
   - piloto;
   - análise por grupos relevantes;
   - desempenho local.

4. **Operação humana**
   - cargo responsável;
   - procedimento de contestação;
   - prazo definido.

5. **Go / No-Go**
   - decisão registrada;
   - limites;
   - plano de resposta.

### Regra sugerida

> Sem decisão final autônoma de alto impacto até que os gates de domínio, dados, validação e operação humana estejam concluídos.

---

## 3.7 O que ainda precisa ser decidido pelo grupo na Entrega 3

- [ ] O grupo banca o **SLA de 1 hora** como proposta viável?
- [ ] Qual redação final será usada para os atores do cliente sem inventar cargos?
- [ ] Quais critérios exatos disparam revisão humana na priorização?
- [ ] O “modo assistido” será adotado como regra para novos setores?
- [ ] Quem será formalmente o responsável de Operações, se o case não o informa?
- [ ] A classificação de impacto será mantida? Se sim, deixar claro que é proposta analítica.

---

# 4. Entrega 4 — Cultura e funil de inovação

## 4.1 Diagnóstico central

O conflito entre Comercial e Técnica não parece ser apenas interpessoal.

### Evidências da pesquisa de clima

| Indicador | Técnico | Comercial | Leitura |
|---|---:|---:|---|
| “Prometemos o que o produto entrega” | 22% | 79% | Gap de 57 p.p. |
| “Temos tempo adequado de validação” | 17% | 68% | Gap de 51 p.p. |
| “Sei a quem escalar problema ético” | 29% | 21% | Fragilidade transversal de governança. |
| eNPS | -31 | +16 | Experiências internas muito diferentes. |

Outros dados:

- eNPS geral: **-12**.
- Turnover total em 12 meses: **19%**.
- Turnover no time de dados: **27%**.

### Interpretação

**INFERÊNCIA:** Técnica e Comercial partem de pressupostos incompatíveis:

- Técnica: a empresa vende **confiabilidade** e precisa de tempo de validação.
- Comercial: a empresa vende **velocidade** e rigor excessivo pode atrasar o cliente.

Sem critério compartilhado de arbitragem, o conflito reaparece em:

- go-live;
- claims comerciais;
- priorização de backlog;
- tolerância a risco.

---

## 4.2 Schein — três camadas

### 1. Artefatos

Evidências observáveis:

- decisão de go-live concentrada;
- ausência de comitê de ética/risco;
- backlog de **97 PM** para **30 PM** de capacidade;
- baixa clareza sobre escalonamento ético;
- percepção muito diferente entre Técnica e Comercial.

### 2. Valores declarados

Da Fase 1:

- transparência;
- não amplificação de danos;
- reversibilidade;
- responsabilidade;
- privacidade.

Além disso:

- Comercial enfatiza valor/cliente/velocidade;
- Técnica enfatiza qualidade/risco/validação.

### 3. Pressuposto profundo

**INFERÊNCIA:** confiabilidade e velocidade são tratadas como escolhas rivais, e cada área tende a assumir que o seu critério deve prevalecer quando há conflito.

---

## 4.3 Duas intervenções já propostas

### Intervenção A — Gate único de Portfólio e IA

Participantes sugeridos:

- Head of AI Management;
- CEO como sponsor;
- CTO;
- Produto;
- Comercial;
- DPO.

Prazo sugerido:

- operar em **30 dias**;
- revisão em **90 dias**.

Sinais observáveis:

- 100% das novas iniciativas e go-lives passam pelo mesmo registro;
- nenhum go-live fora do gate;
- redução do gap de percepção em pesquisa futura.

**PROPOSTA**, não dado histórico.

### Intervenção B — Opportunity Brief + ritual quinzenal Mercado × Técnica

Cada pedido deve entrar com:

- problema;
- usuário;
- valor;
- risco;
- esforço;
- evidência.

Sinal esperado:

- redução de prioridades fora da fila;
- mais decisões registradas;
- menos conflito por interpretação informal.

---

## 4.4 Funil de inovação sugerido

### Gate 0 — Intake

Entrada:

- problema;
- usuário;
- owner;
- hipótese de valor;
- risco;
- esforço.

Encerrar se:

- não houver owner;
- não houver problema demonstrável.

### Gate 1 — Descoberta

Avançar se houver:

- aderência estratégica;
- risco preliminar aceitável;
- evidência de demanda;
- métrica;
- viabilidade.

Encerrar se:

- não houver evidência;
- esforço crescer sem novo caso.

### Gate 2 — Piloto

Avançar com:

- dados;
- controles;
- caso econômico;
- meta do piloto;
- reversão;
- ausência de no-go crítico.

Encerrar se:

- dois ciclos sem avanço;
- risco crítico.

### Gate 3 — Escala

Avançar após:

- piloto aprovado;
- economia validada;
- suporte;
- reuso;
- governança.

Encerrar se:

- baixa repetibilidade;
- custo inviável.

---

## 4.5 Critérios comuns de portfólio

Usar critérios claros, sem pseudo-precisão:

- fit com a tese e mercados atuais;
- valor para cliente/receita/retenção;
- risco e IA responsável;
- reuso;
- evidência de demanda;
- esforço/capacidade.

### Atenção aos scores

Se aparecerem scores como **85, 74 etc.**, precisam ter memória de cálculo por critério.

Se essa memória não existir, melhor retirar os números e usar avaliação qualitativa.

---

## 4.6 Backlog — leitura já construída

| Iniciativa | Esforço | Valor informado | Decisão de apoio já sugerida |
|---|---:|---|---|
| Crédito para bancos | 14 PM | R$ 8,4 mi | Avançar para descoberta/piloto |
| Expansão México | 22 PM | R$ 6,0 mi | Condicionar |
| Reescrita do pipeline de dados | 18 PM | Sem receita direta | Avançar |
| Explicabilidade | 9 PM | Retenção | Avançar |
| Agente conversacional de triagem | 11 PM | R$ 3,2 mi | Validar |
| ISO/IEC 42001 | 7 PM | Acesso a contas públicas | Avançar por gate |
| Módulo veterinário | 16 PM | R$ 2,1 mi | Recusar neste ciclo |

### Por que recusar o módulo veterinário neste ciclo

- novo domínio;
- consome **16 PM**;
- equivale a **53% da capacidade disponível atual** de 30 PM;
- representa apenas cerca de **10,7% do potencial de receita listado** entre iniciativas com valor informado;
- baixa aderência ao foco atual.

A recusa é **estratégica**, não moral.

---

## 4.7 Alocação de recursos proposta

- **55%** — melhoria do produto atual;
- **30%** — expansão adjacente;
- **15%** — transformação/plataforma.

### Interpretação

Essa proporção:

- é **proposta gerencial**;
- não deve ser apresentada como “a proporção correta”;
- pode ser revista trimestralmente;
- precisa de justificativa simples para cada bloco.

### Justificativa sugerida

**55% core:** confiabilidade, dados, explicabilidade, privacidade e governança.

**30% adjacências:** crédito, triagem e expansão internacional condicionada.

**15% transformação:** capacidades reutilizáveis de plataforma e governança.

**Não afirmar “multi-tenant”** ou outra arquitetura específica se o case não informar.

---

## 4.8 O que ainda precisa ser decidido pelo grupo na Entrega 4

- [ ] Manter ou remover scores numéricos sem memória de cálculo?
- [ ] Confirmar a alocação 55/30/15 como proposta.
- [ ] Confirmar a recusa do módulo veterinário neste ciclo.
- [ ] Confirmar as duas intervenções e seus prazos.
- [ ] Corrigir o anexo da pesquisa de clima: usar o verdadeiro Quadro 15.
- [ ] Remover qualquer arquitetura técnica não informada pelo case.
- [ ] Garantir que o diagnóstico de Schein esteja ligado às evidências da pesquisa.

---

# 5. Entrega 5 — Due diligence ESG da expansão

## 5.1 Tese central

A expansão só é defensável se:

- equidade;
- privacidade;
- governança de dados;
- supervisão humana;
- rastreabilidade;
- prestação de contas

deixarem de ser respostas pontuais e virarem capacidades permanentes.

---

## 5.2 Temas materiais já identificados

- equidade algorítmica;
- privacidade e dados sensíveis;
- governança contratual;
- qualidade e representatividade;
- supervisão e reversibilidade;
- conformidade regulatória;
- segurança cibernética;
- energia/cloud;
- diversidade do time.

### Dados úteis

- FNR de **31,8%** no subgrupo 60+ / CEP D/E.
- Melhor subgrupo: **10,6% de FNR**.
- Razão atual: aproximadamente **3,0x**.
- CEP D/E = **25% da base**.
- CEP D/E concentra **47 de 74 reclamações formais**, cerca de **63,5%** (o case arredonda para 64%).
- **2,09 mi** de registros de clientes com autorização contratual frágil ou silente.
- Política específica de saúde ainda sem versão aprovada.
- Energia/cloud: **1.240 MWh/ano**.
- Provedor: **62% de fontes renováveis**.
- Mulheres: **31% do time**, **12% da liderança**.
- Pessoas negras: **14% do time**, **6% da liderança**.

---

## 5.3 Equidade — linguagem correta

### O que os dados permitem dizer

- há **disparidade de desempenho** entre subgrupos;
- o pior subgrupo tem FNR aproximadamente 3 vezes maior que o melhor;
- há concentração desproporcional de reclamações em CEP D/E;
- isso justifica auditoria e monitoramento por subgrupo.

### O que os dados NÃO permitem afirmar

Não afirmar como fato que:

- CEP D/E “causa” o viés;
- o sistema “reproduziu desigualdades históricas” de forma causalmente comprovada;
- CEP D/E é sinônimo de vulnerabilidade econômica individual.

### Redação mais defensável

> O sistema apresentou disparidades relevantes de desempenho. Os dados são compatíveis com a hipótese de reprodução de padrões históricos, mas o case não permite concluir causalidade definitiva. O CEP deve ser tratado como possível proxy/contexto e ponto de auditoria.

---

## 5.4 Privacidade e dados sensíveis

Controles mínimos sugeridos:

### Inventário de dados

Registrar:

- fonte;
- finalidade;
- instrumento;
- vigência;
- responsável;
- retenção;
- status de autorização.

### Minimização e acesso

- classificar dados sensíveis;
- revisar acessos ao menos a cada 90 dias, em linha com compromisso da Fase 1.

### Treinamento

- impedir entrada de nova fonte com status contratual não validado.

### Transferência internacional

- DPO/Jurídico deve definir a regra antes da ativação de novo mercado;
- o case não informa quais regimes locais se aplicam.

### Incidentes

- registrar resposta;
- manter trilha por versão de modelo/dataset;
- permitir rastreabilidade.

### Nota jurídica importante

> Autorização contratual frágil ou silente é um **gap de governança**, mas não permite concluir automaticamente que o tratamento é ilegal.

A base legal aplicável **não é informada**.

---

## 5.5 Métrica pública de impacto

### Opção já construída

**Métrica:** FNR por subgrupo + razão de disparidade entre maior e menor FNR.

**Baseline atual:** ~3,0x (31,8 ÷ 10,6).

**Periodicidade sugerida:**

- quinzenal internamente;
- publicação trimestral agregada.

**Responsável sugerido:** Head of AI Management.

### Decisão associada

Se houver piora material ou superação de limite interno aprovado após validação local:

- bloquear release;
- investigar;
- revisar dados/modelo/processo.

### Cuidado com thresholds

Os limites **1,25x / 1,50x** não vêm do case.

Portanto:

- remover, se não houver justificativa;
- ou apresentar explicitamente como limite interno provisório proposto.

A atividade pede:

- métrica;
- periodicidade;
- responsável.

Ela **não exige** threshold arbitrário.

---

## 5.6 Gates ESG sugeridos para expansão

### Dados

Condição:

- nenhuma fonte de cliente com status contratual não validado entra em novo treinamento.

Evidência:

- revisão das fontes e instrumentos;
- registro central.

### Equidade

Condição:

- validação local por subgrupo antes de produção.

Evidência:

- relatório de desempenho por release e população local.

### Privacidade

Condição:

- política de dados sensíveis aprovada;
- controles ativos.

### Supervisão

Condição:

- reversões e contestações rastreáveis;
- urgentes: imediatas;
- não urgentes contestadas: até 48h.

### Prestação de contas

Condição:

- primeiro reporte público agregado de equidade.

Periodicidade sugerida:

- trimestral.

---

## 5.7 O que ainda precisa ser decidido pelo grupo na Entrega 5

- [ ] Manter escala 1–5 da materialidade ou trocar por Alta/Média/Baixa?
- [ ] Se mantiver 1–5, declarar explicitamente que é **avaliação gerencial proposta**.
- [ ] Remover ou justificar thresholds 1,25x / 1,50x.
- [ ] Confirmar FNR por subgrupo + razão de disparidade como métrica pública.
- [ ] Confirmar periodicidade e responsável.
- [ ] Revisar linguagem causal sobre CEP.
- [ ] Não presumir consentimento ou outra base legal específica.
- [ ] Confirmar gates ESG antes de escala.

---

# 6. Pontos de integração entre Entregas 3, 4 e 5

As três entregas se conectam diretamente.

### Entrega 3 → Entrega 4

Se não houver responsabilidade e gate claros, o conflito Comercial × Técnica continua sendo resolvido informalmente.

### Entrega 4 → Entrega 5

Se o funil de inovação não considerar risco, equidade e privacidade, ESG vira checagem tardia.

### Entrega 5 → Entrega 3

Se a métrica de equidade piorar, precisa existir alguém com autoridade real para suspender o uso.

### Tese integrada

> A Lumis precisa transformar governança, cultura e ESG em mecanismos operacionais de decisão — não apenas princípios declarados.

---

# 7. Prompts documentados já utilizados

## Prompt 1 — Camadas, controle e dependências

> Com base exclusivamente nas informações fornecidas no estudo de caso da Lumis Intelligence e nos quadros de porte da empresa, custos e câmbio, cadeia de fornecimento e participantes/tamanho de mercado, analise o ecossistema de IA em que a empresa opera. Identifique as camadas de infraestrutura, modelos fundacionais, dados e aplicação; o que a Lumis controla; dependências estruturais; e impactos de mudanças de preço, termos, disponibilidade ou escopo. Não invente fornecedores ou tecnologias e diferencie fatos de inferências.

### Resultado obtido

- maior controle na camada de aplicação;
- controle parcial dos dados;
- dependência relevante de nuvem e modelos fundacionais;
- impactos em custo, continuidade e qualidade tratados como inferências.

### Verificação

Confronto com os Quadros 3 a 6.

Foram removidas afirmações sobre:

- arquitetura proprietária;
- vantagem tecnológica exclusiva;
- elementos não comprovados pelo case.

---

## Prompt 2 — Concorrência e defensabilidade

> Com base exclusivamente no estudo de caso e no quadro de participantes, classifique concorrentes diretos, indiretos, potenciais e fornecedores; em seguida responda o que parece difícil de copiar na Lumis. Não presuma vantagem proprietária sem evidência e diferencie fato de hipótese.

### Resultado obtido

- Aster: concorrente direto no problema hospitalar;
- Núcleo: concorrente indireto/potencial direto;
- consultorias: substitutos/indiretos;
- fornecedor de modelo: ameaça vertical potencial;
- diferencial mais plausível: combinação de dados, integração e aprendizagem operacional.

### Verificação

- classificação competitiva mantida como inferência;
- ameaça do fornecedor sustentada pela entrada/anúncio em saúde;
- não tratar o fornecedor como concorrente direto já estabelecido sem evidência.

---

# 8. Prompts de validação que podem ser reutilizados nas Entregas 3, 4 e 5

> **Observação:** os prompts abaixo são modelos de continuidade/validação. Não devem ser descritos como “já utilizados” se o grupo não os executar.

## Entrega 3 — responsabilidade

> Com base exclusivamente no Anexo A e na Declaração de Intenção da Fase 1, identifique todas as decisões delegadas ao Lumis Insight, o volume, a revisão humana atual, os responsáveis informados e as lacunas. Separe claramente fatos do case de propostas de governança. Não invente cargos. Para cada decisão de alto impacto, proponha critérios executáveis para revisão humana e suspensão.

## Entrega 4 — cultura e portfólio

> Com base exclusivamente na pesquisa de clima, no backlog e nos materiais da Fase 1, diagnostique a cultura da Lumis nas três camadas de Schein. Use evidência explícita para sustentar cada camada. Depois proponha duas intervenções, um funil de inovação e critérios de portfólio. Não crie scores numéricos sem memória de cálculo.

## Entrega 5 — ESG

> Com base exclusivamente nos indicadores socioambientais, desempenho por subgrupo, situação contratual dos dados e compromissos da Fase 1, identifique temas materiais de ESG, riscos de equidade, privacidade, supervisão e governança. Diferencie disparidade de causalidade. Não presuma base legal. Proponha uma métrica pública com periodicidade, responsável e decisão associada.

---

# 9. Perguntas de provocação úteis para revisão do grupo

## Geral

1. Qual é a tese final em uma frase?
2. Estamos chamando cada coisa corretamente de fato, cálculo, inferência ou proposta?
3. Existe algum número “bonito” sem origem reproduzível?
4. Existe algum cargo inventado?
5. Existe alguma proposta escrita como se já fosse política da empresa?

## Entrega 3

1. O prazo de 1 hora é fato ou proposta?
2. O grupo realmente consegue defender esse SLA?
3. O prazo de 48h está ligado corretamente à Fase 1?
4. A revisão humana vale para quais casos exatamente?
5. Estamos sugerindo revisão de 640 mil decisões ou usando critério de risco?
6. Em novo setor, faz mais sentido “sem automação” ou “modo assistido”?

## Entrega 4

1. O diagnóstico de Schein nasce da pesquisa de clima ou só da interpretação?
2. Existe memória de cálculo dos scores?
3. 55/30/15 é regra ou proposta?
4. Qual é a justificativa em uma frase para cada bloco?
5. Por que recusar o veterinário?
6. Alguma arquitetura técnica foi presumida sem fonte?
7. O anexo usado é realmente o Quadro 15?

## Entrega 5

1. Podemos dizer que houve causalidade?
2. CEP D/E está sendo tratado como proxy ou como condição individual comprovada?
3. De onde vêm 1,25x / 1,50x?
4. Qual métrica pública o grupo realmente está disposto a assumir?
5. A matriz 1–5 é medição ou julgamento?
6. Estamos presumindo consentimento como base legal?
7. Quem bloqueia uma release se a disparidade piorar?

---

# 10. Contribuições e correções de pesquisa externa — manter separadas do case

Estas informações vieram de revisão externa de mercado e **não devem ser misturadas com os dados fictícios da Lumis**.

Segundo a revisão compartilhada:

- cerca de **40 fontes** foram conferidas;
- **93 links** foram testados;
- foram identificadas **13 correções**.

## Correções informadas

Remover afirmações que não constavam nas fontes verificadas:

- MV: “sepse 6–12h”;
- Rede D'Or: recall de 69%;
- Einstein: “250 profissionais”;
- Porto: “15 anos”.

Ajustes informados:

- Tasy: aquisição de **R$ 940 milhões**, equivalente a aproximadamente **€ 131 milhões**, e não € 161 milhões;
- Tasy: presença em **mais de 2.000 instituições**, não “500 hospitais”;
- Epic AI Charting: **anunciado em agosto de 2025**, não tratar como produto já lançado nessa data.

## Leituras de ameaça competitiva

### Aster

- 210 hospitais usam o sistema;
- forte vantagem de distribuição;
- o módulo tem adicional de R$ 340 mil.

**Cuidado:** não comparar R$ 340 mil diretamente com o ticket de R$ 1,084 mi da Lumis como se fossem produtos equivalentes. O valor da Aster é um **módulo adicional sobre contrato existente**.

### Núcleo

- 74 contas;
- Lumis: 38 contas;
- hoje não tem IA preditiva.

Leitura:

- não é concorrente direto idêntico hoje;
- já possui distribuição no mesmo ambiente;
- pode se tornar ameaça se avançar para IA preditiva.

### Fornecedor de modelo

Leitura:

- pode avançar verticalmente para saúde;
- a Lumis depende estruturalmente dessa camada;
- isso reforça que “usar um bom modelo” não é moat defensável por si só.

### Brecha de qualidade

- 94,1% na validação histórica;
- 87,6% em produção atual.

Leitura:

- claims antigos precisam ser contextualizados;
- “94%” não representa automaticamente desempenho atual.

---

# 11. Pontos que permanecem como hipótese ou informação indisponível

| Tema | Status | Tratamento recomendado |
|---|---|---|
| Base legal LGPD por fonte | Não informada | Registrar lacuna; não presumir a partir do contrato |
| Arquitetura técnica / multi-tenant / stack | Não informada | Não afirmar como fato |
| Thresholds de equidade | Não informados | Qualquer limite é proposta interna |
| Responsável nominal por Operações | Não informado | Não inventar; recomendar formalização |
| Causalidade do CEP no viés | Não comprovada | Tratar como proxy/ponto de auditoria |
| Scores numéricos do backlog | Não suportados sem memória | Preferir decisão qualitativa |
| SLA de suspensão em 1h | Não é histórico | Rotular como proposta |
| Proporção 55/30/15 | Não é regra do case | Rotular como proposta gerencial |
| Matriz ESG 1–5 | Não é classificação regulatória | Rotular como avaliação gerencial |

---

# 12. Checklist final para quem continuar o trabalho

## Entrega 3

- [ ] separar estado atual e desenho proposto;
- [ ] usar cargos reais;
- [ ] fechar critérios de revisão humana;
- [ ] decidir SLA proposto;
- [ ] formalizar modo assistido em novo domínio;
- [ ] manter coerência com as 48h da Fase 1.

## Entrega 4

- [ ] centralizar a pesquisa de clima no diagnóstico;
- [ ] aplicar Schein com evidência;
- [ ] remover score sem memória de cálculo;
- [ ] confirmar 55/30/15;
- [ ] confirmar recusa do veterinário;
- [ ] corrigir o anexo;
- [ ] não presumir arquitetura.

## Entrega 5

- [ ] usar disparidade, não causalidade;
- [ ] tratar CEP como possível proxy;
- [ ] retirar thresholds arbitrários;
- [ ] fechar métrica pública;
- [ ] definir periodicidade e responsável;
- [ ] não presumir base legal;
- [ ] exigir gates antes da escala.

## Integração final

- [ ] manter uma única tese;
- [ ] procurar números sem fonte;
- [ ] procurar propostas parecendo fatos;
- [ ] procurar cargos inexistentes;
- [ ] procurar contradições entre entregas;
- [ ] separar claramente pesquisa externa do case;
- [ ] documentar prompts utilizados de fato;
- [ ] registrar verificações feitas;
- [ ] garantir que o documento final seja único e articulado.

---

# 13. Estrutura sugerida para o documento final do grupo

1. Capa e identificação da equipe.
2. Memorando ao Conselho — máximo de 2 páginas.
3. Nota metodológica.
4. Entrega 1 — Mapa do Território.
5. Entrega 2 — Auditoria do Ativo.
6. Entrega 3 — Linha de Responsabilidade.
7. Entrega 4 — Cultura e Funil de Inovação.
8. Entrega 5 — Due Diligence ESG.
9. Conclusão — uma única tese de crescimento.
10. Apêndice de prompts utilizados, resultados e verificação.
11. Matrizes, tabelas e gráficos de apoio.

---

## Nota metodológica sugerida

> Os fatos e valores referentes à Lumis foram extraídos do Anexo A e dos materiais produzidos na Fase 1. Cálculos derivados são identificados como cálculos do grupo. Interpretações sobre causas, riscos ou comportamento são tratadas como inferências. Prazos, thresholds, estruturas de governança e alocações que não constam do case são apresentados explicitamente como propostas. Pesquisa externa é usada apenas para contexto de mercado e é mantida separada dos dados fictícios da Lumis.

---

## Fechamento

Este arquivo deve funcionar como **base de continuidade**, não como substituto da decisão do grupo.

A parte mais importante para a próxima etapa é preservar três coisas:

1. **rastreabilidade** — saber de onde saiu cada afirmação;
2. **honestidade analítica** — não transformar hipótese em fato;
3. **integração** — Entregas 3, 4 e 5 precisam sustentar a mesma direção estratégica.

A tese mais consistente até aqui permanece:

> **GO condicionado — fortalecer o core e a governança, corrigir riscos de dados e desempenho e só então ampliar autonomia e escala.**
