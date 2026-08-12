# Plano de Execução: Manifestação Técnica sobre PL

> **[HISTÓRICO]** Documento da fase V1–V3 (mai/2026), mantido como registro. O método vigente é o V5/V5.2: `workflow/V5/` + `workflow/V5.2/ECONOMIA-ONLY.md` (ótica exclusivamente econômica — sem argumento jurídico no corpo).

## Pré-requisito (feito pelo usuário, 1 vez por PL)

1. Acesse notebooklm.google.com
2. Crie notebook: `"PL-XXXX-YYYY — <ementa curta>"`
3. Adicione o PDF do PL como fonte
4. Me passe a URL

---

## Fase 0 — Ingestão (Claude Code, automático)

```bash
pdftotext "resumir projetos de lei/<arquivo>.pdf" - | head -300
mkdir -p "resumir projetos de lei/PL-XXXX-YYYY/"
```

Extrai: número, ementa, artigos, categoria, ofício.

---

## Fase 1 — Registro e pesquisa profunda no NotebookLM

```bash
# Registrar o notebook
cd ~/.claude/skills/notebooklm
python scripts/run.py notebook_manager.py add \
  --url "<URL do usuário>" \
  --name "PL-XXXX-YYYY — <ementa>" \
  --description "<tema>" \
  --topics "<categoria>,rio de janeiro,legislação municipal"

# Pesquisa profunda (popula NB com fontes relevantes automaticamente)
python scripts/run.py ask_question.py \
  --question "Faça uma pesquisa profunda sobre [tema do PL]. Quais as principais evidências acadêmicas, dados quantitativos e legislação correlata?" \
  --notebook-url "<URL>"

# Inventário real das fontes adicionadas
python scripts/run.py list_sources.py \
  --notebook-url "<URL>" \
  --out /tmp/nb_inventario_PL-XXXX-YYYY.json
```

---

## Fase 2 — agentic_research com NB-first

Lançar 4 duplas P+E em paralelo. **Cada pesquisador recebe a URL do NB e instrução obrigatória:**

```
PROTOCOLO DE BUSCA (obrigatório nesta ordem):
1. Consultar NotebookLM PRIMEIRO:
   cd ~/.claude/skills/notebooklm
   python scripts/run.py ask_question.py \
     --question "<pergunta específica do tópico>" \
     --notebook-url "<URL>"
   Fazer mínimo 3 queries com termos diferentes.
2. Só após esgotar o NB → WebSearch.
3. Toda fonte nova encontrada na web → adicionar ao NB antes de citar.
```

### Tópicos invariantes

| Dupla | Pesquisador busca | Escritor produz |
|-------|-------------------|-----------------|
| T1 | Legislação base + o que o PL altera artigo a artigo | Exegese econômico-descritiva (2 parágrafos; sem juízo de validade — V5.2) |
| T2 | Evidências de benefícios de medidas similares | Prós com citações formais |
| T3 | Riscos, lacunas, precedentes negativos | Ressalvas técnicas operacionais |
| T4 | Dados quantitativos locais + comparativo municipal | Parágrafo de dados |

### Formato de citação obrigatório (modelo Marcel)

```
(SOBRENOME, Inicial.; SOBRENOME2, Inicial. "Título do trabalho", Veículo/Editora, Ano)
```

Exemplos:
- `(LEITE, M. L. S.; CUNHA, E. V. "Economia solidária no Cariri", Observatório de la Economía Latinoamericana, 2024)`
- `(SECRETARIA NACIONAL DE ECONOMIA SOLIDÁRIA; IPEA. "Mapeamento de Economia Solidária no Brasil", IPEA, 2016)`
- `(IVISA-RIO. "Portaria nº 569/2023", Prefeitura do Rio de Janeiro, 2023)`

**Regras duras para os escritores:**
- Nenhuma citação sem `F-T.N` correspondente no inventário
- Zero `(Autor, ano)` informal — sempre formato completo acima
- Zero surveys fantasma

---

## Fase 3 — Costura

Coordenador monta o documento final:

```
[Abertura formal — referência ao ofício + posição]
[Exegese — rascunho T1]
[Benefícios — rascunho T2 com citações formais]
[Ressalvas técnicas — rascunho T3]
[Dados — rascunho T4]
[Conclusão técnica — "nada a opor" / ressalvas]
```

---

## Fase 4 — Output

```
resumir projetos de lei/PL-XXXX-YYYY/
  manifestacao_PL-XXXX-YYYY.md
  inventario_fontes_PL-XXXX-YYYY.md
```

Push para https://github.com/OttoBoop/manifestacoes-pl-rj

---

## Gatilho de execução

Quando o usuário disser: **"executa o plano para PL X, URL do NB: https://..."**
→ Claude Code executa as fases 0-4 sem mais planejamento.
