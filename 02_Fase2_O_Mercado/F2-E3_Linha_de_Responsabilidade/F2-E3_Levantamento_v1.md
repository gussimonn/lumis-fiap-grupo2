# F2-E3 · Linha de Responsabilidade: levantamento consolidado v1 (revisado)

**Data:** 07/10/2026

**Status:** levantamento v1, montado a partir de duas propostas (lente de governança e lente de narrativa) e do estudo de base. Foi revisado com as correções conferidas nos originais (ver "Notas de verificação" no fim) e com a skill humanizer (`SKILL.md` e `PT-BR.md`). A revisão não alterou número, fonte, hipótese marcada nem tabela de dados (D-010). Este arquivo é material de apoio em .md e ainda não é a entrega. A entrega final será um .docx feito a partir do `Modelo_Entrega_Lumis.docx` (D-011, D-013 a D-015).

**Como foi feito:** leitura do Cap. 1, do Cap. 2, das entregas da Fase 1, da F2-E1, da F2-E2 e da F2-E5, com conferência adversarial de números, cargos, coerência e cobertura do enunciado. Não houve busca na web, e a marca d'água dos PDFs não foi reproduzida.

**Fontes**
- Cap. 2: 1.1, 1.2, 2.2 a 2.7, 4.1 a 4.3 e Quadros 2, 3, 5, 7 a 17. Os Quadros 12, 13, 14 e 16 foram conferidos de novo no `cap02_raw.txt`.
- Cap. 1: 1.1, 1.2, 2.1, 2.2, 4.2 e 4.3.
- F1-E1, F1-E2 e F1-E3 (C1 a C5), mais `00_Lumis/Compromissos_Vigentes.md`. O texto literal do C2 foi conferido na F1-E3, e a tabela de stakeholders na F1-E2.
- F2-E1 v2.
- F2-E2 v2, conferida no .docx da working tree **salvo às 15:53 de 07/10/2026**. O arquivo estava aberto no Word (arquivo de trava `~$`) e pode mudar. Conferir de novo antes de citar.
- F2-E5 v1 (já na main pelo merge `8cd89ce`).
- DECISOES.md e ESTADO.md da working tree, não commitados, conferidos agora (D-003 a D-006, D-009, D-023 a D-029 e as duas entradas duplicadas; ver §10.3).

**Legenda**

| Marcador | Uso |
|---|---|
| `[fonte: …]` | Dado conferido |
| `[fonte: conta da equipe sobre o Quadro N]` | Conta nossa sobre um quadro |
| `[hipótese]` | Leitura sem quadro que a sustente |
| `[proposta]` | Desenho de governança da equipe. Não é fato da Lumis. No .docx sai com o estilo Tag Hipótese |
| `[não consta]` | Não está nos capítulos nem nas entregas |
| `[NV]` | Referência externa não verificada. Não citar no corpo |

---

## 0. Tese (para abrir a entrega)

Hoje a Lumis delega cerca de 1,05 milhão de decisões por mês [fonte: conta da equipe sobre o Quadro 12]. Para nenhuma delas os quadros mostram um cargo da Lumis que aprovou o uso, que monitora com critério ou que tenha poder formal de suspender em prazo conhecido. Na priorização, a falta de aprovação interna está escrita [fonte: Cap. 2, Quadro 12]. Nas outras quatro decisões, [não consta]. Nenhum quadro dá a um cargo o poder de suspender [não consta]. A F1-E2 deu esse poder à "Liderança da Lumis (CEO, CTO e Head of AI Management)", em conjunto e sem prazo [fonte: F1-E2], e esta entrega o atribui a cargos individuais. Quatro fatos sustentam a tese:

1. A única alavanca formal descrita nos quadros é a liberação de versão. Ela é exclusiva do CTO, e a Lumis não tem comitê de ética nem de risco [fonte: Cap. 2, nota do Quadro 12].
2. A decisão de maior volume, a priorização da fila, foi autorizada pela "Diretoria comercial do cliente, sem aprovação interna formal" [fonte: Cap. 2, Quadro 12].
3. Dois dos quatro incidentes foram detectados pelo cliente [fonte: conta da equipe sobre o Quadro 14].
4. Só 21% a 29% das pessoas sabem a quem escalar um problema ético [fonte: Cap. 2, Quadro 15].

**Frase de abertura sugerida** [proposta]: "A decisão de maior volume do Lumis Insight, a que ordena a fila de pacientes, foi liberada por uma diretoria comercial do cliente, sem aprovação interna. O quadro registra revisão humana em 2% dos casos, e o viés foi descoberto pelo hospital [fonte: Cap. 2, Quadros 12 e 14]. Depois da crise, o capítulo fala em revisão obrigatória nos casos de maior impacto, mas o critério e o dono dessa contenção não estão escritos [não consta]. Esta entrega dá a cada decisão um cargo que autoriza, um que monitora e um que pode desligar, com prazo, e diz o que fazemos já."

**Princípios de desenho** [proposta]:
1. **Frear é fácil, religar é difícil.** Uma chave suspende. Para reativar, são precisas duas chaves e o critério de saída cumprido.
2. **Quem libera não é o único que monitora nem o único que suspende** [hipótese; por analogia com a pergunta "Medida por quem?", Cap. 2, 2.3].
3. **A autorização do cliente é necessária, mas não basta.** A Lumis também autoriza.
4. **Todo prazo de suspensão é meta até haver um teste registrado.**

**Padrão para o texto:** "O problema não é o CTO. É que só existe uma porta controlada" [hipótese apoiada no Quadro 14]. A frase descreve a estrutura e não julga pessoas.

---

## 1. O que o enunciado pede

**Enunciado, literal** [fonte: Cap. 2, seção 4, Entrega 3, p. 15-16]: "Se a Lumis vai crescer, precisa saber quem responde por quê antes de crescer — e não depois do próximo incidente." Os quatro itens pedidos:
1. "Mapa das decisões hoje delegadas ao sistema, classificadas por nível de impacto sobre as pessoas afetadas."
2. "Para cada decisão de alto impacto: quem autoriza o uso, quem monitora, quem tem poder de suspender o sistema e em que prazo essa suspensão pode ser executada."
3. "Definição dos casos em que a revisão humana é obrigatória, com o critério que sustenta essa escolha."
4. "Análise do que muda nessa estrutura caso a Lumis entre em um novo setor, considerando que a empresa não domina os dados nem os erros típicos desse novo domínio."

Dados indicados: Quadros 12, 13 e 14. O enunciado diz "Estrutura de responsabilidade" e o título do quadro diz "…responsabilidades". É só diferença de redação.

Box do enunciado: "Nenhuma linha deste documento pode terminar em uma área. Toda responsabilidade precisa terminar em um cargo."

**Regras gerais:**
- "Não invente números sobre a Lumis… identificar o que falta também é resultado de análise" [fonte: Cap. 2, p. 14].
- Conclusão sem quadro é hipótese [fonte: Cap. 2, Anexo A, p. 20].

**Critérios de avaliação** [fonte: Cap. 2, 4.3]:
- O central é a **responsabilidade nomeada**: "clareza na atribuição de responsabilidades a cargos concretos, com mecanismos exequíveis de controle e suspensão".
- Também contam:
  - honestidade analítica (registrar a fragilidade);
  - integração e defesa (coerência entre as cinco entregas);
  - disciplina estratégica (critério de recusa);
  - consistência ESG ("métrica, prazo e responsável").
- Disciplina do curso: "responsabilidade organizacional, linha de decisão, revisão humana e poder de suspensão do sistema" [fonte: Cap. 2, Quadro 2].

**Memorando do Vetor, item 4** [fonte: Cap. 2, 1.1]: "Quem responde, com nome e cargo, por cada decisão que o sistema toma. E que estrutura existe para decidir o que a empresa constrói e o que recusa construir."

**Conceito-núcleo** [fonte: Cap. 2, 2.4]: cada decisão delegada tem quem responda por ela: "quem autorizou o uso, quem definiu o limite de atuação, quem determinou em que casos há revisão humana obrigatória e quem decide desligar o sistema". Somando as colunas do enunciado, a matriz da E3 fica com: autoriza, define limite e revisão, monitora, suspende, executa e prazo.

**Perguntas explícitas**

| # | Pergunta |
|---|---|
| P1 | Quais decisões existem e qual o impacto de cada uma, com que critério? |
| P2 | Para cada decisão de alto impacto: quem autoriza, quem monitora, quem suspende e em que prazo? |
| P3 | Quando a revisão humana é obrigatória e por quê? |
| P4 | O que muda num setor cujos dados e erros a Lumis não domina? |
| P5 | Quem responde, com nome e cargo? Quem decide o que se constrói e o que se recusa? |

**Perguntas implícitas (o que o avaliador e o Vetor vão procurar)**

| # | Pergunta | Base |
|---|---|---|
| I1 | A autorização do cliente substitui a da Lumis? Na priorização, sim | Q12 |
| I2 | Quem faz contrapeso ao CTO? | Nota do Q12 |
| I3 | Quem controla a mudança que vem do fornecedor de modelo? Se ela passa pela liberação [não consta] | Q14, 09/2025; Q5 |
| I4 | Como a Lumis passa a detectar antes do cliente? | Q14 |
| I5 | Quem executa a restrição já decidida? "A F2-E3 define quem executa a restrição e com que poder" | D-026 |
| I6 | Quem responde pelas decisões sobre fornecedores? Isso foi prometido à E3 | F2-E1, seção 5 |
| I7 | O prazo de suspensão é exequível? O tempo atual é [não consta] | — |
| I8 | A revisão humana tem critério observável? Hoje há uma amostra de 2% e um corte de R$ 50 mil | Q12 |
| I9 | O que se faz agora com os gatilhos que já foram atingidos? | §5.5 |
| I10 | Comitês e diretorias do cliente são instâncias, não cargos. Quem responde do lado do cliente? | Q12; cargos [não consta] |
| I11 | O "Você" do Q13 é o Head of AI Management. Na E3 ele assina a própria linha | Cap. 1, 1.2 |

**Armadilhas a evitar:**
- Linha que termina em área, órgão ou instituição: "Dados", "Comercial", "Operação da Lumis", "Atendimento", "time de sucesso do cliente", "comitê X", "hospital", "seguradora".
- Chamar Yuri, Camila ou Marcos por um título que não consta.
- Apresentar comitê ou cargo inexistente como se existisse.
- Apresentar prazo como fato.
- Usar nomes do Cap. 1 (Rafael Campos, Daniela Meireles).
- Somar "revisão humana obrigatória nos casos de maior impacto" (Cap. 2, 1.1) com a priorização inteira.
- Usar o volume de "mais de três milhões" do Cap. 1.
- Concentrar liberar, monitorar e suspender num cargo só.
- Pôr a CEO como freio operacional.
- Atribuir intenção a pessoas.
- Citar artigo ou item de norma não conferido.
- Pôr códigos internos (C1 a C5, D-0XX) no corpo do .docx. Desde a D-031 (l. 146), as entregas citam compromissos e decisões pelo nome, porque "a banca não tem acesso aos arquivos internos".

---

## 2. Onde a E3 entra na história

