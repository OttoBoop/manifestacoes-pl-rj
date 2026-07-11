---
name: audit_sources
description: Auditoria rigorosa de fontes de um texto longo (estudo, artigo, relatório) já escrito. Extrai sistematicamente cada citação, verifica contra fonte primária com trecho literal, e entrega relatório para decisão humana. Usa múltiplos agentes verificadores em paralelo. NUNCA corta texto por conta própria — só o usuário decide.
---

# Audit Sources

> **Status:** esqueleto inicial (em construção). Skill sendo refinada durante o primeiro case real de uso. Conteúdo será atualizado a cada Wave do case para capturar aprendizados.

## Quando usar

Dispare esta skill quando o usuário pedir, sobre um texto longo já escrito:
- "auditar as fontes", "verificar as fontes", "revisar as referências"
- "checar se as citações estão corretas"
- "conferir cada afirmação contra a fonte"
- Equivalentes: confirmar, validar, auditar rigorosamente

**Não use** para:
- Apenas listar as referências (escopo mais amplo que isso)
- Escrever texto novo
- Corrigir texto (a skill só audita; decisão de corrigir é do usuário)

## Princípios duros

1. **Buscar é obrigação do verificador; cortar é decisão humana.**
2. **"Confirmado" exige trecho que substancia a afirmação** + localização (URL + âncora, PDF + página, ou livro + capítulo). Citação literal é desejável, mas paráfrase também confirma desde que a informação esteja na fonte.
3. **NotebookLM-first é não-negociável — porque o NB é a BASE DE CONHECIMENTO do projeto, não uma "fonte alternativa".**

   **Por que NB-first é estrutural (não convenção):**
   - **Razão maior:** o NotebookLM é onde o conhecimento do projeto VIVE. A skill `agentic_research` instrui o pesquisador a (a) começar suas buscas no NB, (b) salvar fontes encontradas no NB durante a pesquisa, (c) usar funções de "pesquisa rápida" e "pesquisa profunda" do NB que adicionam fontes automaticamente. **Se tudo funcionou bem na fase de pesquisa, TODAS as evidências do texto auditado já estão no NB.** Por isso, ao auditar, começar pelo NB não é otimização — é começar pela base correta. O pesquisador pode ter falhado em adicionar tudo, mas a hipótese de trabalho é: a fonte está lá.
   - **Razão menor:** NB é otimizado para varredura de grandes textos e bases curadas. Verificador (agente LLM) não é. Usar NB economiza tokens e reduz alucinação por document-grounded retrieval.

   **Constraint dura:** o verificador NÃO pula NB com base em "essa fonte é governamental, não acadêmica" ou "esse tema não é o foco do notebook" ou qualquer palpite sobre conteúdo. Esses palpites são, em todo caso, falsos pela razão maior acima — se o autor do artigo usou a fonte, o pesquisador deveria ter colocado no NB. Pular NB com essa justificativa é falha **gravíssima** porque ignora a arquitetura da pipeline `agentic_research → audit_sources`.

   **Falhas históricas que motivaram esta regra (case Compstat 2026-04):**
   - Wave 2: 5 verificadores rodaram com ZERO chamadas ao NotebookLM, apesar de o notebook conter Cardoso 2024, PERF reports e papers centrais.
   - Wave 2-bis: coordenador (eu mesmo, depois de já ter codificado a regra NB-first) pulou NB para F-3.12 Cano, F-5.2 SSP-RS e F-4.9 celular, com a justificativa: *"esses são dados governamentais, não acadêmicos centrais; provavelmente o notebook (focado em Police Performance Management) não tem essas fontes — vou economizar tempo e ir direto na web"*. **Esse raciocínio é estruturalmente errado:** o NB é a base do projeto inteiro, não um arquivo acadêmico de tema restrito. Inventário posterior do NB confirmou que ele tem ISP, FRIPERJ, FBSP, releases Prefeitura, Igarapé etc — exatamente o tipo de fonte que o coordenador "achou que não estaria lá".
