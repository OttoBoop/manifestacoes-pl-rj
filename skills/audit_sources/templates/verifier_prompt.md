# Template: Prompt do Agente Verificador (Wave 2)

Use este template ao lançar cada agente verificador via `Agent` com `subagent_type: general-purpose` e `run_in_background: true`.

Substitua `{{...}}` por valores concretos do case.

---

```
AGENTE VERIFICADOR — Bloco {{X}} ({{seções cobertas, ex: §2 Transformação NY}})
da auditoria de fontes de {{nome do estudo}}.

## Sua missão
Verificar cada fonte F-X.Y do recorte `{{caminho do bloco_X_input.md}}` contra
fonte primária. Para cada item, preencher status, trecho literal, localização
e histórico de busca em `{{caminho do bloco_X_output.md}}` (já existe; estenda
o que está lá).

## Princípios duros — NÃO NEGOCIÁVEIS

### 1. NotebookLM-FIRST
O usuário tem notebook curado com as fontes mais relevantes do case. Você
DEVE começar pelo NotebookLM antes de qualquer WebSearch ou WebFetch.

- Notebook URL: {{NOTEBOOK_URL}}
- Notebook ID: {{NOTEBOOK_ID}}
- Comando:
  ```bash
  cd /home/otavio/.claude/skills/notebooklm && \
    python scripts/run.py ask_question.py \
    --question "..." \
    --notebook-url "{{NOTEBOOK_URL}}"
  ```

Para cada F-X.Y, mínimo 1 query ao NotebookLM antes de ir para web.
Se o NotebookLM responder "não tenho essa fonte", documentar a resposta
literal e SÓ ENTÃO ir para web.

### 2. Aspas literais exigem trecho literal localizado
Se o texto auditado tem aspas duplas (citação literal), você precisa achar
a frase EXATA no documento original. Se não achar:
- Marque como ⚠️ PARCIAL
- Sugira ao coordenador remover as aspas (vira paráfrase) OU substituir por
  citação literal documentada
- NUNCA confirme uma aspa sem ter o trecho literal — isso é fabricação

### 3. "Não achei" exige esgotamento documentado
Antes de marcar ❓ INVERIFICÁVEL, você precisa ter:
- 3+ queries distintas no NotebookLM (com respostas literais registradas)
- 2+ métodos de extração de PDF tentados (curl+pdftotext, WebFetch, mirror)
- 5+ queries WebSearch variando termos
- Tudo registrado no histórico de busca abaixo

### 4. Você NÃO corta texto
Sua função é reportar status. Decisão de cortar/manter/reformular é do
usuário. Não sugira corte. Não infira além do que a fonte diz.

### 5. Adjetivos sem fonte são problemáticos
Se o texto auditado tem qualificações descritivas ("pichado", "icônico",
"considerado pequeno por especialistas"), tente localizar a fonte do adjetivo.
Se não achar, marque o adjetivo como ⚠️ PARCIAL com nota: "qualificação
descritiva sem fonte localizada".

### 6. Surveys fantasma são proibidos
Se o texto cita "pesquisa aponta", "surveys mostram", "estudos sugerem"
sem autor + ano + título, marque como ❓ e EXIJA fonte específica antes de
qualquer confirmação.

## Para cada fonte F-X.Y, preencher

```markdown
#### F-X.Y — {{título da fonte como já catalogado}}
- **Tipo:** {{já preenchido pelo extrator}}
- **Substancia (§X.Y):** {{já preenchido pelo extrator}}
- **Nota do artigo:** {{já preenchido pelo extrator}}
- **Status:** ✅ CONFIRMADA / ⚠️ PARCIAL / ❓ INVERIFICÁVEL
- **URL/ref candidata:** {{URL ou referência primária identificada}}
- **Verificação:**
  - **Trecho literal da fonte (para ✅):** "{{citação exata}}"
  - **Localização precisa:** {{URL+âncora, PDF+página, livro+capítulo}}
  - **Observações:** {{o que confere, o que não, nuances}}
- **Histórico de busca (OBRIGATÓRIO para ⚠️ e ❓):**

  ### NotebookLM (notebook: {{NOTEBOOK_ID}})
  - **Q1 (literal):** "..."
  - **Resposta NB (literal, completa, NÃO RESUMIDA):** "..."
  - **Q2 (se Q1 não bastou):** "..."
  - **Resposta NB:** "..."

  ### PDF primário
  - **URL tentada:** ...
  - **Método 1 (WebFetch):** {{resultado: ok/binário/403/timeout}}
  - **Método 2 (curl + pdftotext):**
    ```bash
    curl -L "URL" -o /tmp/file.pdf && pdftotext /tmp/file.pdf - | head -200
    ```
    {{resultado}}
  - **Método 3 (se aplicável):** {{ocrmypdf, mirror IA, SciHub, etc.}}

  ### WebSearch
  - **Q1:** "..." → top hits: ...
  - **Q2:** "..." → top hits: ...
  - **(mínimo 5 queries para ❓)**

  ### Fontes secundárias verificadas (se houver)
  - {{nome + URL + o que confirma}}
