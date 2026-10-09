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

### D-023 · 07/10/2026 · [Organização] F2-E5: qual expansão a due diligence analisa
O enunciado pede os riscos "no novo mercado", mas a direção de crescimento só será escolhida no memorando (F2-M). A F2-E5 analisa a expansão como o Vetor Capital a propõe (dois novos países e o Lumis Insight como plataforma) [fonte: Cap. 2, 1.1] e usa dois casos concretos do backlog: a expansão para o México e o módulo de risco de crédito para bancos [fonte: Cap. 2, Quadro 16]. Responsável pela entrega: Felipe Alef.
**Motivo:** deixar a F2-E5 útil para qualquer direção que o memorando escolher e permitir que ela aponte uma expansão arriscada demais.

### D-024 · 07/10/2026 · [Lumis] Métrica de impacto pública: falso negativo por subgrupo
A Lumis passa a publicar, a cada trimestre, a taxa de falso negativo da priorização de atendimento por subgrupo de idade e faixa de CEP, com sensibilidade, tamanho da amostra e a razão entre o pior e o melhor subgrupo. Ponto de partida: razão de 3,0 vezes (1º sem/2026). Meta proposta: até 1,5 vez em 12 meses. Publicação pelo Head of AI Management, apuração por Yuri Nakamura (Dados), auditoria independente anual. Responsáveis provisórios até a F2-E3. Detalhes em `F2-E5_Due_Diligence_ESG/F2-E5_Metrica_Publica_v1.md`.
[fonte: Cap. 2, Quadros 10 e 17; F2-E5] · Compromissos ligados: C1 e C2.
**Motivo:** é o número que originou a crise, mede o dano mais grave do produto e mostra a distribuição que a média esconde.

### D-025 · 07/10/2026 · [Organização] F2-E5 v1 montada no padrão visual
A F2-E5 v1 foi gerada por script (`F2-E5_Due_Diligence_ESG/figuras/montar_docx.py`), com a mesma base de formatação da F2-E2 v1 (a F2-E1 v2, que segue o `Modelo_Entrega_Lumis.docx`). Estrutura no formato adotado na F2-E1 (D-012): conclusão no início, cinco seções curtas, uma figura (matriz de materialidade dupla, gerada por `gerar_figuras.py`) e seis tabelas. O conteúdo vem dos quatro arquivos de apoio da pasta (`F2-E5_Materialidade_v1.md`, `F2-E5_Equidade_v1.md`, `F2-E5_Privacidade_v1.md` e `F2-E5_Metrica_Publica_v1.md`). Limites, metas e responsáveis estão marcados como propostas da equipe, e os cargos serão confirmados na F2-E3.
**Motivo:** entregar a F2-E5 no mesmo padrão das outras entregas da Fase 2.

### D-026 · 06/10/2026 · [Lumis] C2 mantido: restringir já a recomendação automática para idosos de CEP C e D/E
O compromisso C2 (Não Amplificação de Danos) fica como está. A F2-E2 v2 recomenda restringir a recomendação automática nos recortes 60+ CEP C e 60+ CEP D/E até a correção. Hoje o falso negativo deles é 2,2 e 3,0 vezes o do melhor subgrupo [fonte: Cap. 2, Quadro 10], acima do limite de 2 vezes proposto no indicador 1 [hipótese]. O modelo segue rodando em paralelo, sem decidir, para medir a correção. Custo estimado: cerca de 154 mil decisões por mês (24% do total) passam ao protocolo de triagem do próprio hospital [conta; hipótese: distribuição das decisões igual à da base]. A carga por hospital e a receita afetada não constam. A F2-E3 define quem executa a restrição e com que poder. A alternativa descartada foi revisar o C2 para aceitar a contenção atual.
[fonte: F2-E2 Levantamento v1, seção 3.5]
**Motivo:** pela letra do C2, o 31,8% já é padrão de viés, e manter o compromisso sem agir contradiria a Fase 1 e a F2-E1.