4. **Esgotar busca antes de desistir.** Mínimo: 3+ queries no NotebookLM + 2 métodos distintos para PDF primário (curl+pdftotext, WebFetch, mirror IA) + 5+ queries web variando termos. Tudo documentado no histórico de busca do output.
5. **"Não achei" não é resposta.** Antes de marcar ❓ INVERIFICÁVEL: esgotamento documentado conforme regra 4. Output sem histórico de busca expandido é rejeitado pelo coordenador.
5a. **NUNCA declarar inexistência de uma fonte.** É proibido escrever "esse artigo não existe" ou "essa fonte é alucinação". O verificador escreve, no máximo: *"Falhei em localizar esta fonte. Documentei o protocolo abaixo. O usuário decide se a busca foi suficiente."* Inexistência é conclusão do usuário, não do verificador.

   **Protocolo OBRIGATÓRIO antes de afirmar "não localizei":**

   1. **Inventário REAL do NotebookLM (não via query!):** o `ask_question.py` usa RAG retrieval — quando você pergunta "liste fontes", o NB retorna apenas o top-N relevante para "liste fontes" (vago), nunca a lista exhaustive. **Falha histórica no case Compstat 2026-04:** notebook tinha 183 fontes; minha query de inventário retornou ~50 (~27%). Toda negativa do NB sobre fontes não-retornadas era FALSO NEGATIVO.

      **Solução implementada (case Compstat 2026-04):** existe agora `~/.claude/skills/notebooklm/scripts/list_sources.py` que abre o notebook autenticado (Playwright headless), lê o painel `<source-picker>` direto do DOM e retorna a lista exaustiva via `aria-label` dos checkboxes individuais (cada `mat-checkbox.select-checkbox input` tem o título completo da fonte). Comando:

      ```bash
      cd ~/.claude/skills/notebooklm && python scripts/run.py list_sources.py \
          --notebook-url "<URL>" --out /tmp/nb_inventario_real.json
      ```

      O JSON é uma lista plana de strings (títulos das fontes). Validado: para o notebook do case (~183 fontes) retornou 183 entradas. Use ANTES de qualquer auditoria envolvendo NB.
   2. **Query específica ao NB:** "Existe nas suas fontes o artigo X de autor Y, ano Z, periódico W?". Documentar resposta literal. **Atenção: NB negativo aqui significa "não retornado no top-N do retrieval", não "não existe na biblioteca".**
   3. **Query de conceito ao NB:** "Há nas suas fontes algum trabalho que discute [conceito central do artigo procurado]?" — pede ao NB para varrer por tema, não por título. Documentar resposta literal.
   4. **Instigar o NB com múltiplas reformulações:** se 2 e 3 vierem negativos, refazer com sinônimos / variações de título / autor diferente / co-autores / palavras-chave técnicas / nome do journal. Mínimo 3 reformulações distintas. Cada reformulação muda o RAG retrieval — uma pode trazer fonte que outra não trouxe. Documentar todas.
   5. **Triangulação NB ↔ inventário UI:** verificar se a fonte buscada está na lista do usuário. Se está mas NB diz que não tem, é falso negativo confirmado — significa que o conteúdo da fonte não bate com a query (precisa reformular). Se NÃO está na lista UI, então de fato não está no notebook (NB negativo = real).
   6. **Só após 1-5 documentados:** sair do NB e ir para web (Google Scholar, Semantic Scholar, ResearchGate, repositório institucional, DOI lookup).
   7. **Web também documentado:** queries + top hits + tentativas de PDF. Mínimo 5 queries web variando termos.
   8. **Reportar ao usuário:** "Após [protocolo], não localizei. **Você decide:** (a) fonte realmente não existe; (b) existe mas em fonte que minha busca não cobriu; (c) erro de transcrição (autor/ano/título trocado) — me dá pista pra refazer."

   Falhas históricas que motivaram esta regra (case Compstat 2026-04):
   - F-3.1 (Eterno 2020 "Compstat Lite") declarado "não existe" após 1 query NB + 1 web search. Inexistência é conclusão do usuário, não do verificador.
   - Inventário via query retornou ~50 fontes; UI mostrava 183. ~73% das fontes invisíveis. **NotebookLM via API atual NÃO pode ser usado como inventário — usar UI do humano.**