- **Fase 1.**
  - Faltaram "mecanismos de checagem, monitoramento, alerta e revisão humana" [fonte: F1-E1; D-004].
  - A IA é "apoio à decisão, sem substituir a responsabilidade humana" (D-006).
  - A F1-E2 atribui à "Liderança da Lumis (CEO, CTO e Head of AI Management)" a decisão de "restringir, pausar ou suspender seu uso quando necessário". À "Equipe técnica e de dados" atribui a "capacidade técnica para implementar alterações ou suspender seu funcionamento", e aos hospitais a possibilidade de "suspender seu uso localmente" [fonte: F1-E2]. O poder existe, mas é coletivo e sem prazo.
  - O C4 dá ao Head of AI Management a coordenação de incidentes.
  - O C2 diz: "Caso seja identificado um padrão de viés, erro recorrente ou risco relevante, a causa deverá ser investigada, o sistema corrigido e, quando necessário, seu uso para aquela decisão deverá ser suspenso até a correção" [fonte: F1-E3]. A leitura de que o 31,8% já torna a suspensão necessária é da equipe [fonte: D-026].
  - O C3 fixa revisão imediata em urgência e em até 48 h nos casos contestados.
  - C1, C2 e C5 dizem só "a Lumis", sem cargo [fonte: F1-E3; Compromissos_Vigentes.md].
  - **Na E3, a Fase 1 vira organograma.**
- **Abertura do Cap. 2.** O texto diz que o sistema "continua rodando — agora com revisão humana obrigatória nos casos de maior impacto" [fonte: Cap. 2, 1.1]. O Quadro 12 registra a priorização com amostragem de 2%. A tensão está dentro do próprio Cap. 2, e por isso a D-003, que trata de conflito entre capítulos, não se aplica. O Q12 não tem data [não consta]. A seção 5.1 do Anexo traz o "fechamento do 2º trimestre de 2026", e o plano de contenção vem depois do incidente de 07/2026. Os 2% podem, portanto, ser anteriores à contenção [hipótese]. Quais são os "casos de maior impacto" [não consta]. Leitura [hipótese]: é uma contenção pós-crise de escopo indefinido, sem dono nem critério escritos. Esse é o primeiro achado da E3.
- **F2-E1.**
  - "O que faz o Lumis Insight funcionar é alugado" [fonte: F2-E1].
  - Promessa à E3: "a Entrega 3 define quem responde por cada decisão sobre fornecedores" [fonte: F2-E1, seção 5].
- **F2-E2.**
  - Definiu o que medir: cinco indicadores, cada um com a decisão que dispara (Tabela 4) [fonte: F2-E2 v2].
  - Recomendou "restringir já a recomendação automática" nos idosos de CEP C e D/E e deixou para a E3 "quem executa a restrição" [fonte: F2-E2 v2, seção 5; D-026].
  - A versão vigente tirou a coluna "Quem responde": "quem autoriza, monitora e suspende é tema da Entrega 3" [fonte: DECISOES, D-031].
  - **A E2 definiu o que medir. A E3 define quem age quando o número passa do limite.**
- **F2-E5 (Felipe Alef).**
  - Recorte de expansão: plataforma e dois países, com México e crédito como casos (D-023, que vale só para a F2-E5).
  - Métrica pública trimestral (D-024).
  - Cargos provisórios até a E3 (D-024, D-025).
  - Atribui ao Head of AI o poder de suspender.
  - A E5 depende da E3 para fechar os cargos.
- **Vetor Capital.** Propõe "triplicar o time técnico, abrir operação em dois novos países" e virar "plataforma" [fonte: Cap. 2, 1.1]. O capítulo avisa: "sem uma linha de responsabilidade explícita, a expansão para novos setores multiplica exposição sem multiplicar controle" [fonte: Cap. 2, 2.4]. No memorando, a E3 entra como condição prévia ao aporte.
- **Fase 7.** A coerência será cobrada [fonte: Cap. 2, p. 13]. Todo prazo proposto aqui vira promessa auditável. Por isso preferimos um prazo menor e testado a um ambicioso que não se cumpre.

---

## 3. Dados do Anexo

### Quadro 12, Decisões delegadas ao sistema [fonte: Cap. 2, Quadro 12, seção 5.9, p. 26]

| Decisão | Volume mensal | Revisão humana atual | Quem autorizou o uso |
|---|---|---|---|
| Priorização da fila de atendimento | 640.000 | Amostragem de 2% | Diretoria comercial do cliente, sem aprovação interna formal |
| Sugestão de protocolo clínico | 210.000 | Obrigatória, médico responsável | Comitê clínico do hospital |
| Classificação de risco de sinistro | 74.000 | Por exceção, apenas acima de R$ 50 mil | Diretoria da seguradora |
| Sinalização de risco de crédito | 31.000 | Obrigatória | Comitê de crédito do banco |
| Roteamento de mensagens de suporte | 95.000 | Nenhuma | Operação da Lumis |

Nota literal: "A Lumis não possui comitê de ética ou de risco. A decisão de colocar uma nova versão do modelo em produção é hoje exclusiva do diretor de tecnologia."

**Notas:**
- **N1. Extração.** O raw quebra a célula "Diretoria comercial / …formal", e o layout confirma o texto completo. "Diretor de tecnologia" é o CTO.
- **N2. Volumes.**
  - O total é 1.050.000 por mês, e a priorização responde por 61% [fonte: conta da equipe sobre o Quadro 12].
  - O Cap. 1 dizia "mais de três milhões". Vale o Cap. 2, com a divergência sinalizada (D-003).
  - A F2-E2 estimou cerca de 323 mil registros por mês em campo [fonte: conta da equipe sobre o Quadro 9]. A origem da diferença em relação aos 640 mil [não consta].
- **N3. Amostragem.** 2% de 640 mil dá cerca de 12.800 revisões por mês [fonte: conta da equipe sobre o Quadro 12]. Quem faz essa revisão (Lumis ou hospital), com que critério e quem a registra [não consta].
- **N4. Autorizadores.**
  - Nenhuma das cinco linhas termina em cargo. Quatro terminam em órgãos do cliente, e uma termina numa área da Lumis ("Operação") que não aparece no Q13.
  - A falta de aprovação interna só está explícita na priorização. Nas demais, aprovação interna [não consta].
- **N5. Assimetria.** O crédito (31 mil por mês) tem revisão obrigatória. A priorização (640 mil por mês, dano clínico, viés medido) tem 2%. O controle segue quem autorizou e o costume de cada setor, e não o impacto [hipótese; o erro do crédito é não consta].
- **N6. Sinistro.** O corte de R$ 50 mil é um critério financeiro da seguradora e não mede o impacto sobre o segurado. A origem do corte e a distribuição por valor [não consta].
- **N7. Aprendizado contínuo.** O Cap. 1 diz que o sistema "aprende continuamente", e o Cap. 2 fala em liberação de versões. Se há mudança fora de uma liberação discreta [não consta]. Sinalizar.

### Quadro 13, Estrutura de responsabilidades [fonte: Cap. 2, Quadro 13, seção 5.10, p. 26]

| Papel | Responsável | Escopo atual |
|---|---|---|
| Direção executiva | Renata Souza (CEO) | Decisão final sobre produto, mercado e capital |
| Tecnologia | Paulo Adjaí (CTO) | Arquitetura, modelos e liberação de versões para produção |
| Dados | Yuri Nakamura | Pipelines, qualidade de dados e conjuntos de treinamento |
| Gestão de IA | Você | Governança, risco, relação com regulador e coerência das decisões |
| Comercial | Camila Torres | Vendas, contas e material de divulgação |
| Produto | Marcos Villela | Roteiro de produto e priorização de backlog |
| Jurídico e proteção de dados | Ana Beatriz Rangel (DPO) | Contratos, conformidade e resposta a incidentes |

**Notas:**
- **N8. Cargo explícito.**
  - Só CEO, CTO e DPO têm cargo explícito no quadro. "Você" é o Head of AI Management [fonte: Cap. 1, 1.2].
  - Para Yuri, Camila e Marcos o quadro dá só o papel, e o cargo deles é [não consta].
  - Para escrever sem inventar: "Yuri Nakamura, responsável por Dados [fonte: Cap. 2, Quadro 13]", porque o quadro o coloca na coluna "Responsável". Nunca escrever "Head de Dados" ou "Diretora Comercial" como fato. Ver Q-1.
- **N9. Divergências com o Cap. 1** (D-003; vale o Cap. 2):
  - CTO: Rafael Campos (Cap. 1) e Paulo Adjaí (Cap. 2).
  - Jurídico: Daniela Meireles, diretora jurídica (Cap. 1), e Ana Beatriz Rangel, DPO (Cap. 2).
  - O motivo da troca [não consta].
- **N10. Sobreposição.** "Resposta a incidentes" está com a DPO [fonte: Q13], e o C4 dá ao Head of AI a coordenação da investigação [fonte: F1-E3]. São dois donos para o mesmo processo. A resolução está na §5.2.
- **N11. Ausentes do Q13.** Faltam papéis que outros quadros citam: "Operação da Lumis" (Q12), "Auditoria interna" e "Equipe interna" (Q14), "time de sucesso do cliente" (nota do Q17). O cargo por trás de cada um é [não consta]. Também são [não consta] a quem o Head of AI se reporta e a composição do conselho.

### Quadro 14, Registro de incidentes, últimos 24 meses [fonte: Cap. 2, Quadro 14, seção 5.11, p. 27]

| Data | Ocorrência | Detectado por | Tempo até a correção |
|---|---|---|---|
| 03/2025 | Modelo passou a descartar exames de laboratório recém-credenciado | Cliente | 22 dias |
| 09/2025 | Queda de desempenho após atualização do fornecedor de modelo | Equipe interna | 6 dias |
| 01/2026 | Duplicidade de registros inflou o número de "vidas analisadas" | Auditoria interna | Corrigido no sistema; não corrigido no material comercial |
| 07/2026 | Viés etário e regional na priorização de atendimento | Cliente (Hospital Vila Ipê) | Em tratamento |

**Notas:**
- **N12. Cabeçalho.** No PDF aparece hifenizado ("DETECTAD/O POR"). O correto é "Detectado por". O quadro não tem nota.
- **N13. Colunas que faltam.** O registro não tem severidade, responsável, quem decidiu, tempo até a contenção, se houve suspensão nem quem comunicou [não consta]. Ele mede só a "correção". O C4 exige registrar "erros, vieses identificados, revisões e decisões de suspensão" para auditoria [fonte: F1-E3], e o registro atual não atende a isso [hipótese de leitura].
- **N14. Contas** [fonte: conta da equipe sobre o Quadro 14]:
  - 2 de 4 incidentes foram detectados pelo cliente. Nenhum foi detectado por monitoramento com dono nomeado, porque "equipe interna" e "auditoria interna" são áreas.
  - Três de quatro acionariam o indicador 4 da F2-E2 ("Incidente descoberto pelo cliente, ou aberto há mais de 30 dias"): 03/2025 e 07/2026 por terem sido detectados pelo cliente, e 01/2026 por seguir aberto no material comercial [Q14], há mais de 30 dias [hipótese: a data atual do caso não consta].
  - Dois estão abertos: 01/2026 ("não corrigido no material comercial") e 07/2026 ("em tratamento") [Q14]. Há quanto tempo [não consta].

