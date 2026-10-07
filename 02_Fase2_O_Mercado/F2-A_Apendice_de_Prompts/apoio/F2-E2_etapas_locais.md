# F2-E2: resultado bruto das etapas sem pesquisa web

Material de apoio gerado pelos subagentes em 06/10/2026. Sem revisão de estilo.

## Entendimento da entrega

# F2-E2: o que é a entrega e o que o conselho espera dela

Nenhuma skill da Arkium cobre esta tarefa, porque é trabalho acadêmico da FIAP com empresa fictícia. Esta análise se baseia em cinco fontes: o Cap. 2 (texto limpo), o `Dados_Quadros_7-11.md`, os três arquivos de `00_Lumis/`, a v1 do colega (.docx), a F2-E1 v2 e as decisões D-004, D-007 e D-012 a D-022. Nenhum arquivo foi criado ou alterado.

---

## 1. O que é esta entrega

**Em linguagem simples:** a F2-E2 é a auditoria do único ativo que a Lumis diz ter, a base de dados, e dos números que ela usa para se vender. A pergunta do fundo é direta: "de que é feito o ativo da Lumis?" [fonte: Cap. 2, seção 4, p. 15]. A entrega responde a ela em quatro camadas:
- de onde vêm os dados e se a Lumis tem direito de usá-los;
- o que as variáveis medem de fato;
- se os números de vitrine se sustentam;
- quais números a gestão deveria acompanhar no lugar deles.

**Onde ela entra no dossiê.** O formato da fase é "um documento único, com identificação da equipe, reunindo as cinco entregas articuladas entre si — e não como cinco anexos independentes", mais um memorando ao conselho de no máximo duas páginas [fonte: Cap. 2, 4.2, p. 18]. A F2-E2 é a parte que responde aos itens 2 ("Fundamento do ativo") e 3 ("Evidência, não narrativa") do memorando do Vetor Capital [fonte: Cap. 2, p. 5].

**O que ela recebe da F2-E1 v2**, que já prometeu estes pontos:
- A tese: "o único ativo que poderia ser da Lumis, a base de dados, ainda não é dela".
- O texto: "A auditoria completa fica para a Entrega 2".
- O texto: "A Entrega 2 detalha contratos e métricas".
- A composição da base (Tabela 4 da F2-E1): 63,6% pública, 9,5% sintética, 26,8% de clientes.
- As quatro travas dos dados de clientes: autorização, concentração, escala e viés.
- A recomendação "Trocar os 94% por validação em campo, por subgrupo e publicada".
- O fosso possível (D-009): "dado de desfecho com direito de uso limpo e validação auditável por subgrupo".

**O que ela passa adiante:**
- **F2-E3 (Linha de responsabilidade):** cada indicador proposto precisa de um dono, e a F2-E3 vai exigir que "Toda responsabilidade precisa terminar em um cargo" [fonte: Cap. 2, p. 16]. Os gatilhos de suspensão dos indicadores (falso negativo por subgrupo) viram poder de suspender na F2-E3. Dois fatos tensionam essa ponte: hoje uma nova versão vai a produção por decisão exclusiva do CTO, e a revisão humana cobre 2% das 640 mil decisões por mês [fonte: Cap. 2, Quadro 12].
- **F2-E5 (ESG):** os dados da E5 incluem "Desempenho por subgrupo" e "Situação contratual dos dados" [fonte: Cap. 2, p. 17], que são a mesma matéria-prima da E2. A métrica pública de impacto que a E5 pede tem de sair de um dos cinco indicadores da E2, para não criar um número novo e solto.
- **Memorando:** a E2 entrega as "condições prévias" do aporte: regularizar contratos, aposentar as métricas que não se sustentam e passar a medir por subgrupo.

---

## 2. O objetivo: a pergunta e o que vai ser avaliado

**A pergunta:** que parte do ativo da Lumis sobrevive a uma auditoria independente, e o que precisa mudar para que o restante sobreviva?

**O que o enunciado exige, item a item** [fonte: Cap. 2, p. 15]:

| # | Exigência | Detalhe obrigatório |
|---|---|---|
| 1 | Origem, base **contratual e legal** dos dados | Com identificação dos **pontos frágeis** |
| 2 | Análise das principais variáveis | Para cada uma: o que pretende medir, o que de fato mede e que distorção introduz. **Ao menos um caso de proxy tratado explicitamente** |
| 3 | Revisão crítica das métricas apresentadas ao mercado | Como foram apuradas, **o que autorizam concluir e o que não autorizam** |
| 4 | Novo conjunto de indicadores de gestão | **No máximo cinco**, cada um ligado a **uma decisão concreta que ele muda**, com **abertura por subgrupo quando aplicável** |
| 5 | As quatro perguntas (Medida em quê? Por quem? Muda alguma decisão? Esconde qual distribuição?) | Aplicadas **a cada indicador proposto OU descartado** [fonte: Cap. 2, 2.3, p. 9] |
| 6 | Regra geral da fase | "Não invente números sobre a Lumis: se algo não está no anexo, trate como informação indisponível e diga isso explicitamente" [fonte: Cap. 2, seção 4, p. 14] |

**O que o professor vai avaliar:**
- **Critérios da seção 4.3** [fonte: Cap. 2, p. 18-19]:
  - *Honestidade analítica*: "registrar as fragilidades encontradas no ativo da Lumis em vez de contorná-las".
  - *Rigor sobre dados e métricas*: "o que as variáveis representam e a diferença entre número apresentável e número útil".
  - *Integração e defesa*: coerência entre as cinco entregas e o memorando.
- **Disciplinas do Quadro 2** [fonte: Cap. 2, 4.1, p. 17]:
  - Computational Thinking & AI for Leaders: "leitura crítica de dados, variáveis e representação da informação; análise de proxies e de suas distorções".
  - Data-Driven Business & Analytics: "distinção entre métrica de vaidade e métrica de decisão; construção do conjunto de indicadores de gestão".
- **Conceitos do capítulo que o leitor espera ver aplicados:**
  - "dado como testemunho" (2.2, p. 7);
  - o exemplo do gasto como proxy de gravidade: "está medindo quem teve mais acesso a atendimento" (2.2, p. 8);
  - métricas de vaidade (2.3, p. 8);
  - a lei de Goodhart (2.3, p. 8: "No momento em que a acurácia vira o número que define bônus e discurso comercial...").

**Onde a v1 do colega fica aquém dessas exigências:**
1. **Indicadores descartados:** as quatro perguntas só aparecem nos cinco indicadores propostos. Os descartes não passam por elas: as cinco métricas do Quadro 11 e o indicador "auditorias contratuais concluídas", que é citado mas não testado. O enunciado pede "proposto OU descartado", e essa é a lacuna mais clara.
2. **Base legal:** a v1 trata só o lado contratual. A LGPD, com dado de saúde como dado sensível, não aparece. Também falta a política de privacidade para dados de saúde, que está "em elaboração desde 2024, sem versão aprovada" [fonte: Cap. 2, Quadro 17].
3. **Vantagem defensável:** o item 2 do memorando pergunta "qual parte disso constitui vantagem defensável", e a v1 não responde.
4. **Caso de proxy:** a v1 escolheu o CEP. É válido, mas o próprio capítulo dá o exemplo de custo e gasto (2.2), e o Quadro 8 tem "Custo acumulado → Gravidade" (15,1%) e "Nº de atendimentos → Necessidade" (18,4%). O caso mais forte é o par custo e atendimentos, com o CEP como reforço.
5. **Fontes erradas:** a v1 atribui as quatro perguntas ao "Capítulo 1". Elas estão no Cap. 2, 2.3.
6. **Marcadores:** faltam `[fonte]`, `[hipótese]` e `[não consta]`.
7. **Fatos de apoio não usados:**
   - Quadro 14: o incidente de 01/2026 foi "Corrigido no sistema; não corrigido no material comercial", e isso reforça que o "5 milhões de vidas" é passivo conhecido.
   - Quadro 17: o cruzamento de reclamações por CEP "nunca foi" feito.
   - A divergência "três" (narrativa, p. 6) contra "dois" (Quadro 5) nos maiores contratos frágeis, que deve ser sinalizada conforme D-003.

---

## 3. O que precisamos comunicar (mensagens centrais)

**M1. A base parece grande, mas a parte que só a Lumis tem é pequena e tem autorização frágil.**
- A base soma 22,0 mi de registros, e só 26,8% (5,9 mi) vêm de clientes.
- Desses, 35,4% (2,09 mi, Vila Ipê e Prisma) têm autorização "genérica" ou "silente".
- O contrato da Prisma vence em 12/2026, e nenhum dos seis instrumentos passou por revisão jurídica.
- O modelo atual já foi treinado com esses dados, então o risco é de hoje, e não só nos vencimentos.

[fonte: Cap. 2, Quadro 7] O ponto da LGPD (dado de saúde é sensível, e a base legal para treinar um produto vendido a terceiros é incerta) entra como [hipótese], porque o caso não traz parecer jurídico. A política de privacidade de saúde ainda não foi aprovada [fonte: Quadro 17].

**M2. O modelo mede acesso ao sistema de saúde e chama isso de gravidade.** É o caso de proxy e o mecanismo do viés do D-004.
- Os dois maiores pesos são nº de atendimentos (18,4%) e custo acumulado (15,1%). Juntos somam 33,5%, e os dois medem quem conseguiu ser atendido [fonte: Quadro 8; Cap. 2, 2.2].
- Se somarmos as variáveis que tendem a refletir acesso, renda ou rede (atendimentos, custo, tempo consulta-exame, CEP, plano e faltas), elas pesam 64,9%. As variáveis mais diretamente clínicas (comorbidades e painel laboratorial) pesam 18,1% [cálculo da equipe sobre o Quadro 8; a classificação é [hipótese]].
- Um ponto aparentemente contraditório ajuda a explicar: a idade tem peso de 12,7%, mas o idoso de CEP D/E é quem mais fica para trás. Uma leitura possível é que a idade puxa a prioridade para cima e as variáveis de acesso puxam para baixo quem tem menos histórico registrado [hipótese, a testar na Fase 3].
- A definição técnica de "peso" [não consta].

**M3. Os 94% descrevem 48 mil registros de 2023, e não o produto em campo. Em campo, o erro que importa dobra e se concentra em quem já é mais vulnerável. Esta é a mensagem desconfortável.**
- Na validação, o falso negativo é de 7,4%. Em campo, com 1,94 mi de registros, sobe para 17,7% [fonte: Quadro 9].
- No grupo de 60 anos ou mais em CEP D/E, o falso negativo é de 31,8%: quase 1 em cada 3 pacientes que deveriam ser priorizados não é, três vezes o melhor subgrupo (10,6%) [fonte: Quadro 10].
- O número mais incômodo foi medido por outra pessoa: foi o Vila Ipê, e não a Lumis, que apurou e enviou o dado [fonte: Cap. 2, p. 25]. Isso responde, na prática, à pergunta "Medida por quem?".
- O CEP D/E é 25% da base e concentra 64% das reclamações, e esses dados nunca foram cruzados com o desempenho do modelo [fonte: Quadro 17].
- A mensagem não deve ser suavizada. A frase do capítulo ajuda o tom: "O número nunca foi mentira. Ele apenas nunca foi o que o comercial acreditava que era" (p. 6).

