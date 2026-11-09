# Execução do prompt P1 (tradução da lógica): saída bruta

Material de apoio do Apêndice A. Execução em 08/11/2026 com Claude (Anthropic), numa sessão separada que leu só as seções A.1 a A.3 de `Anexo_A1-A4_transcrito.md`, sem acesso ao restante do dossiê, sem web e sem gravar arquivos. O texto do prompt é o do Apêndice A (P1). Abaixo, a resposta completa, sem edição.

---

**(1) O caminho de um caso em sete passos**

1. **Entrada.** O sistema recebe do cliente o registro do paciente, com até 34 campos preenchidos. Responsável: integração (time técnico). [fonte: Quadro A.1, etapa 1]

2. **Ausência de dados.** O sistema vê quais campos vieram vazios e preenche cada um com uma suposição fixa. Dos 34 campos, 11 costumam chegar vazios, mas o anexo só documenta o tratamento de 5 deles. Responsável: time de dados. [fonte: Quadro A.1, etapa 2; Quadro A.3]
   - Histórico de internações (vazio em 23% dos registros): o sistema assume zero internações, e o paciente é tratado como se não tivesse necessidade.
   - Custo acumulado de procedimentos (31%): assume zero. A R-19 não se aplica e a pontuação cai.
   - Comorbidades (19%): assume nenhuma. A R-07 não se aplica.
   - Resultado de exames (42%): assume a média da base. O caso fica mais perto da média e os extremos se achatam.
   - Tipo de plano (8%): assume categoria básica. Isso aciona a R-23, que anula o bônus da R-19.
   - Os campos vazios não se distribuem por igual: registros de unidades públicas e de clientes com sistemas mais antigos têm, em média, 2,4 vezes mais campos vazios que os de unidades privadas de grande porte.

3. **Pontuação.** Um modelo estatístico dá ao caso uma pontuação de 0 a 100, com base nas variáveis do "Quadro A.6 da Fase 2". Esse quadro não está no anexo, e a fórmula também não. Responsável: time de dados. [fonte: Quadro A.1, etapa 3]

4. **Ajustes.** As regras do Quadro A.2 somam ou subtraem pontos. Há 41 regras ativas e só 8 estão publicadas (tabela abaixo). Elas são avaliadas na ordem apresentada, e a primeira que se aplica encerra a avaliação do seu bloco. O anexo não diz que regras formam cada bloco. Por isso não dá para saber, por exemplo, se a R-04 e a R-07 podem somar juntas no mesmo caso. Responsável: time técnico. [fonte: Quadro A.1, abertura e etapa 4; Quadro A.2]

5. **Cortes (classificação).** A pontuação ajustada é comparada aos limiares: 72 ou mais é alta, de 45 a 71 é média e abaixo de 45 é baixa. A R-38 muda a faixa, não os pontos, e o anexo não diz em que passo ela entra. Como age sobre a faixa, só pode agir depois que a faixa existe [dedução, não documentada]. Responsável: "definido em 2023, sem revisão". [fonte: Quadro A.1, etapa 5; Quadro A.2]

6. **Desempate.** Se dois casos têm a mesma pontuação ajustada e a mesma faixa, vem primeiro o que entrou no sistema há mais tempo. Essa regra não está documentada em lugar nenhum: foi encontrada lendo o código. O responsável aparece como "não documentado". [fonte: Quadro A.1, etapa 6; Quadro A.3]

7. **Saída.** O sistema devolve ao cliente a faixa de prioridade e os três fatores de maior peso. A pontuação em número não é devolvida. Essa decisão é de 2023, para evitar que hospitais calibrassem registros em busca de pontuações mais altas, e nunca foi comunicada formalmente a nenhum cliente. O anexo não diz como os três fatores são escolhidos. A faixa é uma recomendação de prioridade, não um diagnóstico. O próprio corte de 72 teve objetivo operacional, não clínico. Responsável: integração (time técnico). [fonte: Quadro A.1, etapa 7 e nota; Quadro A.2]

**(2) Regras publicadas, na ordem de avaliação**

