# F2-E5: Riscos de equidade na expansão (v1, material de apoio)

> **Responsável:** Felipe Alef · **Data:** 07/10/2026 · **Etapa 2 de 4** da F2-E5.
> **Pergunta do enunciado:** "que grupos podem ser prejudicados de forma desproporcional pelo sistema no novo mercado e como isso será medido" [fonte: Cap. 2, Entrega 5].
> **Base:** Quadros 10 e 17, com apoio dos Quadros 8, 12 e 14. Expansão analisada conforme D-023.

---

## 1. Quem já é prejudicado hoje

Falso negativo é o paciente que deveria ser priorizado e foi classificado como baixa prioridade [fonte: Cap. 2, nota do Quadro 10].

| Subgrupo | Peso na base | Sensibilidade | Falso negativo | Comparado ao melhor subgrupo |
|---|---|---|---|---|
| 18 a 59, CEP A/B | 21% | 89,4% | 10,6% | referência |
| 18 a 59, CEP C | 27% | 85,7% | 14,3% | 1,3 vez |
| 18 a 59, CEP D/E | 15% | 79,8% | 20,2% | 1,9 vez |
| 60+, CEP A/B | 13% | 84,1% | 15,9% | 1,5 vez |
| 60+, CEP C | 14% | 76,5% | 23,5% | 2,2 vezes |
| 60+, CEP D/E | 10% | 68,2% | 31,8% | 3,0 vezes |

[fonte: Cap. 2, Quadro 10; razões: cálculo]

- O erro cresce com a idade e com a faixa de CEP, e os dois efeitos se somam. No grupo 60+ D/E, quase 1 em cada 3 pacientes que precisavam de prioridade não a recebe.
- Os subgrupos 60+ de CEP C e D/E, juntos, são 24% da base e têm o dobro ou o triplo do erro do melhor subgrupo.
- As reclamações apontam na mesma direção: por paciente, a faixa D/E reclama 8 vezes mais que a A/B [fonte: Cap. 2, Quadro 17; cálculo]. A empresa nunca cruzou essas reclamações com o desempenho do modelo [fonte: Cap. 2, nota do Quadro 17].
- A abertura existe só por idade e CEP. Desempenho por sexo, raça ou cor, deficiência ou tipo de plano: [não consta]. Não dá para dizer que esses grupos estão protegidos; dá para dizer que ninguém mediu.

## 2. Por que o erro tende a acompanhar a expansão

Cinco das dez variáveis de maior peso medem acesso ao sistema de saúde tanto quanto necessidade clínica [fonte: Cap. 2, Quadro 8; leitura da F2-E2]:

| Variável | Peso | O que diz medir | O que também mede |
|---|---|---|---|
| Nº de atendimentos em 24 meses | 18,4% | Necessidade de cuidado | Quem consegue ser atendido |
| Custo acumulado de procedimentos | 15,1% | Gravidade | Quem tem cobertura para gastar |
| Faixa de CEP agrupada | 8,9% | Região de residência | Renda e infraestrutura do bairro |
| Tipo de plano ou cobertura | 7,4% | Cobertura contratada | Capacidade de pagamento |
| Nº de faltas em consultas | 5,3% | Adesão ao tratamento | Transporte, trabalho e distância |

Juntas, pesam 55,1% do modelo [cálculo]. Quem tem menos acesso aparece nos dados como "menos grave" e cai na fila. Esse mecanismo não depende do país nem do setor: vai junto com o modelo para qualquer mercado novo [hipótese, coerente com o diagnóstico D-004].

## 3. Grupos em risco em cada frente da expansão

