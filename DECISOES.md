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

### D-012 · 06/10/2026 · [Organização] F2-E1 v2 reescrita como relatório ao conselho
A equipe achou a v2 técnica demais, com dados em excesso e estrutura de texto gerado por IA. O mapa foi reescrito para o conselho, em torno de uma tese ("quase tudo o que faz o Lumis Insight funcionar é alugado, e o único ativo que poderia ser da Lumis ainda não é dela"), contada em quatro passos que se encadeiam: onde a Lumis está, quem pode tomar esse espaço, o que pode mudar sem ela decidir e o que é difícil de copiar. A conclusão abre o texto e não se repete no fim. Saem do corpo a síntese consolidada, os desdobramentos e as tabelas de camadas e de participantes. Ficam a tabela de dependências e a de veredito, que guardam os números. O arquivo continua com o nome v2, a pedido da equipe. Na voz do texto, os contratos de dados aparecem como "pendentes de revisão". A versão anterior está em `_Historico/2026-10-06_F2-E1_Mapa_do_Territorio_v2_antes-storytelling.docx`.
**Motivo:** dar coesão ao texto e deixar no corpo só os números que mudam a conclusão.

### D-013 · 06/10/2026 · [Organização] Design system dos documentos
Os documentos da equipe passam a seguir o design system em `00_Lumis/Design_System/`: logo do Lumis Insight (anel azul aberto com um ponto de luz âmbar), paleta Noite `#1F3A5F` e Lúmen `#E8A33D`, Georgia nos títulos e Calibri no texto, cores fixas para os marcadores `[fonte]`, `[hipótese]`, `[não consta]` e `[risco]`, e o Feixe (arcos concêntricos) como artefato visual da capa. O ponto de partida de cada entrega é `Modelo_Entrega_Lumis.docx`. Vale a partir da F2-E2. As entregas já feitas não precisam ser refeitas. O Cap. 1 e o Cap. 2 não trazem identidade visual da Lumis; tudo foi criado pela equipe.
**Motivo:** pedido da equipe para dar um padrão visual simples aos documentos.

### D-014 · 06/10/2026 · [Organização] Design system com paleta de saúde (substitui as cores de D-013)
A paleta azul-noite e âmbar de D-013 sai. Entram três cores, uma para cada voz do produto: Vital `#3DBE93` (saúde), Profundo `#0F2D3A` (dados) e Pulso `#2BA6C9` (inovação), com Vital escuro `#1E8C6B` para texto. O logo ganhou um ponto Pulso saindo pela abertura do anel, e o Feixe ganhou uma linha de pulso que vira pontos de dado. O verde se inspira no tom de saúde da Arkium sem copiá-lo. Tipografia, marcadores e modelo de entrega seguem como em D-013. A versão anterior está em `_Historico/2026-10-06_Design_System_v1_azul-ambar/`.
**Motivo:** pedido da equipe para uma cor que lembre saúde e para uma identidade que misture saúde, dados e inovação.

### D-015 · 06/10/2026 · [Organização] Capa revista e padrão visual obrigatório
O Feixe da capa foi redesenhado para parecer menos artificial: fundo com brilho suave e grão, arcos com espaçamento crescente e alguns pontilhados, e um batimento cardíaco desenhado como curva, cujas repetições viram pontos de dado do verde ao ciano. O desenho sai de `_fonte/gerar_feixe.py`. O CLAUDE.md passou a exigir que todo material gerado no LumisOS siga o design system. A versão anterior da pasta está em `_Historico/2026-10-06_Design_System_v2_verde-capa-geometrica/`.
**Motivo:** a equipe gostou da identidade e achou a capa artificial demais, e pediu que o padrão valha para tudo o que for gerado.

