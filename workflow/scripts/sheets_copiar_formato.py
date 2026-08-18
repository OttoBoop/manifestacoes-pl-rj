#!/usr/bin/env python3
"""Copia SOMENTE a formatação de uma linha-modelo para um intervalo de linhas
na planilha viva (tabela 19). Não altera conteúdo.

Uso: python3 sheets_copiar_formato.py --modelo 342 --de 343 --ate 356
"""

import argparse
import sys
import time
from pathlib import Path

SKILL = Path.home() / ".claude/skills/notebooklm"
sys.path.insert(0, str(SKILL / "scripts"))

from patchright.sync_api import sync_playwright  # noqa: E402
from browser_utils import BrowserFactory  # noqa: E402

SHEET_URL = ("https://docs.google.com/spreadsheets/d/"
             "1_dvWvV8RUrX3Mm6XZEwPhMQh-6JU3_GA/edit#gid=0")
SHOT = Path("/tmp/claude-1000/-home-otavio-Documents-vscode/"
            "d396d56d-4996-4413-97c8-5dc334ea99d9/scratchpad")


def goto(page, ref):
    nb = page.locator("#t-name-box").first
    nb.click()
    page.keyboard.press("Control+a")
    page.keyboard.type(ref)
    page.keyboard.press("Enter")
    time.sleep(1.0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--modelo", type=int, required=True)
    ap.add_argument("--de", type=int, required=True)
    ap.add_argument("--ate", type=int, required=True)
    a = ap.parse_args()

    with sync_playwright() as pw:
        ctx = BrowserFactory.launch_persistent_context(pw, headless=True)
        ctx.grant_permissions(["clipboard-read", "clipboard-write"],
                              origin="https://docs.google.com")
        page = ctx.new_page()
        page.set_viewport_size({"width": 1600, "height": 1000})
        page.goto(SHEET_URL, wait_until="domcontentloaded", timeout=90000)
        time.sleep(10)

        goto(page, f"A{a.modelo}:E{a.modelo}")
        page.keyboard.press("Control+c")
        time.sleep(1.5)
        print(f"copiado A{a.modelo}:E{a.modelo}")

        goto(page, f"A{a.de}:E{a.ate}")
        page.keyboard.press("Control+Alt+v")   # colar somente formatação
        time.sleep(3)
        page.keyboard.press("Escape")
        time.sleep(4)
        page.screenshot(path=str(SHOT / "sheets_formato.png"))
        print(f"formatação aplicada em A{a.de}:E{a.ate}")
        ctx.close()


if __name__ == "__main__":
    main()