### D-027 · 06/10/2026 · [Organização] Diretrizes da F2-E2 v2 (a partir do levantamento)
- **Base:** a v1 do colega e o `F2-E2_Levantamento_v1.md`. Estrutura e tom da F2-E1 v2: tese no início, pedido ao conselho, quatro blocos na ordem do enunciado, tabelas curtas, uma figura, detalhe técnico no anexo.
- **Proxy:** o caso principal é custo acumulado e número de atendimentos, o exemplo do Cap. 2 (2.2). O CEP entra como reforço.
- **Indicadores:** cinco. (1) falso negativo por subgrupo, com a regra de liberação de versão; (2) direito de uso da base de treino; (3) reclamações por faixa de CEP cruzadas com o desempenho; (4) incidentes detectados antes do cliente; (5) afirmações públicas auditáveis. A disponibilidade de ponta a ponta sai da cesta e entra nos descartados, com as quatro perguntas.
- **Amostra do indicador 1:** revisão humana de 10% nos subgrupos críticos e janela de 90 dias com leitura quinzenal nos demais.
- **Marcadores:** sem estilo novo. Conta da equipe vira `[fonte: conta da equipe sobre o Quadro N]`, com o estilo Tag Fonte, e o contexto externo entra como referência numerada, como na F2-E1.
- **Referências no corpo:** até cinco: Obermeyer et al. (2019), Wong et al. (2021), LGPD, Guia de Agentes de Tratamento da ANPD e NIST AI RMF. Cada uma é aberta no original por alguém da equipe antes da entrega.
- **Prompts:** a F2-E2 não leva apêndice de prompts, porque o enunciado só exige na Entrega 1. O registro fica em `F2-A_Apendice_de_Prompts/F2-A_Registro_de_Prompts_F2-E2_v1.md`.
**Motivo:** a equipe aprovou as seis recomendações da seção 6 do levantamento.

### D-028 · 07/10/2026 · [Organização] F2-E2 v2 enxuta para o documento integrado
O corpo da v2 caiu de 7 para 4 páginas, e o anexo ficou em 3 páginas mais curtas. Os números saíram do corpo e foram para a Tabela A1 do anexo ("Os números por trás do texto"). O texto passa a dizer a proporção em palavras ("um terço dos dados de clientes", "de cada 10 idosos, 3"). As tabelas do corpo ficaram mais curtas: a das fontes juntou DATASUS e sintéticos, a das variáveis ficou com as quatro que medem acesso, a das afirmações tem três colunas e a dos indicadores tem quatro, com um só ponto de ação por indicador. Saíram do corpo o tamanho financeiro do risco, a nota "dois contra três", a decomposição por idade e CEP, a amostra em números e os descartados, que seguem no anexo. Entraram as três edições que a equipe fez no Word: o pedido ao conselho mais curto, Sanare e Meridiano só como "Autoriza com condição." e a base legal sem o marcador de hipótese. A versão editada pela equipe está em `_Historico/2026-10-07_F2-E2_Auditoria_do_Ativo_v2_editado-no-word.docx`.
**Motivo:** pedido da equipe para reduzir o corpo antes de consolidar o documento integrado e para comunicar as decisões com menos dados e porcentagens.

### D-029 · 07/10/2026 · [Organização] F2-E2 v2: anexo só com as quatro perguntas
O anexo da F2-E2 ficou só com as três tabelas das quatro perguntas (afirmações do mercado, indicadores propostos e indicadores descartados), que o enunciado exige. Saíram a tabela "Os números por trás do texto" e as listas de variáveis, divergências e do que não consta. Esses dados continuam no `F2-E2_Levantamento_v1.md` e no `Dados_Quadros_7-11.md`. No documento integrado, as três tabelas podem ir para a seção de matrizes de apoio. Entraram também duas edições da equipe no Word: saiu a frase sobre a queda de desempenho ser comum em IA clínica, e com ela a referência a Wong et al. (as referências passam de cinco para quatro, revendo a lista da D-027), e saiu o marcador de fonte do memorando na seção 4. A versão editada pela equipe está em `_Historico/2026-10-07_F2-E2_Auditoria_do_Ativo_v2_editado-no-word-2.docx`.
**Motivo:** a equipe escolheu manter na entrega só o anexo que o enunciado exige.

### D-030 · 07/10/2026 · [Organização] F2-E2 v2 sem anexo: as quatro perguntas no corpo
A F2-E2 deixa de ter anexo. As quatro perguntas entram no corpo, porque são exigência da própria entrega. Na seção 4, a tabela das afirmações do mercado passou a ter as quatro perguntas e o destino de cada uma (Tabela 3). Na seção 5 entraram a Tabela 5 (indicadores propostos e as quatro perguntas, com a situação de hoje) e a Tabela 6 (indicadores descartados). O documento ficou com 5 páginas no total. Substitui a parte da D-029 que mantinha as três tabelas em anexo. A versão anterior está em `_Historico/2026-10-07_F2-E2_Auditoria_do_Ativo_v2_com-anexo.docx`.
**Motivo:** a equipe entende que as quatro perguntas são análise da entrega, e não material de apoio.