**M4. Nenhuma das cinco métricas públicas sobrevive a uma auditoria independente do jeito que é divulgada. Pela regra do fundo, hoje elas são passivo.**

[fonte: Quadro 11; memorando, item 3]

| Métrica | Por que não se sustenta | Fonte |
|---|---|---|
| 94% | Ambiente controlado | Quadros 9 e 11 |
| -30% no tempo de triagem | Um hospital, seis semanas, sem grupo de controle | Quadro 11 |
| 5 mi de vidas | Duplicidade já detectada e não corrigida no material comercial | Quadro 14 |
| NPS 72 | Nove respondentes escolhidos pelo comercial | Quadro 11 |
| 99,9% | Mede a API, e não o serviço | Quadro 11 |

A ligação com Goodhart [fonte: Cap. 2, 2.3] explica como uma empresa honesta chega a esse painel. Essa explicação prepara a F2-E4 (fratura entre técnico e comercial).

**M5. A Lumis precisa trocar números de vitrine por cinco indicadores de gestão, cada um com dono e gatilho de decisão. Isso é condição prévia do aporte e é o caminho para o fosso.**
- A validação auditável por subgrupo e o direito de uso limpo são o que pode tornar a base difícil de copiar [fonte: F2-E1 v2; D-009].
- Os cinco indicadores da v1 servem de base, mas dois pedem revisão:
  - "Disponibilidade ponta a ponta": precisa dizer que decisão muda. Senão, é melhor trocá-lo por um indicador de validação externa ou de evidência reproduzível.
  - "Reclamações por 1.000": o denominador por subgrupo depende de volumes absolutos que o caso só dá em percentual (Quadro 17). Marcar [hipótese] ou explicar a conta.
- Nenhum indicador deve estimar "pacientes prejudicados por mês". A prevalência de casos de alta prioridade [não consta], então não dá para converter a taxa de falso negativo em número de pessoas.

---

## 4. O que o conselho e o Vetor Capital gostariam de ver

**Perguntas que um conselheiro faria ao ler:**
1. "Se um cliente ou a ANPD questionar amanhã, quanto da base a Lumis teria de retirar, e o modelo continua de pé sem esses dados?" (item 2: base legal)
2. "Quanto disso é nosso de verdade? DATASUS qualquer um tem." (item 2: vantagem defensável)
3. "Qual número da apresentação eu posso repetir para o meu comitê sem ser desmentido?" (item 3)
4. "Quem mediu o 31,8%? Vocês sabiam antes do hospital?" (Medida por quem; Quadro 14: detectado pelo cliente)
5. "O que acontece no dia em que o falso negativo de um subgrupo passar do limite? Quem desliga, e em quanto tempo?" (ponte com a F2-E3 e com C2)
6. "Isso vai se repetir quando entrarmos em outro setor?" (Cap. 2, 2.6: "replicação de um problema em escala maior")

**O que o deixaria seguro:**
- Números ruins mostrados pela própria Lumis, com fonte e sem eufemismo.
- Um inventário claro do que é ativo, do que é passivo e do que é condição para virar ativo.
- Um prazo concreto: Prisma antes de 12/2026 e Vila Ipê antes de 03/2027.
- Indicadores com dono (cargo), periodicidade, limite e a ação que cada limite dispara.
- A separação entre fato, cálculo da equipe, hipótese e o que não consta. Isso mostra que o documento sobrevive a uma auditoria.

**O que o faria desconfiar:**
- Repetir 94%, "5 milhões de vidas" ou NPS 72 em qualquer parte do dossiê sem a ressalva. Pela regra do fundo, isso é passivo assumido.
- Média sem abertura por subgrupo.
- Hipótese jurídica apresentada como fato, ou fato apresentado com rodeio.
- Mais de cinco indicadores, ou indicador sem decisão associada ("decoração", Cap. 2, 2.3).
- Proxy tratado como curiosidade técnica. O capítulo diz que "Era uma decisão de gestão. Sempre foi." (2.2).

---

## 5. Como comunicar isso ao conselho

**Formato.** Seguir a F2-E1 v2 (D-012, D-018 a D-021):
- relatório ao conselho com a conclusão no início, num destaque de duas ou três frases mais três tópicos, sem repeti-la no fim;
- seções que se encadeiam;
- tabelas só onde guardam números, figuras simples e poucas;
- fontes nas legendas e citação leve no texto;
- no máximo cinco referências externas;
- arquivo .docx a partir do `Modelo_Entrega_Lumis.docx` (D-013 a D-015).

O tamanho sugerido é de 4 a 5 páginas de corpo, o mesmo da F2-E1 (D-008/D-018).

**Tese sugerida para o destaque:** "O ativo da Lumis é real, mas ainda não é auditável: a parte exclusiva da base tem autorização frágil, o modelo mede acesso como se fosse gravidade e os números que vendem o produto não sobrevivem fora da demonstração."

**Ordem das seções**, que segue o enunciado e encadeia as mensagens:

| Seção | Conteúdo | No corpo | Fica fora do corpo |
|---|---|---|---|
| 0. Destaque | Tese mais 3 tópicos (direito de uso, proxy/viés, métricas) | Texto | |
| 1. De onde vêm os dados e se podemos usá-los | M1; ativo, passivo e condição | Tabela 1: fontes, volume, autorização, vencimento, risco (Quadro 7, compacta) | Contas de conferência e divergência "três/dois" em nota |
| 2. O que o modelo mede de fato | M2; caso de proxy explícito (custo e atendimentos, mais CEP) | Tabela 2: as 10 variáveis com "diz medir / mede de fato / distorção", ou só as 6 de acesso, com as demais em nota | Classificação completa em anexo, se ficar longa |
| 3. O que acontece em campo | M3, a mensagem desconfortável | Figura 1: falso negativo por subgrupo (a da v1 serve). Quadro 9 em duas linhas no texto ou numa tabela mínima | |
| 4. Os números que mostramos ao mercado | M4 | Tabela 3: métrica, como foi apurada, o que autoriza, o que não autoriza e decisão (manter, reformular ou aposentar). Essa decisão é o "descarte" que exige as quatro perguntas | Quatro perguntas aplicadas a cada métrica descartada, em anexo ou em colunas curtas |
| 5. O que passamos a medir | M5; até 5 indicadores | Tabela 4: indicador, decisão que muda, gatilho, dono (cargo), abertura | Tabela completa das quatro perguntas por indicador, em anexo |
| 6. O que isso muda na tese | 3 ou 4 linhas: condições prévias para o memorando e pontes com E3 e E5 | Texto | |
| Notas e referências | Fonte por quadro; distinção entre fato, cálculo e hipótese | | |
| Apêndice | Prompts e verificação (D-007) | | Obrigatório só na E1 [fonte: 4.2]. Na E2 é opcional, mas coerente com a trilha de auditoria pedida pela equipe |

**Tom:**
- Frases curtas e declarativas, com o número logo depois da afirmação.
- Sem eufemismo nem adjetivo: "1 em cada 3 idosos de CEP D/E que deveriam ser priorizados não é" funciona melhor que "desempenho materialmente inferior".
- Falar das pessoas pela conduta e pelo fato, sem atribuir culpa ao comercial. A explicação estrutural vem de Goodhart e da cultura (F2-E4).
- Marcar `[fonte: Cap. 2, Quadro X]`, `[hipótese]` e `[não consta]` com os estilos Tag do modelo.
- Passar o texto pela skill humanizer (PT-BR) antes da versão final (D-010).

**[não consta] que o caso não traz e que deve ser declarado no texto:**
- a definição de "peso";
- a prevalência de casos de alta prioridade;
- se os outros 34 contratos envolvem dados;
- parecer jurídico ou LGPD;
- o volume absoluto por subgrupo para a taxa de reclamações;
- o desempenho por cliente.

---

## 6. Pontes obrigatórias

| Ponte | O que a E2 precisa mostrar | Tensão a decidir |
|---|---|---|
| **C1 Transparência** | Exige informar "as limitações". O painel do Quadro 11 contradiz isso hoje. A E2 deve recomendar a correção pública das métricas (aposentar ou reformular), em especial a duplicidade "não corrigida no material comercial" [Quadro 14]. | Manter C1 e assumir o custo comercial de rever o painel. Contrariar isso exige nova entrada em DECISOES. |
| **C2 Não Amplificação de Danos** | Exige "Revisão quinzenal com indicadores por grupo" e "Suspensão do uso até a correção quando houver padrão de viés". O indicador de falso negativo por subgrupo é a forma de medir C2 e deve ter periodicidade quinzenal, coerente com o compromisso. O cruzamento entre reclamações e desempenho [Quadro 17] também é C2. | Os 31,8% já são um "padrão de viés". Pela letra do C2, há suspensão pendente (o incidente segue "Em tratamento", Quadro 14). A E2 precisa nomear isso, e a decisão sobre suspender ou restringir fica para a E3. Não pode ficar em silêncio. |
| **C5 Segurança e Privacidade** | "Minimização de dados": questionar variáveis como CEP e tipo de plano, que pesam e não são clínicas. Também os 35,4% com autorização frágil e a política de saúde não aprovada [Quadros 7 e 17]. | O C5 diz "a Lumis" sem cargo. A E2 já deve indicar o DPO (Ana Beatriz Rangel, Quadro 13) como dona do indicador contratual, o que prepara a E3. |
| **D-004 (viés vindo dos dados)** | A E2 é onde o D-004 ganha mecanismo: as variáveis de acesso (Quadro 8) transformam menor acesso histórico de idosos periféricos em baixa prioridade, e os Quadros 10 e 17 mostram o efeito. Citar D-004 [fonte: F1-E1]. | O mecanismo exato é [hipótese] até a Fase 3 ("O Motor"). |
| **Promessas da F2-E1 v2** | (a) "auditoria completa" dos contratos, incluindo as condições de Sanare (anonimizado) e Meridiano (auditoria anual); (b) "detalha contratos e métricas"; (c) "Trocar os 94% por validação em campo, por subgrupo e publicada" vira indicador; (d) as quatro travas (autorização, concentração, escala, viés) reaparecem; (e) o fosso possível (D-009). | Coerência de números com a F2-E1: 35,4%, 9,5%, 26,8%, 63,6% e "seis instrumentos sem revisão jurídica" (D-017). |

**Arquivos usados:**
- `C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Dados_Quadros_7-11.md`
- `C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/F2-E2_Auditoria_do_Ativo_v1.docx`
- `C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/README.md`
- `C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E1_Mapa_do_Territorio/F2-E1_Mapa_do_Territorio_v2.docx`
- `C:/Users/gusta/Downloads/LumisOS/00_Lumis/Compromissos_Vigentes.md`
- `C:/Users/gusta/Downloads/LumisOS/DECISOES.md`
- `C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/21178879-392f-48c9-b000-b7bcda3abb02/scratchpad/cap2_limpo.txt`

## Auditoria da v1 do colega

# Auditoria crítica da v1 da F2-E2 (Auditoria do Ativo)

Skills usadas: `humanizer` (SKILL.md e PT-BR.md, lidas da pasta do projeto). Nenhuma skill Arkium cobre este tema, que é um trabalho acadêmico da FIAP.

