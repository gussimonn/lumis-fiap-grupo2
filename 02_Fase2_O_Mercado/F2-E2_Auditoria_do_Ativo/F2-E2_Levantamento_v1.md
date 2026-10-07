# F2-E2 · Levantamento para a v2

06/10/2026 · Base: v1 do colega (`F2-E2_Auditoria_do_Ativo_v1.docx`) · Método: lemos o enunciado e o Anexo A do Cap. 2 e auditamos a v1. Refizemos as contas com uma segunda verificação independente e fizemos pesquisa externa em seis frentes. Só entram os achados confirmados ou corrigidos. Depois, uma crítica cruzada (professor, analista do Vetor Capital e conselheiro) revisou este levantamento, e os pontos dela já estão incorporados. Nenhuma skill da Arkium cobre este trabalho, porque ele é acadêmico e trata de empresa fictícia.

Como ler as marcações: `[fonte: ...]` é dado do caso, `[conta]` é cálculo da equipe sobre um quadro, `[hipótese]` é leitura nossa sem quadro que a sustente e `[não consta]` é dado que o anexo não traz. `[não verificado]` marca fonte externa que só conferimos em parte. Ela não vai para o corpo e não sustenta recomendação. O contexto externo leva o ID do achado (PRX, LEG, MET, IND, CON ou DIL), e a referência completa está na seção 7.

## 0. O que muda da v1 para a v2

- **Abertura.** A v2 abre com a tese e com o que pedimos ao conselho. Hoje a v1 abre falando de si mesma e deixa a conclusão para o fim da seção 1.
- **Base legal.** Entra uma subseção curta sobre a LGPD. Ela trata dado de saúde como dado sensível, o papel de controlador e de operador e a política de privacidade que ainda não foi aprovada. A v1 trata só do contrato.
- **Quatro perguntas nos descartes.** As cinco métricas do painel comercial e os candidatos que a equipe descartar passam pelas quatro perguntas. É a lacuna mais clara frente ao enunciado.
- **Caso de proxy.** O caso principal passa a ser custo acumulado e número de atendimentos, que é o exemplo do próprio capítulo (2.2). O CEP fica como reforço. O mecanismo é citado como fato do caso, porque o capítulo o afirma.
- **Dados que mudam a leitura.** Entram o incidente de 01/2026 (duplicidade corrigida no sistema e mantida no material comercial), as reclamações por CEP, a revisão humana de 2%, a sensibilidade e a participação de cada subgrupo, o duplo papel do Vila Ipê e o tamanho financeiro do risco (Quadro 3).
- **Indicadores.** Cada indicador ganha valor de hoje, decisão, limite marcado como `[hipótese]`, cargo do Quadro 13 e alguém de fora que confere. A leitura é quinzenal, como manda o C2, sobre uma janela que tenha casos suficientes para separar sinal de ruído. "Drift" se junta ao indicador de falso negativo e "disponibilidade" sai da cesta.
- **C2.** A v2 toma posição: mantém o compromisso e recomenda restringir já a recomendação automática nos dois recortes que passam do limite, com o custo dito.
- **Marcadores e citações.** As quatro perguntas passam a ser citadas no Cap. 2, 2.3 (a v1 diz Capítulo 1), cada quadro aparece numerado na legenda e fato, conta, hipótese e lacuna ficam separados.
- **Forma.** O texto segue o padrão da F2-E1 v2: relatório ao conselho, tabelas curtas, uma figura, sem jargão e sem travessão. Sai a seção 7 "Decisões recomendadas", que repete o resto.

## 1. Entendendo a entrega

### 1.1 O que é esta entrega

A F2-E2 audita o único ativo que a Lumis diz ter, a base de dados, e os números que ela usa para se vender. O enunciado resume assim: "O fundo quer saber de que é feito o ativo da Lumis. Você precisa responder com precisão, inclusive quando a resposta for desconfortável" [fonte: Cap. 2, seção 4, p. 15].

A resposta vem em quatro camadas:
- de onde vêm os dados e se a Lumis tem direito de usá-los;
- o que as variáveis medem de fato;
- se os números de vitrine aguentam uma auditoria;
- que números a gestão deveria acompanhar no lugar deles.

**Lugar no dossiê.** A fase pede "um documento único, com identificação da equipe, reunindo as cinco entregas articuladas entre si", mais um memorando ao conselho de no máximo duas páginas [fonte: Cap. 2, 4.2]. A F2-E2 responde aos itens 2 ("Fundamento do ativo") e 3 ("Evidência, não narrativa") do memorando do Vetor Capital [fonte: Cap. 2, p. 5].

**O que a F2-E1 v2 já prometeu e esta entrega precisa cumprir:**
- a tese de que "o único ativo que poderia ser da Lumis, a base de dados, ainda não é dela";
- as frases "A auditoria completa fica para a Entrega 2" e "A Entrega 2 detalha contratos e métricas";
- a composição da base: 63,6% pública, 9,5% sintética e 26,8% de clientes;
- as quatro travas dos dados de clientes: autorização, concentração, escala e viés;
- a recomendação "Trocar os 94% por validação em campo, por subgrupo e publicada";
- o fosso possível (D-009): "dado de desfecho com direito de uso limpo e validação auditável por subgrupo".

**O que ela passa adiante:**
- **F2-E3.** Cada indicador precisa terminar num cargo [fonte: Cap. 2, p. 16]. A E2 decide o que fazer quando um limite é ultrapassado. A E3 recebe o desenho de quem executa e com que poder. Hoje colocar uma versão em produção é decisão exclusiva do CTO, e a revisão humana cobre 2% das 640 mil decisões por mês [fonte: Cap. 2, Quadro 12 e p. 26].
- **F2-E5.** A E5 pede "desempenho por subgrupo" e "situação contratual dos dados" [fonte: Cap. 2, p. 17]. A métrica pública de impacto da E5 deve sair de um dos cinco indicadores desta entrega, para o dossiê não ganhar um número novo e solto.
- **Memorando.** A E2 entrega as condições prévias do aporte: regularizar os contratos, aposentar as métricas que não se sustentam e medir por subgrupo.

### 1.2 O objetivo

A pergunta que a entrega responde: que parte do ativo da Lumis passa numa auditoria independente, e o que precisa mudar para que o resto também passe?

Checklist do enunciado [fonte: Cap. 2, seção 4, p. 15]:

- [ ] Origem, base contratual e base legal dos dados, com os pontos frágeis identificados.
- [ ] Análise das principais variáveis: o que cada uma pretende medir, o que mede de fato e que distorção pode introduzir.
- [ ] Ao menos um caso de variável proxy tratado de forma explícita.
- [ ] Revisão crítica das métricas apresentadas ao mercado: como foram apuradas, o que autorizam concluir e o que não autorizam.
- [ ] No máximo cinco indicadores de gestão, cada um ligado a uma decisão concreta que ele muda.
- [ ] Abertura por subgrupo em cada indicador, quando se aplica.
- [ ] As quatro perguntas (Medida em quê? Por quem? Muda alguma decisão? Esconde qual distribuição?) aplicadas a cada indicador proposto ou descartado [fonte: Cap. 2, 2.3, p. 9].
- [ ] Nenhum número inventado sobre a Lumis. O que não está no anexo é tratado como informação indisponível, e isso é dito no texto [fonte: Cap. 2, seção 4, p. 14].
- [ ] Resposta ao item 2 do memorando: "qual parte disso constitui vantagem defensável" [fonte: Cap. 2, p. 5].

**O que vai ser avaliado** [fonte: Cap. 2, 4.1 e 4.3]:
- Honestidade analítica: "registrar as fragilidades encontradas no ativo da Lumis em vez de contorná-las". Isso vale nos dois sentidos. O que o caso afirma não pode virar hipótese, e o que é leitura nossa não pode virar fato.
- Rigor sobre dados e métricas: o que as variáveis representam e a diferença entre número apresentável e número útil.
- Integração e defesa: coerência com as outras entregas e com o memorando.
- As disciplinas ligadas: leitura crítica de variáveis e análise de proxies (Computational Thinking & AI for Leaders) e a diferença entre métrica de vaidade e métrica de decisão (Data-Driven Business & Analytics).
- Os conceitos do capítulo que o leitor espera ver aplicados: dado como testemunho e variável como proxy (2.2), métricas de vaidade e lei de Goodhart (2.3).

### 1.3 O que precisamos comunicar

**M1. A base parece grande, mas a parte que só a Lumis tem é pequena e tem autorização frágil.** São 22,0 mi de registros, e a parte exclusiva são os 5,9 mi de clientes (26,8%). Desses, 35,4% (2,09 mi, Vila Ipê e Prisma) vêm de contratos com cláusula genérica ou silentes, e nenhum dos seis instrumentos passou por revisão jurídica [fonte: Cap. 2, Quadro 7]. O DATASUS (63,6%) tem autorização, só não é exclusivo. A Prisma vence em 12/2026, daqui a 2 ou 3 meses [conta]. O modelo já foi treinado com esses dados, então o risco existe hoje (D-020).

Tamanho do risco [fonte: Cap. 2, Quadro 3]: ARR de R$ 41,2 mi e ticket médio de R$ 1,084 mi. Se Vila Ipê e Prisma pagam perto do ticket médio [hipótese], os dois contratos valem cerca de R$ 2,2 mi por ano, uns 5% do ARR [conta]. Uma multa simples da LGPD chega a 2% do faturamento por infração (art. 52, II). Com faturamento perto do ARR [hipótese], isso dá cerca de R$ 0,8 mi por infração [conta]. O custo maior provavelmente está em retirar dados e retreinar o modelo [hipótese], e esse custo [não consta].

**M2. O modelo mede acesso a atendimento e chama isso de gravidade.** Isso é fato do caso, e não leitura nossa. O capítulo diz, sobre usar gasto como indicador de gravidade: "Foi exatamente isso que aconteceu no incidente da Fase 1. [...] Houve uma escolha de representação" [fonte: Cap. 2, 2.2, p. 8]. E o desempenho em campo "cai mais em exatamente os grupos que geraram a reclamação" [fonte: Cap. 2, 1.2, p. 6]. Os dois maiores pesos são número de atendimentos (18,4%) e custo acumulado (15,1%) [fonte: Cap. 2, Quadro 8].

A parte que é nossa e fica como `[hipótese]`: quais variáveis carregam o acesso e quanto pesam. Pelo nosso critério (variáveis que registram uso passado de serviços ou renda: atendimentos, custo, CEP e tipo de plano), são 49,8% do peso [conta] [hipótese: critério da equipe]. O efeito do CEP está bem sustentado pelo Quadro 10. O efeito da idade tem duas explicações possíveis, e o anexo não permite separá-las: o rótulo do treino reflete uso passado, ou há poucos idosos na base de treino.

**M3. Os 94% descrevem 48 mil registros de 2023. Em campo, o erro que importa mais que dobra e se concentra em quem já é mais vulnerável.** O falso negativo vai de 7,4% na validação para 17,7% em campo [fonte: Cap. 2, Quadro 9]. Entre os pacientes de 60 anos ou mais de CEP D/E que precisavam de prioridade, 31,8% foram classificados como baixa prioridade, três vezes a taxa do melhor subgrupo [fonte: Cap. 2, Quadro 10]. Quem apurou o 31,8% foi o Hospital Vila Ipê, e não a Lumis [fonte: Cap. 2, destaque após o Quadro 10].

