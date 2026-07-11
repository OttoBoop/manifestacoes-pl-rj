# Template: Prompt do Agente Extrator (Wave 1)

Use este prompt para lançar o agente que varre o texto a auditar e cataloga cada citação no arquivo `auditoria_fontes.md`.

Substitua `{{...}}` pelo caso concreto.

---

```
AGENTE EXTRATOR — Wave 1 da auditoria de fontes de {{nome do estudo/artigo}}.

## Sua missão
Ler o texto completo em `{{caminho do artigo}}`, identificar **cada citação** (autor-data inline, nota sobrescrita, e itens da seção Referências), mapear cada uma à(s) afirmação(ões) do texto que ela sustenta, e preencher o arquivo `{{caminho do auditoria_fontes.md}}` (já existe como esqueleto).

## Importante
- **Você NÃO está verificando** se a fonte substancia a afirmação — isso é trabalho da Wave 2.
- **Você está mapeando**: para cada fonte citada, qual(is) afirmação(ões) do texto dependem dela.
- **Todo status fica ⏳ "a verificar".** Não preencha verificação.
- **Não reescreva o texto. Não edite o texto.** Só edite o `auditoria_fontes.md`.

## Leia antes
1. `{{caminho do artigo}}` — o texto a auditar
2. `{{caminho do auditoria_fontes.md}}` — o esqueleto do seu output
3. `~/.claude/skills/audit_sources/SKILL.md` — para entender o espírito da auditoria

## Formato de cada item no auditoria_fontes.md

Preencha a seção de cada §X.Y do texto com **um bloco por fonte**, neste formato:

```markdown
#### F-1.1 — {{autor/título curto e ano}}
- **Tipo:** {{acadêmico / reportagem / dados oficiais / panfleto / entrevista / etc.}}
- **Substancia (§X.Y, parágrafo N):** "{{trecho literal do texto que depende da fonte}}"
- **Nota do artigo:** {{número da nota sobrescrita ou "inline"}}
- **Status:** ⏳ a verificar
- **URL/ref candidata:** {{se o texto indica URL; senão, fonte provável}}
```

## Regras de numeração

- Use `F-<seção>.<N>` como ID. Ex: F-1.1, F-1.2, F-2.1, F-3.3, etc.
- Numere sequencialmente dentro de cada seção.
- Se a mesma fonte aparece em múltiplas seções, crie **um bloco por seção** referenciando a mesma fonte. Na Wave 2, cada ocorrência será checada contra o trecho específico que ela substancia ali.

## Cobertura obrigatória

1. **Cada nota sobrescrita** no corpo do texto
2. **Cada citação autor-data inline** ("Bratton, 1998", etc.)
3. **Cada item da seção "Referências"** — cada um vira um bloco, indicando onde ele aparece no corpo do texto
4. **Afirmações factuais sem citação explícita** que dependem claramente de fonte — marcar como "FONTE IMPLÍCITA" e sugerir a fonte provável. Ex: "Em 1990, Nova York registrou 2.245 homicídios" → fonte implícita: NYPD Historical Crime Data.
5. **Todo número específico** — mesmo se o parágrafo já tem nota com fonte agregada, cada número específico (ex: "2,13 milhões", "32%", "70% dos cariocas", "R$ 3,3 bilhões") é uma afirmação verificável separada. Crie bloco F-X.Y para cada um, mesmo que apontem para a mesma fonte. Razão: na Wave 2 cada número será cotejado individualmente — um pode bater e o outro não. Falha histórica no case Compstat: "2,13 milhões de turistas" e "32% do total Brasil" iam num único bloco F-1.6 — ambos estavam errados (1,19M e 20% reais), o desencontro só apareceu na verificação porque o extrator separou o suficiente.
6. **Toda qualificação descritiva** ("considerado pequeno por especialistas", "cidade pichada de ponta a ponta", "icônico") — adjetivos descritivos que sugerem fato verificável. Marcar como "FONTE IMPLÍCITA — adjetivo descritivo" e sugerir buscar fonte. Razão: Wave 3 do case Compstat detectou múltiplos adjetivos sem fonte que o usuário rejeitou (*"Quem disse que estava pichado? Quem???"*).

## Formato de saída

Entregue o arquivo `auditoria_fontes.md` preenchido. Preserve a estrutura do esqueleto existente (cabeçalho, metodologia, resumo executivo vazio, por seção, decisões humanas, log). Preencha **só as seções "### §X"**.

## Ferramentas permitidas
- Read (do texto e do esqueleto)
- Edit/Write (apenas no `auditoria_fontes.md`)

## Ao final
Retorne breve relatório:
- Total de fontes catalogadas por seção
- Fontes de maior ocorrência (aparecem várias vezes)
- Fontes "implícitas" que identificou
- Achados editoriais (erros tipográficos de numeração, inconsistências de ano, referências órfãs — listadas sem citação no corpo)

Não edite nenhum outro arquivo.
```

---

## Lições do primeiro case (Compstat Integral vs. Compstat Lite)

- Extrator identificou 93 blocos em ~8 minutos para artigo de ~12k palavras
- Seções mais densas: §3 (26 fontes) e §2 (18 fontes)
- Sinalização de "FONTE IMPLÍCITA" funcionou bem — permitiu ao coordenador identificar 13 afirmações factuais que deveriam ter citação
- Achado editorial importante do extrator: notas numeradas fora de ordem e referências órfãs — vale pedir esse check explicitamente
