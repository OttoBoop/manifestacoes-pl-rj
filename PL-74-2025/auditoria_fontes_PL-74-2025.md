# Auditoria de Fontes — Manifestação Técnica PL 74/2025

**Texto auditado:** `manifestacao_PL-74-2025.md`  
**NB URL:** https://notebooklm.google.com/notebook/192029b0-017e-4bfa-85f0-b6fa25a28b8e  
**NB inventário real:** 6 fontes (via list_sources.py)  
**Data:** 2026-05-07  
**Status:** Wave 2 concluída — aguardando decisões do usuário  

---

## Metodologia

- NB-first obrigatório: toda busca começa no NotebookLM
- "Confirmado" exige trecho literal ou paráfrase substanciada + URL
- Nunca declarar inexistência — apenas "não localizei após protocolo"
- **Decisões de cortar/manter/reescrever são do usuário**

---

## Resumo executivo

| Status | Quantidade |
|--------|-----------|
| ✅ Confirmado | 7 |
| ⚠️ Parcial / divergência | 8 |
| ❓ Inverificável | 0 |
| IMPLÍCITA s/ problemas | 3 |
| Achados editoriais | 6 |
| **Total citações auditadas** | **20** |

---

## Decisões necessárias do usuário

> Estas são as correções que requerem sua escolha. Registre sua decisão na última coluna.

| ID | Citação/Afirmação | Problema encontrado | Opções | Decisão |
|----|-------------------|--------------------|----|---------|
| D-01 | "20.662 empreendimentos econômicos solidários" + IPEA/SENAES 2016 | IPEA/SENAES 2016 diz **19.708**, não 20.662. O 20.662 aparece em publicação do MTE sobre a Lei Paul Singer (fonte distinta) | (a) Manter 20.662 e trocar a fonte para MTE/Lei Paul Singer; (b) Corrigir para 19.708 mantendo IPEA/SENAES | — |
| D-02 | "movimentando cerca de R$ 50 bilhões anuais — aproximadamente 3% do PIB nacional" | Na fonte SEBRAE/CRAB: R$102bi está vinculado ao 3% do PIB; R$50bi é "receita do mercado" (conceito distinto). Combinar R$50bi + 3% PIB é inconsistente | (a) Usar "R$102 bilhões anuais — aproximadamente 3% do PIB"; (b) Usar "R$50 bilhões anuais" sem citar 3% PIB | — |
| D-03 | "Circuito Carioca de Artesanato registrou crescimento de 52%" | Fonte usa "Circuito Rio Ecosol", nunca "Circuito Carioca de Artesanato". O percentual 52% é cálculo do autor (não declarado na fonte) | (a) Corrigir nome para "Circuito Rio Ecosol" + remover "52%" e usar só "R$1 milhão a mais"; (b) Manter com nota explicativa | — |
| D-04 | "Súmula Vinculante 38 do STF" para competência municipal | SV 38 trata de **horário de funcionamento de comércio** ("É competente o Município para fixar o horário de funcionamento de estabelecimento comercial") — não de competência municipal geral | (a) Substituir SV38 por "art. 30, I e V, da CF/88 + RE 586.224 (Tema 145 RG)"; (b) Manter SV38 com qualificação "por aplicação analógica do art. 30, I, CF" | — |
| D-05 | Decreto Rio 48.753/2021 como fonte da competência da SEOP para feiras | A competência específica para "feiras em áreas públicas" está no **Decreto Rio 51.958/2023** (art. 16), não no 48.753/2021. O 48.753 estabelece o quadro geral, mas não o dispositivo literal citado | (a) Trocar citação para Decreto 51.958/2023; (b) Manter 48.753 com nota sobre a cadeia normativa | — |
| D-06 | Curitiba (Lei 14.786/2016) citada como exemplo de município com regulamentação bem-sucedida | Nenhuma fonte para Curitiba no inventário ou no texto. O dado de Curitiba não tem referência bibliográfica | (a) Adicionar fonte para Curitiba (Câmara Curitiba 2016 — disponível no inventário F-4.4); (b) Remover Curitiba e manter só BH | — |
| D-07 | R$2,9mi em 2016 e "R$1,9 milhão em 2015" | R$2,9mi confirmado na fonte. R$1,9mi é implícito (2,9 – 1,0 = 1,9), não declarado explicitamente. "52%" calculado | (a) Reescrever para "passando de cerca de R$1,9 milhão em 2015 (estimado) para R$2,9 milhões"; (b) Simplificar para "R$2,9 milhões em 2016, cerca de R$1 milhão a mais que em 2015" (mais fiel à fonte) | — |
| D-08 | PRANDINO 2021 — "sem comprometer a titularidade estatal" | Artigo existe e co-autoria confirmada (Diego Prandino + Paloma Oliveira — co-autora omitida). "Titularidade estatal" não localizada no resumo público (pode estar no corpo do artigo) | (a) Reformular como paráfrase sem aspas + adicionar co-autora; (b) Manter como paráfrase + nota "acesso ao corpo do artigo pendente" | — |

---