6. **Surveys fantasma são proibidos.** Toda menção a "pesquisa aponta", "surveys mostram", "estudos sugerem" exige autor + ano + título identificáveis. Sem isso, a sentença é removida ou marcada como inverificável. Regra ancorada em fala do usuário no case Compstat: *"OFENDIDO em ter lido a opção [sem fonte], nem me sugira algo tão absurdo como citar uma pesquisa sem fonte"*.
7. **Adjetivos descritivos sem fonte são removidos.** "Pichado de ponta a ponta", "considerado pequeno por especialistas", "icônico" etc. — toda qualificação descritiva precisa fonte ou sai. Regra ancorada em fala do usuário: *"Quem disse que o trecho estava pichado? Quem???"*.
8. **Aspas literais exigem trecho literal localizado.** Se o verificador não localiza a frase exata, ele NÃO confirma — marca como paráfrase e sugere remoção das aspas. Confirmar uma aspa sem ter o trecho literal é fabricação.
9. **Decisões sobre o texto vêm do usuário**, nunca do coordenador unilateralmente.
10. **Coordenador relata em tempo real ao humano e isso implica três coisas simultâneas:**
    - **(a) Monitora o agente ativo.** Se há background rodando, abrir `Monitor` filtrando eventos relevantes (sucesso, falha, timeout, evidências chegando). Não esperar notificação automática.
    - **(b) Trabalha em paralelo.** Enquanto o background processa, o coordenador investiga próximos itens via web/PDF/leitura. Ficar ocioso é apenas o sintoma do erro maior: ter ignorado (a).
    - **(c) Verbaliza ao humano** — cada nova evidência, cada falha, cada decisão de mudar de tática vira um update curto à conversa. O ato de narrar é parte do controle de qualidade: força o coordenador a notar inconsistências e permite ao humano intervir antes de erros se acumularem.

    Regras ancoradas em duas falas do usuário no case Compstat 2026-04:
    - *"só de falar para o humano o que está acontecendo, o orquestrador já pode perceber alguns erros por parte dos agentes"*
    - *"COMO ASSIM VC TÁ ESPERANDO UM AGENTE TERMINAR O TRABALHO NO BACKGROUND. Você é o orquestrador. Suas instruções já dizem que vc tem que monitorar os agentes e me atualizar em tempo real"*

10b. **Quando o humano aponta um novo problema, NÃO interromper a narrativa do background.** Padrão errado observado no case Compstat 2026-04: humano apontou erro X, coordenador "limpou a mesa" matando background Y sem (a) reportar último status de Y, (b) consultar humano se Y deveria continuar. Coordenador correto SOMA: *"Você apontou X, vou tratar — e o background Y continua processando, último status é Z, vou seguir narrando os dois."* Matar background unilateralmente porque a conversa mudou de tópico é falha grave: descarta trabalho potencialmente útil e silencia o humano sobre o que foi descartado. **Antes de qualquer `TaskStop`**, reportar status atual + perguntar ao humano se deve seguir ou parar.