**M4. Nenhuma das cinco afirmações públicas passa numa auditoria independente do jeito que é divulgada.** Pela regra do fundo, hoje elas são passivo. O problema está na forma de divulgar, e não necessariamente no número. O 94,1% e o 99,92% podem ser reproduzidos dentro do escopo em que foram medidos. Como diz o capítulo, "O número nunca foi mentira" [fonte: Cap. 2, p. 6]. A exceção é "mais de 5 milhões de vidas", que está sabidamente inflada desde 01/2026 e continua no material comercial [fonte: Cap. 2, Quadros 11 e 14].

**M5. A Lumis troca números de vitrine por cinco indicadores, cada um com dono, limite e decisão. Isso é condição prévia do aporte e também o caminho para o fosso.** Validação auditável por subgrupo e direito de uso limpo são o que pode tornar a base difícil de copiar [fonte: F2-E1 v2; D-009].

### 1.4 O que o conselho quer ver

**Perguntas que o conselheiro e o analista do Vetor Capital vão fazer:**
1. "Se um cliente ou a ANPD questionar amanhã, quanto da base teríamos de retirar? O modelo continua de pé sem esses dados?" (item 2: base legal)
2. "Quanto disso é nosso de verdade? DATASUS qualquer concorrente tem." (item 2: vantagem defensável)
3. "Como vocês têm dados de 2019 se a empresa foi fundada em 2022?" (due diligence; ver a nota de divergência em 3.1)
4. "Que número da apresentação eu posso repetir ao meu comitê sem ser desmentido?" (item 3)
5. "Quem mediu o 31,8%? Vocês sabiam antes do hospital?" (Medida por quem?)
6. "No dia em que o falso negativo de um subgrupo passar do limite, quem desliga, em quanto tempo e quanto custa para o hospital?" (ponte com a F2-E3 e com o C2)
7. "Isso se repete quando a Lumis entrar em outro setor ou país?" [fonte: Cap. 2, 2.6, "replicação de um problema em escala maior"]

O guia de IA para conselheiros feito com o IBGC traz a mesma lista do outro lado da mesa: inventário dos sistemas e dos riscos de cada um, monitoramento dos princípios de IA responsável e supervisão adequada dos riscos (CON-04). Investidores americanos citam viés e dano reputacional entre os riscos materiais de IA (CON-06).

**O que deixa o conselho seguro:**
- números ruins mostrados pela própria Lumis, com fonte e sem eufemismo;
- uma separação clara entre o que é ativo, o que é passivo e o que é condição para virar ativo;
- prazos concretos: Prisma antes de 12/2026 e Vila Ipê antes de 03/2027;
- indicadores com cargo responsável, alguém de fora que confere, periodicidade, limite e a ação que o limite dispara;
- o custo de cada decisão pedida, em reais ou em decisões por mês;
- fato, conta, hipótese e lacuna marcados, para que o próprio documento possa ser auditado.

**O que faz o conselho desconfiar:**
- 94%, "5 milhões de vidas" ou NPS 72 repetidos em qualquer parte do dossiê sem ressalva;
- média sem abertura por subgrupo;
- hipótese apresentada como fato, ou fato do caso rebaixado a hipótese;
- mais de cinco indicadores, ou indicador sem decisão associada;
- uma regra de suspensão que o próprio documento já mostra estar ultrapassada, sem dizer o que se faz hoje;
- proxy tratado como detalhe técnico, quando o capítulo diz que "Era uma decisão de gestão. Sempre foi." [fonte: Cap. 2, 2.2].

### 1.5 Como comunicar ao conselho

**Estrutura.** A pirâmide de Minto organiza a abertura (CON-09):
- situação: o fundo quer saber de que é feito o ativo;
- complicação: os números públicos não passam numa auditoria, e o modelo erra mais com idosos de CEP D/E;
- questão: o ativo é defensável?
- resposta: ainda não, e o documento diz o que muda isso.

Depois vêm os quatro blocos do enunciado, na ordem dele.

**Abrir pela decisão.** O Código do IBGC pede que todo material para deliberação comece com um sumário e com o posicionamento fundamentado da diretoria, e que o conselheiro identifique "com clareza e objetividade, o assunto a ser deliberado e eventuais pontos de atenção" (CON-02). Na v2, isso é um destaque curto em prosa, com a tese e o pedido, que não se repete no fim (D-012). O guia da Board Intelligence vai na mesma linha, com sumário de uma página e frases curtas (CON-08) [não verificado; não entra no corpo].

**Má notícia primeiro.** O IBGC pede informação "verdadeira, tempestiva, clara e relevante, sejam elas positivas ou negativas" (CON-01). Os estudos de mercado mostram que gestores tendem a atrasar notícias ruins e que, quando elas saem, a reação é maior (Kothari et al., CON-13). Há um contraponto: divulgar mais está associado a processos que avançam (Cutler et al., CON-13). Por isso a regra é divulgar com precisão, sem acumular volume. O Vila Ipê já descobriu o viés [fonte: Cap. 2, Quadro 14], então esperar não protege ninguém.

**Corpo e anexo.**
- No corpo ficam só os números que mudam a conclusão: composição e autorização da base (Q7), queda da validação para o campo (Q9), falso negativo por subgrupo (Q10), o placar das cinco afirmações (Q11) e os cinco indicadores (CON-16).
- No anexo ficam a tabela completa das variáveis, os pesos alternativos, as quatro perguntas aplicadas a cada afirmação e indicador, as contas de conferência, a conta de amostra e a lista do que não consta.

**Tabela ou gráfico.** Tabela quando o leitor precisa comparar valores exatos. Gráfico só quando há um padrão a mostrar, com um título que já diga a mensagem, sem 3D e sem enfeite (CON-10). Na v2, isso dá uma figura (falso negativo por subgrupo) e quatro tabelas, como na F2-E1 v2 (D-019). Nenhuma tabela do corpo passa de cinco colunas, para caber em retrato.

**Ressalva ao lado do número.** A limitação aparece junto do dado, e não só no anexo (CON-11). Exemplo: "94,1%, medidos em 48 mil registros de dois hospitais da mesma região, em 2023 [fonte: Cap. 2, Quadro 9]".

**Tamanho.** O enunciado não fixa páginas para a E2. O único limite é o do memorando, de duas páginas [fonte: Cap. 2, 4.2]. Sugerimos de 4 a 5 páginas de corpo, como na F2-E1, mais o anexo [hipótese: escolha da equipe].

**Tom.**
- Frases curtas e declarativas, com o número logo depois da afirmação.
- Linguagem comum. Exemplo: "de cada 10 idosos de bairros D/E que precisavam de prioridade, 3 ficaram para trás". A frase do anexo correta é "31,8% dos que precisavam de prioridade foram classificados como baixa prioridade". Dizer "erra 31,8% dos idosos" está errado, porque a acurácia nesse grupo é 79,3% (CON-19).
- Termos técnicos traduzidos ou levados ao anexo:

| Termo | No corpo da v2 |
|---|---|
| contra-indicador | "o custo do ajuste: quantos pacientes a mais passam a ser priorizados" |
| valor preditivo positivo | anexo |
| calibrar por subgrupo | anexo |
| teste contrafactual | "trocar só o CEP e o plano de um mesmo paciente e ver se a prioridade muda" |
| igualdade de oportunidade | "mesma taxa de erro grave em todos os grupos" |
| cocontroladora | "responsável pelos dados junto com o cliente" |
| plano de controle de mudanças da FDA | "regra de liberação definida antes, como a FDA exige de dispositivos médicos com IA"; detalhe no anexo |

- Pessoas descritas pela conduta e pelo fato, sem culpar o comercial. A explicação estrutural vem de Goodhart [fonte: Cap. 2, 2.3] e fica para a F2-E4.
- A frase do capítulo ajuda no tom: "O número nunca foi mentira. Ele apenas nunca foi o que o comercial acreditava que era" [fonte: Cap. 2, p. 6].
- Evitar listas de três no destaque e na tese. A v1 foi criticada por isso.
- Revisão final com a skill humanizer (D-010).

## 2. Diagnóstico da v1 do colega

**O que fica.**
- Todos os números conferem com os Quadros 7 a 11, e as contas estão certas: 9,5%, −6,5 p.p., −10,3 p.p., +10,3 p.p. e três vezes.
- A tabela por fonte, com vencimento e prioridade Prisma e depois Vila Ipê, e a frase "a renovação não deve ser o único gatilho".
- A tabela das variáveis com "o que a empresa diz medir" ao lado de "o que pode medir de fato". É o formato que o enunciado pede.
- A escolha de sensibilidade e falso negativo como métricas certas para priorização.
- A tabela do painel com as colunas "autoriza" e "não autoriza". O conteúdo das cinco linhas serve de ponto de partida para a tabela de descartes.
- Os indicadores de falso negativo por subgrupo, de cobertura contratual e de reclamações normalizadas por subgrupo.
- O cuidado com causalidade no CEP. Na v2, a causa geral vira fato do caso (2.2) e o peso de cada variável fica como `[hipótese]`.
- A Figura 1, que fica com o grupo pior em destaque.

**O que corrigir.** A v1 não tem número errado. Os problemas são de citação, de leitura otimista e de hipótese apresentada como fato.

**O que falta frente ao enunciado.**
- A base legal.
- As quatro perguntas aplicadas aos descartes.
- A vantagem defensável.
- O caso de proxy do próprio capítulo.
- Gatilho e valor de hoje em cada indicador.
- Os Quadros 3, 12, 14 e 17.

