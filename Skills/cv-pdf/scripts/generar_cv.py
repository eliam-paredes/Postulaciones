#!/usr/bin/env python3
"""Genera un PDF de CV (o carta) legible por ATS a partir de un cv.md.

Uso:
  python generar_cv.py Casos/<slug>/cv.md [--salida X.pdf] [--idioma es|en]
                       [--plantilla cv|carta] [--papel letter|a4] [--estilo ruta.css]
  python generar_cv.py --check      # comprueba requisitos

Imprime con Microsoft Edge / Google Chrome en modo headless (vienen con el
sistema) o, si no hay, con Playwright. Sin dependencias obligatorias.
"""
import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PLANTILLAS = AQUI.parent / "templates"


# ---------------------------------------------------------------- markdown → html
def inline(texto: str) -> str:
    t = html.escape(texto, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
               lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])", r"<em>\1</em>", t)
    return t


def md_a_html(md: str) -> str:
    lineas = md.replace("\r\n", "\n").split("\n")
    out, en_lista, en_bloque = [], False, False
    cabecera = 0       # líneas tras el h1 (titular, contacto)
    meta = 0           # líneas tras un h3 (organización, fechas)

    def cerrar_lista():
        nonlocal en_lista
        if en_lista:
            out.append("</ul>")
            en_lista = False

    def cerrar_bloque():
        nonlocal en_bloque
        cerrar_lista()
        if en_bloque:
            out.append("</div>")
            en_bloque = False

    for cruda in lineas:
        linea = cruda.rstrip()
        s = linea.strip()
        if s.startswith("<!--"):
            continue
        if not s:
            cerrar_lista()
            cabecera = 0
            meta = 0
            continue
        if s.startswith("# "):
            cerrar_bloque()
            out.append(f"<h1>{inline(s[2:].strip())}</h1>")
            cabecera = 1
            continue
        if s.startswith("## "):
            cerrar_bloque()
            cabecera = 0
            out.append(f"<h2>{inline(s[3:].strip())}</h2>")
            continue
        if s.startswith("### "):
            cerrar_bloque()
            cabecera = 0
            out.append('<div class="bloque">')
            en_bloque = True
            out.append(f"<h3>{inline(s[4:].strip())}</h3>")
            meta = 1
            continue
        if s.startswith(("- ", "* ")):
            meta = 0
            if not en_lista:
                out.append("<ul>")
                en_lista = True
            out.append(f"<li>{inline(s[2:].strip())}</li>")
            continue
        cerrar_lista()
        if cabecera == 1:
            out.append(f'<p class="titular">{inline(s)}</p>')
            cabecera = 2
            continue
        if cabecera == 2:
            out.append(f'<p class="contacto">{inline(s)}</p>')
            cabecera = 0
            continue
        if meta == 1:
            out.append(f'<p class="org">{inline(s)}</p>')
            meta = 2
            continue
        if meta == 2:
            out.append(f'<p class="fechas">{inline(s)}</p>')
            meta = 0
            continue
        out.append(f"<p>{inline(s)}</p>")
    cerrar_bloque()
    return "\n".join(out)


def construir_html(md: str, css: str, titulo: str, papel: str, idioma: str) -> str:
    extra = "@page { size: A4; }" if papel == "a4" else ""
    return (f'<!doctype html><html lang="{idioma}"><head><meta charset="utf-8">'
            f"<title>{html.escape(titulo)}</title><style>{css}\n{extra}</style></head>"
            f"<body>{md_a_html(md)}</body></html>")


# ---------------------------------------------------------------- navegador
def buscar_navegador():
    candidatos = []
    for var in ("PROGRAMFILES(X86)", "PROGRAMFILES", "LOCALAPPDATA"):
        base = os.environ.get(var)
        if base:
            candidatos += [Path(base) / "Microsoft/Edge/Application/msedge.exe",
                           Path(base) / "Google/Chrome/Application/chrome.exe"]
    candidatos += [Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
                   Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")]
    for c in candidatos:
        if c.exists():
            return str(c)
    for nombre in ("msedge", "microsoft-edge", "google-chrome", "chrome", "chromium",
                   "chromium-browser"):
        p = shutil.which(nombre)
        if p:
            return p
    return None


def imprimir_con_navegador(nav: str, html_path: Path, pdf_path: Path) -> bool:
    with tempfile.TemporaryDirectory() as perfil:
        cmd = [nav, "--headless=new", "--disable-gpu", "--no-first-run",
               "--no-pdf-header-footer", "--print-to-pdf-no-header",
               f"--user-data-dir={perfil}", f"--print-to-pdf={pdf_path.resolve()}",
               html_path.resolve().as_uri()]
        try:
            subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        except (subprocess.TimeoutExpired, OSError) as e:
            print(f"  aviso: el navegador falló ({e})", file=sys.stderr)
    return pdf_path.exists() and pdf_path.stat().st_size > 0


def imprimir_con_playwright(html_path: Path, pdf_path: Path) -> bool:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(html_path.resolve().as_uri())
        pg.pdf(path=str(pdf_path), prefer_css_page_size=True, print_background=True)
        b.close()
    return pdf_path.exists()


def check() -> int:
    ok = True
    nav = buscar_navegador()
    print(f"[{'OK' if nav else '--'}] Navegador para imprimir: {nav or 'no encontrado'}")
    try:
        import playwright  # noqa: F401
        print("[OK] Playwright instalado (alternativa)")
    except ImportError:
        print("[--] Playwright no instalado (opcional: pip install playwright && playwright install chromium)")
        ok = ok and bool(nav)
    try:
        import pypdf  # noqa: F401
        print("[OK] pypdf instalado (verificación)")
    except ImportError:
        print("[!!] Falta pypdf para verificar: pip install pypdf")
        ok = False
    return 0 if ok and nav else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("md", nargs="?")
    ap.add_argument("--salida")
    ap.add_argument("--idioma", default="es", choices=["es", "en"])
    ap.add_argument("--plantilla", default="cv", choices=["cv", "carta"])
    ap.add_argument("--papel", default="letter", choices=["letter", "a4"])
    ap.add_argument("--estilo")
    ap.add_argument("--nombre", default="Eliam-Paredes")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    if a.check:
        return check()
    if not a.md:
        ap.error("falta la ruta del cv.md")

    md_path = Path(a.md)
    md = md_path.read_text(encoding="utf-8")
    css_path = Path(a.estilo) if a.estilo else PLANTILLAS / f"{a.plantilla}.css"
    css = css_path.read_text(encoding="utf-8")

    if a.salida:
        pdf_path = Path(a.salida)
    else:
        sufijo = {"cv": {"es": "CV", "en": "Resume"},
                  "carta": {"es": "Carta", "en": "Cover-Letter"}}[a.plantilla][a.idioma]
        pdf_path = md_path.parent / f"{a.nombre}-{sufijo}.pdf"
    html_path = pdf_path.with_suffix(".html")
    titulo = pdf_path.stem.replace("-", " ")
    html_path.write_text(construir_html(md, css, titulo, a.papel, a.idioma), encoding="utf-8")
    if pdf_path.exists():
        pdf_path.unlink()

    nav = buscar_navegador()
    hecho = nav and imprimir_con_navegador(nav, html_path, pdf_path)
    if not hecho:
        hecho = imprimir_con_playwright(html_path, pdf_path)
    if not hecho:
        print("ERROR: no pude imprimir el PDF. Instala Edge/Chrome o Playwright "
              "(pip install playwright && playwright install chromium).", file=sys.stderr)
        return 1
    print(f"PDF generado: {pdf_path}")
    print(f"HTML intermedio: {html_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
