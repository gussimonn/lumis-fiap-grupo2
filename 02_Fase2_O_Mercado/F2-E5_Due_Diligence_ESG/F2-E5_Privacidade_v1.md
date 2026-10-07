# F2-E5: Privacidade e dados sensíveis na operação ampliada (v1, material de apoio)

> **Responsável:** Felipe Alef · **Data:** 07/10/2026 · **Etapa 3 de 4** da F2-E5.
> **Pergunta do enunciado:** "tratamento de privacidade e dados sensíveis na operação ampliada" [fonte: Cap. 2, Entrega 5].
> **Base:** Quadros 7 e 17, com apoio dos Quadros 12 e 13. Lei: LGPD (Lei 13.709/2018), texto compilado no Planalto, conferido em 07/10/2026 (https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) [contexto externo].
> **Aviso:** a leitura jurídica abaixo é da equipe e serve para apontar riscos. A posição final é da DPO da Lumis, Ana Beatriz Rangel [fonte: Cap. 2, Quadro 13].

---

## 1. Onde a Lumis está hoje

| Fonte | Registros | Tipo de dado | Autorização para treinamento | Ponto frágil |
|---|---|---|---|---|
| Hospital Vila Ipê | 1,2 mi atendimentos (2019 a 2026) | Saúde (sensível) | Cláusula genérica: "melhoria contínua do serviço"; vence em 03/2027 | Os dados começam em 2019, três anos antes do contrato de 2022. Com que base foram obtidos: [não consta] |
| Rede Sanare | 3,4 mi atendimentos | Saúde (sensível) | Sim, para uso agregado e anonimizado; vence em 08/2028 | Só vale se a anonimização for irreversível (LGPD, art. 12). Prova de anonimização: [não consta] |
| Seguradora Prisma | 890 mil sinistros | Sinistros; se a seguradora for de saúde, dado sensível [hipótese] | Contrato silente; vence em 12/2026 | Sem autorização e com prazo curto |
| Banco Meridiano | 410 mil operações | Financeiro | Sim, com auditoria anual do cliente; vence em 05/2028 | Depende de a auditoria anual ser feita |
| DATASUS | 14,0 mi registros | Saúde, pública | Sim | Baixo |
| Dados sintéticos | 2,1 mi registros | Gerados internamente | Sim | De quais dados foram gerados: [não consta]. Se vieram de dados de clientes, herdam as mesmas restrições [hipótese] |

[fonte: Cap. 2, Quadro 7]

- Nenhum dos seis instrumentos passou por revisão jurídica desde a assinatura [fonte: Cap. 2, texto após o Quadro 7].
- A política de privacidade para dados sensíveis de saúde está em elaboração desde 2024, sem versão aprovada [fonte: Cap. 2, Quadro 17].
- Dos 5,9 mi de registros de clientes, 3,81 mi (64,6%) têm autorização explícita, mas condicionada; 2,09 mi (35,4%) têm autorização fraca ou nenhuma; e 0% passou por revisão jurídica [fonte: Cap. 2, Quadro 7; cálculo].

Isso já entra em choque com o compromisso C5, que promete usar "apenas os dados necessários" e controlar o acesso [fonte: F1-E3].

## 2. O que a LGPD exige e onde a Lumis fica exposta

| Regra | O que diz | Risco para a Lumis |
|---|---|---|
| Art. 5º, II | Dado referente à saúde é dado pessoal sensível | Quase toda a base da Lumis é sensível |
| Art. 11 | Dado sensível só pode ser tratado com consentimento específico e destacado ou em hipóteses listadas, como tutela da saúde em procedimento feito por profissionais ou serviços de saúde | Não fica claro qual hipótese cobre o uso de dados de um hospital para treinar um produto vendido a outros clientes [hipótese; confirmar com a DPO] |
| Art. 11, § 4º | É vedado o uso compartilhado de dados de saúde entre controladores para obter vantagem econômica, salvo nos casos de prestação de serviços de saúde em benefício do titular | Uma plataforma que aprende com dados de vários clientes e vende o resultado a terceiros pode esbarrar nessa vedação [hipótese] |
| Art. 11, § 5º | É vedado às operadoras de planos de saúde usar dados de saúde para seleção de riscos na contratação e na exclusão de beneficiários | A Lumis classifica risco de sinistro para 9 seguradoras (74 mil decisões por mês) [fonte: Cap. 2, Quadros 3 e 12]. Se alguma for operadora de saúde, o uso pode ser vedado [hipótese] |
| Art. 12 | Dado anonimizado deixa de ser dado pessoal, salvo se a anonimização puder ser revertida com esforço razoável | A autorização da Sanare depende disso |
| Art. 33 | Transferência internacional só para país com proteção adequada ou com garantias, como cláusulas contratuais, ou com consentimento específico | Necessária em qualquer novo país |
| Art. 38 | A ANPD pode exigir relatório de impacto à proteção de dados, inclusive de dados sensíveis | Não consta que a Lumis tenha esse relatório [não consta] |
| Art. 52, II | Multa de até 2% do faturamento no Brasil, limitada a R$ 50 mi por infração | Com faturamento próximo do ARR de R$ 41,2 mi, cerca de R$ 0,8 mi por infração [cálculo; hipótese de faturamento igual ao ARR]. O risco maior é ter de retirar dados e retreinar o modelo (F2-E1) |