| Frente | Grupo em risco | Por quê | Evidência |
|---|---|---|---|
| Hoje, Brasil (saúde) | Idosos de CEP C e D/E | Falso negativo de 23,5% e 31,8% | [fonte: Cap. 2, Quadro 10] |
| Plataforma e novos países | Populações de baixa renda e com pouco acesso à rede de saúde no país de destino | As variáveis de acesso (55,1% do peso) penalizam quem usa menos o sistema [hipótese] | Perfil de acesso à saúde no país de destino: [não consta] |
| Caso 1: México | Subgrupos que a Lumis ainda não consegue identificar | Não há dado local de desfecho para descobrir onde o modelo erra; o erro de hoje só foi percebido porque um cliente apurou por conta própria [fonte: Cap. 2, Quadro 14] | Base mexicana de dados e de referência: [não consta] |
| Caso 2: crédito para bancos | Moradores de CEP de baixa renda e pessoas com pouco histórico financeiro | Se CEP e cobertura (16,3% do peso no modelo de saúde) forem reaproveitados, o modelo pode negar crédito por endereço [hipótese]. Crédito é acesso a serviço essencial, uma das áreas de maior exigência no AI Act [fonte: Cap. 2, seção 2] | Hoje o crédito tem revisão humana obrigatória [fonte: Cap. 2, Quadro 12]; variáveis do modelo de crédito: [não consta] |

## 4. Como medir

Proposta da equipe. Os indicadores 1 e 2 retomam os indicadores 1 e 5 da F2-E2, para que as duas entregas falem a mesma língua.

| # | Indicador | Como se calcula | Limite proposto | O que acontece se passar do limite | Periodicidade |
|---|---|---|---|---|---|
| E1 | Falso negativo por subgrupo e razão entre o pior e o melhor subgrupo | Falso negativo em produção aberto por idade × CEP; razão = pior ÷ melhor | Razão de até 1,5 vez (hoje: 3,0) [proposta] | Revisão humana obrigatória para o subgrupo afetado e, se persistir, suspensão daquela decisão até a correção, como prevê o C2 | Quinzenal, alinhada ao C2 |
| E2 | Reclamações por 1.000 pacientes, por subgrupo, cruzadas com E1 | Reclamações formais ÷ pacientes processados, por faixa de CEP e idade | Nenhuma faixa acima de 2 vezes a média [proposta] | Auditoria de equidade e investigação da causa | Mensal |
| E3 | Taxa de reversão humana por subgrupo | Classificações alteradas por profissionais (registro do C3) ÷ classificações revisadas | Diferença entre subgrupos sinalizada quando passar de 2 vezes [proposta] | Revisão das variáveis de acesso (seção 2) | Mensal |
| E4 | Representatividade antes de entrar no mercado | Peso de cada subgrupo nos dados de validação ÷ peso na população atendida no novo mercado | Todo subgrupo com amostra suficiente para medir E1 [proposta] | Sem isso, o mercado não entra em produção | Uma vez, antes da entrada; depois, anual |
| E5 | Diferença de aprovação no crédito (só no caso 2) | Taxa de aprovação de cada faixa de CEP ÷ taxa da faixa com mais aprovações | Mínimo de 0,8, por analogia com a "regra dos quatro quintos", criada nos EUA para seleção de emprego: taxa de um grupo abaixo de 80% da do grupo com maior taxa é tratada como indício de impacto desigual [contexto externo: 29 CFR § 1607.4(D), https://www.law.cornell.edu/cfr/text/29/1607.4] | Revisão humana obrigatória e retirada de CEP e cobertura do modelo de crédito | Mensal |

**Quem responde (provisório, a fechar na F2-E3):** a apuração fica com Yuri Nakamura (Dados) e a decisão de exigir revisão ou suspender fica com o Head of AI Management, como coordenador previsto no C4 [fonte: Cap. 2, Quadro 13; F1-E3].

## 5. Condição para a expansão

Do ponto de vista de equidade, recomendamos que nenhuma frente nova entre em produção antes de:

1. o E1 do Brasil estar dentro do limite, ou com revisão humana obrigatória nos subgrupos acima dele;
2. o E4 estar cumprido no novo mercado, com validação local por subgrupo;
3. no crédito, o modelo ser validado sem CEP e sem tipo de cobertura, ou com o E5 acompanhado desde o primeiro dia.

Essas condições valem para o memorando (F2-M) como "condições prévias" ao aporte.

## 6. Pontos para a equipe validar

- Os limites de E1 a E5 são propostas nossas, não números do caso. Vale discutir se 1,5 vez é rígido demais para começar.
- A "regra dos quatro quintos" foi conferida na fonte (29 CFR § 1607.4(D), aberta em 07/10/2026). Ela é dos EUA e de seleção de emprego; aqui serve só de referência para o crédito.
