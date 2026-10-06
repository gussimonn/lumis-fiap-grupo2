# CLAUDE.md — LumisOS

Trabalho acadêmico de **Gestão em IA (FIAP)**. A Lumis Intelligence é uma empresa **fictícia**. Atuamos como Head of AI Management ao longo de 7 fases. Não é material da Arkium.

## Antes de responder sobre andamento
Abrir `ESTADO.md` e conferir contra os arquivos reais da pasta. Nunca responder por memória de conversa.

## Fontes de verdade
- Dados da Lumis: **somente** os capítulos em `0X_*/_Enunciado/` e as entregas já feitas. Regra do curso: *"Não invente números sobre a Lumis: se algo não está no anexo, trate como informação indisponível e diga isso explicitamente."* Uma conclusão que não se apoia num quadro é **hipótese** e deve ser marcada como tal.
- Citar a origem: `[fonte: Cap. 2, Quadro 9]`, `[fonte: F1-E3]`, `[não consta]`, `[hipótese]`.
- Pesquisa externa (mercado, casos reais) entra com referência completa e é identificada como contexto externo.
- Em conflito entre capítulos, vale o mais recente, com a divergência sinalizada (D-003).

## Onde gravar
- Entrega: um único arquivo vigente, em `.docx` (ex.: `F2-E1_Mapa_do_Territorio_v2.docx`). Não manter cópia `.md` da entrega (D-011).
- Material de apoio (levantamento, dados transcritos, registro de prompts) pode ficar em `.md` na pasta da entrega.
- Antes de substituir uma versão, mover a anterior para `_Historico/`.
- Toda decisão de gestão vira entrada em `DECISOES.md` (append-only).
- Ao concluir ou avançar uma entrega, atualizar `ESTADO.md`.
- Novo capítulo recebido: PDF em `0X_*/_Enunciado/`, briefing no `README.md` da fase e subpastas `FX-EY_Nome`.

## Escrita
Todo texto escrito ou revisado aqui (entregas, memorandos, READMEs, ESTADO, DECISOES) passa pela skill `humanizer` em `.claude/skills/humanizer/`: ler o `SKILL.md` e a adaptação `PT-BR.md` antes de redigir. Revisar não muda número, fonte, hipótese marcada, bloco de código nem URL (D-010).

## Padrão visual (D-013 a D-015)
Todo material gerado aqui (entrega, memorando, anexo, slide, planilha, imagem ou página) segue o design system em `00_Lumis/Design_System/`. Ler o `README.md` dessa pasta antes de gerar.
- Documento Word: partir de `Modelo_Entrega_Lumis.docx` e usar só os estilos dele. Nada de cor ou fonte aplicada à mão.
- Cores: Vital `#3DBE93` (saúde), Profundo `#0F2D3A` (dados), Pulso `#2BA6C9` (inovação), Vital escuro `#1E8C6B` para texto. Não usar outras cores de marca.
- Fontes: Georgia nos títulos, Calibri no texto (fora do Office: Source Serif 4 e Source Sans 3).
- Logo e Feixe: usar os arquivos de `logo/` e `artefato/`, sem redesenhar. O Feixe entra uma vez por documento, na capa.
- Marcadores `[fonte]`, `[hipótese]`, `[não consta]` e `[risco: Cx]` com os estilos de caractere Tag do modelo.
- Mudança no padrão: editar os scripts em `_fonte/`, gerar de novo, guardar a versão anterior em `_Historico/` e registrar em `DECISOES.md`.
- As entregas da Fase 1 e a F2-E1 ficam como estão, salvo pedido da equipe.

## Coerência (critério da Fase 7)
Toda nova entrega deve ser checada contra `00_Lumis/Compromissos_Vigentes.md`. Se contradisser um compromisso, decida explicitamente: manter, ou revisar com nova entrada em `DECISOES.md`.

## Nomes
- **Lumis Intelligence** = a empresa. **Lumis Insight** = o produto.
- Os PDFs do curso têm marca d'água com dados pessoais do aluno. Não reproduzir esses dados nos arquivos de trabalho.
