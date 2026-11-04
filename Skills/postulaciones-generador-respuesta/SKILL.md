---
name: postulaciones-generador-respuesta
description: >-
  Escribe la respuesta de Eliam a "¿Por qué quieres trabajar aquí?" en tres
  versiones (técnica, misión/cultura y pitch de 30 s), usando el análisis de
  la oferta, la investigación de la empresa y su CV real. Usar cuando el
  usuario prepara una postulación o entrevista. Es la Skill 3 del flujo de
  postulación.
---

# postulaciones-generador-respuesta

Objetivo: una respuesta que hable de lo que gana la empresa, con una prueba
real de Eliam, en palabras que él pueda decir en voz alta.

## Qué leer (no preguntes, lee)

1. `Casos/<slug>/analisis.md`: must-have y pain points.
2. `Casos/<slug>/empresa.md`: sobre todo la sección 5.
3. `CV/cv_total.md`: la única fuente de pruebas y números.
4. `CV/motivaciones.md` si existe: qué le atrae de verdad a Eliam.

## Principios (Dale Carnegie + Hormozi, en corto)

- Habla desde lo que ellos necesitan, no desde lo que él quiere.
- Un elogio concreto y verificable de la empresa, nunca adulación genérica.
- Una prueba concreta en vez de adjetivos ("publiqué TrapNight: más de 1.500
  descargas" en vez de "soy muy proactivo").
- Termina en lo que aporta, no en lo que pide.

## Pasos

1. **Elige un hook** (solo uno):
   - Problema técnico: la oferta tiene un pain point claro.
   - Misión o producto: la empresa tiene propósito claro o un producto que
     Eliam conoce.
   - Momento de la empresa: crecimiento, lanzamiento o ronda reciente.
   - Stack: la tecnología es el imán real (Three.js, Unity, IA).
2. **Elige 3 puntos clave:** algo de la empresa (de `empresa.md`), un pain
   point (de `analisis.md`) y una prueba de Eliam (de `cv_total.md`).
3. **Escribe las 3 opciones** con esta estructura:
   aprecio concreto → su problema o momento → prueba de Eliam → qué aporta.

## Salida (exacta, nada más)

```
## Respuesta: ¿Por qué quieres trabajar aquí?

**Estrategia:** [hook elegido, 1-2 líneas]

**Puntos clave**
- [elemento de la empresa]
- [pain point que responde]
- [prueba real de Eliam]

**Opción A (técnica, 60-90 s)**
"[texto]"

**Opción B (misión/cultura, 60-90 s)**
"[texto]"

**Opción C (pitch de 30 s)**
"[texto]"
```

Guarda lo mismo en `Casos/<slug>/respuesta.md`.

## Reglas

- **Idioma:** el de la oferta. En inglés, nivel intermedio (B1): frases de
  10-15 palabras, palabras comunes, contracciones (I'm, I've, that's). Nada
  que Eliam no pueda repetir en una llamada.
- **Números:** solo los que están en `cv_total.md` (por ejemplo, 1.500+
  descargas, 4,7 estrellas, 14 contratos, 100% Job Success, Top Rated). Si
  ninguno encaja, no pongas número. Nunca inventes horas ahorradas,
  porcentajes ni clientes.
- **Datos de la empresa:** solo los de `empresa.md` marcados [VERIFICADO].
- **Si falta algo** (una motivación personal, un producto que usa): escribe
  un `[placeholder]` y no lo inventes.
- **Prohibido:** salario, ubicación o "crecer profesionalmente" como motivo;
  quejas de trabajos anteriores; "apasionado", "me emociona", "dinámico
  equipo", "candidato perfecto", "passionate", "excited", "perfect fit".
- **Nunca incluyas:** "Por qué funciona", lint de autenticidad ni
  "Adaptaciones recomendadas".
- Sin guiones largos, emojis ni signos de exclamación.

## Ejemplo de Opción C (inglés, B1)

"I saw you're moving your product demos to the web with 3D. That's what I
do. I build 3D models in Blender and bring them to React with Three.js. I'm
Top Rated on Upwork, with 100% Job Success. I'd like to help your team ship
those demos faster."

## Control antes de responder

- [ ] Cada número existe en `cv_total.md`.
- [ ] Cada dato de la empresa existe en `empresa.md`.
- [ ] Cada opción habla más de ellos que de él.
- [ ] Sin secciones extra.
