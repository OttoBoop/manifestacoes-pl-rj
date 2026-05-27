# Auditoria de Fontes — Manifestação Técnica PL nº 1897/2026

**Data da auditoria:** 2026-05-26
**Arquivo auditado:** `manifestacao_PL-1897-2026-short.md`
**Auditor (extração):** Agente Extrator automatizado
**Auditor (verificação):** Agente Verificador Wave 2

---

## Blocos de Citação

---

### [F-1] Competência municipal — CF/1988, art. 30
**Texto no documento:** "A competência municipal é exercício legítimo do art. 30, I e II da CF/1988"
**Fonte declarada:** Constituição Federal de 1988, art. 30, incisos I e II
**Tipo:** referência jurídica
**Status:** ✅ CONFIRMADO
**Trecho localizado:** "Art. 30. Compete aos Municípios: I — legislar sobre assuntos de interesse local; II — suplementar a legislação federal e a estadual no que couber."
**Fonte verificada:** portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirBase=CF&abrirArtigo=30 + planalto.gov.br/ccivil_03/constituicao/constituicao.htm
**Nota:** Aplicação ao contexto do PL (criação de premiações municipais ao voluntariado) é consagrada pela doutrina e jurisprudência sobre art. 30 I.

---

### [F-2] Complementação da Lei Federal nº 9.608/1998
**Texto no documento:** "complementando a Lei Federal nº 9.608/1998"
**Fonte declarada:** Lei Federal nº 9.608/1998 (Lei do Voluntariado)
**Tipo:** referência jurídica
**Status:** ✅ CONFIRMADO
**Trecho localizado:** "Art. 1º Considera-se serviço voluntário, para fins desta Lei, a atividade não remunerada prestada por pessoa física a entidade pública de qualquer natureza ou a instituição privada de fins não lucrativos [...] Parágrafo único. O serviço voluntário não gera vínculo empregatício nem obrigação de natureza trabalhista, previdenciária ou afim."
**Fonte verificada:** https://www.planalto.gov.br/ccivil_03/leis/l9608compilado.htm
**Nota:** Lei existe, está em vigor, define serviço voluntário como não remunerado sem vínculo empregatício; conforme descrito na manifestação.

---

### [F-3] 57 milhões de voluntários ativos no Brasil
**Texto no documento:** "o Brasil conta com 57 milhões de voluntários ativos"
**Fonte declarada:** IDIS/Datafolha, 2021
**Tipo:** dado numérico
**Status:** ✅ CONFIRMADO
**Trecho localizado:** "O Brasil conta com 57 milhões de voluntários ativos, segundo Pesquisa Voluntariado no Brasil 2021 (IDIS/Datafolha)"
**Fonte verificada:** https://www.idis.org.br/o-brasil-conta-com-57-milhoes-de-voluntarios-ativos-segundo-pesquisa-voluntariado-no-brasil-2021/ + cobertura CNN Brasil, GIFE, Observatório 3º Setor
**Nota:** Número e terminologia ("ativos") confirmados no título oficial da pesquisa.

---

### [F-4] 34% da população com 16 anos ou mais é voluntária
**Texto no documento original:** "34% da população adulta" → **corrigido para** "34% da população com 16 anos ou mais"
**Fonte declarada:** IDIS/Datafolha, 2021
**Tipo:** dado numérico / percentual
**Status:** ⚠️ PARCIAL → ✅ CORRIGIDO
**Trecho localizado:** "34% dos brasileiros com 16 anos ou mais praticaram voluntariado" — equivale a ~57M da população de referência (16+, ~167M em 2021)
**Fonte verificada:** https://www.idis.org.br/o-brasil-conta-com-57-milhoes-de-voluntarios-ativos-segundo-pesquisa-voluntariado-no-brasil-2021/ (metodologia confirma base 16+)
**Discrepância DC-1:** O texto original usava "34% da população adulta" sem especificar faixa. A pesquisa IDIS usa "16 anos ou mais" como base — não a definição legal de adulto (18+). 34% × ~167M (pop. 16+ em 2021) ≈ 56,8M ≈ 57M — internamente consistente. Se lido como 18+, a conta divergiria (~53M em vez de 57M).
**Correção aplicada:** "34% da população adulta" → "34% da população com 16 anos ou mais"

---

