#!/usr/bin/env python3
"""
nb_create_notebook.py — Cria um novo notebook no NotebookLM via browser automation.

Uso:
    python nb_create_notebook.py --title "PL-1904-2026 — Atendimento bancário PcD/Idosos"
    python nb_create_notebook.py --title "..." [--out /tmp/novo_nb_url.txt]

Retorna a URL do notebook criado (copiada do URL da página ou via clipboard).
"""

import argparse
import sys
import time
import random
from pathlib import Path

NB_SKILL_DIR = Path.home() / ".claude" / "skills" / "notebooklm"
sys.path.insert(0, str(NB_SKILL_DIR / "scripts"))

_venv_site = NB_SKILL_DIR / ".venv" / "lib"
if _venv_site.exists():
    for _py in sorted(_venv_site.iterdir()):
        _sp = _py / "site-packages"
        if _sp.exists():
            sys.path.insert(0, str(_sp))
            break

from patchright.sync_api import sync_playwright

STATE_FILE = NB_SKILL_DIR / "data" / "browser_state" / "state.json"
BROWSER_PROFILE_DIR = NB_SKILL_DIR / "data" / "browser_state" / "browser_profile"
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
NB_HOME_URL = "https://notebooklm.google.com/"
BROWSER_ARGS = [
    '--disable-blink-features=AutomationControlled',
    '--disable-dev-shm-usage',
    '--no-sandbox',
    '--no-first-run',
]


def delay(min_ms=300, max_ms=800):
    time.sleep(random.uniform(min_ms / 1000, max_ms / 1000))


def create_notebook(title: str, out_file: Path | None = None) -> str | None:
    """Cria novo notebook no NB e retorna sua URL."""
    import json

    # Load cookies from existing auth
    cookies = []
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            cookies = json.load(f).get('cookies', [])

    playwright = sync_playwright().start()
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=str(BROWSER_PROFILE_DIR),
        executable_path="/usr/bin/chromium",
        headless=True,
        no_viewport=True,
        ignore_default_args=["--enable-automation"],
        user_agent=USER_AGENT,
        args=BROWSER_ARGS,
    )

    if cookies:
        context.add_cookies(cookies)

    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1200})

    print(f"🌐 Abrindo NotebookLM...")
    page.goto(NB_HOME_URL, wait_until="domcontentloaded")
    delay(2000, 3000)

    nb_url = None
    try:
        # Fechar modal se existir
        try:
            page.keyboard.press("Escape")
            delay(300, 500)
        except:
            pass

        # Procurar botão "Criar notebook" / "New notebook" / equivalente
        create_btn = None
        for selector in [
            'button:has-text("Criar notebook")',
            'button:has-text("New notebook")',
            'button:has-text("Novo notebook")',
            'button[aria-label*="Create"]',
            'button[aria-label*="Criar"]',
            'button[aria-label*="New notebook"]',
            'a:has-text("Criar notebook")',
            '[role="button"]:has-text("Criar")',
        ]:
            try:
                el = page.query_selector(selector)
                if el and el.is_visible():
                    create_btn = el
                    print(f"  ✓ Botão encontrado: {selector}")
                    break
            except:
                continue

        if not create_btn:
            # Debug: listar botões visíveis
            btns = page.query_selector_all("button, [role='button'], a")
            print("  DEBUG: botões/links disponíveis na página:")
            for b in btns[:20]:
                try:
                    txt = (b.inner_text() or "").strip()[:50]
                    aria = b.get_attribute("aria-label") or ""
                    href = b.get_attribute("href") or ""
                    if txt or aria:
                        print(f"    [{txt}] aria={aria} href={href[:40]}")
                except:
                    pass
            context.close()
            playwright.stop()
            return None

        create_btn.click(force=True)
        delay(2000, 3000)

        # Aguardar a URL mudar para o novo notebook (sair de /notebook/creating)
        page.wait_for_url("**/notebook/**", timeout=15000)
        # Esperar o /creating virar um UUID real (aumentado de 20s para 60s)
        nb_url = None
        for _ in range(60):
            current = page.url
            if "/notebook/creating" not in current and "/notebook/" in current:
                nb_url = current
                break
            time.sleep(1)
        if not nb_url:
            nb_url = page.url
            print(f"  ⚠️ URL ainda em /creating após 60s: {nb_url}")
        else:
            print(f"  ✅ Notebook criado: {nb_url}")

        # Se houver campo de título, preenchê-lo
        for selector in [
            'input[placeholder*="título"]',
            'input[placeholder*="Título"]',
            'input[aria-label*="título"]',
            '[contenteditable="true"][aria-label*="título"]',
        ]:
            try:
                el = page.query_selector(selector)
                if el and el.is_visible():
                    el.triple_click()
                    delay(200, 400)
                    page.keyboard.type(title)
                    page.keyboard.press("Enter")
                    delay(500, 800)
                    print(f"  ✓ Título definido: {title}")
                    break
            except:
                continue

    except Exception as e:
        print(f"  ❌ Erro: {e}")
    finally:
        context.close()
        playwright.stop()

    if nb_url and out_file:
        out_file.write_text(nb_url)
        print(f"  💾 URL salva em: {out_file}")

    return nb_url


def main():
    parser = argparse.ArgumentParser(description="Cria novo notebook no NotebookLM")
    parser.add_argument("--title", required=True, help="Título do notebook")
    parser.add_argument("--out", help="Arquivo para salvar a URL do notebook criado")
    args = parser.parse_args()

    out = Path(args.out) if args.out else None
    url = create_notebook(args.title, out)

    if url:
        print(f"\n📚 URL do novo notebook: {url}")
    else:
        print("❌ Falha ao criar notebook")
        sys.exit(1)


if __name__ == "__main__":
    main()