### D-031 · 07/10/2026 · [Organização] F2-E2 v2: uma tabela de indicadores e sem códigos internos
- Os indicadores ficam numa tabela só (Tabela 4), com as quatro perguntas. A coluna "Muda alguma decisão?" traz a decisão concreta e o limite que a dispara. A coluna "Quem responde" saiu: quem autoriza, monitora e suspende é tema da Entrega 3. Os descartados viraram a Tabela 5.
- Saiu a frase "os pontos de ação são proposta da equipe, e os cargos são provisórios até a Entrega 3". A legenda da Tabela 4 diz que os limites são proposta da equipe.
- Saíram do texto os códigos internos (D-XX, C1, C2). Os compromissos aparecem pelo nome, com a origem na Declaração de Intenção da Fase 1.
- Entrou a edição da equipe no Word: saiu o parágrafo "Pedido ao conselho" da abertura.
Versões anteriores em `_Historico/2026-10-07_F2-E2_Auditoria_do_Ativo_v2_com-codigos-internos.docx` e `_Historico/2026-10-07_F2-E2_Auditoria_do_Ativo_v2_editado-no-word-3.docx`.
**Motivo:** a banca não tem acesso aos arquivos internos, e a E2 deve tratar só do que o enunciado pede dela.

### D-032 · 07/10/2026 · [Organização] F2-E2 v2 enxuta para o documento único, com figuras
A F2-E2 foi reescrita para entrar no documento único da fase mostrando só o essencial. O corpo caiu para cerca de 3,5 páginas. As tabelas de texto viraram figuras:
- Figura 1: composição da base, com o que é exclusivo da Lumis e o que está frágil.
- Figura 2: o que cada variável de acesso diz medir e o que mede de fato.
- Figura 3: erro em campo por grupo, a mesma de antes.
- Figuras 4 e 5: matrizes curtas com as quatro perguntas, uma para as métricas de hoje e outra para os cinco indicadores.
As respostas das matrizes têm poucas palavras. Saíram do corpo a tabela das fontes, a referência ao NIST, a revisão de 10% em parágrafo próprio e o indicador descartado "acurácia global em campo", que repetia a linha dos 94%. A "decisão de agora" vem antes da Figura 5. As figuras são geradas por `figuras/gerar_figuras_v2.py`. A versão anterior está em `_Historico/2026-10-07_F2-E2_Auditoria_do_Ativo_v2_antes-enxugar-para-documento-unico.docx`.
**Motivo:** as entregas vão para um documento único, que não pode ficar gigante, e a equipe pediu menos informação e mais figuras.

### D-033 · 07/10/2026 · [Organização] Renumeração das decisões duplicadas depois do merge da F2-E5
O merge da F2-E5 deixou duas entradas D-027, duas D-028 e duas D-029. As três mais recentes, todas da F2-E2, passaram a D-030 ("sem anexo"), D-031 ("uma tabela de indicadores e sem códigos internos") e D-032 ("enxuta para o documento único"). Na D-030, a referência "substitui a parte da D-026" virou D-029, que é a entrada do anexo depois da renumeração do merge. O texto das entradas não mudou. Versão anterior em `_Historico/2026-10-07_DECISOES_antes-renumerar-duplicadas.md`.
**Motivo:** cada decisão precisa de um número único para ser citada na Fase 7.

### D-034 · 07/10/2026 · [Lumis] Linha de responsabilidade das decisões do Lumis Insight (F2-E3)
- A CEO autoriza cada uso do sistema em cada cliente, com parecer obrigatório do Head of AI Management e da DPO. A autorização do cliente continua necessária, mas não basta.
- O CTO libera versões novas e atualizações do fornecedor. O Head of AI Management confere o teste por grupo e pode barrar a liberação.
- O responsável por Dados mede o erro por grupo e cruza as reclamações. Um auditor externo, contratado pela CEO, refaz a conta.
- O Head of AI Management acompanha os alertas e decide suspender ou restringir. O CTO e a DPO também podem suspender. O CTO executa, com o responsável por Dados como suplente. Religar exige o CTO e o Head of AI Management juntos; sem acordo, o sistema segue suspenso e a CEO leva o caso ao conselho.
- Prazo: decisão em até 24 horas e execução em mais 24 depois de confirmado o alerta, imediata com dano clínico em curso. É meta até o teste de suspensão, em até 30 dias e depois a cada trimestre.
- Alertas lidos a cada quinze dias. Priorização: grupo com o dobro do erro do melhor (F2-E2). Protocolo: o dobro de sugestões alteradas pelo médico (E3 da F2-E5). Crédito: aprovação abaixo de 80% da melhor faixa de CEP (E5 da F2-E5). Sinistro: o dobro de negativas da melhor faixa [proposta].
- Executa a D-026: o Head of AI Management ordena a restrição e o CTO executa de imediato.
- Muda a F1-E2, que dava o poder de suspender à liderança em conjunto, e amplia o C4, que dava ao Head of AI Management só a coordenação de incidentes. Os compromissos C1 a C5 ficam com o texto atual e ganham cargo: C1 com o Head of AI Management, C5 com a DPO, a leitura quinzenal do C2 com o responsável por Dados e o Head of AI Management. Confirma os cargos provisórios da D-024 e da F2-E5.
- Setor novo: portão com o responsável por Produto (leva o pedido), a CEO (decide) e o parecer do Head of AI Management e da DPO; modo sombra até haver erro medido por grupo; especialista do domínio que define erro grave; suspensão testada antes da entrada. O exemplo é o pedido do setor veterinário [fonte: Cap. 2, Quadro 16].
[fonte: Cap. 2, Quadros 12 a 16; F1-E2; F1-E3; F2-E2; F2-E5] · Compromissos ligados: C1 a C5.
**Motivo:** o enunciado pede que toda responsabilidade termine em um cargo, e hoje só a liberação de versão tem dono. Quem libera não deve ser o único que acompanha e suspende.

