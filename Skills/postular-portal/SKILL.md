---
name: postular-portal
description: >-
  Flujo completo cuando Eliam pega una oferta de empleo que se postula por
  portal, formulario o LinkedIn: crea la carpeta del caso y responde en UNA
  sola respuesta con el análisis, la investigación de empresa y la respuesta
  a "¿Por qué quieres trabajar aquí?". Usar siempre que pegue una oferta (texto,
  archivo o URL) y NO sea por correo.
---

# postular-portal

Sigue los pasos en orden. No te saltes ninguno. No preguntes nada salvo que
falte la oferta.

## Paso 1 · Carpeta del caso

1. Nombre: `Casos/AAAA-MM-empresa-puesto/`
   - `AAAA-MM`: año y mes de HOY.
   - `empresa` y `puesto`: minúsculas, sin tildes, palabras unidas con guion,
     máximo 3 palabras cada uno. Ej.: `Casos/2026-11-lumen-frontend-developer/`.
   - Si la oferta no dice la empresa, búscala en la web con una frase literal
     de la oferta. Si no aparece, usa `empresa-confidencial`.
2. Copia `Casos/_plantilla/oferta.md`, rellena los campos y pega la oferta
   literal debajo. Si es URL, abre la página con WebFetch y copia el texto.

## Paso 2 · Skill 1 (análisis)

Ejecuta `postulaciones-analisis-requerimientos`. Guarda `analisis.md`.

## Paso 3 · Skill 2 (empresa)

Ejecuta `postulaciones-investigacion-empresa` con búsquedas web reales.
Guarda `empresa.md`.

## Paso 4 · Skill 3 (respuesta)

Ejecuta `postulaciones-generador-respuesta`, en el idioma de la oferta.
Guarda `respuesta.md`. El hook revisa el archivo al guardarlo: si se queja,
corrige y vuelve a guardar. También puedes ejecutar
`python Herramientas/lint_texto.py Casos/<slug>/respuesta.md`.

## Paso 5 · Registro

Añade una fila a `Casos/registro.md` con estado `analizada`.

## Paso 6 · Responder (UNA sola respuesta)

```
## Análisis de requerimientos
(salida de la Skill 1)

## Empresa · [Nombre]
(salida de la Skill 2)

## Respuesta: ¿Por qué quieres trabajar aquí?
(salida de la Skill 3)

Siguiente paso: ¿quieres el CV adaptado (cv-adaptador) o un mensaje al reclutador (outreach-propuestas)?
```

Sin introducción, sin resumen final y sin hacer el siguiente paso hasta que
lo pida.

Ejemplo completo de un caso bien hecho: `Casos/_ejemplo-portal/`. Imita su
formato y su largo.