| ID | Problema na v1 | Correção na v2 |
|---|---|---|
| V1-01 | Atribui as quatro perguntas ao "Capítulo 1" | `[fonte: Cap. 2, 2.3, p. 9]` |
| V1-02 | Cita "Anexo A do case" sem número de quadro; usa os Quadros 12, 14 e 17 sem citar | Quadro numerado em cada legenda (D-018); "caso" no lugar de "case" |
| V1-03 | A figura mostra só o falso negativo | Somar sensibilidade e participação: 60+ D/E tem sensibilidade de 68,2%, e os três subgrupos acima da média somam 39% da base [conta] |
| V1-04 | Omite o incidente de 01/2026 | Dizer que a duplicidade foi "corrigida no sistema; não corrigida no material comercial" [fonte: Quadro 14] |
| V1-05/06 | Omite o Quadro 17 (reclamações por CEP) e o Quadro 12 (revisão de 2%) | Usar os dois em métricas e indicadores |
| V1-08 | Chama Sanare e Meridiano de "mais robusta" | "Autoriza com condição ainda não verificada"; nenhum instrumento passou por revisão jurídica |
| V1-09 | Diz que DATASUS não tem fragilidade e trata os sintéticos como controle interno | DATASUS retrata o SUS até 2024 [hipótese de representação]; a origem dos sintéticos [não consta] |
| V1-10 | Não sinaliza as divergências do caso | Notas curtas, conforme D-003: "dois" (Quadro 5) contra "três" (1.2) e dados anteriores à fundação (Quadros 3 e 7) |
| V1-11/12 | Apresenta o mecanismo de cada variável como fato; a coluna "Risco" aparece como dado | O mecanismo geral é fato do caso [fonte: Cap. 2, 2.2, p. 8]. O papel de cada variável e o percentual de peso ficam `[hipótese]`, com "Risco: leitura da equipe" na legenda |
| V1-14 | Não trata a base legal | Subseção LGPD (ver 3.1) |
| V1-16 | O caso de proxy escolhido é o CEP | Custo acumulado e atendimentos, com o CEP como reforço (ver 3.2) |
| V1-18/25 | Decisões em forma de menu, sem gatilho e sem valor de hoje | Limite, decisão e valor atual em cada indicador (ver 3.4) |
| V1-20/21 | Não aplica as quatro perguntas aos descartes | Tabela de descartes (ver 3.3 e 3.4) |
| V1-23/24 | "Não plenamente defensável" é eufemismo, e falta a vantagem defensável | Dizer o que é defensável em números (ver 3.1) |
| V1-28/29 | "Drift" repete o indicador 1; "disponibilidade" não muda decisão do conselho | Juntar o "drift" ao indicador 1 e trocar a disponibilidade |
| V1-31/32 | Responsáveis são áreas ("Operações" nem existe no Quadro 13) | Cargos do Quadro 13, com quem apura, quem confere de fora e quem decide. Onde o cargo não existe, `[não consta]` com cargo provisório `[hipótese]` |
| V1-33 | O indicador 1 é mensal | Leitura quinzenal, como manda o C2, sobre janela com amostra suficiente |
| V1-38/39 | Abre com "Esta entrega audita..." | Abrir com a tese |
| V1-40 a 45 | Jargão (drift, baseline, rollback, E2E, claim, CS) e muletas de estilo: 15 travessões, "não é apenas X, mas Y", tríades, "robusta", "exatamente três vezes" | Linguagem comum e revisão com o humanizer |
| V1-46 | Seis tabelas e uma figura em três páginas | Quatro tabelas curtas e uma figura no corpo; o resto vai para o anexo |

## 3. Achados por tema do enunciado

### 3.1 Origem, base contratual e base legal dos dados

**Dado do anexo** [fonte: Cap. 2, Quadro 7 e texto após o quadro]:

| Fonte | Volume e período | Instrumento | O que diz | Vencimento |
|---|---|---|---|---|
| Hospital Vila Ipê | 1,2 mi atendimentos, 2019 a 2026 | Contrato de 2022 | Cláusula genérica: "melhoria contínua do serviço" | 03/2027 |
| Rede Sanare (7 unidades) | 3,4 mi atendimentos, 2020 a 2026 | Aditivo de 2024 | Sim, para uso agregado e anonimizado | 08/2028 |
| Seguradora Prisma | 890 mil sinistros, 2021 a 2026 | Contrato de 2021 | Silente | 12/2026 |
| Banco Meridiano | 410 mil operações, 2023 a 2026 | Contrato de 2023 | Sim, com auditoria anual do cliente | 05/2028 |
| DATASUS | 14,0 mi registros, 2015 a 2024 | Uso público | Sim | Não se aplica |
| Sintéticos internos | 2,1 mi registros, 2024 a 2026 | Geração própria | Sim | Não se aplica |

Outros fatos do anexo:
- "Nenhum dos seis instrumentos passou por revisão jurídica desde a assinatura" [fonte: texto após o Quadro 7].
- A política de privacidade para dados sensíveis de saúde está "em elaboração desde 2024, sem versão aprovada" [fonte: Quadro 17].
- A DPO é Ana Beatriz Rangel [fonte: Quadro 13].
- O Vila Ipê aparece em dois papéis: é a fonte com cláusula genérica e é o cliente que apurou o viés e mandou a notificação formal [fonte: Quadros 7, 10 e 14]. A Lumis depende dos dados de quem está reclamando dela.
- A Lumis tem 38 contas (24 hospitais e clínicas, 9 seguradoras e 5 bancos), ARR de R$ 41,2 mi e ticket médio de R$ 1,084 mi [fonte: Cap. 2, Quadro 3, 5.1, p. 19]. A Prisma deve ser uma das 9 seguradoras e o Vila Ipê um dos 24 hospitais [hipótese: o quadro não lista nomes].
- Os dados de clientes vêm de 38 contas, e só quatro fontes aparecem no Quadro 7. Se as outras 34 fornecem dados para treino [não consta].

**Divergências a sinalizar (D-003):**
- "Dois" contra "três". O Quadro 5 fala em "dois dos maiores contratos" com cláusula frágil e a narrativa fala em "três" [fonte: Cap. 2, 1.2, p. 6]. O Quadro 7 sustenta dois, e usamos o Quadro 7.
- Dados anteriores à empresa. A Lumis foi fundada em 2022 [fonte: Quadro 3], e a narrativa fala em base "construída ao longo de quatro anos" [fonte: Cap. 2, 1.2, p. 6]. Mas o contrato da Prisma é de 2021, os dados do Vila Ipê começam em 2019 e os da Sanare em 2020 [fonte: Quadro 7]. O contrato do Vila Ipê (2022) é posterior a três anos dos dados que ele cobre, e o aditivo da Sanare (2024) é posterior a quatro. Se a Lumis recebeu histórico anterior ao contrato, e sob que cláusula, [não consta]. É a primeira pergunta que uma due diligence faria. Tratamos o uso retroativo como mais um ponto frágil da base legal [hipótese].

**Conta da equipe** (verificada):
- Composição da base: clientes 26,8%, DATASUS 63,6%, sintéticos 9,5%. A parte exclusiva da Lumis é a de clientes, 5,9 mi. O DATASUS tem autorização de uso, só que qualquer concorrente também tem.
- A Sanare sozinha é 57,6% dos dados de clientes. Sem ela, sobram 2,5 mi (42,4%).
- Autorização frágil: 2,09 mi, que são 35,4% dos dados de clientes. No corpo, usar só essa forma. O "9,5% da base total" coincide com o percentual dos sintéticos e confunde o leitor, por isso fica no anexo.
- Autorização expressa (Sanare + Meridiano): 3,81 mi, que são 64,6% dos dados de clientes. Mesmo essa parte depende de condições cujo cumprimento [não consta].
- Com autorização expressa e revisão jurídica: 0%.
- Prazos contados de 06/10/2026: Prisma em 2 a 3 meses, Vila Ipê em 5 a 6 meses. As duas fontes que vencem primeiro são as mesmas que têm autorização frágil. Nenhuma fonte de cliente passa de 08/2028.
- Receita ligada às duas fontes frágeis: cerca de R$ 2,2 mi por ano, uns 5% do ARR [conta; hipótese: as duas pagam perto do ticket médio].
- Multa simples: até 2% do faturamento, com teto de R$ 50 mi por infração (LGPD, art. 52, II). Com faturamento perto do ARR [hipótese], cerca de R$ 0,8 mi por infração [conta].
- Se for preciso retirar esses dados ao fim do contrato [hipótese], a base de clientes cai para 3,81 mi e a total para 19,91 mi, e os clientes passam a ser 19,1% da base. Se o fim do contrato obriga a retirar os dados [não consta].

**Contexto externo verificado.**
- Dado referente à saúde é dado pessoal sensível (LGPD, art. 5º, II). Para tratá-lo, é preciso uma base do art. 11. O consentimento só vale se for "específico e destacado, para finalidades específicas" (LEG-01, LEG-02).
- O princípio da finalidade proíbe "tratamento posterior de forma incompatível" com o que foi informado ao titular (art. 6º, I). Uma cláusula de "melhoria contínua do serviço" dificilmente cobre treinar um produto vendido a outros clientes (LEG-02).
- O operador age "em nome do controlador" (art. 5º, VII; art. 39). O guia da ANPD diz que ele "só poderá tratar os dados para a finalidade previamente estabelecida pelo controlador" e que, se descumprir, é equiparado ao controlador e responde junto (art. 42, §1º, I) (LEG-04).
- Dado anonimizado só deixa de ser dado pessoal se a anonimização não puder ser revertida com meios razoáveis (art. 12) (LEG-01). A palavra "anonimizado" no aditivo da Sanare depende de prova técnica. A ANPD ainda não teria versão final do guia de anonimização (LEG-11) [não verificado; não entra no corpo].
- O art. 11, §4º proíbe o uso compartilhado de dado de saúde entre controladores com objetivo de vantagem econômica, salvo em serviços de saúde em benefício do titular. O §5º proíbe operadoras de planos de saúde de usar dado de saúde para seleção de riscos (LEG-03). Se a Prisma é operadora de plano de saúde [não consta].
- Banco Meridiano: o sigilo bancário só cede com "consentimento expresso dos interessados", e a quebra fora da lei é crime (LC 105/2001, arts. 1º e 10) (LEG-09). A autorização do banco não é consentimento do correntista. Se as operações são identificadas [não consta].
- DATASUS: dado de acesso público "deve considerar a finalidade, a boa-fé e o interesse público que justificaram sua disponibilização" (LGPD, art. 7º, §3º) (LEG-15).
- Sanções: o teto da multa simples (2% do faturamento, até R$ 50 mi por infração) vem do art. 52, II da LGPD (LEG-01). O mesmo art. 52 prevê eliminação dos dados e suspensão do tratamento (DIL-04). A Res. CD/ANPD 4/2023 entra só pela classificação da gravidade. Ela trata como grave a infração que possa afetar significativamente interesses e direitos fundamentais dos titulares e que envolva, entre outras situações, dado sensível, idosos, larga escala, vantagem econômica ou efeito discriminatório (LEG-05). Pendência: conferir a redação exata do artigo no original antes de citar.
- Precedentes:
  - No Reino Unido, o regulador concluiu que o uso de 1,6 mi de registros do Royal Free pela DeepMind fugia do que os pacientes esperariam, e a cobrança caiu primeiro sobre o hospital (LEG-07).
  - Nos EUA, a FTC mandou a Everalbum apagar os modelos treinados com dados usados fora do prometido (DIL-03).
  - A ANPD suspendeu em 2024 o treinamento de IA da Meta por hipótese legal inadequada e falta de transparência (LEG-06) [não verificado; só por resumo; anexo, como contexto].
- Prontuário digital segue a LGPD e exige confidencialidade (Lei 13.787/2018), e o médico tem dever de sigilo (Código de Ética Médica, art. 73) (LEG-10) [não verificado; fonte secundária para o CFM; anexo, como contexto].
- Vantagem defensável: volume de dados raramente é fosso, porque dado tende a virar commodity (a16z, DIL-10). Combina com a leitura da F2-E1 (D-009).

