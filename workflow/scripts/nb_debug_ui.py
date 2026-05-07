#!/usr/bin/env python3
"""Debug: abre NB, clica Add source e dump o HTML da página para inspecionar seletores."""
import sys, json, time, random
from pathlib import Path

NB_SKILL_DIR = Path.home() / ".claude" / "skills" / "notebooklm"
sys.path.insert(0, str(NB_SKILL_DIR / "scripts"))

from patchright.sync_api import sync_playwright

STATE_FILE = NB_SKILL_DIR / "data" / "browser_state" / "state.json"
BROWSER_PROFILE_DIR = NB_SKILL_DIR / "data" / "browser_state" / "browser_profile"

NB_URL = "https://notebooklm.google.com/notebook/192029b0-017e-4bfa-85f0-b6fa25a28b8e"

def load_cookies():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f).get('cookies', [])
    return []

pw = sync_playwright().start()
ctx = pw.chromium.launch_persistent_context(
    user_data_dir=str(BROWSER_PROFILE_DIR),
    executable_path="/usr/bin/chromium",
    headless=True,
    no_viewport=True,
    ignore_default_args=["--enable-automation"],
    args=['--disable-blink-features=AutomationControlled','--no-sandbox'],
)
ctx.add_cookies(load_cookies())
page = ctx.new_page()
page.set_viewport_size({"width": 1920, "height": 1200})
page.goto(NB_URL, wait_until="domcontentloaded")
time.sleep(3)

# Screenshot 1: estado inicial
page.screenshot(path="/tmp/nb_debug_1_initial.png")
print("Screenshot 1: estado inicial")

# Dump botões visíveis
buttons = page.query_selector_all("button")
print(f"\nBotões encontrados ({len(buttons)}):")
for b in buttons[:30]:
    try:
        txt = b.inner_text().strip()[:60]
        aria = b.get_attribute("aria-label") or ""
        cls = b.get_attribute("class") or ""
        vis = b.is_visible()
        if vis:
            print(f"  [vis] text='{txt}' aria='{aria}' class='{cls[:40]}'")
    except: pass

# Screenshot 2: tentar clicar primeiro botão de add
for selector in [
    'button[aria-label="Add source"]',
    'button:has-text("Add source")',
    'button[aria-label*="add"]',
    'button.add-source',
    '[data-source-action]',
]:
    try:
        el = page.query_selector(selector)
        if el and el.is_visible():
            print(f"\n✅ Encontrou botão Add: {selector}")
            el.click(force=True)
            time.sleep(2)
            page.screenshot(path="/tmp/nb_debug_2_after_add_click.png")
            print("Screenshot 2: após clicar Add source")

            # Dump HTML do overlay/modal que apareceu
            overlay = page.query_selector('.cdk-overlay-container')
            if overlay:
                html = overlay.inner_html()
                Path("/tmp/nb_debug_overlay.html").write_text(html)
                print(f"Overlay HTML salvo em /tmp/nb_debug_overlay.html ({len(html)} chars)")

            # Dump todos os inputs visíveis
            inputs = page.query_selector_all("input, textarea")
            print(f"\nInputs ({len(inputs)}):")
            for inp in inputs:
                try:
                    if inp.is_visible():
                        t = inp.get_attribute("type") or ""
                        ph = inp.get_attribute("placeholder") or ""
                        aria = inp.get_attribute("aria-label") or ""
                        print(f"  [vis] type={t} placeholder='{ph}' aria='{aria}'")
                except: pass
            break
    except Exception as e:
        print(f"  {selector}: {e}")

ctx.close()
pw.stop()
print("\nDebug concluído.")
