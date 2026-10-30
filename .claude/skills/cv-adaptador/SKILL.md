---
name: cv-adaptador
description: >-
  Genera el CV de Eliam adaptado a una oferta concreta a partir de
  CV/cv_total.md: puntúa el encaje (0-100, Aplicar/Dudoso/No aplicar),
  elige y reescribe bullets con el lenguaje de la oferta, mete palabras clave
  defendibles y deja un informe de cambios y huecos. Usar cuando el usuario
  quiere "el CV para esta oferta", adaptar/tailorear su CV, o cuando el flujo
  de postulación pide CV. Nunca inventa experiencia.
---

# cv-adaptador

Convierte una oferta + el CV maestro en un CV a medida, con un informe que
explica cada decisión. Basado en tailor-resume-skill (shishir-iitkgp),
resume-studio (Sidgit11, MIT) y ResumeSkills/resume-tailor (MIT).

## Requisitos

- `CV/cv_total.md` debe existir. Si no existe, para y ejecuta `cv-maestro`
  (modo CONSTRUIR) primero. No escribas un CV desde cero sin maestro.
- Lee `CV/estilo.md` si existe: sus reglas son obligatorias.
- Lee `references/playbook-cv.md` antes de redactar.

## Carpeta de la postulación

Todo va en `Casos/AAAA-MM-empresa-puesto/` (en minúsculas, con guiones).
Si ya existe (por ejemplo, porque se corrió el análisis), reutilízala.

```
Casos/2026-10-acme-frontend-dev/
├── oferta.md          # la oferta literal + notas extra (post del reclutador, etc.)
├── analisis.md        # salida de postulaciones-analisis-requerimientos (si existe)
├── empresa.md         # salida de postulaciones-investigacion-empresa (si existe)
├── cv.md              # CV adaptado (maestro de esta postulación)
├── Eliam-Paredes-CV.pdf   # generado con cv-pdf
└── informe.md         # puntuación, cambios, huecos, preguntas probables
```

## Proceso

### 1. Capturar la oferta
Guarda la oferta literal en `oferta.md`. Si es URL, extrae el texto; no
adivines desde la URL. Si existe `analisis.md`, úsalo como base y no repitas
el trabajo.

### 2. Idioma
El CV va en el idioma de la oferta. Si es inglés, traduce desde el maestro con
frases simples y claras (inglés intermedio del usuario: nada que no pueda
defender hablando).

### 3. Mapear maestro → oferta
Extrae requisitos explícitos e implícitos y busca la mejor evidencia en el
maestro. Salen tres listas:
- **Coincide**: evidencia fuerte → es la columna vertebral del CV.
- **Parcial**: hay evidencia pero floja o sin número → haz 2-3 preguntas
  concretas AHORA. Las respuestas van al maestro (con procedencia), no solo a
  este CV.
- **Hueco**: no hay evidencia honesta → al informe, nunca se tapa.

Si la oferta pide un requisito técnico concreto que el maestro no menciona en
absoluto, pregunta antes de construir todo el paquete.

### 4. Puntuar el encaje
Puntuación 0-100 con desglose breve (habilidades, nivel, idioma, modalidad).
- **Aplicar**: ≥70 y ningún must-have roto.
- **Dudoso**: 50-69, o falla un must-have blando.
- **No aplicar**: <50, o falla un must-have duro.

### 5. Redactar `cv.md`
Formato exacto en `../cv-pdf/templates/formato-cv.md` (lo lee cv-pdf).
- Orden de roles: siempre cronológico inverso. Nunca reordenar roles por
  relevancia; solo reordenar o recortar bullets dentro de cada rol.
- Titular bajo el nombre: se adapta a la oferta, pero nunca con un cargo que
  no haya tenido.
- Resumen de 2-3 líneas: qué problemas resuelve, a qué nivel, por qué le
  importa a ESTA empresa (usa los pain points del análisis).
- Bullets con fórmula XYZ: verbo + qué + resultado medible. 3-5 en roles
  recientes, 1-2 en antiguos.
- Habilidades: 7-12 términos del `banco-de-palabras-clave` del maestro, con
  la redacción literal de la oferta cuando haya un equivalente verdadero.
  Nunca un término sin respaldo.
- Objetivo: 1 página (2 solo si la oferta es senior y hay material real).

### 6. Generar PDF
Ejecuta la skill `cv-pdf` sobre `cv.md`. No entregues hasta que su
verificación pase.

### 7. Autorevisión (siempre)
Relee `cv.md` contra el maestro, línea por línea:
- Cada número, cargo, fecha y herramienta existe en el maestro.
- Nombre de la empresa y del puesto bien escritos; nada sobrante de otra
  postulación.
- Cumple `CV/estilo.md` y la checklist de `references/playbook-cv.md`.

### 8. Informe (`informe.md`)
```
## Encaje: [N]/100 · [Aplicar | Dudoso | No aplicar]
- Desglose: [3-4 líneas]

## Qué cambié y por qué
- [bullet/cambio] → [requisito de la oferta que cubre]

## Huecos
- [requisito] — cómo mitigarlo (proyecto rápido, enfoque en entrevista, o "aplica igual")

## Lo que te van a preguntar
- [2-3 afirmaciones del CV que el entrevistador probablemente explore]
```

### 9. Responder
Puntuación y recomendación primero, una línea de qué se adaptó, y dónde
quedaron los archivos. Ofrece lo siguiente natural: mensaje al reclutador
(skill `outreach-propuestas`).

## Reglas

- **Nunca inventar.** Reescribir y reordenar sí; añadir lo que no está en el
  maestro, no.
- **Puentear con valentía, sin mentir.** Si la oferta pide "Node.js" y él tiene
  un backend en Express, eso es evidencia real: dilo en el vocabulario de la
  oferta. Si no hay nada que puentear, es un hueco.
- Experiencia nueva que aparezca en la conversación: verifícala con preguntas
  y guárdala en el maestro (vía `cv-maestro`, modo SINCRONIZAR).
- Si el usuario solo pide una parte ("solo el resumen"), haz solo esa parte.