### [F-5] 70% dos voluntários nunca ouviram falar dos ODS
**Texto no documento:** "70% deles nunca ouviram falar dos ODS"
**Fonte declarada:** IDIS/Datafolha, 2021
**Tipo:** dado numérico / percentual
**Status:** ✅ CONFIRMADO
**Trecho localizado:** "Com menos de 8 anos para o fim do prazo da Agenda 2030 da ONU, 70% dos voluntários brasileiros nunca ouviram falar da pauta" (título oficial IDIS); "70% dos respondentes não conhecem os Objetivos de Desenvolvimento Sustentável (ODS)" (corpo do comunicado).
**Fonte verificada:** https://www.idis.org.br/com-menos-de-8-anos-para-o-fim-do-prazo-da-agenda-2030-da-onu-70-dos-voluntarios-brasileiros-nunca-ouviram-falar-da-pauta/
**Nota:** Dado consistente em múltiplas fontes IDIS.

---

### [F-6] 862 milhões de voluntários mensais no mundo
**Texto no documento:** "O Programa das Nações Unidas para os Voluntários estima 862 milhões de voluntários mensais no mundo"
**Fonte declarada:** UNV, *State of the World's Volunteerism Report*, 2022
**Tipo:** dado numérico
**Status:** ✅ CONFIRMADO
**Trecho localizado:** "globally 862 million people (aged 15 years and older) perform one or another form of volunteering activity every month, representing 11 percent of the total global population"
**Fonte verificada:** https://knowledge.unv.org/evidence-library/2022-state-of-the-worlds-volunteerism-report-building-equal-and-inclusive-societies + https://swvr2022.unv.org/
**Nota:** O relatório UNV especifica base etária "15 anos ou mais". O termo "mensalmente" é adequado: o relatório usa "every month".

---

### [F-7] UNV reconhece parcerias voluntários-governos como vitais à Agenda 2030
**Texto no documento original:** "condição necessária ao alcance da Agenda 2030" → **corrigido para** "são 'vitais' para o alcance da Agenda 2030"
**Fonte declarada:** UNV, *State of the World's Volunteerism Report*, 2022
**Tipo:** paráfrase
**Status:** ⚠️ PARCIAL → ✅ CORRIGIDO
**Trecho localizado (UNV original):** "the ways in which volunteers and state authorities interact, collaborate and partner are vital for the achievement of the 2030 Agenda for Sustainable Development"
**Fonte verificada:** https://www.unv.org/news/state-worlds-volunteerism-report-launched-kenya-urges-cooperation-between-volunteers-and + https://knowledge.unv.org/evidence-library/2022-state-of-the-worlds-volunteerism-report-building-equal-and-inclusive-societies
**Discrepância DC-2:** O UNV usa "vital" (crucial, essencial) — a manifestação original parafraseou como "condição necessária", expressão logicamente mais forte (implica impossibilidade sem parceria). O sentido geral é compatível, mas a tradução elevava a intensidade retórica.
**Correção aplicada:** "condição necessária" → "são 'vitais' para o alcance da Agenda 2030"

---

### [F-8] Lei Federal nº 14.370/2022 adota "premiação" como política pública
**Texto no documento:** "A Lei Federal nº 14.370/2022 já adota o instrumento 'premiação' como política pública"
**Fonte declarada:** Lei Federal nº 14.370/2022
**Tipo:** referência jurídica
**Status:** ✅ CONFIRMADO
**Trecho localizado:** "O Prêmio Portas Abertas tem a finalidade de reconhecer e condecorar os entes federativos que se destacarem na implementação do Programa Nacional de Prestação de Serviço Civil Voluntário."
**Fonte verificada:** https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/Lei/L14370.htm (Lei 14.370, de 15/06/2022)
**Nota:** Lei 14.370/2022 cria o Programa Nacional de Prestação de Serviço Civil Voluntário com foco em jovens 18-29, 50+ sem emprego formal e PcD. O Prêmio Portas Abertas é a dimensão de reconhecimento institucional. A manifestação usa corretamente o prêmio como analogia para o instrumento "premiação como política pública".

---

### [F-9] Lei Municipal nº 6.906/2021 — lei base alterada pelo PL
**Texto no documento:** "acrescenta disposições à Lei Municipal nº 6.906/2021"
**Fonte declarada:** Lei Municipal nº 6.906/2021 (Rio de Janeiro)
**Tipo:** referência jurídica
**Status:** ✅ CONFIRMADO
**Trecho localizado:** "Adota a Agenda 2030 para o Desenvolvimento Sustentável como diretriz para a promoção de Políticas Públicas Municipais, cria o programa e a comissão para os objetivos de desenvolvimento sustentável, e dá outras providências."
**Fonte verificada:** https://e.camara.rj.gov.br/Arquivo/Documents/legislacao/html/l69062021.html (Câmara Municipal Rio de Janeiro — arquivo HTML oficial)
**Nota DC-3:** A lei 6.906/2021 tem foco principal na Agenda 2030/ODS. O nome "Viva Voluntário" pode referir-se ao programa criado em seu interior, mas não consta na ementa. Risco baixo: o PL 1897/2026 cita corretamente essa lei como base a ser alterada.