## 3. O que a expansão muda

| Frente | Risco novo | O que fazer antes |
|---|---|---|
| Plataforma | Mais clientes no mesmo modelo, com dados de um cliente melhorando o produto vendido a outro (art. 11, § 4º) [hipótese] | Separar por cliente os dados de treinamento; contrato-padrão novo, revisado pela DPO, com autorização específica para treinamento |
| Novos países e México | Dado de saúde de brasileiros processado fora do país, ou dado de mexicanos tratado no Brasil (art. 33). Lei mexicana aplicável: [não consta]; exige pesquisa externa | Definir onde os dados ficam armazenados; base para a transferência (cláusulas-padrão da ANPD); relatório de impacto por país |
| Crédito para bancos | Usar no crédito um modelo treinado com dados de saúde. Dado de saúde usado para negar crédito seria vantagem econômica com dado sensível (art. 11, § 4º) [hipótese] | Regra fixa: dado de saúde nunca alimenta modelo de crédito; modelo de crédito treinado só com dados financeiros autorizados (hoje, só o Meridiano tem autorização) |

## 4. Como medir

| # | Indicador | Hoje | Meta proposta | Responsável | Periodicidade |
|---|---|---|---|---|---|
| P1 | % dos registros de clientes usados em treinamento com autorização explícita e revisão jurídica vigente (retoma o indicador 2 da F2-E2) | 0% com revisão jurídica; 64,6% com autorização explícita [cálculo] | 100% antes de qualquer nova frente; registros sem base saem do treinamento [proposta] | Ana Beatriz Rangel (DPO) | Trimestral |
| P2 | % dos acessos a dados de pacientes revisados nos últimos 90 dias (compromisso C5) | [não consta] | 100% [fonte: F1-E3] | Ana Beatriz Rangel (DPO), com Yuri Nakamura (Dados) | A cada 90 dias |
| P3 | Incidentes de privacidade registrados e dias até a ação corretiva (compromisso C5) | Registro de incidentes existe, mas sem categoria de privacidade [fonte: Cap. 2, Quadro 14] | Registro no dia em que é identificado; ação corretiva documentada [fonte: F1-E3] | Ana Beatriz Rangel (DPO) | Mensal |

Responsáveis provisórios, a confirmar na F2-E3.

## 5. Condições de privacidade para a expansão

Recomendamos que nenhuma frente nova entre em produção antes de:

1. a política de privacidade para dados de saúde ser aprovada;
2. os seis instrumentos de dados passarem por revisão jurídica, com aditivos para a Prisma (antes de 12/2026) e o Vila Ipê (antes de 03/2027);
3. existir relatório de impacto à proteção de dados para a plataforma e para cada país;
4. no crédito, estar formalizada a regra de que dado de saúde não entra no modelo.

As condições 1 e 2 coincidem com as recomendações da F2-E1 e da F2-E2 e já podem entrar no memorando (F2-M) como condições prévias ao aporte.

## 6. Pontos para a equipe validar

- A leitura do art. 11, § 4º, aplicada à plataforma e ao crédito, é interpretação nossa. Vale citar como risco, sem afirmar violação.
- As cláusulas-padrão de transferência internacional foram regulamentadas pela ANPD (Resolução CD/ANPD nº 19/2024), conforme fonte já usada no levantamento da F2-E1 (https://cnbsp.org.br/2024/08/30/artigo-breve-analise-sobre-a-transferencia-internacional-de-dados-resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024-por-cintia-rosa-pereira-de-lima-e-juliana-roman/).
