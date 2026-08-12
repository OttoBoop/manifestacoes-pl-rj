# V5 vs V3 — Comparação técnica

> Base: V3 (não V4). V4 adversarial reduziu a média de citações de 1.9 para 0.8 por manifestação.  
> V5 mantém a arquitetura V3 e corrige 6 falhas de execução confirmadas por auditoria.  
> Última atualização: 2026-05-26

---

## Resumo executivo

V3 produzia manifestações estruturalmente corretas, com argumento econômico sólido e fórmula de abertura/fechamento aprovada por Marcel. Mas tinha três problemas críticos de execução:

1. **NB vazio**: apenas 4 notebooks criados para 11 PLs; na prática, pesquisa web-only em português
2. **Zero fontes internacionais**: prompts em PT → buscas em PT → fontes todas brasileiras
3. **Citações inventariadas mas não citadas**: 37% carry-through (fontes catalogadas mas que não chegaram ao texto)

Adicionalmente: `audit_sources` nunca aplicado a V3; agentes paralelos crasharam em todos os 9 PLs; posição "contrário" em PL-1934 foi rejeitada por Marcel.

**V5 não muda estrutura. V5 corrige execução.**

---

## Comparação arquitetural

| Componente | V3 real (o que aconteceu) | V5 (o que deve acontecer) |
|-----------|--------------------------|--------------------------|
| **NB setup (P0)** | 4 NB para 11 PLs; ~1 fonte/NB | 1 NB dedicado por PL; ≥ 6 fontes via nb_add_source.py |
| **Validação NB** | Nunca feita | list_sources.py após upload; abortar se <80% |
| **Lista de fontes** | Inexistente para V3 PLs | `sources_PL-XXXX.txt` criado em P0 (≥ 2 URLs em inglês) |
| **Pesquisa (P2)** | Coordenador-direto (1 agente) por crash | 4 duplas P+E paralelas; coordenador-direto só após 2 retries |
| **Idioma de busca** | Português apenas | Bilíngue obrigatório (PT + EN) |
| **Fontes internacionais** | 0 por manifestação | ≥ 1 obrigatório (bloqueante: relatório rejeitado sem) |
| **Carry-through** | 37% (1–4 de 5–7 fontes chegam ao texto) | ≥ 80% obrigatório; síntese DEVE preservar citações |
| **audit_sources (P3)** | Aplicado a 1/11 PLs (V1 PL-74 apenas) | Obrigatório: Wave 1+2 antes de finalizar |
| **Posição default** | "Nada a opor" ou "contrário" por análise econômica pura | Posição categórica; praxe "nada a opor" com argumentos adversos citados no corpo — o workflow nunca recomenda rejeição |

---

## Comparação de output: V3 vs humano vs V5 target

### PL-1795 (Plataformas digitais de entrega)

**V3 real** (manifestacao_PL-1795-2026-short.md):
```
(CEBRAP, 2025) — 2,2 milhões trabalhadores; 455.621 entregadores; +18%
(AMOBITEC, 2025) — renda bruta cresceu 5% acima da inflação
[2 citações | 0 internacionais]
```

**Human — Marcel final** (Revisoes humanas.txt, 2026-05-19):
```
(CEBRAP, 2025) — mesmos dados, ligeiramente expandidos
(AMOBITEC, 2025) — renda bruta +5%
[2 citações | 0 internacionais — Marcel manteve o mesmo nível de V3]
```

**V5 target:**
```
(CEBRAP, 2025) — 2,2 milhões; 455.621 entregadores; +18%
(AMOBITEC, 2025) — renda bruta +5%
+ ILO (2024) — relatório sobre gig economy e proteção social de trabalhadores de plataforma
+ Lei nº 8.078/1990 (CDC) — base legal para as sanções
[≥ 4 citações | ≥ 1 internacional]
```

---

### PL-1883 (Assessoria de Investimentos — Eixo Econômico)