O que li: o texto completo da v1 (`F2-E2_Auditoria_do_Ativo_v1.docx`, com parágrafos, tabelas, negritos e estilos), a Figura 1 (`figuras/fig1_subgrupo.png`) e `Dados_Quadros_7-11.md`. Também conferi no `cap2_limpo.txt` as seções 1.2, 2.2, 2.3 e 4.3, o enunciado das Entregas 2 e 3 e os Quadros 10 a 12. Li ainda `Compromissos_Vigentes.md`, `Pessoas_e_Cargos.md`, `Empresa_e_Contexto.md`, D-003, D-004, D-012 e D-017 a D-021, e a F2-E1 v2.

## Veredito em poucas linhas

A v1 está bem montada. Os números que ela usa estão certos e ela cobre os quatro blocos do enunciado. Na correção, perderia pontos em três frentes:

1. **Parte legal.** A v1 só trata do contrato. A LGPD não aparece, nem a política de privacidade que está sem versão aprovada.
2. **As quatro perguntas não foram aplicadas aos descartes.** O enunciado pede as perguntas para cada métrica descartada, e a v1 não fez isso para as cinco métricas do painel comercial nem para o indicador de auditorias contratuais. Ela também deixa de usar dados do caso que mudam a leitura: o incidente de 01/2026, as reclamações por CEP, a revisão de 2% e a sensibilidade e a participação de cada subgrupo.
3. **Responsabilidade e comunicação.** Os responsáveis terminam em áreas, e não em cargos. O texto não traz nenhum marcador `[fonte]`, `[hipótese]` ou `[não consta]`, cita o capítulo errado e fala para técnicos, quando deveria falar ao conselho e começar pela conclusão.

A v1 também não responde a uma pergunta do memorando do fundo: **qual parte do ativo é defensável hoje.**

---

## 1. Fidelidade aos dados

Números conferidos e corretos: 22,0 mi; 5,9 mi (26,8%); 2,09 mi (35,4%); 9,5% da base; os seis instrumentos sem revisão jurídica; os vencimentos 12/2026 e 03/2027; os pesos do Quadro 8; o Quadro 9 inteiro. As variações também batem: −6,5 p.p., −10,3 p.p. e +10,3 p.p. Batem ainda os 31,8% contra 10,6% (3,0 vezes) e os cinco valores do Quadro 11. Não achei número errado. Os problemas são de citação, de dados que ficaram de fora e de leitura apresentada como fato.

| ID | Trecho da v1 | Problema | Correção sugerida |
|---|---|---|---|
| V1-01 | Seção 8: "Capítulo 1 — 'A IA e o Mercado', seção 2.3" e seção 6: "as quatro perguntas do Capítulo 1" | Citação errada. O Cap. 1 é "Gestão de IA: Um Caminho sem Volta". As quatro perguntas estão no Cap. 2, seção 2.3, p. 9. O próprio enunciado fala em "perguntas apresentadas neste capítulo". | Trocar por `[fonte: Cap. 2, 2.3, p. 9]` nas duas passagens. |
| V1-02 | Seção 8: "Anexo A do case" | Os quadros não estão numerados e falta o Quadro 10 como fonte do gráfico. O texto também usa os Quadros 12, 14 e 17 sem citar. "Case" é anglicismo. | Citar `[fonte: Cap. 2, Quadro N]` em cada legenda, como manda D-018, e trocar "case" por "caso". |
| V1-03 | Fig. 1 e leitura do gráfico: só o falso negativo | Faltam a **sensibilidade** e a **participação na base** do Quadro 10. Com elas, a leitura muda. A sensibilidade de 60+ D/E é **68,2%**, contra 89,4% no melhor grupo. Os três subgrupos acima da média de 17,7% (18-59 D/E 20,2%, 60+ C 23,5%, 60+ D/E 31,8%) somam **39% da base** `[cálculo: 15+14+10]`. O problema não fica num nicho de 10%. | Tabela com os seis subgrupos e as colunas participação, sensibilidade e falso negativo. Frase para o conselho: "o modelo erra acima da média em quatro de cada dez pacientes da base". |
| V1-04 | Seção 5: "Mais de 5 milhões de vidas… Substituir… ou deduplicar" | Fica de fora o **Quadro 14 (01/2026)**: a duplicidade foi achada pela auditoria interna, corrigida no sistema e **não corrigida no material comercial**. Ou seja, a empresa sabe há cerca de nove meses que o número está inflado e continua a divulgá-lo. É o ponto mais sensível para o critério de honestidade e para C1. | Dizer isso com todas as letras, com fonte. Decisão: retirar o número já e publicar o valor deduplicado. Esse valor `[não consta]` no caso. |
| V1-05 | O texto não fala do Quadro 17 | Faltam as reclamações por CEP (A/B 8, C 19, D/E 47) e o fato de que **nunca foram cruzadas** com o desempenho do modelo. Por paciente, a faixa D/E registra cerca de **8 vezes** mais reclamações que a A/B `[cálculo: (47/25)/(8/34) = 8,0]`. Esse é o segundo sinal independente do viés, ao lado do Quadro 10. | Usar na seção de desempenho e no indicador 5. Citar `[fonte: Cap. 2, Quadro 17]`. |
| V1-06 | O texto não fala do Quadro 12 | Falta o dado de **revisão humana por amostragem de 2%** em 640 mil decisões por mês, ou seja, 12.800 revisões por mês `[cálculo]`. É isso que limita como o falso negativo pode ser medido em campo. Também fica de fora que o uso foi autorizado pela diretoria comercial do cliente sem aprovação interna. | Citar no indicador 1, em "Medida em quê?". Mostrar que, com amostra proporcional, o subgrupo 60+ D/E teria cerca de 1.280 casos revisados por mês `[hipótese: amostragem uniforme]`. |
| V1-07 | Seção 4 toma 87,6% e 17,7% como verdade | O número de campo também precisa passar pelas quatro perguntas. O caso não diz como a Lumis chegou ao valor de referência em campo `[não consta]` (desfecho? revisão?). A amostra de 1,94 mi no semestre é menor que as cerca de 3,84 mi priorizações do período `[cálculo: 640 mil × 6]`. | Dizer: "o número de campo é o melhor disponível, mas o caso não informa como foi apurado `[não consta]`". O próprio indicador proposto resolve isso. |
| V1-08 | Tabela 1: Sanare e Meridiano "Mais robusta" | Leitura otimista demais. Nenhum dos seis instrumentos passou por revisão jurídica. A Sanare autoriza só uso **agregado e anonimizado**, e se o treinamento usa registro por paciente, a condição pode não estar sendo cumprida `[hipótese]`. Se o Meridiano fez a auditoria anual exigida, `[não consta]`. A F2-E1 v2 já diz que essas autorizações "dependem de condições". | Trocar por "Autoriza, com condição ainda não verificada". |
| V1-09 | Tabela 1: DATASUS "Sem fragilidade contratual indicada" e sintéticos "Controle interno" | Duas lacunas. (a) O DATASUS é 63,6% da base e vai só até 2024. Ele retrata a população do SUS, enquanto a Lumis é usada em hospitais privados, seguradoras e bancos, o que é uma distorção de representação `[hipótese]`. (b) O caso não diz de que dados os sintéticos foram gerados `[não consta]`. Se vieram de dados de clientes, herdam a fragilidade deles `[hipótese]`. | Uma linha para cada ponto. |
| V1-10 | O texto não fala das divergências do Cap. 2 | Os dados de clientes vêm de 38 contratos, e só 4 fontes aparecem no Quadro 7. O Quadro 5 fala em "dois" contratos frágeis e a narrativa (1.2) em "três dos maiores clientes". Pela regra D-003, isso precisa ser sinalizado. | Nota curta: "[não consta] se os outros 34 contratos tratam de dados; o Cap. 2 diverge entre dois e três contratos frágeis; usamos o Quadro 7". |
| V1-11 | Seção 1: "risco é transformar desigualdades de acesso em sinais aparentemente clínicos" | Boa leitura, mas apresentada como fato. Que as variáveis causam o viés é **hipótese**, embora consistente com D-004 e com o Quadro 10. O próprio texto da seção 3 diz "sem assumir causalidade", e a síntese não segue isso. | Marcar `[hipótese]` e ligar a D-004 `[fonte: F1-E1]`. |
| V1-12 | Tabela 2, coluna "Risco: Alto / Médio / Muito alto" | É uma classificação da equipe, mas aparece sem rótulo, como se fosse dado. O caso também não define o que é "peso" `[não consta]`. | Legenda: "Risco: leitura da equipe" e nota sobre o "peso". |
| V1-13 | "exatamente três vezes" | A conta está certa (3,0). O "exatamente" é ênfase desnecessária. | "três vezes". |

## 2. Cumprimento do enunciado, item a item

| ID | Item do enunciado | Situação na v1 | Correção |
|---|---|---|---|
| V1-14 | Origem, base contratual **e legal** | **Parcial.** O título da seção diz "contratual/legal", mas só o contrato é tratado. O item 2 do memorando pergunta "sob que base legal". Ficaram de fora: (a) dado de saúde é dado pessoal sensível na LGPD, e treinar um produto vendido a terceiros pede base legal própria; (b) é preciso dizer se os dados estão de fato anonimizados; (c) a política de privacidade para dados sensíveis de saúde está **em elaboração desde 2024, sem versão aprovada** `[fonte: Cap. 2, Quadro 17]`; (d) quem controla o dado: o hospital é controlador e a Lumis é operadora `[hipótese]`. A F2-E1 v2 deixou a base legal como `[hipótese]` e passou "a auditoria completa" para esta entrega. | Criar uma subseção "Base legal", curta. A LGPD (arts. 5º, 11 e 12) entra como contexto externo com referência completa, e as conclusões jurídicas ficam como `[hipótese]` até o parecer da DPO. Fechar com o pedido: "parecer de Ana Beatriz Rangel (DPO) sobre os seis instrumentos antes do próximo treinamento". |
| V1-15 | Variáveis: o que pretendem medir, o que medem, distorção | **Atendido em forma.** A Tabela 2 tem as três colunas, mas a distorção vem genérica ("pode refletir…") e sem a **direção do efeito**. Não explica como cada variável empurra o idoso de CEP D/E para baixa prioridade: menos atendimentos, menor custo, mais faltas e maior tempo até o exame levam a pontuação menor `[hipótese: direção dos coeficientes não consta]`. | Ligar cada variável de alto risco ao resultado do Quadro 10 numa frase. Dar o número que resume tudo: **64,9% do peso** dos dez maiores está em variáveis que medem acesso ou uso do serviço (atendimentos, custo, tempo até exame, CEP, plano e faltas) `[cálculo]` `[classificação da equipe]`. Só 18,1% está em variáveis clínicas diretas (comorbidades e exames) `[cálculo]`. |
| V1-16 | "Trate explicitamente ao menos um caso de **variável proxy**" | **Atendido, mas com o caso mais fraco.** A v1 escolhe o CEP, e a empresa diz que o CEP mede "região de residência", o que de fato mede. O proxy de verdade é aquele em que o que a empresa diz que mede é diferente do que se mede: **custo acumulado → "gravidade"** (15,1%), que é **o exemplo do próprio Cap. 2, seção 2.2** ("histórico de gastos… mede quem teve mais acesso"), e **nº de atendimentos → "necessidade de cuidado"** (18,4%, o maior peso). O professor espera ver o conceito do capítulo aplicado. | Fazer do custo acumulado o caso explícito de proxy, citando 2.2, e deixar o CEP como complemento, porque leva renda para dentro do modelo. Se quiserem, usar como análogo real o estudo de Obermeyer et al. (2019, *Science*), sobre um algoritmo que usava gasto como proxy de necessidade, como contexto externo com referência completa, verificado conforme D-007. |
| V1-17 | Métricas ao mercado: como foram apuradas, o que autorizam e o que não autorizam | **Atendido.** A Tabela 4 é boa. Falta usar o vocabulário do capítulo: **métrica de vaidade** e **lei de Goodhart** (a acurácia virou número de discurso comercial, como no exemplo da seção 2.3). Falta também dizer que, numa fila de priorização, **acurácia é a métrica errada** para virar manchete, porque esconde o falso negativo. | Uma frase com cada conceito, citando a seção 2.3. |
| V1-18 | Até 5 indicadores, cada um com uma **decisão concreta** que ele muda | **Parcial.** As decisões estão escritas como menu de opções ("investigação, recalibração, restrição ou suspensão quando houver deterioração relevante") e sem **gatilho**. Um conselheiro pergunta: "a partir de que número a Lumis suspende?". | Para cada indicador: um limite proposto pela equipe e marcado como proposta, uma decisão e quem decide. Exemplo: "falso negativo de qualquer subgrupo acima de X%, ou pior grupo acima de 2 vezes o melhor, leva à suspensão do uso naquele perfil até correção (C2)". |
| V1-19 | Abertura por subgrupo | **Atendido** nos cinco indicadores. Mas o indicador 5 promete abrir "por CEP e idade", e o Quadro 17 só traz CEP. | "Idade: [não consta] hoje; passa a ser registrada." |
| V1-20 | **Quatro perguntas aplicadas a cada indicador descartado** | **Não atendido.** As cinco métricas do painel comercial foram descartadas ou reformuladas, e a Tabela 4 **não aplica as quatro perguntas** a elas: tem outras colunas. O caso mais claro de "Medida por quem?" está aí: no NPS, os respondentes foram "todos indicados pelo time comercial", e quem mede tem interesse no resultado. | Criar uma tabela de descartes com as quatro perguntas como colunas, em cada uma das cinco métricas. Pode ser a própria Tabela 4 refeita: "Medida em quê / por quem / muda decisão / esconde qual distribuição / destino". |
| V1-21 | "Auditorias contratuais concluídas" descartado num parágrafo | O indicador não vem do caso e aparece do nada: é a figura que o humanizer chama de "discutir com ninguém" (§5). Também não recebeu as quatro perguntas. | Ou entra na tabela de descartes com as quatro perguntas, ao lado dos outros candidatos considerados, ou sai do texto. |
| V1-22 | Seção 7 "Decisões recomendadas" | O enunciado não pede essa seção, e ela repete as seções 2 a 6. Diz "instituir os cinco indicadores com responsáveis e periodicidade definidos", mas eles não foram definidos (só o indicador 1 tem periodicidade). | Absorver na abertura (o que pedimos ao conselho) ou cortar. |

