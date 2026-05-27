# Metas de Curto Prazo — V5

> Checklist executável. Marcar ✅ conforme completo.  
> Última atualização: 2026-05-26

---

## Bloco 0 — Setup imediato (esta semana)

- [x] Criar pasta `workflow/V5/`
- [x] Criar `LONG_TERM_GOALS.md`
- [x] Criar `SHORT_TERM_GOALS.md`
- [x] Criar `V5-VS-V3.md` (comparação técnica completa)
- [ ] Atualizar `PROOF-OF-CONCEPT.md` — adicionar seção V5 ao log de execução e workaround W-6 (retry de agentes)

---

## Bloco 1 — Para cada novo PL recebido (P0 obrigatório)

Executar ANTES de qualquer chamada ao agentic_research:

```
- [ ] 1. Criar NB dedicado via nb_create_notebook.py
         python3 workflow/scripts/nb_create_notebook.py \
           --title "PL-XXXX-YYYY — [ementa curta]" \
           --out /tmp/nb_url_PL-XXXX.txt

- [ ] 2. Criar PL-XXXX-YYYY/sources_PL-XXXX.txt com ≥ 6 URLs
         — Mínimo 2 em inglês (OCDE, ILO, Banco Mundial, artigo acadêmico, etc.)
         — Mínimo 2 brasileiras institucionais (FGV, CEBRAP, IBGE, órgão regulador)
         — Mínimo 1 legal/regulatório (Planalto, CVM, BC, Câmara Federal)

- [ ] 3. Adicionar todas as fontes ao NB
         while read url; do
           python3 workflow/scripts/nb_add_source.py \
             --notebook-url "$(cat /tmp/nb_url_PL-XXXX.txt)" --url "$url"
         done < PL-XXXX-YYYY/sources_PL-XXXX.txt

- [ ] 4. Validar com list_sources.py
         cd ~/.claude/skills/notebooklm
         python scripts/run.py list_sources.py \
           --notebook-url "$(cat /tmp/nb_url_PL-XXXX.txt)" \
           --out /tmp/nb_inventory_PL-XXXX.json
         # Checar: ≥ 80% das fontes do .txt aparecem no JSON

- [ ] 5. Só então invocar agentic_research com NB_URL injetado nos prompts
```

---

## Bloco 2 — Prompts de pesquisa bilíngues

- [ ] Para cada tópico, o pesquisador deve rodar queries em **PT e EN**:
  - Exemplo T2 (impacto econômico): 
    - PT: "plataformas digitais entrega trabalho Brasil regulamentação 2024"  
    - EN: "platform work gig economy delivery apps regulation Brazil 2024"
  - Fonte internacional achada na web → adicionar ao NB antes de citar
- [ ] Adicionar ao prompt de cada pesquisador a instrução:
  ```
  Você DEVE incluir ≥ 1 citação de fonte internacional no seu relatório.
  Sem isso, o relatório é rejeitado e você será reiniciado.
  Aceito: artigo acadêmico, relatório OCDE/ILO/BID/Banco Mundial, estudo comparativo.
  ```

---

## Bloco 3 — Parallel agent retry (próxima execução agentic_research)

- [ ] Diagnóstico: ao lançar 4 duplas P+E, monitorar com Monitor e registrar qual agente crashou e por quê
- [ ] Se crash: retry automático × 2 com timeout de 8 minutos (antes estava 3 min)
- [ ] Se 2 retries falharem: fallback coordenador-direto (documentar como W-6)
- [ ] Documentar no PROOF-OF-CONCEPT.md:
  ```
  W-6: Parallel agent crash → retry ×2 com timeout 8min → coordenador-direto como last resort
  ```

---

## Bloco 4 — audit_sources retroativo (3 PLs prioritários)

Aplicar audit_sources Wave 1+2 retroativamente aos PLs V3 mais importantes:

- [ ] PL-1883/2026 (Assessoria de Investimentos — mais citações, mais impacto)
- [ ] PL-1866/2026 (Gorjeta + música ao vivo — FGV/ABRASEL, Lei Federal 13.419)
- [ ] PL-1795/2026 (Plataformas digitais — CEBRAP, AMOBITEC)

Para cada um: verificar se as 2–3 citações que chegaram ao texto estão corretas (autor, ano, título, URL).

---

## Bloco 5 — Reescrever PL-1934 com posição "nada a opor"

Marcel pediu explicitamente: "refazer esse, colocar nada a opor, citar os argumentos contrários".

- [ ] Reescrever `PL-1934-2026/manifestacao_PL-1934-2026-short.md` com:
  - Abertura: "nada a opor"
  - Corpo: argumento econômico principal (pricing hoteleiro, FOHB/HotelInvest)
  - Ressalva técnica: os 4 pontos do parágrafo de salvaguardas (excludente tempo técnico, gradualidade, limite a diárias unitárias, check-in por culpa do hóspede)
  - Manter os dados: FOHB/HotelInvest 2024, MTur 2024
- [ ] Regenerar PDF
- [ ] Usar como template para PLs futuros com trade-offs econômicos evidentes

---

## Métricas de sucesso para o próximo PL processado em V5

Preencher `PL-XXXX-YYYY/V5-AUDIT.md` após cada PL:

| Critério | Meta | Resultado |
|----------|------|-----------|
| NB criado e validado (≥ 5 fontes no list_sources.py) | ✅ | — |
| ≥ 1 citação internacional no short | ✅ | — |
| ≥ 4 citações totais no short | ✅ | — |
| ≥ 80% carry-through inventário → texto | ✅ | — |
| audit_sources Wave 1+2 aplicado | ✅ | — |
| Posição alinhada com SMDE (nada a opor + caveats) | ✅ | — |
| **Status geral** | **PASS** | — |

---

## Calendário estimado

| Prazo | Entregável |
|-------|------------|
| Imediato | ✅ Pasta V5 + 3 documentos criados |
| Próximo ofício CVL | Aplicar V5 full (P0 + bilíngue + retry + audit) |
| ~3 semanas | Retroativamente auditar PL-1883, PL-1866, PL-1795 |
| ~3 semanas | Reescrever PL-1934 com nova posição |
| ~6 semanas | Avaliar benchmarks: V5 atingiu metas? Planejar V6 se necessário |
