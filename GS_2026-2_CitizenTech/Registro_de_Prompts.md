# Prosa · Registro de prompts da GS (material de apoio)

> Ferramenta: Claude (Anthropic), em sessão do Claude Code com busca na web, em 17/11/2026. Responsável pela sessão: Felipe Alef.
> O anexo A4 do deck resume este registro. Aqui fica o que foi pedido, o que voltou e o que foi corrigido.

## Contexto dado à IA

- Enunciado da GS: `_Enunciado/1TGIOR_Fase4_Global_Solutions_2026-2.pdf`.
- Escolhas da equipe, respondidas em pergunta da IA: tema "pequeno produtor" (assistente por WhatsApp e áudio para a agricultura familiar) e escopo "deck completo em PDF e roteiro do vídeo; a gravação fica com o grupo".
- Padrões do repositório: `CLAUDE.md`, design system em `00_Lumis/Design_System/` e escrita pela skill `humanizer`.

## Buscas e verificações

| # | Busca (texto usado) | O que voltou | O que fizemos |
|---|---|---|---|
| P1 | "Censo Agropecuário 2017 agricultura familiar 3,9 milhões estabelecimentos 77% orientação técnica IBGE" | 3.897.408 estabelecimentos familiares (77%); a orientação técnica não era 77% e sim 20,1% a 20,2% | Corrigida a hipótese; usado 20,2% (Atlas do Espaço Rural, IBGE) |
| P1b | "Censo Agropecuário 2017 percentual estabelecimentos receberam assistência técnica 20%" | 20,2% (Atlas IBGE), 20,1% (produtores), 19,9% (outra tabulação) | Usado 20,2% e anotada a diferença de denominador |
| P1c | "Censo Agropecuário 2017 orientação técnica produtores pretos 9,57% pardos 10,83% brancos 31,12%" | Confirmado na Agência de Notícias do IBGE; indígenas 8,4% | Usado no slide 2 e no slide 11 |
| P1d | "agricultura familiar 10 milhões pessoas ocupadas 67% Censo Agro 2017" | 10,1 milhões, 67% do total (IBGE) | Usado no slide 2 |
| P1e | "TIC Domicílios 2024 área rural acesso internet percentual WhatsApp Cetic.br" | 76% da população rural usa internet; 82% dos rurais conectados usam só o celular; dado específico de WhatsApp não encontrado | Usado 82%; não afirmamos percentual de uso do WhatsApp |
| P1f | "perdas agricultura eventos climáticos extremos Brasil prejuízo bilhões CNM seca estiagem 2024" | R$ 6,7 bi no agro até ago/2024 (CNM), números parciais | Usado como "ao menos" e "até agosto" |
| P1g | "Embrapa ZARC Plantio Certo aplicativo zoneamento agrícola risco climático produtor" | App gratuito, ~15 mil ativos (2021); adoção do Zarc evitou R$ 8,7 bi (2021) | Usado para mostrar a distância entre informação e uso |
| P2 | "WhatsApp Business Platform preço Brasil 2025 mensagem de utilidade conversa de serviço gratuita por mensagem" | Só fontes de terceiros; R$ 0,035 a R$ 0,05; mudança de regra das mensagens de serviço em datas divergentes | Usado R$ 0,04 com a incerteza declarada no anexo A1 |
| P3 | "PL 2338/2023 inteligência artificial aprovado Senado dezembro 2024 classificação alto risco tramitação Câmara 2026" | Aprovado no Senado em 10/12/2024; comissão especial na Câmara sem votação até a data das fontes | Citado como "aprovado no Senado, em análise na Câmara" |
| P4 | "Lei 14.785/2023 agrotóxicos receituário agronômico obrigatório profissional habilitado" | Receituário por profissional habilitado; Resolução Confea 1.149/2025 | Base do bloqueio automático de agrotóxico e dose |

## Geração e conferência

| # | Pedido | Resultado | Revisão |
|---|---|---|---|
| P5 | "Agora precisamos entregar o GS baseado no documento", com as escolhas acima | Deck de 12 slides e 5 de anexo, roteiro de 5 minutos | Conta refeita em script Python (custo R$ 2,84; equilíbrio de 66.265 ativos; sensibilidade de preço e de revisão) |
| P5b | Conferência do deck contra o enunciado, slide a slide | Todos os itens do enunciado presentes; siglas TAM, SAM e SOM sem explicação; link do vídeo pendente | Siglas explicadas no slide 3; link fica como pendência da equipe |
| P5c | Releitura do anexo A4 | A primeira versão do A4 descrevia duas revisões que não aconteceram | A4 reescrito só com o que está nesta tabela |
| P6 | 19/11: "se cada um mandar os vídeos isolados, conseguimos unir todos?" e "editar para manter o foco no olhar para a câmera e a qualidade aderente aos slides" | Montagem com ffmpeg (`video/montar_video.py`): abertura com nomes e RMs, slide do deck ao lado da câmera, volume igualado, silêncios das pontas cortados, tratamento de cor e ruído no trecho do Felipe. As falas não foram editadas | A IA avisou que não consegue corrigir a direção do olhar; ficou como está. Trocas de slide calculadas pela proporção do roteiro e conferidas por quadros. Vídeo publicado como não listado (4:09) |

> O P6 foi feito depois da exportação do deck v3 e por isso não aparece no anexo A4; o A4 cobre a construção do conteúdo.

## Pendências da equipe

- Leitura final do deck e do roteiro por pelo menos um integrante, com ajustes de texto onde a equipe discordar.
- Gravar o vídeo, publicar como "não listado", colar o link na capa e gerar o PDF de novo.
- Se alguém usar outra ferramenta de IA no ajuste, acrescentar uma linha neste registro e no anexo A4.