## 3. Honestidade analítica e rigor

| ID | Ponto | Problema | Correção |
|---|---|---|---|
| V1-23 | "o ativo… é relevante em escala, mas não pode ser tratado como plenamente defensável" | **Suaviza.** O critério de honestidade pede o registro direto da fragilidade. "Não plenamente defensável" é eufemismo. | Dizer o que é defensável hoje, em números (ver V1-24). |
| V1-24 | Falta "qual parte constitui vantagem defensável" (memorando, item 2) | Não está respondido. Com os dados: **73,2% da base não é exclusiva** (DATASUS e sintéticos) `[cálculo]`. Dos 26,8% de clientes, só Sanare e Meridiano têm autorização expressa, ou seja, 3,81 mi, **17,3% da base**, e mesmo assim com condições não verificadas e sem revisão jurídica `[cálculo]`. A Sanare sozinha é cerca de 74% do dado clínico de clientes, o que traz risco de concentração `[cálculo; já na F2-E1 v2]`. E é dessa base que vem o viés (D-004). | Uma tabela curta: "o que é nosso / com que direito / o que trava", coerente com a Tabela 3 da F2-E1 v2 ("Difícil de copiar: nada hoje"). |
| V1-25 | Sobre o indicador 3, "Cobertura contratual válida" | A v1 não calcula o valor de hoje. Pela definição dela (autorização explícita **e** revisão jurídica vigente), o valor atual é **0%**, porque nenhum instrumento foi revisado. Só pela autorização, fica em no máximo 64,6% `[cálculo]`. Esse é o número mais forte da entrega para o conselho. | Mostrar o valor de hoje em cada indicador, quando houver dado, ou `[não consta]`. |
| V1-26 | Vila Ipê aparece em dois papéis sem ligação | O cliente que notificou o viés (Quadro 10) é também a fonte com cláusula genérica, que vence em 03/2027 (Quadro 7). A Lumis depende dos dados de quem está reclamando dela. | Uma frase na seção de origem dos dados. |
| V1-27 | A v1 não separa fato, cálculo e hipótese | Não há nenhum marcador no documento, o que contraria a regra do curso ("não invente números… diga isso explicitamente") e o CLAUDE.md (estilos Tag do modelo). As variações em p.p. são cálculo e aparecem como dado. | Marcar com `[fonte]`, `[cálculo]`, `[hipótese]` e `[não consta]` usando os estilos Tag do `Modelo_Entrega_Lumis.docx`. |
| V1-28 | O indicador 2 ("Drift vs. baseline") repete o indicador 1 | Os dois medem sensibilidade e falso negativo por subgrupo e só mudam o momento (troca de versão ou rotina). Gasta uma das cinco vagas. A evidência que o justificaria não é citada: o incidente de 09/2025, queda após atualização do fornecedor, 6 dias para corrigir `[Quadro 14]`. | Juntar ao indicador 1 como uma regra ("nenhuma versão entra se piorar o falso negativo de algum subgrupo") e usar a vaga livre num indicador que falta. Candidatos: (a) **parcela dos incidentes detectada pela própria Lumis, e não pelo cliente**: hoje 2 de 4 vieram do cliente, com 22 dias e "em tratamento" `[Quadro 14]`; (b) **discordância do revisor humano por subgrupo** na amostra de 2%, que liga a C3 e alimenta o indicador 1. Decisão da equipe. |
| V1-29 | O indicador 4 ("Disponibilidade ponta a ponta") | Conserta uma métrica de vaidade, mas é operacional, não tem abertura por subgrupo que faça sentido para equidade e não muda nenhuma decisão do conselho. | Avaliar se vira descarte (com as quatro perguntas) ou sai para dar lugar a um dos candidatos de V1-28. Decisão da equipe. |
| V1-30 | Pela C2, a situação atual já deveria disparar ação | 31,8% é um "padrão de viés". A C2 prevê suspensão até a correção, e a v1 não diz se isso já vale hoje. O Cap. 2 (1.1) informa que há plano de contenção com revisão humana obrigatória nos casos de maior impacto. | Uma frase: "pelo nosso compromisso C2, o 31,8% já é gatilho; hoje vale o plano de contenção `[fonte: Cap. 2, 1.1]`; o indicador 1 formaliza o gatilho". |

## 4. Responsabilidade ("Medida por quem?")

| ID | Trecho | Problema | Correção |
|---|---|---|---|
| V1-31 | Tabela 5: "área de Dados", "DPO/Jurídico", "Operações/Tecnologia", "CS registra; Gestão de IA cruza" | Termina em **áreas**. A regra da F2-E3 é "toda responsabilidade precisa terminar em um cargo", e o critério de avaliação da fase é "responsabilidade nomeada" (4.3). "Operações" nem existe no Quadro 13, e "CS" não tem responsável nomeado. | Usar os nomes do Quadro 13: Yuri Nakamura (Dados), Ana Beatriz Rangel (DPO), Paulo Adjaí (CTO), Head of AI Management (nós), Camila Torres (Comercial, a quem o CS responde `[hipótese]`). |
| V1-32 | "Medida por quem?" só diz quem calcula | A pergunta do capítulo é se **quem produz o número tem interesse no resultado** e se a apuração pode ser repetida por alguém de fora. A v1 não fala em conflito de interesse: o CTO libera a versão e mede o próprio desempenho, e o CS, sob o Comercial, registra as reclamações. Também falta quem **decide** com base no indicador. | Três papéis por indicador: quem apura, quem confere de forma independente (Head of AI Management ou o próprio cliente, como fez o Vila Ipê) e quem decide. Hoje só o CTO decide colocar uma versão em produção `[fonte: Cap. 2, texto após o Quadro 12]`, e isso é fragilidade a registrar e ponte para a F2-E3. |

## 5. Coerência com compromissos, decisões e F2-E1

| ID | Ponto | Problema | Correção |
|---|---|---|---|
| V1-33 | C2: "revisão **quinzenal** com indicadores por grupo" | O indicador 1 é "mensal", o que contradiz o compromisso vigente. | Quinzenal nos indicadores 1 e 5, ou nova entrada em DECISOES.md se a equipe quiser mudar a cadência. |
| V1-34 | C1, ponto de cobrança: painel comercial não reproduzível | A v1 trata do painel, mas não cita a C1 nem diz que manter os números atuais **descumpre** o compromisso de transparência. O Quadro 17 também diz que não há nenhuma métrica de impacto publicada. | Ligar a Tabela 4 à C1 numa frase. A métrica pública de impacto fica para a F2-E5. |
| V1-35 | C5, ponto de cobrança: política de privacidade e os 35,4% | Os 35,4% estão no texto, mas a política sem versão aprovada não, e a C5 não é citada. | Entra na subseção "Base legal" (V1-14). |
| V1-36 | D-004: o viés vem dos dados históricos e de uma falha de governança | A v1 nunca liga a análise de proxy ao diagnóstico da Fase 1. Isso conta no critério "Integração e defesa". | Uma frase: "a análise de variáveis confirma o diagnóstico da Fase 1 `[fonte: F1-E1; D-004]`". |
| V1-37 | F2-E1 v2: "A auditoria completa fica para a Entrega 2", contratos "pendentes de revisão", Tabela 4 (63,6 / 9,5 / 26,8%) | A v1 não retoma esses pontos. O vocabulário diverge: a F2-E1 usa "autorização fraca" e a v1 usa "frágil/robusta". | Retomar a composição da base com os mesmos números, usar o mesmo termo (sugestão: "autorização fraca ou ausente") e abrir com uma frase de ligação: "a Entrega 1 mostrou que a base é o único ativo possível; aqui verificamos de que ela é feita". |

## 6. Comunicação para o conselho

