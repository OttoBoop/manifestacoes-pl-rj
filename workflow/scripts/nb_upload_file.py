#!/usr/bin/env python3
"""
nb_upload_file.py — Faz upload de arquivo local (PDF, DOCX, TXT) ao NotebookLM.

Workaround W-4: PDFs escaneados não podem ser extraídos com pdftotext.
O NotebookLM (Gemini) faz OCR interno ao processar o PDF — então basta subir o arquivo.

Uso:
    python nb_upload_file.py --notebook-url URL --file /caminho/arquivo.pdf
    python nb_upload_file.py --notebook-url URL --files lista_arquivos.txt
"""

import argparse
import sys
import time
import json
import random
from pathlib import Path

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


def upload_file(page, file_path: Path) -> bool:
    """Faz upload de arquivo local ao notebook — NB em pt-BR."""
    if not file_path.exists():
        print(f"  ❌ Arquivo não encontrado: {file_path}")
        return False

    print(f"  📎 Enviando: {file_path.name} ({file_path.stat().st_size // 1024} KB)")
    try:
        # Garantir painel de fontes aberto
        for selector in [
            'button[aria-label="Adicionar fonte"]',
            'button:has-text("Adicionar fontes")',
            'button:has-text("Adicionar fonte")',
        ]:
            btn = page.query_selector(selector)
            if btn and btn.is_visible():
                btn.click(force=True)
                delay(800, 1200)
                break

        # Clicar em "Upload" / "Fazer upload" / equivalente em pt-BR
        upload_btn = None
        for selector in [
            'button:has-text("Fazer upload")',
            'button:has-text("Upload")',
            'button:has-text("Carregar")',
            'button[aria-label*="upload"]',
            'button[aria-label*="Upload"]',
            'button[aria-label*="arquivo"]',
            'mat-list-item:has-text("Upload")',
            'mat-list-item:has-text("Fazer upload")',
            '[role="menuitem"]:has-text("Upload")',
            '[role="menuitem"]:has-text("Fazer upload")',
            '[role="option"]:has-text("Upload")',
        ]:
            try:
                el = page.query_selector(selector)
                if el and el.is_visible():
                    upload_btn = el
                    break
            except:
                continue

        if not upload_btn:
            # Debug: listar botões/opções visíveis no overlay
            all_btns = page.query_selector_all('.cdk-overlay-container button, .cdk-overlay-container [role="menuitem"], .cdk-overlay-container [role="option"]')
            print("  DEBUG: opções disponíveis no overlay:")
            for b in all_btns[:15]:
                try:
                    txt = b.inner_text().strip()
                    aria = b.get_attribute("aria-label") or ""
                    if txt or aria:
                        print(f"    [{txt}] aria={aria}")
                except:
                    pass

            # Tentar drop-zone-button (mesmo padrão do nb_add_source)
            btns = page.query_selector_all('.drop-zone-button')
            for b in btns:
                txt = (b.inner_text() or "").strip()
                aria = b.get_attribute("aria-label") or ""
                combined = (txt + aria).lower()
                if any(kw in combined for kw in ["upload", "carregar", "arquivo", "file"]):
                    upload_btn = b
                    print(f"  Encontrado via drop-zone: [{txt}]")
                    break

        if not upload_btn:
            print("  ❌ Botão de upload não encontrado. Use --show-browser para debug.")
            return False

        # Interceptar file chooser antes de clicar
        with page.expect_file_chooser(timeout=5000) as fc_info:
            upload_btn.click(force=True)

        file_chooser = fc_info.value
        file_chooser.set_files(str(file_path))
        print(f"  📤 Arquivo selecionado no chooser")
        delay(3000, 5000)

        # Aguardar indexação (barra de progresso desaparecer ou status de sucesso)
        for _ in range(30):
            # Verificar se apareceu confirmação de upload
            success_indicators = [
                'mat-icon:has-text("check_circle")',
                '*:has-text("indexado")',
                '*:has-text("processado")',
                '*:has-text("adicionado")',
            ]
            for sel in success_indicators:
                try:
                    el = page.query_selector(sel)
                    if el and el.is_visible():
                        print(f"  ✅ Upload confirmado")
                        return True
                except:
                    pass
            time.sleep(2)

        print(f"  ⚠️ Upload enviado, aguardando indexação (sem confirmação visual capturada)")
        return True

    except Exception as e:
        print(f"  ❌ Erro: {e}")
        return False


def upload_files_to_notebook(notebook_url: str, files: list[Path]) -> dict:
    """Abre o notebook e faz upload de múltiplos arquivos."""
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

    try:
        page.keyboard.press("Escape")
        delay(500, 800)
    except:
        pass

    for f in files:
        success = upload_file(page, f)
        results[str(f)] = success
        if success:
            time.sleep(5)  # Aguarda indexação entre uploads

    context.close()
    playwright.stop()

    return results


def main():
    parser = argparse.ArgumentParser(description="Faz upload de arquivo ao NotebookLM")
    parser.add_argument("--notebook-url", required=True, help="URL do notebook NotebookLM")
    parser.add_argument("--file", help="Caminho do arquivo a subir")
    parser.add_argument("--files", help="Arquivo .txt com um caminho por linha")
    args = parser.parse_args()

    files = []
    if args.file:
        files.append(Path(args.file))
    if args.files:
        with open(args.files) as f:
            files.extend(Path(l.strip()) for l in f if l.strip())

    if not files:
        print("❌ Forneça --file ou --files")
        sys.exit(1)

    print(f"📚 Notebook: {args.notebook_url}")
    print(f"📂 {len(files)} arquivo(s) a enviar")

    results = upload_files_to_notebook(args.notebook_url, files)

    success = sum(1 for v in results.values() if v)
    failed = sum(1 for v in results.values() if not v)

    print(f"\n📊 Resultado: {success} ✅  {failed} ❌")
    for path, ok in results.items():
        print(f"  {'✅' if ok else '❌'} {path}")

    out = Path("/tmp/nb_upload_result.json")
    out.write_text(json.dumps(results, indent=2))
    print(f"\n💾 Resultado salvo em {out}")


if __name__ == "__main__":
    main()
