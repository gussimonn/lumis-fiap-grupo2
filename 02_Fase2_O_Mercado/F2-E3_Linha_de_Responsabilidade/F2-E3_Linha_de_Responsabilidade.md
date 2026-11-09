# F2-E3 · Linha de Responsabilidade

> Texto da Entrega 3 como foi no documento único (`F2-D_Documento_Integrado_v3.docx`), com os quadros de apoio desta entrega que estão no Apêndice B. É uma cópia para leitura: se houver diferença, vale o .docx. Os números de figura, tabela, seção e nota são os do documento único. Extraído em 09/10/2026.

## Entrega 3 · A linha de responsabilidade

> **Os registros da Lumis não mostram, para nenhuma decisão do Lumis Insight, um cargo que autorizou o uso, um que acompanha o erro e um que pode desligar o sistema em prazo conhecido. Propomos um cargo para cada etapa: autorizar, acompanhar, suspender e religar.**

### 3.1 As decisões que o sistema toma hoje

O sistema toma cerca de um milhão de decisões por mês. Classificamos como de alto impacto toda decisão que afeta a saúde ou o acesso a um serviço essencial: são quatro das cinco.

| Decisão | Por mês | Revisão humana hoje | Quem autorizou o uso | Impacto |
|---|---|---|---|---|
| Priorização da fila de atendimento | 640 mil | Amostra de 2% | Diretoria comercial do cliente, sem aprovação interna formal | Alto |
| Sugestão de protocolo clínico | 210 mil | Sempre, pelo médico | Comitê clínico do hospital | Alto |
| Classificação de risco de sinistro | 74 mil | Só acima de R$ 50 mil | Diretoria da seguradora | Alto |
| Sinalização de risco de crédito | 31 mil | Sempre | Comitê de crédito do banco | Alto |
| Roteamento de mensagens de suporte | 95 mil | Nenhuma | Operação da Lumis | Baixo |

*Tabela 4. Decisões delegadas ao sistema. Fonte: Cap. 2, Quadro 12. A coluna Impacto é classificação da equipe.*

O controle segue o costume do cliente: o crédito tem revisão em todos os casos; a priorização, com viés já medido, só em 2%.

### 3.2 Quem responde hoje

A Lumis não tem comitê de ética nem de risco. Dos sete papéis com dono, só um controla o que entra em produção: a liberação de nova versão do modelo, exclusiva do CTO. Os quatro incidentes dos últimos dois anos entraram por outras portas: dados de entrada, atualização do fornecedor, material comercial e acompanhamento por grupo [hipótese]. Dois foram percebidos pelo cliente antes da Lumis (Tabela 17, Apêndice B).

### 3.3 A linha de responsabilidade proposta

Quem libera uma versão não é o único que acompanha o erro nem o único que pode suspender. Suspender exige um cargo; religar, dois. E a Lumis passa a autorizar cada uso, além do cliente.

| Etapa | Cargo responsável | Contrapeso |
|---|---|---|
| Autorizar cada uso em cada cliente | CEO | Parecer obrigatório do Head of AI Management e da DPO |
| Liberar versão nova ou atualização do fornecedor | CTO | Head of AI Management confere o teste por grupo e pode barrar |
| Medir o erro por grupo e cruzar as reclamações | Responsável por Dados | Auditor externo, contratado pela CEO, refaz a conta |
| Acompanhar e confirmar o alerta | Head of AI Management | DPO como suplente |
| Suspender ou restringir | Head of AI Management | CTO e DPO também podem suspender |
| Executar a suspensão | CTO | Responsável por Dados como suplente |
| Religar | CTO e Head of AI Management, juntos | Sem acordo, segue suspenso e a CEO leva o caso ao conselho |
| Aprovar os números divulgados ao mercado | Head of AI Management | Responsável Comercial corrige o material |
| Proteger dados pessoais e direito de uso | DPO | Responsável por Dados retira o dado sem autorização |
| Prestar contas ao conselho | CEO | Head of AI Management relata as suspensões diretamente |

*Tabela 5. Quem responde por cada etapa. Proposta da equipe sobre os cargos do Cap. 2, Quadro 13.*

