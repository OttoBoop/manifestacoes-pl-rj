#!/usr/bin/env python3
"""
nb_add_source.py — Adiciona fontes URL a um notebook NotebookLM via browser automation.

Reutiliza auth e browser profile da skill notebooklm original (não modifica a skill).
Criado como workaround para ausência de script de adição de fontes na skill original.

Uso:
    python nb_add_source.py --notebook-url URL --sources urls.txt
    python nb_add_source.py --notebook-url URL --url "https://..."
"""

import argparse
import sys
import time
import json
import random
from pathlib import Path

# Reutiliza configs da skill notebooklm sem modificar nada dela
NB_SKILL_DIR = Path.home() / ".claude" / "skills" / "notebooklm"
sys.path.insert(0, str(NB_SKILL_DIR / "scripts"))

from patchright.sync_api import sync_playwright

STATE_FILE = NB_SKILL_DIR / "data" / "browser_state" / "state.json"
BROWSER_PROFILE_DIR = NB_SKILL_DIR / "data" / "browser_state" / "browser_profile"
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
BROWSER_ARGS = [
    '--disable-blink-features=AutomationControlled',
    '--disable-dev-shm-usage',
    '--no-sandbox',
    '--no-first-run',
]


def load_cookies():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            state = json.load(f)
            return state.get('cookies', [])
    return []


def delay(min_ms=300, max_ms=800):
    time.sleep(random.uniform(min_ms / 1000, max_ms / 1000))


def ensure_sources_panel_open(page):
    """Garante que o painel de fontes está aberto (visível com botão Adicionar fonte)."""
    # Se já existe botão "Adicionar fontes" visível, painel já está aberto
    btn = page.query_selector('button[aria-label="Adicionar fonte"]')
    if btn and btn.is_visible():
        return True
    # Tentar abrir via botão alternativo
    for selector in ['button:has-text("Adicionar fontes")', 'button[aria-label*="fonte"]']:
        try:
            el = page.query_selector(selector)
            if el and el.is_visible():
                el.click(force=True)
                delay(800, 1200)
                return True
        except:
            continue
    return False


def add_url_source(page, url: str) -> bool:
    """Adiciona uma URL como fonte ao notebook — NB em pt-BR."""
    print(f"  ➕ Adicionando: {url}")
    try:
        # Garantir painel aberto
        ensure_sources_panel_open(page)

        # Clicar em "Sites" (botão que abre o input de URL)
        sites_btn = None
        for selector in [
            'button.drop-zone-button:has-text("Sites")',
            'button:has-text("Sites")',
            'button[aria-label*="Sites"]',
            'button[aria-label*="site"]',
        ]:
            try:
                el = page.query_selector(selector)
                if el and el.is_visible():
                    sites_btn = el
                    break
            except:
                continue

        if not sites_btn:
            # Tentar clicar no botão "Adicionar fontes" primeiro para abrir o modal
            add_btn = page.query_selector('button[aria-label="Adicionar fonte"]')
            if add_btn:
                add_btn.click(force=True)
                delay(800, 1200)
                # Tentar Sites novamente
                for selector in ['button:has-text("Sites")', 'button:has-text("site")']:
                    try:
                        el = page.query_selector(selector)
                        if el and el.is_visible():
                            sites_btn = el
                            break
                    except:
                        continue

        if not sites_btn:
            print("  ❌ Botão 'Sites' não encontrado")
            return False

        sites_btn.click(force=True)
        delay(600, 1000)

        # Encontrar campo de URL
        url_input = None
        for selector in [
            'input[type="url"]',
            'input[placeholder*="URL"]',
            'input[placeholder*="url"]',
            'input[placeholder*="http"]',
            'input[placeholder*="sites"]',
            'input[placeholder*="Sites"]',
            'textarea[placeholder*="URL"]',
        ]:
            try:
                inp = page.query_selector(selector)
                if inp and inp.is_visible():
                    url_input = inp
                    break
            except:
                continue

        # Se não encontrou por placeholder, tentar qualquer input visível no overlay
        if not url_input:
            inputs = page.query_selector_all('.cdk-overlay-container input, .cdk-overlay-container textarea')
            for inp in inputs:
                try:
                    if inp.is_visible():
                        url_input = inp
                        break
                except:
                    continue

        if not url_input:
            print("  ❌ Campo de URL não encontrado após clicar Sites")
            page.keyboard.press("Escape")
            delay(300, 500)
            return False

        url_input.click(force=True)
        delay(200, 400)
        page.keyboard.type(url)
        delay(300, 500)

        # Confirmar
        for selector in [
            'button:has-text("Inserir")',
            'button:has-text("Insert")',
            'button:has-text("Adicionar")',
            'button[type="submit"]',
        ]:
            try:
                btn = page.query_selector(selector)
                if btn and btn.is_visible():
                    btn.click(force=True)
                    delay(2000, 3000)
                    print(f"  ✅ Enviada, indexando...")
                    return True
            except:
                continue

        page.keyboard.press("Enter")
        delay(2000, 3000)
        print(f"  ✅ Enviada via Enter, indexando...")
        return True

    except Exception as e:
        print(f"  ❌ Erro: {e}")
        return False


def add_sources_to_notebook(notebook_url: str, urls: list[str]) -> dict:
    """
    Abre o notebook e adiciona múltiplas URLs como fontes.
    Retorna dict com resultados por URL.
    """
    results = {}

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

    cookies = load_cookies()
    if cookies:
        context.add_cookies(cookies)

    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1200})

    print(f"🌐 Abrindo notebook...")
    page.goto(notebook_url, wait_until="domcontentloaded")
    delay(2000, 3000)

    # Fechar modal inicial se existir
    try:
        page.keyboard.press("Escape")
        delay(500, 800)
    except:
        pass

    for url in urls:
        success = add_url_source(page, url)
        results[url] = success
        if success:
            # Aguardar indexação antes da próxima fonte
            time.sleep(3)

    context.close()
    playwright.stop()

    return results


def main():
    parser = argparse.ArgumentParser(description="Adiciona fontes URL ao NotebookLM")
    parser.add_argument("--notebook-url", required=True, help="URL do notebook NotebookLM")
    parser.add_argument("--url", help="URL única a adicionar")
    parser.add_argument("--sources", help="Arquivo .txt com uma URL por linha")
    args = parser.parse_args()

    urls = []
    if args.url:
        urls.append(args.url)
    if args.sources:
        with open(args.sources) as f:
            urls.extend(line.strip() for line in f if line.strip())

    if not urls:
        print("❌ Forneça --url ou --sources")
        sys.exit(1)

    print(f"📚 Notebook: {args.notebook_url}")
    print(f"🔗 {len(urls)} fonte(s) a adicionar")

    results = add_sources_to_notebook(args.notebook_url, urls)

    success = sum(1 for v in results.values() if v)
    failed = sum(1 for v in results.values() if not v)

    print(f"\n📊 Resultado: {success} ✅  {failed} ❌")
    for url, ok in results.items():
        print(f"  {'✅' if ok else '❌'} {url}")

    # Salvar resultado como JSON para o log
    out = Path("/tmp/nb_add_source_result.json")
    out.write_text(json.dumps(results, indent=2))
    print(f"\n💾 Resultado salvo em {out}")


if __name__ == "__main__":
    main()
