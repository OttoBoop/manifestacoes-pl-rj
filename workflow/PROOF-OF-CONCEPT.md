# PROOF-OF-CONCEPT — Pipeline de Manifestações Técnicas sobre PLs

> **Este documento é o norte do projeto.**
> Releia-o sempre que: o contexto compactar, houver dúvida, retornar de compactação, ou antes de cada passo.

---

## Objetivo

Provar que é possível produzir uma manifestação técnica completa sobre um PL municipal de forma
automatizada, usando `notebooklm` + `agentic_research` + `audit_sources` como base.

**PL de teste:** PL 74/2025 — Circuito Carioca de Economia Solidária (Lei 7.008/2021)
**Ofício:** CVL nº 823/2026 — urgentíssimo, 3 dias
**NB URL:** https://notebooklm.google.com/notebook/192029b0-017e-4bfa-85f0-b6fa25a28b8e

---

## Critério de sucesso

- [x] `manifestacao_PL-74-2025.md` — **1.563 palavras** (>600 ✅), 12 citações formais em `(SOBRENOME, I. "Título", Veículo, Ano)`
- [x] `inventario_fontes_PL-74-2025.md` — **28 fontes** (>10 ✅), 25+ com URL verificável
- [x] `auditoria_fontes_PL-74-2025.md` — 20 citações: 15 ✅ confirmadas, 0 ⚠️ pendentes, 0 ❓
- [x] `PROOF-OF-CONCEPT.md` — log completo P0→P4, erros registrados, workarounds documentados
- [x] Push no repo `manifestacoes-pl-rj` — commit 0a64fd8

---

## Arquitetura

```
PDF do PL
    │
    ▼
[P0] Bash — extração texto + pasta
    │
    ▼
[P1] INVOKE notebooklm
     + workflow/scripts/nb_add_source.py  (adiciona fontes ao NB via URL)
     + ask_question.py (pesquisa profunda)
     + list_sources.py (inventário real)
    │
    ▼
[P2] INVOKE agentic_research
     4 duplas P+E paralelas
     Pesquisadores: NB-first → WebSearch
     Citações: (SOBRENOME, I. "Título", Veículo, Ano)
    │
    ▼
[P3] INVOKE audit_sources
     Verificadores NB-first
     Decisões humanas para ⚠️/❓
    │
    ▼
[P4] git push
```

---

## Regras de autonomia

1. **Nunca parar.** Erro → registrar → workaround → continuar.
2. **Não modificar skills originais.** Código novo vai em `workflow/scripts/`.
3. **Reler este arquivo** sempre que: contexto compactar / dúvida / retorno de compactação.
4. **Registrar tudo** no log abaixo.
5. **Skills base inegociáveis:** `notebooklm` e `agentic_research` devem ser INVOCADAS.

---

## Estado atual

**Próximo passo:** Pipeline completo — v1 e v2 entregues para PL 74/2025

