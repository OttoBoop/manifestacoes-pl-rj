# V5-AUDIT — PL nº 1897/2026

**Data de processamento:** 2026-05-26
**Pipeline versão:** V5
**Arquivo auditado:** manifestacao_PL-1897-2026-short.md
**Ofício:** CVL nº 1276/2026
**Posição:** Nada a opor

---

## Checklist V5

| Critério | Status | Observação |
|----------|--------|------------|
| texto_extraido.md ≥ 200 palavras úteis | ✅ | OCR via NB — 4 artigos completos + justificativa |
| NB criado + ≥2 EN fontes indexadas | ✅ | sdgs.un.org (EN) + UNDP (EN) + PL PDF (PT) = 3 usáveis |
| manifestacao-short ≥ 4 citações | ✅ | 6 citações (Lei 6.906, CF/1988, IDIS/Datafolha, UNV 2022, Lei 14.370, Lei 9.608) |
| ≥1 citação internacional no short | ✅ | UNV State of World's Volunteerism 2022 (EN) |
| audit_sources Wave 1+2 aplicado | ✅ | 10 ✅ + 2 ⚠️ corrigidos + 0 ❓ |
| PDF gerado ≤ 1 página | ✅ | 1 página, 14 KB, 321 palavras |
| V5-AUDIT.md criado | ✅ | Este arquivo |
| commit + push para manifestacoes-pl-rj | ✅ | Concluído |

---

## Fontes do NB (inventário list_sources.py)
- SEI_000184.002513_2026_91.pdf (PL original — OCR)
- THE 17 GOALS | Sustainable Development (sdgs.un.org — EN)
- Sustainable Development Goals | UNDP (undp.org — EN)
- [2 fontes com erro/404 — não usadas]

---

## Flags da pesquisa para audit_sources
1. **F-T2.7** (RLV Rio — Global Evaluation Initiative): URL retornou 404 — não incluída no short. Verificar se existe página alternativa na Prefeitura do Rio.
2. **F-T4.1** (PNADC 2022): PDF do IBGE ficou inacessível; dado confirmado por fontes secundárias convergentes — verificar diretamente em biblioteca.ibge.gov.br.
3. **F-T2.3** (A/69/700): citação pode ser do UNV PDF citando o documento ONU — verificar atribuição antes de usar em versão longa.

---

## Correções aplicadas (audit)
- F-4: "34% da população adulta" → "34% da população com 16 anos ou mais" (base IDIS é 16+)
- F-7: "condição necessária" → "são 'vitais'" (fidelidade ao trecho original UNV SWVR 2022)

## STATUS
✅ PASS — 10 ✅ confirmados + 2 ⚠️ corrigidos + 0 ❓ inverificáveis
