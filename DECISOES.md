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

### D-008 · 05/10/2026 · [Organização] Diretrizes da F2-E1 v2 (a partir da v1 do colega)
- **Base:** a versão do colega (`F2-E1_Mapa_do_Territorio_v1_colega.pdf`) é o esqueleto. Mantêm-se a estrutura de 7 seções, a camada transversal de integração e operação e a nuance de que os R$ 340 mil da Aster são adicional sobre contrato existente.
- **Tese de "difícil de copiar":** híbrida. Parte da combinação apontada pelo colega, testa cada elemento contra os dados e conclui que hoje a combinação é frágil, a base é passivo e o fosso ainda precisa ser construído.
- **Dados:** usar também os Quadros 7, 9, 10 e 14 onde forem indispensáveis, com citação leve no texto.
- **Pesquisa externa:** seletiva, com 5 a 8 análogos reais rotulados como análogos.
- **Ordem de criticidade:** dados de clientes → modelo fundacional → câmbio → nuvem → bases clínicas.
- **Apêndice A:** os prompts do colega são substituídos pelos prompts de pesquisa do F2-A.
- **Formato:** .docx com 4 a 5 páginas de corpo, mais uma cópia em .md na pasta.
- **Equipe:** Bruno Müller, Diego Franca Evangelista, Felipe Alef, Gustavo Halfen Simon e Maria Fernanda Barros. Na identificação, só os nomes.

### D-009 · 05/10/2026 · [Lumis] Leitura do território (F2-E1 v2)
A Lumis controla de fato só a camada de aplicação. A dependência estrutural mais crítica é a de dados de clientes, e a mais rápida é a do fornecedor de modelo. A ameaça competitiva principal é a distribuição de quem já está instalado no hospital e a internalização pelos grandes compradores. Hoje, quase nada na Lumis é difícil de copiar: o fosso possível (dado de desfecho com direito de uso limpo e validação auditável por subgrupo) precisa ser construído. Esse fosso se conecta ao compromisso C2.
[fonte: F2-E1 v2]

### D-010 · 05/10/2026 · [Organização] Padrão de escrita: skill humanizer
Todo texto do LumisOS passa pela skill `humanizer` (github.com/blader/humanizer, commit 225a6f3, MIT), instalada em `.claude/skills/humanizer/` com uma adaptação para o português (`PT-BR.md`). A revisão tira marcas de texto gerado por IA (contrastes "não X, e sim Y", travessões, tríades, negrito decorativo, frases de efeito) e não altera números, fontes, hipóteses, prompts nem URLs. A primeira aplicação foi a F2-E1 v2; a versão anterior à revisão está em `_Historico/2026-10-05_F2-E1_Mapa_do_Territorio_v2.*`.
**Motivo:** pedido da equipe para que a escrita das entregas soe como texto da equipe.

### D-011 · 05/10/2026 · [Organização] A entrega fica só em .docx
Cada entrega tem um único arquivo vigente, em `.docx`. A cópia `F2-E1_Mapa_do_Territorio_v2.md` foi apagada; o `.docx` já tinha o mesmo texto revisado. Substitui a parte "mais uma cópia em .md" de D-008. Levantamento, dados transcritos e registro de prompts continuam em `.md`, porque são material de apoio.
**Motivo:** evitar duas fontes para o mesmo documento.
