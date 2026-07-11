#!/usr/bin/env python3
"""
List all sources from a NotebookLM notebook by scraping the source panel DOM.

Why this exists: ask_question.py uses RAG retrieval — it answers based on top-N
relevant docs, never the exhaustive list. For an audit, you need the REAL
inventory. This script opens the notebook with an authenticated browser, reads
the source panel DOM, and emits the full list as JSON.

Usage:
    python scripts/run.py list_sources.py --notebook-url URL [--out FILE]
    python scripts/run.py list_sources.py --notebook-id ID
"""
import argparse
import json
import sys
import time
from pathlib import Path

from patchright.sync_api import sync_playwright

# Add parent dir
sys.path.insert(0, str(Path(__file__).parent))

from auth_manager import AuthManager
from notebook_manager import NotebookLibrary
from browser_utils import BrowserFactory


def list_sources(notebook_url: str, headless: bool = True) -> list:
    """Return list of source titles for the given notebook URL."""
    auth = AuthManager()
    if not auth.is_authenticated():
        print("⚠️ Not authenticated. Run: python scripts/run.py auth_manager.py setup", file=sys.stderr)
        return []

    print(f"📚 Notebook: {notebook_url}", file=sys.stderr)

    with sync_playwright() as p:
        ctx = BrowserFactory.launch_persistent_context(p, headless=headless)
        page = ctx.new_page()
        # Wide viewport so source panel renders (it collapses in narrow viewports)
        page.set_viewport_size({"width": 1920, "height": 1200})

        page.goto(notebook_url, wait_until="domcontentloaded", timeout=30000)
        try:
            page.wait_for_url(lambda u: "notebooklm.google.com/notebook" in u, timeout=15000)
        except Exception:
            pass

        # Wait for source panel + content to render
        print("  ⏳ Waiting for source panel to load...", file=sys.stderr)
        try:
            page.wait_for_selector("source-picker mat-checkbox.select-checkbox", timeout=30000)
        except Exception as e:
            print(f"  ⚠️ Timed out waiting for source panel: {e}", file=sys.stderr)

        # Give Angular a moment to populate all entries
        time.sleep(3)

        # Extract source titles from aria-labels of per-source checkboxes
        titles = page.evaluate("""
        () => {
          const checkboxes = document.querySelectorAll(
            'mat-checkbox.select-checkbox input[aria-label]'
          );
          return Array.from(checkboxes).map(cb => cb.getAttribute('aria-label'));
        }
        """)

        ctx.close()
        return titles or []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--notebook-url", help="Full notebook URL")
    parser.add_argument("--notebook-id", help="Notebook ID from library")
    parser.add_argument("--out", help="Optional output file (JSON)")
    parser.add_argument("--show-browser", action="store_true", help="Disable headless")
    args = parser.parse_args()

    url = args.notebook_url
    if not url:
        if not args.notebook_id:
            lib = NotebookLibrary()
            active = lib.get_active_notebook()
            if not active:
                print("⚠️ No notebook URL provided and no active notebook in library", file=sys.stderr)
                return 1
            url = active.get("url")
        else:
            lib = NotebookLibrary()
            nb = lib.get_notebook(args.notebook_id)
            if not nb:
                print(f"⚠️ Notebook id not found: {args.notebook_id}", file=sys.stderr)
                return 1
            url = nb.get("url")

    titles = list_sources(url, headless=not args.show_browser)

    print(f"\n📊 Found {len(titles)} sources\n", file=sys.stderr)

    if args.out:
        with open(args.out, "w") as f:
            json.dump(titles, f, ensure_ascii=False, indent=2)
        print(f"💾 Wrote {args.out}", file=sys.stderr)
    else:
        for i, t in enumerate(titles, 1):
            print(f"{i:3d}. {t}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