| ID | Trecho | Problema | Correção |
|---|---|---|---|
| V1-38 | Abertura: "Esta entrega audita a composição…" | Começa falando de si mesma (humanizer §25) e não pela conclusão. A F2-E1 v2 (D-012) abre com a tese. O conselho quer saber de cara de que é feito o ativo e se os números aguentam auditoria (memorando, itens 2 e 3). | Abrir com a tese em duas frases e três tópicos com números. Esboço: "Quase três quartos da base não são exclusivos da Lumis, e o que é exclusivo ainda não tem direito de uso verificado. Os números que vendemos não se sustentam fora da demonstração, e um deles está errado e sabemos disso desde janeiro." |
| V1-39 | "Conclusão executiva" no fim da seção 1 | A conclusão está escondida depois das três fragilidades. | Subir para a primeira linha e não repetir no fim (D-012). |
| V1-40 | Jargão: drift (2), baseline (1), rollback (2), E2E (2), API (2), claim (3), CS (1), case (3), "materialmente", "p.p." | Opaco para um conselheiro não técnico. | "Queda de desempenho entre versões", "versão aprovada", "voltar à versão anterior", "do início ao fim do serviço", "afirmação pública", "time de atendimento ao cliente", "caso", "bem menor". Explicar "p.p." uma vez e falso negativo em linguagem comum: "de cada 10 idosos de bairros D/E que precisavam de prioridade, 3 foram deixados para trás". |
| V1-41 | Travessões: 15 em-dash e 2 en-dash | Humanizer §8. Os quatro rótulos em negrito terminam em "—", e há "— ou deixados para trás", "— não só API —" e "18–59". | Trocar por dois-pontos ou ponto. Faixas: "18 a 59 anos". |
| V1-42 | "não é apenas a quantidade, mas o direito de uso" (seção 2), "não é apenas 'qual o peso', mas 'o que representa'" (seção 3), "mede atividade, não resultado" (seção 6) | Humanizer §1 ("não X, mas Y"). | Dizer direto: "O problema está no direito de uso." |
| V1-43 | "corrigir fragilidades…, monitorar proxies e substituir métricas" / "reproduzíveis, contextualizadas e auditáveis" / "renda, acesso a serviços e infraestrutura" | Tríades forçadas (§6). | Manter só os itens que trazem ideia distinta. |
| V1-44 | "robusta/robustez" (4 vezes), "crítico" (5), "relevante" (3), "particularmente críticos", "enxuto" | Palavras típicas de IA (§12). | "Clara", "expressa", "grave", ou cortar. |
| V1-45 | "Fecha a distância entre validação e campo." / "Transforma métricas em mecanismos de decisão." | Frase de efeito no fim (§2). | Cortar junto com a seção 7. |
| V1-46 | Seis tabelas e uma figura em três páginas, a Tabela 2 com dez linhas e a Tabela 5 com células longas | Denso para o conselho. Os números que mudam a conclusão ficam enterrados. | Seguir D-018/D-019: tabelas curtas, só com o que muda a conclusão. Mover a Tabela 2 completa para anexo e deixar no corpo as quatro ou cinco variáveis de acesso. |

## 7. O que está bom e deve ficar na v2

- **V1-47.** Todos os números conferem com o Quadro 7 ao 11. As contas (9,5%, −6,5/−10,3/+10,3 p.p., 3 vezes) estão certas.
- **V1-48.** A Tabela 1 por fonte, com vencimento e leitura de risco, e a prioridade Prisma, depois Vila Ipê. A frase "a renovação não deve ser o único gatilho" mostra que o risco existe hoje, como na F2-E1 v2 e em D-020.
- **V1-49.** A Tabela 2, com a coluna "O que a empresa diz medir" ao lado de "o que pode medir de fato". É o formato que o enunciado pede.
- **V1-50.** Ênfase em sensibilidade e falso negativo, e não em acurácia, como métricas certas para priorização.
- **V1-51.** A Tabela 4, com as colunas "autoriza / não autoriza". O conteúdo das cinco linhas está correto e é o ponto de partida da tabela de descartes.
- **V1-52.** Os indicadores 1 (falso negativo por subgrupo), 3 (cobertura contratual sobre os registros usados) e 5 (reclamações normalizadas por subgrupo, com a observação de que número absoluto sem denominador distorce). São os três melhores e devem ficar.
- **V1-53.** O cuidado com causalidade no CEP ("sem assumir causalidade apenas pela correlação"), que deve virar marcador `[hipótese]`.
- **V1-54.** A Figura 1, que é simples e legível. Na v2, colorir o grupo pior e incluir a sensibilidade ou a participação, ou trocar por tabela.

---

## As 10 mudanças mais importantes para a v2, em ordem

1. **Abrir pela conclusão, em linguagem de conselho** (V1-38, V1-39, V1-23, V1-24). Dar uma tese de duas frases e dizer o que é defensável hoje em números: 73,2% da base não é exclusiva; dos dados de clientes, só 17,3% da base tem autorização expressa, com condições não verificadas; nenhum instrumento foi revisado juridicamente.
2. **Tratar a base legal, e não só o contrato** (V1-14, V1-35, V1-08, V1-09). Dado de saúde sensível na LGPD, anonimização condicionada da Sanare, política de privacidade sem versão desde 2024 `[Quadro 17]`, DATASUS e sintéticos. LGPD como contexto externo com referência, conclusões como `[hipótese]` até o parecer da DPO.
3. **Aplicar as quatro perguntas a cada descartado** (V1-20, V1-21). Uma tabela com as cinco métricas do painel e qualquer outro candidato considerado, com as quatro perguntas como colunas.
4. **Trazer o incidente de 01/2026** (V1-04). O "5 milhões de vidas" está errado, a empresa sabe disso desde 01/2026 e continua divulgando. Decisão: retirar já.
5. **Trocar o caso explícito de proxy para custo acumulado e atendimentos** (V1-16, V1-15). É o exemplo da seção 2.2 do Cap. 2. Dar o número-resumo de 64,9% do peso em variáveis de acesso `[cálculo]` e ligar à D-004.
6. **Responsáveis com nome e cargo, mais quem confere e quem decide** (V1-31, V1-32). Quadro 13, conflito de interesse explícito e a fragilidade de só o CTO liberar versão.
7. **Cada indicador com valor de hoje, gatilho e decisão** (V1-18, V1-25, V1-30). Por exemplo, a cobertura contratual com revisão jurídica hoje é 0%, e o 31,8% já é gatilho pela C2.
8. **Rever a cesta de cinco** (V1-28, V1-29, V1-33). Juntar "drift" ao indicador 1, avaliar se a disponibilidade sai, considerar "incidentes detectados pela Lumis antes do cliente" ou "discordância do revisor por subgrupo" e ajustar a cadência para quinzenal (C2).
9. **Usar os dados que mudam a leitura** (V1-03, V1-05, V1-06, V1-07, V1-26). Sensibilidade e participação por subgrupo (39% da base acima da média), reclamações por paciente cerca de 8 vezes maiores em D/E, revisão de 2%, origem do número de campo `[não consta]` e o duplo papel do Vila Ipê.
10. **Marcadores, citações e texto humanizado** (V1-01, V1-02, V1-27, V1-40 a V1-46, V1-37). Corrigir "Capítulo 1" para Cap. 2, 2.3. Usar `[fonte]`, `[cálculo]`, `[hipótese]` e `[não consta]` com os estilos Tag. Tirar jargão, travessões, "não X, mas Y", tríades e palavras de IA. Alinhar o vocabulário com a F2-E1 v2. Cortar a seção 7.

Arquivos de referência:
- `C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/F2-E2_Auditoria_do_Ativo_v1.docx`
- `C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Dados_Quadros_7-11.md`
- `C:/Users/gusta/AppData/Local/Temp/claude/c--Users-gusta-Downloads-LumisOS/21178879-392f-48c9-b000-b7bcda3abb02/scratchpad/v1_audit.txt` (texto extraído da v1)

## Contas

# Contas de apoio da F2-E2: Auditoria do Ativo

Todas as contas usam só os dados do Anexo A transcritos em `C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Dados_Quadros_7-11.md`. Conferi o Quadro 12 e o Quadro 17 também no texto do Cap. 2. Nenhuma skill da Arkium cobre este tema, porque é um trabalho acadêmico. Nenhum arquivo foi criado ou alterado.

Como ler as marcações:
- **[fonte]**: valor tirado de um quadro.
- **[hipótese]**: premissa nossa, que não está no anexo.
- **[não consta]**: o dado não existe no anexo.
- Valores em p.p. são diferenças absolutas. Valores em % relativo comparam um número com o ponto de partida.

---

## Bloco A: base de dados e contratos (Quadro 7)

### CAL-01: de que é feita a base de 22,0 mi de registros?
- Clientes: 1,2 + 3,4 + 0,89 + 0,41 = 5,9 mi. Isso dá 5,9 ÷ 22,0 = **26,8%**.
- DATASUS: 14,0 ÷ 22,0 = **63,6%**.
- Sintéticos internos: 2,1 ÷ 22,0 = **9,5%**.
- Conferência: 5,9 + 14,0 + 2,1 = 22,0. [fonte: Cap. 2, Quadro 7]

**Para o conselho:** quase dois terços da base vêm de dado público, que qualquer concorrente também pode usar. Mais um décimo é dado gerado pela própria Lumis. Só pouco mais de um quarto vem de clientes.

### CAL-02: quanto pesa cada fonte de cliente?

| Fonte | Volume | % da base de clientes (÷5,9) | % da base total (÷22,0) |
|---|---|---|---|
| Rede Sanare | 3,4 mi | **57,6%** | 15,5% |
| Hospital Vila Ipê | 1,2 mi | 20,3% | 5,5% |
| Seguradora Prisma | 0,89 mi | 15,1% | 4,0% |
| Banco Meridiano | 0,41 mi | 6,9% | 1,9% |

Há uma observação sem conta: duas das quatro fontes de clientes não são prestadores de saúde. A Prisma entra com sinistros de seguro e o Meridiano com operações bancárias. O anexo não diz como esses dados entram no modelo de priorização clínica [não consta].

**Para o conselho:** mais da metade do dado de clientes vem de uma única rede (Sanare). Se esse cliente sair, a parte proprietária da base cai a menos da metade.

### CAL-03: qual o peso das fontes frágeis?
- Fontes frágeis: Vila Ipê, com cláusula genérica (1,2 mi), e Prisma, com contrato silente (0,89 mi). Juntas somam 2,09 mi.
- Na base de clientes: 2,09 ÷ 5,9 = **35,4%**.
- Na base total: 2,09 ÷ 22,0 = **9,5%**.

**Para o conselho:** pouco mais de um terço do dado proprietário não tem autorização clara para treinar o modelo. Nenhum dos seis instrumentos passou por revisão jurídica desde a assinatura [fonte: texto após o Quadro 7].

### CAL-04: em que grau de autorização está cada parte da base de clientes?

| Grau | Fontes | Volume | % clientes |
|---|---|---|---|
| Forte, com condição | Sanare (uso agregado e anonimizado) + Meridiano (auditoria anual) | 3,81 mi | **64,6%** |
| Genérica | Vila Ipê ("melhoria contínua do serviço") | 1,2 mi | **20,3%** |
| Silente | Prisma | 0,89 mi | **15,1%** |

**Para o conselho:** mesmo a parte "forte" depende de condições que precisam ser cumpridas e provadas. A Sanare exige uso agregado e anonimizado. O Meridiano exige auditoria anual. O anexo não diz se essas condições estão sendo cumpridas hoje [não consta].

### CAL-05: quais contratos vencem antes de 12/2027?
- **Seguradora Prisma: vence em 12/2026.** De hoje (06/10/2026) até lá são cerca de 2 meses.
- **Hospital Vila Ipê: vence em 03/2027.** São cerca de 5 meses. É também o cliente que mandou a notificação formal [fonte: Quadro 10, destaque; Quadro 14].
- Sanare (08/2028) e Meridiano (05/2028) vencem depois de 12/2027.
- As fontes que vencem antes de 12/2027 são as mesmas fontes frágeis: 2,09 mi, ou 35,4% da base de clientes.
- Se as duas saírem sem renovação que autorize o treinamento:
  - a base de clientes cai para 3,81 mi (−35,4%);
  - a base total cai para 19,91 mi (−9,5%);
  - a parte de clientes na base total cai de 26,8% para 3,81 ÷ 19,91 = **19,1%**.

