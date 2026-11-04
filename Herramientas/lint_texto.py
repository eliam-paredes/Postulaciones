"""Revisa los textos que se envian (correo, carta, respuestas, mensajes, CV)
contra las reglas del proyecto. Sale con codigo 1 si hay errores.

Uso:
    python Herramientas/lint_texto.py Casos/<slug>/correo.md
    python Herramientas/lint_texto.py Casos/<slug>/respuesta.md

Tambien funciona como hook de Claude Code (PostToolUse): si recibe JSON por
stdin con tool_input.file_path, revisa ese archivo y, si hay errores, los
devuelve por stderr con codigo 2 para que el modelo los corrija.

Que revisa:
    Todos:        guion largo, emojis, signos de exclamacion, frases prohibidas.
    correo.md:    la seccion "## Carta" tiene 80-130 palabras, sin listas,
                  máximo 700 caracteres, con cierre "Atentamente," + "Eliam Paredes".
    propuestas:   "## Propuesta final" tiene 50-150 palabras sin contar enlaces.
    respuesta.md: sin secciones prohibidas ("Por qué funciona", lint, adaptaciones).
    cv.md:        sin la palabra "Junior".
    Aviso (no error): [placeholders] sin rellenar.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Archivos a los que se aplica (son textos para enviar).
ARCHIVOS = {"correo.md", "respuesta.md", "mensajes.md", "cv.md", "carta.md"}

EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF⭐⭕✅❌️]"
)

FRASES_PROHIBIDAS = [
    # español
    "espero que estés bien", "espero que se encuentre bien", "me emociona",
    "me entusiasma la oportunidad", "candidato perfecto", "candidato ideal",
    "apasionado", "apasionada", "sinergia", "sin fricciones", "dinámico equipo",
    "crecer profesionalmente",
    # inglés
    "i hope this finds you well", "i hope you are well", "excited about this opportunity",
    "perfect fit", "passionate", "leverage", "seamless", "dive deep", "synergy",
]

SECCIONES_PROHIBIDAS_RESPUESTA = [
    "por qué funciona", "why it works", "lint", "adaptaciones recomendadas",
    "autenticidad",
]


def quitar_comentarios(texto: str) -> str:
    return re.sub(r"<!--.*?-->", " ", texto, flags=re.S)


def seccion(texto: str, titulo: str) -> str | None:
    m = re.search(rf"^##\s+{titulo}\s*$(.*?)(?=^##\s|\Z)", texto, flags=re.M | re.S | re.I)
    return m.group(1).strip() if m else None


def revisar(ruta: Path) -> tuple[list[str], list[str]]:
    errores, avisos = [], []
    texto = quitar_comentarios(ruta.read_text(encoding="utf-8"))
    nombre = ruta.name.lower()
    bajo = texto.lower()

    for n, linea in enumerate(texto.splitlines(), 1):
        if "—" in linea or " -- " in linea:
            errores.append(f"línea {n}: guion largo (—). Usa coma o punto.")
        if EMOJI.search(linea):
            errores.append(f"línea {n}: emoji.")
        sin_md = re.sub(r"!\[", "", linea)  # imagenes markdown
        if "!" in sin_md or "¡" in sin_md:
            errores.append(f"línea {n}: signo de exclamación.")

    for frase in FRASES_PROHIBIDAS:
        if re.search(rf"(?<!\w){re.escape(frase)}(?!\w)", bajo):
            errores.append(f'frase prohibida: "{frase}".')

    if nombre == "correo.md":
        carta = seccion(texto, "Carta")
        if carta is None:
            errores.append('falta la sección "## Carta".')
        else:
            palabras = len(re.findall(r"\b[\wáéíóúñü.@/:-]+\b", carta, flags=re.I))
            if not 80 <= palabras <= 130:
                errores.append(f"la carta tiene {palabras} palabras; debe tener 80-130.")
            if len(carta) > 700:
                errores.append(f"la carta tiene {len(carta)} caracteres; máximo 700 con espacios.")
            for n, linea in enumerate(carta.splitlines(), 1):
                if re.match(r"^\s*([-*+]|\d+[.)])\s+", linea):
                    errores.append(f"la carta tiene una lista (línea {n} de la carta). Solo texto corrido.")
                    break
            if not re.search(r"(Atentamente|Sincerely|Kind regards|Best regards),", carta):
                errores.append('la carta no cierra con "Atentamente," (o "Sincerely,").')
            if "Eliam Paredes" not in carta:
                errores.append('la carta no termina con la firma "Eliam Paredes".')
        for campo in ("Para:", "Asunto:", "Adjunto:"):
            if campo.lower() not in bajo:
                errores.append(f'falta el campo "{campo}".')

    if "propuestas" in {x.lower() for x in ruta.parts}:
        final = seccion(texto, r"Propuesta final")
        if final is not None:
            sin_enlaces = re.sub(r"https?://\S+", " ", final)
            palabras = len(re.findall(r"[\wáéíóúñü'’]+", sin_enlaces, flags=re.I))
            if not 50 <= palabras <= 150:
                errores.append(
                    f"la propuesta final tiene {palabras} palabras sin enlaces; debe tener 50-150."
                )

    if nombre == "respuesta.md":
        for titulo in re.findall(r"^#+\s+(.+)$", texto, flags=re.M):
            t = titulo.lower()
            for prohibida in SECCIONES_PROHIBIDAS_RESPUESTA:
                if prohibida in t:
                    errores.append(f'sección prohibida en respuesta.md: "{titulo.strip()}".')
        if re.search(r"^\s*[—-]\s*por qué funciona", bajo, flags=re.M):
            errores.append('respuesta.md incluye "Por qué funciona". Quítalo.')

    if nombre == "cv.md" and re.search(r"\bjunior\b", bajo):
        errores.append('el CV dice "Junior" (regla de CV/estilo.md).')

    marcadores = sorted(set(re.findall(r"\[[^\]\n]{2,60}\](?!\()", texto)))
    marcadores = [m for m in marcadores if not re.match(r"\[(VERIFICADO|INFERIDO|SUPOSICIÓN|x| )\]", m)]
    if marcadores:
        avisos.append("datos por rellenar: " + ", ".join(marcadores))

    return errores, avisos


def modo_hook() -> int:
    try:
        datos = json.load(sys.stdin)
    except Exception:
        return 0
    ruta = (datos.get("tool_input") or {}).get("file_path")
    if not ruta:
        return 0
    p = Path(ruta)
    partes = {x.lower() for x in p.parts}
    aplica = p.name.lower() in ARCHIVOS and "casos" in partes
    aplica = aplica or ("propuestas" in partes and p.suffix == ".md" and p.name.lower() != "leeme.md")
    if not aplica or not p.exists():
        return 0
    errores, avisos = revisar(p)
    if errores:
        print(f"lint_texto.py encontró problemas en {p.name}. Corrígelos:", file=sys.stderr)
        for e in errores:
            print(f"- {e}", file=sys.stderr)
        return 2
    return 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    if len(sys.argv) == 1 and not sys.stdin.isatty():
        return modo_hook()
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    hay_error = False
    for arg in sys.argv[1:]:
        p = Path(arg)
        errores, avisos = revisar(p)
        estado = "FALLA" if errores else "PASA"
        print(f"{estado} · {p}")
        for e in errores:
            print(f"  ERROR: {e}")
        for a in avisos:
            print(f"  AVISO: {a}")
        hay_error = hay_error or bool(errores)
    return 1 if hay_error else 0


if __name__ == "__main__":
    sys.exit(main())
