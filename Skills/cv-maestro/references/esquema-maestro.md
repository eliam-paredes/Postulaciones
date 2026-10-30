# Formato de los archivos del CV

Sigue estos formatos exactos para que cualquier sesión futura pueda leer lo que
escribieron las anteriores.

## CV/cv_total.md

```markdown
# CV maestro · Eliam Paredes
Actualizado: AAAA-MM-DD

## perfil
Contacto: email · teléfono · ciudad · linkedin · github · portafolio
Objetivos: tipos de rol, nivel, remoto/presencial, idiomas de trabajo
Narrativa: 2-4 frases con el hilo de su carrera y hacia dónde va.

## rol: upwork-freelance-frontend          <!-- ancla: estable para siempre -->
Empresa: Upwork · Tipo: freelance
Cargo: Front-end / 3D Web Developer | Fechas: Abr 2024 – Actualidad | Lugar: Remoto
Alcance: tipo de clientes, tamaño de proyectos, con quién trabajaba
Fuente: CV-ES.pdf, entrevista 2026-10-29

### proyecto: configurador-3d-cliente-x    <!-- ancla: estable para siempre -->
- Qué hizo, en una línea
  - métrica: redujo el tiempo de carga de 8 s a 2 s {fuente: entrevista 2026-10-29}
- Historia (respuestas de entrevista, casi literal): contexto, obstáculo, qué hizo él
- Stack: React, Three.js, ...
- [VAGO] qué parte hizo él vs el otro dev

## educacion
### Ingeniería de Software
UNAPEC
Abr 2024 – Actualidad

## certificaciones
## idiomas
## extras            <!-- charlas, premios, juegos publicados, open source -->
## aparcado          <!-- material que no encaja aún en ningún rol -->

## banco-de-palabras-clave
<!-- Términos que el usuario SÍ puede defender, agrupados. cv-adaptador elige de aquí. -->
- Front-end: React, TypeScript, Vite, ...
- 3D / tiempo real: Three.js, Unity, Blender, ...
- IA: integración de LLMs, automatizaciones, ...
- Diseño: Figma, Adobe, ...
```

Reglas:
- Fechas siempre `Mes AAAA` (Ene, Feb, Mar, Abr, May, Jun, Jul, Ago, Sep, Oct, Nov, Dic). Nunca solo el año.
- Más nuevo gana: si el usuario corrige un dato, se actualiza en su sitio y se anota en `cambios.md`. No se guardan dos versiones.
- Cada término del banco de palabras clave debe estar respaldado por algún rol o proyecto.

## CV/estilo.md

Un archivo de reglas, no un diario. Corto (~30 reglas), en imperativo, con fecha.

```markdown
# Reglas de estilo
<!-- Una línea por regla, con fecha y motivo. La más nueva gana. -->

## nunca
- Usar guiones largos (—). (2026-10-29, corrección del usuario)

## siempre
- Poner el stack al final de cada bullet técnico. (2026-10-29)

## enfoque
- Presentar el trabajo de 3D como resultados de negocio, no solo técnicos. (2026-10-29)

## formato
<!-- Contrato de renderizado. Solo si el usuario eligió algo distinto al default. -->
- Fuente: Calibri 10.5pt. (2026-10-29)
- RIESGO ACEPTADO: ... (fecha) — no volver a advertir.
```

## CV/cambios.md

Solo se añade, lo más nuevo arriba. Una línea por evento.

```markdown
# Cambios
- 2026-10-29 [maestro] Construcción inicial desde CV-ES.pdf + CV-EN.pdf + entrevista
- 2026-10-29 [estilo] Añadida "nunca: guiones largos"
```