---

## 4. Item 1: mapa das decisões por impacto

### 4.1 Critério de classificação [proposta, com a base de cada eixo]

| Código | Eixo | Pergunta | Base |
|---|---|---|---|
| K1 | Natureza do dano | Afeta saúde ou vida, acesso a serviço essencial (cobertura, crédito) ou só conveniência? | Cap. 2, 2.4 ("saúde, crédito e acesso a serviços essenciais" entre os mais exigentes); Cap. 1, 4.1; nota do Q10 (falso negativo = paciente que deveria ser priorizado) |
| K2 | Reversibilidade no prazo útil | O dano pode ser desfeito antes de produzir efeito? | C3 [fonte: F1-E3]; Cap. 1, 4.3 |
| K3 | Vulnerabilidade | O afetado não escolheu o sistema? É idoso, de CEP D/E, titular de dado sensível? | Cap. 1, 4.2; Q10; Q17; F1-E2 (paciente: influência baixa, impacto muito alto) |
| K4 | Evidência de erro | Há erro medido por grupo ou incidente? | Q9, Q10, Q14; C2 |
| K5 | Controle atual | Revisão obrigatória, por amostra, por exceção ou nenhuma | Q12 |
| K6 | Escala | Volume por mês | Q12 |
| K7 | Legitimidade da autorização | Quem autorizou tinha competência para o risco? Houve aprovação interna? | Q12; Cap. 2, 2.4 |
| K8 | Domínio conhecido | A Lumis conhece os dados e os erros típicos? | Cap. 2, 2.6 |

**Regra de agregação** [proposta, testável]:
- **Alto:** K1 é saúde ou serviço essencial **e** vale pelo menos um entre K2 (irreversível no prazo útil), K3 (grupo vulnerável) e K4 (erro medido).
- **Médio:** K1 é serviço essencial, com K2 reversível e sem K3 nem K4 conhecidos.
- **Baixo:** K1 é conveniência.
- Quando K1 é saúde ou serviço essencial, um dado desconhecido em K4 ou K8 conta como alto até prova em contrário. Quando K1 é conveniência, o desconhecido não sobe o nível. Sobe a condição de reclassificação.
- K5 a K8 **não rebaixam** o nível e só aumentam a intensidade do controle. O nível e o controle atual aparecem em colunas separadas.
- Motivo: volume alto não pode servir de argumento para revisar menos, nem uma revisão já existente pode servir para rebaixar a decisão (D-005).

A referência ao AI Act entra como contexto do próprio capítulo. Artigos e anexos são [NV] e não serão citados. A ISO/IEC 42001 também entra só como contexto do capítulo, que a apresenta como norma que "formaliza a ideia de um sistema de gestão de IA, com papéis e responsabilidades definidos" [fonte: Cap. 2, 2.4], sem número de cláusula. Os termos "human-in-the-loop", "viés de automação", "RACI" e "separação de funções" [não consta] no curso. Se forem usados, entram como contexto externo, com referência conferida.

O §4.3 lista decisões humanas sobre o sistema, e não decisões delegadas a ele. Por isso fica fora do mapa do item 1 e alimenta o item 2.

### 4.2 Classificação das decisões do Quadro 12 [hipótese da equipe sobre os Quadros 9, 10, 12, 14 e 17]

| Decisão | Afetado | K1 | K2 | K3 | K4 | K5 / K7 (controle atual) | Nível | Justificativa |
|---|---|---|---|---|---|---|---|---|
| Priorização da fila | Pacientes, sem escolha | Saúde | Atraso já ocorrido não se desfaz [hipótese] | 60+ e CEP D/E [Q10; Q17] | FN em campo 17,7% contra 7,4% declarado [Q9]; 60+ D/E 31,8%, 3,0 vezes o melhor [Q10]; incidente 07/2026 [Q14] | 2% de amostra; autorização comercial sem aprovação interna [Q12] | **Alto (crítico)** | Atende a todos os eixos e tem a maior escala. A restrição da D-026 está decidida e ainda não tem executor |
| Sugestão de protocolo | Pacientes | Saúde | Reversível se o médico examina | Pacientes [hipótese] | Erro por subgrupo [não consta]; ligação com o incidente de 03/2025 [não consta] | Revisão obrigatória pelo médico; comitê clínico [Q12] | **Alto** | O controle atual é forte. Risco residual: aceitar a sugestão sem exame [hipótese; conceito externo]. Taxa de aceitação sem alteração [não consta] |
| Risco de crédito | Tomadores (não mapeados na F1-E2) | Serviço essencial [Cap. 2, 2.4] | Reversível com revisão | CEP de baixa renda, se a variável for usada [hipótese; uso no crédito não consta] | [não consta] (vale como alto pela regra) | Revisão obrigatória; comitê do banco [Q12]; o Meridiano tem auditoria anual do cliente sobre dados [Q7] | **Alto** | O controle atual é forte. Dano no acesso a crédito. Critério da revisão [não consta] |
| Risco de sinistro | Segurados (não mapeados) | Acesso a cobertura [hipótese]; toca saúde se a seguradora for operadora de saúde [não consta] | Depende de levar a negativa ou atraso; efeito [não consta] | [não consta] | [não consta] (vale como alto pela regra) | Revisão só acima de R$ 50 mil; diretoria da seguradora [Q12] | **Alto provisório** [hipótese] | Sem erro medido não dá para rebaixar. Abaixo de R$ 50 mil, que pode ser a maioria, não há revisão. A equipe pode preferir médio-alto (Q-6) |
| Roteamento de suporte | Usuários do suporte (perfil [não consta]) | Conveniência [hipótese] | Reversível | [não consta] | [não consta] | Nenhuma revisão; "Operação da Lumis" (área) | **Baixo, condicionado** | Sobe para médio se o canal receber relato clínico ou contestação de decisão do modelo, porque o canal do C1 poderia passar por ele [hipótese]. A linha também precisa terminar em cargo |

**Decisão futura já pedida.** O "Agente conversacional de triagem", pedido pelo Comercial [fonte: Cap. 2, Quadro 16], seria uma decisão nova sobre pacientes. Classificação antecipada: alto [proposta]. Ele só entra depois de passar pelo portão do §8 e ter dono na matriz do §5.3.

### 4.3 Decisões sobre o sistema, fora do Q12 [proposta: tratar no item 2]

Estas decisões ajudam a explicar três dos quatro incidentes [hipótese de leitura] e cumprem a promessa da E1.

| Decisão sobre o sistema | Dono hoje | Evidência |
|---|---|---|
| Liberar versão para produção | Paulo Adjaí (CTO), sozinho | Nota do Q12; Q13 |
| Aceitar atualização do fornecedor de modelo | [não consta] | Q14, 09/2025. O Q5 prevê "termos revisáveis a qualquer tempo com aviso de 30 dias". O aviso vale para os termos, e não consta que valha para a troca de versão |
| Incluir dados no treino | Yuri Nakamura (conjuntos de treinamento); nenhum parecer jurídico | Q7 (nenhum dos seis instrumentos revisado); Q13 |
| Escolher variáveis do modelo | CTO e Yuri [Q13]; "era uma decisão de gestão" | Cap. 2, 2.2; Q8 |
| Afirmar números ao mercado | Camila Torres (material de divulgação) | Q11, Q13, Q14 (01/2026) |
| Autorizar o uso num cliente ou decisão nova | O cliente; não consta aprovação da Lumis | Q12 |
| Entrar em mercado ou setor novo | Os pedidos vêm do investidor (México), do sócio-fundador (veterinário) e do comercial (crédito) [fonte: Cap. 2, Quadro 16]; Marcos Villela prioriza o backlog [fonte: Cap. 2, Quadro 13]; go/no-go [não consta] | Q13; Q16; Cap. 2, 2.6 |

---

## 5. Item 2: linha de responsabilidade das decisões de alto impacto

### 5.1 Fragilidade atual

| Função | Hoje | Base |
|---|---|---|
| Autorizar o uso | Fica com o cliente, em órgãos coletivos, em 4 de 5 decisões. Na priorização foi uma diretoria **comercial**, sem aprovação interna formal. Nas demais, aprovação interna [não consta] | Q12 |
| Liberar versão | Exclusiva do CTO, sem comitê de ética ou de risco | Nota do Q12; Q13 |
| Mudança vinda do fornecedor | Se a atualização do fornecedor passa pela liberação [não consta]. Em 09/2025, uma atualização do fornecedor derrubou o desempenho | Q14 |
| Monitorar | Nenhum cargo tem o monitoramento por subgrupo como responsabilidade escrita. As reclamações "nunca" foram cruzadas com o desempenho. Quem detectou foram o cliente e áreas internas | Q14; nota do Q17 |
| Suspender | Nos quadros do Cap. 2, poder formal de um cargo [não consta]. A F1-E2 atribui a suspensão à liderança em conjunto (CEO, CTO e Head of AI Management), sem cargo único nem prazo, e dá à equipe técnica e de dados a capacidade técnica de suspender. O mecanismo técnico (desligar tudo, por cliente ou por subgrupo) [não consta]. O prazo [não consta]. Se há rollback [não consta] | Varredura dos Q12 a Q14, do Cap. 2 e da F1-E2 |
| Escalar | 29% do técnico, 21% do comercial e 24% dos demais sabem a quem escalar | Q15 |
| Validar antes da produção | "Tempo adequado de validação": 17% do técnico, 68% do comercial e 38% dos demais | Q15; tensão em Cap. 2, 2.5 |
| Pessoa-chave | Rotatividade de 27% no time de dados (19% no total). Um apurador único é um risco [hipótese] | Nota do Q15 |

**Leitura** [hipótese]: na prática, quem constrói também libera e decide se há problema. A base está no próprio capítulo: "Medida por quem? Quem produziu o número tem interesse no resultado dele?" [fonte: Cap. 2, 2.3]. No texto, o fato vai sem juízo: "a liberação é exclusiva do CTO, sem instância de revisão" [fonte: nota do Q12].

### 5.2 Papéis propostos e separação de funções [proposta]