**Para o conselho:** o risco jurídico e o risco de prazo caem sobre as mesmas fontes. A primeira vence em cerca de dois meses. Nenhuma das quatro fontes de clientes passa de 08/2028.

### CAL-06: quanto da base é dado proprietário com autorização sólida?
- 3,81 ÷ 22,0 = **17,3%** da base total.

**Para o conselho:** o memorando pede "qual parte disso constitui vantagem defensável" [fonte: Cap. 2, p. 5]. Pelo critério de dado proprietário com autorização expressa, o teto é de cerca de 17% da base. Essa leitura é nossa [hipótese] e o anexo não a apresenta.

---

## Bloco B: variáveis e pesos (Quadro 8)

O anexo não traz a definição técnica de "peso" [não consta]. Somar pesos é uma aproximação, e as variáveis podem estar correlacionadas entre si. Conferência: os dez pesos somam 100,0%.

### CAL-07: quanto do modelo depende de acesso ou de condição socioeconômica?

**Critério.** Uma variável conta como proxy de acesso quando o valor dela muda conforme o paciente consegue chegar ao serviço, pagar por ele ou ser atendido nele, e não apenas conforme o quadro clínico. É o mesmo raciocínio do capítulo: "histórico de gastos [...] mede quem teve mais acesso a atendimento" [fonte: Cap. 2, 2.2].

| Cenário | Variáveis incluídas | Soma |
|---|---|---|
| **Estrito (4 óbvias)** | #1 nº de atendimentos 18,4 + #2 custo acumulado 15,1 + #6 faixa de CEP 8,9 + #7 tipo de plano 7,4 | **49,8%** |
| **Amplo** | Estrito + #5 tempo entre consulta e exame 9,8 (depende da fila e da oferta local) + #9 faltas 5,3 (depende de transporte e trabalho) + #10 especialidade de origem 4,3 (a via de entrada depende de acesso) | **69,2%** |
| **Máximo** | Amplo + #4 comorbidades *registradas* 11,2 (só é registrado o que foi diagnosticado) | **80,4%** |

Os cenários amplo e máximo são classificação da equipe [hipótese]. A empresa descreve essas variáveis de outro modo [fonte: Quadro 8, coluna "O que a empresa diz que ela mede"].