### D-035 · 07/10/2026 · [Organização] F2-E3 v1 enxuta e com cargos sem nome
A F2-E3 v1 foi gerada por `F2-E3_Linha_de_Responsabilidade/figuras/montar_v1.py`, com cerca de 3,5 páginas, para entrar no documento único. Os responsáveis aparecem pelo papel (CEO, CTO, DPO, Head of AI Management, responsável por Dados, Comercial e Produto), sem nome. As tabelas têm células curtas; explicações ficam no texto. O levantamento completo fica como apoio em `F2-E3_Levantamento_v1.md`.
**Motivo:** pedido da equipe: o documento único não pode ficar gigante, e a E3 deve mostrar só o essencial.

### D-036 · 07/10/2026 · [Lumis] F2-E5 alinhada à F2-E2 e à F2-E3
- O indicador E1 e a métrica pública passam a ter meta de até 1,5 vez e limite de 2 vezes. Entre 1,5 e 2 vezes, o subgrupo fica em alerta, com revisão humana de 10% dos casos. Acima de 2 vezes, a recomendação automática é restrita de imediato. Sai a espera de dois ciclos quinzenais, que contrariava a D-026. A meta de 1,5 vez da D-024 continua.
- A conferência contra os compromissos deixa de dizer que nada contradiz o C2 e registra o ajuste.
- Os cargos seguem a D-034, citados pelo papel. Os compromissos aparecem pelo nome no .docx, sem códigos internos (D-031).
- Correção da numeração: E2 (reclamações) retoma o indicador 3 da F2-E2, e P1 (direito de uso) o indicador 2.
Versão anterior em `_Historico/2026-10-07_F2-E5_Due_Diligence_ESG_v1_antes-alinhar-com-E2-E3.docx`. Responsável pela entrega: Felipe Alef, que deve revisar o ajuste.
**Motivo:** as entregas vão juntas no documento único, e o mesmo indicador não pode ter dois limites nem duas regras de suspensão.

### D-037 · 08/10/2026 · [Lumis] Pressuposto profundo do conflito entre técnico e comercial (F2-E4)
O diagnóstico de cultura da F2-E4 adota como pressuposto profundo uma crença comum às duas áreas: "Aqui, modelo validado é modelo bom: a qualidade se prova antes de o produto ir a campo, pela média, e depois disso o número vale" [hipótese]. O par do Cap. 2, 2.5 (o técnico acha que a empresa vende confiabilidade; o comercial, velocidade) fica na mesma terceira camada, como pressupostos de cada área que essa crença torna incompatíveis: se a qualidade se resolve antes, só resta brigar sobre quanto tempo validar, e sem número de campo por grupo a briga não tem árbitro. Daí o critério compartilhado [proposta]: o desempenho medido em campo, por grupo, decide o que o comercial pode prometer e o que avança no funil. As duas intervenções propostas (regra única de prova e mesa de campo quinzenal) partem desse critério. Detalhes em `F2-E4_Cultura_e_Funil_de_Inovacao/F2-E4_Levantamento_v1.md`, §4 e §5.
[fonte: Cap. 2, 1.2, 2.5 e Quadros 9 a 11, 14 e 15; F2-E1 v2, Tabela 3] · Compromissos ligados: C1 e C2.
**Motivo:** decisão da equipe. A leitura literal do capítulo não explica por que as duas áreas concordam em não saber a quem escalar um problema ético (21% a 29%) nem por que ninguém mediu o erro por grupo antes do hospital.