| Função | Cargo + nome | Por quê | Limite |
|---|---|---|---|
| **Autorizar o uso** (por decisão e por cliente) | Renata Souza (CEO), com **parecer obrigatório** do Head of AI Management (risco) e de Ana Beatriz Rangel (DPO; direito de uso e contrato) | Q13: a CEO tem a "decisão final sobre produto, mercado". O parecer põe o risco na decisão sem passar o freio para quem tem meta comercial | A autorização do cliente continua necessária, mas não basta: são duas autorizações. A CEO só supera um parecer contrário por escrito e com motivo, e o caso vai à próxima reunião do conselho |
| **Definir limite e casos de revisão** | Head of AI Management | Q13: "governança, risco" | Mudança de limite só vale com parecer do auditor externo e informe ao conselho, para que o Head não defina e aplique a mesma régua sozinho. Se a Q-5 criar o comitê, ele dá parecer, e a decisão continua com o Head |
| **Liberar versão**, incluindo a atualização do fornecedor | Paulo Adjaí (CTO) | Q13 | Dentro da regra "Versão que piora algum grupo não vai para produção" [fonte: F2-E2 v2, Tabela 4]. O Head of AI confere a regra e pode vetar a liberação (duas chaves) |
| **Apurar** os indicadores | Yuri Nakamura, responsável por Dados | Q13; a F2-E2 e a F2-E5 já usam assim | Ele também monta o treino. Por isso há conferência de fora: "O cliente e um auditor refazem a conta" [fonte: F2-E2 v2, Tabela 4] |
| **Monitorar** (ler, cruzar, confirmar o gatilho) | Head of AI Management. Leitora suplente: Ana Beatriz Rangel (DPO) | Não tem meta comercial e não libera | Confirma o gatilho, mas não libera versão |
| **Suspender ou restringir** | Head of AI Management. Também podem suspender sozinhos: Paulo Adjaí (CTO) e Ana Beatriz Rangel (DPO, quando a causa é dado ou contrato) | Uma chave basta para frear. Três chaves separam funções e garantem que haja alguém disponível [hipótese] | Toda suspensão entra no registro no mesmo dia |
| **Executar a suspensão** | Paulo Adjaí (CTO). Executor suplente: Yuri Nakamura, responsável por Dados | Controla a produção. A F1-E2 dá à equipe técnica e de dados "capacidade técnica para… suspender" | Executa no prazo e não pode recusar. Se discordar, recorre depois de executar. O procedimento deve poder ser executado pelo suplente e é testado no teste de 30 dias (§5.5) |
| **Reativar** (critério de saída cumprido) | CTO **e** Head of AI Management, juntos, mais o cargo que suspendeu, se for outro (DPO) | Duas chaves para religar | Sem acordo, o sistema segue suspenso e o caso vai ao conselho. Registro no registro de incidentes e suspensões |
| **Reverter suspensão por motivo de negócio** | Renata Souza (CEO) | Q13: decisão final | Só vale para suspensão sem causa de dano a pessoas, por exemplo uma falha técnica de disponibilidade. Suspensão ligada a viés, erro recorrente ou revisão contestada (C2, C3) só termina pelo critério de saída, com duas chaves (D-005). Sempre por escrito, com motivo e informe ao conselho |
| **Coordenar a investigação de incidentes** | Head of AI Management | C4 | — |
| **Manter o registro de incidentes e suspensões** | Head of AI Management mantém; Ana Beatriz Rangel (DPO) confere. A DPO responde pelos incidentes de dados e pelas notificações legais | Indicador 4 da F2-E2 v2 ("Pelo Head of AI Management. A DPO confere"); Q13 ("resposta a incidentes"); C4; C5 | Resolve a N10: o Head coordena e registra, e a DPO confere e notifica. Quando a DPO suspende, o Head registra. Quando o Head suspende, a DPO confere |
| **Relação com o regulador** | Head of AI Management; a DPO nos temas de proteção de dados | Q13 | — |
| **Prestar contas ao conselho** | Renata Souza (CEO) apresenta. Head of AI Management relata **diretamente** as suspensões, os pareceres contrários superados e as mudanças de limite | Indicador 4 da F2-E2 | Incidente detectado pelo cliente ou aberto há mais de 30 dias vai à pauta. A composição do conselho [não consta] |
| **Contratar o auditor externo** | Renata Souza (CEO), por proposta do Head of AI Management | Independência em relação a quem apura | O relatório vai direto ao conselho. Periodicidade: Q-3 |

**Escolhas da consolidação (uma linha cada):**
- *Quem autoriza o uso:* a CEO, com parecer obrigatório do Head of AI e da DPO (Proposta B), e não o Head com coassinatura (Proposta A). Motivo: o Head já monitora e suspende, e aprovar também concentraria funções demais. A palavra é "parecer", porque a CEO pode superá-lo. Chamar isso de veto não seria preciso.
- *Quem suspende:* o Head of AI, com o CTO e a DPO como chaves adicionais (Proposta A). Motivo: o freio fica distribuído e o risco de pessoa-chave diminui.
- *Reativar e reverter:* reativar exige critério de saída e duas chaves. A CEO só reverte suspensão sem causa de dano a pessoas. Sem acordo para reativar, o sistema segue suspenso.
- *Registro de incidentes:* fica com o Head of AI, e a DPO confere, como já está na F2-E2 v2 (indicador 4). A consolidação anterior passava o registro para a DPO. Isso inverteria a F2-E2 e exigiria nova entrada em DECISOES. A separação vem da conferência cruzada.

**Por que o Head of AI, e não a CEO, decide suspender.** A versão anterior da F2-E2 dizia "a CEO decide" (hoje em `_Historico`). A vigente deixou a questão para a E3 [fonte: DECISOES, D-031], e a F2-E5 propõe o Head of AI.
- A CEO responde pelo resultado comercial e pela "decisão final". Dar a ela o gatilho operacional mistura a decisão de risco com o interesse no resultado [hipótese; por analogia com Goodhart e "Medida por quem?", Cap. 2, 2.3].
- O prazo também ficaria inexequível, porque a CEO não lê o indicador quinzenal [hipótese].
- A CEO fica com a autorização do uso e com a reversão restrita. Isso confirma o provisório da F2-E5 e exige nova entrada em DECISOES (Q-2).

**Concentração no Head of AI.** O Head define o limite, monitora, suspende, mantém o registro, publica a métrica (D-024) e talvez presida o comitê. A concentração se defende porque ele não constrói nem libera. Ainda assim, ela pede quatro contrapesos [proposta]:
1. auditor externo, com relatório direto ao conselho;
2. CTO e DPO também com chave de freio, e a DPO conferindo o registro;
3. mudança de limite só com parecer do auditor e informe ao conselho;
4. relato direto do Head ao conselho sobre suspensões e pareceres superados. A quem o Head se reporta [não consta]. Se ele responder à CEO, sem esse canal direto o freio fica subordinado a quem autoriza o uso.

### 5.3 Matriz por decisão de alto impacto

Prazo atual: [não consta] em todas as linhas. Prazos propostos: [proposta], justificados no §5.6. "Hoje" vem dos quadros, e "Proposto" é desenho da equipe. Em todas as linhas, a contraparte do cliente é um cargo [não consta], que o contrato passa a exigir. A cláusula fica com Ana Beatriz Rangel (DPO).

O prazo é contado de ponta a ponta: **latência de detecção** (periodicidade da leitura ou evento) + **confirmação do gatilho pelo Head of AI** + **decisão em até 24 h** + **execução em até 24 h**. O teto de 48 h vale só a partir da confirmação. Gatilhos por evento (notificação de cliente, contestação, incidente) não esperam a leitura periódica.

| Decisão | Autoriza o uso | Monitora (gatilho / apura / lê) | Pode suspender | Executa | Prazo hoje | Prazo proposto | Reativa |
|---|---|---|---|---|---|---|---|
| **Priorização da fila** | Hoje: diretoria comercial do cliente, sem aprovação interna [Q12]. Proposto: CEO, com parecer do Head of AI e da DPO. Do cliente: o cargo clínico responsável pela triagem, exigido em contrato [cargo não consta] | Gatilho: razão ≥ 2,0 (R1) ou evento. Yuri Nakamura apura o indicador 1 a cada quinzena; Head of AI lê e confirma. Indicador 3 (reclamações) cruzado por Yuri | Head of AI (tudo, por cliente ou por subgrupo); CTO; DPO. O hospital pode suspender localmente [fonte: F1-E2] | Paulo Adjaí (CTO); suplente Yuri Nakamura | [não consta] | Detecção: até 15 dias pela leitura ou imediata por evento. Depois da confirmação: decisão em até 24 h e execução em até 24 h. Com dano clínico em curso, decisão imediata | CTO + Head of AI depois de 2 leituras quinzenais seguidas abaixo do limite |
| **Sugestão de protocolo** | Hoje: comitê clínico do hospital [Q12]. Proposto: igual à priorização. Do cliente: quem preside o comitê clínico [cargo não consta] | Gatilho [proposta]: diferença de reversão humana entre subgrupos acima de 2 vezes (indicador E3 da F2-E5, mensal). Yuri apura a taxa de aceitação sem alteração e o erro por subgrupo (hoje [não consta]); Head of AI lê | Igual | Paulo Adjaí (CTO); suplente Yuri Nakamura | [não consta] | Detecção: até 1 mês pela leitura ou imediata por evento; depois, 24 h + 24 h | Igual |
| **Risco de crédito** | Hoje: comitê de crédito do banco. Proposto: CEO, com parecer da DPO (dado de saúde fora do modelo de crédito [proposta da F2-E5]) e do Head of AI | Gatilho [proposta]: razão de aprovação por faixa de CEP abaixo de 0,8 (indicador E5 da F2-E5, mensal, desenhado para o novo módulo; aplicar ao crédito de hoje é extensão nossa). Yuri apura; Head of AI lê | Head of AI; DPO; CTO | Paulo Adjaí (CTO); suplente Yuri Nakamura | [não consta] | Detecção: até 1 mês; depois, 24 h + 24 h | Igual |
| **Risco de sinistro** | Hoje: diretoria da seguradora. Proposto: CEO, com parecer da DPO e do Head of AI. A DPO avalia o contrato Prisma, que é silente [Q7], e a LGPD (Lei nº 13.709/2018), art. 11, § 5º, se a seguradora for operadora de saúde [hipótese de aplicação; texto conforme F2-E5_Privacidade_v1.md, l. 36, conferido no Planalto em 07/10/2026] | Hoje não há indicador nem gatilho. Gatilho [proposta]: razão de negativa por grupo, com limite de 0,8 por analogia ao E5. Yuri passa a apurar erro e negativa por grupo (hoje [não consta]); Head of AI lê | Head of AI; DPO; CTO | Paulo Adjaí (CTO); suplente Yuri Nakamura | [não consta] | Até existir o indicador, só vale o gatilho por evento (24 h + 24 h). Depois, igual ao crédito | Igual |
| **Versão nova ou atualização do fornecedor** (afeta todas) | Hoje: só o CTO para versões; atualização do fornecedor [não consta]. Proposto: CTO libera e Head of AI confere a regra | Yuri testa por subgrupo antes; Head of AI confere. O CTO acompanha os avisos do fornecedor e a DPO acompanha os termos. Se as atualizações do modelo têm aviso prévio [não consta]; o Q5 prevê 30 dias de aviso só para revisão de termos [hipótese sobre o alcance] | Head of AI veta a liberação; qualquer chave manda voltar à versão anterior | Paulo Adjaí (CTO) | [não consta]; em 09/2025 a correção levou 6 dias | Nenhuma atualização entra sem teste por subgrupo. Sem travamento de versão [não consta], volta à versão anterior em até 24 h depois de detectada. Isso supõe rollback e travamento de versão (recomendação da E1), ambos [não consta] | Duas chaves |

**Linhas de apoio que também precisam de cargo:**

