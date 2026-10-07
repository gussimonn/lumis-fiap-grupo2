# F2-E5: Matriz de materialidade (v1, material de apoio)

> **Responsável:** Felipe Alef · **Data:** 07/10/2026 · **Etapa 1 de 4** da F2-E5.
> **Expansão analisada (D-023):** a proposta do Vetor Capital (dois novos países e o Lumis Insight virando plataforma) [fonte: Cap. 2, 1.1], com dois casos concretos do backlog: a expansão para o México e o módulo de risco de crédito para bancos [fonte: Cap. 2, Quadro 16].
> **Quadros:** 17 (indicadores socioambientais e de equidade), 10 (desempenho por subgrupo) e 7 (situação contratual dos dados), mais os Quadros 3, 11, 12, 14, 15 e 16 onde indicado.

---

## 1. Como lemos a materialidade

O Cap. 2 define materialidade como identificar "quais temas socioambientais afetam de fato o negócio e sobre quais o negócio produz impacto relevante". Por isso cada tema recebe duas notas:

- **Impacto no negócio** (risco financeiro): o tema pode reduzir receita, travar o aporte, gerar multa, litígio ou perda de cliente?
- **Impacto do negócio** (sobre pessoas e meio ambiente): o Lumis Insight pode causar dano relevante a pacientes, clientes, colaboradores ou ao ambiente?

| Nota | Critério |
|---|---|
| Alto | Há evidência no Anexo A de dano ou de risco já materializado (incidente, reclamação, contrato frágil, número publicado sem base) |
| Médio | O risco aparece nos dados, mas ainda não gerou incidente, ou a expansão pode agravá-lo [hipótese] |
| Baixo | O tema existe, mas os dados não mostram efeito relevante hoje |

Um tema é material quando tem nota Alta em pelo menos um dos dois eixos.

## 2. Temas e notas

| # | Tema | Pilar | Impacto do negócio (pessoas e ambiente) | Impacto no negócio (risco financeiro) | Material? |
|---|---|---|---|---|---|
| T1 | Equidade no acesso ao atendimento | S | **Alto.** Falso negativo de 31,8% em 60+ de CEP D/E, 3 vezes o melhor subgrupo [fonte: Cap. 2, Quadro 10]. A faixa D/E é 25% dos pacientes e concentra 64% das reclamações; por paciente, reclama 8 vezes mais que a faixa A/B [fonte: Cap. 2, Quadro 17; cálculo] | **Alto.** Originou a notificação do Hospital Vila Ipê e o incidente ainda em tratamento [fonte: Cap. 2, Quadro 14]. O Vila Ipê também é fonte de dados com cláusula frágil [fonte: Cap. 2, Quadro 7] | Sim |
| T2 | Privacidade e dados sensíveis de saúde | G/S | **Alto.** A base tem 22,0 mi de registros de saúde e de sinistros; a política de privacidade para dados de saúde está em elaboração desde 2024, sem versão aprovada [fonte: Cap. 2, Quadros 7 e 17] | **Alto.** 35,4% dos dados de clientes têm autorização fraca, nenhum dos seis instrumentos passou por revisão jurídica, e o contrato da Prisma vence em 12/2026 [fonte: Cap. 2, Quadro 7]. Multa da LGPD de até 2% do faturamento, limitada a R$ 50 mi por infração [fonte: F2-E1] | Sim |
| T3 | Transparência das decisões e das métricas | G | **Alto.** São 640 mil priorizações de fila por mês com revisão humana em 2% da amostra [fonte: Cap. 2, Quadro 12]. O paciente não sabe que foi classificado por IA [hipótese; ver C1] | **Alto.** As cinco métricas do painel comercial não se sustentam como divulgadas, e a acurácia anunciada (94%) cai para 87,6% em campo [fonte: Cap. 2, Quadros 9 e 11]. O fundo trata número não auditável como passivo [fonte: Cap. 2, 1.1]. A explicabilidade, pedida pelo regulador e pelos clientes, está no backlog [fonte: Cap. 2, Quadro 16] | Sim |
| T4 | Governança e responsabilidade sobre a IA | G | **Alto.** Não há comitê de ética nem de risco, e só o CTO libera versões do modelo [fonte: Cap. 2, nota do Quadro 12]. Dois dos quatro incidentes foram detectados pelo cliente, e um deles ficou 22 dias sem correção [fonte: Cap. 2, Quadro 14] | **Alto.** O comitê do Vetor não aprova a operação sem o capítulo ESG [fonte: Cap. 2, 1.1]. A certificação ISO/IEC 42001 está no backlog como condição de acesso a contas públicas [fonte: Cap. 2, Quadro 16] | Sim |
| T5 | Clima e retenção das equipes | S | **Médio.** eNPS de −31 no time técnico; só 21% a 29% das áreas sabem a quem escalar um problema ético [fonte: Cap. 2, Quadro 15] | **Alto.** Rotatividade de 27% no time de dados [fonte: Cap. 2, texto após o Quadro 15]. A F2-E1 classificou o conhecimento da equipe como moderadamente difícil de copiar, e ele sai com as pessoas [fonte: F2-E1] | Sim |
| T6 | Diversidade de quem decide o que o sistema otimiza | S | **Médio.** Mulheres são 18% do time técnico e 12% da liderança; pessoas negras são 6% da liderança [fonte: Cap. 2, Quadro 17]. O capítulo liga a composição das equipes ao que o sistema otimiza [fonte: Cap. 2, seção 2]; o efeito direto sobre o viés do modelo é [hipótese] | **Médio.** Sem evidência de perda de cliente ou de capital por esse motivo no Anexo A [não consta] | Não (monitorar) |
| T7 | Consumo de energia e emissões | E | **Baixo.** 1.240 MWh por ano, 75% em inferência, com 62% de fonte renovável no provedor de nuvem (38% não renovável, cerca de 471 MWh) [fonte: Cap. 2, Quadro 17; cálculo] | **Baixo.** Nenhum quadro liga energia a custo, cliente ou regulação. Como a inferência cresce com o volume, a expansão aumenta o consumo [hipótese] | Não (monitorar) |