### D-038 · 08/10/2026 · [Lumis] Recusas, distribuição dos 30 meses-pessoa e exceção do crédito (F2-E4)
- **Recusas:** o módulo veterinário é recusado (domínio desconhecido, fora do ativo a construir, sem responsável do domínio e fora do foco da F2-E1). O agente conversacional de triagem é recusado neste ciclo, porque automatiza de novo a etapa do falso negativo de 31,8% e iria contra a restrição da D-026; volta ao portão quando a razão de falso negativo estiver em até 1,5 vez em todos os grupos e a explicabilidade estiver entregue. O México fica fora desta janela de seis meses (22 dos 30 meses-pessoa) e é reavaliado ao fim dela, com as condições da F2-E5. Juntas, as três abrem mão de R$ 11,3 mi dos R$ 19,7 mi de receita potencial listada (57,4%) [fonte: conta da equipe sobre o Quadro 16].
- **Distribuição** [proposta]: 23,4 meses-pessoa (78%) em melhoria do produto atual (compromissos já assumidos, correção do viés, explicabilidade por marco, primeira fatia do pipeline e diagnóstico da ISO/IEC 42001); 5,6 (19%) em expansão adjacente, só Descoberta e modo sombra do crédito para bancos; 1,0 (3%) em transformação, para a Descoberta da prova auditável de desempenho por subgrupo como oferta.
- **Crédito para bancos:** entra como exceção registrada ao foco da F2-E1 ("hospitais e seguradoras médios"), que não muda. Motivos: 5 bancos já clientes, 31 mil decisões por mês já em operação com revisão humana, terreno onde a Aster não chega e dado do Banco Meridiano autorizado até 05/2028, e a maior receita por mês-pessoa do backlog (R$ 0,600 mi). Segue as regras da F2-E5 para o crédito.
[fonte: Cap. 2, 2.6 e Quadros 3, 7, 10, 12 e 16; F2-E1 v2; F2-E2 v2; F2-E3 v1; F2-E5 v1] · Compromissos ligados: C2 e D-005.
**Motivo:** a equipe delegou estas escolhas. O enunciado exige pelo menos uma recusa e uma proporção justificada entre os três horizontes; 1,0 mês-pessoa em transformação responde ao terceiro horizonte e à "plataforma" do Vetor sem tirar capacidade da correção do viés. A exceção registrada evita reabrir a F2-E1.

### D-039 · 08/10/2026 · [Organização] Levantamento da F2-E4 pelo método da Fase 2
O levantamento da F2-E4 seguiu o método da D-007: sete frentes de pesquisa (três com busca na web), um verificador adversarial por frente, síntese com a skill humanizer, crítica em três leituras (professor, conselheiro e analista do Vetor Capital) e revisão. Dos 306 achados, 242 foram confirmados, 61 corrigidos e 3 ficaram de fora. Registro em `F2-A_Apendice_de_Prompts/F2-A_Registro_de_Prompts_F2-E4_v1.md` e material bruto em `apoio/F2-E4_achados_e_verificacoes.json`. As fontes externas que forem para o corpo ainda precisam ser abertas por alguém da equipe.
**Motivo:** manter a trilha de auditoria da pesquisa feita com IA, como nas entregas anteriores.

### D-040 · 08/10/2026 · [Lumis] F2-E4: demais decisões do levantamento, conforme a recomendação
A equipe pediu que as perguntas abertas da §12.3 do levantamento seguissem a recomendação:
- A mesa de campo, a leitura quinzenal por grupo e a semente do comitê de risco e ética viram um fórum só, com uma parte de risco (Head of AI Management, só parecer) e uma de produto (Responsável por Produto).
- A CEO só decide contra um parecer contrário do portão por escrito, e o caso vai ao conselho; quem pediu não vota [proposta; a composição do conselho não consta]. Estende a D-034.
- A ISO/IEC 42001 conta como melhoria do produto atual.
- O trabalho de governança já assumido (D-024, D-026, D-034, D-036) sai dos 30 meses-pessoa: 3,0 para compromissos e teto de 3,5 para a correção do viés.
- As metas de percepção são direção (pelo menos +10 pontos em 01/2027, com resultado julgado em 07/2027), com pesquisa curta aplicada por terceiro.
- Fatias de 10% (Descoberta) e mais 30% (modo sombra), e teto de 10 meses-pessoa por iniciativa sem nova decisão.
- Schein citado pela edição da editora (2017, com Peter Schein), com nota de que o curso lista 2016.
- O prazo de validação continua com o CTO, a partir da proposta da mesa. O portão da CEO vale para iniciativas que mudam decisão sobre pessoas, mercado ou setor; pipeline, explicabilidade e ISO entram pela priorização do Responsável por Produto, com parecer do Head of AI Management. Estende a D-034.
[fonte: F2-E4_Levantamento_v1.md, §5 a §7 e §12.3]
**Motivo:** fechar as escolhas antes do .docx, mantendo a linha de responsabilidade da F2-E3.