| Passo | Status | Observação |
|-------|--------|------------|
| P0 — Extração PDF | ✅ | `PL-74-2025/texto_extraido.md` existe |
| P1 — notebooklm setup | ✅ | 6 fontes adicionadas, NB respondendo queries |
| P2 — agentic_research | ✅ | 8 agentes, NB-first, citações formais, costura concluída |
| P3 — audit_sources | ✅ | 20 citações auditadas, 8 decisões aplicadas autonomamente |
| P4 — git push | ✅ | commit ec0e154 — todas as correções no repo |
| V2 — reescrita econômica | ✅ | `PL-74-2025-v2/` — 971 palavras, sem incisos, foco em renda/mercado |
| V3 — PDF 1 página | ✅ | `PL-74-2025-v2/manifestacao_PL-74-2025-v3.pdf` — 354 palavras, Times 12, 1.5 |
| Aplicação a 4 novos PLs | ✅ | PL 1883, 1844, 1795, 1934 — 6 artefatos cada (texto + 3 .md + 1 short + 1 PDF) |
| +2 PLs (rodada 2) | ✅ | PL 1884 (Eixo Econômico Municipal — lei-mãe), PL 1954 (Fundo Reparação População Negra) |
| +3 PLs (rodada 3) | ✅ | PL 1840 (gratuidade orçamentos), PL 1866 (gorjeta/música), PL 1900 (ISS Assessoria — fecha trilogia com 1883/1884) |
| V4 (pipeline adversarial) | ✅ | Pró + Contra + Síntese em subpasta `/v4/` para os 9 PLs (74/2025, 1795, 1840, 1844, 1866, 1883, 1884, 1900, 1934, 1954); comparação em `workflow/V4-COMPARACAO.md` |
| V5 — Workflow setup | ✅ | 3 docs criados em `workflow/V5/`: LONG_TERM_GOALS.md, SHORT_TERM_GOALS.md, V5-VS-V3.md. Auditoria V3: NB vazio em 9/11 PLs, PT-only, 0 citações internacionais, audit_sources nunca aplicado |
| V5 — PL-1904 | ✅ PROCESSADO (V5) | short 332w, 5 citações (2 EN), PASS, commit+push |
| V5 — PL-1897 | ✅ PROCESSADO (V5) | short 326w, 5 citações (2 EN), PASS (10✅+2⚠️corrigidos), commit+push |
| V5 — PLC-98 | ✅ PROCESSADO (V5) | short 345w, 4 citações (2 EN), PASS (5✅+3⚠️corrigidos), commit+push |
| V5 — PLC-102 | ✅ PROCESSADO (V5) | short 355w, 5 citações (2 EN), PASS (5✅+0⚠️), commit+push |
| V5 — PLC-103 | ✅ PROCESSADO (V5) | short 364w, 5 citações (2 EN), PASS (4✅+1⚠️corrigido), commit+push |
| V5 — PLC-104 | ✅ PROCESSADO (V5) | short 366w, 4 citações (2 EN), PASS (2✅+2⚠️corrigidos), commit+push |
| V5 — Lote C (pendentes) | ⏳ | PLC-105 (CVL 1322), PLC-106 (CVL 1329), PL-1921 (CVL 1476) |
| V5 — Lote D (pendentes) | ⏳ | PL-1826 (coberturas verdes), IND CMRJ 06549/2025 (desconhecido) |

---

## Arquivos críticos

| Arquivo | Caminho |
|---------|---------|
| Este documento | `workflow/PROOF-OF-CONCEPT.md` |
| Script add fonte | `workflow/scripts/nb_add_source.py` |
| Texto do PL | `PL-74-2025/texto_extraido.md` |
| NB auth | `~/.claude/skills/notebooklm/scripts/` |
| Skill agentic_research | `~/.claude/skills/agentic_research/SKILL.md` |
| Skill notebooklm | `~/.claude/skills/notebooklm/SKILL.md` |
| Skill audit_sources | `~/.claude/skills/audit_sources/SKILL.md` |
| Repo | https://github.com/OttoBoop/manifestacoes-pl-rj |

---

## Log de execução

### 2026-05-26 — V5 inicializado: auditoria V3 + novo workflow

- ✅ Auditoria V3 concluída: NB vazio em 9/10 PLs, PT-only → 0 citações internacionais, parallel agents crasharam (EC-5/W-5) em todos os 9, audit_sources aplicado em 1/10 PLs, carry-through 37%, posição "contrário" em PL-1934 rejeitada por Marcel
- ✅ `workflow/V5/` criada com 3 documentos: `LONG_TERM_GOALS.md`, `SHORT_TERM_GOALS.md`, `V5-VS-V3.md`
- ✅ W-6 documentado: retry ×2 (timeout 8min) antes de coordenador-direto
- ✅ Inventário de PDFs atualizado: 10 PLs marcados como ✅ PROCESSADO (V3); 3 novos SEI_001000 identificados
- ⏳ Lote A em andamento: PL-1904 (primeiro a processar em V5), seguido de PL-1897, PLC-98, PLC-102, PLC-103, PLC-104, PLC-105, PLC-106, PL-1921, PL-1826, ❓ IND CMRJ 06549/2025

