#!/usr/bin/env python3
"""Acrescenta linhas à tabela 19 ("Manifestação PLs SUBDEI") da planilha VIVA
do Google Sheets, usando o navegador já logado do perfil da skill notebooklm.

Uso:
  python3 sheets_append_tabela19.py --tsv controle-excel/tabela19_novas_2026-08-18.tsv \
      [--start-row 343] [--headed] [--dry-run]

O TSV tem 5 colunas por linha (Ação, Prazo, Responsável, Status, Observação).
Escreve célula a célula a partir de A<start-row>, na aba SUBDEI. NÃO apaga nada:
só preenche linhas vazias abaixo do fim atual da tabela.
Regra da casa: verificar permissão de edição antes; abortar se somente leitura.
"""

import argparse
import csv
import re
import sys
import time
from pathlib import Path

SKILL = Path.home() / ".claude/skills/notebooklm"
sys.path.insert(0, str(SKILL / "scripts"))

from patchright.sync_api import sync_playwright  # noqa: E402
from browser_utils import BrowserFactory  # noqa: E402

SHEET_URL = ("https://docs.google.com/spreadsheets/d/"
             "1_dvWvV8RUrX3Mm6XZEwPhMQh-6JU3_GA/edit#gid=0")
SHOT_DIR = Path("/tmp/claude-1000/-home-otavio-Documents-vscode/"
                "d396d56d-4996-4413-97c8-5dc334ea99d9/scratchpad")


def goto_cell(page, ref):
    """Usa a Name Box (Caixa de nome) para pular direto para uma célula."""
    box = page.locator("#t-name-box")
    box.click()
    page.keyboard.press("Control+a")
    page.keyboard.type(ref)
    page.keyboard.press("Enter")
    time.sleep(0.6)


def type_cell(page, text):
    """Digita o conteúdo de uma célula.

    IMPORTANTE: usar keyboard.type (eventos reais). O Sheets NÃO captura
    keyboard.insert_text (CDP Input.insertText) — o texto some silenciosamente.
    """
    page.keyboard.type(text, delay=8)
    time.sleep(0.15)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tsv", required=True)
    ap.add_argument("--start-row", type=int, default=343)
    ap.add_argument("--headed", action="store_true", help="mostra o navegador")
    ap.add_argument("--dry-run", action="store_true",
                    help="abre, checa permissão e sai sem escrever")
    args = ap.parse_args()

    with open(args.tsv, encoding="utf-8") as f:
        rows = [r for r in csv.reader(f, delimiter="\t") if any(c.strip() for c in r)]
    assert all(len(r) == 5 for r in rows), "TSV deve ter 5 colunas por linha"
    print(f"Linhas a escrever: {len(rows)} (a partir de A{args.start_row})")

    with sync_playwright() as pw:
        ctx = BrowserFactory.launch_persistent_context(pw, headless=not args.headed)
        page = ctx.new_page()
        page.set_viewport_size({"width": 1600, "height": 1000})
        page.goto(SHEET_URL, wait_until="domcontentloaded", timeout=90000)
        time.sleep(10)

        if "accounts.google.com" in page.url:
            print("❌ Não autenticado no Google neste perfil.", file=sys.stderr)
            ctx.close()
            sys.exit(2)

        body = page.inner_text("body")[:4000]
        if re.search(r"Somente leitura|View only|Modo de exibição|Solicitar acesso|Request edit access", body):
            print("❌ SEM PERMISSÃO DE EDIÇÃO (planilha aberta como somente leitura).", file=sys.stderr)
            page.screenshot(path=str(SHOT_DIR / "sheets_readonly.png"))
            ctx.close()
            sys.exit(3)

        # Fecha painel lateral do Gemini e banner de navegador, que roubam foco
        for sel in ['button[aria-label*="Fechar"]', 'button[aria-label*="Close"]',
                    'div[role="button"][aria-label*="Fechar"]']:
            for i in range(page.locator(sel).count()):
                try:
                    page.locator(sel).nth(i).click(timeout=1500)
                    time.sleep(0.4)
                except Exception:
                    pass
        page.keyboard.press("Escape")
        time.sleep(1)

        page.screenshot(path=str(SHOT_DIR / "sheets_aberto.png"))
        print(f"✅ Planilha aberta e editável — título: {page.title()[:70]}")

        if args.dry_run:
            ctx.close()
            return

        goto_cell(page, f"A{args.start_row}")
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                type_cell(page, val)
                if j < 4:
                    page.keyboard.press("Tab")
            page.keyboard.press("Enter")           # commit; volta à coluna A
            goto_cell(page, f"A{args.start_row + i + 1}")
            print(f"  ✍️  linha {args.start_row + i}: {row[0][:38]}")

        time.sleep(6)  # deixa o autosave concluir
        page.screenshot(path=str(SHOT_DIR / "sheets_final.png"))
        saved = bool(re.search(r"Salvo no Drive|Todas as alterações|Saved to Drive|Última edição",
                               page.inner_text("body")[:6000]))
        print("💾 autosave detectado" if saved else "⚠️  não vi confirmação de autosave — conferir no export")
        ctx.close()


if __name__ == "__main__":
    main()
