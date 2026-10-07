# F2-E5: Métrica de impacto pública (v1, material de apoio)

> **Responsável:** Felipe Alef · **Data:** 07/10/2026 · **Etapa 4 de 4** da F2-E5.
> **Pergunta do enunciado:** "ao menos uma métrica de impacto que a Lumis passará a acompanhar e reportar publicamente, com a periodicidade e o responsável definidos" [fonte: Cap. 2, Entrega 5]. Hoje a Lumis não publica nenhuma [fonte: Cap. 2, Quadro 17].
> **Decisão:** D-024.

---

## 1. A métrica

**Taxa de falso negativo na priorização de atendimento, por subgrupo de idade e faixa de CEP.**

Escolhemos esse número porque:
- foi ele que originou a crise: o Hospital Vila Ipê o calculou por conta própria e o enviou junto com a notificação [fonte: Cap. 2, destaque após o Quadro 10];
- mede o dano mais grave do produto: o paciente que precisava de prioridade e não recebeu;
- mostra a distribuição que a média esconde, como pede a quarta pergunta sobre métricas ("Esconde qual distribuição?") [fonte: Cap. 2, seção 2];
- responde direto ao compromisso C2 (Não Amplificação de Danos) [fonte: F1-E3].

## 2. Ficha da métrica

| Item | Definição |
|---|---|
| O que se mede | % dos pacientes que deveriam ter sido priorizados e foram classificados como baixa prioridade, em produção |
| Abertura | 6 subgrupos (18 a 59 e 60+, por faixa de CEP A/B, C e D/E), como no Quadro 10. Nos novos mercados, a mesma abertura, adaptada à divisão de renda do país [proposta] |
| O que se publica | Para cada subgrupo: falso negativo, sensibilidade e tamanho da amostra. Mais a razão entre o pior e o melhor subgrupo e o valor do período anterior |
| Ponto de partida | 1º semestre de 2026: de 10,6% (18 a 59, A/B) a 31,8% (60+, D/E); razão de 3,0 vezes [fonte: Cap. 2, Quadro 10; cálculo] |
| Meta | Razão de até 1,5 vez em 12 meses, e nenhum subgrupo acima do falso negativo geral da validação declarada (7,4%) em 24 meses [proposta; base: Cap. 2, Quadro 9] |
| Periodicidade da publicação | Trimestral, no site da Lumis e no relatório enviado a cada cliente [proposta] |
| Acompanhamento interno | Quinzenal, como prevê o C2 [fonte: F1-E3] |
| Responsável pela publicação | Head of AI Management, que já coordena incidentes e prestação de contas pelo C4 [fonte: F1-E3; Cap. 2, Quadro 13] |
| Responsável pela apuração | Yuri Nakamura, responsável por Dados [fonte: Cap. 2, Quadro 13] |
| Verificação | Auditoria independente uma vez por ano, para que o número sobreviva ao critério do fundo: "qualquer número que não sobreviva a uma auditoria independente será tratado como passivo" [fonte: Cap. 2, 1.1] |
| O que acontece se piorar | Subgrupo acima do limite entra em revisão humana obrigatória; se persistir por dois ciclos quinzenais, o uso para aquela decisão é suspenso até a correção, como prevê o C2 [proposta; fonte: F1-E3] |

Os responsáveis são provisórios até a F2-E3 fechar a linha de responsabilidade.

## 3. Por que essa métrica não vira "métrica bonita"

Aplicamos as quatro perguntas do Cap. 2 [fonte: Cap. 2, seção 2]:

| Pergunta | Resposta |
|---|---|
| Medida em quê? | Em produção, com a base completa do período, e não num conjunto de validação montado à parte |
| Medida por quem? | Pela área de Dados, com auditoria independente anual; o tamanho da amostra de cada subgrupo é publicado junto |
| Muda alguma decisão? | Sim: dispara revisão humana obrigatória e, se persistir, a suspensão do uso naquele subgrupo |
| Esconde qual distribuição? | Nenhuma das que conhecemos: é publicada por subgrupo. Sexo, raça ou cor e deficiência ainda não são medidos [não consta] e devem entrar na abertura quando houver dado |

Há um risco de Goodhart: se a meta pesar sozinha, o modelo pode baixar o falso negativo marcando todos como prioridade [hipótese]. Por isso a sensibilidade e a proporção de pacientes priorizados também são publicadas.

## 4. Conferência contra os compromissos C1 a C5

| Compromisso | A F2-E5 contradiz? | Como a F2-E5 responde |
|---|---|---|
| C1 Transparência | Não | A métrica pública cumpre o C1 com número. A política de privacidade aprovada também é condição prévia (etapa 3) |
| C2 Não Amplificação de Danos | Não | Os indicadores E1 a E5 e a métrica pública dão número e limite ao monitoramento quinzenal por grupo e à suspensão previstos no C2 |
| C3 Reversibilidade | Não | O indicador E3 usa o registro de revisões que o C3 exige |
| C4 Responsabilidade | Não | O Head of AI Management responde pela publicação; os cargos de apuração foram nomeados |
| C5 Segurança e Privacidade | Não | Os indicadores P1 a P3 medem o C5, inclusive a revisão de acessos a cada 90 dias |

Nenhuma contradição encontrada. A F2-E5 aumenta a cobrança sobre os compromissos, porque transforma os textos de C2 e C5 em indicadores com limite e responsável.

## 5. Resultado da F2-E5 para o memorando

A expansão leva para novos mercados riscos que a Lumis ainda não resolveu em casa. As condições prévias saídas da F2-E5 são:

1. falso negativo por subgrupo dentro do limite no Brasil, ou com revisão humana obrigatória nos subgrupos acima dele;
2. validação local por subgrupo antes de entrar em cada novo mercado;
3. política de privacidade aprovada e os seis instrumentos de dados revisados, com aditivos para a Prisma e o Vila Ipê;
4. relatório de impacto à proteção de dados para a plataforma e para cada país;
5. no crédito, dado de saúde fora do modelo e acompanhamento da diferença de aprovação por faixa de CEP;
6. métrica pública de falso negativo por subgrupo publicada antes da expansão.
