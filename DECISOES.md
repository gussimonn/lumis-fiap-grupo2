# DECISÕES — LumisOS

Registro **append-only**: só se acrescentam entradas, nunca se apagam ou editam as anteriores. Para mudar uma decisão, crie uma nova entrada que cite a anterior ("substitui D-00X").

Tipos:
- **[Lumis]** decisão tomada como Head of AI Management. Será cobrada no Julgamento (Fase 7).
- **[Organização]** decisão sobre como esta pasta e o trabalho são conduzidos.

---

### D-001 · 04/10/2026 · [Organização] Estrutura por fase e entrega com nomes temáticos
Pastas `01_` a `07_`, uma por fase. Dentro de cada fase, uma subpasta por entrega, identificada pelo código `F<fase>-E<nº>` seguido do nome temático (ex.: `F1-E2_Mapa_de_Stakeholders`). Controle central em `ESTADO.md` e `DECISOES.md`. Base de conhecimento da empresa em `00_Lumis/`. Versões anteriores em `_Historico/`.
**Motivo:** permitir auditoria do ciclo inteiro na Fase 7 e manter o contexto de cada entrega.

### D-002 · 04/10/2026 · [Organização] Originais preservados até autorização
Os 5 PDFs da raiz foram **copiados** para a nova estrutura, sem mover nem apagar. A remoção dos originais depende de autorização explícita.

### D-003 · 04/10/2026 · [Organização] Regra para conflito entre capítulos
Quando o Cap. 1 e o Cap. 2 (ou capítulos futuros) divergirem, vale o capítulo **mais recente**, e a divergência fica sinalizada no arquivo de `00_Lumis/` correspondente.

### D-004 · Fase 1 (data não consta) · [Lumis] Diagnóstico da origem do viés
A origem mais provável do viés está nos **dados históricos**, que já refletiam menor prioridade para idosos de regiões periféricas. Somou-se a isso uma **falha de gestão e governança**: faltavam checagem, monitoramento, alerta e revisão humana.
[fonte: F1-E1]

### D-005 · Fase 1 (data não consta) · [Lumis] Prioridade da governança
Diante do conflito entre a continuidade do negócio e a segurança dos afetados, a governança deve **priorizar a segurança dos afetados**.
[fonte: F1-E2, "Leitura do mapa"]

### D-006 · Fase 1 (data não consta) · [Lumis] Declaração de Intenção com 5 compromissos
A IA é apoio à decisão e não substitui a responsabilidade humana. Foram adotados os compromissos C1 Transparência, C2 Não Amplificação de Danos, C3 Reversibilidade, C4 Responsabilidade e Prestação de Contas e C5 Segurança e Privacidade. Detalhes e pontos de cobrança em [00_Lumis/Compromissos_Vigentes.md](00_Lumis/Compromissos_Vigentes.md).
[fonte: F1-E3]

### D-007 · 05/10/2026 · [Organização] Método de pesquisa com IA da Fase 2
A pesquisa externa é feita por subagentes, com verificação adversarial independente de cada achado, e todo o registro (prompts, resultados, veredictos e material bruto) fica em `F2-A_Apendice_de_Prompts/`. Achados "não confirmado" e "refutado" não entram no texto. Antes da entrega, as URLs usadas no texto final são conferidas por pessoa.
**Motivo:** atender a regra "Pesquisa não checada não é pesquisa" (Cap. 2, Entrega 1) e manter trilha de auditoria para a Fase 7.