| Decisão | Proposta |
|---|---|
| Afirmações públicas | Camila Torres propõe e executa a retirada; Head of AI Management aprova [proposta; constava da versão anterior da F2-E2, hoje em `_Historico`]. A vigente diz "Por quem não vende. Cliente ou auditor refaz" e "sai antes da próxima apresentação" [fonte: F2-E2 v2, Tabela 4, indicador 5] |
| Inclusão de dados no treino | Ana Beatriz Rangel (DPO) dá o parecer e pode barrar (indicador 2 da F2-E2; P1 da F2-E5); Yuri Nakamura executa a retirada. Regra: "Dado sem autorização e parecer fica fora do próximo treino" [fonte: F2-E2 v2, Tabela 4] |
| Roteamento de suporte (baixo) | Camila Torres responde [hipótese de vínculo: o Q3 agrupa "comercial e CS"; o Q13 dá a ela "contas"]; Paulo Adjaí (CTO) executa a parte técnica |
| Registro de reclamações | Camila Torres responde pelo registro [hipótese]; Yuri Nakamura cruza com o desempenho; Head of AI Management decide a investigação. Preenche a lacuna da F2-E2, que diz "Pelo time de sucesso do cliente, cargo [não consta]" [fonte: F2-E2 v2, Tabela 4, indicador 3] |
| Contraparte no cliente | O cargo é [não consta] em todos os casos. Perante o cliente, responde o Head of AI Management, e o contrato passa a exigir a indicação de um cargo signatário do lado do cliente. A cláusula fica com a DPO, responsável por contratos [fonte: Q13] |

### 5.4 Decisões sobre fornecedores (promessa da E1) [proposta]

| Decisão | Responsável |
|---|---|
| Segundo fornecedor e travamento de versão | Paulo Adjaí (CTO) propõe; Renata Souza (CEO) aprova. Se a Q-5 criar o comitê, ele dá parecer antes |
| Preço e termos | Ana Beatriz Rangel (DPO) negocia o contrato; Renata Souza (CEO) aprova o impacto no capital |
| Portabilidade da nuvem (renova em 04/2027; migração de 7 meses [fonte: Q5]) | Paulo Adjaí (CTO) |
| Teto das bases clínicas | Ana Beatriz Rangel (DPO) |
| Hedge cambial | Renata Souza (CEO). Se existe hoje [não consta] |

### 5.5 O que se faz já (gatilhos já atingidos)

O conselho desconfia de regra que não diz o que se faz hoje [fonte: F2-E2 Levantamento, 1.4].

| Gatilho | Situação | Decide / executa | Prazo [proposta] |
|---|---|---|---|
| Restrição em 60+ CEP C e 60+ CEP D/E, com o modelo em paralelo [fonte: D-026] | Decidida pela equipe (D-026) e recomendada na F2-E2 v2, seção 5 ("restringir já"). Execução [não consta]. O incidente de 07/2026 segue "em tratamento" [Q14] | Head of AI ordena, com base na D-026 e no compromisso de Não Amplificação de Danos; Paulo Adjaí (CTO) executa; Head of AI comunica, com Camila Torres para as contas. O hospital assume a triagem de cerca de 154 mil decisões por mês [fonte: D-026, conta com hipótese] | Ordem imediata; execução em até 48 h, sem esperar o conselho. O conselho recebe o informe na reunião seguinte e ratifica depois, sem autorizar antes. Sem mecanismo por subgrupo [não consta], revisão humana em 100% desses recortes até a execução (custo [não consta]) |
| Teste de suspensão | Nunca feito [não consta] | Paulo Adjaí (CTO) executa uma suspensão simulada por subgrupo e por cliente, e Yuri Nakamura repete como suplente; Head of AI confere e registra; DPO confere o registro | Em até 30 dias; depois, a cada trimestre por decisão de alto impacto. O tempo medido substitui a meta |
| Retirar "5 milhões de vidas" | Aberto no material comercial [Q14] | Camila Torres retira; Head of AI aprova | Antes da próxima apresentação [fonte: F2-E2 v2, Tabela 4] |
| Dados sem autorização e parecer | Nenhum dos seis instrumentos revisado [Q7]; Prisma e Vila Ipê vencem em 12/2026 e 03/2027 [Q7] | DPO dá o parecer e barra; Yuri retira | Parecer da DPO sobre os seis contratos antes do próximo treino; dado sem autorização e parecer fica fora do próximo treino; renegociar Prisma e Vila Ipê antes do vencimento [fonte: F2-E2 v2; Cap. 2, Quadro 7] |
| Incidentes de 07/2026 e 01/2026 ao conselho | Acionam o indicador 4 e estão abertos [conta da equipe sobre o Quadro 14] | CEO apresenta; Head of AI relata | Próxima reunião do conselho |

### 5.6 Justificativa dos prazos propostos

1. **Âncora interna, por analogia** [proposta]. O C3 promete revisão imediata em urgência e em até 48 h nos casos contestados [fonte: F1-E3]. O C3 trata da revisão de um caso contestado, em saúde, feita pela instituição de saúde, e não da suspensão do sistema. Usamos as 48 h como teto por analogia: suspender o sistema não deveria levar mais tempo do que revisar um caso. Para crédito e sinistro, não há compromisso de prazo vigente [não consta].
2. **Evidência do Q14.** A correção levou de 6 a 22 dias, e há casos em aberto. Correção e contenção são coisas diferentes. O prazo proposto é de **contenção**: suspender ou restringir, com retorno à triagem do hospital. A correção pode levar mais tempo, desde que o sistema não decida enquanto isso.
3. **Latência de detecção.** As 48 h correm a partir da confirmação do gatilho. Antes disso, a leitura leva até 15 dias na priorização e até 1 mês no protocolo, no crédito e no sinistro. Por isso todo gatilho por evento (notificação de cliente, contestação, incidente) dispara a confirmação sem esperar a leitura. O Q14 mostra que hoje o cliente detecta antes.
4. **Exequibilidade.** O mecanismo técnico [não consta]. Os prazos são **metas** até haver um teste registrado. Se a meta falhar, o prazo declarado ao cliente e ao regulador passa a ser o tempo testado.
5. **Referência externa.** NIST AI RMF 1.0 (NIST AI 100-1, 2023) [fonte: F2-E2 v2, ref. 4]. Na F2-E2, ela sustenta a frase "O NIST pede que todo sistema de IA tenha responsável e meio definidos para ser desligado". O ESTADO.md registra que as quatro referências da F2-E2 ainda não foram conferidas no original. Subcategoria específica: só depois que alguém da equipe abrir o documento e registrar o item e a data da consulta. Nenhuma referência do repositório fixa prazo em horas. As 48 h são nossas.

---

## 6. Leitura do Quadro 14: que linha falhou

A coluna "linha que falhou" é [hipótese de leitura sobre o Q14]. A causa técnica de cada incidente [não consta].

| Incidente | Quem detectou / tempo | Linha que falhou | O que a proposta muda |
|---|---|---|---|
| 03/2025, exames de laboratório recém-credenciado descartados | Cliente; 22 dias | **Entrada de dados.** Mudou a fonte do cliente e não havia gatilho nem dono. Yuri tem "qualidade de dados" [Q13], mas não há alerta. Hoje, 22 dias até a correção seriam incompatíveis com o C3, que exige revisão em até 48 h nos casos contestados [hipótese de leitura; o C3 é posterior ao incidente] | Fonte nova entra em revisão obrigatória (R3). Yuri apura alertas de entrada, o Head of AI decide a contenção e o contrato prevê aviso de mudança do cliente (DPO) |
| 09/2025, queda após atualização do fornecedor | Equipe interna (cargo [não consta]); 6 dias | **Porta sem controle** [hipótese]. A versão mudou por atualização do terceiro [Q14]. Se a atualização passou pela "liberação exclusiva do CTO" [não consta] | A atualização do fornecedor passa a ser tratada como liberação de versão, com duas chaves, teste por subgrupo e volta à versão anterior. Travar a versão em contrato [fonte: F2-E1] |
| 01/2026, duplicidade nas "vidas analisadas" | Auditoria interna (cargo [não consta]); sistema corrigido, material não | **Encerramento sem dono entre áreas.** O técnico corrigiu, e não consta que o dono do material (Camila Torres [Q13]) tenha sido acionado. Contradiz o compromisso de Transparência [fonte: F2-E2 v2, seção 4] | O incidente só fecha com todos os canais encerrados (sistema, cliente, material, regulador). O Head of AI aprova afirmações públicas. A auditoria interna existe e é um monitor independente, mas o cargo dela [não consta] |
| 07/2026, viés etário e regional | Cliente (Vila Ipê), que mediu o 31,8% "por conta própria" [box p. 25]; em tratamento | **Autorização sem a Lumis** [Q12]; **monitoramento por subgrupo sem dono**; reclamações nunca cruzadas [nota do Q17]; revisão de 2% sem foco no risco; **poder de suspender só coletivo** [F1-E2]. O C2 prevê suspensão "quando necessário", e não consta que tenha havido suspensão | Matriz do §5.3; indicador 1 quinzenal; restrição da D-026 executada (§5.5); revisão por amostra no nível de alerta (R2); incidente acima de 30 dias vai ao conselho |

**Padrão** [hipótese]: os quatro incidentes entraram por portas sem dono descrito nos quadros: fonte de dados, fornecedor, material comercial e autorização do cliente. Nenhum entrou pela única porta com dono descrito, a liberação do CTO. Em nenhum consta um cargo que tenha decidido conter.

**Registro de incidentes proposto** (atende ao C4) [proposta]: acrescentar as colunas severidade, tempo até a contenção, se houve suspensão (sim/não e quem decidiu), cargo que coordenou, cargo que comunicou e data de encerramento em cada canal. O Head of AI mantém o registro e a DPO confere, como no indicador 4 da F2-E2.

---

## 7. Item 3: casos de revisão humana obrigatória

**Princípio** [proposta]: cada caso tem gatilho observável, cobertura (100% ou amostra), prazo, quem revisa, que cargo da Lumis garante e quem registra. Revisão sem registro não é auditável e não conta. Pelo C3, a revisão clínica é da instituição de saúde, e a Lumis garante o registro e o rastreio [fonte: F1-E3]. Na Lumis, Paulo Adjaí (CTO) garante a função de registro e rastreio no sistema, e o Head of AI Management guarda e lê os registros. Do lado do cliente, o cargo de quem revisa é [não consta] em todos os casos, e o contrato passa a exigir um cargo signatário (cláusula com Ana Beatriz Rangel, DPO). O piso vem dos compromissos já assumidos: C3 (imediato / 48 h) e C2 (leitura quinzenal). A amostra de 10% da D-027 é redistribuída em R1 e R2 (ver §9).