## 3. O que a expansão muda em cada tema

| Tema | Plataforma e dois novos países (proposta do Vetor) | Caso 1: México (22 meses-pessoa, R$ 6,0 mi em 12 meses) | Caso 2: crédito para bancos (14 meses-pessoa, R$ 8,4 mi em 12 meses) |
|---|---|---|---|
| T1 Equidade | O modelo passa a classificar populações das quais a Lumis não tem histórico; o viés de hoje foi aprendido com dados que a empresa conhecia [hipótese] | Sem dado local de desfecho, a Lumis não sabe em quais subgrupos vai errar mais [hipótese]. Base mexicana de referência: [não consta] | CEP e tipo de cobertura já pesam 16,3% no modelo de saúde [fonte: Cap. 2, Quadro 8]; reaproveitados no crédito, podem negar crédito por endereço [hipótese] |
| T2 Privacidade | Mais clientes e fontes de dados com o mesmo modelo de contrato sem revisão [hipótese] | Transferência internacional de dado de saúde e outra lei de proteção de dados. Qual lei e quais regras se aplicam: [não consta] no caso; exige pesquisa externa | Só o Banco Meridiano autoriza treinamento, com auditoria anual [fonte: Cap. 2, Quadro 7]; os outros 4 bancos: [não consta] |
| T3 Transparência | Plataforma vendida em escala com as mesmas métricas do painel comercial [hipótese] | Material comercial em outro idioma e mercado, com os mesmos 94% [hipótese] | Hoje o crédito tem revisão humana obrigatória [fonte: Cap. 2, Quadro 12]; a pressão por escala pode reduzi-la [hipótese] |
| T4 Governança | Mais decisões delegadas sem comitê e com liberação de versão só pelo CTO | Operação a distância, sem estrutura local de responsabilidade [hipótese] | Decisão de crédito afeta acesso a serviço essencial, uma das áreas mais exigentes do AI Act [fonte: Cap. 2, seção 2] |
| T5 Clima | Triplicar o time técnico [fonte: Cap. 2, 1.1] com eNPS técnico de −31 | Concorre pela mesma capacidade: as duas iniciativas somam 36 meses-pessoa contra 30 disponíveis em 6 meses [fonte: Cap. 2, Quadro 16; cálculo] | (idem) |
| T7 Energia | Mais inferência, mais consumo [hipótese] | Matriz energética da nuvem no novo país: [não consta] | Volume adicional de inferência: [não consta] |

## 4. Leitura

- Cinco dos sete temas são materiais, e quatro deles (T1 a T4) têm nota Alta nos dois eixos. Todos os quatro são problemas de hoje, anteriores à expansão.
- A expansão leva para novos mercados riscos que a Lumis ainda não resolveu em casa, o mesmo ponto a que chegaram a F2-E1 e a F2-E2.
- T1 e T2 batem direto nos compromissos C2 (Não Amplificação de Danos) e C5 (Segurança e Privacidade) [fonte: Compromissos_Vigentes].
- O ambiental (T7) é o tema de menor peso. Mesmo assim entra na matriz, porque o capítulo o lista como material para IA em saúde e porque cresce com a expansão.

## 5. Próximas etapas

1. ~~Matriz de materialidade~~ (esta)
2. ~~Riscos de equidade~~ (ver [F2-E5_Equidade_v1.md](F2-E5_Equidade_v1.md))
3. ~~Privacidade e dados sensíveis~~ (ver [F2-E5_Privacidade_v1.md](F2-E5_Privacidade_v1.md))
4. ~~Métrica pública e conferência contra C1 a C5~~ (ver [F2-E5_Metrica_Publica_v1.md](F2-E5_Metrica_Publica_v1.md)). Documento montado: [F2-E5_Due_Diligence_ESG_v1.docx](F2-E5_Due_Diligence_ESG_v1.docx).
