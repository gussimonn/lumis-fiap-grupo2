# Lumis Intelligence — Empresa e Contexto

Arquivo vigente. Última conferência: 04/10/2026, contra o Cap. 1 e o Cap. 2.

## Quem é

- **Lumis Intelligence:** empresa brasileira de IA fundada em 2022 por um trio de ex-pesquisadores universitários. Sede em dois andares no Itaim Bibi, São Paulo. [fonte: Cap. 1, 1.1–1.2; Cap. 2, Quadro 3]
- **Lumis Insight:** sistema de análise preditiva que aprende continuamente com os dados de uso.
  - Saúde: recomenda diagnósticos, prioriza atendimentos e sugere protocolos.
  - Bancos: avalia risco de crédito.
  - Seguradoras: classifica sinistros.
  [fonte: Cap. 1, Dossiê]
- **Posição na cadeia de IA:** camada de **aplicação**. Usa modelos fundacionais de terceiros com ajustes próprios. O ativo próprio é a base histórica de dados de clientes. [fonte: Cap. 2, 1.2 e 2.1]

## Números — fechamento do 2º tri/2026 [fonte: Cap. 2, Quadro 3 e texto do Anexo A]

| Indicador | Valor |
|---|---|
| Clientes ativos | 38 contas (24 hospitais/clínicas, 9 seguradoras, 5 bancos) |
| ARR | R$ 41,2 mi |
| Ticket médio anual | R$ 1,084 mi |
| Crescimento de receita (12 meses) | 62% |
| Churn anual de contas | 11% |
| Colaboradores | 96 (48 técnicos, 22 comercial/CS, 14 produto/design, 12 administrativo) |
| Margem bruta | 58% |
| Custo direto mensal | R$ 1,44 mi |
| Queima de caixa mensal | R$ 1,90 mi |
| Caixa disponível | R$ 22,0 mi |
| Runway | 11,6 meses |
| Custo direto em moeda estrangeira | 72,2% (câmbio R$ 5,40). A receita é 100% em BRL. |
| Mercado endereçável no Brasil (IA em gestão clínica e de risco) | R$ 2,1 bi (2026) → R$ 3,4 bi (2029). Participação da Lumis: ~2%. |

**Proposta do Vetor Capital:** R$ 120 mi por 22% da empresa. Implica avaliação pré-investimento de R$ 425,5 mi, cerca de 10,3× o ARR. A oferta vale por 60 dias.

**Base de dados:** 22,0 mi de registros no total. Desses, 5,9 mi (26,8%) são dados de clientes, e 2,09 mi (35,4% da parte contratual) têm autorização frágil ou inexistente para uso em treinamento: Hospital Vila Ipê (cláusula genérica) e Seguradora Prisma (contrato silente, vence em 12/2026). Nenhum dos 6 instrumentos foi revisado juridicamente desde a assinatura. [fonte: Cap. 2, texto após o Quadro 7]

**Desempenho:** [fonte: Cap. 2, Quadro 9 e destaque após o Quadro 10]

| Recorte | Amostra | Acurácia | Sensibilidade | Falso negativo |
|---|---|---|---|---|
| Validação 2023 (2 hospitais da mesma região) | 48.000 | 94,1% | 92,6% | 7,4% |
| Campo, base completa, 1º sem/2026 | 1.940.000 | 87,6% | 82,3% | 17,7% |

O pior subgrupo é **60+ com CEP na faixa D/E: 31,8% de falso negativo**, 3× o subgrupo de melhor desempenho. Foi esse o número que o Hospital Vila Ipê apurou e enviou junto com a notificação.

**Equidade:** a faixa D/E representa 25% da base processada e concentra 64% das reclamações formais (47 de 74). Essas reclamações nunca foram cruzadas com os dados de desempenho do modelo. [fonte: Cap. 2, Quadro 17]

**Pessoas:** eNPS de −12. Rotatividade de 19% no total e de 27% no time de dados. [fonte: Cap. 2, texto após o Quadro 15]

**Capacidade:** 30 meses-pessoa disponíveis em 6 meses, contra um backlog de 97 meses-pessoa. [fonte: Cap. 2, texto após o Quadro 16]

> Os Quadros 4–7, 10, 12 e 14–16 do Anexo A têm layout complexo. Para valores linha a linha, consultar o PDF em [02_Fase2_O_Mercado/_Enunciado/](../02_Fase2_O_Mercado/_Enunciado/). A transcrição para markdown está pendente.

## Linha do tempo da história

| Quando | Fato | Fonte |
|---|---|---|
| 2022 | Fundação | Cap. 2, Quadro 3 |
| 2023 | Montado o conjunto de validação que origina o número "94% de acurácia" | Cap. 2, 1.2 e Quadro 9 |
| 03/2025 → 07/2026 | Quatro incidentes registrados. O último é o viés etário e regional, detectado pelo Hospital Vila Ipê e ainda em tratamento. | Cap. 2, Quadro 14 [não verificado linha a linha: tabela com extração irregular] |
| 07/2026 | Pesquisa de clima (81 de 96 respondentes) | Cap. 2, Quadro 15 |
| Fase 1 | Notificação formal do hospital. A ANS pede resposta em 72 h. Renata contrata o Head of AI Management. | Cap. 1 |
| Fase 2 (+3 semanas) | O hospital aceitou o plano de contenção, o regulador recebeu a 1ª resposta e o sistema segue com revisão humana obrigatória nos casos de maior impacto. O Vetor Capital dá 60 dias para uma tese de crescimento. A Aster Health anuncia entrada no Brasil. | Cap. 2, 1.1–1.2 |

## Divergências entre capítulos (regra D-003: vale o mais recente)

| Tema | Cap. 1 | Cap. 2 (vigente) |
|---|---|---|
| Aporte de R$ 120 mi | "Aporte recente" já feito por um fundo de SP | **Proposta** do Vetor Capital, ainda não aceita, com prazo de 60 dias |
| Crescimento | "200% no último ano" | 62% de receita em 12 meses (podem ser métricas diferentes) |
| Volume de decisões | "Mais de 3 milhões por mês" | O Quadro 12 soma cerca de 1,05 mi por mês nas 5 decisões listadas |
| CTO e jurídico | Ver [Pessoas_e_Cargos.md](Pessoas_e_Cargos.md) | |
