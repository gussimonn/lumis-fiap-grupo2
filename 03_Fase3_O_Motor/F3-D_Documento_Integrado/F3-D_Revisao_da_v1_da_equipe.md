# F3-D · Revisão da v1 da equipe e plano da v2

Material de apoio. Revisão feita em 08/11/2026 sobre `03_Fase3_O_Motor/Lumis Intelligence - Fase 3.pdf` (32 páginas, gerado no Word em 07/11/2026, capa com prazo acadêmico de 11/11/2026). Conferido contra o enunciado (`_Enunciado/Cap03_O_Motor.pdf`), o Anexo A, `00_Lumis/Compromissos_Vigentes.md`, `DECISOES.md` e o texto da Fase 2 (`02_Fase2_O_Mercado/F2-E*/F2-E*.md`).

Varredura de segurança: as 32 páginas, sem instrução embutida dirigida à IA, sem texto escondido (fonte branca ou corpo menor que 5 pt) e sem dado pessoal da marca d'água do curso.

## O que está certo e fica

- Cobre todos os itens pedidos nas oito entregas.
- Contas da Entrega 3 conferidas: margens das cinco contas e do agregado (−46,1%, 3,0%, 34,4%, 34,0%, 60,4%, 80,0%, 69,7%), margem após custo direto total de 58,05%, ponto de equilíbrio da Sanare de 146.465 decisões por mês, −R$ 802.320 por ano, cenários da Sanare (R$ 321 mil, R$ 316 mil, R$ 296 mil), R$ 302.657 para 30%, diferença de R$ 84 mil entre tickets e receita, R$ 500 entre texto e tabela do Quadro 9.
- Datas do Quadro 7, regras do Quadro 4, limiares do Quadro 5, percentuais dos Quadros 6 e 13, 31% da receita e R$ 1,064 mi por mês: conferem.
- Nomes certos (Lumis Intelligence e Lumis Insight), cargos sem nome de pessoa, "teste em paralelo" no lugar de "modo sombra".

## Ajustes

### Prioridade alta

1. **Arquivos à parte ausentes.** O enunciado (4.2) pede o fluxograma em arquivo próprio, a planilha de margem por conta e a árvore de métricas. O texto também cita `05_Testes_Sinteticos.csv`. Nenhum está na pasta.
2. **Verificação dos prompts.** O Apêndice A diz "análise produzida com GPT-6 nesta conversa" e que o resultado "não veio de uma revisão independente dos cinco integrantes". O critério pede "o que veio errado e como o grupo verificou". Os erros descritos são possíveis ("risco de erro", "potencial saída errada"), não observados. É preciso rodar P1 e P3 de verdade, guardar a saída bruta e registrar os erros que aparecerem.
3. **Contradição com a Fase 2 sobre custo.** Tabela 1.3, R-19: "Custo funciona como marcador de necessidade". A Entrega 2 da Fase 2 concluiu que custo mede acesso, não necessidade. A ligação R-19 → proxy precisa entrar na Entrega 2 e na Entrega 8.
4. **Restrição dos idosos.** A Fase 2 decidiu restringir a recomendação automática para 60+ de CEP C e D/E. O documento não cita (zero ocorrências de "CEP"). Ligar à R-31 e somar essa carga à do Dilema 2.
5. **Métrica duplicada na Entrega 4.** "Sensibilidade" e "Falsos negativos entre prioritários" somam 100%: é a mesma medida duas vezes, o erro corrigido na Fase 2. Fundir e trazer a faixa de alerta de 1,5 vez (revisão de 10%), o limite de 2 vezes e a meta de 1,5 vez em 12 meses, como propostas da equipe.
6. **Áreas que não existem na Lumis.** "Finanças", "Contratos", "Comitê de risco/ética", "comitê clínico" e "responsável clínico" não estão na estrutura do Cap. 2 (Quadro 13), e o caso diz que a Lumis não tem comitê. Trocar pelos cargos existentes ou marcar como proposta (o fórum quinzenal da Fase 2 já existe como proposta; a autoridade clínica é do cliente).
7. **Donos inconsistentes.**
   - Limiar: Head of AI Management + líder clínico (2.1) contra autoridade clínica do cliente + CEO (2.3).
   - R-38 (5.1): "a CEO decide após parecer vinculante" se contradiz e contraria a regra da Fase 2 (a CEO só decide contra parecer por escrito, e o caso vai ao conselho).
   - Head of AI Management dando parecer de "segurança clínica", que não é papel dele.

