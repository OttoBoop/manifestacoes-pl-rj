---
name: agentic_research
description: Orquestra N duplas de agentes (1 pesquisador + 1 escritor por tópico) em paralelo para produzir um documento longo fundamentado, com comunicação bidirecional P↔E mediada pelo coordenador e reporte contínuo ao usuário. Use para notas técnicas, estudos, artigos, white papers ou qualquer peça longa que exija pesquisa séria + escrita coesa.
---

# Agentic Research

## Quando usar

Dispare esta skill quando o usuário pedir um documento longo (≥ 1.500 palavras) que:
- Exige pesquisa em múltiplas fontes (NotebookLM, web, arquivos locais)
- Se beneficia de uma narrativa coesa com múltiplas seções
- Seria lento demais escrito sequencialmente
- Admite decomposição em **tópicos narrativos** (não apenas seções formais)

Exemplos de pedido: "escreva uma nota técnica sobre X nos moldes Y", "quero um estudo sobre Z", "faça uma análise profunda de W com fontes".

**Não use** para respostas curtas, explicações diretas, ou peças sem exigência de pesquisa.

## Arquitetura

```
                        ┌────────────────────────────────┐
                        │  COORDENADOR (modelo principal)│
                        │  • Define N tópicos narrativos │
                        │  • Supervisiona progresso      │
                        │  • Reporta ao usuário          │
                        │  • Costura produto final       │
                        └──┬─────────────────────────────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
       TÓPICO T1      TÓPICO T2   ...  TÓPICO Tn
            │              │              │
        ┌───┴───┐      ┌───┴───┐      ┌───┴───┐
      [P1]  [E1]    [P2]  [E2]    [Pn]  [En]
       pesquisa  escreve   em paralelo
```

**Paralelismo em 2 níveis:**
1. **Entre tópicos:** as N duplas rodam simultaneamente
2. **Dentro da dupla:** P e E rodam em paralelo — E já vai escrevendo com o brief enquanto P pesquisa

**Comunicação P↔E (mediada pelo coordenador via SendMessage):**
- `[PRECISO DE P: <pergunta>]` — escritor pede clarificação ao pesquisador
- `[SUGESTÃO PARA E: <info>]` — pesquisador oferece algo novo ao escritor
- Iterações podem ocorrer várias vezes por dupla

**Documentação de fontes desde o início (integração com `audit_sources`):**

Toda dupla P+E deve produzir, junto com o rascunho, um **inventário de fontes rastreáveis**. Isso evita que o texto vá para auditoria posthoc com atribuições erradas ou citações que não existem.

- **Pesquisador** entrega, junto ao relatório narrativo, uma lista `F-T.N` no mesmo formato que `audit_sources` consome: autor, ano, título, URL + âncora ou PDF + página, trecho (literal ou paráfrase com localização).
- **Escritor** cita no rascunho com autor-data ou nota sobrescrita, e referencia o `F-T.N` do inventário do pesquisador quando a fonte não for óbvia, deixando rastro para auditoria futura.
- **Regra dura:** nenhuma citação entra no texto sem um item correspondente no inventário. Se o pesquisador não conseguiu ancorar uma afirmação em fonte verificável, essa afirmação volta para discussão — não vai para o rascunho.

Quando o documento final for submetido a `audit_sources`, a Wave 2 de verificação encontra material já trabalhado — o trabalho de auditoria vira conferência (não reinvestigação do zero).

**O NotebookLM é a base de conhecimento do projeto inteiro:**

O pesquisador NÃO acumula fontes só localmente para o relatório dele. Toda fonte usada precisa estar (ou ser adicionada) ao **NotebookLM do caso** — aquele que o usuário curou no início do projeto. Isso porque:

1. **Pipeline `agentic_research → audit_sources` é mediada pelo NB.** A skill `audit_sources` começa toda verificação no NB (regra dura: NotebookLM-first). Se o pesquisador trabalhou direito, **toda evidência citada no texto está no NB** — então o auditor encontra tudo lá. Sem isso, audit_sources reinventa a roda.
2. **NB tem funções nativas que ajudam o pesquisador.** "Pesquisa rápida" e "pesquisa profunda" do NB **adicionam fontes automaticamente à biblioteca** quando ele encontra material novo. O pesquisador deve usar essas funções como ferramenta primária — não só fazer queries one-shot.
3. **Conhecimento sobrevive ao projeto.** Quando o estudo termina, o NB fica como acervo verificável — outros estudos podem se beneficiar, e auditorias futuras têm base sólida.

**Constraint dura para o pesquisador:**
- Comece toda busca pelo NotebookLM do caso (não pelo Google).
- Quando achar fonte nova relevante na web, **adicione-a ao NB** (via função de adicionar fonte) antes de citá-la no relatório.
- Use "pesquisa profunda" do NB para temas amplos — ela varre fontes e adiciona automaticamente.
- Cada item `F-T.N` do inventário deve ter um identificador da fonte no NB (título do documento como aparece no painel lateral).

