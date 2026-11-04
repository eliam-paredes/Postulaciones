---
name: postular-upwork
description: >-
  Flujo completo para postularse a un trabajo de Upwork: detecta la pista
  (software/web/IA, 3D/animación/video o juegos/Unity), saca el dolor del
  cliente, arma un boceto de 4 partes con la ecuación de valor de Hormozi y
  entrega la propuesta final de 50-150 palabras lista para pegar, con los
  enlaces que prueban el trabajo. Usar siempre que Eliam pegue un post,
  brief o enlace de Upwork, o pida "propuesta", "cover letter" o "proposal"
  para un cliente freelance.
---

# postular-upwork

Una propuesta de Upwork no se gana contando quién eres. Se gana cuando el
cliente siente que ya entendiste su problema y que contratarte no tiene
riesgo. Ejemplo completo bien hecho: `Ventas/propuestas/_ejemplo-upwork.md`.
Imita su formato y su largo.

Antes de escribir lee:
- `CV/cv_total.md`: la única fuente de pruebas (contratos de Upwork, reviews,
  proyectos, stack). Nada fuera de ahí.
- `Skills/outreach-propuestas/references/reglas-voz.md`: voz y lista prohibida.
- `references/hormozi-propuestas.md`: cómo vender en la propuesta.

## Paso 1 · Elegir la pista

| El post pide | Pista | Portafolio principal |
|---|---|---|
| Web, front-end, React, SaaS, Three.js, APIs, IA, automatización | **Software** | https://eliam-paredes.github.io |
| Animación, modelado, render, Blender, VFX, motion, edición de video | **3D/Video** | https://www.behance.net/eliam_paredes |
| Juegos, Unity, C#, game design, herramientas de editor | **Juegos** | https://marav-stress.itch.io/ |

Si mezcla dos (ej.: modelo 3D para Three.js), la pista es la del entregable
final y se añade un enlace de la otra. Enlaces extra por pista en
`references/enlaces.md`: usa como máximo 2, solo si se parecen al proyecto.

## Paso 2 · Dolor y necesidad (para Eliam, en español)

- **Dolor principal**: qué le frustra, qué le cuesta tiempo o dinero. Lee el
  post buscando el miedo: "fiable, sin excusas" = le fallaron antes; "loop
  sin cortes" = ya vio uno que salta; "debe escalar" = su código actual no
  aguanta. Cita la frase del post y di el problema real en una línea.
- **Resultado soñado**: lo que quiere al final, técnico y de negocio (más
  ventas, un canal que publica cada semana, una demo para inversores).
- **Objeciones probables**: 1-2 dudas que tendrá para contratar (idioma,
  plazos, si sabe hacer justo esto).
- **Instrucciones del post**: si pide empezar con una palabra, responder
  preguntas o no adjuntar algo, anótalo. Se cumple literalmente y primero.
- **Señales del cliente** (si las pega): gasto, tasa de contratación, pago
  verificado, reseñas. Si aparece su nombre o el de su empresa, úsalo.

## Paso 3 · Boceto (4 partes)

1. **Hook** (2 primeras líneas, es lo único que se ve en la vista previa).
   Su problema con sus palabras, o un detalle del post que demuestre que lo
   leíste (herramienta, estilo, plataforma). Prohibido empezar con "Hi, my
   name is", "I'm an expert", "I read your post" o repetir el título.
2. **Solución y enfoque**: cómo lo harías, en 2-3 pasos concretos del
   oficio. Cada paso quita un dolor o una objeción. Si el post hace
   preguntas, respóndelas aquí.
   - Software: arquitectura, componentes, rendimiento, integración de API,
     despliegue.
   - 3D/Video: pipeline de modelado, rigging, keyframes, loop, materiales,
     render de prueba a baja calidad, compositing, formato de entrega.
   - Juegos: mecánica, prototipo jugable, build, herramientas de editor.
3. **Prueba y portafolio**: una o dos líneas de credibilidad real del CV
   maestro (Top Rated, 100% Job Success, el contrato de Upwork más parecido,
   un proyecto similar). Luego el portafolio principal y hasta 2 enlaces
   extra. En trabajos pequeños y urgentes basta una línea.
4. **Quitar el riesgo + pregunta de cierre**: una muestra pequeña gratis o
   una prueba corta (ver `references/hormozi-propuestas.md`), y una pregunta
   técnica fácil de responder que obligue a contestar (motor de render,
   formato, plazo, si ya tiene los archivos). Invita al chat, no a una
   llamada de 30 minutos.

## Paso 4 · Propuesta final (la que se envía)

Resume el boceto en **50-150 palabras** (los enlaces no cuentan):
- Mantiene las 4 partes, en ese orden.
- Párrafos de 1-2 frases. Hasta 3 viñetas cortas en la solución.
- Más "you" que "I". Contracciones en inglés (I'd, I'll, you're).
- Idioma del post. En inglés, nivel B1: frases que Eliam pueda repetir en
  una llamada.
- Enlaces en líneas sueltas, sin emojis: `Portfolio: https://...`.
- Nada de exclamaciones, guiones largos ni frases de la lista prohibida.

Si el post trae preguntas de filtro (screening questions), respóndelas
aparte, 1-3 frases cada una.

**Precio** (si el post lo pide o es precio fijo): da un número o un rango
con el supuesto que lo mueve. No bajes el precio para ganar: sube el valor
(muestra gratis, entrega por partes, revisiones claras).

## Paso 5 · Guardar

`Ventas/propuestas/AAAA-MM-cliente-o-proyecto.md` (minúsculas, sin tildes):

```
Pista: [Software | 3D/Video | Juegos]
Post: [URL si la hay]

## Dolor
## Boceto
## Propuesta final
## Preguntas del cliente      (solo si hay)
## Precio                     (solo si aplica)

<!-- POST ORIGINAL
[texto pegado del post]
-->
```

El post va dentro del comentario para que el hook no lo revise. El hook
(`Herramientas/lint_texto.py`) comprueba que la propuesta final tenga
50-150 palabras sin contar enlaces. Si se queja, corrige y guarda otra vez.

## Paso 6 · Responder (UNA sola respuesta, en este orden)

```
## Dolor del cliente
- Dolor: ...
- Resultado soñado: ...
- Objeciones: ...

## Boceto
Hook / Solución / Prueba / Riesgo + pregunta (compacto)

## Propuesta final (N palabras)
[texto listo para pegar]

## Preguntas del cliente   (si hay)

Siguiente paso: seguimiento si no contesta en 3-4 días (outreach-propuestas).
```

## Checklist antes de entregar
- [ ] Instrucciones del post cumplidas literalmente
- [ ] Las 2 primeras líneas hablan del cliente, no de Eliam
- [ ] Un detalle técnico que solo diría alguien que hace este trabajo
- [ ] Toda prueba está en `CV/cv_total.md` (ningún número ni cliente inventado)
- [ ] Portafolio de la pista correcta y máximo 2 enlaces extra relacionados
- [ ] Riesgo quitado (muestra, prueba corta o entrega por partes)
- [ ] Termina en una pregunta fácil de responder
- [ ] 50-150 palabras sin contar enlaces
