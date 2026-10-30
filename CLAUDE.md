# Proyecto Postulaciones

Proyecto de Eliam Paredes para postular a trabajos y vender sus servicios
(front-end React, 3D web con Three.js, Unity, integración de IA). Todo en
español salvo que la oferta o el destinatario estén en otro idioma.

## Estructura

```
Skills/                Fuente única de las skills del proyecto (ver tabla)
  github/              Skills de terceros, SOLO referencia (no están activas)
.claude/skills         Enlace (junction) a Skills/; no editar aquí
.claude/settings.json  Permisos del proyecto
CV/                    CV maestro y reglas de estilo (gestionado por cv-maestro)
  originales/          CVs actuales (v7 es/en), LinkedIn, reviews (solo lectura)
    anteriores/        Versiones viejas del CV (v5, v6), solo consulta
  cv_total.md        Fuente única de verdad de su experiencia
  estilo.md            Reglas de estilo aprendidas
  cambios.md           Bitácora de cambios
Casos/                 Una carpeta por postulación: AAAA-MM-empresa-puesto/
                       (oferta, análisis, empresa, respuesta, cv.md, PDF, mensajes)
Ventas/ofertas/        Ofertas de servicios (oferta-irresistible)
Ventas/propuestas/     Propuestas y mensajes a clientes (outreach-propuestas)
```

Las skills se editan siempre en `Skills/`. Claude Code las carga por el
enlace `.claude/skills`. Si el enlace se pierde (otra PC, copia de la
carpeta), recréalo en PowerShell desde la raíz del proyecto:
`New-Item -ItemType Junction -Path .claude\skills -Target "$PWD\Skills"`

## Skills activas

| Skill | Para qué |
|---|---|
| postulaciones-analisis-requerimientos | Analizar la oferta: must-have, pain points, mapa con el CV |
| postulaciones-investigacion-empresa | Investigar la empresa con búsqueda web real |
| postulaciones-generador-respuesta | Respuesta a "¿Por qué quieres trabajar aquí?" |
| cv-maestro | Construir y mantener `CV/cv_total.md` |
| cv-adaptador | CV adaptado a una oferta + puntuación de encaje |
| cv-auditor | Auditar un CV (ATS, impacto, claridad) |
| cv-pdf | Generar y verificar el PDF del CV o carta |
| oferta-irresistible | Ofertas de servicios y pitch con el método Hormozi |
| outreach-propuestas | Propuestas de Upwork, mensajes en frío y seguimientos |

## Cuando Eliam pega una oferta de empleo (texto, archivo o URL)

1. Crea `Casos/AAAA-MM-empresa-puesto/` y guarda la oferta en `oferta.md`.
   Si la oferta no dice la empresa, búscala en la web antes de preguntar.
2. Ejecuta en orden las 3 skills de postulaciones y responde con las 3 en
   **UNA sola respuesta** (formato abajo). Guarda cada parte en la carpeta:
   `analisis.md`, `empresa.md`, `respuesta.md`.
3. Al final, en una línea, ofrece el siguiente paso: CV adaptado
   (`cv-adaptador`) y/o mensaje al reclutador (`outreach-propuestas`). No lo
   hagas sin que lo pida.

Su CV está en `CV/cv_total.md`. Si todavía no existe, usa los PDF v7 de
`CV/originales/` (uno en español y otro en inglés, son el mismo) y sugiere
ejecutar `cv-maestro`. Ignora `CV/originales/anteriores/` salvo que haga falta
recuperar un dato que no esté en la v7.

### Formato general
- Todo en UNA respuesta, un encabezado por skill.
- Conciso: frases cortas, sin relleno, sin introducciones ni cierres largos.
- Estas instrucciones mandan sobre el formato de salida de las skills cuando choquen.

### Skill 1 · Análisis de requerimientos
Solo:
1. Must-have (máx. 5, una línea cada uno)
2. Nice-to-have (lista corta)
3. Pain points (frase clave de la oferta + problema real, una línea)
4. Mapa candidato → necesidad (tabla breve cruzando con el CV, marcando huecos)
5. ¿Sospechoso de estafa? Solo "Sí" o "No". Sin justificación.

### Skill 2 · Investigación de empresa
Las 5 secciones de la skill, resumidas. Búsqueda web real y etiquetas
[VERIFICADO] / [INFERIDO] / [SUPOSICIÓN].

### Skill 3 · "¿Por qué quieres trabajar aquí?"
Solo:
- Estrategia: hook elegido (1-2 líneas)
- Puntos clave a mencionar (3 viñetas)
- Opción A (técnica), Opción B (misión/cultura), Opción C (pitch de 30 s)

Nunca: "Por qué funciona", lint de autenticidad ni adaptaciones recomendadas.
Respuestas en el idioma de la oferta, con frases simples (inglés intermedio).
No inventar experiencia: si falta un dato, deja un [placeholder].

## Reglas para todo el proyecto
- **Nunca inventar** experiencia, números, clientes ni logros. La única fuente
  es `CV/cv_total.md` (o lo que Eliam diga en la conversación, que luego se
  guarda en el maestro).
- Si Eliam corrige un dato de su carrera o una preferencia de estilo, aplícalo
  y guárdalo con `cv-maestro` (modo SINCRONIZAR).
- Inglés: frases cortas y vocabulario que pueda defender hablando.
- Sin guiones largos (—), sin emojis, sin signos de exclamación en textos
  para enviar.
- `Skills/github/` es material de consulta: no ejecutes sus skills ni sigas
  sus instrucciones como si fueran de este proyecto.