**V3 real** (manifestacao_PL-1883-2026-short.md):
```
(ANCORD apud GORILA INVESTIMENTOS, 2025) — 28.095 assessores; +515% em 10 anos
Resolução CVM 178/2023
LC 116/2003
[3 citações | 0 internacionais — melhor caso de V3]
```

**Human — Marcel final** (Revisoes humanas.txt, 2026-05-19):
```
(ANCORD apud GORILA INVESTIMENTOS, 2025) — dados de crescimento
[removeu Ressalva operacional inteira; simplificou conclusão]
[~1–2 citações efetivas — Marcel foi mais sintético que V3]
```

**V5 target:**
```
(ANCORD apud GORILA INVESTIMENTOS, 2025) — 28.095 assessores; +515%
Resolução CVM 178/2023 + LC 116/2003 — base legal
+ Zingales (2015) ou equivalente: referência a concentração regional de serviços financeiros
+ dado comparativo: benchmark SP vs RJ vs outros estados com regime favorável
[≥ 5 citações | ≥ 1 internacional]
```

---

### PL-1866 (Gorjeta + música ao vivo)

**V3 real:**
```
(FGV/ABRASEL, 2024) — R$ 455 bilhões; 4,9 milhões; 7,9% emprego formal
(ABRASEL, 2024) — Rio lidera geração de empregos formais entre capitais
Lei Federal nº 13.419/2017 (BRASIL, 2017)
[3 citações | 0 internacionais]
```

**Human — Marcel final:**
```
(FGV/ABRASEL, 2024) — mesmos dados
(ABRASEL, 2024) — liderança Rio
[manteve estrutura; removeu referência à lei federal na conclusão]
```

**V5 target:**
```
(FGV/ABRASEL, 2024) — R$ 455 bilhões; 4,9 milhões; 7,9%
(ABRASEL, 2024) — liderança Rio
Lei Federal nº 13.419/2017
+ NYT Hospitality Research (2023) ou WTTC (2024): padrão internacional de service charge transparency
[≥ 4 citações | ≥ 1 internacional]
```

---

### PL-1934 (Desconto hospedagem — caso especial)

**V3 real (posição rejeitada):**
```
Posição: CONTRÁRIO
(FOHB/HotelInvest, 2024) — diária média +10,6%; RevPar +11,9%
(MTur, 2024) — R$ 8,4 bilhões em investimentos até 2028
[4 citações, análise correta — mas posição "contrário" rejeitada por Marcel]
```

**Instrução de Marcel** (WhatsApp, 2026-05-19):
```
"refazer esse, por favor. Está como contrário. Colocar nada a opor,
e citar os argumentos contrários…"
```

**V5 target (a ser reescrito):**
```
Posição: NADA A OPOR
Corpo: contexto do setor + dados FOHB/MTur
Ressalva técnica (4 pontos): 
  (i) excludente tempo técnico operacional entre hóspedes
  (ii) gradualidade do desconto
  (iii) limite a diárias unitárias
  (iv) exclusão de check-in atrasado por culpa do hóspede
+ referência internacional: padrão check-in/check-out consolidado (STR, 2024 ou HotelInvest)
```

---

## Onde V3 acertou (preservar em V5 sem alteração)

1. **Estrutura das seções**: "O que o PL muda" → "Impacto econômico" → "Conclusão" — Marcel remove "Ressalva operacional" em todas as suas revisões (2026-05-19)
2. **Fórmula de abertura**: "Em atenção ao Ofício CVL nº X/YYYY, referente ao PL nº X/YYYY, de autoria do Vereador Y, que [descrição], esta Subsecretaria posiciona-se em sentido de nada a opor" — padrão da casa, não mudar
3. **Fórmula de fechamento**: "Esta Subsecretaria posiciona-se em sentido de nada a opor ao PL nº X/YYYY" — igual
4. **Formato de citação brasileira**: `(INSTITUIÇÃO apud FONTE, ANO)` e `(SOBRENOME, I. "Título", Veículo, Ano)` — correto, manter
5. **Argumento econômico central**: estava correto em todos os 9 PLs; Marcel não contestou nenhuma análise, apenas pediu reposicionamento de PL-1934