## Citações confirmadas ✅

| ID | Afirmação | Fonte | Trecho confirmado |
|----|-----------|-------|-------------------|
| C-08 | 216 feiras, 300→600 empreendedores, R$2mi — Niterói | PREFEITURA DE NITERÓI, 2022 | "Ao longo de 2022, foram realizadas 216 feiras [...] que movimentaram mais de R$ 2 milhões [...] dobrou o número de empreendedores [...] de 300 para 600" |
| C-06 | "ganhos multidimensionais" superiores às formas informais | SILVA, A. L. F., 2017 | "uma feira de economia solidária possibilita a geração de ganhos multidimencionais" (grafia original) ⚠️ Nota: autor é da UFBA; periódico é da UnB |
| C-10 | Lei 15.068/2024 (Lei Paul Singer) — número correto | Planalto/NB, 2024 | Lei nº 15.068, de 23 de dezembro de 2024 — confirmado |
| C-14 | 1,423 milhão de trabalhadores — IPEA/SENAES 2016 | IPEA/SENAES, 2016 | "Ao todo, estão envolvidos nesses EES 1.423.631 pessoas associadas" (mas associado a 19.708 EES, não 20.662) |
| C-15 parcial | 8,5 mi artesãos, 77% mulheres | SEBRAE/CRAB, 2024 | "O setor engloba aproximadamente 8,5 milhões de artesãos, sendo 77% mulheres" ✅ |
| C-16 | 300 artesãos, 19 Redes, 90% mulheres, 13+ pontos fixos | CÂMARA RJ, 2025 | Confirmado via NB (fonte presente no notebook) |
| C-12 parcial | SEOP competente para eventos em áreas públicas (geral) | Decreto 48.753/2021 | Decreto existe e atribui competências à SEOP — mas especificidade para feiras está no Decreto 51.958/2023 (ver D-05) |

---

## Citações parcialmente confirmadas ⚠️

(Ver tabela de Decisões acima — D-01 a D-08)

---

## Afirmações implícitas sem fonte (sem problema técnico)

| ID | Afirmação | Status |
|----|-----------|--------|
| C-13 | "sistema Rio Mais Fácil Eventos demanda pareceres de múltiplos órgãos" | Aceitável como conhecimento tácito do processo administrativo municipal; pode ser fundamentada no Decreto 51.958/2023 se necessário |
| C-18 | "regulamentação deve nomear expressamente o órgão emissor" | Recomendação técnica do redator — aceitável |
| C-19 | Prazo de 90 dias para CVS/RJ | Recomendação do redator — aceitável como discricionariedade técnica |

---

## Achados editoriais

| AE | Descrição | Gravidade | Ação recomendada |
|----|-----------|-----------|-----------------|
| AE-01 | Curitiba sem fonte | Alta | Ver D-06 |
| AE-02 | Título SEBRAE: "tecida a mãos" deve ser "tecida à mão" | Baixa | Corrigir na próxima revisão |
| AE-03 | Sigla CRAB não identificada no texto | Baixa | CRAB = Centro de Referência do Artesanato Brasileiro (identificado nos pesquisadores) |
| AE-04 | Dados IPEA 2016 usados em 2026 (10 anos de defasagem) | Média | Adicionar nota "(dados de 2016, mais recente disponível)" |
| AE-05 | Lei 7.008/2021 descrita via notícia, não via texto legal | Baixa | Aceitável em manifestação técnica; ou adicionar citação do Diário Oficial |
| AE-06 | SV 38 pertinência | Alta | Ver D-04 |

---

## Nota sobre SILVA 2017

- Autor: André Luis Ferreira da Silva — da **UFBA** (Universidade Federal da Bahia)
- Periódico: **Mundo do Trabalho Contemporâneo** (MTC), publicado pela **UnB**
- A citação "(UnB, 2017)" pode induzir interpretação equivocada (autor sendo da UnB)
- Sugestão: "(SILVA, A. L. F. 'A metodologia de construção das feiras...', Mundo do Trabalho Contemporâneo, UFBA/UnB, 2017)"

---

## Log de execução

### Wave 0 — Preparação
- ✅ Esqueleto criado
- ✅ NB inventário via list_sources.py: 6 fontes

### Wave 1 — Extração
- ✅ 20 citações catalogadas + 6 achados editoriais
- Extrator identificou AE-06 (SV38 pertinência) e AE-01 (Curitiba sem fonte)

### Wave 2 — Verificação paralela
- ✅ Verificador A: lei 15.068 ✅ | faturamento ⚠️ (D-02) | SV38 ⚠️ (D-04)
- ✅ Verificador B: vendas 2016 ⚠️ (D-03/D-07) | Niterói ✅ | SILVA 2017 ✅
- ✅ Verificador C: PRANDINO ⚠️ (D-08) | Decreto ⚠️ (D-05) | IPEA ⚠️ (D-01)
- ✅ Coordenador verificou SV38 diretamente: confirmou "horário comercial"

### Wave 3 — Aguardando usuário
- ⏳ 8 decisões pendentes (D-01 a D-08)