**Por que isso é estrutural:** o auditor tem regra dura "NB-first". Se o pesquisador deixou fontes só em arquivos locais ou só na web, o auditor não encontra na primeira passada e (a) precisa de muito mais tempo, (b) corre risco de marcar como "não localizada" uma fonte que de fato existe mas não está catalogada onde deveria estar, (c) pode produzir falsos negativos. A pipeline só funciona quando o pesquisador respeita o NB como base canônica.

## Fluxo executivo

### Fase 0 — Planejamento (coordenador + usuário)

1. **Entender a narrativa** com o usuário: tese, público-alvo, tom, guia de estilo, extensão-alvo
2. **Decompor em N tópicos narrativos** (geralmente 5-8). Cada tópico = um argumento que avança a tese
3. **Definir mapa tópico → seção do documento final**
4. **Apresentar plano ao usuário** e obter aprovação antes de gastar tokens com agentes

### Fase 1 — Wave Pesquisa + Escrita (paralela)

Lançar **em uma única mensagem com múltiplas Agent calls em paralelo**:
- N agentes Pesquisadores (P1...Pn) em background
- N agentes Escritores (E1...En) em background — simultâneos aos pesquisadores

Cada escritor recebe:
- Narrativa geral + guia de estilo
- Brief do tópico (argumento, extensão, vizinhança)
- Instrução para começar a escrever com o que tem + sinalizar `[PRECISO DE P: …]` se faltar
- ID do pesquisador correspondente (para futuros SendMessage)

**Importante:** o relatório do pesquisador pode ou não estar pronto quando o escritor começa. Se não estiver, o escritor trabalha com o brief e aguarda passivamente — sem bloquear — a chegada do material.

Se o pesquisador entregar primeiro, o coordenador pode opcionalmente encaminhar o relatório ao escritor via SendMessage.

### Fase 2 — Coordenação e mediação

Conforme eventos chegam (agent completion, pedidos P↔E):
1. Identificar se há pedido `[PRECISO DE P: …]` → SendMessage ao P correspondente, recebe, encaminha ao E via SendMessage
2. Identificar se há `[SUGESTÃO PARA E: …]` → avaliar relevância e, se for o caso, encaminhar ao E
3. **Reportar ao usuário** em formato sintético:

```
📊 Status [HH:MM]
• T1: E1 entregou — 740 palavras ✓
• T2: E2 pedindo dados a P2; SendMessage enviado
• T3: P3 sugeriu info nova; encaminhei a E3
• T4-T7: em andamento
```

**Gatilhos de pausa (usar AskUserQuestion):**
- Argumento-base do plano não se sustenta nas fontes
- Rascunhos se contradizem em fato central
- Escritor propõe reestruturação significativa da narrativa

### Fase 3 — Costura

Quando todos os N escritores entregaram:
1. Ler os N rascunhos na sequência da narrativa
2. Produzir documento integrado com:
   - Transições suaves entre seções
   - Gancho/tese presente em TODAS as seções (não só a final)
   - Numeração de referências consolidada
   - Conclusão curta e enfática
3. Validar contra guia de estilo (quando houver)

## Convenções de prompt

### Prompt do Pesquisador (P)

```
Você é o PESQUISADOR P{N} de [descrição do estudo].

## Contexto do estudo
- Público: …
- Tese: …
- Paralelos/ganchos: …

## Seu tópico (T{N}: "<nome>")
**Argumento a fundamentar:** …
**Perguntas específicas a responder:** …

## Ferramentas
- WebSearch, NotebookLM (via skill), Read de arquivos locais

## Formato do relatório (400-800 palavras)
# Relatório P{N} — <tópico>
## <subseção 1>
## <subseção 2>
## Fontes principais (com URLs quando houver)

Retorne APENAS o relatório.
```

### Prompt do Escritor (E)

```
Você é o ESCRITOR E{N} de [descrição do estudo].

## Contexto do estudo
- Público, tese, paralelos, guia de estilo (leia o arquivo X)

## Sua missão (Tópico T{N}: "<nome>")
**Argumento central:** …
**Extensão alvo:** …
**Posição no documento:** …
**O que deve estar presente:** …

## Relatório do seu pesquisador P{N} (se já entregue)
<texto do relatório>

## Canal com pesquisador P{N}
Se precisar, marque `[PRECISO DE P: <pergunta específica>]`. O coordenador
consultará P{N} (ID <id>) e te devolverá a resposta. Enquanto isso, continue
escrevendo outras partes — não bloqueie.

## Formato de output
1. Rascunho em markdown (citações conforme guia)
2. Lista de fontes usadas
3. Opcional: [PRECISO DE P: ...]

Retorne SOMENTE esses três itens.
```

Templates completos em `templates/researcher_prompt.md` e `templates/writer_prompt.md`.

## Sinais entre agentes