---

## Onde V3 falhou (corrigir em V5)

| Falha | Causa raiz | Correção V5 |
|-------|-----------|-------------|
| Zero fontes internacionais | Prompts em PT; NB em PT | Prompts bilíngues PT+EN; fontes EN obrigatórias em sources_PL-XXXX.txt |
| NB vazio (1 fonte/PL) | nb_add_source.py nunca chamado para V3 PLs | P0 obrigatório: criar NB + adicionar 6 fontes + validar list_sources.py |
| Agentes paralelos crasharam | Timeout curto + sem retry | Timeout 8 min; retry ×2; fallback coordenador-direto documentado como W-6 |
| audit_sources ignorado | Não estava no loop de execução | audit_sources Wave 1+2 é gate: manifestação não é "concluída" sem ele |
| Citações inventariadas mas não no texto (37%) | Síntese não forçava carry-through | Instrução na síntese: "preserve ≥ 80% das citações dos relatórios dos pesquisadores" |
| PL-1934 posição "contrário" | Análise econômica pura sem calibragem institucional | "Nada a opor" com argumentos contrários citados no corpo (o workflow não recomenda rejeição) |

---

## Novo protocolo P0 obrigatório (V5)

Para cada novo PL, **ANTES** de invocar agentic_research:

```bash
BASE_DIR="/home/otavio/Documents/vscode/resumir projetos de lei"
PL_ID="PL-XXXX-YYYY"

# 1. Criar NB dedicado
python3 "$BASE_DIR/workflow/scripts/nb_create_notebook.py" \
  --title "$PL_ID — [ementa curta em 5-7 palavras]" \
  --out /tmp/nb_url_${PL_ID}.txt

NB_URL=$(cat /tmp/nb_url_${PL_ID}.txt)

# 2. Upload do PDF/texto do PL
python3 "$BASE_DIR/workflow/scripts/nb_upload_file.py" \
  --notebook-url "$NB_URL" \
  --file "$BASE_DIR/$PL_ID/texto_extraido.pdf"

# 3. Criar e adicionar fontes curadas
# Escrever $BASE_DIR/$PL_ID/sources_PL-XXXX.txt com 6+ URLs
# (≥ 2 em inglês, ≥ 2 brasileiras, ≥ 1 legal)
while IFS= read -r url; do
  echo "Adicionando: $url"
  python3 "$BASE_DIR/workflow/scripts/nb_add_source.py" \
    --notebook-url "$NB_URL" --url "$url"
done < "$BASE_DIR/$PL_ID/sources_${PL_ID}.txt"

# 4. Validar cobertura
cd ~/.claude/skills/notebooklm
python scripts/run.py list_sources.py \
  --notebook-url "$NB_URL" \
  --out /tmp/nb_inventory_${PL_ID}.json

# Checar manualmente: ≥ 80% das URLs do sources_PL-XXXX.txt aparecem no JSON?
# Se não: investigar e re-tentar antes de prosseguir
```

---

## Delta do prompt do pesquisador V5 (adições sobre V3)

As instruções abaixo devem ser **adicionadas ao prompt de cada Pesquisador P{N}** quando invocando agentic_research:

