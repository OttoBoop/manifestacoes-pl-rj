# Índice de Avaliações de Políticas (Manifestações Técnicas SMDE)

> Tabela mestre de todas as manifestações já produzidas pela pipeline.
> Fonte canônica de detalhe por PL: `workflow/PROOF-OF-CONCEPT.md` (inventário de PDFs) + `<PASTA>/V5-AUDIT.md`.
> **Atualizado:** 2026-06-15 — **33 manifestações entregues** + 1 bloqueada.

---

## Fluxo de avaliação (resumo)

```
PDF do despacho (Ofício CVL/SGV ou Despacho de Ciência)
   │
   ├─ [P0] Bash — cria pasta PL-XXXX-YYYY/ + extrai texto
   ├─ [P1] skill notebooklm — cria NB, faz upload do PDF (OCR Gemini),
   │        adiciona ≥6 fontes (≥2 EN), pesquisa profunda, list_sources
   ├─ [P2] skill agentic_research — 4 duplas P+E paralelas (NB-first),
   │        citações formais (SOBRENOME. "Título", Veículo, Ano)
   ├─ [P3] skill audit_sources — verificação NB-first das citações,
   │        decisões conservadoras aplicadas
   ├─ escreve manifestacao-short.md (250–370 palavras, ≥4 citações, ≥1 EN,
   │        formato "nada a opor" / "ciência da lei")
   ├─ gera PDF (gerar_pdf_manifestacao.py — Times 12, 1.5, A4, 1 página)
   └─ [P4] V5-AUDIT.md + .gitignore + commit + push + copia p/ entregáveis
```

**3 skills encadeadas:** `notebooklm` (base de conhecimento) → `agentic_research` (pesquisa+escrita) → `audit_sources` (verificação).

---

## Tabela mestre — 33 manifestações

| # | PL/PLC | Ofício | Autor | Ementa (resumo) | Posição | Palavras | Citações (EN) | Entregável |
|---|--------|--------|-------|-----------------|---------|----------|---------------|------------|
| 1 | PL 74/2025 | CVL 823/2026 | Carlo Caiado | Circuito Carioca de Economia Solidária (Lei 7.008/21) | Nada a opor | 343 | 4 (1) | 01-06 |
| 2 | PL 1795/2026 | SMG 1526/2026 | Salvino Oliveira | Transparência/segurança em entregas por plataformas digitais | Nada a opor | 317 | 4 (2) | 01-06 |
| 3 | PL 1826/2026 | SMG 1665/2026 | Marcio Santos | Programa de Coberturas Verdes e Sustentáveis | Nada a opor | 361 | 4 (1) | 01-06 |
| 4 | PL 1840/2026 | CVL 925/2026 | Marcio Santos | Gratuidade de orçamentos e visitas técnicas prévias | Nada a opor | 340 | 4 (1) | 01-06 |
| 5 | PL 1844/2026 | CVL 992/2026 | Wagner Tavares | Sinalização dos polos gastronômicos | Nada a opor | 288 | 4 (1) | 01-06 |
| 6 | PL 1866/2026 | CVL 1133/2026 | Marcio Ribeiro | Taxa de serviço (gorjeta) e taxa de música ao vivo | Nada a opor | 347 | 4 (1) | 01-06 |
| 7 | PL 1883/2026 | CVL 1214/2026 | Rafael Aloisio Freitas | Eixo Econômico Municipal de Assessoria de Investimentos | Nada a opor | 332 | 4 (1) | 01-06 |
| 8 | PL 1884/2026 | CVL 1218/2026 | Rafael Aloisio Freitas | Conceito de Eixo Econômico Municipal | Nada a opor | 322 | 4 (1) | 01-06 |
| 9 | PL 1897/2026 | CVL 1276/2026 | Vitor Hugo | Prêmio Viva Voluntário (Lei 6.906/21 / Agenda 2030) | Nada a opor | 326 | 5 (2) | 27-05 |
| 10 | PL 1900/2026 | CVL 1294/2026 | Rafael Aloisio Freitas | ISS sobre Assessoria de Investimentos (Lei 691/84) | Nada a opor | 353 | 4 (1) | 01-06 |
| 11 | PL 1904/2026 | CVL 1342/2026 | Fabio Silva | Funcionário p/ idosos e PcD em ATMs bancários | Nada a opor | 332 | 5 (2) | 27-05 |
| 12 | PL 1921/2026 | CVL 1476/2026 | — | Democratização de Imóveis (enfrentamento à violência contra mulheres) | Nada a opor | 331 | 4 | 27-05 |
| 13 | PL 1934/2026 | CVL 1568/2026 | Fabio Silva | Desconto em diárias de hospedagem (check-in/out) | **Nada a opor** (reescrita — original era contrário) | 351 | 4 (1) | 01-06 |
| 14 | PL 1954/2026 | CVL 1722/2026 | Felipe Pires | Fundo de Reparação e Renda da População Negra (FMRDRPN) | Nada a opor | 326 | 4 (1) | 01-06 |
| 15 | PLC 98/2026 | CVL 1227/2026 | Salvino Oliveira | Certidão de renda em HIS, EIS e locação de curta duração (LC 97/09) | Nada a opor | 345 | 4 (2) | 27-05 |
| 16 | PLC 102/2026 | CVL 1268/2026 | Marcio Ribeiro | Manutenção, auditoria e seguro em shopping centers | Nada a opor | 355 | 5 (2) | 27-05 |
| 17 | PLC 103/2026 | CVL 1279/2026 | Paulo Messina | Reviver Centro — reavaliação bienal de incentivos (LC 229/21) | Nada a opor | 364 | 5 (2) | 27-05 |
| 18 | PLC 104/2026 | CVL 1283/2026 | Rafael Aloisio Freitas | Estruturas em áreas de concessão vs. regime de quiosques | Nada a opor | 366 | 4 (2) | 27-05 |
| 19 | PLC 105/2026 | CVL 1322/2026 | Marcio Santos | Recarga de veículos elétricos (Código de Obras LC 198/19) | Nada a opor | 346 | 4 | 27-05 |
| 20 | PLC 106/2026 | CVL 1329/2026 | Flávio Valle | Recarga de veículos elétricos em condomínios | Nada a opor | 348 | 4 | 27-05 |
| 21 | PL 163/2025 | Despacho Ciência | Marcio Santos | Dia do Empreendedorismo Jovem (Lei 9.326/26) | **Ciência da lei** | 367 | 5 (2) | 04-06 |
| 22 | PL 1320/2025 | Despacho Ciência | Diego Faro | Mês do Empreendedorismo Carioca (Lei 9.337/26) | **Ciência da lei** | 361 | 5 (1) | 04-06 |
| 23 | PL 1538/2025 | SGV OFI 10541/2025 | Helena Vieira | Empresas Gestoras de Comércio Popular (MEI) | Nada a opor | 356 | 4 (2) | 07-06 |
| 24 | PL 1964/2026 | CVL 1765/2026 | Fernando Armelau | Dia do Empresário no Calendário Oficial | Nada a opor | 314 | 4 (2) | 07-06 |
| 25 | PL 1985/2026 | CVL 1902/2026 | Rick Azevedo | Mobilidade dos Entregadores por Bicicleta | Nada a opor | 370 | 3 (2) | 07-06 |
| 26 | PL 1990/2026 | CVL 1933/2026 | Salvino Oliveira | Auditoria de Conformidade para Telecom em Favelas | Nada a opor | 368 | 4 (2) | 07-06 |
| 27 | PL 2007/2026 | CVL 2002/2026 | Salvino Oliveira | Acesso a Serviços Básicos / Combate a Monopólios | Nada a opor | 355 | 3 (2) | 07-06 |
| 28 | PLC 112/2026 | CVL 2108/2026 | Inaldo Silva | Banheiro Família em Restaurantes | Nada a opor | 368 | 4 (2) | 07-06 |
| 29 | PL 2040/2026 | CVL 2229/2026 | Flávio Valle | Selo de Prevenção e Combate ao Antissemitismo | Nada a opor | 344 | 4 (3) | 07-06 |
| 30 | PELOM 5/2026 | CVL 2288/2026 | Rafael Aloisio Freitas | Engenhos Publicitários (art. 463 da Lei Orgânica) | Nada a opor | 370 | 4 (3) | 07-06 |
| 31 | PL 2076/2026 | CVL 3513/2026 | Alana Passos | Aliança Comercial de Bairro / microcorredores comerciais | Nada a opor | 367 | 4 (2) | 07-06 |
| 32 | PL 2078/2026 | CVL 3548/2026 | Alana Passos | Audiências Públicas Territoriais p/ intervenções urbanas | Nada a opor | 367 | 4 (3) | 07-06 |
| 33 | PL 2097/2026 | CVL 3646/2026 | Salvino Oliveira | Política de Incentivo a Residências Estudantis | Nada a opor | 368 | 4 (2) | 07-06 |

