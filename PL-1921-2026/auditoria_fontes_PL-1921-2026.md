# Auditoria de Fontes — PL nº 1921/2026

**Data:** 2026-05-27
**Pipeline:** V5
**Texto auditado:** manifestacao_PL-1921-2026-short.md
**Auditor:** Ariadne (Claude Code) + agente verificador

---

## Metodologia
- Wave 1: extração de citações pelo coordenador
- Wave 2: verificação via agente + WebFetch FBSP + WebSearch UN Women + UN/DESA SDGs
- NB URL: https://notebooklm.google.com/notebook/981be072-0a76-4e7e-9031-6ad44ad42fc1
- Nota: browser state NB expirado — verificações feitas via fonte primária direta

---

## Resumo executivo

| Status | Quantidade |
|--------|------------|
| ✅ CONFIRMADO | 1 |
| ⚠️ CORRIGIDO | 3 |
| ❓ INVERIFICÁVEL | 0 |
| **TOTAL** | **4 afirmações** |

---

## Wave 1 — Extração de citações

### F-1
**Citação:** BRASIL. "Constituição Federal", Senado Federal, 1988
**Afirmação:** Competência municipal nos arts. 30, I e II, e 226, §8º, da CF/1988

### F-2
**Citação:** FBSP. "19º Anuário Brasileiro de Segurança Pública", Fórum Brasileiro de Segurança Pública, 2025
**Afirmações:**
- F-2a: 4 mulheres vítimas de feminicídio a cada 24 horas no Brasil
- F-2b: 1.492 casos de feminicídio em 2024

### F-3
**Citação:** UN WOMEN. "Facts and Figures: Ending Violence Against Women", UN Women, 2025
**Afirmação:** menos de 40% das vítimas buscam qualquer ajuda; maioria recorre a família, não a serviços formais

### F-4
**Citação:** ONU. "Goal 5 — Gender Equality", UN/DESA, 2015
**Afirmação:** ODS 5 da Agenda 2030 estabelece a eliminação de todas as formas de violência contra mulheres como compromisso internacional do Brasil

---

## Wave 2 — Verificação

### F-1 — CF/1988
**Status: ✅ CONFIRMADO**
- Art. 30, I: "legislar sobre assuntos de interesse local"
- Art. 30, II: "suplementar a legislação federal e a estadual no que couber"
- Art. 226, §8º: "O Estado assegurará a assistência à família na pessoa de cada um dos que a integram, criando mecanismos para coibir a violência no âmbito de suas relações."

---

### F-2 — FBSP 19º Anuário 2025
**Status: ⚠️ CORRIGIDO (número do anuário corrigido)**
- Afirmação original citava "18º Anuário" com os mesmos dados
- Os dados 2024 (1.492 casos; razão de ~4/dia) constam do 19º Anuário Brasileiro de Segurança Pública (FBSP, 2025), referente ao ano-base 2024
- Correção aplicada: citação atualizada para "19º Anuário Brasileiro de Segurança Pública", FBSP, 2025

---

### F-3 — UN Women 2025
**Status: ⚠️ CORRIGIDO (afirmação original substituída)**
- Afirmação original: "vítimas buscam ajuda por proximidade geográfica" — não localizada no documento UN Women "Facts and Figures"
- O que UN Women 2025 realmente documenta: menos de 40% das vítimas de violência por parceiro íntimo buscam qualquer tipo de ajuda; entre as que buscam, a maioria recorre à família e amigos, não a serviços formais
- Correção aplicada: "menos de 40% das vítimas buscam qualquer ajuda e a maioria recorre a família, não a serviços formais"

---

### F-4 — ONU SDG 5
**Status: ⚠️ CORRIGIDO (adjetivo "vinculante" removido)**
- Afirmação original: "meta global vinculante"
- Os ODS são compromissos voluntários dos Estados-membros, não tratados vinculantes
- Correção aplicada: "compromisso internacional do Brasil" (sem "vinculante")

---

## Decisões

| # | Fonte | Status | Decisão |
|---|-------|--------|---------|
| F-1 | CF/1988 | ✅ | Mantido |
| F-2 | FBSP 19º Anuário 2025 — 1.492 feminicídios | ⚠️ | Corrigido: "18º" → "19º Anuário" |
| F-3 | UN Women 2025 — vítimas e busca de ajuda | ⚠️ | Corrigido: "proximidade geográfica" → "<40% buscam ajuda, maioria recorre a família" |
| F-4 | ONU Goal 5 / SDG 5 | ⚠️ | Corrigido: "vinculante" → "compromisso internacional" |

---

## STATUS FINAL
✅ PASS — 1 ✅ confirmado + 3 ⚠️ corrigidos + 0 ❓ inverificáveis