```

## Distinção crítica: aspas vs paráfrase

- **Aspas literais entre " " no texto auditado** → você precisa achar a frase
  EXATA. Não confirme com "espírito alinhado" ou "fonte trata do tema".
- **Paráfrase atribuída ("Bratton argumenta que...", "Cano faz um diagnóstico
  de...")** → você verifica se a TESE/INFORMAÇÃO está na obra do autor. Não
  precisa achar formulação exata.

## Distinção crítica: número e categoria

Quando o texto cita um número específico em contexto técnico, a categoria
importa tanto quanto o número. Exemplos do case Compstat:
- "homicídios dolosos" ≠ "letalidade violenta" ≠ "mortes violentas" no ISP-RJ
- "perda turística" pode ser CNC ou IFec-RJ — verificar atribuição
- Pesquisas de opinião têm DATA DE CAMPO ≠ DATA DE PUBLICAÇÃO — checar ambas

Sempre confirmar a definição operacional da métrica antes de validar o número.

## Proibições explícitas

- ❌ NÃO corte texto. NÃO sugira corte. NÃO infira além da fonte.
- ❌ NÃO invente trechos para preencher "Trecho literal".
- ❌ NÃO marque ❓ INVERIFICÁVEL sem esgotamento documentado (regra 3).
- ❌ NÃO pule o NotebookLM (regra 1).
- ❌ NÃO confirme aspas literais sem trecho literal localizado (regra 2).
- ❌ NÃO sugira "surveys" sem autor+ano+título como substituição.
- ❌ NÃO trave em PDF binário — use receitas do appendix técnico da skill.

## Output

Preencher `{{caminho do bloco_X_output.md}}` — preserve o cabeçalho e
estenda cada F-X.Y conforme estrutura acima.

Ao final do arquivo, adicionar relatório curto:

```markdown
## Relatório final do Bloco {{X}}

### Totais
- ✅ CONFIRMADA: N
- ⚠️ PARCIAL: N
- ❓ INVERIFICÁVEL: N

### Fontes problemáticas (com motivo)
1. F-X.Y — {{tipo de problema + sugestão}}
2. ...

### Lições para a skill (audit_sources)
1. {{padrão observado neste bloco que deveria virar regra geral}}
```

## Limites operacionais

- Tempo alvo: 15-20 minutos por bloco (mais que Wave 2 anterior porque
  NotebookLM-first adiciona overhead — vale a pena pela qualidade)
- Out-of-credit é comum nos últimos minutos: sempre persistir output no
  arquivo conforme avança, NÃO esperar acumular tudo no final
- Se NotebookLM falhar (re-auth necessária, browser crash), reporte ao
  coordenador imediatamente via output parcial — não tente seguir só com web

Retorne ao coordenador (a) caminho do output, (b) resumo curto dos achados,
(c) qualquer obstáculo técnico (PDF que não cedeu, NotebookLM down, etc.).
```

---

## Notas sobre o template

### Por que NotebookLM-first
Falha histórica do case Compstat (2026-04): 5 verificadores rodaram com **zero** chamadas ao NotebookLM, apesar de o notebook conter Cardoso 2024 e papers acadêmicos centrais. O coordenador improvisava o prompt e esquecia de mencionar o NB. Template formal resolve.

### Por que histórico de busca obrigatório
O usuário pediu "provas concretas" de que uma fonte não existe — não basta o agente dizer "não achei". O histórico expandido permite ao usuário:
- Auditar a auditoria (queries foram bem formuladas?)
- Detectar se o agente desistiu cedo demais
- Reproduzir a busca se quiser

### Por que distinguir aspas vs paráfrase
Causa raiz de vários ⚠️ no case Compstat: agente confirmava paráfrase como se fosse aspa literal, ou marcava aspa literal como inverificável quando deveria sugerir reformulação como paráfrase.

### Quando usar este template
Após Wave 1 (extração) ter populado o `auditoria_fontes.md` com blocos F-X.Y. Cada verificador recebe um recorte (`bloco_X_input.md`) com sub-conjunto de F-X.Y para verificar.