---

## Evolução por entregável (reconcilia o marco "22")

| Entregável | Lote | Qtd | Acumulado |
|------------|------|-----|-----------|
| `entregáveis 27-05-2026/` | A/B/C (PLC-98→106, PL-1897/1904/1921) | 9 | 9 |
| `entregáveis 01-06-2026/` | D/E + POC (PL-74, 1795, 1826, 1840, 1844, 1866, 1883, 1884, 1900, 1934, 1954) | 11 | 20 |
| `entregáveis 04-06-2026/` | F — ciência da lei (PL-163, PL-1320) | 2 | **22** |
| `entregáveis 07-06-2026/` | G+H (PL-1538, 1964, 1985, 1990, 2007, PLC-112, 2040, PELOM-5, 2076, 2078, 2097) | 11 | **33** |

> O número **22** corresponde ao acervo concluído até o entregável de **04-06-2026**. A varredura da pasta de despachos identificou os **11 faltantes** (Lote G+H), processados e entregues em 07-06-2026 → **33** no total.

---

## Bloqueado (não processável)

| Documento | Autor | Motivo |
|-----------|-------|--------|
| IND CMRJ 06549/2025 | Vereador Leonel de Esquerda | PDF contém apenas despachos de roteamento; texto da indicação ausente. Ver `IND-CMRJ-06549-2025/BLOQUEIO.md`. Aguarda documento da Câmara. |

## Fora de escopo (não são despachos a processar)

- **PL 1736/2025** (Polo Gastronômico Magarça) — é o **exemplo-modelo** do Marcel (formato V1 antigo), usado como semente em `workflow_manifestacao_pl.md`. Não há despacho pendente.
- Anexos na pasta de despachos: planilhas de custos, plano de mídia, formulário de patrocínio, Ofício CVM, protocolos MDEPRO/MCTI, tabela ISS — material de apoio, não PLs.