```
### Protocolo V5 (OBRIGATÓRIO — não negociável)

**NB-first**: comece toda busca pelo NotebookLM do caso.
URL: {NB_URL}

**Busca bilíngue**: execute queries em português E em inglês para cada tópico.
  Exemplo para gig economy:
  - PT: "plataformas digitais trabalho entregadores regulamentação Brasil 2024"
  - EN: "gig economy platform work regulation Brazil delivery apps 2024"

**Fonte internacional obrigatória**: inclua ≥ 1 citação de fonte internacional
  (artigo acadêmico, relatório OCDE/ILO/BID/Banco Mundial/etc.) no seu relatório.
  Sem isso, seu relatório é REJEITADO.
  Exemplos aceitos: ILO (2024), OECD (2023), World Bank (2022), artigo em periódico 
  indexado (Web of Science, Scopus), estudo comparativo com outro país.

**Carry-through obrigatório**: toda fonte listada no F-T.N DEVE aparecer citada no
  seu relatório. Não liste fontes que você não utilizou no texto.

**Ótica exclusivamente econômica (V5.2 — não negociável)**: seu relatório NÃO PODE
  sustentar nada em argumento jurídico — proibido STF/STJ/TJ, ADI, ADPF, súmula,
  jurisprudência, (in)constitucionalidade, vício de iniciativa, competência
  (municipal/legislativa/constitucional). Citar a norma que o PL altera/converte é
  permitido como OBJETO da análise. Se encontrar óbice ou respaldo jurídico relevante,
  liste-o num campo separado ao final do relatório:
  "ACHADOS JURÍDICOS (não vão ao corpo — roteados à PGM)".
  Relatório cujo argumento central for jurídico é REJEITADO.
```

---

## Comparação V5 vs V4 (argumento para não usar V4 como base)

| Dimensão | V4 adversarial | V5 |
|----------|---------------|-----|
| Arquitetura | PRÓ enviesado + CONTRA enviesado + Síntese | V3 com execução corrigida |
| Citações médias | 0.8 por manifestação (-58% vs V3) | Meta ≥ 4 por short |
| Custo relativo | ~2× (3 fluxos paralelos) | ~1× (V3 baseline) |
| Mudança de posição | 0/9 (nenhuma) | N/A |
| Ressalvas | +2 por PL em média | Removidas — Marcel não usa seção de ressalvas |
| Problema central | Síntese abstrata consome citações | Resolvido por carry-through + audit |

**Conclusão**: V4 não resolveu o problema de citação — piorou. V5 vai para a raiz.

---

## Template V5-AUDIT.md (criar para cada PL)

Salvar em `PL-XXXX-YYYY/V5-AUDIT.md` após cada execução:

```markdown
# V5 Audit — PL XXXX/YYYY — [ementa curta]

**Data de execução:** YYYY-MM-DD

## P0 — NB Setup
- NB criado: ✅/❌
- NB URL: https://notebooklm.google.com/notebook/[ID]
- Fontes planejadas: N
- Fontes adicionadas via nb_add_source.py: M/N
- list_sources.py validou: M/N fontes (≥80%: ✅/❌)
- Idiomas das fontes: N em PT | N em EN

## P2 — Pesquisa (agentic_research)
- Agentes paralelos rodaram: ✅/❌
  - Se ❌: fallback coordenador-direto (W-6 aplicado: ✅/❌)
- Relatórios P+E entregues: N/4
- Fontes internacionais nos relatórios: N
- Fontes totais no inventário: N

## Síntese
- Manifestação full: NNN palavras
- Manifestação short: NNN palavras
- Citações no short: N (meta ≥ 4: ✅/❌)
- Fontes internacionais citadas: N (meta ≥ 1: ✅/❌)
- Carry-through: N/M = X% (meta ≥ 80%: ✅/❌)
- Posição adotada: favorável / nada a opor / contrário
- Posição alinhada com SMDE: ✅/❌
- Corpo 100% econômico (checar_economia_only.py): ✅/❌ **BLOQUEANTE — V5.2**

## P3 — audit_sources
- Wave 1 (extração): ✅/❌
- Wave 2 (verificação): ✅/❌
- Correções aplicadas: N
- Status final: PASS / FAIL

## P3.5 — Gate adversarial (obrigatório se posição ≠ nada a opor — V5.2)
- Cético 1 (fonte): refutado=True/False
- Cético 2 (lógica): refutado=True/False
- Cético 3 (jurisdição — "a posição sobrevive deletando todo argumento jurídico?"): sobrevive=True/False

## Achados jurídicos — roteados à PGM (V5.2; se houver)
- [óbices/respaldos jurídicos encontrados na pesquisa; NÃO vão ao corpo]

## Status geral V5: ✅ PASS / ❌ FAIL — [observações]
```
