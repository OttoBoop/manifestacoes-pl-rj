# Auditoria de Fontes — Manifestação Técnica PLC nº 98/2026

**Arquivo auditado:** `manifestacao_PLC-98-2026-short.md`
**Data da auditoria:** 2026-05-27
**Auditor:** Ariadne (Claude Code)
**Protocolo:** NB-first (NotebookLM consultado antes de qualquer fonte web)

---

## Metodologia

1. Leitura integral do texto auditado (16 linhas, ~350 palavras)
2. Extração de todas as citações explícitas e afirmações implícitas verificáveis
3. Consulta ao NotebookLM do projeto antes de qualquer busca web
4. Verificação via WebFetch (planalto.gov.br, sdgs.un.org, world-habitat.org) + WebSearch
5. Decisão sobre status: ✅ CONFIRMADO / ⚠️ PARCIAL / ❓ INVERIFICÁVEL
6. Decisão sobre correção: exclusivamente do usuário

**Nota NB-first:** O NotebookLM consultado (https://notebooklm.google.com/notebook/4f771810-1d68-4398-9fc6-bf4567826383) contém apenas o texto do PLC 98/2026 e legislação citada. Não contém o relatório World Habitat nem dados MCMV históricos. Confirmado via query direta.

---

## Citações verificadas

---

### [F-1] CF/1988 — Arts. 30 I e II, 182, 6º

**Trecho no texto:** "A competência municipal está fundada nos arts. 30, I e II, e 182 da CF/1988 (BRASIL. 'Constituição Federal', Senado Federal, 1988)" e "em consonância com o art. 6º da CF/1988"

**Status:** ✅ CONFIRMADO

**Trechos localizados:**

- **Art. 6º (direito à moradia):** "São direitos sociais a educação, a saúde, a alimentação, o trabalho, a moradia, o transporte, o lazer, a segurança, a previdência social, a proteção à maternidade e à infância, a assistência aos desamparados, na forma desta Constituição."

- **Art. 30, I e II (competência municipal):**
  - Inciso I: "legislar sobre assuntos de interesse local"
  - Inciso II: "suplementar a legislação federal e a estadual no que couber"

- **Art. 182 (política urbana), caput:** "A política de desenvolvimento urbano, executada pelo Poder Público municipal, conforme diretrizes gerais fixadas em lei, tem por objetivo ordenar o pleno desenvolvimento das funções sociais da cidade e garantir o bem-estar de seus habitantes."

**Fonte verificada:** https://modeloinicial.com.br/lei/CF/constituicao-federal/art-30 e https://modeloinicial.com.br/lei/CF/constituicao-federal/art-182 (espelhos do texto do Planalto)

**Nota:** A citação bibliográfica (BRASIL. "Constituição Federal", Senado Federal, 1988) é formalmente imprecisa — a autoridade oficial é o Congresso Nacional/Diário Oficial; o Senado Federal publica versões atualizadas mas não é o promulgador. Imprecisão menor, comum na literatura técnica. Os artigos citados existem e têm o conteúdo afirmado.

---

### [F-2] Lei nº 11.977/2009 — PMCMV

**Trecho no texto:** "Com 6 milhões de unidades MCMV contratadas no Brasil, o rigor na triagem é determinante (BRASIL. 'Lei nº 11.977/2009', Congresso Nacional, 2009)"

**Status:** ⚠️ PARCIAL

**O que foi confirmado:**
- Lei 11.977/2009 existe, está publicada no Planalto, e cria o Programa Minha Casa, Minha Vida (PMCMV).
- Ementa: "Dispõe sobre o Programa Minha Casa, Minha Vida – PMCMV e a regularização fundiária de assentamentos localizados em áreas urbanas..."
- Data: 7 de julho de 2009. Confirmado via WebSearch + links do Planalto.

**O que NÃO foi confirmado:**
- O número "6 milhões de unidades MCMV contratadas" **não está sustentado pela Lei 11.977/2009** — a lei não contém dados de execução, apenas institui o programa.
- O dado correto encontrado nas fontes oficiais: em março de 2024 (15º aniversário do programa), a Agência Gov divulgou "mais de **7,7 milhões** de moradias contratadas" desde 2009. O número "6 milhões" não corresponde a nenhum marco identificável no acervo pesquisado.
- A frase une dado quantitativo ("6 milhões") com referência à lei instituidora (11.977/2009), como se a lei sustentasse o número. Isso é incorreto estruturalmente: a lei não cita esse número.

**Fonte verificada:**
- Lei: https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/lei/l11977.htm
- Dado 7,7 milhões: https://agenciagov.ebc.com.br/noticias/202403/minha-casa-minha-vida-completa-15-anos-abrindo-portas-para-novos-sonhos-de-conquista-da-casa-propria ("O programa chega a 2024 celebrando a marca de mais de 7,7 milhões de moradias contratadas.")

**Discrepância:** O número "6 milhões" está desatualizado (subestimado) e a lei citada não é a fonte do dado. A referência correta para o dado quantitativo seria uma nota da Agência Gov, MCIDADES ou CAIXA, não a lei instituidora.

---

### [F-3] World Habitat "The Airbnb Effect" 2024

**Trecho no texto:** "O Art. 1º-C tem precedente internacional consolidado: Amsterdã, Barcelona e Nova York limitaram o Airbnb para preservar moradia acessível (WORLD HABITAT. 'The Airbnb Effect: Short-Term Rentals with Long-Term Consequences', World Habitat, 2024)"

**Status:** ⚠️ PARCIAL — com duas discrepâncias

**O que foi confirmado:**
- O artigo existe e é da World Habitat: título confirmado como "The Airbnb Effect: short-term rentals with long-term consequences".
- URL real: https://world-habitat.org/blog/airbnb-and-the-housing-crisis/
- Barcelona e Nova York são mencionadas no artigo como exemplos de cidades que limitaram o Airbnb. Confirmado via WebFetch direto na URL.
- A afirmação de fundo (Airbnb pressiona oferta de moradia acessível) é factualmente suportada pelo artigo.

**Discrepâncias identificadas:**

1. **Ano errado:** O artigo foi publicado em **18 de dezembro de 2025**, não em 2024 como consta na citação.

2. **Amsterdam não está no artigo:** O texto auditado afirma que "Amsterdã, Barcelona e Nova York limitaram o Airbnb" como afirmação atribuída a este artigo específico. A verificação direta via WebFetch mostra que o artigo da World Habitat **menciona Barcelona e Nova York, mas não menciona Amsterdam**. Amsterdam é factualmente correta como cidade que regulamentou o Airbnb (confirmado por fontes independentes — ver F-6), mas **não está neste artigo específico**. O texto auditado atribui os três exemplos à mesma fonte, o que é impreciso.

**Fonte verificada:** https://world-habitat.org/blog/airbnb-and-the-housing-crisis/ (acesso direto via WebFetch)

**Nota:** O artigo é de autoria de David Ireland (CEO, World Habitat), publicado em dezembro de 2025. A organização é registrada como instituição de caridade nº 270987 (Reino Unido).

---

### [F-4] ONU "Goal 11" — UN/DESA 2015

**Trecho no texto:** "A ODS 11.1 da Agenda 2030 estabelece meta de moradia adequada para todos até 2030 (ONU. 'Goal 11', UN/DESA, 2015)"

**Status:** ✅ CONFIRMADO

**Trecho localizado:** Meta 11.1 (texto literal): "By 2030, ensure access for all to adequate, safe and affordable housing and basic services and upgrade slums."

Em português (ONU Brasil): "Até 2030, garantir o acesso de todos a habitação segura, adequada e a preço acessível, e aos serviços básicos e urbanizar as favelas."

**Fonte verificada:** https://sdgs.un.org/goals/goal11 (página oficial confirmada via WebFetch)

**Nota:** A atribuição "UN/DESA 2015" é tecnicamente correta — o Departamento de Assuntos Econômicos e Sociais da ONU (UN/DESA) é o órgão custodiante dos ODS, e 2015 é o ano de adoção da Agenda 2030 (Resolução A/RES/70/1, setembro de 2015). A referência é adequada.

---

### [F-5] FONTE IMPLÍCITA — "6 milhões de unidades MCMV contratadas no Brasil"

**Trecho no texto:** "Com 6 milhões de unidades MCMV contratadas no Brasil..."

**Status:** ⚠️ PARCIAL — número subestimado e sem fonte própria

**Verificação:**
- O número "6 milhões" não corresponde a nenhum marco oficial identificável nas fontes pesquisadas.
- Fontes oficiais (Agência Gov, março 2024): **mais de 7,7 milhões** de unidades contratadas desde a criação do programa em 2009.
- Fontes recentes (Agência Gov, janeiro 2025): 1,26 milhão contratadas apenas em 2024; desde a retomada em 2023, 1,9 milhão.
- A meta para 2026 é de 3 milhões de unidades na fase atual (Lula III).
- "6 milhões" pode referir-se a um período anterior (estimativa de 2016 era de ~4,2 milhões contratados), mas nenhum marco de exatamente "6 milhões" foi identificado.

**Fontes verificadas:**
- https://agenciagov.ebc.com.br/noticias/202403/minha-casa-minha-vida-completa-15-anos-abrindo-portas-para-novos-sonhos-de-conquista-da-casa-propria
- https://agenciagov.ebc.com.br/noticias/202501/minha-casa-minha-vida-fecha-2024-com-1-26-milhao-de-unidades-contratadas-1

**Nota:** O número correto e verificável para uso na manifestação seria "mais de 7,7 milhões de unidades contratadas desde 2009" com citação à nota da Agência Gov de março/2024.

---

### [F-6] FONTE IMPLÍCITA — Amsterdam, Barcelona e Nova York limitaram o Airbnb

**Trecho no texto:** "Amsterdã, Barcelona e Nova York limitaram o Airbnb para preservar moradia acessível"

**Status:** ✅ CONFIRMADO — os três fatos são verdadeiros, mas a fonte citada (World Habitat 2024) não menciona Amsterdam

**Verificação por cidade:**

- **Barcelona:** Confirmado. Em junho de 2024, Barcelona anunciou política de banimento total de aluguéis de curta duração até 2028. Fonte: World Habitat (https://world-habitat.org/blog/airbnb-and-the-housing-crisis/) e Bloomberg (2024-07-09).

- **Nova York:** Confirmado. A Local Law 18 entrou em vigor em 2023, exigindo registro de hosts e presença do proprietário durante a estadia, o que efetivamente restringiu o Airbnb. Fonte: World Habitat (mesma URL acima).

- **Amsterdam:** Confirmado por fontes independentes. Amsterdam impôs limite de 30 noites/ano em 2019, reduzido para 15 noites/ano em abril de 2026, com multas de até €20.500. Fontes: Hostaway, ProofSnap, Keycafe (2026). O número de aluguéis de curta duração no Airbnb em Amsterdam caiu 54% entre 2019 e 2024. **Porém, Amsterdam não é mencionada no artigo da World Habitat citado** — é uma informação factual correta, mas a fonte atribuída no texto não a cobre.

**Fontes verificadas:**
- https://world-habitat.org/blog/airbnb-and-the-housing-crisis/ (Barcelona e NY)
- https://www.hostaway.com/blog/airbnb-rules-in-amsterdam-2026/ (Amsterdam)
- https://getproofsnap.com/posts/short-term-rental-regulations-netherlands-amsterdam-2026.html (Amsterdam)

**Nota:** A afirmação factual sobre as três cidades é verdadeira. O problema é de atribuição: a fonte citada (World Habitat) cobre Barcelona e Nova York, mas não Amsterdam. Para cobrir as três cidades, é necessária uma segunda fonte ou reformular a citação.

---

### [F-7] FONTE IMPLÍCITA — Art. 48 Lei 8.245/1991 define locação por temporada

**Trecho no texto:** "O art. 1º-C usa 'locação de curta duração' sem definição legal — a regulamentação deverá precisar o conceito (cf. Lei nº 8.245/1991, art. 48)"

**Status:** ✅ CONFIRMADO

**Trecho localizado — Art. 48, caput (texto literal):**
"Considera-se locação para temporada aquela destinada à residência temporária do locatário, para prática de lazer, realização de cursos, tratamento de saúde, feitura de obras em seu imóvel, e outros fatos que decorrem tão-somente de determinado tempo, e contratada por prazo não superior a noventa dias, esteja ou não mobiliado o imóvel."

**Art. 48, parágrafo único:** "No caso de a locação envolver imóvel mobiliado, constará do contrato, obrigatoriamente, a descrição dos móveis e utensílios que o guarnecem, bem como o estado em que se encontram."

**Fonte verificada:** https://modeloinicial.com.br/lei/L-8245-1991/lei-inquilinato/art-48 (espelho do texto do Planalto); https://www.legjur.com/legislacao/art/lei_00082451991-48

**Nota:** O art. 48 define "locação para temporada" com prazo máximo de 90 dias. A referência é tecnicamente correta como ponto de partida para a regulamentação, embora o conceito de "locação de curta duração" do PLC não seja idêntico — locações via plataformas digitais (Airbnb) costumam ser diárias, não mensais, e têm natureza distinta da locação por temporada da Lei 8.245. A ressalva do texto auditado (pedir regulamentação para precisar o conceito) é pertinente.

---

## Sumário executivo

| ID | Descrição | Status |
|----|-----------|--------|
| F-1 | CF/1988 arts. 30 I/II, 182, 6º | ✅ CONFIRMADO |
| F-2 | Lei 11.977/2009 + "7,7 milhões unidades" | ⚠️ CORRIGIDO — número atualizado, fonte trocada para Agência Gov 2024 |
| F-3 | World Habitat "Airbnb Effect" 2025 | ⚠️ CORRIGIDO — ano 2025, Amsterdam removida |
| F-4 | ONU Goal 11 / UN/DESA 2015 | ✅ CONFIRMADO |
| F-5 | Implícita: "7,7 milhões unidades MCMV" | ⚠️ CORRIGIDO — número atualizado |
| F-6 | Implícita: Barcelona e Nova York (Amsterdam removida) | ✅ CONFIRMADO — agora atribuição correta |
| F-7 | Implícita: Art. 48 Lei 8.245/1991 | ✅ CONFIRMADO |

**Contagem pós-correções:** 5 ✅ CONFIRMADO/CORRIGIDO | 2 ⚠️ CORRIGIDO | 0 ❓ INVERIFICÁVEL
**Placar final:** 5 ✅ confirmados + 3 ⚠️ corrigidos (DC-1, DC-2, DC-3) + 0 ❓

---

## Discrepâncias críticas

### DC-1: Ano do artigo World Habitat (F-3)
- **Citado no texto:** 2024
- **Ano real:** 2025 (publicado em 18 de dezembro de 2025)
- **Impacto:** Erro de ano em citação — a manifestação foi redigida em maio de 2026, então o artigo existia e pode ser citado; mas o ano está errado.

### DC-2: Amsterdam ausente na fonte citada (F-3 / F-6)
- **Afirmação no texto:** "Amsterdã, Barcelona e Nova York limitaram o Airbnb" atribuída ao artigo World Habitat
- **Realidade:** O artigo da World Habitat cobre apenas Barcelona e Nova York. Amsterdam não é mencionada naquele artigo.
- **Amsterdam como fato:** É verdadeiro — Amsterdam regulamentou o Airbnb desde 2019 e restringiu a 15 noites/ano em 2026. Mas precisa de fonte própria se listada junto das outras.

### DC-3: Número "6 milhões" subestimado e sem fonte adequada (F-2 / F-5)
- **Citado no texto:** "6 milhões de unidades MCMV contratadas no Brasil"
- **Número correto (2024):** Mais de 7,7 milhões de unidades contratadas desde 2009 (Agência Gov, março/2024)
- **Problema estrutural:** A Lei 11.977/2009 não contém esse dado — é uma lei instituidora, não um relatório de execução. O dado quantitativo precisa de fonte própria (nota da Agência Gov ou MCIDADES).

---

## Decisões do usuário

| ID | Discrepância | Opções | Decisão |
|----|-------------|--------|---------|
| DC-1 | Ano World Habitat: 2024 → corrigir para 2025 | (a) corrigir para 2025; (b) manter e aceitar erro menor | ✅ APLICADO: corrigido para 2025 |
| DC-2 | Amsterdam sem cobertura na fonte citada | (a) remover Amsterdam da lista; (b) adicionar nota de rodapé com fonte independente; (c) reformular | ✅ APLICADO: Amsterdam removida; mantidos apenas "Barcelona e Nova York" |
| DC-3 | "6 milhões" desatualizado e sem fonte própria | (a) atualizar para "mais de 7,7 milhões" + citar Agência Gov março/2024; (b) remover o dado; (c) manter com ressalva | ✅ APLICADO: "mais de 7,7 milhões" + SECOM/Agência Gov 2024 |

---

## Log de execução

- **NB consultado:** https://notebooklm.google.com/notebook/4f771810-1d68-4398-9fc6-bf4567826383 — contém apenas o PLC 98/2026 e legislação citada. Não tem World Habitat nem dados MCMV.
- **CF/1988:** WebFetch direto ao Planalto falhou (timeout/socket). Verificado via modeloinicial.com.br (espelho) e WebSearch com textos literais confirmados.
- **Lei 11.977/2009:** Confirmada via WebSearch + links Planalto. Texto do Art. 1º verificado.
- **World Habitat:** WebFetch direto à URL https://world-habitat.org/blog/airbnb-and-the-housing-crisis/ — funcionou. Ano 2025 e ausência de Amsterdam confirmados diretamente.
- **sdgs.un.org/goals/goal11:** WebFetch funcionou — página existe, Goal 11 e meta 11.1 confirmados.
- **Dado MCMV 7,7 milhões:** WebFetch + WebSearch — Agência Gov março/2024 confirma 7,7 milhões. Nenhuma fonte encontrou marco de "6 milhões".
- **Art. 48 Lei 8.245/1991:** Planalto retornou página vazia via curl. Verificado via modeloinicial.com.br + WebSearch — texto literal confirmado.
- **Amsterdam:** WebSearch ampla confirmou regulação desde 2019 (30 noites/ano) e redução para 15 noites/ano em abril de 2026.