### D-016 · 06/10/2026 · [Organização] Contexto antes da entrega e conversa passo a passo
O CLAUDE.md passou a exigir que, em todo chat novo sobre uma entrega, o Claude leia o README da fase e o da entrega, o trecho do enunciado com os objetivos e critérios, o contexto da Lumis em `00_Lumis/` e as decisões ligadas, e resuma à equipe o que entendeu antes de começar. A conversa vai passo a passo, com uma pergunta por vez (no máximo duas), aviso antes de gerar ou alterar arquivo e explicação simples do que foi feito. A versão anterior do CLAUDE.md está em `_Historico/2026-10-06_CLAUDE_antes-regras-de-entrega.md`.
**Motivo:** pedido da equipe para que cada entrega comece pelo enunciado e pelo contexto da Lumis, e para que a interação seja mais fácil de acompanhar.

### D-017 · 06/10/2026 · [Organização] F2-E1 v2 no padrão visual e com figuras
A pedido da equipe, que achou o texto longo demais, a F2-E1 v2 foi refeita a partir do `Modelo_Entrega_Lumis.docx`. Ela ganhou cinco figuras: camadas, direções de ameaça, prazos das dependências, margem por cenário e a escala do que é difícil de copiar. As figuras ficam em `F2-E1_Mapa_do_Territorio/figuras/`, com os scripts que as geram e que montam o .docx. As tabelas de camadas e de participantes saíram, e a de dependências virou a Tabela 1. O Apêndice A passa a dizer que a IA apoiou a pesquisa e a redação, com revisão e reescrita final da equipe. Na mesma revisão foi corrigido um dado: o Cap. 2 (Quadro 7) diz que os seis instrumentos de dados estão sem revisão jurídica, e não os 38 contratos. Esta entrada abre uma exceção pontual à regra do CLAUDE.md de deixar a F2-E1 como está. A versão anterior está em `_Historico/2026-10-06_F2-E1_Mapa_do_Territorio_v2_antes-design.docx`.
**Motivo:** reduzir o texto, mostrar os dados como figura e alinhar a entrega ao design system.

### D-018 · 06/10/2026 · [Organização] F2-E1 v2 enxuta, a partir dos ajustes da equipe
A nova versão parte da que a equipe ajustou: capa só com título e subtítulo e "nosso stakeholder" no lugar de "gestor". Ela tem menos texto, mais tópicos e menos citações. As referências caíram de 10 para 5 (MV/KLAS, Einstein, Wong et al., TechCrunch e Shapiro e Varian). As fontes do caso agora ficam nas legendas e na nota final. A Tabela 1 passou a ter três colunas: dependência, o que pode acontecer e resposta recomendada. As figuras não mudaram. A versão da equipe está em `_Historico/2026-10-06_F2-E1_Mapa_do_Territorio_v2_ajustes-equipe.docx`.
**Motivo:** pedido da equipe por um documento mais curto e objetivo.

### D-019 · 06/10/2026 · [Organização] F2-E1 v2: menos figuras, mais tabelas
Saíram a figura da linha do tempo e a da escala do que é difícil de copiar. Os prazos viraram a coluna "Prazo" da tabela de dependências, agora Tabela 2. A escala foi substituída por uma figura simples de três faixas (passivo, copiável ou parcial, difícil de copiar), no mesmo desenho da Figura 1. As ameaças da seção 2 passaram de tópicos para a Tabela 1, que ganhou a coluna "O que joga a favor da Lumis". As seções agora alternam figura, tópicos e tabela. Os arquivos das figuras antigas continuam em `figuras/`, sem uso no documento. A versão anterior está em `_Historico/2026-10-06_F2-E1_Mapa_do_Territorio_v2_antes-tabelas.docx`.
**Motivo:** pedido da equipe, que acha que as tabelas ajudam a visualizar e que a figura da escala não funcionou.

