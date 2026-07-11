# Workflow: Manifestação Técnica Automatizada sobre PLs

> ⚠️ **Documento histórico — versão V1 do método (mai/2026).**  
> Este documento descreve a abordagem **jurídica** original (V1) do projeto, com foco em exegese de incisos e análise de competência constitucional. Esse foco foi **superado** após feedback dos colaboradores ("a SMDE dá opinião econômica, não jurídica").  
>  
> **Para o método atual** e para replicar o fluxo, consultar:  
> - [README.md](README.md) — documentação completa e didática das 4 versões do método (V1→V4) com receita passo a passo  
> - [workflow/PROOF-OF-CONCEPT.md](workflow/PROOF-OF-CONCEPT.md) — log de execução completo e workarounds  
> - [workflow/V4-COMPARACAO.md](workflow/V4-COMPARACAO.md) — tabela comparativa V3 vs V4 caso a caso  
>  
> Este documento é preservado para referência histórica da evolução do método.

---

**Versão:** 1.0 — mai/2026  
**Autor:** Otávio Bopp (com suporte do Claude Code / Ariadne)  
**Contexto:** Subsecretaria — análise de Projetos de Lei da Câmara Municipal do Rio de Janeiro

---

## Sumário executivo

Este workflow automatiza a produção de manifestações técnicas sobre Projetos de Lei (PLs),
respondendo a ofícios que solicitam posição da Subsecretaria sobre proposições legislativas.

**O problema inicial:** cada PL é único — tema, impacto, legislação correlata e dados relevantes
variam completamente de um para o outro. A princípio, isso parece inviabilizar uma análise
sistemática automatizada.

**A resposta:** o que é invariante não é o *conteúdo*, mas a *estrutura analítica*. Toda
manifestação precisa responder às mesmas perguntas — o que o PL faz, quais são os efeitos
esperados, quais são os riscos, quais dados sustentam a análise — e sempre conclui com uma
posição técnica fundamentada. Isso permite um fluxo de agentes com constraints bem definidos:
um pesquisador por tópico, buscando evidências reais; um escritor por seção, produzindo
texto com citações rastreáveis.

**Tecnologia utilizada:** Claude Code com três skills encadeadas:
- `notebooklm` — base de conhecimento por PL, com acesso ao Google NotebookLM via automação de browser
- `agentic_research` — 4 duplas pesquisador + escritor rodando em paralelo, uma por tópico analítico
- `audit_sources` — verificação opcional das citações antes do envio oficial

---

## Arquitetura

```
INPUT: PDF do PL depositado em pasta
            │
            ▼
    ┌─────────────────┐
    │  FASE 0         │  Extração de texto (pdftotext)
    │  Ingestão       │  → número PL, ementa, artigos, categoria
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │  FASE 1         │  Criar notebook no Google NotebookLM
    │  NotebookLM     │  → adicionar PDF do PL como fonte primária
    └────────┬────────┘  → pesquisa profunda inicial para popular fontes
             │
             ▼
    ┌─────────────────┐
    │  FASE 2         │  Coordenador lê PL → define 4 tópicos invariantes
    │  Planejamento   │  → apresenta plano ao usuário para aprovação
    └────────┬────────┘
             │
             ▼
    ┌─────────────────────────────────────────────┐
    │  FASE 3 — Pesquisa + Escrita (paralelo)      │
    │                                              │
    │  [P1] Exegese ──► [E1] Exegese              │
    │  [P2] Prós    ──► [E2] Prós                 │
    │  [P3] Contras ──► [E3] Contras              │
    │  [P4] Dados   ──► [E4] Dados/Comparativo    │
    │                                              │
    │  Pesquisadores: NB-first → web → adicionam   │
    │  fontes ao NB; entregam inventário F-T.N     │
    └────────┬────────────────────────────────────┘
             │
             ▼
    ┌─────────────────┐
    │  FASE 4         │  Coordenador costura os 4 rascunhos
    │  Produção       │  no formato oficial de manifestação
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │  FASE 5         │  manifestacao_PL-XXXX-YYYY.md
    │  Output         │  inventario_fontes_PL-XXXX-YYYY.md
    └────────┬────────┘
             │
             ▼
    Revisão humana (Marcel/Otávio)
    → Word → assinatura → envio oficial
```

---

## Fase 0 — Ingestão do PL

**Gatilho:** PDF do PL depositado na pasta `resumir projetos de lei/`.

**O coordenador executa:**

```bash
# Extrair texto do PDF para leitura
pdftotext "resumir projetos de lei/<arquivo>.pdf" - | head -300

# Criar diretório de trabalho para este PL
mkdir -p "resumir projetos de lei/PL-XXXX-YYYY/"
```

