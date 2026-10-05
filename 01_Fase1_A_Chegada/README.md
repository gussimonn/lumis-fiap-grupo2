# Fase 1 — A Chegada ✅

**Enunciado:** [_Enunciado/Cap01_Gestao_de_IA_Um_Caminho_sem_Volta.pdf](_Enunciado/Cap01_Gestao_de_IA_Um_Caminho_sem_Volta.pdf)

## A história
Renata Souza (CEO) chama você com urgência. Um hospital cliente notificou formalmente que o Lumis Insight rebaixava sistematicamente a prioridade de **idosos de regiões periféricas**. Ninguém sabe se o problema está no modelo ou nos dados, e a ANS quer resposta em **72 h**. Você é contratado como o primeiro **Head of AI Management** e tem cinco dias úteis para mostrar que foi a contratação certa.

## Conceitos-chave do capítulo
- **Wiener:** o risco não é a máquina se rebelar, e sim a negligência humana de delegar sem controle.
- **Simon (racionalidade limitada):** o sistema herda os limites e vieses dos dados e de quem o treinou.
- **Russell (alinhamento):** o objetivo declarado era "otimizar o fluxo clínico". O objetivo real, cuidado equitativo, nunca foi especificado.
- **As 4 perguntas do gestor:** Pronto para quem? Justo como? Auditável por quem? Responsável perante quem?

## Entregas

| Código | Entrega | O que o enunciado pede | O que entregamos |
|---|---|---|---|
| [F1-E1](F1-E1_Mapa_da_Situacao/) | Mapa da Situação (máx. 2 p.) | Relatório de entrada: o que o sistema faz, tipo de IA, erros e custo humano, origem do viés | Classificação + recomendação. Casos IBM Watson for Oncology e Epic Sepsis Model. Viés vindo dos dados históricos + falha de governança. |
| [F1-E2](F1-E2_Mapa_de_Stakeholders/) | Mapa de Stakeholders | Quem controla, usa, é afetado, financia e regula, com influência × impacto × consciência | 10 stakeholders. Contraste entre poder e impacto. Conflito entre continuidade e segurança. |
| [F1-E3](F1-E3_Declaracao_de_Intencao/) | Declaração de Intenção (máx. 1 p.) | ≥ 5 compromissos verificáveis (Transparência, Não Amplificação e Reversibilidade obrigatórios + 2 livres) | C1–C5, com C4 (Responsabilidade) e C5 (Segurança e Privacidade) como livres. Ver [Compromissos_Vigentes](../00_Lumis/Compromissos_Vigentes.md). |

## O que esta fase deixa para as próximas
- Os **compromissos C1–C5** passam a ser critério de julgamento em todas as fases.
- A **matriz de stakeholders** guia a estratégia de governança (Fases 2 e 4).
- O **diagnóstico do viés** (D-004) ganha evidência no Cap. 2: os Quadros 8 e 10 mostram variáveis proxy (CEP, custo acumulado, nº de atendimentos) e o falso negativo de 31,8% no grupo 60+ D/E.