### D-041 · 08/10/2026 · [Organização] F2-E4 v1 montada no padrão visual
A F2-E4 v1 foi gerada por `F2-E4_Cultura_e_Funil_de_Inovacao/figuras/montar_v1.py`, com a mesma base da F2-E3 v1, e tem cinco páginas, três figuras (clima por grupo, funil com o que o comercial pode dizer em cada etapa e backlog contra capacidade, geradas por `gerar_figuras_v1.py`) e cinco tabelas. Cargos sem nome, compromissos pelo nome e nenhum código interno no texto. Três referências externas (Schein, Cooper e Nagji e Tuff), que alguém da equipe precisa abrir no original antes da entrega.
**Motivo:** entregar a F2-E4 no mesmo padrão das outras entregas da Fase 2, enxuta para o documento único.

### D-042 · 08/10/2026 · [Lumis] Memorando ao conselho: aceitar o aporte com condições e liberação por etapas
A equipe decidiu a direção do memorando (F2-M): recomendar ao conselho aceitar o aporte do Vetor Capital (R$ 120 mi por 22%) com liberação por etapas, ligada a condições verificáveis, e com outra ordem de uso.
- **Onde crescer:** primeiro onde a Lumis já tem cliente: hospitais e seguradoras médios no Brasil (foco da F2-E1). O novo módulo de risco de crédito para os bancos já clientes entra como exceção, só até o modo sombra (D-038). A sinalização de crédito que já roda continua.
- **Uso do aporte:** contratar em ondas, sem triplicar o time de uma vez; nenhum país novo nesta janela de seis meses (o México é reavaliado ao fim dela); da plataforma, só 1,0 mês-pessoa para testar se a prova de desempenho por grupo vira oferta.
- **Cláusula de saída:** se o Vetor exigir países ou plataforma em produção antes das condições, a recomendação é não aceitar o aporte nesses termos. Custo assumido: caixa para 11,6 meses no fechamento do 2º tri/2026 e nenhuma outra fonte de capital conhecida [não consta].
- **Condições prévias:** doze, em três prazos (cinco em até 30 dias, uma no vencimento dos contratos de dados e seis antes de cada frente nova), iguais no memorando e no fechamento do documento único. Riscos assumidos: Aster nos hospitais durante a janela, receita de que as recusas abrem mão (57,4% da listada), carga da restrição nos hospitais, renegociação dos contratos e pessoas (contratação em ondas e dependência do Responsável por Dados).
[fonte: F2-E1 a F2-E5; F2-E4_Levantamento_v1.md, §7.7 e §13; F2-Material_apoio_consolidado.md, §2] · Compromissos ligados: C1 a C5 e D-005.
**Motivo:** as cinco entregas apontam a mesma direção ("GO condicionado"). A cláusula de saída torna a recomendação verificável, e o enunciado admite recomendar não aceitar o aporte nas condições atuais.

### D-043 · 08/10/2026 · [Organização] Documento único (F2-D) e memorando (F2-M) da Fase 2
- **Dois arquivos .docx:** o documento único e o memorando, separados, porque o enunciado não diz se o memorando vai dentro do documento (Cap. 2, 4.2). O apêndice de prompts da Entrega 1 entra como Apêndice A do documento único.
- **Ordem:** a tese em uma página (as cinco perguntas do Vetor); a Entrega 5 primeiro, porque é "o capítulo que o comitê de investimento lerá primeiro" (Cap. 2, seção 4) e sem ela o comitê "não aprova operação" (Cap. 2, 1.1); depois as Entregas 1, 2, 3 e 4; um fechamento com as doze condições prévias, o uso do aporte e a coerência com a Declaração de Intenção; referências únicas; Apêndice A. As seções levam o número da entrega do enunciado (5.1, 1.1...).
- **Tamanho enxuto** (escolha da equipe): cortes de repetição entre as entregas. Saíram as figuras de ameaças e de margem da Entrega 1 e as do funil e da capacidade da Entrega 4, cujos dados estão nas tabelas; a frase sobre o que o comercial pode dizer em cada etapa passou da figura do funil para o texto. Os indicadores de equidade e de privacidade da F2-E5 aparecem pelo nome, sem os códigos E1 a E5 e P1 a P3.
- **Figuras da Entrega 2 refeitas só para o dossiê**, em `F2-D_Documento_Integrado/figuras/` (`gerar_figuras_e2_dossie.py`): ordem dos vencimentos (Prisma em 12/2026, Vila Ipê em 03/2027), citações exatas do Quadro 11, "9 respondentes", faixa de alerta do indicador 1 e cargos na coluna "Medida por quem?". As figuras e o .docx da F2-E2 não mudam.
- **Montagem por script:** `F2-D_Documento_Integrado/figuras/montar_v1.py` parte do `Modelo_Entrega_Lumis.docx`, guarda o texto final das partes e gera o documento único e o memorando.
- **Revisão:** redação por partes; sete leituras independentes (fatos em duas partes, coerência, banca, leitores do conselho e do Vetor, estilo e diagramação), com 231 achados; consolidação com conferência no Cap. 2; ajuste com passada do humanizer; conferência final de fatos, coerência e estilo; conferência de números contra as fontes, de páginas e de códigos internos.
- **As entregas individuais (.docx) ficam como estão.** A versão de envio é o documento único. Ajustes de coerência feitos só nele estão na D-044.
**Motivo:** o enunciado pede as cinco entregas articuladas num documento único, e a equipe pediu um dossiê direto, que o comitê leia começando pelo ESG.

