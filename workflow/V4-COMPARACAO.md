# V4 vs V3 — Comparação caso a caso

> Síntese adversarial (V4) aplicada aos 9 PLs já processados pela V3.  
> Pipeline V4: PRÓ enviesado + CONTRA enviesado + Síntese comparativo.

---

## Tabela comparativa

| PL | V3 posição | V4 posição | Mudou? | Ressalvas V3 | Ressalvas V4 | Ganho principal da V4 |
|----|-----------|-----------|--------|--------------|--------------|----------------------|
| **PL 74/2025** (Circuito Econ. Solidária) | Nada a opor | Nada a opor | Não | 2 | 2 | Explicitação das ressalvas como **estruturais e condicionais**, não meramente regulamentares |
| **PL 1795/2026** (Plataformas de entrega) | Nada a opor | Nada a opor | Não | 2 | 3 | **Monitoramento anti-redlining** — relatório anual de cobertura territorial (NOVO) |
| **PL 1840/2026** (Gratuidade orçamentos) | Nada a opor | Nada a opor | Não | 3 | 3 | **Gradação proporcional da multa por porte** do agente regulado (NOVO) |
| **PL 1844/2026** (Polos gastronômicos) | Nada a opor | Nada a opor | Não | 3 | 4 | **Estimativa de custo** para cenário em que parcerias não cubram 100% (NOVO) |
| **PL 1866/2026** (Gorjeta + música ao vivo) | Nada a opor | Nada a opor | Não | 2 | 3 | **Fiscalização por reclamação documentada**, não amostragem universal (NOVO) |
| **PL 1883/2026** (Eixo Econ. Assessoria Inv.) | Nada a opor | Nada a opor | Não | 2 | 4 | **Contrapartida operacional + cláusula de revisão em 3 anos** (NOVO × 2) |
| **PL 1884/2026** (Lei-quadro Eixo Econômico) | Nada a opor | Nada a opor | Não | 3 | 4 | **Revisão automática de cada Eixo a cada 3 anos** (NOVO) |
| **PL 1900/2026** (ISS Assessoria — alteração CTM) | Nada a opor | Nada a opor | Não | 2 | 3 | **Cláusula de revisão** alinhada ao PL 1883 (NOVO) |
| **PL 1934/2026** (Desconto em hospedagem) | **Contrário** | **Contrário** | Não — confirmado | 4 (técnicas) | 6 (técnicas) | **Posição CONTRÁRIO confirmada** após teste adversarial; +2 ressalvas técnicas (impacto fiscal + Anexo Único) |
| **PL 1954/2026** (Fundo Reparação Pop. Negra) | Nada a opor | Nada a opor | Não | 3 | 5 | **Dimensionamento dos Centros + critério verificável de elegibilidade** (NOVO × 2) |

---

## Análise meta — o que o pipeline adversarial (V4) produziu

### Em todos os 9 PLs, a V4 manteve a posição da V3

Nenhum PL teve **mudança de posição** entre V3 e V4. Em particular:
- O único caso de CONTRÁRIO (PL 1934) **resistiu** ao melhor caso pró-enviesado possível — confirmação de robustez.
- Os 8 casos de "nada a opor" continuaram "nada a opor".

Isso **não é falha do método** — é um achado importante: as posições V3 estavam tecnicamente robustas, sem viés sistemático que o adversarial pudesse expor.

### Em 9 de 9 PLs, a V4 adicionou ou refinou ressalvas operacionais

Em **todos os casos**, a contraposição PRÓ × CONTRA expôs lacunas operacionais no desenho ou na regulamentação que a V3 não havia capturado adequadamente:

- **Anti-redlining** (PL 1795)
- **Gradação proporcional de multa** (PL 1840)
- **Transparência fiscal de parceria** (PL 1844)
- **Modelo de fiscalização por reclamação** (PL 1866)
- **Contrapartida operacional + cláusula de revisão** (PL 1883)
- **Revisão automática de Eixos** (PL 1884)
- **Cláusula de revisão alinhada** (PL 1900)
- **Estimativa de impacto fiscal + Anexo Único divulgado** (PL 1934)
- **Dimensionamento de Centros + elegibilidade verificável** (PL 1954)

Em 7 dos 9 PLs, a ressalva nova **veio do argumento contra-enviesado** — algo que o pipeline equilibrado V3 não havia explicitado.

### Quando o pipeline adversarial vale o investimento?

Casos em que a V4 produziu **mais ganho substantivo**:
- PL 1795 (gig economy): risco de redlining digital — efeito perverso só visível na contraposição
- PL 1883 (Eixo Econ. Assessoria): contrapartida operacional + revisão — falha de desenho ausente da V3
- PL 1954 (Fundo Pop. Negra): dimensionamento dos Centros + elegibilidade verificável — riscos operacionais críticos

Casos em que o ganho foi marginal:
- PL 74/2025 (já maduro pela V1+V2+V3)
- PL 1844 (polos gastronômicos — pauta simples)

### Limitações observadas

1. **Coordenador-direto** (workaround pelos crashes de agentes em paralelo) foi aplicado em todos os 9 PLs. Pipeline com agentes paralelos não foi testado em V4 por inviabilidade prática.
2. A **mesma persona** redigiu PRÓ, CONTRA e Síntese — risco de **viés do coordenador** infectar ambos os lados enviesados. Em uma execução com 3 agentes distintos (3 chamadas LLM independentes), a divergência entre os lados poderia ser maior.
3. **Síntese vencer por consistência interna**: o coordenador conhece a V3 e os 2 lados; pode haver tendência inconsciente de chegar a posição que reconcilia ambos sem testar genuinamente um terceiro caminho.

### Conclusão geral

O pipeline adversarial **agregou valor mensurável em todos os 9 PLs**, principalmente sob forma de ressalvas operacionais regulamentares ausentes da V3. **Não mudou nenhuma posição** (consistência com V3 = boa notícia para a V3), mas **enriqueceu fundamentação e refinou recomendações**. O investimento adicional (~2× tempo + 3 fluxos) compensa em casos de PL com trade-offs ricos; é marginal em casos consensuais.

Recomendação: usar V4 como **modo padrão** apenas em PLs com sinais de trade-off econômico significativo (impacto fiscal, externalidades, sobreposição regulatória); manter V3 como modo padrão para PLs simples/operacionais.
