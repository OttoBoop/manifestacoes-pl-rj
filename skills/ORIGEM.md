# Skills do fluxo de manifestações — cópia versionada

As três skills que o fluxo usa (`workflow_manifestacao_pl.md` as referencia) vivem
instaladas em `~/.claude/skills/` — é **lá** que o Claude Code as executa. Esta pasta
é a **cópia versionada junto com as PLs**, para que as regras do fluxo acompanhem o
repositório (regra do Otávio, 10/07/2026: "as principais skills devem estar na mesma
pasta com as PLs").

| Skill | Papel no fluxo | Instalação executável |
|-------|----------------|----------------------|
| `agentic_research/` | 4 duplas pesquisador+escritor por PL (T1 exegese, T2 prós, T3 contras, T4 dados); inventário F-T.N | `~/.claude/skills/agentic_research/` |
| `audit_sources/` | Verificação NB-first das citações antes do envio | `~/.claude/skills/audit_sources/` |
| `notebooklm/` | Base de conhecimento por PL (upload PDF/OCR, fontes, queries) | `~/.claude/skills/notebooklm/` |

**Não copiados** (são estado da máquina, não regra): `notebooklm/.venv/`,
`notebooklm/data/` (autenticação Google + browser profile) e `notebooklm/images/`.
Para executar a partir de um clone novo, instale a skill em `~/.claude/skills/` e
autentique com `python scripts/run.py auth_manager.py setup`.

**Sincronização:** ao alterar uma skill em `~/.claude/skills/`, recopiar para cá no
mesmo commit em que a mudança for usada pelo fluxo.