**Extrai e registra:**
- Número do PL (ex: `1736/2025`)
- Ementa completa (título do projeto entre aspas)
- Número do ofício solicitante (se fornecido junto)
- Categoria temática (urbanismo, saúde, cultura, mobilidade, segurança, etc.)
- Artigos principais — o que o PL cria, altera ou revoga
- Leis existentes que o PL menciona ou afeta

---

## Fase 1 — Criação do NotebookLM

**Por que 1 notebook por PL:** o NotebookLM é a base de conhecimento canônica do projeto.
Os pesquisadores começam suas buscas nele, adicionam fontes novas durante a pesquisa,
e o auditor (se acionado) encontra tudo centralizado lá. Sem o NB, cada fase reinventa a roda.

**Passo 1 — Usuário cria o notebook no Google NotebookLM (manual):**
> Acesse notebooklm.google.com → Criar notebook → Adicionar o PDF do PL como fonte → Copiar URL

**Passo 2 — Registrar o notebook no Claude Code:**

```bash
cd ~/.claude/skills/notebooklm
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "PL-XXXX-YYYY — <ementa curta>" \
  --description "<tema do PL em 1-2 frases>" \
  --topics "<categoria>,rio de janeiro,câmara municipal"
```

**Passo 3 — Pesquisa profunda inicial (popula o NB):**

```bash
python scripts/run.py ask_question.py \
  --question "Quais são as principais evidências acadêmicas, dados quantitativos e legislação
correlata sobre [tema do PL]? Inclua papers, relatórios institucionais e dados do município
do Rio de Janeiro quando disponíveis." \
  --notebook-url "https://notebooklm.google.com/notebook/..."
```

Isso usa a função de pesquisa profunda do NB, que varre e adiciona fontes automaticamente.
O NB começa com o PDF do PL e termina esta fase com 10-30 fontes relevantes.

---

## Fase 2 — Decomposição em tópicos

O coordenador lê o texto extraído do PL e monta o plano de análise.

**4 tópicos invariantes para qualquer PL:**

| # | Tópico | Pergunta central |
|---|--------|-----------------|
| T1 | **Exegese jurídica** | O que o PL exatamente cria, modifica ou revoga? Qual o contexto jurídico? Quais leis existentes são afetadas? |
| T2 | **Prós e benefícios** | Quais os efeitos positivos esperados? Há evidências empíricas de medidas similares? |
| T3 | **Contras e riscos** | Quais os riscos e efeitos colaterais? Há precedentes negativos em outros contextos? |
| T4 | **Dados + Comparativo** | Quais números sustentam (ou questionam) o PL? Como outros municípios trataram questão similar? |

**Antes de lançar os agentes**, o coordenador apresenta ao usuário:
- Os 4 tópicos com as perguntas específicas
- As fontes que o NB já tem (resultado da pesquisa profunda)
- Estimativa de tempo

Aguarda aprovação explícita antes de prosseguir.

---

## Fase 3 — Pesquisa paralela (agentic_research)

O coordenador lança **4 duplas pesquisador + escritor em paralelo**, em uma única chamada.

### Prompt-base do Pesquisador

```
Você é o PESQUISADOR P{N} da análise do PL {número}/{ano}.

## Contexto
PL: {ementa completa}
Categoria: {categoria temática}
NotebookLM do caso: {URL}

## Seu tópico (T{N}: "{nome}")
Pergunta central: {pergunta do tópico}
Perguntas específicas: {3-5 perguntas derivadas do texto do PL}

## Protocolo de busca (obrigatório nesta ordem)
1. NotebookLM PRIMEIRO — sempre. Use ask_question.py com 3+ queries variando termos.
2. Quando achar fonte relevante na web, adicione ao NB via notebook_manager.py antes de citar.
3. WebSearch para fontes não presentes no NB.

## Prioridade de fontes para {tópico}
{lista específica por tópico — ver seção abaixo}

## Formato de entrega
- Relatório narrativo (400-600 palavras)
- Inventário F-T.N: autor | ano | título | URL/página | trecho relevante
- Regra dura: nenhuma afirmação sem entrada F-T.N correspondente
```

### Prioridade de fontes por tópico

**T1 (Exegese):**
- Legislação municipal RJ (Leis Orgânicas, leis complementares, decretos)
- Legislação federal correlata
- Doutrina jurídica (livros, artigos de direito municipal/urbanístico)
- Precedentes legislativos em outros municípios

**T2 (Prós):**
- Papers acadêmicos (Google Scholar, SciELO, NBER, IPEA)
- Relatórios FGV, IPEA, IBRE
- Cases de sucesso documentados em outros municípios/países
- Dados IBGE relevantes ao tema