Ordem: R-04 → R-07 → R-11 → R-15 → R-19 → R-23 → R-31 → R-38. É a ordem em que aparecem no Quadro A.2, e o anexo diz que as regras são avaliadas na ordem apresentada. Não consta onde as outras 33 regras entram nessa sequência, nem onde começa e termina cada bloco.

| Regra | Condição | Efeito | Fonte |
|---|---|---|---|
| R-04 | Internação nos últimos 90 dias | +12 pontos | Quadro A.2 (criada em 2022) |
| R-07 | Registro de comorbidade crônica | +9 pontos | Quadro A.2 (2022); Quadro A.3 |
| R-11 | Mais de 2 faltas em consultas agendadas | −7 pontos | Quadro A.2 (2023) |
| R-15 | Encaminhamento vindo de pronto-socorro | +15 pontos | Quadro A.2 (2022) |
| R-19 | Custo acumulado de procedimentos no quartil superior | +11 pontos | Quadro A.2 (2023); Quadro A.3 |
| R-23 | Plano contratado da categoria básica | Anula o +11 da R-19 | Quadro A.2 (2024); Quadro A.3 |
| R-31 | 75 anos ou mais e nenhuma internação recente | −6 pontos | Quadro A.2 (2023) |
| R-38 | Cliente é conta estratégica e o caso é limítrofe | Sobe uma faixa (+1 faixa) | Quadro A.2 (2025) |

Ressalvas de dependência:
- **R-19 e R-23.** A R-23 só tem efeito se a R-19 tiver se aplicado. Custo vazio vira zero, e aí a R-19 não se aplica [Quadro A.3]. Plano vazio vira "básica", e aí a R-23 anula o bônus [Quadro A.3]. Há também um conflito que o anexo não resolve. Se as duas estiverem no mesmo bloco, vale a regra "a primeira que se aplica encerra o bloco": a R-19 viria antes e a R-23 nem seria avaliada. O texto da R-23, porém, supõe que ela anula a R-19. O resultado depende de como os blocos estão definidos, e isso não consta.
- **R-38.** Não estão definidos o que é caso "limítrofe", o critério para ser conta estratégica, o passo em que a regra é aplicada, nem o que acontece com um caso que já está em alta. É a única regra publicada que mexe na faixa, e não nos pontos.
- **R-07.** Comorbidades em branco viram "nenhuma", e a regra não se aplica [Quadro A.3].
- **R-04 e R-31.** Histórico de internações em branco vira zero, e a R-04 não se aplica [Quadro A.3]. Num paciente de 75 anos ou mais, isso parece cumprir a condição da R-31 (−6), mas o anexo não confirma essa combinação [dedução a confirmar]. O que é internação "recente" na R-31 também não está definido; os 90 dias só aparecem na R-04.

**(3) Cortes**

| Faixa | Pontuação ajustada | % dos casos em 2026 | Definida em |
|---|---|---|---|
| Alta prioridade | 72 ou mais | 18% | mar/2023 |
| Média prioridade | de 45 a 71 | 44% | mar/2023 |
| Baixa prioridade | abaixo de 45 | 38% | mar/2023 |

[fonte: Quadro A.2]

- Os cortes valem para a pontuação já ajustada, ou seja, depois do passo 4.
- O corte de 72 foi calibrado em março de 2023 para que a fila de alta prioridade de um cliente específico, o Hospital Vila Ipê, coubesse na capacidade daquela unidade naquele momento. O objetivo era operacional, não clínico. Depois ele foi replicado para todos os clientes seguintes e nunca foi recalibrado. Hoje governa a priorização em 38 contas, com capacidades, perfis de pacientes e realidades regionais completamente diferentes. [fonte: Quadro A.2]
- Os limiares estão em números inteiros. Não consta o que acontece com pontuação fracionária (por exemplo, entre 71 e 72 ou entre 44 e 45), nem se há arredondamento.
- A R-38 pode deixar um caso numa faixa acima da que a pontuação indica.

**(4) Dois testes aritméticos (sintéticos e condicionais)**

Condições que valem para os dois testes:
- Todos os valores são inventados para o teste, inclusive a pontuação do modelo, porque a fórmula não consta.
- Nenhuma das 33 regras não publicadas se aplica.
- O cliente não é conta estratégica, então a R-38 fica de fora.
- As pontuações são inteiras, o que evita a questão do arredondamento.

