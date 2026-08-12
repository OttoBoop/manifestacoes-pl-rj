#!/usr/bin/env python3
"""Gate V5.2 "economia-only": bloqueia argumento jurídico no corpo da manifestação.

Uso: python3 checar_economia_only.py <manifestacao-short.md> [outra.md ...]

Lista DURA (exit 1): tribunais, jurisprudência, (in)constitucionalidade, vício de
iniciativa, fórmula de competência. Lista de AVISO (exit 0, warn): CF, Constituição,
Lei Orgânica, "competência" isolada — podem ser objeto do PL (R3 do ECONOMIA-ONLY.md);
o coordenador julga. Regra completa: workflow/V5.2/ECONOMIA-ONLY.md
"""

import re
import sys

HARD = [
    (r"\bSTF\b", "STF"),
    (r"\bSTJ\b", "STJ"),
    (r"\bTJ-?[A-Z]{2}\b", "Tribunal de Justiça (sigla)"),
    (r"Supremo Tribunal", "Supremo Tribunal"),
    (r"Superior Tribunal", "Superior Tribunal"),
    (r"Tribunal de Justiça", "Tribunal de Justiça"),
    (r"\bADI\b", "ADI"),
    (r"\bADPF\b", "ADPF"),
    (r"[Ss]úmula", "súmula"),
    (r"[Tt]ema (repetitivo|\d+)", "tema repetitivo/numerado (STF/STJ)"),
    (r"[Jj]urisprud", "jurisprudência"),
    (r"constitucionalidade", "(in)constitucionalidade"),
    (r"inconstitucional", "inconstitucional"),
    (r"[Vv]ício de iniciativa", "vício de iniciativa"),
    (r"iniciativa parlamentar", "iniciativa parlamentar"),
    (r"[Cc]ompetência (municipal|legislativa|constitucional|privativa|do [Pp]oder)",
     "fórmula de competência"),
]

WARN = [
    (r"\bCF\b|CF/1988", "menção à CF"),
    (r"Constituição", "Constituição"),
    (r"Lei Orgânica", "Lei Orgânica"),
    (r"[Cc]ompetência", "'competência' isolada"),
    (r"art(igo|\.)\s*\d+[^.]{0,30}da (CF|Constituição)", "artigo da CF"),
]


def check(path):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    hard_hits, warn_hits = [], []
    for i, line in enumerate(lines, 1):
        for rx, label in HARD:
            if re.search(rx, line):
                hard_hits.append((i, label, line.strip()[:110]))
        for rx, label in WARN:
            if re.search(rx, line) and not any(re.search(h, line) for h, _ in HARD):
                warn_hits.append((i, label, line.strip()[:110]))
    return hard_hits, warn_hits


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    blocked = False
    for path in sys.argv[1:]:
        hard_hits, warn_hits = check(path)
        print(f"== {path}")
        if hard_hits:
            blocked = True
            print(f"  ❌ BLOQUEADO — {len(hard_hits)} ocorrência(s) da lista dura:")
            for ln, label, ctx in hard_hits:
                print(f"     L{ln} [{label}] {ctx}")
        if warn_hits:
            print(f"  ⚠️  {len(warn_hits)} aviso(s) — julgar se é objeto do PL (R3) ou argumento (R1):")
            for ln, label, ctx in warn_hits:
                print(f"     L{ln} [{label}] {ctx}")
        if not hard_hits and not warn_hits:
            print("  ✅ corpo 100% econômico")
    sys.exit(1 if blocked else 0)


if __name__ == "__main__":
    main()