| Sinal | De | Para | Ação do coordenador |
|-------|-----|------|---------------------|
| `[PRECISO DE P: ...]` | E | P | SendMessage a P com a pergunta; devolver resposta a E via SendMessage |
| `[SUGESTÃO PARA E: ...]` | P | E | Avaliar relevância; se encaixa na narrativa, encaminhar a E via SendMessage |
| `[CONTRADIÇÃO COM T{X}]` | E ou P | Coord | Pausar, investigar, e se preciso perguntar ao usuário |
| `[RESTRUTURAR NARRATIVA]` | E | Coord | Pausar e usar AskUserQuestion para alinhar com usuário |

## Exemplos de uso

**Caso de validação (2026-04):** nota técnica "Compstat Integral vs. Compstat Lite" para o Gabinete do Vereador Flávio Valle. 7 tópicos narrativos, 7 duplas de agentes, ~11.000 palavras de artigo integrado. Ver `/home/otavio/Documents/vscode/flaviovalle-estudos/compstat/artigo_compstat.md` como referência.

**Outros casos aplicáveis:**
- Estudos comparativos de política pública (benchmark internacional → recomendação local)
- Análises históricas com múltiplas fontes primárias
- Relatórios técnicos multi-capítulo
- Artigos acadêmicos com revisão de literatura + empírico + discussão

## Dicas operacionais

1. **Comece com planejamento sólido.** Cada tópico deve ser claramente delimitado. Sobreposição entre tópicos gera rascunhos redundantes.
2. **Nunca lance agentes sem brief detalhado.** Um escritor sem contexto narrativo produz texto genérico.
3. **Use NotebookLM quando o usuário tiver curadoria de fontes** — reduz alucinação drasticamente. Para web search, prefira dados institucionais (governo, IBGE, ISP, FBI, etc.).
4. **Relatórios ao usuário devem ser breves DURANTE o fluxo, prolixos NO CHECKPOINT.** Em fluxo (ex.: status entre wave 1 e 2), bullets com ✓/⏳/⚠ bastam. Em revisão geral (ex.: consolidação para decisão humana), prolixidade é desejada — o usuário precisa do contexto literal de cada item para decidir. Comprimir para 8 itens uma lista de 50 erros é falha grave (case Compstat 2026-04).
5. **Não costure prematuramente.** Espere todos os rascunhos antes de começar a Fase 3 — pode haver dependências cruzadas que só aparecem ao ler tudo junto.
6. **Respeite o guia de estilo do usuário.** Se ele tiver um, passe o caminho do arquivo para cada escritor com instrução de leitura obrigatória.
7. **Atenção às permissões.** Se a skill precisar criar arquivos em `~/.claude/skills/`, pode enfrentar bloqueio — o coordenador (não o subagente) costuma ter permissão.

## Regras duras (emergidas do case Compstat, 2026-04)

1. **Coordenador relata em tempo real ao humano.** O ato de verbalizar o que cada agente está fazendo é parte do controle de qualidade — força o coordenador a notar inconsistências (que ficariam invisíveis se ele só observasse) e permite ao humano intervir antes de erros se acumularem. Fala do usuário: *"só de falar para o humano o que está acontecendo, o orquestrador já pode perceber alguns erros por parte dos agentes — melhor do que se ele simplesmente estivesse observando sem precisar relatar nada ao humano"*.

2. **Adjetivos descritivos sem fonte são proibidos.** "Pichado de ponta a ponta", "considerado pequeno por especialistas", "icônico" — toda qualificação descritiva precisa fonte ou sai. Escritor não inventa qualificações para preencher espaço narrativo. Fala do usuário: *"Quem disse que estava pichado? Quem???"*.

3. **Argumentos sem citação são proibidos.** "Pesquisas mostram", "surveys indicam", "estudos sugerem" sem autor + ano + título identificáveis NÃO entram no texto. Se o ponto é válido mas a fonte é "lembrança vaga", pesquisador busca fonte real ou escritor remove. Fala do usuário: *"Não existem surveys fantasma, você precisa dar a fonte para esse tipo de informação"*.

4. **Atribuições autor-data exigem fonte real.** Escritor não pode escrever "Harcourt e Ludwig (2006) documentam X" se o paper deles não documenta X. Falha histórica do case Compstat: paper Harcourt & Ludwig 2006 (sobre broken windows vs Moving to Opportunity) foi citado para sustentar tese sobre turismo que não está no paper. Pesquisador deve confirmar atribuição antes de o escritor citar.

5. **Aspas duplas exigem trecho literal documentado.** Se o pesquisador não tem o trecho literal, escritor usa paráfrase atribuída sem aspas. Falha histórica: aspas atribuídas a Bratton, McCarthy, Anemone que ninguém localizou em fonte primária.

6. **Documentação de fontes desde o início.** Pesquisador entrega lista no formato `F-T.N` consumível pela skill `audit_sources` (autor, ano, título, URL+âncora ou PDF+página, trecho literal ou paráfrase com localização). Escritor cita autor-data ou nota sobrescrita E referencia o `F-T.N` do inventário do pesquisador. Sem isso, `audit_sources` reinventa a roda na auditoria.