### CAL-08: quanto do modelo é sinal clínico direto?
- No critério estrito, só o #8 painel de exames laboratoriais conta: **6,9%**. Mesmo ele depende de o exame ter sido feito.
- Somando o #4 comorbidades: 6,9 + 11,2 = **18,1%**.
- A idade (#3, 12,7%) é demográfica. Não é acesso nem sinal clínico direto.

**Para o conselho:** pelo critério mais conservador, metade do peso do modelo mede acesso e condição socioeconômica. Sinal clínico direto fica entre 7% e 18%. Isso ajuda a explicar por que o erro se concentra nos idosos de CEP D/E, que são justamente os pacientes com menos acesso.

---

## Bloco C: desempenho declarado contra o desempenho em campo (Quadros 9 e 10)

### CAL-09: quanto o desempenho cai da validação para o campo?

| Métrica | Validação 2023 | Campo 1º sem/2026 | Diferença (p.p.) | Variação relativa |
|---|---|---|---|---|
| Acurácia | 94,1% | 87,6% | **−6,5 p.p.** | 6,5 ÷ 94,1 = **−6,9%** |
| Sensibilidade | 92,6% | 82,3% | **−10,3 p.p.** | 10,3 ÷ 92,6 = **−11,1%** |
| Falso negativo | 7,4% | 17,7% | **+10,3 p.p.** | 10,3 ÷ 7,4 = **+139%** |
| Erro total (100 − acurácia) | 5,9% | 12,4% | +6,5 p.p. | **2,1 vezes** |

### CAL-10: quantas vezes o falso negativo aumentou?
- 17,7 ÷ 7,4 = **2,4 vezes**.

**Para o conselho:** a acurácia anunciada cai "só" 6,5 p.p. O erro que importa clinicamente, deixar de priorizar quem precisava, mais que dobrou. A acurácia esconde a piora.

### CAL-11: o falso negativo médio ponderado pelo Quadro 10 bate com o Quadro 9?
- Conta: 0,21×10,6 + 0,27×14,3 + 0,15×20,2 + 0,13×15,9 + 0,14×23,5 + 0,10×31,8
- Parcelas: 2,226 + 3,861 + 3,030 + 2,067 + 3,290 + 3,180 = **17,65%**. O Quadro 9 traz 17,7%, então é coerente.
- Na mesma conta, a sensibilidade ponderada dá 82,35% (Quadro 9: 82,3%) e a acurácia ponderada dá **87,2%** (Quadro 9: 87,6%). A diferença de 0,4 p.p. é compatível com o arredondamento das participações.
- Premissa: o falso negativo se calcula sobre os casos que deveriam ser priorizados. Ponderar pela participação na base só é exato se essa proporção for igual em todos os subgrupos [hipótese]. A coincidência com o Quadro 9 sugere que a aproximação é razoável.

### CAL-12: qual a distância entre o pior e o melhor subgrupo?
- Falso negativo: 31,8 ÷ 10,6 = **3,0 vezes**, ou +21,2 p.p.
- Sensibilidade: 89,4 ÷ 68,2 = **1,31 vez**, ou −21,2 p.p.
- Acurácia: 91,2 − 79,3 = −11,9 p.p.

**Para o conselho:** a média de 82,3% de sensibilidade esconde um subgrupo em que o sistema acerta 68 de cada 100 casos que deveriam ser priorizados.

### CAL-13: quanto pesa a idade e quanto pesa o CEP? (decomposição simples do falso negativo)

**Efeito da idade, com CEP fixo (60+ contra 18–59):**

| CEP | 18–59 | 60+ | Diferença | Razão |
|---|---|---|---|---|
| A/B | 10,6 | 15,9 | +5,3 p.p. | 1,50 vez |
| C | 14,3 | 23,5 | +9,2 p.p. | 1,64 vez |
| D/E | 20,2 | 31,8 | +11,6 p.p. | 1,57 vez |

Média simples: +8,7 p.p.

**Efeito do CEP, com idade fixa (D/E contra A/B):**

| Idade | CEP A/B | CEP D/E | Diferença | Razão |
|---|---|---|---|---|
| 18–59 | 10,6 | 20,2 | +9,6 p.p. | 1,91 vez |
| 60+ | 15,9 | 31,8 | +15,9 p.p. | 2,00 vezes |

Média simples: +12,75 p.p. O CEP C fica no meio: +3,7 p.p. entre 18–59 e +7,6 p.p. entre 60+.

**Interação.** Se os dois efeitos simplesmente se somassem, o subgrupo 60+ D/E teria 10,6 + 5,3 + 9,6 = 25,5%. O observado é 31,8%, ou seja, 6,3 p.p. a mais. Como multiplicação, a conta fica perto: 10,6 × 1,50 × 1,91 = 30,3%. Os dois efeitos se reforçam.

**Agregados** (ponderados pela participação, mesma premissa da CAL-11):

| Recorte | Falso negativo |
|---|---|
| 18–59 anos | 14,5% |
| 60+ | 23,1% |
| CEP A/B | 12,6% |
| CEP C | 17,4% |
| CEP D/E | 24,8% |

**Para o conselho:** o CEP pesa mais que a idade, e os dois juntos pioram o resultado além da soma dos dois. O problema é de acesso, como já mostrava a CAL-07, e não só de faixa etária.

### CAL-14: a amostra de validação representa o campo?
- 48.000 ÷ 1.940.000 = **2,5%** da amostra de campo. Dito de outro modo, o campo é 40,4 vezes maior.
- A validação usou dois hospitais da mesma região, em 2023. O anexo não traz a composição dela por idade e CEP [não consta].

**Para o conselho:** o número de vitrine vem de uma amostra 40 vezes menor que o uso real, de um único lugar, e com três anos de idade.

---

## Bloco D: o que esse erro representa em pacientes (Quadros 9, 10 e 12)

### CAL-15: quantos pacientes deixam de ser priorizados?

**Não dá para calcular com precisão.** Faltam três dados:
- a prevalência de casos que deveriam ser priorizados entre as 640.000 decisões por mês [não consta];
- o número de pacientes únicos, já que uma decisão não é um paciente e o mesmo paciente pode passar várias vezes [não consta];
- como a decisão se divide entre subgrupos dentro desse volume [não consta].

Há também uma divergência a sinalizar. O campo do 1º semestre de 2026 tem 1,94 mi de registros em 6 meses, cerca de 323 mil por mês. Isso é metade das 640 mil decisões por mês do Quadro 12. O anexo não explica a diferença [não consta]. Uma possibilidade é que a avaliação só tenha usado os casos com desfecho conhecido [hipótese].

**Estimativa ilustrativa [hipótese].** Conta: falsos negativos por mês = 640.000 × prevalência × 17,7%.

| Prevalência suposta | Casos a priorizar/mês | Falsos negativos/mês (17,7%) | Se fosse 7,4% (validação) | Excesso em relação à validação |
|---|---|---|---|---|
| 5% | 32.000 | ≈ 5.660 | ≈ 2.370 | ≈ 3.300 |
| 10% | 64.000 | ≈ 11.330 | ≈ 4.740 | ≈ 6.590 |
| 20% | 128.000 | ≈ 22.660 | ≈ 9.470 | ≈ 13.180 |

As prevalências de 5%, 10% e 20% são premissas nossas, só para dar ordem de grandeza. As contagens são de decisões, não de pessoas.

**Para o conselho:** em qualquer premissa razoável, são milhares de decisões por mês em que alguém que deveria ser priorizado não foi. Mais de um terço delas, cerca de 35% (CAL-17), cai na faixa D/E.

### CAL-16: quantas decisões por mês passam sem revisão humana?
- Revisadas: 640.000 × 2% = **12.800 por mês**.
- Sem revisão: 640.000 − 12.800 = **627.200 por mês** (98%), ou cerca de **7,5 mi por ano**.
- Na premissa de 10% da CAL-15: dos cerca de 11.330 falsos negativos por mês, por volta de 227 cairiam na amostra revisada. Por volta de 11.100 passariam sem nenhum olho humano [hipótese].
- O uso foi autorizado pela diretoria comercial do cliente, sem aprovação interna formal. A Lumis não tem comitê de ética nem de risco [fonte: Quadro 12 e texto, p. 26].

### CAL-17: quanto do erro total cai em cada recorte? [hipótese: mesma prevalência em todos os subgrupos]
- 60+ D/E: 3,18 ÷ 17,65 = **18,0% dos falsos negativos**, para 10% da base.
- CEP D/E inteiro: (3,03 + 3,18) ÷ 17,65 = **35,2% dos falsos negativos**, para 25% da base.

---

## Bloco E: reclamações por faixa de CEP (Quadro 17)

### CAL-18: a participação nas reclamações acompanha a participação na base?

| Faixa | Na base | Reclamações | % das reclamações | Razão (% reclamações ÷ % base) |
|---|---|---|---|---|
| A/B | 34% | 8 | 10,8% | 0,32 |
| C | 41% | 19 | 25,7% | 0,63 |
| D/E | 25% | 47 | **63,5%** (o capítulo arredonda para 64%) | **2,54** |
| Total | 100% | 74 | 100% | — |

### CAL-19: qual a taxa relativa de reclamação por faixa?
- D/E contra A/B: (47 ÷ 25) ÷ (8 ÷ 34) = 1,88 ÷ 0,235 = **8,0 vezes**.
- C contra A/B: (19 ÷ 41) ÷ (8 ÷ 34) = **2,0 vezes**.
- Para comparar: o falso negativo agregado de D/E contra A/B é 24,8 ÷ 12,6 = **2,0 vezes** (CAL-13).

Limites da comparação:
- O total é pequeno: 74 reclamações.
- Não sabemos quem reclamou (paciente, hospital ou médico) [não consta].
- Não há volume de reclamação por cliente [não consta].
- O registro nunca foi cruzado com o desempenho do modelo [fonte: Quadro 17, observação].

**Para o conselho:** a reclamação cresce bem mais que o erro medido, 8 vezes contra 2 vezes. Pode haver dano que o falso negativo não captura, ou um viés na forma de registrar as reclamações [hipótese]. Só cruzando as duas bases dá para saber.

---

## Bloco F: painel comercial (Quadro 11)

### CAL-20: qual a distância entre 94,1% e 87,6%?
- 94,1 − 87,6 = **6,5 p.p.**, ou −6,9% relativo.
- Em erro: de 5,9% para 12,4%, o que dobra (2,1 vezes).
- O painel mostra acurácia. O dado mais relevante para o paciente é a sensibilidade em campo (82,3%) e a do pior subgrupo (68,2%).

### CAL-21: qual a margem de erro de um NPS com n = 9?
- Cada respondente move o NPS em 100 ÷ 9 = **11,1 pontos**.
- **Inconsistência:** com 9 respostas, o NPS só pode assumir valores múltiplos de 11,1. Os mais próximos de 72 são 66,7 e 77,8. Nenhuma combinação de 9 respostas dá 72. O anexo não explica a diferença [não consta]. Pode ser arredondamento, ponderação ou outro n [hipótese].
- **Margem aproximada [hipótese]:**
  - Premissa: 80% promotores, 12% neutros e 8% detratores, o que dá NPS de cerca de 72.
  - Variância por resposta: (0,80 + 0,08) − 0,72² = 0,362, logo desvio-padrão de 0,60.
  - Erro-padrão: 0,60 ÷ √9 = 0,20, ou 20 pontos.
  - IC 95%: ±1,96 × 20 ≈ **±39 pontos**, ou seja, de cerca de 33 a 100.
  - Com outro mix (por exemplo, 7 promotores, 2 neutros e nenhum detrator), a margem fica em ±27.
  - Com n = 9, a aproximação normal já é frágil.
- A margem estatística não cobre o viés de seleção: os 9 respondentes foram indicados pelo time comercial.

**Para o conselho:** o número não se sustenta numa auditoria. Nenhuma combinação de respostas reproduz 72, a margem passa de ±25 pontos e a amostra foi escolhida a dedo.

### CAL-22: o que significa 99,92% de disponibilidade?
- Indisponível: 0,08% × 8.760 h = **7,0 h por ano**, cerca de **35 min por mês**. O "99,9%" divulgado admitiria 8,76 h por ano.
- O número mede só a interface de programação (API), não o serviço de ponta a ponta [fonte: Quadro 11].
- Exemplo [hipótese]: se a integração com o hospital e a carga de dados tiverem 99,5% cada, a cadeia fica em 0,9992 × 0,995 × 0,995 ≈ 98,9%, cerca de **95 h por ano** de serviço indisponível.
- Disponibilidade também não diz nada sobre a qualidade da resposta. Em 03/2025, o modelo descartou exames de um laboratório recém-credenciado por 22 dias, e quem detectou foi o cliente. A API seguia "no ar" [fonte: Quadro 14].

### CAL-23: o que dá e o que não dá para calcular nas outras afirmações do painel?
- **"Mais de 5 milhões de vidas":** é a soma de registros processados, com reprocessamentos do mesmo paciente incluídos. O número de vidas únicas é **informação indisponível**. A duplicidade foi corrigida no sistema em 01/2026, mas não no material comercial [fonte: Quadro 14].
- **"Redução de 30% no tempo de triagem":** foi um piloto de 6 semanas em um hospital, sem grupo de controle. Não dá para separar o efeito do sistema de outros fatores. Nenhuma conta é possível com o anexo, e a margem também é **informação indisponível**.

---

## Dados que faltam e que a V2 deve declarar como [não consta]
- Prevalência de casos a priorizar.
- Pacientes únicos por mês.
- Volume de decisões por subgrupo.
- Definição técnica de "peso".
- Composição da amostra de validação por idade e CEP.
- Explicação para o campo de 1,94 mi no semestre (cerca de 323 mil por mês) contra as 640 mil decisões por mês.
- Volume de reclamações por cliente e quem reclamou.
- Cumprimento das condições dos contratos da Sanare e do Meridiano.
- Uso dos dados da Prisma e do Meridiano no modelo de priorização clínica.
- Os outros 34 dos 38 contratos.
- Como o NPS 72 foi calculado com 9 respondentes.

## Verificação independente das contas

# Verificação independente das contas da F2-E2

Nenhuma skill da Arkium cobre este tema, porque é um trabalho acadêmico da FIAP. Não criei nem alterei nenhum arquivo. Refiz todas as contas a partir de `C:/Users/gusta/Downloads/LumisOS/02_Fase2_O_Mercado/F2-E2_Auditoria_do_Ativo/Dados_Quadros_7-11.md`, que é uma transcrição do Anexo A. Não abri o PDF original. Por isso, se houver erro na transcrição, ele passa para estas contas.

## Veredito por conta

| CAL | Veredito | Observação |
|---|---|---|
| 01 | confere | 26,8%, 63,6% e 9,5%. A soma dá 22,0. |
| 02 | confere | 57,6 / 20,3 / 15,1 / 6,9 e 15,5 / 5,5 / 4,0 / 1,9. Sem a Sanare, sobram 2,5 mi, ou 42,4% da base de clientes, que é menos da metade. |
| 03 | confere | 35,4% e 9,5%. |
| 04 | confere | 3,81 ÷ 5,9 = 64,6%. |
| 05 | corrigir prazos + premissa_fragil | O anexo dá só mês e ano. De 06/10/2026 até 12/2026 vão **2 a 3 meses**. Até 03/2027 vão **5 a 6 meses**. Os volumes conferem: 19,91 mi, −9,5% e 3,81 ÷ 19,91 = 19,1%. Mas o anexo não diz se o fim do contrato obriga a tirar os registros históricos da base de treino [não consta]. O cenário "a base cai para 19,91 mi" é [hipótese]. |
| 06 | confere + premissa_fragil | 17,3% está certo. Dois cuidados: (a) o Meridiano é dado bancário, e o anexo não diz que ele sirva ao modelo clínico [não consta]; (b) a Sanare autoriza só uso agregado e anonimizado. "Teto de cerca de 17%" é leitura nossa e deve continuar marcado como [hipótese]. |
| 07 | confere + premissa_fragil | 49,8%, 69,2% e 80,4% estão certos. Os dez pesos somam 100,0%. Fragilidades: (a) até o cenário estrito é classificação da equipe. O capítulo só aponta explicitamente o caso do "histórico de gastos", que corresponde ao #2 e, por extensão, ao #1. Por isso o estrito também deve levar [hipótese]. (b) O quadro chama esses pesos de "dez maiores", mas eles somam 100%. Ou o modelo tem só dez variáveis, ou os pesos foram normalizados [não consta]. |
| 08 | confere + premissa_fragil | 6,9% e 18,1% estão certos. A #4 entra como acesso no cenário "máximo" da CAL-07 e como sinal clínico aqui, então os dois intervalos se sobrepõem. É preciso dizer isso no texto. A frase "isso ajuda a explicar por que o erro se concentra..." afirma uma causa e deve levar [hipótese]. |
| 09 | confere | −6,5 p.p. (−6,9%), −10,3 p.p. (−11,1%), +10,3 p.p. (+139%) e 2,1 vezes. |
| 10 | confere | 17,7 ÷ 7,4 = 2,39, ou 2,4 vezes. |
| 11 | **corrigir** | O FN ponderado (17,65%), a sensibilidade ponderada (82,35%) e a acurácia ponderada (87,17%) conferem. **O erro está na explicação da diferença de 0,4 p.p. na acurácia.** Explico abaixo. |
| 12 | confere | 3,0 vezes e +21,2 p.p.; 1,31 vez; −11,9 p.p. |
| 13 | confere + premissa_fragil | Todos os números conferem: 5,3/9,2/11,6, média 8,7; 9,6/15,9, média 12,75; 3,7/7,6; aditivo 25,5 (+6,3); multiplicativo 30,3; agregados 14,5 / 23,1 / 12,6 / 17,4 / 24,8. O problema é a comparação. O "efeito idade" junta as três faixas de CEP, e o "efeito CEP" usa só o extremo D/E contra A/B. CEP C contra A/B dá +3,7 e +7,6 p.p., menos que o efeito da idade nas mesmas faixas (+5,3 e +9,2). Correção do texto: "o extremo D/E pesa mais que a idade". Não vale dizer "o CEP pesa mais" de forma genérica. |
| 14 | confere + ajuste de texto | 2,5% e 40,4 vezes estão certos. "De um único lugar" está errado. O anexo diz "dois hospitais da mesma região", então o certo é "de uma única região". |
| 15 | confere | 32.000 / 5.664 / 2.368 / 3.296; 64.000 / 11.328 / 4.736 / 6.592; 128.000 / 22.656 / 9.472 / 13.184. 1,94 mi ÷ 6 = 323 mil, ou 50,5% de 640 mil. As premissas já estão marcadas. |
| 16 | confere | 12.800; 627.200; 7,53 mi por ano; 227 e cerca de 11.100. Supõe que a amostra de 2% é aleatória [hipótese] e que todo erro dentro da amostra revisada seria detectado [hipótese]. Essas duas premissas precisam estar escritas. |
| 17 | confere | 3,18 ÷ 17,654 = 18,0%; 6,21 ÷ 17,654 = 35,2%. |
| 18 | confere | 10,8 / 25,7 / 63,5%; razões 0,32 / 0,63 / 2,54. Quadro 10 por CEP: 21+13 = 34, 27+14 = 41, 15+10 = 25. Bate com o Quadro 17. |
| 19 | confere + premissa_fragil | 8,0 vezes, 1,97 vez (≈2,0) e 24,84 ÷ 12,63 = 1,97 (≈2,0). O "8 contra 2" compara coisas diferentes. A taxa de reclamação é por paciente. O FN é por caso que deveria ser priorizado. Se D/E tiver mais casos graves, o número de FN por paciente cresce mais que 2 vezes, mesmo com o mesmo FN. Também não se sabe se o período dos 25% (pacientes processados) é o mesmo dos 12 meses de reclamações [não consta]. As duas ressalvas entram nos limites. |
| 20 | confere | 6,5 p.p.; −6,9%; de 5,9% para 12,4%, 2,1 vezes. |
| 21 | confere | O passo é de 11,1 pontos. 72 não é alcançável: os vizinhos são 66,7 e 77,8. Variância 0,3616, desvio-padrão 0,601, EP de 20 pontos, IC ±39 (33 a 100, com teto em 100). Para o mix 7/2/0: variância 0,173, EP 13,9, IC ±27. "Escolhida a dedo" carrega juízo. Prefiro a redação do anexo: "indicados pelo time comercial". |
| 22 | corrigir (pequeno) | 7,0 h por ano, 35 min por mês e 8,76 h estão certos. Na cadeia, 0,9992 × 0,995 × 0,995 = 0,98923. A indisponibilidade dá 1,077% × 8.760 = **cerca de 94 h por ano**, não 95. |
| 23 | confere | O valor divulgado é 5,2 mi de registros [fonte: Quadro 11]. |

## Detalhe da CAL-11

O texto diz que a diferença de 0,4 p.p. "é compatível com o arredondamento das participações". **Não é.**

A acurácia é medida sobre todos os casos. Então ponderar pela participação na base é a conta exata para ela, e a hipótese de prevalência não entra aqui. O que pode variar é o arredondamento: cada participação tem uma margem de ±0,5 p.p., e a soma precisa dar 100. No caso extremo, os três subgrupos de maior acurácia ganham +0,5 cada e os três de menor perdem 0,5 cada. A acurácia muda 0,005 × (268,8 − 248,6) = **+0,10 p.p. no máximo**. O resultado chega a no máximo 87,27%, longe de 87,6%.

Texto corrigido: "A acurácia ponderada dá 87,2%, contra 87,6% no Quadro 9. O arredondamento das participações explica no máximo 0,1 p.p. O resto não tem explicação no anexo [não consta]." Esse item deve entrar na lista de dados que faltam.

A coincidência do FN (17,65 contra 17,7) continua válida, com a premissa de prevalência igual em todos os subgrupos [hipótese].

## Números apresentados como dados da Lumis que não estão no anexo

Nenhum número inventado. Alguns pontos de redação dão a uma inferência o ar de dado:
- CAL-05: "cerca de 2 meses" e "cerca de 5 meses" são contas nossas, imprecisas porque o anexo dá só mês e ano. Usar "2 a 3" e "5 a 6".
- CAL-05: a base "cai para 19,91 mi". O anexo não diz que os dados saem da base quando o contrato termina.
- CAL-08: "pacientes com menos acesso" para D/E é inferência e leva [hipótese].
- CAL-14: "um único lugar" deve ser "uma única região".
- CAL-21: "escolhida a dedo" deve ser "indicados pelo time comercial".

---

## Lista de contas corrigida, pronta para uso

**Bloco A, Quadro 7**
- **CAL-01.** Clientes 5,9 mi = 26,8%; DATASUS 14,0 mi = 63,6%; sintéticos 2,1 mi = 9,5%. Total 22,0 mi [fonte: Cap. 2, Quadro 7].
- **CAL-02.** Base de clientes / base total: Sanare 57,6% / 15,5%; Vila Ipê 20,3% / 5,5%; Prisma 15,1% / 4,0%; Meridiano 6,9% / 1,9%. Sem a Sanare, restam 2,5 mi (42,4% da base de clientes). O uso de sinistros (Prisma) e de operações bancárias (Meridiano) no modelo clínico não consta no anexo [não consta].
- **CAL-03.** Fontes frágeis (Vila Ipê + Prisma) = 2,09 mi: 35,4% da base de clientes e 9,5% da base total. Nenhum dos seis instrumentos passou por revisão jurídica [fonte: texto após o Quadro 7].
- **CAL-04.** Forte com condição 3,81 mi (64,6%); genérica 1,2 mi (20,3%); silente 0,89 mi (15,1%). O cumprimento das condições hoje não consta no anexo [não consta].
- **CAL-05.** Prisma vence em 12/2026, daqui a 2 a 3 meses. Vila Ipê vence em 03/2027, daqui a 5 a 6 meses, e é o cliente da notificação formal [fonte: Quadro 10, destaque; Quadro 14]. São as mesmas fontes frágeis: 2,09 mi, 35,4% dos clientes. Se for preciso retirar esses dados ao fim do contrato [hipótese], a base de clientes cai para 3,81 mi e a total para 19,91 mi (−9,5%). A participação de clientes na base total vai a 19,1%. Nenhuma fonte de cliente vence depois de 08/2028.
- **CAL-06.** Dado de cliente com autorização expressa: 3,81 ÷ 22,0 = 17,3% da base total. Ler isso como teto da vantagem defensável é escolha nossa [hipótese]. O Meridiano exige auditoria anual, e a pertinência de dado bancário ao modelo clínico não consta no anexo [não consta].

**Bloco B, Quadro 8** (definição de "peso" [não consta]; os dez "maiores" somam 100,0%, então ou o modelo tem só dez variáveis, ou os pesos foram normalizados [não consta]; somar pesos é uma aproximação)
- **CAL-07.** Peso atribuído a proxy de acesso ou condição socioeconômica, conforme a classificação da equipe [hipótese]: estrito (#1, #2, #6, #7) 49,8%; amplo (+ #5, #9, #10) 69,2%; máximo (+ #4) 80,4%. Só o #2 corresponde diretamente ao exemplo do capítulo [fonte: Cap. 2, 2.2].
- **CAL-08.** Sinal clínico direto: #8 = 6,9%; com o #4, 18,1%. Idade (#3) = 12,7%, demográfica. O #4 aparece nos dois lados, no cenário máximo da CAL-07 e aqui. Os intervalos se sobrepõem.

**Bloco C, Quadros 9 e 10**
- **CAL-09.** Da validação para o campo: acurácia −6,5 p.p. (−6,9%); sensibilidade −10,3 p.p. (−11,1%); falso negativo +10,3 p.p. (+139%); erro total de 5,9% para 12,4% (2,1 vezes).
- **CAL-10.** Falso negativo: 17,7 ÷ 7,4 = 2,4 vezes.
- **CAL-11.** Ponderado pela participação: FN 17,65% (Quadro 9: 17,7%), sensibilidade 82,35% (82,3%), acurácia 87,2% (87,6%). Para o FN, a conta supõe prevalência igual em todos os subgrupos [hipótese]. Na acurácia, o arredondamento das participações explica no máximo 0,1 p.p. O resto da diferença de 0,4 p.p. não tem explicação no anexo [não consta].
- **CAL-12.** Pior contra melhor subgrupo: FN 3,0 vezes (+21,2 p.p.); sensibilidade 89,4 contra 68,2 (−21,2 p.p., 1,31 vez); acurácia −11,9 p.p.
- **CAL-13.** Idade, com CEP fixo: +5,3 / +9,2 / +11,6 p.p. (A/B, C, D/E), média +8,7. CEP D/E contra A/B, com idade fixa: +9,6 / +15,9 p.p., média +12,75. CEP C contra A/B: +3,7 / +7,6. Juntos, os dois efeitos pioram o resultado além da soma: aditivo 25,5% contra 31,8% observado (+6,3 p.p.); multiplicativo cerca de 30,3%. Agregados [hipótese de prevalência igual]: 18–59 14,5%; 60+ 23,1%; A/B 12,6%; C 17,4%; D/E 24,8%. Leitura: **o extremo D/E** pesa mais que a idade. CEP C contra A/B pesa menos que a idade.
- **CAL-14.** A validação é 2,5% do campo (o campo é 40,4 vezes maior). Vem de dois hospitais de uma única região, em 2023. Composição por idade e CEP [não consta].

**Bloco D, Quadros 9, 10 e 12**
- **CAL-15.** Prevalência, pacientes únicos e decisões por subgrupo [não consta]. O campo tem cerca de 323 mil registros por mês, contra 640 mil decisões por mês. A diferença não tem explicação no anexo [não consta]. FN por mês = 640.000 × prevalência × 17,7% [hipótese de prevalência]:
  - 5%: cerca de 5.660 (com o FN da validação, cerca de 2.370; excesso de cerca de 3.300);
  - 10%: cerca de 11.330 (4.740; excesso de 6.590);
  - 20%: cerca de 22.660 (9.470; excesso de 13.180).
  São decisões, não pessoas.
- **CAL-16.** Revisadas: 12.800 por mês. Sem revisão: 627.200 por mês (98%), cerca de 7,5 mi por ano. Com prevalência de 10%, supondo amostra aleatória e detecção total na revisão [hipótese], cerca de 227 FN por mês seriam revisados e cerca de 11.100 não. Uso autorizado pela diretoria comercial do cliente, sem aprovação interna formal; não há comitê de ética nem de risco [fonte: Quadro 12 e texto, p. 26].
- **CAL-17.** [hipótese: prevalência igual] 60+ D/E concentra 18,0% dos FN com 10% da base. CEP D/E concentra 35,2% dos FN com 25% da base.

**Bloco E, Quadro 17**
- **CAL-18.** Reclamações: A/B 10,8% (razão 0,32), C 25,7% (0,63), D/E 63,5% (2,54). O capítulo arredonda para 64%.
- **CAL-19.** Taxa relativa de reclamação: D/E contra A/B 8,0 vezes; C contra A/B 2,0 vezes. FN agregado D/E contra A/B: 2,0 vezes. Limites:
  - n = 74;
  - quem reclamou e o volume por cliente [não consta];
  - as bases nunca foram cruzadas [fonte: Quadro 17];
  - a reclamação é por paciente e o FN é por caso a priorizar, então diferenças de prevalência entre faixas mudam a comparação [hipótese];
  - o período da distribuição por CEP pode não coincidir com os 12 meses de reclamações [não consta].

**Bloco F, Quadro 11**
- **CAL-20.** 94,1 − 87,6 = 6,5 p.p. (−6,9%). O erro sobe de 5,9% para 12,4% (2,1 vezes). A sensibilidade em campo é 82,3%, e no pior subgrupo 68,2%.
- **CAL-21.** Com n = 9, cada resposta move o NPS em 11,1 pontos. 72 não é alcançável: os valores possíveis mais próximos são 66,7 e 77,8 [não consta como foi calculado]. A margem aproximada [hipótese de mix] fica entre ±27 e ±39 pontos, e a aproximação normal é frágil com n = 9. Os respondentes foram indicados pelo time comercial [fonte: Quadro 11].
- **CAL-22.** 99,92% significa 7,0 h por ano (cerca de 35 min por mês) de indisponibilidade. O "99,9%" divulgado admitiria 8,76 h. O número vale só para a API [fonte: Quadro 11]. Exemplo [hipótese]: com integração e carga de dados a 99,5% cada, a cadeia fica em cerca de 98,9%, ou cerca de **94 h por ano**. O incidente de 03/2025 (22 dias, detectado pelo cliente) aconteceu com a API no ar [fonte: Quadro 14].
- **CAL-23.** "Mais de 5 milhões de vidas" corresponde a 5,2 mi de registros, com reprocessamentos. O número de vidas únicas é informação indisponível. A duplicidade foi corrigida no sistema e não no material comercial [fonte: Quadro 14]. "−30% no tempo de triagem" (30,4%) vem de um piloto de 6 semanas, em um hospital, sem grupo de controle. Não há conta possível e a margem é informação indisponível.

**Acrescentar à lista de dados que faltam:**
- explicação para a acurácia de 87,6% no Quadro 9 contra 87,2% ponderada pelo Quadro 10;
- se o fim do contrato obriga a retirar os dados da base de treinamento;
- o período de referência da distribuição de pacientes por CEP no Quadro 17.