10c. **Orquestrador NUNCA aguarda. Ponto.**

   "Aguardando" é falha sempre que aparece. A função de orquestrador é monitorar agentes ativos, trabalhar em paralelo nos próximos itens, e reportar continuamente ao humano. Quem monitora não aguarda — observa em tempo real e age. Aguardar passivamente até "a tarefa estar concluída" é incompatível com o papel. Se o orquestrador escreve "aguardando", o erro já aconteceu: ou ele matou prematuramente o trabalho que poderia continuar (ver 10b), ou desistiu de caminhos técnicos óbvios (raspar DOM, ler código, propor patch, escrever script novo), ou silenciou-se quando deveria estar relatando.

   Regra prática: a palavra "aguardando" no output do coordenador é tratada como bandeira vermelha — sinal de que ele está em modo errado e precisa identificar imediatamente (a) o que está rodando que ele deveria estar narrando, (b) o que ele deveria estar fazendo em paralelo, (c) qual caminho técnico não tentou.

   **Quando o orquestrador pode descansar (única condição legítima):**
   - **Todos os agentes concluíram E** o coordenador entregou um bom relatório ao humano **E** não há mais nada a fazer além de esperar o feedback humano.
   - "Bom relatório" significa: cobre tudo que foi pedido, com contexto literal, opções concretas, e está pronto para o humano decidir sem ambiguidade.
   - Mesmo assim, se a janela de espera for longa, usar o tempo para preparar fases futuras (esqueleto Wave 4, refinar achados parciais, atualizar skills) é melhor que ficar parado — mas NÃO é obrigatório, porque o relatório já está completo.

   **Humano com capacidade física exclusiva** (ex: clicar botão em UI sem API alguma) — antes de pedir, esgotar todas as alternativas técnicas e reportar quais foram tentadas.

   Falha histórica adicional do case Compstat 2026-04 (Wave 3): coordenador entregou consolidado de 50 itens, humano levou ~1 hora escrevendo decisões. Coordenador ficou em modo "aguardando" o tempo todo, sem usar a janela para preparar Wave 4, refinar achados parciais, melhorar registros, ou rodar verificações adicionais. Resultado: hora desperdiçada que poderia ter adiantado o trabalho posterior.

   Falha histórica que motivou esta regra (case Compstat 2026-04): descobri limite RAG do NB → entrei em "aguardando inventário via UI" → usuário corrigiu apontando que existiam caminhos técnicos (raspar DOM Playwright, ler scripts existentes, escrever script novo). Eu tinha endurecido a regra com "aguardando só legítimo quando...", mas o usuário corrigiu de novo: a hedge cria brecha. **Resposta: cortar a hedge. Orquestrador não aguarda.**
11. **Decisões do usuário ficam no `auditoria_fontes.md`**, não em arquivo lateral. Cada decisão é versionada junto com o artigo, com fala literal preservada quando ancora regra geral.
12. **Lições técnicas ficam na skill assim que descobertas.** Se a Wave N descobre como extrair um tipo de PDF, o método entra na skill antes da Wave N+1. Skill é viva — não é manual congelado.

## Distinção fundamental: citação literal vs. paráfrase

- **Citação literal entre aspas no texto auditado** → verificador precisa achar a frase exata (ou marcar como paráfrase e sugerir remoção das aspas).
- **Paráfrase atribuída a autor** ("Cano faz um diagnóstico de...", "Bratton argumenta que...") → verificador checa se a **informação/tese** está na obra do autor. Não precisa achar formulação exata.

O que é inaceitável é **afirmar sem fonte** ou **inventar atribuição** (ex: citar Harcourt & Ludwig 2006 para afirmação que não consta do paper deles). Isso é erro factual grave.

## Arquitetura em 4 fases

