#!/usr/bin/env python3
"""Verifica que un PDF de CV sea legible por ATS. El código decide, no el ojo.

Uso:
  python verificar_cv.py ruta/al/CV.pdf [--paginas 1] [--oferta Casos/<slug>/oferta.md]

Comprueba: texto extraíble, nº de páginas, títulos estándar, email y teléfono,
fechas Mes AAAA (ninguna solo con año), nº de palabras, caracteres raros y,
si se da la oferta, cobertura de palabras clave. Guarda el texto plano en
<pdf>-texto-ats.txt. Sale con 1 si hay fallos duros.
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

TITULOS = {
    "es": ["resumen", "experiencia", "proyectos", "educación", "educacion", "habilidades",
           "certificaciones", "idiomas", "perfil"],
    "en": ["summary", "experience", "work experience", "projects", "education", "skills",
           "certifications", "languages", "profile"],
}
MESES = (r"(ene|feb|mar|abr|may|jun|jul|ago|sep|sept|oct|nov|dic|"
         r"jan|apr|aug|dec|enero|febrero|marzo|abril|mayo|junio|julio|agosto|"
         r"septiembre|octubre|noviembre|diciembre|january|february|march|april|june|"
         r"july|august|september|october|november|december)\.?")
RESULTADOS = []


def chk(nombre, ok, detalle, duro=True):
    RESULTADOS.append((nombre, ok, detalle, duro))


def extraer(pdf: Path):
    try:
        from pypdf import PdfReader
    except ImportError:
        print("Falta pypdf: pip install pypdf", file=sys.stderr)
        sys.exit(2)
    r = PdfReader(str(pdf))
    paginas = [p.extract_text() or "" for p in r.pages]
    return paginas


def normal(s: str) -> str:
    return unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--paginas", type=int, default=1, help="máximo de páginas permitido")
    ap.add_argument("--oferta", help="oferta.md para medir cobertura de palabras clave")
    ap.add_argument("--carta", action="store_true", help="es una carta: omite chequeos de CV")
    a = ap.parse_args()

    pdf = Path(a.pdf)
    paginas = extraer(pdf)
    texto = "\n".join(paginas)
    Path(str(pdf.with_suffix("")) + "-texto-ats.txt").write_text(texto, encoding="utf-8")
    lineas = [l.strip() for l in texto.splitlines() if l.strip()]
    palabras = len(re.findall(r"\w+", texto))

    chk("texto extraíble", palabras > 80, f"{palabras} palabras extraídas")
    chk("páginas", len(paginas) <= a.paginas, f"{len(paginas)} (máx. {a.paginas})")
    chk("email en el cuerpo", bool(re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", texto)), "")
    chk("teléfono en el cuerpo", bool(re.search(r"\+?\d[\d\s().-]{7,}\d", texto)), "", duro=False)

    if not a.carta:
        idioma = "en" if re.search(r"\b(experience|education|skills)\b", texto, re.I) else "es"
        encontrados = [l for l in lineas if normal(l) in {normal(t) for t in TITULOS[idioma]}]
        chk("títulos estándar", len(encontrados) >= 3,
            f"{len(encontrados)} encontrados: {', '.join(encontrados) or 'ninguno'}")

        solo_anio = [l for l in lineas
                     if re.fullmatch(r"(19|20)\d{2}\s*[–—-]\s*((19|20)\d{2}|actualidad|present|presente)", l, re.I)]
        chk("fechas con mes", not solo_anio,
            "ok" if not solo_anio else "solo año en: " + " | ".join(solo_anio[:4]))
        con_mes = len(re.findall(MESES + r"\s+(19|20)\d{2}", texto, re.I))
        chk("fechas Mes AAAA presentes", con_mes >= 2, f"{con_mes} fechas con mes", duro=False)

        chk("longitud (350-700 palabras)", 350 <= palabras <= 700,
            f"{palabras} palabras; ideal ~475-600", duro=False)
        prohibidas = [p for p in ["responsable de", "encargado de", "apasionado", "orientado a resultados",
                                  "proactivo", "responsible for", "passionate", "results-driven",
                                  "team player", "detail-oriented", "synergy"]
                      if p in texto.lower()]
        chk("lenguaje prohibido", not prohibidas, ", ".join(prohibidas) or "ninguno", duro=False)

    raros = sorted({c for c in texto if ord(c) > 0x2400 and c not in "–—•·’“”"})
    chk("caracteres raros", not raros, "".join(raros) or "ninguno", duro=False)

    if a.oferta and Path(a.oferta).exists():
        oferta = normal(Path(a.oferta).read_text(encoding="utf-8"))
        cv = normal(texto)
        tech = set(re.findall(r"\b[a-z][a-z0-9.+#-]{1,20}\b", oferta))
        candidatas = [t for t in tech if re.search(r"[.+#]|js$|sql|api|aws|ui|ux|3d|ai|ml", t)
                      or t in {"react", "typescript", "javascript", "python", "unity", "blender", "figma",
                               "docker", "git", "node", "vue", "angular", "webgl", "threejs", "html", "css"}]
        faltan = sorted(t for t in candidatas if t not in cv)
        chk("palabras clave técnicas de la oferta", len(faltan) <= max(2, len(candidatas) // 4),
            f"faltan: {', '.join(faltan) or 'ninguna'} (de {len(candidatas)})", duro=False)

    duros = 0
    print(f"\nVerificación de {pdf.name}\n" + "-" * 48)
    for nombre, ok, detalle, duro in RESULTADOS:
        marca = "OK  " if ok else ("FALLO" if duro else "AVISO")
        if not ok and duro:
            duros += 1
        print(f"[{marca}] {nombre}" + (f" — {detalle}" if detalle else ""))
    print("-" * 48)
    print(f"Texto ATS guardado en: {pdf.with_suffix('')}-texto-ats.txt")
    print("RESULTADO: " + ("PASA" if duros == 0 else f"NO PASA ({duros} fallos duros)"))
    return 0 if duros == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
