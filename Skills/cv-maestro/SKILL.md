---
name: cv-maestro
description: >-
  Construye y mantiene el CV maestro de Eliam (CV/cv_total.md): la fuente
  única de verdad con toda su experiencia, logros medibles y su procedencia.
  Usar cuando el usuario comparte CVs, LinkedIn, proyectos o datos de su
  carrera; cuando pide crear, actualizar o "sincronizar" su CV; o cuando
  corrige un dato o una preferencia de estilo de su CV. No genera el CV para
  una oferta concreta (eso es cv-adaptador).
---

# cv-maestro

El CV maestro NO es un CV. Es un banco de experiencia mucho más grande que
cualquier CV, del que salen todas las versiones adaptadas. Si el maestro es
rico, cada CV nuevo es editar, no escribir.

Basado en resume-studio (Sidgit11, MIT) y resume-builder-skill (dabydat, MIT).

## Archivos que gestiona

```
CV/
├── originales/          # CVs, exportes de LinkedIn, cartas, reviews que aporta el usuario (solo lectura)
├── cv_total.md        # fuente única de verdad (formato en references/esquema-maestro.md)
├── estilo.md            # reglas de estilo aprendidas (lint, máx. ~30 reglas)
└── cambios.md           # bitácora: qué se aprendió/cambió y por qué (más reciente arriba)
```

**Al empezar, siempre:** lee `CV/cv_total.md` y `CV/estilo.md` si existen.
Las reglas de `estilo.md` son obligatorias en todo lo que produzcas.

## Modo 1 · CONSTRUIR (no existe el maestro o llega material nuevo)

1. **Ingerir todo.** Lee lo que haya en `CV/originales/` y lo que pegue el
   usuario (CV en español e inglés: son el mismo, fusiónalos sin duplicar).
   Pide fuentes de alto valor que la gente olvida, sin bloquear el trabajo:
   perfil de Upwork y sus reviews, portafolio/GitHub, proyectos de Marav
   Studios, ofertas de trabajos que ya tuvo, mensajes de clientes contentos.
2. **Redactar el maestro de inmediato, anotado.** Convierte todo al formato de
   `references/esquema-maestro.md`. Marca los huecos en línea:
   - `[SIN MÉTRICA]` logro sin cuantificar
   - `[VAGO]` no se sabe qué hizo él vs el equipo
   - `[FINO]` rol o periodo casi vacío
   Enséñale el borrador pronto: las marcas visibles hacen que la gente hable.
3. **Entrevistar contra los huecos.** Lee `references/banco-preguntas.md`.
   3-5 preguntas por ronda, primero lo reciente y lo relevante para sus
   objetivos (front-end, 3D web, IA). Usa AskUserQuestion si está disponible.
   Ofrece salida en cada ronda: "suficiente por ahora" es válido.
4. **Guardar y registrar.** Escribe el maestro, añade una línea en
   `cambios.md` y dile qué sigue flojo.

## Modo 2 · SINCRONIZAR (siempre activo)

Cuando el usuario corrija algo, en cualquier skill o momento, clasifica:

1. **Puntual** ("acorta este bullet") → aplica, no guardes.
2. **Regla de estilo** ("nunca pongas 'apasionado'", "sin guiones largos") →
   aplica Y guarda en `estilo.md` con fecha. Si contradice una regla vieja, la
   reemplaza (gana la nueva) y lo anotas en `cambios.md`.
3. **Dato de carrera** ("también hice X", "fueron 12 clientes, no 10") →
   aplica Y fusiona en `cv_total.md` en su ancla, con procedencia.

Si es ambiguo, pregunta una vez: "¿Siempre, o solo para este CV?"

## Reglas

- **Nunca inventar.** Ningún número, cargo, fecha, cliente o logro que el
  usuario no haya dicho o que no esté en sus documentos. Si falta la métrica,
  el bullet va sin número o se pregunta.
- Cada métrica lleva su fuente: `{fuente: CV-2025.pdf}`,
  `{fuente: entrevista 2026-10-29}`.
- Las anclas (`## rol: ...`, `### proyecto: ...`) no se renombran nunca: así
  las ediciones caen en su sitio y no se duplican.
- El maestro se escribe en español. Los CVs en inglés se generan desde él.
- No borres anotaciones `[SIN MÉTRICA]`/`[VAGO]`/`[FINO]` sin evidencia: son
  la lista de pendientes.