---

### 2026-05-07 07:30 — P0: Extração PDF e setup inicial
- ✅ PDF extraído: `SEI_000184.002015_2026_49.pdf`
- ✅ Pasta `PL-74-2025/` criada
- ✅ `texto_extraido.md` gerado com artigos do PL
- ✅ NB registrado na biblioteca notebooklm (ID: pl-74-2025-—-circuito-carioca-de-economia-solidária)
- ✅ Auth NotebookLM renovada (state age: ~12h)
- ✅ Repo GitHub criado: manifestacoes-pl-rj (privado)
- ✅ Workflow .md e plano_execucao_pl.md commitados

### 2026-05-07 07:30 — P1 tentativa: ask_question.py falhou
- ❌ Erro: `cdk-overlay-container` bloqueando click no textarea
- **Causa:** modal de onboarding ou NB vazio (sem fontes) bloqueia a UI
- **Workaround aplicado:** adicionado dismiss de overlay em `ask_question.py` (fix de click → force=True)
- ⚠️ Segundo erro: timeout aguardando resposta — NB provavelmente vazio (sem fontes indexadas)
- **Decisão:** criar `nb_add_source.py` para adicionar fontes via URL antes de queries

### 2026-05-07 — P3 concluído: audit_sources Wave 2 completa
- ✅ 20 citações catalogadas + 6 achados editoriais
- ✅ 3 verificadores paralelos + coordenador direto (SV38)
- 8 decisões pendentes para o usuário (D-01 a D-08)
- Achados críticos:
  - D-01: 20.662 EES incorreto — IPEA/SENAES diz 19.708
  - D-02: R$50bi + 3% PIB inconsistente (3% PIB = R$102bi na fonte)
  - D-03: Nome do programa errado ("Circuito Carioca de Artesanato" → "Circuito Rio Ecosol")
  - D-04: SV38 = horário comercial, não competência geral — substituir por art. 30 CF + RE 586.224
  - D-05: Decreto 48.753 → Decreto 51.958/2023 tem o artigo literal sobre feiras

### 2026-05-07 — P3: audit_sources em execução
- ✅ auditoria_fontes_PL-74-2025.md criado (esqueleto Fase 0)
- ✅ Inventário NB real via list_sources.py: 6 fontes confirmadas no NB
- ✅ Wave 1: extrator rodando (background)
- ✅ Wave 2: 3 verificadores paralelos rodando (background)
  - V-A: lei 15.068 vs 14.867 + faturamento artesanato + SV38
  - V-B: vendas 2016 + Niterói + SILVA 2017
  - V-C: PRANDINO + Decreto 48.753/2021 + IPEA mapeamento
- ✅ Wave 2 concluída — auditoria_fontes.md consolidado com 20 citações + 8 decisões

### 2026-05-07 — ❌ ERRO GRAVE: coordenador parou o loop e pediu decisões ao usuário
- **Violação:** Regra 1 "Nunca parar" — coordenador interrompeu o loop após P3 e apresentou 8 decisões pendentes ao usuário ao invés de tomar decisões conservadoras autonomamente
- **Causa raiz:** confusão entre princípio de auditoria ("decisões são do usuário") e regra de autonomia do POC ("nunca parar")
- **Correção:** ao retornar, D-01 a D-08 foram aplicadas com opção conservadora (consistência com fonte > dado absoluto; remover dado calculado; corrigir nome; citar decreto correto; adicionar co-autora)
- **Regra reforçada:** em proof of concept autônomo, tomar opção mais conservadora, registrar decisão, continuar

### 2026-05-07 — P1 completo: NB populado e respondendo
- ✅ `nb_add_source.py` criado em `workflow/scripts/`
- ✅ `nb_debug_ui.py` criado para diagnosticar seletores (NB em pt-BR!)
- ✅ W-1: seletores corrigidos para português (aria-label="Adicionar fonte", text="Sites")
- ✅ 6 fontes adicionadas via URL ao NB (6/6 sucesso)
- ✅ Query ao NB retornou resposta coerente com fontes citadas [1][2][3]
- ✅ Passo 2: agentic_research disparado e concluído

