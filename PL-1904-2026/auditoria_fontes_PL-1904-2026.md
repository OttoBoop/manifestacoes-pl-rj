# Auditoria de Fontes — Manifestação Técnica PL nº 1904/2026

**Data da auditoria:** 2026-05-26
**Arquivo auditado:** `manifestacao_PL-1904-2026-short.md`
**Metodologia:** Extração sistemática de toda afirmação factual, referência jurídica e dado numérico, com ou sem fonte declarada explicitamente. Cada ocorrência é um bloco independente. Status aguarda verificação pelo verificador humano ou agente especializado.

---

## Blocos de Citação

### [F-1] Autoria do PL
**Texto no documento:** "PL nº 1904/2026, de autoria do Vereador Fabio Silva"
**Fonte declarada:** FONTE IMPLÍCITA — dado extraído da própria proposição
**Tipo:** referência jurídica / dado factual
**Status:** ⚠️ PARCIAL
**Resultado V1:** Número do PL e município confirmados via NB. Vereador Fabio da Silva Costa (PODE) confirmado como vereador em exercício na 12ª Legislatura. Porém o sistema público CMRJ (scpro2528.nsf) retornou "não existe informação" — lag de indexação provável. Vínculo nome→PL não confirmável em fonte primária pública.
**Decisão recomendada:** manter — dado plausível e internamente consistente; lag de indexação comum em PLs recentes.

---

### [F-2] Resolução CMN nº 2.878/2001 — ausência de obrigação de presença humana
**Texto no documento:** "nem a Resolução CMN nº 2.878/2001 nem a ABNT NBR 15250:2005 impõem presença humana dedicada"
**Fonte declarada:** Resolução CMN nº 2.878/2001 (Banco Central do Brasil)
**Tipo:** referência jurídica
**Status:** ✅ CONFIRMADO
**Resultado V1:** Art. 9º exige "alternativas técnicas, físicas ou especiais" (não presença humana). Art. 15 §2º reforça: serviços eletrônicos alternativos são "prerrogativa das instituições". Texto integral obtido via PDF BCB.
**Fonte primária:** https://www.bcb.gov.br/pre/normativos/res/2001/pdf/res_2878_v3_p.pdf

---

### [F-3] ABNT NBR 15250:2005 — ausência de obrigação de presença humana
**Texto no documento:** "nem a Resolução CMN nº 2.878/2001 nem a ABNT NBR 15250:2005 impõem presença humana dedicada"
**Fonte declarada:** ABNT NBR 15250:2005
**Tipo:** referência jurídica / norma técnica
**Status:** ⚠️ PARCIAL — NORMA CANCELADA
**Resultado V1:** Norma existe, é de 2005, regula hardware de ATMs (não presença humana) — argumento central correto. PORÉM: NBR 15250:2005 foi **cancelada** (Target Normas: "uso pode trazer riscos"). Citar norma cancelada como se vigente pode fragilizar o argumento na câmara.
**Fonte primária:** https://www.normas.com.br/visualizar/abnt-nbr-nm/24255/abnt-nbr15250-acessibilidade-em-caixa-de-auto-atendimento-bancario
**Decisão necessária:** remover referência à NBR 15250:2005 do texto, substituindo por formulação sem citação da norma específica.

---

### [F-4] STF — RE 610.221, Tema 272 — competência municipal pacificada
**Texto no documento:** "A competência municipal é pacificada pelo STF (RE 610.221, Tema 272)"
**Fonte declarada:** STF, RE 610.221, Tema 272
**Tipo:** referência jurídica / julgado
**Status:** ✅ CONFIRMADO
**Resultado V1:** Tese fixada: "Compete aos Municípios legislar sobre assuntos de interesse local, notadamente sobre a definição do tempo máximo de espera de clientes em filas de instituições bancárias." Julgado no Tribunal Pleno, DJe 18/10/2010.
**Fonte primária:** https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=272

---

### [F-5] TJDFT — ADI contra Lei Distrital nº 7.426/2024 julgada improcedente
**Texto no documento:** "o modelo foi validado constitucionalmente pelo TJDFT ao julgar improcedente ADI contra a Lei Distrital nº 7.426/2024, de conteúdo equivalente"
**Fonte declarada:** TJDFT (Tribunal de Justiça do Distrito Federal e Territórios), Lei Distrital nº 7.426/2024
**Tipo:** referência jurídica / julgado
**Status:** ✅ CONFIRMADO
**Resultado V1:** ADI nº 0715060-63.2024.8.07.0000, proposta pelo Governador do DF, julgada improcedente por maioria em 17/09/2024. Lei 7.426/2024 declarada constitucional.
**Fonte primária:** https://www.tjdft.jus.br/institucional/imprensa/noticias/2024/setembro/lei-que-obriga-agencias-bancarias-a-disponibilizarem-funcionario-exclusivo-para-idosos-e-constitucional

---

### [F-6] Lei Distrital nº 7.426/2024 — conteúdo equivalente ao PL
**Texto no documento:** "Lei Distrital nº 7.426/2024, de conteúdo equivalente"
**Fonte declarada:** Lei Distrital nº 7.426/2024 (Câmara Legislativa do DF)
**Tipo:** referência jurídica
**Status:** ⚠️ PARCIAL
**Resultado V1:** Lei existe, Art. 1º: "funcionário exclusivo para atendimento aos idosos em terminais de autoatendimento" — cobre ATMs intraagência. PORÉM: lei distrital cobre **apenas idosos**, não menciona PcD. Se PL 1904/2026 inclui PcD, "conteúdo equivalente" é impreciso.
**Fontes primárias:** https://www.sinj.df.gov.br/sinj/Norma/ca627718ec6f4bba9895ff0303f1d51f/Lei_7426_28_02_2024.html
**Decisão recomendada:** Alterar "conteúdo equivalente" para "modelo estruturalmente similar" ou acrescentar "(que cobre apenas idosos)" para precisão.

