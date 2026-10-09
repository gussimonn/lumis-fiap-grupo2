# F2-D — Documento Integrado (peça de envio)
**Status:** 🟡 v3 em 08/10/2026; aguarda revisão da equipe · **Arquivo vigente:** [F2-D_Documento_Integrado_v3.docx](F2-D_Documento_Integrado_v3.docx) · **Decisões:** D-043 a D-047 · **Versões anteriores:** `_Historico/2026-10-08_F2-D_Documento_Integrado_v1.docx` e `_v2.docx`

Documento único, com identificação da equipe, que reúne as cinco entregas articuladas entre si [fonte: Cap. 2, 4.2]. O memorando ao conselho vai em arquivo separado: [F2-M](../F2-M_Memorando_ao_Conselho/).

## Estrutura da v3 (24 páginas; corpo nas páginas 2 a 16)

| Parte | Páginas |
|---|---|
| Capa, com a identificação da equipe | 1 |
| A tese em uma página (as cinco perguntas do Vetor e a nota "como ler") | 2 |
| Entrega 5 · Due diligence ESG da expansão | 3 a 5 |
| Entrega 1 · O mapa do território | 6 e 7 |
| Entrega 2 · Auditoria do ativo: dados e métricas | 8 e 9 |
| Entrega 3 · A linha de responsabilidade | 10 e 11 |
| Entrega 4 · Cultura e funil de inovação | 12 a 14 |
| O que precisa estar resolvido antes (condições, uso do aporte, coerência e o que o Anexo A não informa) | 15 e 16 |
| Referências | 17 |
| Apêndice A: prompts da pesquisa de mercado (Entrega 1) | 18 e 19 |
| Apêndice B: quadros de apoio | 20 a 24 |

A Entrega 5 abre o dossiê porque o enunciado diz que é "o capítulo que o comitê de investimento lerá primeiro" (Cap. 2, seção 4). Cada entrega começa em página nova, e as seções levam o número da entrega do enunciado (5.1, 1.1...).

## O que mudou da v1 para a v2 (D-045)
A v1 estava correta, mas pesada para quem decide: cerca de 90 marcadores no corpo e 21 tabelas. A v2 mantém todas as decisões, números e condições e muda a forma.
- **No corpo, a decisão e o porquê.** Cada entrega abre com a conclusão e fica com uma ou duas peças principais (figura ou tabela). O restante foi para o Apêndice B.
- **Origem na legenda.** Uma nota na página 2 diz que todo número sobre a Lumis vem do Anexo A, com o quadro na legenda de cada figura e tabela. O texto corrido não tem mais `[fonte]`.
- **Hipótese só onde sustenta decisão:** 7 no corpo (eram 22).
- **Um quadro do que falta.** Os "não consta" do corpo viraram o quadro "O que o Anexo A não informa", no fechamento, agrupado por tema e com a seção onde cada lacuna pesa.
- **Apêndice B:** materialidade (evidências), grupos em risco, medidas de equidade e privacidade, pontos da LGPD, ameaças, dependências, variáveis proxy, métricas do painel, incidentes, alertas, clima, camadas da cultura e distribuição. Aqui os marcadores ficam como estavam.

## O que mudou da v2 para a v3 (D-046)
Os mesmos ajustes feitos no memorando: "modo sombra" virou "teste em paralelo" (o sistema roda junto ao processo atual, sem decidir), inclusive no nome da etapa do funil; a tese e a seção 1.2 explicam por que a Aster não chega a seguradoras e bancos e de quem são as 14 das 38 contas; a condição 12 tem o mesmo texto do memorando. As páginas não mudaram.

Depois, a seção 4.4 foi reescrita: sem a citação de Nagji e Tuff, com o título "Como dividimos o tempo da equipe" e com "mês-pessoa" explicado na abertura da Entrega 4. A versão de antes está em `_Historico/2026-10-08_F2-D_Documento_Integrado_v3_antes-secao-4.4.docx`.