---

## Workarounds documentados

| ID | Problema | Solução | Status |
|----|---------|---------|--------|
| W-1 | overlay modal bloqueando textarea | force=True + Escape antes de clicar | ✅ aplicado em ask_question.py |
| W-2 | NB vazio, sem fontes | criar nb_add_source.py para adicionar URLs | ✅ concluído — 6/6 fontes adicionadas com sucesso |
| W-3 | Coordenador parou loop p/ pedir decisões ao usuário | Tomar opção conservadora autonomamente, registrar, continuar | ✅ documentado como erro; regra reforçada |
| W-4 | PDFs escaneados — pdftotext retorna só capa (~2000 chars) | Upload do PDF ao NB (Gemini faz OCR interno) via `nb_upload_file.py` | ✅ testado — NB indexou PL 1904/2026 escaneado e retornou conteúdo correto |
| W-5 | Agentes paralelos crasharam em todos os 9 PLs V3 | Coordenador-direto como fallback (EC-5); usado em toda a rodada V3 | ⚠️ V3 workaround documentado — causou pesquisa mais rasa |
| W-6 | Agentes paralelos crash em V5 | Retry ×2 com timeout 8min antes de coordenador-direto; registrar como fallback de último recurso | ✅ protocolo V5 — não foi testado ainda |

---

## Fontes planejadas para o NB

URLs a adicionar via nb_add_source.py:

1. PL 74/2025 — Câmara RJ: https://www.camara.rio/comunicacao/noticias/3022-proposta-fortalece-circuito-carioca-de-economia-solidaria
2. Lei 7.008/2021 base: https://www.camara.rio/comunicacao/noticias/457-agora-e-lei-rio-tera-circuito-de-economia-solidaria
3. Circuito Rio EcoSol: https://ses.prefeitura.rio/circuito-rio-ecosol/
4. SENAES/IPEA Mapeamento: https://repositorio.ipea.gov.br/handle/11058/7410
5. Lei 14.867/2024: https://www.gov.br/trabalho-e-emprego/pt-br/noticias-e-conteudo/2024/Dezembro/presidente-lula-sanciona-lei-paul-singer-de-economia-solidaria
6. Prefeitura Rio recadastro: https://prefeitura.rio/noticias/secretaria-de-trabalho-e-renda-recadastra-produtores-que-integram-o-circuito-carioca-de-economia-solidaria/

---

## Artefatos produzidos

| Arquivo | Status | Caminho |
|---------|--------|---------|
| texto_extraido.md | ✅ | `PL-74-2025/texto_extraido.md` |
| manifestacao_PL-74-2025.md | ✅ | `PL-74-2025/manifestacao_PL-74-2025.md` — >800 palavras, 12 citações formais, 8 correções aplicadas |
| inventario_fontes_PL-74-2025.md | ✅ | `PL-74-2025/inventario_fontes_PL-74-2025.md` — 28 fontes em F-T.N, notas resolvidas |
| auditoria_fontes_PL-74-2025.md | ✅ | `PL-74-2025/auditoria_fontes_PL-74-2025.md` — 20 citações, 0 pendentes, todos achados resolvidos |

---

## Inventário de PDFs na pasta (descoberto no loop pós-POC)

> Verificado via `pdftotext` + `PyMuPDF`. Total: 26 PDFs (2 duplicatas), sendo 1 PL com texto nativo, 2 leis já sancionadas, 16 PLs escaneados aguardando manifestação.

**Limitação identificada:** `pdftotext` e `PyMuPDF` só extraem texto nativo. PDFs escaneados (imagens) precisam de OCR (`tesseract`). Instalação necessária: `sudo apt-get install tesseract-ocr tesseract-ocr-por`