### D-044 · 08/10/2026 · [Lumis] Ajustes de coerência entre as entregas, feitos no documento único
- **Variáveis de acesso:** vale a leitura da F2-E2 (quatro variáveis, 49,8% do peso). Sai a de cinco variáveis (55,1%) da F2-E5.
- **Indicador 1 (erro por grupo):** uma regra só em todo o dossiê, a da D-036. Acima de 1,5 e até 2 vezes o erro do melhor grupo, alerta e revisão humana de 10%; acima de 2 vezes, restrição imediata, sem esperar nova leitura. O alerta da priorização na linha de responsabilidade (D-034, "o dobro") passa a seguir essa regra. Consequência registrada: o grupo de 18 a 59 anos de CEP D/E (1,9 vez) está em alerta e entra na revisão de 10% já.
- **Reclamações:** o indicador 3 da F2-E2 e o de reclamações da F2-E5 são um só. A partir de 1,5 vez a parcela de pacientes, revisão clínica; acima de 2 vezes, auditoria de equidade. Leitura quinzenal na mesa de campo, sobre os registros dos últimos 90 dias.
- **Frequência:** os sinais de alerta do protocolo e do crédito são lidos a cada quinze dias (D-034). A F2-E5 dizia mensal.
- **Limite de cinco indicadores:** só os indicadores 1, 2 e 3 da F2-E2 contam como indicadores na Entrega 5. Reversão humana, aprovação no crédito e representatividade do novo mercado aparecem como sinais de alerta e condição de entrada.
- **Métrica pública (altera a D-024):** passa a publicar também a parcela de pacientes marcados como prioridade. A justificativa anterior (a sensibilidade impediria o jogo de marcar todos como prioridade) estava errada, porque sensibilidade e falso negativo somam 100% em todos os grupos dos Quadros 9 e 10.
- **Termos e cargos:** "seis instrumentos de dados", como no Quadro 7, no lugar de "seis contratos"; a mesa de campo inclui o Head of AI Management (D-040); a política de privacidade passa ao grupo "antes de cada frente nova"; a saída do modo sombra segue o critério do funil (quatro leituras com o pior grupo até 1,5 vez o melhor); a exceção de crédito "só até o modo sombra" vale para o módulo novo, porque a sinalização de crédito já roda (Quadro 12).
[fonte: Cap. 2, Quadros 8 a 10, 12 e 17; F2-E2 a F2-E5; D-024, D-034, D-036, D-038, D-040] · Compromissos ligados: C1, C2 e C5.
**Motivo:** as entregas foram feitas em momentos diferentes. No documento único, o mesmo indicador não pode ter dois limites, duas frequências nem duas definições.

