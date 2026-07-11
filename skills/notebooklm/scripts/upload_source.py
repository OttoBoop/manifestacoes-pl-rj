#!/usr/bin/env python3
"""Upload a local file as a new source to a NotebookLM notebook.

Why this exists: ask_question.py is read-only; new sources must be added before
RAG retrieval can use them. For audits where the case NB lacks key documents
(SIDRA tables, doc canônico, etc.), we need to add them programmatically.

Usage:
    python scripts/run.py upload_source.py \
        --notebook-url URL --file PATH [--show-browser]
"""
import argparse
import sys
import time
from pathlib import Path

from patchright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).parent))
from auth_manager import AuthManager
from browser_utils import BrowserFactory


def upload_source(notebook_url: str, file_path: str, headless: bool = True) -> bool:
    auth = AuthManager()
    if not auth.is_authenticated():
        print("⚠️ Not authenticated.", file=sys.stderr)
        return False

    fp = Path(file_path).expanduser().resolve()
    if not fp.exists():
        print(f"❌ File not found: {fp}", file=sys.stderr)
        return False

    print(f"📁 File: {fp} ({fp.stat().st_size} bytes)", file=sys.stderr)
    print(f"📚 Notebook: {notebook_url}", file=sys.stderr)

    with sync_playwright() as p:
        ctx = BrowserFactory.launch_persistent_context(p, headless=headless)
        page = ctx.new_page()
        page.set_viewport_size({"width": 1920, "height": 1200})

        page.goto(notebook_url, wait_until="domcontentloaded", timeout=30000)
        try:
            page.wait_for_url(lambda u: "notebooklm.google.com/notebook" in u, timeout=15000)
        except Exception:
            pass

        # Wait for source panel
        try:
            page.wait_for_selector("source-picker", timeout=30000)
        except Exception as e:
            print(f"  ⚠️ Source panel not found: {e}", file=sys.stderr)
            ctx.close()
            return False
        time.sleep(2)

        # Click "Add source" — typical labels in NB UI
        add_clicked = False
        candidates = [
            'button[aria-label*="Add" i]',
            'button[aria-label*="Adicionar" i]',
            'button:has-text("Add source")',
            'button:has-text("Adicionar fonte")',
            'button:has-text("+ Add")',
            'mat-icon:has-text("add")',
        ]
        for sel in candidates:
            try:
                el = page.locator(sel).first
                if el.count() > 0 and el.is_visible(timeout=2000):
                    el.click()
                    print(f"  ✓ Clicked Add button: {sel}", file=sys.stderr)
                    add_clicked = True
                    break
            except Exception:
                continue
        if not add_clicked:
            print("  ❌ Couldn't find Add source button.", file=sys.stderr)
            print("     Trying ESC + retry on visible buttons...", file=sys.stderr)
            # Listar todos os botões visíveis para debug
            btns = page.evaluate("""
                () => Array.from(document.querySelectorAll('button')).filter(b => b.offsetParent !== null).map(b => ({
                    text: (b.innerText||'').slice(0,60),
                    aria: b.getAttribute('aria-label') || '',
                }))
            """)
            for b in btns[:30]:
                print(f"      btn: text={b['text']!r} aria={b['aria']!r}", file=sys.stderr)
            ctx.close()
            return False

        # Wait for upload dialog
        time.sleep(2)

        # NB v2025 dialog: precisa clicar/ativar opção "Upload file" antes do file input aparecer
        # ou o input já está no DOM mas hidden. Tentar várias rotas:
        for sel in ['button:has-text("Upload")', 'button:has-text("Carregar")', 'button:has-text("PDF")',
                    'div[aria-label*="Upload" i]', 'div[role="button"]:has-text("Upload")',
                    'button:has-text("file")']:
            try:
                el = page.locator(sel).first
                if el.count() > 0 and el.is_visible(timeout=1000):
                    el.click()
                    print(f"  ✓ Clicked Upload option: {sel}", file=sys.stderr)
                    time.sleep(1.5)
                    break
            except Exception:
                continue

        # Find file input — try all on page including hidden ones
        file_input = None
        for sel in ['input[type="file"]', 'input[accept]']:
            try:
                els = page.locator(sel)
                count = els.count()
                if count > 0:
                    file_input = els.first
                    print(f"  ✓ Found {count} file input(s) ({sel})", file=sys.stderr)
                    break
            except Exception:
                continue
        if file_input is None:
            print("  ❌ No file input found in dialog. Dumping visible UI:", file=sys.stderr)
            btns = page.evaluate("""
                () => Array.from(document.querySelectorAll('button, [role=button], a')).filter(b => b.offsetParent !== null).map(b => ({
                    tag: b.tagName,
                    text: (b.innerText||'').slice(0,80),
                    aria: b.getAttribute('aria-label') || '',
                }))
            """)
            for b in btns[:40]:
                print(f"      {b['tag']}: text={b['text']!r} aria={b['aria']!r}", file=sys.stderr)
            ctx.close()
            return False

        # Set the file
        file_input.set_input_files(str(fp))
        print(f"  ✓ File uploaded: {fp.name}", file=sys.stderr)

        # Wait for processing — short window since uploads são confirmados via list_sources fora
        print("  ⏳ Waiting for NB to register source (up to 15s)...", file=sys.stderr)
        time.sleep(3)
        end = time.time() + 15
        baseline = None
        while time.time() < end:
            try:
                count = page.evaluate("""
                    () => document.querySelectorAll('mat-checkbox.select-checkbox input').length
                """)
                if baseline is None:
                    baseline = count
                elif count > baseline:
                    print(f"  ✓ Source count went from {baseline} → {count}", file=sys.stderr)
                    break
            except Exception:
                pass
            time.sleep(1)
        else:
            # Não é warning crítico — count check em panel renderiza com delay; o upload em si funciona
            print("  ↻ panel count delay (upload provavelmente OK; valida via list_sources)", file=sys.stderr)

        ctx.close()
        return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--notebook-url", required=True)
    parser.add_argument("--file", required=True)
    parser.add_argument("--show-browser", action="store_true")
    args = parser.parse_args()

    ok = upload_source(args.notebook_url, args.file, headless=not args.show_browser)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