---

### [F-10] PL acrescenta Capítulo II-A com quatro categorias de premiação
**Texto no documento:** "O PL acrescenta o Capítulo II-A à Lei Municipal nº 6.906/2021, instituindo o Prêmio Viva Voluntário em quatro categorias (sociedade civil, ambiental, comunitário e setor público)"
**Fonte declarada:** FONTE IMPLÍCITA — texto do próprio PL nº 1897/2026
**Tipo:** paráfrase (do texto do PL)
**Status:** ✅ CONFIRMADO
**Trecho localizado:** "Art. 1º A Lei nº 6.906, de 24 de maio de 2021, fica acrescida do Capítulo II-A com as seguintes disposições: [...] Art. 13-A. [...] nas seguintes categorias de Voluntariados: I — voluntariado nas organizações da sociedade civil; II — voluntariado no setor ambiental; III — voluntariado no setor comunitário; e IV — voluntariado no setor público."
**Fonte verificada:** texto_extraido.md (OCR via NB)
**Nota:** Capítulo II-A tem 4 artigos (13-A a 13-D). A manifestação descreve corretamente.

---

### [F-11] Art. 2º do PL delega regulamentação ao Executivo
**Texto no documento:** "delega a regulamentação ao Executivo (Art. 2º)"
**Fonte declarada:** FONTE IMPLÍCITA — texto do próprio PL nº 1897/2026, Art. 2º
**Tipo:** referência jurídica (ao PL)
**Status:** ✅ CONFIRMADO
**Trecho localizado:** "Art. 2º O Poder Executivo regulamentará esta Lei no que couber."
**Fonte verificada:** texto_extraido.md
**Nota:** A qualificação técnica da manifestação ("sem balizas mínimas legais") é sustentada pelo texto: nenhum critério de seleção, composição de julgador ou periodicidade está fixado no PL.

---

### [F-12] Art. 13-C é excessivamente amplo
**Texto no documento:** "o Art. 13-C é excessivamente amplo, podendo dificultar a priorização operacional"
**Fonte declarada:** FONTE IMPLÍCITA — juízo técnico da Subsecretaria sobre o texto do PL
**Tipo:** paráfrase (opinião técnica)
**Status:** ✅ CONFIRMADO
**Trecho localizado:** "Art. 13-C. Consideram-se atividades referentes ao Prêmio Viva Voluntária a iniciativa não remunerada de pessoas físicas e pessoas jurídicas, isoladas ou conjuntamente, prestada à pessoa física, a órgão ou à entidade da Administração Pública ou entidade privada sem fins lucrativos, que tenha objetivos de desenvolvimento sustentável, culturais, educacionais, científicos, recreativos, ambientais, de assistência à pessoa ou de promoção e defesa dos direitos humanos e dos animais, que vise ao benefício e à transformação da sociedade."
**Fonte verificada:** texto_extraido.md
**Nota:** A qualificação "excessivamente amplo" é tecnicamente sustentável: o artigo lista 8+ categorias de objetivos sem delimitação de prioridade, inclui pessoas jurídicas (incomum em lei de voluntariado), e abrange desde cultura e recreação até direitos dos animais.

---

## Resumo por Tipo

| Tipo | Quantidade | Blocos |
|---|---|---|
| Dado numérico / percentual | 4 | F-3, F-4, F-5, F-6 |
| Referência jurídica | 5 | F-1, F-2, F-8, F-9, F-11 |
| Paráfrase | 3 | F-7, F-10, F-12 |
| **Total** | **12** | — |

---

## Resultado Wave 2

| Status | Blocos | Ação |
|---|---|---|
| ✅ CONFIRMADO | F-1, F-2, F-3, F-5, F-6, F-8, F-9, F-10, F-11, F-12 | Nenhuma |
| ⚠️ CORRIGIDO | F-4, F-7 | Correções aplicadas no short |
| ❓ INVERIFICÁVEL | — | — |

**Placar final:** 10 ✅ + 2 ⚠️ corrigidos + 0 ❓

---

## Decisões aplicadas ao texto

| Bloco | Discrepância | Decisão | Texto anterior | Texto final |
|---|---|---|---|---|
| F-4 | Base etária IDIS é 16+, não 18+ | CORRIGIR | "34% da população adulta" | "34% da população com 16 anos ou mais" |
| F-7 | UNV usa "vital", não "condição necessária" | CORRIGIR | "condição necessária ao alcance da Agenda 2030" | "são 'vitais' para o alcance da Agenda 2030" |
