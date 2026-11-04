"""Puntua las 8 variantes de CV/variantes/ (y el cv_total.md) contra los
requisitos de una oferta. El calculo lo hace el codigo, no el modelo.

Uso:
    python Herramientas/puntuar_variantes.py Casos/<slug>/requisitos.md --idioma es
    python Herramientas/puntuar_variantes.py Casos/<slug>/requisitos.md --idioma en --todas

Formato de requisitos.md (una linea por requisito; los sinonimos van con |):

    ## Must-have
    - React | React.js | ReactJS
    - Git | GitHub
    ## Nice-to-have
    - Three.js | WebGL

Regla de puntuacion (la de CLAUDE.md):
    must-have = 2 puntos, nice-to-have = 1 punto.
    Cumple (aparece en Resumen, Experiencia, Proyectos o Educacion) = 100 %.
    Parcial (solo en el titular o en Habilidades) = 50 %.
    No aparece = 0 %.
    Encaje = puntos obtenidos / puntos posibles.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
VARIANTES = RAIZ / "CV" / "variantes"
MAESTRO = RAIZ / "CV" / "cv_total.md"

# Secciones que solo "declaran" una habilidad (cuentan como parcial).
SECCIONES_PARCIALES = {
    "habilidades", "skills", "idiomas", "languages",
    "banco-de-palabras-clave", "aparcado",
}
UMBRAL = 80


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def leer_requisitos(ruta: Path) -> list[tuple[str, int, list[str]]]:
    """Devuelve [(nombre, peso, sinonimos)]."""
    reqs, peso = [], None
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        l = linea.strip()
        ln = normalizar(l)
        if l.startswith("#"):
            if "must" in ln or "imprescindible" in ln or "obligatorio" in ln:
                peso = 2
            elif "nice" in ln or "deseable" in ln or "valorable" in ln:
                peso = 1
            else:
                peso = None
            continue
        if peso and re.match(r"^[-*]\s+", l):
            cuerpo = re.sub(r"^[-*]\s+", "", l)
            cuerpo = cuerpo.split("#")[0].strip()  # permite comentarios con #
            sinonimos = [s.strip() for s in cuerpo.split("|") if s.strip()]
            if sinonimos:
                reqs.append((sinonimos[0], peso, sinonimos))
    return reqs


def partir_cv(texto: str) -> tuple[str, str]:
    """Separa el texto en (evidencia fuerte, evidencia parcial)."""
    texto = re.sub(r"<!--.*?-->", " ", texto, flags=re.S)
    fuerte, parcial = [], []
    lineas = texto.splitlines()
    # Titular (linea 2 de un cv.md) = parcial.
    if len(lineas) > 1 and lineas[0].startswith("# "):
        parcial.append(lineas[1])
        lineas = lineas[2:]
    destino = fuerte
    for linea in lineas:
        if linea.startswith("## "):
            nombre = normalizar(linea[3:].strip())
            destino = parcial if nombre in SECCIONES_PARCIALES else fuerte
            continue
        destino.append(linea)
    return normalizar("\n".join(fuerte)), normalizar("\n".join(parcial))


def aparece(termino: str, texto: str) -> bool:
    t = re.escape(normalizar(termino))
    return re.search(rf"(?<![\w]){t}(?![\w])", texto) is not None


def puntuar(texto: str, reqs) -> tuple[float, list[str], list[str]]:
    fuerte, parcial = partir_cv(texto)
    obtenidos = posibles = 0.0
    huecos, parciales = [], []
    for nombre, peso, sinonimos in reqs:
        posibles += peso
        if any(aparece(s, fuerte) for s in sinonimos):
            obtenidos += peso
        elif any(aparece(s, parcial) for s in sinonimos):
            obtenidos += peso * 0.5
            parciales.append(nombre)
        else:
            huecos.append(nombre)
    pct = 100 * obtenidos / posibles if posibles else 0
    return pct, parciales, huecos


def pdf_de(carpeta: Path, idioma: str) -> str:
    sufijo = "-ES.pdf" if idioma == "es" else "-EN.pdf"
    for p in sorted(carpeta.glob("*.pdf")):
        if p.name.endswith(sufijo):
            return p.relative_to(RAIZ).as_posix()
    return "(sin PDF)"


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("requisitos", type=Path)
    ap.add_argument("--idioma", choices=["es", "en"], default="es")
    ap.add_argument("--todas", action="store_true", help="muestra las 8, no solo las 3 mejores")
    args = ap.parse_args()

    if not args.requisitos.exists():
        print(f"No existe {args.requisitos}")
        return 1
    reqs = leer_requisitos(args.requisitos)
    if not reqs:
        print("No encontré requisitos. Revisa el formato: '## Must-have' y '- termino | sinonimo'.")
        return 1

    filas = []
    for carpeta in sorted(d for d in VARIANTES.iterdir() if d.is_dir()):
        md = carpeta / f"cv-{args.idioma}.md"
        if not md.exists():
            continue
        pct, parciales, huecos = puntuar(md.read_text(encoding="utf-8"), reqs)
        filas.append((pct, carpeta.name, parciales, huecos, pdf_de(carpeta, args.idioma)))
    filas.sort(key=lambda f: -f[0])

    n_must = sum(1 for r in reqs if r[1] == 2)
    print(f"Requisitos: {n_must} must-have, {len(reqs) - n_must} nice-to-have · idioma {args.idioma}\n")
    print("| Variante | % | Parcial (solo en Habilidades) | Huecos |")
    print("|---|---|---|---|")
    for pct, nombre, parciales, huecos, _ in (filas if args.todas else filas[:3]):
        print(f"| {nombre} | {pct:.0f}% | {', '.join(parciales) or '-'} | {', '.join(huecos) or '-'} |")

    if MAESTRO.exists():
        pct_m, par_m, hue_m = puntuar(MAESTRO.read_text(encoding="utf-8"), reqs)
        print(f"\ncv_total.md (techo posible): {pct_m:.0f}% · huecos: {', '.join(hue_m) or 'ninguno'}")

    mejor = filas[0]
    print()
    if mejor[0] >= UMBRAL:
        print(f"DECISIÓN: usar {mejor[1]} ({mejor[0]:.0f}%). Adjunto: {mejor[4]}")
    else:
        print(f"DECISIÓN: ninguna llega a {UMBRAL}% (mejor: {mejor[1]}, {mejor[0]:.0f}%). "
              "Crear CV nuevo con cv-adaptador desde CV/cv_total.md.")
        if MAESTRO.exists() and pct_m < UMBRAL:
            print(f"AVISO: ni el cv_total.md llega a {UMBRAL}%. Hacer el mejor CV posible y "
                  f"decir qué falta: {', '.join(hue_m)}")
    print("\nNota: el script busca palabras. Revisa a ojo los huecos: un sinónimo que falte "
          "en requisitos.md puede bajar el %.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