*Teste 1: alta prioridade*
- Entradas: pontuação do modelo 60. Os cinco campos do Quadro A.3 estão preenchidos. O paciente foi encaminhado pelo pronto-socorro, não teve internação nos últimos 90 dias e não tem comorbidade crônica. Tem 1 falta, custo fora do quartil superior, plano não básico e 50 anos.
- Regras que se aplicam: só a R-15.
- Conta: 60 + 15 = 75.
- Corte: 75 é maior ou igual a 72, logo **alta**.
- Saída: faixa alta e três fatores de maior peso, que não dá para determinar com o anexo.
- Os blocos não mudam o resultado, porque só uma regra publicada se aplica. A margem é de 3 pontos: se regras não publicadas tirassem mais de 3 pontos, o caso cairia para média. Se o cliente fosse conta estratégica, o caso já estaria em alta, e o efeito de "+1 faixa" sobre a alta não consta.

*Teste 2: baixa prioridade (mostra a dependência entre R-19 e R-23)*
- Entradas: pontuação do modelo 30. O custo acumulado, que está preenchido, fica no quartil superior. O tipo de plano veio vazio. O paciente não teve internação nos últimos 90 dias e não tem comorbidade crônica. Tem 0 faltas, encaminhamento que não veio de pronto-socorro e 60 anos.
- Passo 2: plano vazio, então o sistema assume categoria básica [Quadro A.3].
- Leitura A (a R-23 anula a R-19, como diz o texto da regra): 30 + 0 = 30. Abaixo de 45, logo **baixa**.
- Leitura B (as duas no mesmo bloco; a R-19 se aplica primeiro, encerra o bloco e a R-23 não é avaliada): 30 + 11 = 41. Abaixo de 45, logo **baixa**.
- O resultado é baixa nas duas leituras. Na leitura A, o campo vazio sozinho custou 11 pontos. A margem até a média é de 4 pontos na leitura B e de 15 na leitura A.
- Se o cliente fosse conta estratégica, o caso só subiria para média se fosse "limítrofe". Como esse termo não está definido, não dá para saber se 30 ou 41 se qualificam, e o resultado ficaria indeterminado.

**(5) DADO AUSENTE**

- As outras 33 regras ativas: o que dizem, que efeito têm e onde entram na ordem. Segundo o anexo, estão no repositório interno.
- A fórmula do modelo estatístico e as suas variáveis, que ficam no Quadro A.6 da Fase 2, fora deste anexo.
- Os limites dos blocos de regras, isto é, que regras formam cada bloco.
- Como a R-23 funciona se a R-19 encerrar o bloco antes dela.
- A definição de caso "limítrofe" na R-38.
- O critério para um cliente ser conta estratégica.
- O passo em que a R-38 é aplicada, e o que ela faz com um caso que já está em alta.
- O arredondamento, o tratamento de pontuação fracionária e se a pontuação ajustada fica limitada a 0–100 depois dos ajustes.
- Como são escolhidos os três fatores de maior peso.
- Quais são os outros 6 dos 11 campos que costumam chegar vazios, e o que o sistema faz com eles. Isso inclui os campos usados pela R-11 (faltas), pela R-15 (origem do encaminhamento) e pela R-31 (idade), se estiverem entre eles.
- Sobre que base e período se calcula o "quartil superior" de custo da R-19.
- O que é internação "recente" na R-31.
- Qual é a "média da base" usada quando faltam os resultados de exames.
- Quem responde pela regra de desempate. Ela só foi encontrada lendo o código.

**(6) Explicação para o cliente (86 palavras)**

O Lumis Insight devolve, para cada paciente, uma faixa de prioridade (alta, média ou baixa) e os três fatores de maior peso. A faixa é uma recomendação de prioridade, não um diagnóstico nem uma avaliação clínica. Ela vem de um modelo estatístico e de regras de ajuste, e o resultado é comparado a cortes fixos. A pontuação numérica não é enviada. Campos vazios são preenchidos com suposições, como zero internações ou plano básico, e isso pode baixar a prioridade. Enviar o registro completo evita essas suposições.