### D-020 · 06/10/2026 · [Lumis] F2-E1 v2: ameaças completas, risco atual dos dados e por que a base ainda não é fosso
- **Ameaças:** a Tabela 1 passou de 4 para 7 linhas. A linha "fornecedor de modelo" virou "os próprios fornecedores", com nuvem e bases como [hipótese]. Núcleo e consultorias ficaram em linhas separadas, e entraram birôs e plataformas de dados (bancos e seguros) e healthtechs de IA clínica [hipótese]. A Figura 2 foi atualizada para bater com a tabela.
- **Risco dos dados:** o risco existe hoje, e não só nos vencimentos. O modelo já foi treinado com os 35,4% de dados de clientes com autorização fraca (Vila Ipê e Prisma), nenhum dos seis instrumentos passou por revisão jurídica, as autorizações da Sanare e do Meridiano têm condições, e a base legal da LGPD para dado de saúde é incerta [hipótese] [fonte: Cap. 2, Quadro 7].
- **Difícil de copiar:** a faixa "Passivo hoje" virou "Valioso, mas travado hoje". A Tabela 3 mostra a composição da base (63,6% pública, 9,5% sintética, 26,8% de clientes). A seção lista as quatro travas dos dados de clientes (autorização, concentração, escala e viés) e explica que os "4 anos" medem a experiência da equipe. O histórico de 2019 a 2026 pode ser o fosso, se os contratos forem regularizados e o viés corrigido [hipótese].
Versões anteriores em `_Historico/2026-10-06_F2-E1_Mapa_do_Territorio_v2_antes-ameacas.docx` e nas figuras `2026-10-06_F2-E1_fig*.png`.
**Motivo:** a equipe não via com clareza o risco dos contratos de dados nem por que a base histórica não é difícil de copiar.

### D-021 · 06/10/2026 · [Organização] F2-E1 v2: a Figura 4 vira tabela e entram as edições da equipe no Word
A figura de faixas do "difícil de copiar" virou a Tabela 3, com as colunas "Hoje", "Elemento" e "Por quê". A tabela da composição da base passou a ser a Tabela 4. A versão gravada incorpora as edições que a equipe fez no Word: saíram da Tabela 1 as linhas de birôs de dados e de healthtechs, a legenda ficou mais curta e saiu o marcador [hipótese] da recomendação de modelo próprio. A Figura 2 voltou a mostrar só Núcleo e consultorias no grupo "por fora". O arquivo editado pela equipe está em `_Historico/2026-10-06_F2-E1_Mapa_do_Territorio_v2_editado-no-word.docx`.
**Motivo:** a figura não funcionou, e a tabela é mais clara.

### D-022 · 06/10/2026 · [Organização] F2-E1 v2: formatação da Tabela 3
A Tabela 3 ("difícil de copiar") ganhou células de nível mescladas e cor de fundo por grupo, seguindo a paleta: âmbar para "valioso, mas travado" e Papel com texto Vital escuro para "difícil de copiar". O "destrava com…" passou para uma linha própria, em itálico. A equipe tinha começado a mesclar células no Word, e essa versão está em `_Historico/2026-10-06_F2-E1_Mapa_do_Territorio_v2_editado-no-word-2.docx`; a nova formatação cobre essa edição.
**Motivo:** pedido da equipe por uma Tabela 3 mais legível.

### D-023 · 06/10/2026 · [Lumis] C2 mantido: restringir já a recomendação automática para idosos de CEP C e D/E
O compromisso C2 (Não Amplificação de Danos) fica como está. A F2-E2 v2 recomenda restringir a recomendação automática nos recortes 60+ CEP C e 60+ CEP D/E até a correção. Hoje o falso negativo deles é 2,2 e 3,0 vezes o do melhor subgrupo [fonte: Cap. 2, Quadro 10], acima do limite de 2 vezes proposto no indicador 1 [hipótese]. O modelo segue rodando em paralelo, sem decidir, para medir a correção. Custo estimado: cerca de 154 mil decisões por mês (24% do total) passam ao protocolo de triagem do próprio hospital [conta; hipótese: distribuição das decisões igual à da base]. A carga por hospital e a receita afetada não constam. A F2-E3 define quem executa a restrição e com que poder. A alternativa descartada foi revisar o C2 para aceitar a contenção atual.
[fonte: F2-E2 Levantamento v1, seção 3.5]
**Motivo:** pela letra do C2, o 31,8% já é padrão de viés, e manter o compromisso sem agir contradiria a Fase 1 e a F2-E1.

