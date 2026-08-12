# V5.2 — Ótica Exclusivamente Econômica ("economia-only")

> Documento normativo. Vigente a partir de 2026-07-29, aplicado a partir de 2026-08-12.
> Origem: determinação de Marcel Grillo Balassiano (Subsecretário), WhatsApp "Despachos SUBDEI", 29/07/2026.
> Complementa os critérios não-negociáveis de `workflow/V5/LONG_TERM_GOALS.md` (§6).

---

## A determinação (verbatim)

Marcel, 29/07/2026 11:39, sobre o PL 2326/2026 (marca Visit Rio, entregue como contrário):

> "@Otávio O. Bopp, faz um parecer nada a opor a esse, por favor... reforça a importância do turismo e eventos e do Visiti Rio, utilizando essas fontes abaixo! Obrigado!"

Marcel, 29/07/2026 11:41, sobre os PLs 2289/2026 e 2290/2026 (tarifa de esgoto, entregues como contrários):

> "E @Otávio O. Bopp, sobre esses dois, faz parecer no sentido de nada a opor, por favor... **no sentido econômico, esquece o jurídico, se não pode pela lei tal... isso é competência dos advogados, PGM, não dos economistas!** hahahaha"

Contexto que já apontava nessa direção: divisão de trabalho de 27/05 ("@Perla... revisar a parte **econômica**... @Luiza..., colocar o **juridiquês**"); Marcel removendo referência a lei federal da conclusão do PL-1866; a versão final do PLC-118 publicada por ele só com o argumento econômico; o PL-2199 assinado por ele como nada a opor sem uma linha de jurisprudência (a versão do repo, contrária com ADI 2.733, não foi a que valeu).

## Por que a regra precisou virar estrutura

O diagnóstico de 2026-08-12 mostrou que **as 4 posições contrárias entregues (PL-2199, 2289, 2290, 2326) usavam jurisprudência como argumento decisivo** — e as três últimas foram devolvidas pelo chefe. A proibição de jurídico existia desde a V2/V3 ("sem competência constitucional; foco econômico", `README.md`), mas ficou enterrada num exemplo de prompt e nunca entrou nos docs do V5. O tópico T1 ainda se chamava "Exegese jurídica", a métrica de citações premiava citar norma (a CF/1988 chegou a contar como "citação internacional") e o gate adversarial não perguntava a natureza do argumento — no PL-2326 ele **refinou** o juridiquês (corrigiu a descrição da ADI) em vez de bloqueá-lo.

---

## A regra

### R1 — Corpo 100% econômico, pró OU contra

O corpo da manifestação sustenta a posição exclusivamente com argumentos econômicos: custo, incentivo, arrecadação, emprego, competitividade, equilíbrio tarifário, evidência empírica, experiência comparada. Vale nos dois sentidos: tanto "é inconstitucional" quanto "a competência municipal está fundada no art. 30 da CF" são argumentos jurídicos — **ambos proibidos**. (A fórmula de competência aparecia em 16 peças antigas; não editar retroativamente, mas não repetir.)

### R2 — Lista-negra dura (nunca no corpo)

STF, STJ, TJRJ/TJ-*, Supremo/Superior Tribunal, Tribunal de Justiça, ADI, ADPF, súmula, tema repetitivo, jurisprudência, (in)constitucional(idade), vício de iniciativa, iniciativa parlamentar como vício, "competência municipal/legislativa/constitucional/privativa" como fundamento, artigo da CF como fundamento.

### R3 — O que continua permitido

Citar a lei, decreto ou programa que o PL **altera, converte, espelha ou referencia** — é o objeto da análise, não argumento de validade.
- ✅ "O PL converte em lei o Decreto Rio nº 56.184/2025, já editado pelo Executivo"
- ✅ "O art. 30, III da Lei nº 11.445/2007 admite o consumo mínimo com objetivos sociais" (descrever o desenho tarifário federal É economia regulatória)
- ❌ "o decreto já exerce competência privativa do art. 84, VI, 'a', da CF"
- ❌ "o STJ firmou no Tema 565 que a cobrança é lícita"

Na dúvida: se a frase responde "**pode/não pode** pela lei?", é da PGM. Se responde "**convém/não convém** economicamente?", é nossa.

### R4 — Achados jurídicos → PGM, via V5-AUDIT

O que a pesquisa encontrar de relevante juridicamente (óbice ou respaldo) não é descartado: vai para a seção **"Achados jurídicos — roteados à PGM"** do `V5-AUDIT.md` do PL, para o revisor humano decidir se aciona a Procuradoria. Precedente: PLC-103 (vício de iniciativa omitido do corpo, "alçada da PGM — SMDE opina no eixo econômico").

### R5 — Métrica de citações recalibrada

Normas (leis, decretos, CF, resoluções) **não contam** no quota de ≥4 citações / ≥1 internacional. Contam: dados oficiais (IBGE, Riotur, Observatório do Turismo), estudos e papers, imprensa, organismos internacionais (OCDE/ILO/BID). Isso remove o incentivo que fazia a CF/1988 ser contada como citação de qualidade.

### R6 — Posições válidas

Favorável / Contrário / Nada a opor. A categoria "Sem competência" foi **eliminada** — declarar incompetência é juízo jurídico (e a SMDE sempre tem ótica econômica sobre qualquer PL).

### R7 — Contrário continua possível — só que com economia

A regra não proíbe posição contrária; proíbe sustentá-la com tribunal. "Contrário exige dano econômico aplicável demonstrado por evidência externa" (gate adversarial). Modelo: PLC-103 revisado — contrário por descompasso de instrumento + incerteza regulatória (Dixit & Pindyck, 1994), sem uma linha de jurisprudência.

---

## Gates

### Gate mecânico (novo, determinístico)

`workflow/scripts/checar_economia_only.py <manifestacao-short.md>` roda **antes de gerar o PDF**:
- **Lista dura** (R2) → exit 1, peça bloqueada.
- **Lista de aviso** (CF, Constituição, Lei Orgânica, "competência" isolada, "art. N da CF") → warn; coordenador julga se é objeto (R3) ou argumento (R1). Ex.: PELOM-5 *altera* a Lei Orgânica — objeto, passa.

### Gate adversarial (formalizado aqui — antes só existia na prática dos Lotes K/L)

Quando a posição ≠ nada a opor, três céticos independentes tentam derrubá-la:
1. **Cético de fonte** — as evidências citadas existem e dizem o que a peça diz?
2. **Cético de lógica** — o vínculo evidência→conclusão sobrevive? (non sequitur mata a posição; precedente PLC-118)
3. **Cético de jurisdição (novo na V5.2)** — *a posição sobrevive se você deletar todo argumento jurídico do raciocínio?* Se não sobrevive, a posição cai ou é reconstruída em base econômica.

### V5-AUDIT

Linha nova e bloqueante no checklist: `Corpo 100% econômico (checar_economia_only.py): ✅/❌` + seção "Achados jurídicos — roteados à PGM" quando houver.

---

## Primeira aplicação

PL 2326, PL 2289 e PL 2290 refeitos em 2026-08-12 por esta regra (ver `refeitos 29-07-2026/`).
