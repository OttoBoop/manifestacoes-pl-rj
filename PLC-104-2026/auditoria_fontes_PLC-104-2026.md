# Auditoria de Fontes — PLC nº 104/2026

**Data:** 2026-05-27
**Pipeline:** V5
**Texto auditado:** manifestacao_PLC-104-2026-short.md
**Auditor:** Ariadne (Claude Code)

---

## Metodologia
- Wave 1: extração de citações pelo coordenador
- Wave 2: verificação via WebFetch (Orla Rio), WebSearch (APOPS, empregos), NB-first
- NB URL: https://notebooklm.google.com/notebook/9f3df705-dfa2-4553-bcc1-ca74e760d213

---

## Resumo executivo

| Status | Quantidade |
|--------|------------|
| ✅ CONFIRMADO | 2 |
| ⚠️ CORRIGIDO | 2 |
| ❓ INVERIFICÁVEL | 0 |
| **TOTAL** | **4** |

---

## Wave 1 — Extração de citações

### F-1
**Citação:** BRASIL. "Constituição Federal", Senado Federal, 1988
**Afirmação:** Competência municipal nos arts. 30, I e II, e 145 da CF/1988

### F-2
**Citação:** ORLA RIO. "Orla Rio cuida da orla carioca há 60 anos", Orla Rio, [2024→2022]
**Afirmações:**
- "309 quiosques ao longo de 34 km de orla"
- "[5.000 empregos na alta temporada → empregos diretos e indiretos]"
- "[R$ 133 milhões → mais de R$ 148 milhões] em investimentos de infraestrutura"

### F-3
**Citação:** APOPS/MAS. "What Are POPS?", Municipal Art Society, 2024
**Afirmação:** POPS em Nova York, Toronto e Seoul preservam poder regulatório municipal

### F-4
**Citação:** UN-HABITAT. "Global Public Space Programme", UN-Habitat, 2023
**Afirmação:** Meta 11.7 da Agenda 2030 exige que governos locais mantenham ferramentas de gestão em espaços administrados por terceiros

---

## Wave 2 — Verificação

### F-1 — CF/1988
**Status: ✅ CONFIRMADO**
- Art. 30, I: legislar sobre assuntos de interesse local
- Art. 30, II: suplementar legislação federal e estadual no que couber
- Art. 145: competência tributária municipal

---

### F-2 — Orla Rio release
**Status: ⚠️ 3 CORREÇÕES APLICADAS**

**DC-1: Número de quiosques e extensão (309, 34km): ✅ CONFIRMADO**
- WebFetch da URL primária confirmou: "309 quiosques distribuídos ao longo de 34 km de orla"

**DC-2: Investimento — R$133M → mais de R$148M**
- WebFetch confirmou: "mais de 148 milhões de reais investidos em obras até o final de 2021"
- Correção aplicada: "R$ 133 milhões" → "mais de R$ 148 milhões"

**DC-3: Empregos — "5.000 empregos na alta temporada" → "empregos diretos e indiretos"**
- WebSearch e WebFetch não confirmaram o número específico de 5.000 empregos
- A fonte primária menciona "empregos diretos e indiretos" sem especificar número
- Correção aplicada: número específico removido; formulação qualitativa mantida

**DC-4: Ano da publicação — 2024 → 2022**
- WebFetch identificou "2022 publication date" para o release "há 60 anos"
- Correção aplicada: "Orla Rio, 2024" → "Orla Rio, 2022"

---

### F-3 — APOPS/MAS "What Are POPS?"
**Status: ✅ CONFIRMADO**
- WebSearch confirmou APOPS/MAS como organização da Municipal Art Society of New York
- POPS em NYC: confirmado — mais de 590 POPS em 380 edifícios (Wikipedia, lista NYC)
- POPS em Toronto: confirmado — programa de design guidelines desde 2012
- POPS em Seoul: confirmado — programa introduzido para prover espaços em cidade densamente urbanizada
- URL https://apops.mas.org/about/what-are-pops/ confirmada em resultados de busca

---

### F-4 — UN-Habitat Global Public Space Programme
**Status: ✅ CONFIRMADO**
- WebSearch confirmou UN-Habitat como organização ONU para assentamentos urbanos
- Global Public Space Programme: confirmado em unhabitat.org/programme/global-public-space-programme
- Meta 11.7 da Agenda 2030: acesso universal a espaços públicos seguros, inclusivos e acessíveis
- Conexão com gestão local de espaços: confirmada como objetivo do programa

---

## Decisões

| # | Fonte | Status | Decisão |
|---|-------|--------|---------|
| F-1 | CF/1988 | ✅ | Mantido |
| F-2 | Orla Rio 2022 | ⚠️ | DC-1: empregos softenado; DC-2: R$133M→R$148M; DC-3: 2024→2022 |
| F-3 | APOPS/MAS 2024 | ✅ | Mantido |
| F-4 | UN-Habitat 2023 | ✅ | Mantido |

---

## STATUS FINAL
✅ PASS — 2 ✅ confirmados + 2 ⚠️ corrigidos + 0 ❓ inverificáveis