```
Fase 0 — Preparação
  Criar esqueleto de auditoria_fontes.md junto ao texto auditado.

Fase 1 — Extração (agente extrator + revisão coordenador)
  Agente lê o texto inteiro, identifica toda citação (autor-data, nota,
  referência), mapeia cada uma à(s) afirmação(ões) que sustenta, produz
  rascunho do auditoria_fontes.md com status ⏳. Coordenador revisa antes
  da Fase 2.

Fase 2 — Verificação paralela (múltiplos agentes por bloco)
  Texto é dividido em blocos (por seção). Um agente verificador por bloco,
  todos em paralelo. Cada um:
    - recebe o recorte do auditoria_fontes.md que lhe cabe
    - para cada fonte: executa busca rigorosa (≥3 queries + PDF + secundária)
    - preenche o recorte com ✅ / ⚠️ / ❓ + trecho literal (para ✅) ou
      histórico de busca (para ❓)
  Monitor ativo para reporte em tempo real ao usuário.

Fase 3 — Consolidação + decisões humanas
  Coordenador consolida os outputs, apresenta resumo ao usuário, e pede
  decisão caso a caso para toda fonte ⚠️ ou ❓. Coordenador NUNCA decide
  sozinho.

Fase 4 — Aplicação + commits granulares
  Coordenador aplica as decisões no texto. Commits por bloco ou por seção,
  referenciando as linhas do auditoria_fontes.md que justificam a mudança.
```

## Fluxo de execução (resumido)

1. **Coordenador** cria `auditoria_fontes.md` junto ao texto auditado
2. **Agente extrator** preenche a lista de citações → coordenador revisa
3. **N agentes verificadores** em paralelo, um por bloco de seções
4. **Monitor** streamando tool_use de cada verificador → coordenador repassa ao usuário
5. **Consolidação + perguntas ao usuário** sobre PARCIAIS e INVERIFICÁVEIS
6. **Coordenador aplica** decisões no texto com commits granulares

## Templates

- `templates/extractor_prompt.md` — prompt do agente extrator _(a ser finalizado na Wave 1)_
- `templates/verifier_prompt.md` — prompt do agente verificador _(a ser finalizado na Wave 2)_

## Formato do `auditoria_fontes.md`

_(Será refinado após a Wave 1 com o formato que o extrator produzir e que o coordenador validar.)_

Seções-padrão:
- Metodologia (regras duras)
- Resumo executivo (contagem)
- Por seção do texto auditado
- Decisões humanas (tabela)
- Log de execução

## Aprendizados acumulados

_(Esta seção é atualizada ao longo do case.)_

### Pós Wave 1 (extração)
- Extrator de 1 agente único funciona bem — não precisa paralelizar esta fase
- 93 blocos em artigo de ~12k palavras foram catalogados em ~8 minutos
- **Pedir explicitamente "FONTE IMPLÍCITA" no prompt** — afirmações factuais sem citação explícita também precisam ser catalogadas
- **Pedir "achados editoriais"** no retorno — erros de numeração, referências órfãs, inconsistências de ano foram descobertos assim
- Para fontes que aparecem em múltiplas seções, usar **um bloco por ocorrência** (não um bloco único) — cada ocorrência pode estar ancorada num trecho diferente, e cada trecho precisa ser verificado separadamente

### Pós Wave 2 (verificação paralela)
- **5 verificadores por bloco, em paralelo, funciona bem.** ~10-12 minutos por bloco. Usar um Monitor filtrando `WebSearch`/`WebFetch`/`Write` para acompanhar em tempo real.
- **Passar NotebookLM URL e instrução explícita** no prompt. Sem isso, agentes ignoram o NotebookLM mesmo quando disponível — foi o que aconteceu no primeiro caso. Preferir NotebookLM a WebSearch para fontes acadêmicas curadas. Templates `templates/verifier_prompt.md` já trazem essa instrução pronta.
- **Separar o bloco em arquivo próprio** (`/tmp/.../bloco_X_input.md` e `/tmp/.../bloco_X_output.md`) — evita colisão de escrita entre verificadores paralelos.
- **Out-of-credit nos últimos minutos é comum** — o agente pode ter escrito o output completo antes de cair; sempre checar o arquivo de output direto, não só o `<result>` da notificação.
- **Alertar o verificador sobre fontes mais frágeis** no próprio prompt (ex.: "essa citação literal provavelmente não tem fonte pública — aceite paráfrase se a tese estiver no autor"). Reduz tempo gasto em busca inútil.
- **Achados recorrentes neste caso:** (a) atribuições erradas de autor-data (Harcourt & Ludwig 2006 ligado a afirmação que não está no paper); (b) citações literais entre aspas quando o que existe é paráfrase; (c) números/datas levemente deslocados ("2023" quando era 2024; "R$ 8 bi" quando era CNC e R$ 10-12 bi); (d) referências bibliográficas com autor errado ou título incompleto (Cabral 2024). Monitorar esses padrões.

