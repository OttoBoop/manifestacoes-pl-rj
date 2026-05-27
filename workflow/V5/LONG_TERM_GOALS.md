# Metas de Longo Prazo — Pipeline de Manifestações Técnicas (V5+)

> Documento de referência estratégica. Atualizar quando houver mudança de chefe, de estilo ou de escopo.  
> Última atualização: 2026-05-26

---

## Visão

Output indistinguível de uma manifestação técnica redigida por economista sênior (padrão Marcel + Perla): densa em citações, com embasamento acadêmico internacional e dados brasileiros, na formatação administrativa correta.

---

## Benchmarks aspiracionais

Baseados nas revisões humanas analisadas (revisões de Marcel via WhatsApp, 2026-05-15 e 2026-05-19) e nos documentos de Perla (Manifestação PL Catadores, Transporte Lagunar, etc.).

| Métrica | V3 real (auditado) | Padrão humano (Marcel) | Padrão Perla (acadêmico) | **Meta V5** |
|---------|-------------------|----------------------|--------------------------|------------|
| Citações no short (~330 palavras) | 1–4 | 2–4 | 3–5 | **≥ 4** |
| Citações no full (~700–900 palavras) | 3–6 | 5–8 | 6–10 | **≥ 8** |
| Fontes internacionais por manifestação | 0 | 0–1 | 3–5 | **≥ 1** |
| Fontes brasileiras por manifestação | 1–4 | 3–6 | 2–4 | **≥ 3** |
| NB dedicado por PL | 36% (4/11) | N/A | N/A | **100%** |
| Fontes adicionadas ao NB por PL | ~1 | N/A | N/A | **≥ 6** |
| Carry-through inventário → texto | 37% | ~100% | ~100% | **≥ 80%** |
| audit_sources aplicado | 9% (1/11) | N/A | N/A | **100%** |
| Posição alinhada com SMDE | 89% (8/9) | 100% | 100% | **100%** |

---

## Critérios de qualidade não-negociáveis (V5)

### 1. Citação mista obrigatória
Toda manifestação deve ter ≥ 1 fonte acadêmica ou de policy internacional, mesmo que breve. Exemplos aceitáveis:
- "conforme documenta Prassl (2018) sobre trabalho em plataformas digitais"
- "Ostrom (1990) sobre governança comunitária de recursos comuns"
- "OCDE (2023) — *Gig Economy and Social Protection*"

Um único "conforme a ILO (2024)" já cumpre o requisito.

### 2. Nenhum dado solto sem fonte
Qualquer número, percentual, ranking ou estatística deve ter `(INSTITUIÇÃO, ANO)` imediatamente após. Sem isso, o dado é removido ou o pesquisador é rejeitado.

### 3. Posição default "nada a opor"
A SMDE raramente posiciona-se formalmente contra um PL. Regra:
- Default: "nada a opor" — sem ressalvas no corpo do texto (Marcel remove sistematicamente toda seção de ressalvas)
- "Contrário" só com ≥ 3 argumentos econômicos independentes **E** consulta ao usuário antes de finalizar

### 4. Inventário → texto (carry-through ≥ 80%)
Se o pesquisador listou 5 fontes no F-T.N, no mínimo 4 devem aparecer citadas no texto. Listar fontes no inventário sem usá-las é sintoma de pesquisa desconectada da síntese.

### 5. audit_sources obrigatório
Nenhuma manifestação é marcada como concluída sem Wave 1 + Wave 2 de audit_sources aplicadas. A verificação de citações é parte estrutural, não opcional.

---

## Tipos de fonte por tier

Para guiar o pesquisador na composição do mix:

| Tier | Tipo | Exemplos brasileiros | Exemplos internacionais |
|------|------|---------------------|------------------------|
| T1 — Legal/Regulatório | Leis, resoluções, complementares | LC 116/2003, Resolução CVM 178/2023, CDC (Lei 8.078/1990) | Diretiva UE 2022/2041 (plataformas), OCDE Guidelines |
| T2 — Dados institucionais | Órgãos oficiais, institutos | IBGE, CEBRAP, FGV, ANCORD, ABRASEL, PROCON | ILO, OECD, World Bank, BID, Eurostat |
| T3 — Acadêmico | Artigos, livros, policy papers | IPEA, FGV CPDOC, Insper | Prassl (2018), Ostrom (1990), De Soto (1989) |
| T4 — Comparativo | Experiências em outros lugares | PROCON-SC, prefeituras SP/BH | Preston Model (UK), Shannon Airport (IRE) |

Uma boa manifestação usa ≥ 1 de cada tier — especialmente T2 + T3.

---

## Evolução planejada além de V5

| Versão | Melhoria principal | Motivação |
|--------|-------------------|-----------|
| **V6** | Integração com legislação municipal (CTM, IOERJ) — busca automática de leis correlatas | Hoje o pesquisador acha as leis por WebSearch; poderiam ser injetadas em P0 |
| **V7** | Prompts especializados por setor (fintech, food service, gig economy, saúde pública, urbanismo) | Cada setor tem suas fontes de referência e arcabouço teórico específico |
| **V8** | Banco de preferências de Marcel — aprendizado acumulado de revisões anteriores injetado nos prompts | Evita repetir os mesmos erros (ex: PL-1934 contrário → nada a opor) |
| **V9** | Pipeline multimodal — PLs que incluem mapas, tabelas de impacto fiscal, gráficos como fontes | Alguns PLs vêm com anexos técnicos que hoje são ignorados |

---

## O que aprendemos com V1–V4

| Versão | Inovação | Limitação descoberta |
|--------|----------|---------------------|
| V1 | Prova de conceito: NotebookLM + agentic_research + audit | Longa demais (1.500+ palavras); citação muito acadêmica para o tom da SMDE |
| V2 | Foco econômico; estilo mais conciso | Ainda sem padrão formal de abertura/fechamento; prompts em PT-only |
| V3 | Short (330w) + PDF 1 página; fórmula de abertura/fechamento; 4 tópicos padronizados | NB não populado para 9/11 PLs; agentes paralelos crasharam; audit nunca aplicado |
| V4 | Adversarial (PRÓ + CONTRA + Síntese) | Reduziu citações (de 1.9 para 0.8 por manifestação); custo 2× sem benefício de posição |
| **V5** | Corrige falhas de execução de V3 sem mudar estrutura | A definir após primeira aplicação real |