Por último (D-047), a seção 5.4 foi refeita: a ficha da métrica pública tem só limite (o dobro) e meta (1,5 vez em 12 meses), marcados como proposta da equipe, sem a meta de 7,4%. A seção 5.2 ficou mais curta, o crédito usa "80% da melhor faixa" e o Apêndice B ganhou a tabela "De onde vem cada número". A mudança foi aplicada sobre o arquivo salvo no Word pela equipe (capa refeita e parágrafos justificados), que está em `_Historico/2026-10-08_F2-D_Documento_Integrado_v3_editado-no-word-antes-limites.docx`.

## Como foi montado
- **Script:** [figuras/montar_v2.py](figuras/montar_v2.py) guarda o texto final de cada parte e gera o documento único e o memorando a partir do `00_Lumis/Design_System/Modelo_Entrega_Lumis.docx`. Para gerar de novo: `python montar_v2.py dossie saida.docx` ou `python montar_v2.py memo saida.docx`; `python montar_v2.py lint` confere códigos internos, travessões e remissões. O script da v1 está em `_Historico/2026-10-08_F2-D_montar_v1.py`.
- **Texto:** o da v1, enxugado. As entregas individuais não mudaram.
- **Figuras:** as mesmas da v1 ([figuras/gerar_figuras_e2_dossie.py](figuras/gerar_figuras_e2_dossie.py) para as quatro da Entrega 2).
- **Conferência da v2:** números contra o Anexo A, as entregas e as decisões (nenhum número sem correspondência), lint sem avisos, páginas conferidas no PDF exportado pelo Word.
- **O .docx vigente tem formatação feita no Word pela equipe** (capa nova e parágrafos justificados) que o script não gera. Para mudar texto: alterar o conteúdo em `montar_v2.py`, gerar um .docx temporário e aplicar o texto novo sobre o vigente com [figuras/sincronizar.py](figuras/sincronizar.py) (`python sincronizar.py vigente.docx gerado.docx saida.docx`), que mantém capa e formatação. Nunca substituir o vigente pelo gerado direto.
- Se alguém editar o .docx no Word, guardar antes a versão anterior em `_Historico/`.

## Composição do envio (Cap. 2, 4.2)
- [x] Documento único com identificação da equipe, com as cinco entregas articuladas
- [x] Memorando ao conselho, no máximo 2 páginas ([F2-M](../F2-M_Memorando_ao_Conselho/))
- [x] Apêndice de prompts da Entrega 1, com resultado e verificação (Apêndice A)
- [ ] Planilhas, matrizes e diagramas: matrizes e diagramas no corpo e no Apêndice B; falta a planilha das contas da equipe (cerca de 15 contas: 49,8%; 2,5; 2,2 e 3,0; 1,9 e 1,5; 154 mil; 57,4%; margens; R$ 19.240 e R$ 40.176; 8,7 meses; R$ 0,6 mi por mês-pessoa; 53% e 73%; 25,8%; 64,6%)
- [ ] Envio pelo portal no prazo [prazo não consta]

## Antes do envio (equipe)
- Revisar o documento único e o memorando.
- Decidir a data da primeira publicação da métrica pública (a condição 8 exige a métrica já publicada antes de qualquer frente nova).
- Decidir se há substituto do Responsável por Dados nos portões do funil (risco de pessoa-chave).
- Abrir no original: Schein, Cooper, Obermeyer e o guia da ANPD; conferir no texto compilado da LGPD a redação usada para o art. 11, § 4º ("entre controladores"), e para o art. 33.
- A imagem da figura das camadas (Entrega 1) ainda diz "roda dentro do sistema hospitalar do cliente", o que não vale para seguradoras e bancos; a legenda marca como leitura da equipe.

## Checagem (08/10/2026, v2)
- [x] Nenhum número sobre a Lumis sem quadro de origem (conferência contra o Anexo A)
- [x] Toda responsabilidade termina em cargo
- [x] Pelo menos uma iniciativa recusada (três, com o custo de cada recusa)
- [x] Toda métrica ESG com periodicidade e responsável
- [x] Checagem contra os compromissos da Declaração de Intenção (no fechamento)
- [x] O que não consta do Anexo A dito explicitamente (quadro no fechamento)
- [x] Nenhum código interno, nome de pessoa da Lumis ou travessão no texto