**Hipótese.**
- Ao treinar o próprio modelo com dados do cliente, a Lumis decide uma finalidade própria e passa a agir como responsável pelos dados junto com o cliente (controladora). Nesse papel, precisa de base legal própria (LEG-04).
- Se o treino usa registro por paciente, a condição da Sanare ("agregado e anonimizado") pode não estar sendo cumprida.
- Retirar uma fonte da base tende a exigir retreino, porque o modelo já incorporou esses dados. A fragilidade contratual vira risco de produto e de custo (LEG-17).
- O DATASUS retrata a população do SUS até 2024, e a Lumis atende hospitais privados, seguradoras e bancos. Isso pode distorcer a representação.
- Se os sintéticos foram gerados a partir de dados de clientes, herdam a fragilidade deles. A origem deles [não consta].
- O que é defensável hoje, em uma linha: no máximo os 3,81 mi de clientes com autorização expressa, e mesmo essa parte tem condições não verificadas. O histórico de clientes pode virar fosso se os contratos forem regularizados, inclusive para o período anterior à assinatura, e se o viés for corrigido (D-020).
- Cláusula que a renegociação com Vila Ipê e Prisma deveria trazer (LEG-16):
  - finalidade nomeada, incluindo treino para uso com outros clientes;
  - papel de cada parte;
  - base legal do art. 11 e quem a obtém junto ao titular;
  - cobertura expressa do histórico anterior à data do contrato;
  - padrão de anonimização com direito de auditoria;
  - destino do modelo treinado ao fim do contrato;
  - vedação de seleção de risco.

**Pedido que fecha a seção:** parecer da DPO sobre os seis instrumentos e sobre o uso retroativo antes do próximo treinamento, e aprovação da política de dados de saúde.

### 3.2 Variáveis e o caso de proxy

**Dado do anexo** [fonte: Cap. 2, Quadro 8]. Os dez pesos somam 100,0%, embora o quadro diga "dez maiores pesos". Ou o modelo tem só dez variáveis, ou os pesos foram normalizados [não consta]. Também não constam a definição técnica de "peso", o sinal de cada variável e o rótulo-alvo do treino [não consta].

| # | Variável (peso) | A empresa diz medir | O que tende a medir [hipótese] | Contexto externo |
|---|---|---|---|---|
| 1 | Nº de atendimentos em 24 meses (18,4%) | Necessidade de cuidado | Quem conseguiu ser atendido | PRX-01, PRX-10 |
| 2 | Custo acumulado (15,1%) | Gravidade | Quem teve acesso a procedimentos pagos | Cap. 2, 2.2; PRX-01 |
| 3 | Idade (12,7%) | Idade | Idade, com fundamento clínico legítimo | PRX-11, PRX-13 |
| 4 | Comorbidades registradas (11,2%) | Carga de doença | Doença diagnosticada, que depende de acesso | PRX-11 |
| 5 | Tempo entre consulta e exame (9,8%) | Urgência percebida | Oferta da rede e fila regional | PRX-07, PRX-08, PRX-20 |
| 6 | Faixa de CEP (8,9%) | Região | Renda e oferta de serviços | PRX-03, PRX-04 |
| 7 | Tipo de plano (7,4%) | Cobertura | Renda | PRX-09 [não verificado] |
| 8 | Painel laboratorial (6,9%) | Estado clínico | Estado clínico, quando o exame foi pedido | PRX-07 |
| 9 | Faltas em consultas (5,3%) | Adesão | Transporte, trabalho e tempo de espera | PRX-05, PRX-06 |
| 10 | Especialidade de origem (4,3%) | Via de entrada | Via de entrada, que depende de acesso | |