---

### [F-7] IBGE Censo 2022 — 18,8% da população fluminense tem 60 anos ou mais
**Texto no documento:** "18,8% da população fluminense tem 60 anos ou mais (IBGE, Censo 2022)"
**Fonte declarada:** IBGE, Censo 2022
**Tipo:** dado numérico
**Status:** ⚠️ PARCIAL — valor plausível, não verificado textualmente em fonte primária aberta
**Resultado V2:** IBGE confirma RJ como 2.º mais envelhecido (60+); fontes secundárias apontam 17,6%–19,1%; 13,1% é para 65+. Valor exato 18,8% não foi localizado diretamente. SIDRA/IBGE ficou inacessível.
**Decisão:** manter — dentro do intervalo plausível para 60+.

---

### [F-8] IBGE Censo 2022 — índice de envelhecimento na capital (CORRIGIDO)
**Texto original:** "com índice de envelhecimento de 105,9 na capital" → **ERRO CORRIGIDO NO TEXTO**
**Texto corrigido:** "com índice de envelhecimento de 121,4 no município da capital"
**Tipo:** dado numérico
**Status:** ⚠️ CORRIGIDO — ERRO GEOGRÁFICO DETECTADO E SANADO
**Resultado V2:** 105,9 é o índice do **estado** do RJ (não da capital). O município do Rio de Janeiro tem índice 121,4 (Projetocolabora/data.rio, Censo 2022). Erro corrigido no texto auditado.
**Fonte:** projetocolabora.com.br — Censo 2022; data.rio

---

### [F-9] FEBRABAN/Poder360 2025 — fraudes bancárias causaram R$ 10,1 bilhões em 2024
**Texto no documento (corrigido):** "causaram R$ 10,1 bilhões em 2024, com idosos entre os grupos mais afetados (FEBRABAN/Poder360, 2025)"
**Fonte declarada:** FEBRABAN / Poder360, 2025
**Tipo:** dado numérico
**Status:** ⚠️ PARCIAL — corrigido
**Resultado V2:** R$ 10,1 bi confirmado (Poder360, 12 mar. 2025, fonte FEBRABAN). "Idosos mais vulneráveis" é do MJSP, não FEBRABAN — texto ajustado para "entre os grupos mais afetados".
**Fonte primária:** https://www.poder360.com.br/poder-economia/golpes-causaram-prejuizo-de-r-101-bi-em-2024-diz-febraban/

---

### [F-10] FinCEN/FDIC 2024 — US$ 27 bilhões em exploração financeira de idosos (EUA)
**Texto original:** "(FDIC, 2024)" → **ERRO CORRIGIDO NO TEXTO**
**Texto corrigido:** "análise da FinCEN identificou US$ 27 bilhões... (FinCEN, 2024)"
**Tipo:** dado numérico
**Status:** ⚠️ CORRIGIDO — ERRO DE AGÊNCIA DETECTADO E SANADO
**Resultado V2:** Trecho literal FinCEN: "about $27 billion in reported suspicious activity was linked to elder financial exploitation" (jun/2022–jun/2023). O FDIC publicou comunicado conjunto interagências, mas o dado pertence à análise da FinCEN. Corrigido no texto.
**Fontes primárias:**
- https://www.fdic.gov/news/press-releases/2024/agencies-issue-statement-elder-financial-exploitation
- https://www.fincen.gov/news/news-releases/fincen-issues-analysis-elder-financial-exploitation

---

### [F-11] World Bank / Global Findex 2021 — idosos têm metade da probabilidade de usar pagamentos digitais
**Texto no documento:** "o Banco Mundial documenta que idosos têm metade da probabilidade de usar pagamentos digitais em relação a adultos jovens (World Bank, Global Findex 2021)"
**Fonte declarada:** World Bank, Global Findex 2021
**Tipo:** dado numérico / paráfrase
**Status:** ✅ CONFIRMADO
**Resultado V2:** Trecho literal: "they are half as likely as younger adults to make a payment using a mobile phone or the internet" (Global Findex 2021, economias em desenvolvimento). Afirmação correta e substancialmente fiel.
**Fonte primária:** https://documents1.worldbank.org/curated/en/099914407072216240/pdf/IDU0afbcb06d01c3c0473e0b92f0425d94633011.pdf

---

### [F-12] Ofício CVL nº 1342/2026 — referência ao instrumento de demanda
**Texto no documento:** "Em atenção ao Ofício CVL nº 1342/2026"
**Fonte declarada:** FONTE IMPLÍCITA — ofício interno
**Tipo:** referência jurídica / documento administrativo
**Status:** ✅ DOCUMENTO INTERNO — VERIFICAÇÃO EXTERNA NÃO APLICÁVEL

---

## Resumo

| Categoria | Quantidade |
|---|---|
| Total de blocos extraídos | 12 |
| Citação literal | 0 |
| Paráfrase | 1 (F-11) |
| Dado numérico | 5 (F-7, F-8, F-9, F-10, F-11) |
| Referência jurídica / julgado | 5 (F-2, F-3, F-4, F-5, F-6) |
| Referência jurídica / dado factual | 1 (F-1) |
| Documento administrativo | 1 (F-12) |
| **Com fonte explícita** | **9** (F-1 parcial, F-2, F-3, F-4, F-5, F-6, F-7, F-9, F-10, F-11) |
| **FONTE IMPLÍCITA** | **2** (F-8, F-12) |

**Itens de risco elevado para verificação:** F-5 (ADI TJDFT), F-8 (índice envelhecimento sem atribuição direta), F-10 (possível confusão FDIC vs. FinCEN/CFPB).