| # | Caso | Gatilho testável | Cobertura e prazo | Quem revisa (cliente) / cargo da Lumis que garante | Critério que sustenta | Status |
|---|---|---|---|---|---|---|
| R1 | Priorização em recorte crítico | FN do recorte ≥ 2,0 vezes o do melhor subgrupo | Sai da recomendação automática: 100% vai à triagem do hospital, com o modelo em paralelo. Ação imediata | Profissional do hospital (cargo [não consta]; cargo signatário exigido em contrato) / Head of AI decide e registra (DPO confere), CTO executa, Yuri mede | K3 + K4; C2 ("padrão de viés"), na leitura da D-026 | [fonte: D-026; F2-E2 v2]. Hoje: 60+ C (2,2) e 60+ D/E (3,0) [Q10] |
| R2 | Priorização em recorte de alerta | Razão acima de 1,5 e abaixo de 2,0 vezes | Amostra de 10% e leitura quinzenal. Se persistir por 2 ciclos, passa a R1 | Profissional do hospital (cargo [não consta]) / Head of AI | Concilia o 1,5 da F2-E5 com o 2 da F2-E2. O alerta começa acima da meta de "até 1,5 vez" da D-024 | [proposta; Q-3]. Entraria hoje 18-59 D/E (1,9). O 60+ A/B (1,50) fica no limite, sem folga [fonte: conta da equipe sobre o Quadro 10] |
| R3 | Fonte de dados, cliente, região ou base nova | Entrada da fonte | 100% até 1 ciclo de validação sem regressão | Profissional do hospital (cargo [não consta]) / Yuri apura, Head of AI libera a saída | Incidente de 03/2025 [Q14]; K8 | [proposta] |
| R4 | Qualquer contestação | Pedido de paciente, profissional ou cliente | Urgente: imediato. Demais: até 48 h | Profissional da instituição de saúde (cargo [não consta]) / Head of AI garante o canal e guarda o registro; CTO garante a função de registro; Yuri cuida da base | C3 e C1 (canal de esclarecimento) | [fonte: F1-E3] |
| R5 | Sugestão de protocolo | Sempre (já é assim) | 100%, com registro de aceita, altera ou rejeita | Médico responsável [Q12] / CTO garante a função de registro, Yuri mede a taxa, Head of AI lê | K1; com o registro, a revisão pode ser verificada | Revisão [fonte: Q12]; medição [proposta]; taxa hoje [não consta] |
| R6 | Sinistro | Classificação que leve a negativa ou atraso, **no lugar** do corte de R$ 50 mil | 100% nesses casos | Analista da seguradora (cargo [não consta]) / Head of AI | K1 e K2; o corte financeiro protege a seguradora, e não a pessoa [hipótese] | [proposta]; efeito da classificação [não consta] |
| R7 | Crédito | Sempre (já é assim), mais auditoria do recorte com razão de aprovação por CEP abaixo de 0,8 | 100% e leitura mensal do indicador | Analista do banco (cargo [não consta]) / Head of AI | K1; regra dos quatro quintos por analogia [fonte: F2-E5, indicador E5] | Revisão obrigatória [fonte: Q12]; limite 0,8 e auditoria [proposta; base F2-E5, indicador E5, desenhado para o novo módulo] |
| R8 | Versão nova ou atualização do fornecedor | Qualquer mudança em produção | Validação por subgrupo antes de entrar e amostra reforçada nas primeiras semanas (duração a definir) | CTO valida; Yuri mede; Head of AI confere | Q14, 09/2025; nota do Q12 | [proposta] |
| R9 | Mercado ou setor novo | Entrada | 100% em modo sombra até haver amostra local por subgrupo (indicador E4 da F2-E5) | Responsável técnico do domínio (cargo [não consta]) / Head of AI | Cap. 2, 2.6; §8 | [proposta]; coerente com a condição 2 da E5 |
| R10 | Roteamento | Mensagem com relato clínico ou contestação de decisão do modelo | Encaminhar a humano no mesmo dia útil | Pessoa do atendimento (cargo [não consta]) / Camila Torres responde [hipótese] | Evita que o canal do C1 passe por robô | [proposta]; se isso ocorre hoje [não consta] |

A explicabilidade das decisões do modelo, pedida por "Regulador e clientes" e ainda no backlog [fonte: Cap. 2, Quadro 16], é o que dá conteúdo à revisão em R1, R4 e R5. Sem ela, quem revisa vê só a classificação [hipótese].

---

## 8. Item 4: o que muda num novo setor

**Recorte.** O enunciado fala em "novo setor… não domina os dados nem os erros típicos". A D-023 define o recorte só da F2-E5 e não obriga a E3. Os candidatos do capítulo:
- **Veterinário.** É o único setor de fato novo no capítulo: pedido pelo "Sócio-fundador", 16 meses-pessoa e R$ 2,1 milhões de receita potencial em 12 meses [fonte: Cap. 2, Quadro 16]. A E5 não o analisa.
- **Plataforma multissetor.** É a proposta do Vetor [fonte: Cap. 2, 1.1]. O próprio cliente configura usos em domínios que a Lumis não conhece [hipótese].
- **México.** É o mesmo setor em outro país, pedido pelo "Investidor" [Q16], sem dado local de desfecho [não consta]. Atende ao "não domina os dados", mas não ao "novo setor".
- **Crédito.** Já existe: 5 bancos e 31 mil decisões por mês [Q3; Q12]. O backlog pede um *módulo* [Q16], o que é aprofundamento e não setor novo.
- A E1 não escolhe setor.
- **Proposta:** veterinário e plataforma como caso principal, por serem setores de fato novos, e México como variação (mesmo setor, dados que a Lumis não domina). A equipe confirma (Q-4). Há um ponto para a E4: o veterinário foi pedido pelo sócio-fundador, então o portão precisa conseguir recusar até um pedido do fundador.

**O que muda na estrutura** [proposta, com base no Cap. 2, 2.4 e 2.6]:
1. **Portão de entrada com dono.**
   - Quem pede varia [Q16]. Marcos Villela prioriza o backlog [Q13] e leva o pedido ao portão.
   - Renata Souza (CEO) decide.
   - Head of AI Management (risco e revisão) e Ana Beatriz Rangel (DPO: base legal local e transferência internacional; lei mexicana [não consta]) dão parecer obrigatório. A CEO só supera um parecer contrário por escrito, e o caso vai ao conselho, a mesma regra do §5.2.
   - A E3 só define o dono do portão. Os "critérios explícitos de entrada e de morte de projeto" [fonte: Cap. 2, 2.6] ficam para o funil da E4, sem fixá-los aqui. O portão também dá dono ao indicador E4 da E5.
   - Isso responde à segunda metade do item 4 do memorando.
2. **Classificação antes do uso.** O novo uso passa pelo §4.1. Sem dado de erro, K4 e K8 são "desconhecidos" e contam como alto, porque K1 é saúde ou serviço essencial.
3. **Modo sombra obrigatório (R9).** O modelo roda em paralelo, sem decidir, até haver medida do erro por subgrupo local. É o mesmo mecanismo da D-026.
4. **Responsável de domínio com cargo e nome.** A Lumis não sabe avaliar os erros típicos [fonte: Cap. 2, 2.6]. É preciso exigir um responsável técnico do domínio, do cliente ou contratado, que assine a definição de "erro grave". Exemplos: médico-veterinário no veterinário; responsável clínico local no México; analista de crédito no banco. Os cargos [não consta].
5. **Suspensão por país ou cliente.** O Head of AI pode suspender por mercado, e o CTO executa no prazo da matriz. O teste de suspensão acontece **antes** do go-live, além do trimestral.
6. **Plataforma.** Se o cliente configura os próprios usos, o padrão do Q12 (uso autorizado por uma diretoria do cliente, sem a Lumis) se multiplica [hipótese]. Por isso a plataforma só libera decisão de alto impacto com a dupla autorização do §5.2.
7. **Dados.**
   - Dado de saúde fora de modelo de crédito [proposta da F2-E5].
   - Cada base nova tem parecer próprio da DPO (indicador 2 da F2-E2).
   - As variáveis de acesso (custo, atendimentos, CEP, plano) só entram depois de teste [fonte: F2-E2 v2; Q8].
8. **Capacidade.**
   - Há 30 meses-pessoa disponíveis para novas iniciativas nos próximos seis meses, contra 97 de backlog [fonte: Cap. 2, Quadro 16], e a rotatividade em Dados é de 27% [nota do Q15].
   - Multiplicar decisões sem multiplicar quem apura repete o incidente de 07/2026 [hipótese]. A condição é ter um apurador nomeado por mercado.
   - Governança consome capacidade, e o memorando precisa dizer isso. A explicabilidade (9 meses-pessoa) e a ISO/IEC 42001 (7 meses-pessoa, pedida pelo Jurídico) já estão no backlog [Q16] e servem de alavanca de priorização para a E4.
9. **Afetados.** A F1-E2 cobre só a saúde. Mapear os afetados do novo domínio é condição de entrada.

**Síntese:** o capítulo diz que "sem uma linha de responsabilidade explícita, a expansão para novos setores multiplica exposição sem multiplicar controle" [fonte: Cap. 2, 2.4]. Por isso a linha de responsabilidade vem antes da expansão. Sobre a base de dados, o capítulo é mais duro: expandir "antes de resolver a questão da base de dados não é crescimento — é replicação de um problema em escala maior" [fonte: Cap. 2, 2.6].

---

## 9. Checagem contra C1–C5 e coerência

No .docx, compromissos e decisões aparecem pelo nome (ex.: "compromisso de Não Amplificação de Danos", "a restrição já recomendada na Entrega 2"). Os códigos ficam só neste material de apoio (D-031).

