---
name: cv-pdf
description: >-
  Convierte un CV en markdown (cv.md) en un PDF limpio y legible por ATS, y
  verifica el resultado con código: texto extraíble, páginas, títulos
  estándar, fechas, contacto y número de palabras. Usar siempre que haya que
  generar, regenerar o comprobar el PDF de un CV o carta de presentación. Para
  otras tareas de PDF (unir, rellenar formularios, OCR) usar la skill pdf
  general si está disponible.
---

# cv-pdf

Principio (de claude-resume-generator-skill, silentashish): **el modelo
escribe el contenido, el código decide si el PDF es aceptable.** Nunca
"estimes" páginas o legibilidad: mídelas.

## Requisitos (comprobar una vez)

```
python .claude/skills/cv-pdf/scripts/generar_cv.py --check
```

- Python 3.9+.
- Un navegador Chromium para imprimir el PDF: Microsoft Edge (viene con
  Windows) o Google Chrome. El script los busca solo. Alternativa: Playwright
  (`pip install playwright && playwright install chromium`).
- `pypdf` para verificar: `pip install pypdf`.

Si falta algo, dilo en un mensaje con el comando exacto para instalarlo.

## Flujo

1. **Formato de entrada.** El `cv.md` sigue `templates/formato-cv.md`. Léelo
   antes de escribir o corregir un `cv.md`.
2. **Generar:**
   ```
   python .claude/skills/cv-pdf/scripts/generar_cv.py Casos/<slug>/cv.md
   ```
   Crea `Eliam-Paredes-CV.pdf` (o el nombre de `--salida`) junto al `cv.md`,
   más el HTML intermedio. Opciones: `--idioma en` cambia el nombre a
   `-Resume.pdf`; `--estilo` apunta a otra hoja CSS.
3. **Verificar:**
   ```
   python .claude/skills/cv-pdf/scripts/verificar_cv.py Casos/<slug>/Eliam-Paredes-CV.pdf --paginas 1
   ```
   Comprueba: texto extraíble y en orden, nº de páginas, títulos estándar,
   email/teléfono en el cuerpo, fechas `Mes AAAA` (ninguna solo con año),
   palabras (aviso fuera de 350-700), caracteres raros. Guarda el texto plano
   en `*-texto-ats.txt`. Sale con código 1 si hay fallos duros.
4. **Corregir hasta que pase.** Si sobra página: recorta bullets menos
   relevantes (nunca bajes la fuente de 9.5pt ni toques márgenes por debajo de
   0.45in). Si falta contenido: añade evidencia real del CV maestro, nunca
   relleno.
5. **Mirar el resultado.** Abre el PDF (o una captura) y revísalo a ojo una
   vez: cortes feos, viudas, saltos raros.

## Reglas

- Una columna, sin tablas, iconos ni imágenes. El diseño vive en
  `templates/cv.css`; no lo cambies salvo que el usuario lo pida (y entonces
  guarda la decisión en `CV/estilo.md`, sección formato).
- El PDF se regenera siempre desde `cv.md`; nunca se edita el PDF a mano.
- Carta de presentación: mismo flujo con `--plantilla carta`.