A linha vale para as quatro decisões de alto impacto; muda só o sinal de alerta de cada uma (Tabela 18, Apêndice B), lido a cada quinze dias. Queixa de cliente, contestação de paciente ou incidente dispara o alerta na hora.

**Prazo para suspender.** Confirmado o alerta, a decisão sai em até 24 horas e a execução em mais 24, sem esperar nova leitura; com dano clínico em curso, a execução é imediata. O teto de 48 horas, o mesmo prometido para revisar um caso contestado, vale como meta até o primeiro teste.

**O que fazemos já.** Executar a restrição da seção 2.5; subir para 10% a revisão no grupo de 18 a 59 anos de CEP D/E, que está em alerta; testar a suspensão em até 30 dias, por cliente e por grupo, e repetir a cada trimestre; e exigir nos contratos um cargo do cliente que assine a autorização de uso (cláusula da DPO).

### 3.4 Quando a revisão humana é obrigatória

- **Priorização em grupo acima de 2 vezes o erro do melhor:** todos os casos voltam à triagem do hospital; acima de 1,5 e até 2 vezes, a revisão sobe de 2% para 10%. Critério: o compromisso de Não Amplificação de Danos.
- **Toda contestação de paciente, profissional ou cliente:** imediata na urgência e em até 48 horas nos demais casos. Critério: o compromisso de Reversibilidade.
- **Toda sugestão de protocolo clínico,** agora com registro de aceite, alteração ou rejeição pelo médico. Critério: revisão sem registro não pode ser auditada.
- **Classificação de sinistro que leve a negativa ou atraso,** no lugar do corte de R$ 50 mil. Critério: o efeito sobre a pessoa.
- **Toda sinalização de risco de crédito,** como já ocorre. Critério: acesso a serviço essencial.
- **Fonte de dados, cliente ou versão nova:** revisão de 10% até uma leitura quinzenal sem piora em nenhum grupo. Critério: dois dos quatro incidentes começaram assim.

### 3.5 O que muda num setor novo

Num setor novo, como o veterinário, a plataforma ou os países que o Vetor propõe, a Lumis não sabe reconhecer o erro típico nem tem dado local para medi-lo. Por isso:

- **Portão de entrada:** o Responsável por Produto leva o pedido, a CEO decide, com parecer obrigatório do Head of AI Management e da DPO (seção 4.3).
- **Teste em paralelo e responsável do domínio:** o sistema roda sem decidir até haver erro medido por grupo; um especialista do setor assina o que conta como erro grave.
- **Medição e suspensão prontas:** antes da entrada, o Responsável por Dados indica quem mede o erro no mercado, o Head of AI Management aprova, e a suspensão é testada.

## Quadros de apoio (Apêndice B do documento único)

| Quando | O que aconteceu | Quem percebeu | Correção | Por onde entrou |
|---|---|---|---|---|
| 03/2025 | Exames de um laboratório novo passaram a ser descartados | Cliente | 22 dias | Dados de entrada |
| 09/2025 | Queda de desempenho após atualização do fornecedor do modelo | Equipe interna | 6 dias | Fornecedor |
| 01/2026 | Registros duplicados inflaram as "vidas analisadas" | Auditoria interna | Só no sistema | Material comercial |
| 07/2026 | Viés etário e regional na priorização | Hospital Vila Ipê | Em tratamento | Acompanhamento por grupo |

*Tabela 17. Incidentes dos últimos 24 meses. Fonte: Cap. 2, Quadro 14. A coluna Por onde entrou é leitura da equipe.*

| Decisão | Sinal de alerta |
|---|---|
| Priorização da fila | Grupo acima de 1,5 vez o erro do melhor (revisão de 10%); acima de 2 vezes, restrição |
| Protocolo clínico | Grupo com mais de 2 vezes as sugestões alteradas pelo médico |
| Risco de crédito | Faixa de CEP com aprovação abaixo de 80% da melhor |
| Risco de sinistro | Faixa de CEP com mais de 2 vezes as negativas da melhor |

*Tabela 18. Alertas por decisão, lidos a cada quinze dias. Limites nas seções 2.5 e 5.2; o do sinistro é proposta da equipe. Dos quatro sinais, o Anexo A só traz o erro por grupo da priorização, medido pelo hospital (Cap. 2, Quadro 10).*
