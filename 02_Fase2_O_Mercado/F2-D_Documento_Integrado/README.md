# F2-D — Documento Integrado (peça de envio)
**Status:** 🟡 v1 montada em 08/10/2026; aguarda revisão da equipe · **Arquivo vigente:** [F2-D_Documento_Integrado_v1.docx](F2-D_Documento_Integrado_v1.docx) · **Decisões:** D-043 e D-044

Documento único, com identificação da equipe, que reúne as cinco entregas articuladas entre si [fonte: Cap. 2, 4.2]. O memorando ao conselho vai em arquivo separado: [F2-M](../F2-M_Memorando_ao_Conselho/).

## Estrutura da v1 (23 páginas)

| Parte | Páginas |
|---|---|
| Capa, com a identificação da equipe | 1 |
| A tese em uma página (as cinco perguntas do Vetor) | 2 |
| Entrega 5 · Due diligence ESG da expansão | 3 a 5 |
| Entrega 1 · O mapa do território | 6 a 8 |
| Entrega 2 · Auditoria do ativo: dados e métricas | 9 a 11 |
| Entrega 3 · A linha de responsabilidade | 12 a 14 |
| Entrega 4 · Cultura e funil de inovação | 15 a 19 |
| O que precisa estar resolvido antes (condições, uso do aporte, coerência) | 19 e 20 |
| Referências | 20 e 21 |
| Apêndice A: prompts da pesquisa de mercado (Entrega 1) | 22 e 23 |

A Entrega 5 abre o dossiê porque o enunciado diz que é "o capítulo que o comitê de investimento lerá primeiro" (Cap. 2, seção 4). As seções levam o número da entrega do enunciado (5.1, 1.1...).

## Como foi montado
- **Script:** [figuras/montar_v1.py](figuras/montar_v1.py) guarda o texto final de cada parte e gera o documento único e o memorando a partir do `00_Lumis/Design_System/Modelo_Entrega_Lumis.docx`. Para gerar de novo: `python montar_v1.py dossie saida.docx` ou `python montar_v1.py memo saida.docx`; `python montar_v1.py lint` confere códigos internos, travessões e remissões.
- **Texto:** integração das entregas vigentes (F2-E1 v2, F2-E2 v2, F2-E3 v1, F2-E4 v1 e F2-E5 v1), com os cortes de repetição e os ajustes de coerência da D-044. As entregas individuais não mudaram.
- **Figuras:** as das entregas, menos as quatro da F2-E2, refeitas para o dossiê com os textos corrigidos ([figuras/gerar_figuras_e2_dossie.py](figuras/gerar_figuras_e2_dossie.py)). Saíram as figuras de ameaças e de margem (Entrega 1) e as do funil e da capacidade (Entrega 4), cujos dados estão nas tabelas.
- **Revisão:** sete leituras independentes (fatos, coerência, banca, leitores do conselho e do Vetor, estilo e diagramação), consolidação, ajuste com o humanizer e conferência final.
- Se alguém editar o .docx no Word, guardar antes a versão anterior em `_Historico/`. O script não lê edições feitas no Word.

## Composição do envio (Cap. 2, 4.2)
- [x] Documento único com identificação da equipe, com as cinco entregas articuladas
- [x] Memorando ao conselho, no máximo 2 páginas ([F2-M](../F2-M_Memorando_ao_Conselho/))
- [x] Apêndice de prompts da Entrega 1, com resultado e verificação (Apêndice A do documento único)
- [ ] Planilhas, matrizes e diagramas: as matrizes e diagramas estão no documento; falta a planilha das contas da equipe (cerca de 15 contas: 49,8%; 2,5; 2,2 e 3,0; 1,9 e 1,5; 154 mil; 57,4%; margens; R$ 19.240 e R$ 40.176; 8,7 meses; R$ 0,6 mi por mês-pessoa; 53% e 73%; 25,8%; 64,6%)
- [ ] Envio pelo portal no prazo [prazo não consta]

## Antes do envio (equipe)
- Revisar o documento único e o memorando.
- Decidir a data da primeira publicação da métrica pública (a condição 8 exige a métrica já publicada antes de qualquer frente nova).
- Decidir se há substituto do Responsável por Dados nos portões do funil (risco de pessoa-chave).
- Abrir no original: Nagji e Tuff (e registrar a data de acesso na referência), Schein, Cooper, Obermeyer e o guia da ANPD; conferir no texto compilado da LGPD a redação usada para o art. 11, § 4º ("entre controladores"), e para o art. 33.
- A imagem da figura das camadas (Entrega 1) ainda diz "roda dentro do sistema hospitalar do cliente", o que não vale para seguradoras e bancos; a legenda marca como leitura da equipe.

## Checagem final (08/10/2026)
- [x] Nenhum número sobre a Lumis sem quadro de origem (conferência contra o Anexo A)
- [x] Toda responsabilidade termina em cargo
- [x] Pelo menos uma iniciativa recusada (três, com o custo de cada recusa)
- [x] Toda métrica ESG com periodicidade e responsável
- [x] Checagem contra os compromissos da Declaração de Intenção (no fechamento)
- [x] Nenhum código interno, nome de pessoa da Lumis ou travessão no texto
