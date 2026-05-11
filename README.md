# Manifestações Técnicas — PLs Câmara Municipal RJ

Pipeline automatizado de análise de Projetos de Lei (PLs) para a Secretaria Municipal de Desenvolvimento Econômico (SMDE) do Rio de Janeiro. Dado o PDF de um PL recebido por Ofício da CVL (Casa Civil), o sistema produz manifestação técnica fundamentada com citações verificáveis, no padrão usado pela Subsecretaria.

**Tecnologia:** [Claude Code](https://claude.com/claude-code) com três skills encadeadas (`notebooklm`, `agentic_research`, `audit_sources`).

---

## O que está aqui

10 PLs processados pela pipeline em diferentes versões metodológicas:

| Pasta | PL | Tema | Versões disponíveis |
|-------|----|----|--------------------|
| [PL-74-2025/](PL-74-2025/) | PL 74/2025 | Circuito Carioca de Economia Solidária | V1 + V4 |
| [PL-74-2025-v2/](PL-74-2025-v2/) | PL 74/2025 (relido) | mesma proposta — versão econômica e PDF 1 página | V2 + V3 |
| [PL-1795-2026/](PL-1795-2026/) | PL 1795/2026 | Plataformas digitais de entrega (gig economy) | V3 + V4 |
| [PL-1840-2026/](PL-1840-2026/) | PL 1840/2026 | Gratuidade de orçamentos e visitas técnicas | V3 + V4 |
| [PL-1844-2026/](PL-1844-2026/) | PL 1844/2026 | Sinalização dos Polos Gastronômicos | V3 + V4 |
| [PL-1866-2026/](PL-1866-2026/) | PL 1866/2026 | Taxa de serviço (gorjeta) + música ao vivo | V3 + V4 |
| [PL-1883-2026/](PL-1883-2026/) | PL 1883/2026 | Eixo Econômico de Assessoria de Investimentos | V3 + V4 |
| [PL-1884-2026/](PL-1884-2026/) | PL 1884/2026 | Lei-quadro Eixo Econômico Municipal | V3 + V4 |
| [PL-1900-2026/](PL-1900-2026/) | PL 1900/2026 | ISS Assessoria — alteração do CTM | V3 + V4 |
| [PL-1904-2026/](PL-1904-2026/) | PL 1904/2026 | Atendimento bancário PcD/idosos | extração apenas |
| [PL-1934-2026/](PL-1934-2026/) | PL 1934/2026 | Desconto em diárias de hospedagem | V3 + V4 (único **contrário**) |
| [PL-1954-2026/](PL-1954-2026/) | PL 1954/2026 | Fundo Reparação População Negra | V3 + V4 |

Documentos-âncora:
- [workflow/PROOF-OF-CONCEPT.md](workflow/PROOF-OF-CONCEPT.md) — log completo de execução, workarounds, estado de cada PL
- [workflow/V4-COMPARACAO.md](workflow/V4-COMPARACAO.md) — tabela comparativa V3 vs V4 caso a caso
- [workflow_manifestacao_pl.md](workflow_manifestacao_pl.md) — documentação V1 histórica (preservada como referência)

---

## As 4 versões do método

A pipeline evoluiu em 4 versões. Cada uma adiciona um vetor metodológico ao anterior. Tabela comparativa:

| Aspecto | V1 (jurídica) | V2 (econômica) | V3 (compacta) | V4 (adversarial) |
|---------|--------------|----------------|---------------|------------------|
| **Foco analítico** | Jurídico — exegese de incisos, competência constitucional, jurisprudência | Econômico — renda, mercado, emprego, dados | Idem V2, mais conciso | Idem V2/V3 + contraposição estruturada |
| **Pipeline de produção** | 1 fluxo agentic_research (4 duplas P+E) | 1 fluxo agentic_research com prompts econômicos | Mesmo + recorte para 1 página | 3 fluxos: pró-enviesado + contra-enviesado + síntese |
| **Tamanho da manifestação** | ~1.500 palavras | ~700-900 palavras | ~350 palavras + PDF | 700-900 palavras (síntese) |
| **Entregável final** | .md longo | .md longo | .md curto + **PDF 1 página** (Times 12, 1.5) | Idem V3 + arquivos pró/contra/log de síntese |
| **Posiciona auditoria** | Wave 1+2 com decisões para usuário | Idem | Auditoria consolidada autônoma | Auditoria consolidada autônoma |
| **Estrutura de arquivos** | `PL-XXXX/` raiz | `PL-XXXX-v2/` separado | Subpasta dentro de v2 | Subpasta `PL-XXXX/v4/` |
| **Quando usar** | Quando demanda é jurídica formal | Quando SMDE precisa dar opinião econômica (regra) | Quando produto final é peça de gabinete | Quando há trade-offs reais (impacto fiscal, externalidades, sobreposição regulatória) |
| **Aumenta tempo de processamento** | Baseline | ≈ baseline | +1 etapa de recorte | ≈ 2× tempo (2 fluxos + síntese) |

### O que cada versão introduziu

**V1 — Jurídica (mai/2026, primeira versão).** Pipeline original com `notebooklm` + `agentic_research` + `audit_sources`. Foco jurídico-administrativo: enumeração de incisos do PL, análise de competência constitucional, citação de jurisprudência STF/STJ. Saída: manifestação longa (~1.500 palavras) em estilo de parecer. Aplicada em PL 74/2025. **Feedback recebido:** muito longa, muito enrolada com referências a "§ 3º do art. 1º", e foco errado — SMDE dá opinião **econômica**, não jurídica (a parte jurídica é da PGM).

**V2 — Reescrita econômica (mai/2026).** Mesma pipeline mas com **prompts dos agentes reorientados**: proibido enumerar incisos (i)-(vii); proibido citar artigos constitucionais (exceto frase genérica); foco em renda, mercado, emprego, dados quantitativos; tom de gestão econômica pública. Saída: ~700-900 palavras. Aplicada em PL 74/2025 v2.

**V3 — Versão compacta (mai/2026).** Mantém V2 e adiciona **última etapa**: recortar a manifestação longa em uma versão de ~350 palavras (`*-short.md`) e gerar **PDF de 1 página** em Times New Roman 12pt, espaçamento 1.5, A4, margens 2.5cm. Saída final é o PDF, peça pronta para gabinete. Aplicada em PL 74/2025 v3 e nos 9 PLs subsequentes. Foi o método mais usado neste repo (V3 = padrão para 9 dos 10 PLs processados).

**V4 — Pipeline adversarial (mai/2026).** Antes da síntese final, rodar **dois fluxos completos em paralelo** — um agente forçado a buscar **apenas argumentos PRÓ** o PL, outro forçado a buscar **apenas argumentos CONTRA** (sem mentir, mas com viés deliberado). Depois, um terceiro agente Síntese compara os dois e produz a manifestação final equilibrada. Aplicada nos 9 PLs já processados pela V3. **Resultado empírico:** nenhuma das 9 manifestações mudou de posição entre V3 e V4, mas **todas as 9 ganharam ressalvas operacionais novas ou refinadas** oriundas do argumento contra-enviesado. Detalhes em [workflow/V4-COMPARACAO.md](workflow/V4-COMPARACAO.md).

---

## Como replicar para um novo PL

### Pré-requisitos

1. **Claude Code instalado** com as três skills em `~/.claude/skills/`:
   - `notebooklm/` — query de NB via Playwright (autenticação manual única no Google)
   - `agentic_research/` — orquestração de duplas pesquisador + escritor
   - `audit_sources/` — verificação de citações
2. **Python 3.10+** com `weasyprint`, `pymupdf`, e dependências da skill notebooklm (`patchright`).
3. **Conta Google ativa** no NotebookLM (autenticada na primeira execução da skill).
4. **Chromium** disponível em `/usr/bin/chromium` (caminho hardcoded nos scripts).

### Setup do PL (P0)

```bash
# Criar pasta do PL na raiz do repo
mkdir -p "resumir projetos de lei/PL-XXXX-YYYY/v4"
cd "resumir projetos de lei"
```

### P1 — NotebookLM dedicado por PL

Cada PL tem um NB próprio para evitar contaminação de contexto entre análises.

```bash
# Criar NB novo
python3 workflow/scripts/nb_create_notebook.py \
  --title "PL-XXXX-YYYY — <ementa curta>" \
  --out /tmp/nb_XXXX_url.txt

# Subir o PDF do PL ao NB (OCR interno do Gemini extrai o texto)
URL=$(cat /tmp/nb_XXXX_url.txt | sed 's/?addSource=true//')
python3 workflow/scripts/nb_upload_file.py \
  --notebook-url "$URL" \
  --file "PL-original.pdf"

# Extrair o texto integral via query
source ~/.claude/skills/notebooklm/.venv/bin/activate
cd ~/.claude/skills/notebooklm
python scripts/run.py ask_question.py \
  --question "Qual é o autor, ementa e texto integral de todos os artigos do PL XXXX/YYYY?" \
  --notebook-url "$URL"
# Salvar resposta em: PL-XXXX-YYYY/texto_extraido.md
```

### P2 — agentic_research

Invocar a skill com 4 tópicos econômicos (V2/V3) ou pró + contra em paralelo (V4):

**V3 (1 fluxo econômico):**
```
/agentic_research

Produzir manifestação técnica V3 sobre PL XXXX/YYYY para SMDE.
- Tópicos: T1 exegese econômica | T2 impacto mensurado | T3 contexto do setor | T4 ressalvas operacionais
- Regra: sem enumeração de incisos; sem competência constitucional; foco econômico
- NB: https://notebooklm.google.com/notebook/...
- Citações obrigatórias: (SOBRENOME, I. "Título", Veículo, Ano)
- Output: PL-XXXX-YYYY/manifestacao_PL-XXXX-YYYY.md (700-900 palavras)
```

**V4 (3 fluxos adversariais):** mesma estrutura, mas duas invocações enviesadas + síntese. Prompts esqueleto em [workflow/PROOF-OF-CONCEPT.md](workflow/PROOF-OF-CONCEPT.md).

### P3 — audit_sources (opcional)

```
/audit_sources

Auditar fontes da manifestação PL-XXXX-YYYY/manifestacao_PL-XXXX-YYYY.md
- NB: https://notebooklm.google.com/notebook/...
- Aplicar correções autonomamente com critério conservador (sem pedir decisões ao usuário)
```

### P4 — Versão curta + PDF 1 página

```bash
# Manualmente: criar manifestacao_PL-XXXX-YYYY-short.md
# com recorte para ~330 palavras (target: PDF 1 página)

# Gerar PDF (Times New Roman 12pt, espaçamento 1.5, A4)
python3 workflow/scripts/gerar_pdf_manifestacao.py \
  --input PL-XXXX-YYYY/manifestacao_PL-XXXX-YYYY-short.md

# Verifica número de páginas via PyMuPDF; alerta se ultrapassar 1 página.
```

### P5 — Commit + push

```bash
# Adicionar exceção do PDF no .gitignore (todos os .pdf são ignorados por padrão)
echo "!PL-XXXX-YYYY/manifestacao_PL-XXXX-YYYY-short.pdf" >> .gitignore

git add PL-XXXX-YYYY/ .gitignore
git commit -m "PL XXXX/YYYY processado"
git push origin main
```

---

## Estrutura completa do repositório

```
resumir projetos de lei/
├── README.md                              ← este arquivo
├── workflow_manifestacao_pl.md            ← documentação V1 histórica
├── .gitignore                              ← bloqueia *.pdf; exceções por PL
├── workflow/
│   ├── PROOF-OF-CONCEPT.md                ← log de execução, workarounds, estado de cada PL
│   ├── V4-COMPARACAO.md                   ← tabela comparativa V3 vs V4
│   └── scripts/
│       ├── nb_create_notebook.py          ← cria NB autônoma via Playwright
│       ├── nb_upload_file.py              ← upload de PDF ao NB (Gemini faz OCR)
│       ├── nb_add_source.py               ← adiciona URL como fonte ao NB
│       ├── nb_debug_ui.py                 ← diagnóstico de seletores do NB
│       ├── gerar_pdf_manifestacao.py      ← .md → PDF 1 página (Times 12, 1.5)
│       ├── extract_pl_camara.py           ← scraper opcional do camara.rio
│       └── sources_pl74_2025.txt          ← URLs adicionadas ao NB do PL 74/2025
├── SEI_*.pdf                              ← PDFs originais dos PLs recebidos (todos ignorados pelo git)
└── PL-XXXX-YYYY/                          ← uma pasta por PL
    ├── texto_extraido.md                  ← texto do PL via OCR do NB
    ├── manifestacao_PL-XXXX-YYYY.md       ← manifestação longa (V3)
    ├── inventario_fontes_PL-XXXX-YYYY.md  ← fontes em formato F-T.N
    ├── auditoria_fontes_PL-XXXX-YYYY.md   ← auditoria das citações
    ├── manifestacao_PL-XXXX-YYYY-short.md ← versão curta ~330 palavras
    ├── manifestacao_PL-XXXX-YYYY-short.pdf ← PDF 1 página (somente este sai do .gitignore)
    └── v4/                                ← subpasta V4 (pipeline adversarial)
        ├── manifestacao_pro.md            ← análise enviesada PRÓ (~500-700 palavras)
        ├── inventario_pro.md
        ├── manifestacao_contra.md         ← análise enviesada CONTRA (~500-700 palavras)
        ├── inventario_contra.md
        ├── manifestacao_v4.md             ← síntese final (700-900 palavras)
        ├── manifestacao_v4-short.md       ← versão curta ~310 palavras
        ├── manifestacao_v4-short.pdf      ← PDF 1 página da V4
        ├── inventario_fontes_v4.md        ← fontes consolidadas
        ├── auditoria_v4.md                ← auditoria pós-síntese
        └── log_sintese.md                 ← decisões do agente síntese (o que keep/discard de cada lado e por quê)
```

---

## Scripts em `workflow/scripts/` — referência

| Script | Função | Uso típico |
|--------|--------|-----------|
| `nb_create_notebook.py` | Cria novo NotebookLM via Playwright, retorna UUID URL | `--title "..." --out /tmp/nb_url.txt` |
| `nb_upload_file.py` | Upload de PDF ao NB (Gemini OCR-iza scanned) | `--notebook-url URL --file XX.pdf` |
| `nb_add_source.py` | Adiciona URL como fonte ao NB | `--notebook-url URL --url https://...` ou `--sources urls.txt` |
| `nb_debug_ui.py` | Diagnóstico interativo dos seletores do NB | usado quando UI do NB muda e seletores quebram |
| `gerar_pdf_manifestacao.py` | Converte .md em PDF 1 página (Times 12pt, 1.5, A4, margens 2.5cm) | `--input X.md [--output X.pdf]` |
| `extract_pl_camara.py` | Tentativa de scraping do camara.rio (não confiável para PLs recentes — usar OCR NB) | `--pl 1840/2026` |

Todos auto-detectam a venv da skill `notebooklm` em `~/.claude/skills/notebooklm/.venv/` — não precisa `source ... activate` manual.

---

## Workarounds documentados

| ID | Problema | Solução | Status |
|----|----------|---------|--------|
| **W-1** | Overlay `cdk-overlay-container` bloqueia textarea de query no NB | `Escape` + `click(force=True)` + `keyboard.type()` no fallback | aplicado em `~/.claude/skills/notebooklm/scripts/ask_question.py` |
| **W-2** | NB original não tinha script para adicionar fontes | `workflow/scripts/nb_add_source.py` criado | concluído |
| **W-3** | Coordenador parou loop pedindo decisões ao usuário (violação da regra "nunca parar") | Tomar opção conservadora autonomamente, registrar, continuar | regra reforçada no PROOF-OF-CONCEPT |
| **W-4** | PDFs escaneados (`pdftotext` retorna só capa, ~2000 chars) | Upload do PDF ao NB; Gemini faz OCR interno e retorna o texto via query | `nb_upload_file.py` |
| **W-5** | Criação de NB às vezes não resolve UUID (fica em `/notebook/creating`) — rate limit do Google | Retry com delay + fallback: reaproveitar NBs vazios criados em sessões anteriores (UUIDs descobertos varrendo a home do NB via Playwright) | aplicado em V3+V4 |
| **EC-5** (V4) | Crash de agentes paralelos em `agentic_research` (ocorreu 3× na sessão) | Workaround coordenador-direto: coordenador escreve a pipeline enviesada diretamente, usando o **mesmo prompt enviesado**. Viés está no prompt, não no executor. | aplicado em V4 |

---

## Formato de citação (regra dura)

Toda manifestação deve usar o formato:

```
(SOBRENOME, I.; SOBRENOME2, I. "Título completo", Veículo/Editora, Ano)
```

Exemplos válidos:
- `(SECRETARIA ESPECIAL DE ECONOMIA SOLIDÁRIA. "Circuito Rio EcoSol", Prefeitura do Rio de Janeiro, 2024)`
- `(SENAES; IPEA. "Os Novos Dados do Mapeamento de Economia Solidária no Brasil", IPEA, 2016)`
- `(SILVA, A. L. F. "A metodologia de construção das feiras de economia solidária", Mundo do Trabalho Contemporâneo, UFBA/UnB, 2017)`

Inventário de fontes (`inventario_fontes_*.md`) usa o esquema **F-T.N** (Fonte, Tópico, Número):

| ID | Autor/Órgão | Ano | Título | URL | Trecho relevante |
|----|-------------|-----|--------|-----|-----------------|

Esse formato é consumido pela skill `audit_sources` na auditoria.

---

## Resultados da V4 — achado principal

Aplicada aos 9 PLs já processados pela V3, a V4 produziu:

- **0 de 9 mudanças de posição** entre V3 e V4 (todas confirmaram V3, inclusive o único CONTRÁRIO — PL 1934)
- **9 de 9 PLs ganharam ressalvas operacionais novas ou refinadas** oriundas do argumento contra-enviesado
- Exemplos de ganhos substantivos: monitoramento anti-redlining (PL 1795), gradação proporcional de multa por porte (PL 1840), revisão automática de Eixos a cada 3 anos (PL 1884), contrapartida operacional + cláusula de revisão (PL 1883)

**Conclusão prática:** o pipeline adversarial **não muda conclusões já robustas, mas enriquece fundamentação** — em particular detectando lacunas operacionais via contraposição PRÓ × CONTRA que o pipeline equilibrado V3 tende a deixar implícitas.

Recomendação de uso: **V3 como padrão**; **V4 quando há trade-offs ricos** (impacto fiscal, externalidades, sobreposição regulatória).

---

## Limitações conhecidas

1. **Rate limit do NotebookLM** — plano free tem limite diário de 50 queries. Pipeline V4 consome ~10 queries por PL (entre pró, contra, síntese). Pausar e retomar no dia seguinte se atingir teto.
2. **Crash de agentes paralelos** — agentes em background falharam 3× na sessão de execução. Workaround coordenador-direto (W-EC5) aplicado em todos os V4. Reduz paralelismo mas é confiável.
3. **Criação de NB instável** — ver W-5. Reaproveitar UUIDs descobertos via varredura quando o retry falha.
4. **`pdftotext` falha em PDFs escaneados** — usar W-4 (upload ao NB para OCR).
5. **PDF final às vezes vira 2 páginas mesmo com ≤350 palavras** — densidade de bold/seções/headers consome espaço vertical. Trim para ~310-320 palavras quando isso acontece.
6. **`extract_pl_camara.py`** — scraping do camara.rio não funciona para PLs muito recentes (não indexados na busca do site). Manter NB upload como path principal.

---

## Cross-references

- [workflow/PROOF-OF-CONCEPT.md](workflow/PROOF-OF-CONCEPT.md) — log completo de execução com timestamps, workarounds e estado de cada PL
- [workflow/V4-COMPARACAO.md](workflow/V4-COMPARACAO.md) — tabela comparativa V3 vs V4 caso a caso + análise meta
- [workflow_manifestacao_pl.md](workflow_manifestacao_pl.md) — documentação V1 histórica (preservada como referência da abordagem original)
- Repo GitHub: https://github.com/OttoBoop/manifestacoes-pl-rj
