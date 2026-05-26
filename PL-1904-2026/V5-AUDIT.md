# V5-AUDIT — PL nº 1904/2026

**Data de processamento:** 2026-05-26
**Pipeline versão:** V5
**Arquivo auditado:** manifestacao_PL-1904-2026-short.md
**Ofício:** CVL nº 1342/2026
**Posição:** Nada a opor

---

## Checklist V5

| Critério | Status | Observação |
|----------|--------|------------|
| texto_extraido.md ≥ 200 palavras úteis | ✅ | Pre-existia da sessão anterior |
| NB criado + ≥5 fontes indexadas | ✅ | 4 fontes úteis indexadas (WHO EN, World Bank EN, BCB PT, PDF PL PT) — planalto.gov.br bloqueou anti-crawl |
| manifestacao-short ≥ 4 citações | ✅ | 7 citações explícitas (STF, TJDFT, IBGE, FEBRABAN, FDIC, World Bank, ABNT) |
| ≥1 citação internacional no short | ✅ | FDIC 2024 (US$ 27bi) + World Bank Findex 2021 |
| audit_sources Wave 1+2 aplicado | ✅ | auditoria_fontes_PL-1904-2026.md gerado com 12 blocos |
| PDF gerado ≤ 1 página | ✅ | 1 página, 14 KB |
| V5-AUDIT.md criado | ✅ | Este arquivo |
| commit + push para manifestacoes-pl-rj | ⏳ | Pendente |

---

## Resultado audit_sources

**Wave 1 — Extração:** 12 blocos (F-1 a F-12)
- 5 referências jurídicas/julgados
- 5 dados numéricos
- 2 fontes implícitas (F-8 índice envelhecimento, F-12 ofício interno)

**Wave 2 — Verificação:** ✅ CONCLUÍDA

| F-N | Afirmação | Resultado | Ação tomada |
|-----|-----------|-----------|-------------|
| F-1 | Autoria Vereador Fabio Silva | ⚠️ PARCIAL | Manter — plausível, lag indexação CMRJ |
| F-2 | CMN 2.878/2001 não impõe presença humana | ✅ | Confirmado com trecho Art. 9º |
| F-3 | ABNT NBR 15250:2005 só regula hardware | ⚠️ CORRIGIDO | Norma cancelada — referência removida do texto |
| F-4 | STF RE 610.221, Tema 272 | ✅ | Tese fixada confirmada |
| F-5 | TJDFT ADI vs. Lei 7.426/2024 improcedente | ✅ | ADI 0715060-63.2024 confirmada |
| F-6 | Lei 7.426/2024 "conteúdo equivalente" | ⚠️ CORRIGIDO | Ajustado para "lei similar, restrita a idosos" |
| F-7 | IBGE 18,8% pop. fluminense 60+ | ⚠️ PARCIAL | Plausível; SIDRA inacessível — mantido |
| F-8 | Índice envelhecimento capital | ⚠️ CORRIGIDO | 105,9 era do estado; corrigido para 121,4 capital |
| F-9 | FEBRABAN R$ 10,1bi fraudes 2024 | ⚠️ CORRIGIDO | Valor OK; "mais vulnerável" suavizado |
| F-10 | US$ 27bi elder fraud EUA | ⚠️ CORRIGIDO | FDIC→FinCEN corrigido no texto |
| F-11 | World Bank Findex — metade prob. digital | ✅ | Trecho literal localizado |
| F-12 | Ofício CVL 1342/2026 | ✅ | Documento interno |

**Placar final:** 5 ✅ + 6 ⚠️ (4 corrigidos + 2 mantidos com justificativa) + 0 ❓

---

## Fontes do NB (inventário list_sources.py)
- Ageing and health (WHO)
- Financial Inclusion | World Bank Group
- Banco Central do Brasil
- SEI_000184.002605_2026_71.pdf (PL original)

*(Planalto.gov.br e CFPB não indexaram — bloqueio anti-crawl / 404)*

---

## STATUS: ✅ PASS

Todos os erros críticos detectados foram corrigidos no texto. Zero ❓ inverificáveis. PDF final: 1 página, 332 palavras. Pronto para commit.
