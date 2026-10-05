# F2-A — Verificação das URLs (F2-E1)

**Responsável:** Felipe Alef · **Data:** 05/10/2026
**Método:** cada link foi aberto e a afirmação feita no texto foi conferida contra o conteúdo da página. Abertura e leitura com apoio do Claude Code; três links que bloqueiam acesso automático (Healthcare Dive e dois do GlobeNewswire) foram abertos manualmente por Felipe. Atende ao último passo de D-007 ("as URLs usadas no texto final são conferidas por pessoa").

---

## 1. Referências da F2-E1 v2 (texto final)

| Ref. | Afirmação no texto da v2 | O que a fonte diz | Status |
|---|---|---|---|
| 1 | Três provedores concentram 63% do mercado global de nuvem (AWS 28%, Microsoft 20%, Google 15%) | Synergy, 30/07/2026: "28%, 20%, and 15%, respectively" no 2T26 | ✅ |
| 2 | MV em 894 hospitais na AL e Tasy em 500 (KLAS, 2025) | MV, 04/08/2025: ranking KLAS da AL com MV 894 e **Philips** 500 | ✅ Sugestão: escrever "Philips (Tasy)", porque a página cita a Philips, não o Tasy |
| 3 | Rede D'Or ampliando o Tasy de 50 para 60 hospitais | Philips, 19/08/2025: "crescerá de 50 para 60" | ✅ |
| 4 | OpenAI entrou na saúde em jan/2026 | TestingCatalog, 08/01/2026: OpenAI for Healthcare com hospitais dos EUA; sem menção ao Brasil | ✅ |
| 5 | Anthropic entrou na saúde em jan/2026 | Anthropic, 11/01/2026: Claude for Healthcare | ✅ |
| 6 | Einstein com perto de 120 algoritmos próprios | Convergência Digital, 08/01/2025: "cerca de 120 algoritmos" | ✅ |
| 7 | Itaú com mais de 1,3 mil modelos de IA | Let's Money, 10/03/2026: "mais de 1,3 mil modelos de IA em operação" | ✅ |
| 8 | Epic Sepsis Model: AUC 0,63; 67% dos casos não identificados | Wong et al., JAMA Intern Med, 21/06/2021: AUC 0,63 (vs 0,76–0,83 declarado); "did not identify 1709 patients with sepsis (67%)" | ✅ |
| 9 | Em 2024 a Anthropic quadruplicou o preço do Haiku | TechCrunch, 04/11/2024: Claude 3.5 Haiku a US$ 1/US$ 5 por milhão de tokens, contra US$ 0,25/US$ 1,25 do Claude 3 Haiku | ✅ Precisão opcional: o aumento foi no lançamento da versão 3.5, a 4× o preço da versão anterior |
| 10 | Shapiro e Varian (1999) | Livro; sem URL | — |

**Resultado:** as 9 referências com URL estão confirmadas. Nenhuma correção obrigatória na v2; duas sugestões de precisão (refs. 2 e 9).

---

## 2. Levantamento v1 (material de apoio)

Os **93 links** da seção 8 de `F2-E1_Levantamento_v1.md` são válidos. As fontes de mercado e concorrência (cerca de 40) foram conferidas no conteúdo; as de infraestrutura, regulação e defensabilidade, só no link.

Afirmações do levantamento que **não se confirmam** nas fontes e não devem ser reaproveitadas em entregas futuras:

| Item no levantamento | O que a fonte diz |
|---|---|
| Tasy: "€ 161 mi" | Exame (#38): R$ 940 mi = € 131 mi |
| Compra do Tasy "com aprovação do CADE" | Não consta nas matérias abertas (#37, #38) |
| MV: predição de sepse "6 a 12 horas antes" | Não consta em #34 nem em #87 |
| Epic: "AI Charting lançado em 08/2025" | Healthcare IT Today (#29): anunciado na UGM 08/2025, uso limitado previsto para o início de 2026 |
| Curiosity: "lançamento no prontuário previsto para 03/2027" | O post da Epic (#27) não traz data |
| "Venda da participação na Abridge" | Não consta em #30 |
| Einstein: "250 profissionais de dados" | Não consta em #81 |
| Rede D'Or: "modelo oncológico com recall de 69%" | Não consta em #85 |
| Porto: "IA em precificação há mais de 15 anos" | Não consta em #92 |
| Bradesco: matéria de 12/09/2026 | Publicada em 27/04/2026 (#89) |
| Neurotech: valores atribuídos ao InvestNews (#45) | #45 não traz valores. Os valores (R$ 620 mi + até R$ 523 mi de earn-out = R$ 1,14 bi) estão em Finsiders (#91), publicado em 10/11/2022 |
| Menlo (#32): preferência pelo fornecedor do prontuário | Confirmado, mas é preferência declarada por clientes dos EUA |

Itens que estavam **[não verificado] ou [parcial]** e agora estão confirmados:
- Autoria do arXiv 2508.12104 (#28): primeiro autor Shane Waxler.
- Epic Sepsis Model (#31): AUC 0,63 e 67% de casos não identificados.
- Data da matéria da Exame sobre a Arvo (#93): 12/03/2026 (R$ 1,8 bi em pagamentos indevidos identificados em 2025).
- Tasy em 500 hospitais na AL (KLAS): confirmado em #33, como "Philips".