**T3 (Contras):**
- Papers críticos ou com resultados mistos
- Notas técnicas de organizações especializadas
- Casos de insucesso ou efeitos colaterais documentados
- Estudos com ressalvas ao tipo de medida proposta

**T4 (Dados + Comparativo):**
- IBGE, IPP/RJ, ISP-RJ, Prefeitura RJ (dados locais)
- SEBRAE, CNI, associações setoriais (dados econômicos)
- Prefeituras de SP, BH, Curitiba (comparativos)
- Relatórios setoriais nacionais e internacionais

### Comunicação entre agentes

| Sinal no texto | De | Ação do coordenador |
|---|---|---|
| `[PRECISO DE P: ...]` | Escritor | Envia pergunta ao pesquisador via SendMessage; repassa resposta ao escritor |
| `[SUGESTÃO PARA E: ...]` | Pesquisador | Avalia relevância e encaminha ao escritor |
| `[CONTRADIÇÃO COM T{X}]` | Qualquer | Pausa, investiga, pergunta ao usuário se necessário |

### Relatórios de status ao usuário

O coordenador reporta a cada conclusão de dupla, no formato:

```
📊 Status [HH:MM]
• T1 (Exegese): P1 entregou 8 fontes + E1 com rascunho — ✓
• T2 (Prós): E2 pediu dados adicionais a P2; aguardando resposta
• T3 (Contras): P3 + E3 em andamento
• T4 (Dados): em andamento
```

---

## Fase 4 — Produção da manifestação

Quando todos os 4 escritores entregaram, o coordenador costura o documento final.

### Formato oficial

**Bloco 1 — Abertura formal**

> Em atenção ao Ofício [ÓRGÃO] nº [N]/[ANO], acerca do PL nº [N]/[ANO], que
> "[EMENTA COMPLETA ENTRE ASPAS]", rogando manifestação técnica sobre a proposição
> legislativa em tela, cumpre informar que esta Subsecretaria se posiciona em sentido
> de [**nada a opor** / **apresentar as seguintes ressalvas técnicas**] à proposta.

**Bloco 2 — Exegese** *(rascunho T1, ~2 parágrafos)*  
O que o PL cria ou altera. Qual o enquadramento jurídico. Que leis existentes são tocadas.
Qual a finalidade declarada.

**Bloco 3 — Análise dos efeitos** *(rascunhos T2 + T3, ~3-4 parágrafos)*  
Prós com citações author-date. Contras e riscos com citações. Se análise não identificou
contras substantivos: registrar brevemente que "a análise não identificou objeções técnicas
relevantes" e seguir para a conclusão.

**Bloco 4 — Dados e comparativo** *(rascunho T4, integrado ou como parágrafo próprio)*  
Números relevantes. Precedentes em outros municípios se disponíveis.

**Bloco 5 — Conclusão**

> Portanto, [tendo em vista os benefícios identificados / considerando as ressalvas apontadas],
> esta Subsecretaria posiciona-se em sentido de [**nada a opor** / **nada a opor, com sugestão
> de emenda conforme item X** / **apresentar ressalvas técnicas quanto a...**] ao PL [N]/[ANO].

### Sobre a posição final (regra de tom)

A conclusão é **técnica**, não política. Três formulações possíveis:

| Situação | Formulação |
|---|---|
| Análise não identificou objeção técnica substantiva | "nada a opor" |
| Análise identificou ponto técnico menor corrigível | "nada a opor, com sugestão de emenda: [texto]" |
| Análise identificou risco técnico concreto com evidência | "apresentamos ressalvas técnicas quanto a [X], com base em [evidência Y]" |

**Nunca:** recomendação de rejeição por razões políticas. O sistema analisa; a decisão política
é da Subsecretaria, não do workflow.

---

## Fase 5 — Output e revisão humana

**Arquivos gerados** em `resumir projetos de lei/PL-XXXX-YYYY/`:

```
manifestacao_PL-XXXX-YYYY.md      ← texto da manifestação, pronto para revisão
inventario_fontes_PL-XXXX-YYYY.md ← inventário F-T.N de todas as fontes usadas
```

**Fluxo de revisão:**
1. Marcel ou Otávio lê `manifestacao_PL-XXXX-YYYY.md`
2. Verifica se a posição final faz sentido técnico
3. Confere citações que pareçam frágeis contra o inventário
4. Copia para Word, formata conforme template do gabinete
5. Assina e envia em resposta ao ofício

**Auditoria opcional (antes do envio):**  
Se a manifestação tiver citações densas ou posição com ressalvas, acionar `audit_sources`
para verificação formal antes de assinar. Ver `~/.claude/skills/audit_sources/SKILL.md`.

