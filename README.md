# Manifestações Técnicas — PLs Câmara Municipal RJ

Pipeline automatizada de análise de Projetos de Lei para a Secretaria Municipal de
Desenvolvimento Econômico (SMDE) do Rio de Janeiro.

## Como funciona

Ver [`workflow_manifestacao_pl.md`](workflow_manifestacao_pl.md) para o fluxo completo.

Resumo: dado o PDF de um PL, o sistema usa agentes em paralelo (pesquisador + escritor
por tópico) para produzir uma manifestação técnica fundamentada em fontes verificáveis.

## Estrutura

```
.
├── workflow_manifestacao_pl.md   ← playbook do pipeline
├── PL-74-2025/                   ← exemplo: PL 74/2025 Economia Solidária
│   ├── texto_extraido.md
│   ├── manifestacao_PL-74-2025.md
│   └── inventario_fontes_PL-74-2025.md
└── PL-XXXX-YYYY/                 ← próximos PLs seguem o mesmo padrão
```

## Skills utilizadas

- [`notebooklm`](https://github.com/anthropics/claude-code) — base de conhecimento por PL
- `agentic_research` — produção paralela com duplas pesquisador + escritor
- `audit_sources` — verificação de citações (opcional, antes do envio)

## Tecnologia

Claude Code (Anthropic) com skills customizadas instaladas em `~/.claude/skills/`.