| Compromisso / decisão | O que a E3 faz | Contradiz? | Posição |
|---|---|---|---|
| **C1** Transparência | Afirmações públicas: Camila propõe e retira, o Head of AI aprova. Canal de esclarecimento: Head of AI (R4). Métrica pública: Head of AI publica (D-024) | Não | **Manter.** Troca "a Lumis" por cargos |
| **C2** Não amplificação | Leitura quinzenal: Yuri apura e o Head lê. Investigação: o Head coordena. Suspensão: o Head decide e o CTO executa. Executa a D-026 | A letra do C2 diz "quando necessário" [fonte: F1-E3]. Pela leitura da equipe registrada na D-026, o recorte ≥ 2 vezes já é padrão de viés e a suspensão é necessária. Esperar 2 ciclos nesse recorte, como faz a F2-E5, enfraquece a aplicação do C2 [hipótese apoiada na D-026] | **Manter.** Os 2 ciclos valem só para o nível de alerta (R2). Com padrão confirmado (≥ 2,0 vezes), a ação é imediata (R1) |
| **C3** Reversibilidade | Paulo Adjaí (CTO) garante a função de registro e rastreio no sistema; o Head of AI guarda e lê. As 48 h viram teto de contenção por analogia [proposta] | Não | **Manter** |
| **C4** Responsabilidade | O Head coordena. As "áreas técnica, jurídica e de negócio" viram CTO, Yuri, DPO, Camila e Marcos. O Head mantém o registro e a DPO confere | **Amplia:** o Head ganha poder individual de suspender, que o C4 não dá | **Manter o texto e registrar a ampliação em DECISOES** |
| **C5** Segurança e privacidade | DPO dona da revisão de acessos a cada 90 dias e do registro de incidente de segurança "assim que identificado" [fonte: F1-E3]; meta de registro no dia em que é identificado [proposta; F2-E5, P3]; Yuri executa (P2 e P3 da E5) | Não | **Manter** |
| F1-E2 (suspensão pela "Liderança da Lumis (CEO, CTO e Head of AI Management)", em conjunto) | Individualiza: o Head decide, o CTO e a DPO também podem frear, o CTO executa. A CEO sai das chaves de freio e fica com a autorização do uso e uma reversão restrita | Detalha e muda a atribuição coletiva | **Registrar na nova D** |
| D-005 (priorizar a segurança dos afetados) / D-006 | A CEO não reverte suspensão ligada a dano a pessoas; o freio é fácil e o religamento difícil; a IA segue como apoio | — | Coerente |
| D-026 (restrição) | Define executor, poder e prazo (§5.5), sem depender de aprovação prévia do conselho | Não | Coerente; não reabrir |
| D-027 (revisão humana de 10% nos subgrupos críticos) | Com a restrição da D-026, os críticos saem da recomendação automática (R1, 100% à triagem do hospital), e os 10% perdem objeto ali e passam ao nível de alerta (R2). Limite de 2 vezes: [fonte: D-026, marcado como hipótese; F2-E2 v2, Tabela 4] | **Sim, altera a aplicação** | **Revisar com nova D** |
| D-024 (meta de até 1,5 vez) | R2 começa acima de 1,5, então quem cumpre a meta não entra em alerta | Não | Coerente |
| F2-E2 v2 vigente, indicador 1 | Deixou para a E3 quem decide (D-031). A versão anterior dizia "a CEO decide" (`_Historico`). A E3 define: Head of AI decide, CEO reverte só o que não envolve dano a pessoas | Não, em relação à vigente | Registrar |
| F2-E2 v2, Tabela 4: "Versão que piora algum grupo não vai para produção" | O CTO libera dentro da regra; o Head of AI confere e pode vetar | Não | Coerente |
| F2-E2 v2, indicador 3 ("time de sucesso do cliente, cargo [não consta]") | Camila registra [hipótese], Yuri cruza, Head decide a investigação | Preenche a lacuna | Registrar |
| F2-E2 v2, indicador 4 ("Pelo Head of AI Management. A DPO confere") | Mantido para o registro de incidentes e suspensões | Não | Coerente |
| F2-E2 v2, Tabela 5 "Pela área de Dados" (indicador descartado) | Termina em área | Menor | Trocar por "Yuri Nakamura, responsável por Dados" se a tabela for ao integrado |
| F2-E5, "Head of AI suspende" | Confirmado e formalizado, com contrapesos | Não | Coerente depois dos ajustes do §10 |
| F2-E1, decisões sobre fornecedores | §5.4 | Não | Cumpre a promessa |
| D-003 | Sinalizar as divergências Cap. 1 × Cap. 2: CTO, jurídico e volume (3 mi × 1,05 mi). A divergência entre "casos de maior impacto" e os 2% fica dentro do Cap. 2 e é sinalizada sem a D-003 | — | Coerente |

**Nova entrada em DECISOES** [proposta; texto-base]: "Linha de responsabilidade da F2-E3:
- O Head of AI Management decide suspender ou restringir. O CTO e a DPO também podem suspender. O CTO executa, e Yuri Nakamura é o executor suplente.
- A CEO autoriza o uso, com parecer obrigatório do Head e da DPO. Parecer contrário só é superado por escrito, com o caso levado ao conselho.
- A CEO reverte por motivo de negócio só suspensão sem causa de dano a pessoas. Suspensão ligada a C2 ou C3 termina pelo critério de saída, com duas chaves.
- Duas chaves na liberação e na reativação. Sem acordo para reativar, o sistema segue suspenso.
- O Head mantém o registro de incidentes e suspensões e a DPO confere (como no indicador 4 da F2-E2).
- O Head relata diretamente ao conselho as suspensões, os pareceres superados e as mudanças de limite.
- Os prazos são metas até o teste de suspensão e contam a partir da confirmação do gatilho.
- O C4 é ampliado para incluir o poder individual de suspender. A atribuição coletiva da F1-E2 passa a ser individual.
- Os 10% da D-027 passam do nível crítico ao nível de alerta.
- Confirma os cargos provisórios da F2-E5."

---

## 10. Avaliação da F2-E5 (Felipe Alef; D-023 a D-025)

### 10.1 Pontos fortes

- Cobre os 4 itens do enunciado.
- Os números conferidos batem com os Quadros 3, 7 a 12 e 14 a 17.
- Limites e metas estão marcados como proposta, e não há marca d'água.
- A métrica pública por subgrupo (D-024) é o mecanismo de prestação de contas de que o C4 precisa.
- "Dado de saúde fora do crédito" é uma regra clara.
- O E4 funciona como portão de mercado.
- As condições prévias podem ser aproveitadas no memorando.
- Usa "Yuri Nakamura, responsável por Dados", com fonte, na tabela da métrica.
- A LGPD foi conferida no Planalto em 07/10/2026, com URL (`F2-E5_Privacidade_v1.md`, l. 5).

### 10.2 Problemas (conferidos nos arquivos de `e5/`)

| # | Gravidade | Problema | Ajuste |
|---|---|---|---|
| P-1 | Alta | Limite de 1,5 vez, com revisão primeiro e "se persistir por dois ciclos quinzenais, o uso… é suspenso" (`F2-E5_Metrica_Publica_v1.md`, l. 33). Conflita com a D-026 e a F2-E2 (2 vezes, restrição imediata). A condição 1 ("ou com revisão humana obrigatória nos subgrupos acima dele", `F2-E5_v1.txt`, l. 152) é mais fraca que a D-026 | Adotar R1 e R2. Citar a restrição da D-026 nas condições |
| P-2 | Alta | "Nenhum ponto desta entrega contradiz os compromissos C1 a C5" (l. 158). Pela leitura da equipe registrada na D-026, a espera de 2 ciclos no recorte ≥ 2 vezes conflita com a D-026 e enfraquece a aplicação do C2. A letra do C2 diz "quando necessário" | Reescrever depois da E3, citando o conflito com a D-026 |
| P-3 | Média | Dá o poder de suspender ao Head como "coordenador previsto no compromisso C4" (l. 87). O C4 só dá coordenação, e o trecho não está marcado como proposta | A E3 formaliza e a E5 passa a citar a E3 |
| P-4 | Média | Linhas que terminam em área: "Pela área de Dados, com auditoria independente anual" (`Metrica_Publica`, l. 44). Sem cargo: quem contrata a auditoria, quem executa a revisão no subgrupo, o go/no-go do E4, os donos das 6 condições prévias e a apuração de reclamações | Trocar pelos cargos do §5.2 e do §5.3 |
| P-5 | Média | Numeração dos indicadores da F2-E2: "E1 e E2 retomam os indicadores 1 e 5" (l. 86) e o P1 "retoma o indicador 3" (`Privacidade`, l. 54). O certo é reclamações = 3 e direito de uso = 2. O limite de reclamações também diverge (2 vezes a média contra 1,5 vez o peso) | Corrigir e unificar |
| P-6 | Média | Auditoria independente anual (D-024) contra "um auditor confere os números a cada trimestre" (F2-E2 v2, conferido no .docx). Omite a subida de 2% para 10% | Q-3 |
| P-7 | Baixa-média | A meta "nenhum subgrupo acima de 7,4%" (l. 139) usa o FN da validação de 2023 [Q9], que a F2-E2 trata como não auditável | Rever a meta |
| P-8 | Baixa | Crédito tratado como expansão nova [Q3; Q12; Q16] | Chamar de "módulo" (§8) |
| P-9 | Baixa | "22,0 mi de registros de saúde e de sinistros" inclui financeiros e sintéticos [Q7]; 62% renovável sem [hipótese]; "[fonte: Cap. 2, seção 2]" cobre subseções diferentes; multa calculada com faturamento igual ao ARR | Trocar "seção 2" pela subseção certa em cada caso: 2.3 (Goodhart e as quatro perguntas), 2.4 (AI Act) e 2.7 (composição das equipes, Materialidade T6). Demais: ajustes de texto |

**O que alinhar com o colega:**
1. Quem suspende.
2. Limite único com dois níveis.
3. Periodicidade da auditoria.
4. Cargos em todas as linhas.
5. Citação da restrição da D-026.
6. Numeração dos indicadores.

### 10.3 Numeração das decisões e estado do repositório (conferido às 15:55 de 07/10/2026)

> **Resolvido em 07/10/2026 (D-033 a D-036):** as duplicadas viraram D-030 a D-032, as decisões da E3 estão na D-034 e na D-035, e a F2-E5 foi alinhada na D-036. O texto abaixo registra o estado antes da correção.

- O merge `8cd89ce` está **concluído**. A Proposta A, que falava em "merge em curso / UU", está desatualizada.
- E5: D-023 a D-025. E2: D-026 (C2 mantido), D-027 (diretrizes), D-028 (v2 enxuta) e D-029 (anexo).
- O .docx vigente da F2-E2 não usa códigos internos (C1 a C5, D-0XX). Eles foram retirados de propósito (D-031). A versão com códigos está em `_Historico/2026-10-07_F2-E2_Auditoria_do_Ativo_v2_com-codigos-internos.docx`. A decisão da restrição deve ser citada como D-026 a partir do DECISOES.md. O `F2-E2_v2.txt` do scratchpad é extração antiga e diz "D-023". Não usar.
- O .docx da F2-E2 foi salvo de novo às 15:53 e estava aberto no Word. A Tabela 4 passou a reunir indicadores e quatro perguntas, sem a coluna "Quem responde", e os descartados viraram a Tabela 5. Conferir de novo antes de citar.
- **Duplicidades na working tree (não commitadas)**, no fim do DECISOES.md:
  - l. 142: segunda **"D-027 · 07/10/2026 · F2-E2 v2 sem anexo: as quatro perguntas no corpo"**. Deveria ser **D-030**. O texto "Substitui a parte da D-026 que mantinha as três tabelas em anexo" deveria dizer **D-029**, um resto da numeração anterior.
  - l. 146: segunda **"D-028 · 07/10/2026 · uma tabela de indicadores e sem códigos internos"**. Deveria ser **D-031**.
  - A D-026 e a D-027 (06/10) aparecem depois da D-023 a D-025 (07/10), fora da ordem cronológica, por causa da renumeração no merge.
  - O ESTADO.md não commitado cita "D-023 a D-028" para a F2-E2. Depois da renumeração, o certo é D-026 a D-031.
  - Quem fez a edição corrige antes do commit, com autorização. Esta análise não alterou nada.
- Com essas correções, as decisões da E3 começam em **D-032**.

---

## 11. Lacunas, hipóteses, decisões da equipe e estrutura do .docx

### 11.1 [não consta] (vai no texto como resultado de análise)