---

## Regras duras

1. **NB-first.** Toda busca começa no NotebookLM do PL — sem exceção, sem palpite sobre
   "esse tema provavelmente não está lá". O NB é a base do projeto.

2. **Sem surveys fantasma.** "Pesquisas mostram", "estudos indicam" sem autor + ano + título
   identificáveis são proibidos. Pesquisador encontra a fonte ou escritor remove a afirmação.

3. **Sem adjetivos sem fonte.** Qualificações descritivas ("bem-sucedido", "consolidado",
   "amplamente reconhecido") exigem fonte ou saem do texto.

4. **Atribuições author-date exigem fonte real.** Escritor não escreve "Silva (2022) demonstra X"
   sem que pesquisador tenha confirmado que Silva (2022) de fato demonstra X.

5. **Conclusão técnica, não política.** A posição final deve ser fundamentada nas evidências
   encontradas na pesquisa, não em preferência do analista.

6. **Coordenador reporta em tempo real.** A cada dupla P+E concluída, o coordenador informa
   o usuário. Não aguarda todos os agentes para dar o primeiro sinal de vida.

7. **Inventário F-T.N obrigatório.** Rascunho sem inventário de fontes não é aceito na costura.

---

## Anti-padrões conhecidos

- **Citar "doutrina" vagamente** sem identificar autor, obra e ano — proibido
- **Omitir a seção de contras** porque o PL parece bom — a seção existe sempre; se não há contras
  substantivos, isso é registrado explicitamente
- **Pular a criação do NB** ("é mais rápido ir direto na web") — quebra a pipeline de auditoria
- **Surveyes fantasma na sugestão de reescrita** — se uma citação caiu, não inventar outra vaga
  para substituir; ou a fonte é real ou a afirmação sai
- **Conclusão política disfarçada de técnica** — se a evidência encontrada não sustenta uma
  posição clara, a conclusão é "nada a opor" + registro das limitações da análise

---

## Exemplo de uso

```
Usuário: "Tenho o PDF do PL 1736/2025 (Polo Gastronômico Magarça). Faz a manifestação."

Coordenador:
  [Fase 0] Lê PDF → PL 1736/2025 / Polo Gastronômico Praça Joaquim Casemiro /
           Lei Geral dos Polos 7.498/2022 / categoria: desenvolvimento econômico urbano

  [Fase 1] Solicita ao usuário: adicione o PDF ao NB "PL-1736-2025 — Polo Magarça"
           Registra NB no Claude Code. Roda pesquisa profunda → NB ganha fontes sobre
           clusters urbanos, Lei 7.498, polos RJ

  [Fase 2] Define tópicos:
    T1: O que é a Lei 7.498 e como o PL altera o rol de polos
    T2: Evidências de efeitos de reconhecimento oficial de clusters comerciais
    T3: Riscos (expectativa frustrada, ausência de ação pública, gentrificação)
    T4: Dados de atividade econômica em Guaratiba / clusters no Rio
  → Apresenta ao usuário → aprovação

  [Fase 3] Lança 4 duplas em paralelo
    P2 encontra: Bulhões et al. 2024 (IBRE), Bolter & Robey 2020 (Upjohn)
    P3 nota: sem contras substantivos para esse tipo de reconhecimento simbólico
    P4 traz: dados ISP-RJ de Guaratiba, histórico de polos reconhecidos no RJ

  [Fase 4] Costura → manifestação no formato oficial com "nada a opor"

  [Fase 5] Salva:
    manifestacao_PL-1736-2025.md
    inventario_fontes_PL-1736-2025.md
```

O resultado deve ser comparável à manifestação que Marcel produziu manualmente —
mas com citações rastreadas, inventário de fontes e capacidade de replicar para qualquer
outro PL com o mesmo rigor.

---

## Localização dos arquivos

| O quê | Onde |
|---|---|
| PDFs dos PLs | `resumir projetos de lei/` |
| Workflow (este arquivo) | `resumir projetos de lei/workflow_manifestacao_pl.md` |
| Outputs por PL | `resumir projetos de lei/PL-XXXX-YYYY/` |
| Skill notebooklm | `skills/notebooklm/SKILL.md` (cópia versionada; executável em `~/.claude/skills/notebooklm/`) |
| Skill agentic_research | `skills/agentic_research/SKILL.md` (cópia versionada; executável em `~/.claude/skills/agentic_research/`) |
| Skill audit_sources | `skills/audit_sources/SKILL.md` (cópia versionada; executável em `~/.claude/skills/audit_sources/`) |
