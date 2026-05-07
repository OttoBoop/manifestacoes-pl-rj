#!/usr/bin/env python3
"""
extract_pl_camara.py — Busca texto de PL no site da Câmara Municipal RJ

Workaround para PDFs escaneados (pdftotext falha):
- Navega camara.rio via Playwright
- Busca pelo número do PL
- Extrai texto do projeto de lei
- Salva em pasta PL-{NUM}-{ANO}/texto_extraido.md

Uso:
    python3 extract_pl_camara.py --pl 1840/2026
    python3 extract_pl_camara.py --pl 1840/2026 --output /caminho/saida.md
"""

import argparse
import asyncio
import re
import sys
from pathlib import Path

try:
    from patchright.async_api import async_playwright
except ImportError:
    print("patchright não encontrado. Tentando playwright...")
    from playwright.async_api import async_playwright


CAMARA_SEARCH_URL = "https://www.camara.rio/atividade-parlamentar/processo-legislativo/pl"
NOTICIAS_URL = "https://www.camara.rio/comunicacao/noticias"


async def buscar_pl(pl_numero: str, output_path: Path | None = None) -> str | None:
    """Busca o texto de um PL no site da Câmara RJ."""
    # Normaliza: "1840/2026" → numero=1840, ano=2026
    match = re.match(r"(\d+)[/.-](\d{4})", pl_numero)
    if not match:
        print(f"Formato inválido: {pl_numero}. Use 1840/2026")
        return None

    num, ano = match.group(1), match.group(2)
    print(f"Buscando PL {num}/{ano} em camara.rio...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        )
        page = await ctx.new_page()

        try:
            # Estratégia 1: busca via URL de notícias
            search_url = f"{NOTICIAS_URL}?search=PL+{num}%2F{ano}"
            await page.goto(search_url, timeout=15000, wait_until="domcontentloaded")
            await page.wait_for_timeout(2000)

            # Procura links com o número do PL
            links = await page.query_selector_all(f"a[href*='{num}']")
            pl_link = None
            for link in links:
                text = await link.inner_text()
                href = await link.get_attribute("href")
                if any(x in (text + (href or "")).lower() for x in [num, f"pl {num}"]):
                    pl_link = href
                    print(f"  Link encontrado: {href}")
                    break

            # Estratégia 2: busca direta com slug provável
            if not pl_link:
                slug_url = f"{NOTICIAS_URL}?search={num}"
                await page.goto(slug_url, timeout=15000, wait_until="domcontentloaded")
                await page.wait_for_timeout(2000)
                links = await page.query_selector_all("a.catItemTitle, a.itemTitle, h2 a, h3 a")
                for link in links:
                    text = await link.inner_text()
                    href = await link.get_attribute("href")
                    if num in (text + (href or "")):
                        pl_link = href
                        print(f"  Link (estratégia 2): {href}")
                        break

            if not pl_link:
                print(f"  PL {num}/{ano} não encontrado em notícias. Tentando busca geral...")
                await page.goto(
                    f"https://www.camara.rio/search?searchword=PL+{num}%2F{ano}",
                    timeout=15000, wait_until="domcontentloaded"
                )
                await page.wait_for_timeout(2000)
                content = await page.content()
                urls = re.findall(r'href="(https?://www\.camara\.rio[^"]*)"', content)
                for u in urls:
                    if num in u:
                        pl_link = u
                        print(f"  Link (busca geral): {u}")
                        break

            if not pl_link:
                print(f"  Não foi possível localizar PL {num}/{ano} em camara.rio")
                await browser.close()
                return None

            # Navega para a página do PL
            if not pl_link.startswith("http"):
                pl_link = f"https://www.camara.rio{pl_link}"

            await page.goto(pl_link, timeout=15000, wait_until="domcontentloaded")
            await page.wait_for_timeout(2000)

            # Extrai o conteúdo principal
            content_el = await page.query_selector(
                "div.itemFullText, div.catItemBody, article, main, div#content"
            )
            if content_el:
                text = await content_el.inner_text()
            else:
                text = await page.inner_text("body")

            # Limpa e formata
            lines = [l.strip() for l in text.split("\n") if l.strip()]
            output_text = f"# PL nº {num}/{ano} — Câmara Municipal RJ\n\n"
            output_text += f"**Fonte:** {pl_link}\n\n---\n\n"
            output_text += "\n".join(lines)

            if output_path:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(output_text, encoding="utf-8")
                print(f"  Salvo em: {output_path}")

            print(f"  Extraídos {len(lines)} parágrafos / {len(output_text)} chars")
            await browser.close()
            return output_text

        except Exception as e:
            print(f"  Erro: {e}")
            await browser.close()
            return None


def main():
    parser = argparse.ArgumentParser(description="Extrai texto de PL do site da Câmara RJ")
    parser.add_argument("--pl", required=True, help="Número do PL (ex: 1840/2026)")
    parser.add_argument("--output", help="Caminho de saída .md (opcional)")
    args = parser.parse_args()

    output = Path(args.output) if args.output else None
    result = asyncio.run(buscar_pl(args.pl, output))
    if not result:
        sys.exit(1)


if __name__ == "__main__":
    main()