### Pós Wave 3 (revisão crítica do consolidado pelo usuário)

**Falhas sistêmicas detectadas** que motivaram regras 3-12 acima:

1. **NotebookLM ignorado.** Os 5 verificadores fizeram **zero chamadas** ao notebook curado, apesar de ele conter Cardoso 2024 e papers acadêmicos centrais do case. Causa raiz: prompt do verificador era improvisado pelo coordenador, não tinha NotebookLM-first explícito. Solução: template `verifier_prompt.md` formal com URL do notebook injetada e ordem obrigatória de busca (NB → PDF → web).
2. **Travamento em PDFs.** Verificadores paravam ao receber binário do WebFetch (PDF Igarapé escaneado, PNV 2013 >10MB, FBSP 2024). Causa raiz: nenhuma alternativa de extração registrada na skill. Solução: appendix técnico (ver abaixo) com receitas testadas.
3. **Atribuição inventada.** "Sundström 2017, Crime Law and Social Change" não existe nesse periódico/ano (paper real é 2015, Global Environmental Change, sobre fiscalização pesqueira). Verificador identificou a discrepância mas só após esgotar buscas web. NotebookLM-first poderia ter resolvido em 1 query.
4. **Atribuição trocada.** Harcourt & Ludwig (2006) usado para sustentar tese sobre turismo que não está no paper deles (paper é sobre disorder-crime e Moving to Opportunity).
5. **Erros de ano em pesquisas de opinião.** Datafolha 2023 → na verdade 2024; Quaest 2024 → na verdade 2025. Padrão: pesquisas de opinião têm data específica de campo + data de publicação; verificador deve checar ambas.
6. **Categorias estatísticas brasileiras confundidas.** "Homicídios dolosos" ≠ "letalidade violenta" ≠ "mortes violentas" no glossário do ISP-RJ. Verificador deve sempre exigir definição operacional da métrica antes de confirmar número.
7. **Surveys fantasma na proposta de correção.** Coordenador (eu) chegou a sugerir ao usuário substituir Harcourt & Ludwig por "surveys da NYC & Company ou do Longwoods International" — isso é o anti-padrão clássico de citar pesquisa que ninguém localizou. Resposta do usuário: rejeição absoluta. Daí regra 6.
8. **Adjetivos sem fonte na proposta de reescrita.** Coordenador sugeriu manter "metrô pichado de ponta a ponta" sem questionar a fonte do adjetivo. Usuário: *"Quem disse que estava pichado? Quem???"*. Daí regra 7.
9. **Coordenador comprimindo demais o consolidado.** Wave 3 inicial listou ~8 itens problemáticos numa lista enxuta — quando a Wave 2 tinha encontrado ~52. Padrão de "treinamento de IA para resposta de tamanho médio" identificado e corrigido pelo usuário. Em revisão geral (checkpoint), prolixidade é esperada e desejada; em fluxo de trabalho, brevidade. Daí regra 10.
10. **Decisões do usuário sumindo.** Coordenador apresentou análise sem registrar para onde vai a decisão dele. Usuário pediu registro permanente no `auditoria_fontes.md`. Daí regra 11.

### Appendix técnico — Extração de PDFs

_(Receitas testadas em 2026-04-15 contra PDFs que travaram a Wave 2 do case Compstat. Atualizar conforme novos métodos forem validados.)_