- **Cargos internos:** os de Yuri Nakamura, Camila Torres e Marcos Villela; a quem o Head of AI se reporta; a composição do conselho.
- **Cargos e nomes do lado do cliente:** diretoria comercial, comitê clínico, diretoria da seguradora, comitê de crédito.
- **Cargo por trás de áreas citadas:** "Operação da Lumis", "auditoria interna", "equipe interna", "time de sucesso do cliente".
- **Suspensão:** poder individual de suspender nos quadros; mecanismo técnico e tempo atual para suspender; existência de rollback; se a Lumis consegue travar a versão do fornecedor; se as atualizações do modelo têm aviso prévio; se a atualização de 09/2025 passou pela liberação.
- **Revisão:** quem faz a revisão de 2% e com que critério; o critério da revisão "obrigatória" no protocolo e no crédito; a origem do corte de R$ 50 mil.
- **Erro e efeito:** erro por subgrupo no protocolo, no sinistro e no crédito; efeito da classificação de sinistro; se as seguradoras são operadoras de saúde; taxa de aceitação sem alteração no protocolo.
- **Pós-crise:** quais são os "casos de maior impacto" do Cap. 2, 1.1; data do Q12.
- **Incidentes:** quem decidiu as correções do Q14; se houve suspensão; data atual do caso e, por isso, há quanto tempo os incidentes estão abertos.
- **Restrição da D-026:** carga por hospital e receita afetada.
- **Novo mercado:** lei de dados do México; regulação veterinária.
- **Regulador:** o nome no Cap. 2. A ANS aparece só no Cap. 1.
- **Pessoas:** motivo da troca de CTO e jurídico entre os capítulos; perfil de quem usa o suporte.
- **Prazos:** compromisso de prazo para crédito e sinistro.

### 11.2 Hipóteses e propostas a marcar

- Escala K1 a K8 e regra de agregação.
- Sinistro como "alto provisório" e roteamento como "baixo condicionado".
- Aceitação automática no protocolo.
- Vínculo de Camila Torres com reclamações e suporte.
- Atualização do fornecedor fora da liberação.
- Leitura de cada incidente e o padrão "portas sem dono".
- 2% possivelmente anteriores à contenção pós-crise.
- Todo o desenho de papéis: autorização pela CEO com parecer obrigatório, três chaves de freio, duas chaves para religar, reversão restrita, registro com o Head e conferência da DPO, suplentes (DPO na leitura, Yuri na execução), relato direto ao conselho, comitê e responsável de domínio.
- Todos os prazos, a âncora no C3 por analogia e o teste de suspensão.
- Gatilhos do protocolo, do crédito atual e do sinistro.
- R2, R3, R6 e R8 a R10.
- Classificação antecipada do agente conversacional de triagem.

### 11.3 Decisões para a equipe

| # | Pergunta | Recomendação |
|---|---|---|
| **Q-1** | Cargos de Yuri, Camila e Marcos: (a) "Yuri Nakamura, responsável por Dados [fonte: Q13]" ou (b) propor títulos formais ao conselho, marcados como proposta? | (a) no corpo e (b) como recomendação no anexo |
| **Q-2** | Confirmam o Head of AI Management como quem suspende (com CTO e DPO como chaves adicionais e reversão restrita da CEO)? E a CEO como quem autoriza o uso, com parecer obrigatório do Head e da DPO? | Sim. Vira a D-032 |
| **Q-3** | Limite em dois níveis (acima de 1,5 e abaixo de 2,0 como alerta com 10%; ≥ 2,0 como restrição imediata) ou só o 2? O 60+ A/B (1,50) entra no alerta? Auditor trimestral nos indicadores (F2-E2) e anual no sistema (F2-E5)? | Dois níveis, com alerta acima de 1,5 (coerente com a meta da D-024); auditor trimestral nos indicadores e anual no sistema |
| **Q-4** | Novo setor: veterinário e plataforma como caso principal, com o México como variação? | Sim. A E5 mantém o próprio recorte (D-023) |
| **Q-5** | Comitê de Risco e Ética de IA: entra na E3 ou fica como semente para a E4 e a Fase 4? | Semente. Na E3, cada linha termina num cargo, e o comitê, se existir, só dá parecer |
| **Q-6** | Sinistro: alto provisório ou médio-alto? | Alto provisório |
| **Q-7** | Registro de incidentes: manter com o Head e a DPO conferindo (como na F2-E2) ou passar à DPO (exige revisar a F2-E2)? | Manter como na F2-E2 |

**Composição do comitê para a Q-5** [proposta]:
- Presidência: Head of AI Management.
- Membros: CEO, CTO, DPO, Yuri Nakamura e Marcos Villela.
- Camila Torres participa sem voto sobre liberação.
- Pauta quinzenal; a ata alimenta o registro do C4.
- O comitê dá parecer e não substitui as chaves individuais de freio nem a decisão da CEO no portão.

### 11.4 Estrutura proposta do .docx

Segue o formato da F2-E1 e da F2-E2: tese no início, tabelas curtas e só o que o enunciado pede (D-028, D-029 e as duplicadas que devem virar D-030 e D-031). Compromissos e decisões aparecem pelo nome, sem códigos internos.

0. **Conclusão e o que se faz já** (meia página).
   - A fragilidade e a linha proposta.
   - O que se faz já: executar a restrição recomendada na Entrega 2, fazer o teste de suspensão em 30 dias, retirar o "5 milhões".
   - Pedido: aprovar a matriz e as chaves.
1. **Hoje: quem responde por quê e o que os incidentes mostram.** Tabela 1 com o Q12 e o Q13 resumidos e a coluna "termina em área?". Tabela 2 com o Q14 e a coluna "porta sem dono". Sinalizar as divergências.
2. **Mapa por impacto (item 1).** Critério em quatro linhas e a Tabela 3 com as 5 decisões, o nível, o controle atual e o motivo.
3. **A linha de responsabilidade (item 2).** Tabela 4: decisão × (autoriza, monitora, suspende, executa, prazo hoje, prazo proposto, reativa). Princípios em quatro linhas. Decisões sobre o sistema e fornecedores em lista curta.
4. **Revisão humana obrigatória (item 3).** Tabela 5 com R1 a R10.
5. **Em novo setor ou mercado (item 4).** Lista curta. Declarar que o portão é dono do funil da E4, sem fixar os critérios que a E4 vai definir.
6. **Coerência.** Compromissos da Declaração de Intenção e entregas anteriores, pelo nome: o que se mantém e o que se revisa.

**Matrizes de apoio do documento integrado:** matriz completa do §5.3, critério K1 a K8, justificativa dos prazos e do teste de suspensão, decisões sobre fornecedores, suplentes e a lista do que não consta.

**Figura possível:** diagrama das "portas" do sistema: dados de entrada, fornecedor, liberação de versão, autorização do cliente, material público e suspensão. Cada porta mostra o dono hoje (quase todas vazias) e o proposto. Alternativa: fluxo "detecção → confirmação pelo Head of AI → decisão em 24 h → execução em 24 h → religar com duas chaves", com os cargos nos nós. Cores Profundo `#0F2D3A` e Vital `#3DBE93`, conforme `00_Lumis/Design_System/`.

---

**Arquivos conferidos nesta consolidação:**
- DECISOES.md (D-003 a D-006, D-023 a D-029 e as duplicadas D-027 e D-028 nas l. 142 e 146, não commitadas)
- ESTADO.md (não commitado)
- 02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/F2-E2_Auditoria_do_Ativo_v2.docx (salvo às 15:53; Tabelas 4 e 5, seção 5, ref. 4; sem códigos D-0XX), extraído em (texto extraído) e2_1553.txt
- 02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/F2-E2_Levantamento_v1.md (l. 437: MANAGE 2.4 como "[não verificado; anexo]")
- (texto extraído) cap02_raw.txt (Q5, Q12 a Q17, 1.1, 2.3, 2.4, 2.6, 5.1, box da E3)
- (texto extraído) F1-E2_Mapa_de_Stakeholders_revisada.txt e F1-E3_Declaracao_de_Intencao_revisada.txt
- (texto extraído) e5/F2-E5_v1.txt, F2-E5_Equidade_v1.md, F2-E5_Materialidade_v1.md, F2-E5_Metrica_Publica_v1.md, F2-E5_Privacidade_v1.md


---

**Notas de verificação**
- Aplicadas, depois de conferidas: retirada do "MANAGE 2.4" e do "conferida"; tese sem afirmar inexistência e com a F1-E2; fornecedor em 09/2025 como hipótese; "Ninguém" trocado por [não consta]; aviso de 30 dias restrito aos termos; pedidos de mercado pelo Q16; §10.3 sem D-026 no .docx; D-027 redistribuída e limite de 2 vezes atribuído à D-026 e à F2-E2; F1-E2 na §5.1 e na §9; LGPD art. 11, § 5º, com data de consulta; frase da 2.6 trocada pela da 2.4; C3 sem anacronismo; abertura com a ressalva dos 2%; "única alavanca formal descrita nos quadros"; contagem do indicador 4 (três de quatro); subseções do P-9; qualificadores do Q16; R7 e crédito como proposta da F2-E5; C5 "assim que identificado"; §5.5 sem depender do conselho; reversão pela CEO restrita; "Quem revisa" terminando em cargo; comitê só com parecer e suplentes nomeados; "veto" trocado por "parecer"; registro unificado; prazo de ponta a ponta com gatilhos; C2 com "quando necessário"; DECISOES fora do desenho da Lumis; contrapesos ao Head; limites de R1 e R2; ESTADO; idades dos incidentes; regra de agregação; Q16 (agente, explicabilidade, ISO/IEC 42001); recorte do novo setor invertido; estrutura do .docx enxuta e sem códigos.
- Descartada em parte: "a F2-E2 não manda tirar dados do próximo treino". O .docx salvo às 15:53 diz "Dado sem autorização e parecer fica fora do próximo treino" (Tabela 4). Foi mantida só a correção do "Já", trocado por "antes da próxima apresentação".
- Ajustada: a citação literal da regra de versão. O texto mudou às 15:53 e passou a ser "Versão que piora algum grupo não vai para produção". Foi citado o literal atual, e não "barrar versão que piore algum grupo".
- Descartada: a linha da §9 "F2-E2, indicador 1, 'a CEO decide' → revisar". A vigente já não diz isso e deixou o tema para a E3 (D-031). Também caiu "Camila propõe; Head aprova" como fonte da F2-E2 vigente: virou proposta, com nota de que constava da versão anterior.
- Descartada: "LGPD sem data de consulta" (cobertura). `F2-E5_Privacidade_v1.md`, l. 5, registra o Planalto conferido em 07/10/2026.
- Descartada: "convenção sem códigos internos não registrada" (coerência). Ela está na D-031, não commitada, criada depois da revisão.
- Ajustada: "Anexo é do fechamento do 2T2026". Esse título é só da seção 5.1. A data do Q12 ficou como [não consta].
- Ajustada: a recomendação da D-027 duplicada. Agora há duas duplicadas (D-027 e D-028), e a E3 começa em D-032, e não em D-031.
- Escolha entre alternativas: registro com o Head e conferência da DPO (arranjo da F2-E2), em vez de passar à DPO; suplente de execução Yuri Nakamura (base F1-E2), em vez de DPO; alerta "acima de 1,5", coerente com a meta da D-024, em vez de "≥ 1,5".
- Descartada: a sugestão de dar à CEO a "palavra final no go/no-go" dentro do comitê. A palavra final fica no portão (§8), e não no comitê.