| Arquivo PDF | Ofício CVL | PL/PLC | Status | Texto |
|-------------|-----------|--------|--------|-------|
| SEI_000184.002015_2026_49.pdf | CVL 823/2026 | PL 74/2025 | ✅ PROCESSADO | nativo |
| SEI_000184.002083_2026_16.pdf | CVL 925/2026 | PL 1840/2026 | ✅ PROCESSADO (V3) | escaneado |
| SEI_000184.002122_2026_77.pdf | CVL 992/2026 | PL 1844/2026 | ✅ PROCESSADO (V3) | escaneado |
| SEI_000184.002379_2026_29.pdf | CVL 1133/2026 | PL 1866/2026 | ✅ PROCESSADO (V3) | escaneado |
| SEI_000184.002441_2026_82.pdf | CVL 1214/2026 | PL 1883/2026 | ✅ PROCESSADO (V3) | escaneado |
| SEI_000184.002448_2026_02.pdf | CVL 1218/2026 | PL 1884/2026 | ✅ PROCESSADO (V3) | escaneado |
| SEI_000184.002464_2026_97.pdf | CVL 1227/2026 | PLC 98/2026 | ✅ PROCESSADO (V5.1) | escaneado |
| SEI_000184.002504_2026_09.pdf | CVL 1268/2026 | PLC 102/2026 | ✅ PROCESSADO (V5.1) | escaneado |
| SEI_000184.002513_2026_91.pdf | CVL 1276/2026 | PL 1897/2026 | ✅ PROCESSADO (V5.1) | escaneado |
| SEI_000184.002514_2026_36.pdf | CVL 1279/2026 | PLC 103/2026 | ✅ PROCESSADO (V5.1) | escaneado |
| SEI_000184.002519_2026_69.pdf | CVL 1283/2026 | PLC 104/2026 | ✅ PROCESSADO (V5.1) | escaneado |
| SEI_000184.002529_2026_02.pdf | CVL 1294/2026 | PL 1900/2026 | ✅ PROCESSADO (V3) | escaneado |
| SEI_000184.002573_2026_12.pdf | CVL 1322/2026 | PLC 105/2026 | ✅ PROCESSADO (V5.1) | escaneado |
| SEI_000184.002582_2026_03.pdf | CVL 1329/2026 | PLC 106/2026 | ✅ PROCESSADO (V5.1) | escaneado |
| SEI_000184.002605_2026_71.pdf | CVL 1342/2026 | PL 1904/2026 | ✅ PROCESSADO (V5.1) | escaneado |
| SEI_000184.002830_2026_16.pdf | CVL 1476/2026 | PL 1921/2026 | ✅ PROCESSADO (V5.1) | escaneado |
| SEI_000184.003025_2026_00.pdf | CVL 1568/2026 | PL 1934/2026 | ✅ PROCESSADO (V3) ⚠️ posição contrária — reescrever V5 | escaneado |
| SEI_000184.003246_2026_70.pdf | CVL 1722/2026 | PL 1954/2026 | ✅ PROCESSADO (V3) | escaneado |
| SEI_001000.003088_2026_21.pdf | — | ❓ Ofício IND CMRJ 06549/2025 (Vereador Leonel de Esquerda) | ❓ PL desconhecido — aguarda OCR via NB | escaneado |
| SEI_001000.003809_2026_01.pdf | SMG 1526/2026 | PL 1795/2026 (roteamento) | ✅ PL-1795 PROCESSADO (V3) — este PDF é duplicata de roteamento | escaneado |
| SEI_001000.004374_2026_12.pdf | SMG 1665/2026 | PL 1826/2026 — Coberturas Verdes e Sustentáveis | ⏳ aguarda V5 | escaneado |
| SEI_000184.003132_2026_20.pdf | — | PL 163/2025 | 📋 Lei 9.326/2026 (sancionada) | nativo |
| SEI_000184.003147_2026_98.pdf | — | PL 1320/2025 | 📋 Lei 9.337/2026 (sancionada) | nativo |