- **PDF de texto puro acessível por URL pública (✅ TESTADO E FUNCIONA):**
  ```bash
  curl -sLo /tmp/file.pdf "URL" && pdftotext /tmp/file.pdf - | head -300
  ```
  Funciona para a maioria dos PDFs governamentais, relatórios institucionais e dissertações.

  **Casos validados:**
  - Cardoso 2024 (UFPE, 1.2MB): extração limpa, página 1 a fim, com referências bibliográficas
  - Igarapé "Pacto pela Vida" 2014 (271KB): V-B disse "binário ilegível com metadados de câmera Canon" — **na verdade extraiu perfeitamente**, inclusive descobriu que os autores reais são José Luiz Ratton, Clarissa Galvão e Michelle Fernandez (não apenas "Instituto Igarapé" como o artigo cita)
  - FBSP "Anuário Segurança em Números 2024" (798KB): V-D disse "binário não parseável" — **extraiu com infografia inclusa**

  **Lição:** "PDF binário" via WebFetch geralmente significa "WebFetch decidiu não parsear", não "PDF não-parseável". Sempre tentar `curl + pdftotext` antes de marcar inverificável. Foi a falha que custou mais tempo na Wave 2 do case Compstat.

- **PDF escaneado (sem camada de texto):**
  ```bash
  curl -sLo /tmp/file.pdf "URL" && ocrmypdf /tmp/file.pdf /tmp/file_ocr.pdf && pdftotext /tmp/file_ocr.pdf -
  ```
  Requer `ocrmypdf` instalado (Arch: `pacman -S ocrmypdf tesseract-data-por`; Debian: `apt install ocrmypdf tesseract-ocr-por`). Lento mas resolve PDFs de câmera. **Status local (2026-04-15): NÃO instalado** — instalar antes de Wave 2-bis se algum PDF realmente exigir OCR (não é o caso da maioria — `pdftotext` puro resolveu tudo testado até agora).

- **PDF muito grande (>10MB) que estoura WebFetch:**
  ```bash
  curl -L "URL" -o /tmp/file.pdf && pdftotext -f START -l END /tmp/file.pdf -
  ```
  Extrai só páginas START a END. Útil para ir direto à seção de interesse (ex: PNV 2013, capítulo de notificação de roubo).

- **PDF atrás de paywall ou bloqueio anti-bot:**
  Tentar (em ordem): (a) versão mirror no Internet Archive (`https://web.archive.org/web/*/URL`); (b) repositório institucional (UFPE, IPEA, SciELO); (c) Sci-Hub se for paper acadêmico; (d) Google Scholar para PDF cache. Nunca aceitar paywall como motivo de marcar inverificável sem ter tentado as 4 opções.

- **PDF cuja URL retorna binário no WebFetch mas é parseável localmente:**
  WebFetch tem heurística que rejeita binário. Solução: usar `Bash + curl + pdftotext` (combo acima) — o ferramental do shell processa o que o WebFetch rejeita.

## Exemplo de uso

Primeiro case real: auditoria do estudo "Compstat Integral vs. Compstat Lite" para o Gabinete do Vereador Flávio Valle (RJ). Ver `flaviovalle-estudos/compstat/auditoria_fontes.md` quando concluído.

## Anti-padrões (lições do primeiro case)

**Não faça o que o coordenador fez errado na primeira tentativa:**

1. **Não corte informação apenas porque a busca inicial não achou a fonte exata.** Se uma afirmação é materialmente verdadeira, existe fonte para ela — o que falta é procurar melhor. Só considerar inverificável após esgotamento de busca.
2. **Não trate auditoria como exercício de exclusão.** Auditoria é para **encontrar evidência**, não para **remover o que é frágil por conveniência**.
3. **Não decida por conta própria.** Mesmo quando uma fonte parece claramente ruim, a decisão de cortar, reformular ou manter é do usuário. Coordenador apresenta; não executa.
4. **Não fique mudo durante a execução.** Reporte a cada entrega de verificador; o usuário precisa ver o processo para poder interromper se algo sair errado.