### D-024 · 06/10/2026 · [Organização] Diretrizes da F2-E2 v2 (a partir do levantamento)
- **Base:** a v1 do colega e o `F2-E2_Levantamento_v1.md`. Estrutura e tom da F2-E1 v2: tese no início, pedido ao conselho, quatro blocos na ordem do enunciado, tabelas curtas, uma figura, detalhe técnico no anexo.
- **Proxy:** o caso principal é custo acumulado e número de atendimentos, o exemplo do Cap. 2 (2.2). O CEP entra como reforço.
- **Indicadores:** cinco. (1) falso negativo por subgrupo, com a regra de liberação de versão; (2) direito de uso da base de treino; (3) reclamações por faixa de CEP cruzadas com o desempenho; (4) incidentes detectados antes do cliente; (5) afirmações públicas auditáveis. A disponibilidade de ponta a ponta sai da cesta e entra nos descartados, com as quatro perguntas.
- **Amostra do indicador 1:** revisão humana de 10% nos subgrupos críticos e janela de 90 dias com leitura quinzenal nos demais.
- **Marcadores:** sem estilo novo. Conta da equipe vira `[fonte: conta da equipe sobre o Quadro N]`, com o estilo Tag Fonte, e o contexto externo entra como referência numerada, como na F2-E1.
- **Referências no corpo:** até cinco: Obermeyer et al. (2019), Wong et al. (2021), LGPD, Guia de Agentes de Tratamento da ANPD e NIST AI RMF. Cada uma é aberta no original por alguém da equipe antes da entrega.
- **Prompts:** a F2-E2 não leva apêndice de prompts, porque o enunciado só exige na Entrega 1. O registro fica em `F2-A_Apendice_de_Prompts/F2-A_Registro_de_Prompts_F2-E2_v1.md`.
**Motivo:** a equipe aprovou as seis recomendações da seção 6 do levantamento.

### D-025 · 07/10/2026 · [Organização] F2-E2 v2 enxuta para o documento integrado
O corpo da v2 caiu de 7 para 4 páginas, e o anexo ficou em 3 páginas mais curtas. Os números saíram do corpo e foram para a Tabela A1 do anexo ("Os números por trás do texto"). O texto passa a dizer a proporção em palavras ("um terço dos dados de clientes", "de cada 10 idosos, 3"). As tabelas do corpo ficaram mais curtas: a das fontes juntou DATASUS e sintéticos, a das variáveis ficou com as quatro que medem acesso, a das afirmações tem três colunas e a dos indicadores tem quatro, com um só ponto de ação por indicador. Saíram do corpo o tamanho financeiro do risco, a nota "dois contra três", a decomposição por idade e CEP, a amostra em números e os descartados, que seguem no anexo. Entraram as três edições que a equipe fez no Word: o pedido ao conselho mais curto, Sanare e Meridiano só como "Autoriza com condição." e a base legal sem o marcador de hipótese. A versão editada pela equipe está em `_Historico/2026-10-07_F2-E2_Auditoria_do_Ativo_v2_editado-no-word.docx`.
**Motivo:** pedido da equipe para reduzir o corpo antes de consolidar o documento integrado e para comunicar as decisões com menos dados e porcentagens.

### D-026 · 07/10/2026 · [Organização] F2-E2 v2: anexo só com as quatro perguntas
O anexo da F2-E2 ficou só com as três tabelas das quatro perguntas (afirmações do mercado, indicadores propostos e indicadores descartados), que o enunciado exige. Saíram a tabela "Os números por trás do texto" e as listas de variáveis, divergências e do que não consta. Esses dados continuam no `F2-E2_Levantamento_v1.md` e no `Dados_Quadros_7-11.md`. No documento integrado, as três tabelas podem ir para a seção de matrizes de apoio. Entraram também duas edições da equipe no Word: saiu a frase sobre a queda de desempenho ser comum em IA clínica, e com ela a referência a Wong et al. (as referências passam de cinco para quatro, revendo a lista da D-024), e saiu o marcador de fonte do memorando na seção 4. A versão editada pela equipe está em `_Historico/2026-10-07_F2-E2_Auditoria_do_Ativo_v2_editado-no-word-2.docx`.
**Motivo:** a equipe escolheu manter na entrega só o anexo que o enunciado exige.