### D-045 · 08/10/2026 · [Organização] Documento único e memorando v2: versão enxuta para quem decide
A equipe avaliou que a v1 do documento único estava correta, mas pesada para leitura: cerca de 90 marcadores no corpo (46 de fonte, 22 de hipótese e 22 de "não consta") e 21 tabelas, o que fazia o leitor perder o argumento. A v2 muda a forma e mantém todas as decisões, números, limites, cargos e condições (D-042 a D-044).
- **Corpo:** a decisão e o porquê. Cada entrega começa em página nova, abre com a conclusão e fica com uma ou duas peças principais. Corpo de 15 páginas (eram 19).
- **Origem:** uma nota na página da tese diz que todo número sobre a Lumis vem do Anexo A, com o quadro na legenda de cada figura e tabela. Sai o `[fonte]` do texto corrido; citação direta leva a seção entre parênteses.
- **Hipóteses:** marcadas só onde sustentam decisão (7 no corpo, 1 no memorando).
- **O que não consta:** reunido no quadro "O que o Anexo A não informa", no fechamento, por tema e com a seção onde pesa. Atende ao enunciado ("identificar o que falta também é resultado de análise").
- **Apêndice B (quadros de apoio):** recebe as tabelas e figuras de prova que saíram do corpo, com os marcadores originais. Também atende ao item "planilhas, matrizes ou diagramas" do 4.2, junto com a planilha das contas, ainda pendente.
- **Memorando:** mesma estrutura, com 1 marcador (eram 11) e as fontes numa nota final.
- **Histórico:** v1 do documento único (com a correção feita no Word pela equipe, "Porque" no lugar de "Por que"), v1 do memorando e o script da v1 em `_Historico/2026-10-08_*`. Na v2 a frase sobre os idosos foi para o quadro do que não consta e manteve "Por que", que é a forma correta em pergunta indireta.
[fonte: pedido da equipe em 08/10/2026; Cap. 2, 4.2 e texto antes da Entrega 1] · Compromissos ligados: nenhum alterado.
**Motivo:** o conselho e o comitê do Vetor precisam decidir lendo o corpo em poucos minutos; a prova continua no documento, no apêndice.

### D-046 · 08/10/2026 · [Organização] "Teste em paralelo" no lugar de "modo sombra"; memorando v3 e documento único v3
- **Termo:** "modo sombra" (tradução de *shadow mode*, jargão de engenharia de ML) sai do documento único e do memorando. Entra "teste em paralelo": o sistema roda junto ao processo atual, sem decidir. A etapa do funil passa a se chamar "Teste em paralelo"; as regras (fatia de até mais 30%, quatro leituras quinzenais com o pior grupo até 1,5 vez o melhor, encerramento com seis leituras acima de 2 vezes) não mudam. "Piloto" foi descartado porque costuma indicar uso real em pequena escala. Os levantamentos e as decisões anteriores (D-038 a D-041) ficam com o termo antigo, que equivale ao novo.
- **Memorando v3:** parte da v2 editada no Word pela equipe (Aster, seguradoras e bancos; fase de teste do crédito; tabela de riscos reescrita). Condições prévias em tabela (condição, responsável e prazo); o pedido ao conselho sobe para o primeiro parágrafo; o uso do aporte vira uma frase; 2 páginas.
- **Documento único v3:** o termo novo, a explicação de por que a Aster não chega a seguradoras e bancos (14 das 38 contas da Lumis) e a condição 12 com o mesmo texto do memorando.
[fonte: pedido da equipe em 08/10/2026] · Compromissos ligados: nenhum alterado.
**Motivo:** o leitor do conselho não conhece o termo técnico; memorando e documento único precisam usar o mesmo nome.

### D-047 · 08/10/2026 · [Lumis] Limites de equidade apresentados como proposta da equipe; sai a meta de 7,4%
- **Métrica pública (seção 5.4):** a ficha passa a ter limite (o dobro do erro do melhor grupo) e meta (1,5 vez em 12 meses), os dois marcados como proposta da equipe, com a justificativa do dobro. Sai a meta de 24 meses de nenhum grupo acima de 7,4%: o número é do caso (validação declarada, Quadro 9), mas usá-lo como meta foi ideia da equipe e acrescentava mais um nível. Saem também "sensibilidade" (é 100% menos o erro) e "valor do período anterior". Continua a publicação da parcela marcada como prioridade (D-044).
- **Seção 5.2:** cada indicador diz o valor de hoje e o limite, com remissão à 5.4; a faixa de revisão de 10% fica no Apêndice B e nas seções 3.3 e 3.4.
- **Crédito:** "0,8 da melhor" passa a "80% da melhor", como proposta da equipe e sem citar a regra americana.
- **Apêndice B:** nova tabela "De onde vem cada número", que separa o que é do caso, o que é conta da equipe e o que é proposta da equipe.
- Os limites e regras da D-036 e da D-044 não mudam; muda a forma de apresentar. O memorando já diz que metas e limites são propostas da equipe e não tem a meta de 7,4%; fica como está.
[fonte: pedido da equipe em 08/10/2026; Cap. 2, Quadros 9, 10, 12 e 17] · Compromissos ligados: Não Amplificação de Danos e Transparência (texto sem mudança).
**Motivo:** os limites pareciam regras do caso. Separar o que é dado do que é proposta torna a seção mais clara e mais honesta.