No corpo, a Tabela 2 traz só as variáveis do critério estrito (#1, #2, #6 e #7), mais as de leitura discutível (#3 e #4). A tabela completa vai para o anexo.

**O caso de proxy explícito.** O caso principal é o custo acumulado (#2) junto com o número de atendimentos (#1). O capítulo dá esse exemplo: um sistema que usa gasto como indicador de gravidade "não está medindo quem está mais doente", e sim "quem teve mais acesso a atendimento" [fonte: Cap. 2, 2.2]. E logo depois afirma que "Foi exatamente isso que aconteceu no incidente da Fase 1. [...] Houve uma escolha de representação que ninguém questionou" [fonte: Cap. 2, 2.2, p. 8]. O mecanismo, portanto, é fato do caso. As duas variáveis são os maiores pesos e somam 33,5% [conta].

O análogo real é o estudo de Obermeyer et al. (2019) (PRX-01). Um algoritmo americano usava custo como proxy de necessidade. Com o mesmo escore, pacientes negros estavam mais doentes. Corrigir a distorção elevaria de 17,7% para 46,5% a fração de pacientes negros elegíveis a cuidado extra.

Cuidado ao citar: o 17,7% do estudo coincide com o falso negativo da Lumis em campo. No texto, os dois números precisam ficar separados para o leitor não confundir.

O CEP (#6) entra como reforço. Ele mede o que a empresa diz ("região"), e por isso mesmo leva renda para dentro do modelo. Na Univ. of Chicago, o código postal prevê bem justamente porque codifica desigualdade (PRX-03).

**Conta da equipe** (verificada):
- Peso em variáveis de acesso ou renda [hipótese: critério da equipe]. No corpo, um único número: 49,8% (#1, #2, #6 e #7, variáveis que registram uso passado de serviços ou renda). No anexo, as leituras alternativas:
  - somando o tempo até o exame e as faltas (#5 e #9): 64,9%;
  - somando também a especialidade (#10): 69,2%;
  - tratando comorbidades e exames como dependentes de atendimento e tirando a especialidade, que tem outra lógica: 83,0%. As bases são diferentes, por isso esse número não se compara direto com o de 69,2%.
- Sinal clínico direto: 6,9% (só #8) ou 18,1% (com #4). A variável #4 pode cair dos dois lados, e isso precisa ser dito no anexo.
- Falso negativo agregado, supondo a mesma prevalência em todos os subgrupos [hipótese]: 18 a 59 anos 14,5%, 60 ou mais 23,1%, CEP A/B 12,6%, C 17,4% e D/E 24,8%.
- Efeito do CEP com idade fixa (D/E contra A/B): +9,6 p.p. em 18 a 59 e +15,9 p.p. em 60 ou mais.
- Efeito da idade com CEP fixo: +5,3, +9,2 e +11,6 p.p.
- Leitura correta: o extremo D/E pesa mais que a idade. CEP C contra A/B pesa menos que a idade.
- Os dois efeitos juntos passam da soma: o esperado seria 25,5% e o observado é 31,8%. Ficam perto do produto (cerca de 30,3%). Sem intervalo de confiança no anexo, não dá para afirmar que a interação é significativa (PRX-16).

**Contexto externo verificado.**
- Classificadores de imagem subdiagnosticam mais em grupos mal atendidos, e mais ainda na interseção de duas desvantagens (Seyyed-Kalantari et al., PRX-12). É o mesmo desenho do Quadro 10.
- O IBGE reconhece subdiagnóstico regional de hipertensão (PRX-11). Isso sustenta a crítica a "comorbidades registradas".
- O momento em que um exame é pedido prevê sobrevida melhor que o resultado em cerca de 68% dos exames comparáveis (Agniel et al., PRX-07). O modelo aprende o comportamento da rede.
- Ponto que pede cuidado: no agregado nacional, idosos usam mais serviços (PRX-10). "O modelo mede acesso" não explica sozinho o pior desempenho dos 60 ou mais, e é nesse grupo que está o 31,8%.

**O que é fato e o que é hipótese no mecanismo.**
- Fato do caso: o viés da Fase 1 veio de uma escolha de representação que mede acesso como se fosse gravidade [fonte: Cap. 2, 2.2, p. 8], e o desempenho cai mais nos grupos da reclamação [fonte: Cap. 2, 1.2, p. 6].
- Bem sustentado pelo Quadro 10: o efeito do CEP. Com a idade fixa, o falso negativo sobe de A/B para D/E nas duas faixas.
- Hipótese, com duas explicações que o anexo não permite separar (PRX-17):
  - o rótulo do treino ou as variáveis dominantes refletem uso passado, e nos idosos a carga de doença cresce mais rápido que o uso registrado;
  - a base de treino tem poucos idosos, em especial de CEP D/E.

A validação de 2023, feita em dois hospitais de uma região, explica por que o problema não apareceu no número divulgado. Ela não explica sozinha o erro em campo.

Testes para a Fase 3 (PRX-19, PRX-02), nenhum deles feito pela Lumis [não consta]:
- trocar o rótulo do treino e comparar o falso negativo por subgrupo;
- retirar o bloco de variáveis de acesso e comparar;
- trocar só o CEP e o plano de um mesmo paciente e ver se a prioridade muda;
- ajustar o ponto de corte por subgrupo (detalhe técnico no anexo).

Pelo C5 (minimização de dados), cabe perguntar se CEP e tipo de plano deveriam estar no modelo.

### 3.3 Métricas do painel comercial

**Dado do anexo** [fonte: Cap. 2, Quadros 9, 11 e 14]: as cinco afirmações e como foram apuradas, reproduzidas na tabela abaixo. Quem apurou a validação de 2023 e a linha de campo do Quadro 9 [não consta]. Supor que foi a própria Lumis é `[hipótese]`. O 31,8% foi apurado pelo Vila Ipê. Se toda a abertura do Quadro 10 vem dele ou da base completa [não consta]. As participações batem com o Quadro 17, o que sugere base completa.

Leitura geral: nenhuma das cinco passa do jeito que é divulgada. O 94,1% e o 99,92% podem ser reproduzidos dentro do escopo em que foram medidos, e o que falha é a forma de divulgar. Só os "5 milhões de vidas" estão errados no próprio número, e a empresa sabe disso desde 01/2026.

Todas as cinco são descartadas ou reformuladas. Por isso, cada uma passa pelas quatro perguntas. Esta é a versão completa, que vai para o anexo:

| Afirmação | Medida em quê? | Por quem? | Muda alguma decisão? | Esconde qual distribuição? |
|---|---|---|---|---|
| "Acurácia de 94%" (94,1%) | 48 mil registros de 2023, dois hospitais da mesma região | [não consta]; apuração interna [hipótese] | Não. Ninguém age quando ela muda, e ela virou discurso (Goodhart, Cap. 2, 2.3) | O falso negativo e os subgrupos. Em campo: 87,6%, FN 17,7% e, no pior subgrupo, 31,8% |
| "Redução de 30% no tempo de triagem" (30,4%) | Seis semanas, um hospital, sem grupo de controle | [não consta] | Não, sem comparação | Não há abertura por subgrupo nem por hospital |
| "Mais de 5 milhões de vidas" (5,2 mi) | Registros processados, com reprocessamentos | A duplicidade foi detectada pela auditoria interna em 01/2026 [fonte: Quadro 14] | Não. É volume (vaidade, Cap. 2, 2.3) | Quantas pessoas únicas há [não consta] |
| "NPS 72" | 9 respondentes | Indicados pelo time comercial | Não | As 38 contas e as 74 reclamações formais em 12 meses, 47 delas de CEP D/E [fonte: Quadro 17] |
| "Disponibilidade de 99,9%" (99,92%) | Só a interface de programação (API) | [não consta] | Pouco. É operacional | O serviço de ponta a ponta e a qualidade da resposta |

Para o corpo (Tabela 3), quatro colunas:

| Afirmação | O que autoriza dizer | O que não autoriza | Destino |
|---|---|---|---|
| "Acurácia de 94%" | Que o modelo acertou 94,1% numa amostra de 2023 de dois hospitais | Que acerta 94% hoje, em qualquer cliente ou grupo | Aposentar. Trocar pelo falso negativo em campo por subgrupo (indicador 1) |
| "Redução de 30% no tempo de triagem" | Que o tempo caiu 30,4% num piloto de seis semanas | Atribuir a queda ao produto ou estender a outros hospitais | Retirar até haver estudo com comparação |
| "Mais de 5 milhões de vidas" | Que houve 5,2 mi de processamentos | Falar em vidas ou pessoas | Retirar já. Sabidamente inflada desde 01/2026 e ainda no material comercial [fonte: Quadro 14] |
| "NPS 72" | Que 9 clientes indicados pelo comercial aprovam | Falar em satisfação da carteira | Aposentar. Reclamação por subgrupo entra como indicador 3 |
| "Disponibilidade de 99,9%" | Que a API ficou no ar 99,92% do tempo | Que o hospital recebeu a priorização correta a tempo | Reformular para ponta a ponta. Sai do material comercial |

**Conta da equipe** (verificada):
- Da validação para o campo, a acurácia cai 6,5 p.p. O falso negativo vai a 2,4 vezes, e o erro total vai de 5,9% para 12,4%. A acurácia esconde a piora que importa.
- A validação equivale a 2,5% da amostra de campo de um semestre.
- Ponderada pelo Quadro 10, a acurácia dá 87,2%, contra 87,6% no Quadro 9. O arredondamento explica no máximo 0,1 p.p. O resto [não consta].
- O campo tem cerca de 323 mil registros por mês, e o Quadro 12 fala em 640 mil decisões por mês. A diferença [não consta].
- NPS: com 9 respostas, cada resposta move o número em 11,1 pontos, e 72 não é um valor possível. Os vizinhos são 66,7 e 77,8. Como o 72 foi calculado [não consta].
- 99,92% de disponibilidade admite 7,0 h por ano, cerca de 35 min por mês. Se a integração e a carga de dados tiverem 99,5% cada [hipótese], a cadeia fica em cerca de 98,9%, perto de 94 h por ano fora do ar.
- Em 03/2025, o modelo descartou exames de um laboratório por 22 dias com a API no ar, e quem detectou foi o cliente [fonte: Quadro 14].

**Contexto externo verificado.**
- Queda entre validação e campo é a regra em IA clínica, e não acidente.
  - O modelo de sepse da Epic teve AUC de 0,63 numa validação independente, contra 0,76 a 0,83 declarados (MET-01).
  - Em 81% das validações externas de modelos cardiovasculares, a discriminação ficou abaixo da derivação (MET-02).
- O TRIPOD+AI exige intervalo de confiança, desempenho por subgrupo sociodemográfico e justificativa da amostra (MET-07). Esse é o checklist mínimo para qualquer número público.
- Piloto curto sem controle está exposto a regressão à média e a efeito Hawthorne (MET-09).
- NPS com n = 9: pelo método da MeasuringU, o intervalo de 95% vai de cerca de 8 a 92 ou de 24 a 93, conforme o mix de respostas (MET-11).
- O livro de SRE do Google define o nível de serviço pela experiência do usuário (MET-13) [não verificado por inteiro; anexo].
- No Texas, a Pieces Technologies, que vende IA clínica a hospitais, fez acordo com o procurador-geral em 2024. Ela nega irregularidade e se obrigou a divulgar definição e método de cada métrica (MET-15) [não verificado; lido via escritório de advocacia; anexo, como contexto, até conferir no original].

**Hipótese.**
- Manter as afirmações contradiz o C1, que pede informar as limitações, e para o fundo vira passivo de conduta, em especial "vidas analisadas" (MET-18).
- Se o CDC alcança uma venda B2B como a da Lumis [não verificado]. Não citar o CDC no corpo.

### 3.4 Indicadores de gestão

**Escolha de método, dita no texto.** Nenhum escore de risco atende ao mesmo tempo todos os critérios de equidade quando a quantidade de casos graves difere entre grupos (IND-05). Para priorização, o dano é o falso negativo [fonte: Cap. 2, Quadro 9]. Por isso, a regra escolhida é a mesma taxa de erro grave em todos os grupos. No anexo, com o nome técnico (igualdade de oportunidade, Hardt et al., IND-05).

Essa escolha tem custo. Baixar o falso negativo de um grupo tende a aumentar os alarmes falsos nesse grupo, o que significa mais pacientes priorizados e mais carga para o hospital (Rajkomar et al., IND-06). O indicador 1 mostra esse custo ao lado.

Para os usos em seguradoras e bancos, a regra adequada pode ser outra [hipótese]. O desempenho por subgrupo nesses usos [não consta].

Os limites abaixo são todos `[hipótese]`. Nenhuma fonte fixa valores para este caso, e a literatura trata o limite como decisão de gestão (IND-09).

Responsáveis provisórios, até a F2-E3 [fonte: Cap. 2, Quadro 13]:
- Yuri Nakamura (Dados) apura;
- o Head of AI Management (nós) confere e coordena, como prevê o C4;
- Paulo Adjaí (CTO) libera versões;
- Ana Beatriz Rangel (DPO) cuida do direito de uso;
- Camila Torres (Comercial) publica;
- Renata Souza (CEO) decide suspensão [hipótese: até a F2-E3 definir].

Quem executa a revisão humana de 2% [não consta]. O Quadro 12 não diz, e o C3 só atribui à instituição de saúde a revisão clínica.

**Indicador 1. Falso negativo em campo por subgrupo (idade × CEP) e razão entre o pior e o melhor subgrupo**
- Valor hoje [fonte: Quadro 10; conta]: pior subgrupo 31,8%, melhor 10,6%, razão 3,0. Sensibilidade do pior subgrupo: 68,2%.
- Decisão que muda: restringir a recomendação automática num recorte, e liberar ou barrar uma nova versão. O "drift" da v1 entra aqui como regra de liberação: nenhuma versão vai a produção se piorar o falso negativo de algum subgrupo [hipótese de limite: mais de 1 p.p.]. A regra é definida antes, como a FDA exige de dispositivos médicos com IA (IND-02; detalhe no anexo).
- Limite [hipótese], com fronteira "a partir de":
  - Nível 1: a partir de 1,5 vez o melhor subgrupo. A revisão humana no recorte sobe de 2% para 10% e o caso vai à pauta quinzenal.
  - Nível 2: a partir de 2 vezes o melhor, ou a partir de 25%. A recomendação automática é suspensa no recorte até a correção, como manda o C2. O modelo continua rodando em paralelo, sem decidir, para medir a correção [hipótese].
- Onde cada subgrupo está hoje [conta]:
  - nível 2: 60+ D/E (3,0 vezes) e 60+ C (2,2 vezes), 24% da base;
  - nível 1: 18 a 59 D/E (1,9 vez) e 60+ A/B (exatamente 1,50 vez: 15,9 ÷ 10,6), 28% da base;
  - abaixo: 18 a 59 C (1,35 vez).
- Custo da regra, se a distribuição das decisões seguir a da base [hipótese] [conta]:
  - nível 2: cerca de 154 mil decisões por mês deixam de ter recomendação automática e passam ao protocolo de triagem do próprio hospital;
  - nível 1: cerca de 18 mil revisões por mês (10% de 179 mil);
  - demais recortes: cerca de 6 mil revisões por mês (2% de 307 mil);
  - total de revisões: cerca de 24 mil por mês, contra 12.800 hoje, quase o dobro.
  - Um corte único de 15% pegaria quatro dos seis subgrupos (52% da base, cerca de 333 mil decisões por mês) (IND-16). Por isso a proposta usa escala.
- Tamanho de amostra [conta]. O falso negativo só se calcula entre os pacientes que precisavam de prioridade, e não sobre todos os casos revisados. No 60+ D/E, com 2% de revisão, são cerca de 1.280 casos revisados por mês. Com prevalência de 10% [hipótese], só uns 128 deles precisavam de prioridade, uns 64 por quinzena. Com 64 casos, a margem de erro fica em torno de ±11 p.p., e não dá para separar 1,5 vez de 2 vezes a cada quinzena. Para chegar perto de ±5 p.p., são precisos uns 320 casos. Há dois caminhos, e a v2 escolhe um:
  - revisão a 10% nos recortes críticos, o que dá uns 320 casos por quinzena no 60+ D/E;
  - janela acumulada de 90 dias com leitura quinzenal. Com 2%, isso dá uns 384 casos e margem de cerca de ±4,7 p.p.
  - A proposta de nível 1 acima já usa o primeiro caminho. Nos recortes do nível 2, a medição vem do modelo rodando em paralelo.
- Custo do ajuste, acompanhado junto: quantos pacientes a mais passam a ser priorizados no mesmo subgrupo (IND-06; nome técnico no anexo).
- Cargos e conferência:
  - Yuri Nakamura (Dados) apura.
  - Conflito admitido: a Lumis mede o erro do próprio produto. Por isso a conferência vem de fora. O cliente que manda o desfecho recalcula o próprio recorte, como o Vila Ipê já fez. Um auditor contratado reproduz o cálculo a cada trimestre [hipótese: a contratação é decisão da E3].
  - O Head of AI Management confere e leva à pauta. A CEO decide a suspensão. O CTO só libera versão dentro da regra.
- Abertura: os seis subgrupos do Quadro 10, leitura quinzenal (C2), também por cliente.
- Quatro perguntas:
  - Medida em quê? Em campo, na amostra de revisão humana ampliada nos recortes críticos e no desfecho informado pelo cliente.
  - Por quem? Pela Lumis (Yuri Nakamura), que tem interesse no resultado. Por isso o cliente e um auditor contratado precisam conseguir reproduzir o número com os mesmos dados.
  - Muda alguma decisão? Sim: restrição de recorte e liberação de versão.
  - Esconde qual distribuição? Diferenças por cliente e por especialidade, que entram como abertura secundária. Também esconde subgrupos que o Quadro 10 não abre (sexo, por exemplo) [hipótese].
- Contexto externo: o NIST AI RMF, em MANAGE 2.4, pede mecanismos e responsáveis para desligar sistemas fora do uso pretendido (IND-03). O GMLP pede monitoramento em uso real (IND-01) [não verificado; anexo].

**Indicador 2. Direito de uso da base de treino**
- Definição: parcela dos registros usados no treino que têm autorização expressa e parecer da DPO. Entram no inventário os dados de clientes e os 2,1 mi de sintéticos, enquanto não se comprovar que estes não vêm de dados de clientes.
- Valor hoje: 0% pela definição, porque nenhum instrumento passou por revisão jurídica [fonte: Quadro 7]. Etapa intermediária: 64,6% dos dados de clientes têm autorização expressa, ainda sem parecer [conta]. Origem dos sintéticos [não consta].
- Decisão que muda: o que entra no próximo treinamento e a ordem de renegociação (Prisma, depois Vila Ipê).
- Limite [hipótese]: nenhum registro sem autorização expressa e parecer entra no próximo treino. Contrato a menos de seis meses do vencimento sem cláusula nova dispara um plano de retirada e retreino.
- Cargos e conferência:
  - Yuri Nakamura mantém o inventário por fonte.
  - Ana Beatriz Rangel (DPO) dá o parecer e pode vetar [hipótese].
  - Conflito admitido: a DPO responde também pelo jurídico [fonte: Quadro 13], então mede o andamento de uma pendência da própria área. A conferência de fora vem do cliente, na auditoria anual que o contrato do Meridiano já prevê [fonte: Quadro 7], e de um parecer jurídico externo [hipótese].
  - A CEO decide renegociar ou retirar.
- Abertura: por fonte e por contrato. Abertura por subgrupo de paciente não se aplica. Retirar o Vila Ipê pode mudar a representação de idosos e de CEP D/E, e isso vai para o indicador 1 [hipótese].
- Periodicidade: mensal até Prisma e Vila Ipê estarem regularizados, depois trimestral, junto da revisão de acessos do C5.
- Quatro perguntas:
  - Medida em quê? No inventário de contratos contra a base de treino.
  - Por quem? Pela DPO, que não depende do resultado comercial, mas responde pela pendência jurídica. Por isso a conferência vem do cliente e de parecer externo.
  - Muda alguma decisão? Sim: entrada no treino e renegociação.
  - Esconde qual distribuição? A concentração. A Sanare é 57,6% dos dados de clientes, então o indicador mostra também a parcela da maior fonte. Esconde ainda o período: um contrato pode estar em dia e não cobrir os anos anteriores à assinatura.

**Indicador 3. Reclamações formais por faixa de CEP, cruzadas com o falso negativo**
- Definição: parcela das reclamações dividida pela parcela da base, por faixa de CEP.
- Valor hoje [fonte: Quadro 17; conta]: D/E 2,54, C 0,63, A/B 0,32. Por paciente, D/E reclama cerca de 8 vezes mais que A/B. Por idade [não consta]; passa a ser registrada.
- Limites da comparação:
  - o total é pequeno: 74 reclamações em 12 meses, umas 6 por mês e 3 por quinzena [conta];
  - quem reclamou [não consta];
  - reclamação é por paciente e falso negativo é por caso a priorizar [hipótese de efeito da prevalência].
- Janela: com 3 casos por quinzena, uma regra quinzenal mede ruído. O índice usa janela móvel de 90 dias, com uns 18 casos [conta]. A cada quinzena só se faz a revisão clínica de cada reclamação nova.
- Decisão que muda: abrir revisão clínica dos casos reclamados e levar o recorte à pauta de restrição do indicador 1.
- Limite [hipótese]: índice a partir de 1,5 na janela de 90 dias.
- Cargos e conferência:
  - Registro: hoje é do time de sucesso do cliente [fonte: Quadro 17]. O cargo responsável [não consta]; provisoriamente Camila Torres (Comercial) [hipótese].
  - Yuri Nakamura cruza com o desempenho. O Head of AI Management decide a investigação (C4).
  - Conflito admitido: quem registra responde a uma área que ganha com menos reclamações [hipótese]. A conferência de fora vem do registro do próprio cliente, que recebe a queixa do paciente [hipótese: canal a definir na E3].
- Abertura: CEP e idade.
- Quatro perguntas:
  - Medida em quê? No registro formal de reclamações, que "nunca foi cruzado" com o desempenho [fonte: Quadro 17].
  - Por quem? Hoje por um time ligado ao Comercial, que tem interesse no resultado. O cliente confere pelo próprio registro.
  - Muda alguma decisão? Sim.
  - Esconde qual distribuição? Quem não reclama. Volume baixo não prova ausência de dano, e quem tem menos acesso tende a reclamar menos [hipótese].
- Contexto externo: o NIST, em MEASURE 3.3, pede que o retorno dos afetados entre nas métricas de avaliação (IND-03). A tecnovigilância da ANVISA trata queixa técnica como sinal de dano (IND-11). Se o produto for software como dispositivo médico, isso pode virar obrigação (IND-10) [hipótese].

**Indicador 4. Incidentes detectados pela Lumis antes do cliente e tempo até a correção completa**
- Definição: o tempo vai até corrigir o sistema e o material público.
- Valor hoje [fonte: Quadro 14]: 2 de 4 incidentes foram detectados por cliente, um deles levou 22 dias, um segue "em tratamento" e um está corrigido no sistema e não no material comercial desde 01/2026.
- Decisão que muda: quando o cliente detecta primeiro, revisar o monitoramento e a regra de liberação. Incidente só fecha com o material público corrigido (C1; o C5 pede "ação corretiva documentada").
- Limite [hipótese]: qualquer incidente detectado primeiro pelo cliente, ou aberto há mais de 30 dias, vai à pauta do conselho.
- Cargos e conferência:
  - O Head of AI Management (C4) registra e conduz.
  - Conflito admitido: ele mede a resposta a incidentes que ele mesmo conduz. A conferência fica com Ana Beatriz Rangel (DPO), que confere o registro, e com quem faz a auditoria interna, cargo que [não consta]. A contagem "detectado pelo cliente" pode ser conferida contra as notificações dos próprios clientes.
  - A CEO recebe o relato.
- Abertura: por tipo de incidente e pelo subgrupo afetado. Mensal.
- Quatro perguntas:
  - Medida em quê? No registro de incidentes, conferido contra as notificações recebidas dos clientes.
  - Por quem? Pelo Head of AI Management, que tem interesse em mostrar resposta rápida. Por isso a DPO e as notificações dos clientes conferem.
  - Muda alguma decisão? Sim: monitoramento e liberação.
  - Esconde qual distribuição? A gravidade e o subgrupo afetado, por isso a classificação vem junto. Também esconde o incidente que ninguém detectou.
- Contexto externo: o NIST, em MANAGE 4.1, pede planos de resposta a incidentes (IND-03). Em Michigan, os alertas de sepse foram pausados por excesso de alertas, e os autores lembram que saber desligar rápido é responsabilidade do sistema de saúde (MET-03).

**Indicador 5. Afirmações públicas auditáveis**
- Definição: parcela das afirmações do material comercial que trazem definição, população, período, intervalo de confiança, pior subgrupo e método que alguém de fora consegue refazer.
- Valor hoje: 0 de 5 [conta sobre o Quadro 11; hipótese de critério].
- Decisão que muda: o que pode ir para o material comercial. Afirmação que não passa sai.
- Limite: qualquer afirmação abaixo do critério é retirada antes da próxima apresentação ao mercado [hipótese].
- Cargos e conferência: Camila Torres (Comercial) propõe. O Head of AI Management aprova. O cliente que forneceu o dado, ou um auditor contratado, refaz o número antes da publicação [hipótese: forma de contratação a definir na E3].
- Abertura: toda métrica de desempenho publicada leva o pior subgrupo ao lado. Revisão a cada nova peça e no mínimo trimestral.
- Quatro perguntas:
  - Medida em quê? No material público contra o checklist do TRIPOD+AI (MET-07).
  - Por quem? Por quem não vende. O Head of AI Management aprova, mas responde pela imagem do próprio trabalho de gestão. Por isso o cliente ou um auditor refaz o número.
  - Muda alguma decisão? Sim: publicar ou retirar.
  - Esconde qual distribuição? A regra do pior subgrupo ainda deixa coisas de fora. Quem escolhe o recorte escolhe qual subgrupo aparece, e o Quadro 10 só abre idade e CEP. A média entre clientes pode esconder um cliente muito pior. E os usos em seguradoras e bancos ficam sem número publicado, porque o desempenho neles [não consta].
- Ligações: é a forma de medir o C1, responde ao item 3 do memorando e dá à F2-E5 a métrica pública de impacto, que deve ser o próprio falso negativo por subgrupo.

**Indicadores descartados**, além das cinco afirmações tratadas em 3.3:

| Candidato | Medida em quê? | Por quem? | Muda alguma decisão? | Esconde qual distribuição? | Destino |
|---|---|---|---|---|---|
| Acurácia global em campo (87,6%) | Base completa | [não consta] | Pouco | O falso negativo e os subgrupos | Descartado; fica só como contexto |
| "Drift" contra a versão aprovada (v1, ind. 2) | Troca de versão | Paulo Adjaí (CTO), que também libera a versão | Sim, mas repete o indicador 1 | Igual ao indicador 1 | Vira a regra de liberação do indicador 1 |
| Disponibilidade de ponta a ponta (v1, ind. 4) | Cadeia técnica | Paulo Adjaí (CTO) [hipótese] | Decisão operacional, que não chega ao conselho | Não tem abertura útil para equidade | Descartado como indicador de gestão; segue como meta técnica |
| Auditorias contratuais concluídas (v1) | Número de auditorias | Ana Beatriz Rangel (DPO) [hipótese] | Não. Mede atividade sem medir resultado | O volume de registros afetados | Absorvido pelo indicador 2, que mede registros |
| Pacientes únicos analisados (deduplicado) | Base deduplicada | Yuri Nakamura (Dados) [hipótese] | Não. É volume | Quem foi mal atendido | Descartado (vaidade; Ries, IND-12) |
| Discordância do revisor humano por subgrupo | Amostra de 2% | Quem executa a revisão [não consta] | Alimenta o indicador 1 | Depende do tamanho da amostra por subgrupo | Vira a fonte de medição do indicador 1 |

Nenhum indicador converte o falso negativo em "pacientes prejudicados por mês". A prevalência de casos a priorizar e o número de pacientes únicos [não consta]. Se a equipe quiser ordem de grandeza, a conta vai para o anexo, marcada como ilustração: com prevalência suposta de 10% [hipótese], seriam cerca de 11.300 decisões por mês com falso negativo, contra 4.700 se valesse o número da validação [conta].

### 3.5 Posição sobre o C2

O limite proposto no indicador 1 já é ultrapassado hoje, e o Compromissos_Vigentes exige decidir entre manter e revisar. A recomendação deste levantamento é **manter o C2**.

- O que a v2 recomenda: restringir já a recomendação automática nos recortes 60+ C e 60+ D/E, até a correção. O plano de contenção atual, com revisão humana obrigatória nos casos de maior impacto [fonte: Cap. 2, 1.1], não cobre a letra do C2 diante de um padrão de viés já apurado.
- Custo, que vai junto do pedido [conta; hipótese de distribuição das decisões igual à da base]: cerca de 154 mil decisões por mês, 24% do total, passam ao protocolo de triagem do próprio hospital. A revisão por amostra sobe de 12.800 para cerca de 24 mil por mês. A receita afetada e a carga em cada hospital [não consta].
- Alternativa descartada: revisar o C2 para aceitar a contenção atual. Isso exigiria nova entrada em DECISOES.md e contradiria a F2-E1, que trata o viés como trava do ativo.
- A E3 recebe só o detalhe de quem executa a restrição e com que poder. A decisão é da E2.
- A equipe precisa registrar essa posição em DECISOES.md (pendência na seção 6).

## 4. Proposta para a v2

**Tese para abrir o documento**, em duas frases curtas:
"Hoje o ativo da Lumis não passa numa auditoria independente. A parte da base que só a Lumis tem está sob contratos frágeis, e o modelo erra mais justamente com quem mais precisa de prioridade."

**Destaque**, em prosa curta, sem lista de três:
"A parte da base que só a Lumis tem são 5,9 milhões de registros de clientes. Desses, 35,4% vêm de contratos com autorização frágil, e nenhum dos seis contratos foi revisado por advogado. Em campo, de cada 10 idosos de bairros D/E que precisavam de prioridade, 3 ficaram para trás, e quem descobriu isso foi o hospital. Das cinco afirmações que a Lumis divulga, nenhuma passa numa auditoria do jeito que é divulgada."

**Pedido ao conselho**, logo abaixo: "Pedimos duas decisões agora: restringir a recomendação automática para idosos de CEP C e D/E, com o custo descrito na seção 6, e tirar do material comercial os números que não se sustentam. A regularização dos contratos e os cinco indicadores vêm com prazo e dono na mesma seção."

**Sequência de seções:**
1. Destaque: tese, resumo e pedido.
2. De onde vêm os dados e se podemos usá-los: M1, base legal, divergências de data e o que é defensável hoje.
3. O que o modelo mede de fato: M2 e o caso de proxy.
4. O que acontece em campo: M3, a mensagem desconfortável.
5. Os números que mostramos ao mercado: M4.
6. O que passamos a medir e o que decidimos agora: M5, os cinco indicadores e a posição sobre o C2.
7. O que isso muda na tese: três ou quatro linhas, com as condições prévias e as pontes para a E3 e a E5.
8. Notas e referências.

**Tabelas e figura no corpo**, no padrão da F2-E1 v2 (tabelas curtas, fonte na legenda, uma cor de destaque, no máximo cinco colunas):
- Tabela 1: fonte, volume e período, autorização, vencimento e o que trava (Quadro 7).
- Tabela 2: as variáveis de acesso e as de leitura discutível, com "diz medir", "mede de fato" e "distorção". O resto fica numa frase e no anexo.
- Figura 1: barras horizontais de falso negativo por subgrupo, com 60+ D/E em destaque e o título "Idosos de CEP D/E têm três vezes mais falso negativo que o melhor grupo". O Quadro 9 entra em duas linhas de texto.
- Tabela 3: as cinco afirmações, com o que autoriza, o que não autoriza e o destino. As quatro perguntas vão para o anexo.
- Tabela 4: os cinco indicadores, com valor hoje, decisão, limite e cargo. Abertura e conferência de fora numa nota abaixo ou no anexo.

**Anexo:**
- Tabela completa das dez variáveis e as leituras alternativas de peso (64,9%, 69,2% e 83,0%), com a base de cada uma.
- Quatro perguntas por afirmação, por indicador proposto e por indicador descartado.
- Contas de conferência, conta de amostra do indicador 1 e custo operacional da posição sobre o C2.
- Divergências do caso ("dois" contra "três"; dados anteriores à fundação; 87,2% contra 87,6%; 323 mil contra 640 mil).
- Termos técnicos usados no corpo em linguagem comum, com o nome técnico.
- Contexto externo marcado [não verificado].
- Lista do que não consta.
- Estimativa ilustrativa de falsos negativos.

**Tamanho:** de 4 a 5 páginas de corpo e de 2 a 3 de anexo [hipótese: escolha da equipe].

**Formato:** `.docx` a partir do `Modelo_Entrega_Lumis.docx`, com marcadores nos estilos Tag (D-013 a D-015). Até cinco referências externas no corpo, como na F2-E1 (D-018), todas verificadas no original. Sugestão: Obermeyer et al. (2019), Wong et al. (2021, já usada na F2-E1), LGPD, Guia de Agentes de Tratamento da ANPD e NIST AI RMF ou TRIPOD+AI.

## 5. Coerência com compromissos e com a F2-E1

| Ponto | O que a v2 precisa mostrar | Contradição a decidir |
|---|---|---|
| C1 Transparência | Manter as afirmações do Quadro 11 descumpre o dever de informar as limitações. O indicador 5 mede o C1 | Retirar as afirmações tem custo comercial. Mantê-las exigiria revisar o C1 em DECISOES.md. A v2 recomenda retirar |
| C2 Não Amplificação de Danos | O indicador 1, com leitura quinzenal, é a forma de medir o C2. O cruzamento das reclamações (indicador 3) também | Pela letra do C2, o 31,8% já é padrão de viés. A v2 mantém o C2 e recomenda restringir já os recortes 60+ C e 60+ D/E, com o custo dito (ver 3.5). Registrar em DECISOES.md |
| C5 Segurança e Privacidade | Política de saúde não aprovada, 35,4% dos dados de clientes com autorização frágil, uso de histórico anterior aos contratos, e CEP e plano no modelo diante da minimização de dados | O C5 diz "a Lumis" sem cargo. A v2 já indica a DPO como dona do indicador 2 |
| C3 e C4 | A revisão de 2% (C3) vira fonte do indicador 1, com amostra ampliada nos recortes críticos. O C4 dá ao Head of AI Management os incidentes (indicador 4) | Quem executa a revisão de 2% [não consta]. O C4 coloca o Head of AI Management como quem conduz e mede os incidentes, e a conferência pela DPO resolve o conflito |
| D-004 | O mecanismo do viés diagnosticado na Fase 1 é fato do caso [fonte: Cap. 2, 2.2, p. 8; F1-E1] | Fica como [hipótese] só a parte da equipe: quais variáveis carregam o acesso, o peso (49,8%) e como ele se divide entre idade e CEP, até os testes da Fase 3 |
| D-009 e F2-E1 v2 | Cumprir "auditoria completa" e "detalha contratos e métricas", repetir 63,6% / 9,5% / 26,8% / 35,4% e "seis instrumentos sem revisão jurídica" (D-017), e transformar "Trocar os 94%..." nos indicadores 1 e 5 | Vocabulário: a F2-E1 usa "autorização fraca" e "pendentes de revisão", e a v1 usa "frágil" e "robusta". Escolher um termo. O anexo diz "frágil ou inexistente". A F2-E1 também fala em histórico como fosso, e a v2 precisa ressalvar o período anterior aos contratos |

## 6. Decisões para a equipe e pendências

**Perguntas a decidir antes da v2:**
1. O caso de proxy principal passa a ser custo acumulado e atendimentos, com o CEP como reforço?
2. O quinto indicador é "afirmações públicas auditáveis", ou a equipe prefere manter a disponibilidade de ponta a ponta da v1?
3. Para o indicador 1, qual caminho de amostra: revisão a 10% nos recortes críticos ou janela de 90 dias com leitura quinzenal?
4. Confirmar a posição sobre o C2 (manter e restringir 60+ C e 60+ D/E já, com o custo dito) e registrá-la em DECISOES.md.
5. Marcadores: criar estilo Tag para `[cálculo]` e `[contexto externo]` (com nova entrada em DECISOES.md) ou escrever `[fonte: conta da equipe sobre o Quadro N]` com os estilos atuais?
6. Quais cinco referências externas entram no corpo? E a E2 leva apêndice de prompts? O enunciado só exige isso na E1.

**Pendências de pesquisa e conferência** (antes da v2; nenhuma fonte nova foi acrescentada aqui):
- Conferir no original, ou manter só no anexo como [não verificado]: LEG-06 (Meta, lido por resumo), MET-15 (Pieces, via escritório de advocacia), PRX-09 (PNS 2019, via Jovem Pan; conferir no IBGE), LEG-10 (CFM, fonte secundária), IND-01 (GMLP) e CON-08 (Board Intelligence), além das demais marcadas como parciais (PRX-02, PRX-07, PRX-20, LEG-07, LEG-11, MET-13, IND-12).
- Conferir na Res. CD/ANPD 4/2023 a redação exata da classificação de infração grave, com a condição de afetar significativamente interesses e direitos fundamentais dos titulares.
- Conferir o art. 52, II da LGPD no texto consolidado (teto da multa simples) e citar com data de consulta.

**O que não consta no caso e deve aparecer como `[não consta]`:**
- definição técnica de "peso", sinal de cada variável, rótulo-alvo, e se o modelo tem só dez variáveis;
- como as faixas de CEP foram construídas;
- prevalência de casos a priorizar, pacientes únicos e decisões por subgrupo;
- composição da validação de 2023 por idade e CEP, e quem a apurou;
- quem apurou a linha de campo do Quadro 9, e se toda a abertura do Quadro 10 veio do Vila Ipê;
- por que o campo tem cerca de 323 mil registros por mês contra 640 mil decisões por mês;
- a diferença entre a acurácia ponderada de 87,2% e os 87,6% do Quadro 9;
- se a Lumis recebeu histórico anterior aos contratos (Vila Ipê desde 2019, Sanare desde 2020, Prisma com contrato de 2021, antes da fundação em 2022), e sob que cláusula;
- se as condições da Sanare e do Meridiano são cumpridas, e se os dados chegam identificados ou anonimizados;
- se a Prisma é operadora de plano de saúde e como sinistros e operações bancárias entram no modelo clínico;
- se o fim do contrato obriga a retirar os dados do treino, e o custo de retreino;
- de que dados vieram os sintéticos;
- se as outras 34 das 38 contas fornecem dados para treino;
- quem consta como controlador e operador em cada contrato, e se os titulares foram informados;
- quem executa a revisão humana de 2%;
- como o NPS 72 foi calculado com 9 respondentes;
- quantidade de pessoas únicas nos 5,2 mi de registros, a data em que a duplicidade começou e a linha de base do piloto de 30%;
- quem reclamou, volume por cliente, idade nas reclamações e período da distribuição de pacientes por CEP;
- o cargo responsável pelo time de sucesso do cliente e quem faz a auditoria interna;
- faturamento exato (o Quadro 3 traz ARR e ticket médio) e receita específica de Vila Ipê e Prisma;
- carga operacional de cada hospital se a recomendação automática for restringida;
- se a Lumis tem regularização na ANVISA e se há relatório de impacto (RIPD);
- desempenho por subgrupo nos usos de seguradoras e bancos;
- data de início do prazo de 60 dias do Vetor Capital.

## 7. Referências externas verificadas

Marcação: "(parcial)" e [não verificado] indicam fonte só em parte conferida. Ela não entra no corpo nem sustenta recomendação até ser conferida no original.

**Proxies e viés**
- PRX-01 · Obermeyer Z, Powers B, Vogeli C, Mullainathan S. "Dissecting racial bias in an algorithm used to manage the health of populations". Science 366(6464):447-453, out/2019. DOI 10.1126/science.aax2342. Resumo via Europe PMC: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:31649194&resultType=core&format=json
- PRX-02 · Obermeyer Z et al. "Algorithmic Bias Playbook". Center for Applied AI, Chicago Booth, jun/2021. https://www.ftc.gov/system/files/documents/public_events/1582978/algorithmic-bias-playbook.pdf (parcial)
- PRX-03 · Nordling L. "A fairer way forward for AI in health care". Nature 573, S103, 26/09/2019. https://media.nature.com/original/magazine-assets/d41586-019-02872-2/d41586-019-02872-2.pdf
- PRX-04 · Hannan EL et al. "The Neighborhood Atlas Area Deprivation Index For Measuring Socioeconomic Status: An Overemphasis On Home Value". Health Affairs 42(5):702-709, mai/2023. DOI 10.1377/hlthaff.2022.01406
- PRX-05 · Samorani M et al. "Machine Learning and Racial Bias in Medical Appointment Scheduling". SSRN 3467047, 2019. https://scu.edu/business/isa/research/selected-publications/machine-learning-and-racial-bias-in-medical-appointment-scheduling.html
- PRX-06 · Tuan W-J et al. "Predicting Missed Appointments in Primary Care". Annals of Family Medicine 23(4):294-301, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12306982/
- PRX-07 · Agniel D, Kohane IS, Weber GM. "Biases in electronic health record data due to processes within the healthcare system". BMJ 361:k1479, abr/2018. DOI 10.1136/bmj.k1479 (parcial)
- PRX-08 · Agência Brasil. "SUS realiza seis em cada dez exames de imagem no Brasil, diz estudo", 22/09/2025 (Atlas da Radiologia no Brasil 2025). https://agenciabrasil.ebc.com.br/saude/noticia/2025-09/sus-realiza-seis-em-cada-dez-exames-de-imagem-no-brasil-diz-estudo
- PRX-09 · IBGE, PNS 2019, divulgação de 04/09/2020, lida em reprodução da Jovem Pan: https://jovempan.com.br/noticias/brasil/sete-em-cada-10-pessoas-que-procuram-servico-de-saude-vao-a-rede-publica-diz-ibge.html [não verificado; conferir no IBGE antes de citar]
- PRX-10 · Palmeira NC et al. "Análise do acesso a serviços de saúde no Brasil segundo perfil sociodemográfico: PNS 2019". Epidemiol. Serv. Saúde, 2022. https://www.scielo.br/j/ress/a/jhSpt69k9S4WNspf7Pj5pbP/?lang=en
- PRX-11 · IBGE. "Pesquisa Nacional de Saúde 2019: Percepção do estado de saúde, estilos de vida, doenças crônicas e saúde bucal", 2020. https://agenciadenoticias.ibge.gov.br/media/com_mediaibge/arquivos/6a25a69bd2bb7bdcdabd528a5bfb5f7d.pdf
- PRX-12 · Seyyed-Kalantari L et al. "Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations". Nature Medicine, 10/12/2021. DOI 10.1038/s41591-021-01595-0
- PRX-13 · World Health Organization. "Ageism in artificial intelligence for health: WHO policy brief", 09/02/2022. https://www.who.int/publications/i/item/9789240040793
- PRX-20 · TCU. "TCU avalia programa Agora Tem Especialistas do Ministério da Saúde", 24/06/2026. https://portal.tcu.gov.br/imprensa/noticias/tcu-avalia-programa-agora-tem-especialistas-do-ministerio-da-saude (parcial)

**Base legal e contratual**
- LEG-01, LEG-02, LEG-04, LEG-15 · Lei 13.709/2018 (LGPD), arts. 5º, 6º, 7º, 11, 12, 39, 42 e 52. Câmara dos Deputados. https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-publicacaooriginal-156212-pl.html (consulta em 06/10/2026; o teto da multa simples vem do art. 52, II)
- LEG-03 · Lei 13.853/2019 (art. 11, §§4º e 5º da LGPD). https://legis.senado.leg.br/norma/31172769/publicacao/31222798
- LEG-04 · ANPD. "Guia Orientativo para Definições dos Agentes de Tratamento de Dados Pessoais e do Encarregado", v2.0, abr/2022, §§ 9, 53 e 62. https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/Segunda_Versao_do_Guia_de_Agentes_de_Tratamento_retificada.pdf
- LEG-05 · Resolução CD/ANPD nº 4, de 24/02/2023 (Dosimetria). https://www.legisweb.com.br/legislacao/?id=442688 (citada só pela classificação da gravidade; conferir a redação exata do artigo antes de citar)
- LEG-06 · ANPD. Suspensão cautelar do treinamento de IA da Meta, jul/2024. https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-determina-suspensao-cautelar-do-tratamento-de-dados-pessoais-para-treinamento-da-ia-da-meta ; Mobile Time, 30/08/2024. https://www.mobiletime.com.br/noticias/30/08/2024/meta-anpd-suspende/ [não verificado; só por resumo]
- LEG-07 · ICO. "Google DeepMind and class action lawsuit" (ICO 40). https://ico.org.uk/for-the-public/ico-40/google-deepmind-and-class-action-lawsuit/ ; The Register, 03/07/2017. https://www.theregister.com/2017/07/03/google_deepmind_trial_failed_to_comply_with_data_protection_law/ ; Prismall v Google UK Ltd [2024] EWCA Civ 1516. https://caselaw.nationalarchives.gov.uk/ewca/civ/2024/1516 (parcial)
- LEG-09 · Lei Complementar 105/2001, arts. 1º e 10. https://www2.camara.leg.br/legin/fed/leicom/2001/leicomplementar-105-10-janeiro-2001-355754-publicacaooriginal-1-pl.html
- LEG-10 · Lei 13.787/2018. https://uniara.com.br/arquivos/file/comite-de-etica/leis/lei-13787.pdf ; Res. CFM 2.217/2018, art. 73, via Aurum. https://www.aurum.com.br/blog/sigilo-medico/ [não verificado; fonte secundária para o CFM]
- LEG-11 · Teletime, 30/01/2024, consulta pública da ANPD sobre anonimização. https://teletime.com.br/30/01/2024/anpd-lanca-consulta-publica-sobre-anonimizacao-de-dados/ [não verificado; só por resumo]
- DIL-03 · FTC. "FTC Finalizes Settlement with Photo App Developer Related to Misuse of Facial Recognition Technology", mai/2021. https://www.ftc.gov/news-events/press-releases/2021/05/ftc-finalizes-settlement-photo-app-developer-related-misuse
- DIL-10 · Casado M, Lauten P. "The Empty Promise of Data Moats". Andreessen Horowitz, 09/05/2019. https://a16z.com/the-empty-promise-of-data-moats/

**Métricas e auditoria**
- MET-01 · Wong A, Otles E, Donnelly JP et al. "External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients". JAMA Internal Medicine, 21/06/2021. https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307
- MET-02 · Wessler BS et al. "External Validations of Cardiovascular Clinical Prediction Models". Circ Cardiovasc Qual Outcomes, 03/08/2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8366535
- MET-03 · Wong A et al. "Quantification of Sepsis Model Alerts in 24 US Hospitals Before and During the COVID-19 Pandemic". JAMA Network Open, 19/11/2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8605481
- MET-07 · Collins GS et al. "TRIPOD+AI statement". BMJ 2024;385:e078378, 16/04/2024. https://www.tripod-statement.org/wp-content/uploads/2019/12/TRIPODAI_checklist.pdf
- MET-09 · Barnett AG, van der Pols JC, Dobson AJ. "Regression to the mean: what it is and how to deal with it". Int J Epidemiol 34(1):215-220, 2005. https://academic.oup.com/ije/article/34/1/215/638499 ; McCambridge J, Witton J, Elbourne DR. "Systematic review of the Hawthorne effect". J Clin Epidemiol 67(3):267-277, 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC3969247
- MET-11 · Lewis JR, Sauro J. "Confidence Intervals for Net Promoter Scores". MeasuringU, 05/01/2021. https://measuringu.com/?p=13651
- MET-13 · Jones C, Wilkes J, Murphy N, Smith C. "Service Level Objectives", em Site Reliability Engineering (O'Reilly/Google, 2016). https://sre.google/sre-book/service-level-objectives/ (parcial)
- MET-15 · Manatt, Phelps & Phillips. "Texas Attorney General Settles Deceptive Marketing Allegations Against Health Care AI Company", 2024. https://www.manatt.com/insights/newsletters/client-alert/texas-attorney-general-settles-deceptive-marketing [não verificado; via escritório de advocacia]

**Indicadores e monitoramento**
- IND-01 · MHRA, FDA e Health Canada. "Good Machine Learning Practice for Medical Device Development: Guiding Principles", 27/10/2021. https://www.gov.uk/government/publications/good-machine-learning-practice-for-medical-device-development-guiding-principles/good-machine-learning-practice-for-medical-device-development-guiding-principles [não verificado; parcial]
- IND-02 · FDA. "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions", 04/12/2024, revisado em 18/08/2025. https://www.fda.gov/media/166704/download
- IND-03 · NIST. "Artificial Intelligence Risk Management Framework (AI RMF 1.0)", NIST AI 100-1, jan/2023. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- IND-05 · Hardt M, Price E, Srebro N. "Equality of Opportunity in Supervised Learning". arXiv:1610.02413, 07/10/2016. https://arxiv.org/abs/1610.02413 ; Kleinberg J, Mullainathan S, Raghavan M. "Inherent Trade-Offs in the Fair Determination of Risk Scores". arXiv:1609.05807, 2016. https://arxiv.org/abs/1609.05807
- IND-06 · Rajkomar A, Hardt M, Howell MD, Corrado G, Chin MH. "Ensuring Fairness in Machine Learning to Advance Health Equity". Annals of Internal Medicine, 04/12/2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6594166/
- IND-09 · Feng J et al. "Clinical artificial intelligence quality improvement". npj Digital Medicine, 31/05/2022. DOI 10.1038/s41746-022-00611-y. https://pmc.ncbi.nlm.nih.gov/articles/PMC9156743/
- IND-10 · ANVISA. "Perguntas e Respostas RDC 657/2022, Software como Dispositivo Médico", v1, 01/09/2022, perguntas 13, 40 e 64. https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2022/software-como-dispositivo-medico-perguntas-e-respostas/perguntas-respostas-rdc-657-de-2022-v1-01-09-2022.pdf/@@download/file
- IND-11 · Resolução RDC ANVISA nº 67, de 21/12/2009 (tecnovigilância). https://www.legisweb.com.br/legislacao/?id=111582
- IND-12 · Ries E. "Vanity Metrics vs. Actionable Metrics", 19/05/2009. https://tim.blog/2009/05/19/vanity-metrics-vs-actionable-metrics/ (parcial)

**Comunicação ao conselho**
- CON-01, CON-02 · IBGC. "Código das Melhores Práticas de Governança Corporativa", 6ª ed., 2023, princípios e itens 3.17.2 e 4.5. https://idbinvest.org/en/download/20706
- CON-04 · Accenture, Microsoft e IBGC. "Guia Inteligência Artificial para conselheiros de administração", out/2024. https://msftstories.thesourcemediaassets.com/sites/42/2024/10/Guia-IA-para-Conselheiros-final.pdf
- CON-06 · Wenger S (Glass Lewis). "US AI Oversight Through Three Lenses". Harvard Law School Forum on Corporate Governance, 11/03/2026. https://corpgov.law.harvard.edu/2026/03/11/us-ai-oversight-through-three-lenses-investor-expectations-the-sp-100-and-company-specific-analysis/
- CON-08 · Board Intelligence. "How to Write Shorter Board Reports", 05/01/2026. https://www.boardintelligence.com/guide-to-shorter-papers [não verificado; parcial]
- CON-09 · Minto B. Site oficial (princípio da pirâmide). https://www.barbaraminto.com/
- CON-10, CON-11 · Government Analysis Function (UK). "Data visualisation: charts" e "Data visualisation: tables", 19/05/2022; "Communicating quality, uncertainty and change", 17/12/2018. https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/ ; https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-tables/ ; https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/
- CON-13 · Kothari SP, Shu S, Wysocki P. "Do Managers Withhold Bad News?". Journal of Accounting Research 47(1):241-276, 2009. https://ideas.repec.org/a/bla/joares/v47y2009i1p241-276.html ; Cutler J, Davis AK, Peterson K. "Disclosure and the outcome of securities litigation". Review of Accounting Studies 24(1):230-263, 2019. DOI 10.1007/s11142-018-9476-9