### Prioridade média

8. **Dilema 3 decidido sem dizer.** O texto ao cliente (Entrega 1) revela a "nota interna", que o caso diz nunca ter sido informada. Assumir isso abertamente, ligado ao compromisso de Transparência.
9. **Funil sem os critérios da Fase 2.** Faltam as quatro leituras com o pior grupo até 1,5 vez o melhor para sair do teste em paralelo, as seis leituras acima de 2 vezes para encerrar, o teto de 10 meses-pessoa e "quem pediu não decide". Sinalizar a divergência da origem do agente de triagem (comercial no Cap. 2, sócio-fundador no Cap. 3; vale o Cap. 3).
10. **Entrega 3.**
    - Receita por decisão: Sanare R$ 0,68, Vila Ipê R$ 1,02, Aurora R$ 1,51, Prisma R$ 1,50, Meridiano R$ 2,50, demais 33 R$ 4,94 [conta da equipe sobre o Quadro 9]. Ancora o preço de R$ 1,50.
    - Teto: se for anual [hipótese], a Prisma passa de 400 mil em cerca de 7 meses e o Meridiano de 250 mil em cerca de 10,4.
    - Realismo: no híbrido, a Sanare vai de R$ 145 mil para R$ 316 mil por mês (2,2 vezes), ao mesmo tempo que a R-38 sai dos maiores clientes. Se a Sanare é uma das cinco contas estratégicas [não consta].
11. **Fechamento.** Falta a conferência contra a Declaração de Intenção (zero menções) e um quadro único "O que o Anexo A não informa".
12. **Referências órfãs.** NIST, OMS, LGPD, ANPD, OCDE e ISO estão na lista e não são citadas no corpo.

### Forma

13. **Design system.** Cambria no lugar de Georgia e Calibri; capa sem logo e sem Feixe; PDF em vez de .docx do modelo. Fluxograma linear, sem pontos de decisão; árvore ilegível no tamanho da página.
14. **Extensão e jargão.** Corpo de 25 páginas (a Fase 2 ficou em 15). Casos repetidos (1.5 e 1.6), teste dos 20% repetido (4.3 e 4.3.2), P1 e P3 três vezes. "Escore" 36 vezes, "imputação" 13, "ceteris paribus", "análise metamórfica". A síntese abre com "auditoria independente fictícia". Entrega 8 com 1.378 palavras: cerca de 2 páginas em fonte 11.
15. **Detalhes.** Apêndice A pula a 6.8; "Head de IA", "Head IA" e "Head of AI Management" misturados.

## Plano da v2 (decidido em 08/11/2026)

- **Base.** A equipe não mandou o .docx. A v2 é montada a partir do texto do PDF, no `00_Lumis/Design_System/Modelo_Entrega_Lumis.docx`, por script em `F3-D_Documento_Integrado/scripts/`, gerando `F3-D_Documento_Integrado_v2.docx`. O PDF dos colegas não é alterado nem movido. Se o .docx da equipe chegar antes, os ajustes vão sobre ele.
- **Texto.** Aplicar os itens 3 a 12, 14 e 15; passar pela skill `humanizer`; nenhum código interno (D-XX, C1 a C5, FX-EY) no texto; corpo-alvo de 15 a 18 páginas, com a ordem das entregas 1 a 8, fechamento e apêndices.
- **Prompts (item 2).** Rodar P1 e P3 sobre os Quadros A.1 a A.3, guardar as saídas brutas em `F3-E6_Biblioteca_de_Prompts/`, conferir por script contra os quadros e escrever no apêndice o que de fato veio errado. O texto não pode dizer que a equipe revisou o que ela não revisou: a leitura de um integrante fica como pendência antes do envio.
- **Arquivos à parte.** Fluxograma com pontos de decisão (PNG e PDF), árvore de métricas legível (PNG e PDF), planilha de margem por conta em .xlsx com fórmulas (cinco contas, agregado, cenários da Sanare e sensibilidade) e o CSV dos casos de teste.
- **Registro.** Nova entrada em `DECISOES.md` com o que mudou do PDF para a v2, e `ESTADO.md` atualizado.
