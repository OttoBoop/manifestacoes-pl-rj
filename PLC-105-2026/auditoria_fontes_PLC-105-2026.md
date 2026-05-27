# Auditoria de Fontes — PLC nº 105/2026

**Data:** 2026-05-27
**Pipeline:** V5
**Texto auditado:** manifestacao_PLC-105-2026-short.md
**Auditor:** Ariadne (Claude Code) + agente verificador

---

## Metodologia
- Wave 1: extração de citações pelo coordenador
- Wave 2: verificação via agente + WebFetch direto IEA PDF + WebSearch ABVE + EUR-Lex
- NB URL: https://notebooklm.google.com/notebook/12549c7c-0ca9-4a00-92b7-fdab481d7315
- Nota: browser state NB expirado (20,5 dias) — verificações feitas via fonte primária direta

---

## Resumo executivo

| Status | Quantidade |
|--------|------------|
| ✅ CONFIRMADO | 2 |
| ⚠️ CORRIGIDO | 3 |
| ❓ INVERIFICÁVEL | 0 |
| **TOTAL** | **5 afirmações** |

---

## Wave 1 — Extração de citações

### F-1
**Citação:** BRASIL. "Constituição Federal", Senado Federal, 1988
**Afirmação:** Competência municipal nos arts. 30, I e II, e 182 da CF/1988

### F-2
**Citação:** ABVE. "Painel de Dados do Setor de Mobilidade Elétrica", Associação Brasileira do Veículo Elétrico, 2025
**Afirmações:**
- F-2a: 61.615 emplacamentos de veículos 100% elétricos em 2024
- F-2b (⚠️ corrigido antes de publicar): crescimento de 219% removido — não localizado no release primário ABVE
- F-2c: frota eletrificada acumulada que ultrapassou 700 mil unidades no primeiro trimestre de 2026

### F-3
**Citação:** IEA. "Global EV Outlook 2025", International Energy Agency, 2025
**Afirmação (⚠️ corrigida):** ~25 veículos por ponto no Brasil, ante 10:1 na China e 13:1 na UE; mais de 12 mil pontos públicos em dez/2024

### F-4
**Citação:** EU. "Energy Performance of Buildings Directive — Directive (EU) 2024/1275", European Commission, 2024
**Afirmação:** UE tornou obrigatória a pré-instalação de eletrodutos em novos edifícios

---

## Wave 2 — Verificação

### F-1 — CF/1988
**Status: ✅ CONFIRMADO**
- Art. 30, I: "legislar sobre assuntos de interesse local"
- Art. 30, II: "suplementar a legislação federal e a estadual no que couber"
- Art. 182: "política de desenvolvimento urbano, executada pelo Poder Público municipal"

---

### F-2 — ABVE 2025
**F-2a — 61.615 BEV em 2024: ✅ CONFIRMADO**
- Release ABVE "Eletrificados superam previsões...2024": 61.615 unidades BEV confirmado
- Fonte secundária (eixos.com.br): "64 mil híbridos (PHEV) e 61,6 mil a bateria (BEV)"

**F-2b — 219% crescimento: ⚠️ CORRIGIDO (removido antes de publicar)**
- Número 219% não localizado no release primário ABVE
- Aparece apenas em repercussões jornalísticas citando ABVE (não fonte primária)
- Decisão: percentual removido; apenas 61.615 mantido como dado confirmado

**F-2c — 700 mil unidades: ⚠️ CORRIGIDO**
- Marco de 700 mil = março de 2026 (705.648 unidades acumuladas jan/2012–mar/2026)
- Correção aplicada: "700 mil unidades no primeiro trimestre de 2026" (documento é de maio/2026 → temporalmente correto)

---

### F-3 — IEA Global EV Outlook 2025
**Status: ⚠️ CORRIGIDO (afirmação original substituída)**
- Afirmação original ("18 veículos/ponto, parâmetro 10:1 para redes maduras"): incorreta
- IEA GEO 2025 cita Brasil: "more than 12,000 public charging points across the country" (dec/2024)
- IEA cita China: "1 charger for every 10 electric cars"; UE: "1 charger for every 13 electric cars"
- "10:1 como parâmetro de redes maduras" inverte a lógica — Oslo (mercado mais maduro) tem >30:1
- Correção aplicada: "mais de 12 mil pontos no Brasil em dez/2024 — razão de ~25 veículos/ponto, ante 10:1 na China e 13:1 na UE"

---

### F-4 — Diretiva EU 2024/1275 (EPBD)
**Status: ⚠️ CORRIGIDO (fonte trocada)**
- Afirmação original citava "Regulation (EU) 2023/1804" (AFIR) — incorreto
- AFIR regula infraestrutura de acesso público em vias, portos e aeroportos (não edifícios)
- Obrigação de pré-instalação de eletrodutos em novos edifícios = Directive (EU) 2024/1275 (EPBD)
  - Vigente desde 28/05/2024; transposição pelos EM até 29/05/2026
- Correção aplicada: citação trocada para "Energy Performance of Buildings Directive — Directive (EU) 2024/1275", European Commission, 2024

---

## Decisões

| # | Fonte | Status | Decisão |
|---|-------|--------|---------|
| F-1 | CF/1988 | ✅ | Mantido |
| F-2a | ABVE 2025 — 61.615 BEV | ✅ | Mantido |
| F-2b | ABVE — 219% | ⚠️ | Removido (não em fonte primária) |
| F-2c | ABVE — 700K frota | ⚠️ | Corrigido: "primeiro trimestre de 2026" |
| F-3 | IEA GEO 2025 | ⚠️ | Corrigido: 12K pontos + China 10:1 + UE 13:1 |
| F-4 | EU — EPBD 2024/1275 | ⚠️ | Corrigido: AFIR→EPBD |

---

## STATUS FINAL
✅ PASS — 2 ✅ confirmados + 3 ⚠️ corrigidos + 0 ❓ inverificáveis
