Pista: 3D/Video (con parte de software: Three.js)
Post: pegado en el chat (Super Boring AI, sitio 3D con coche de F1 que se ensambla al hacer scroll)

## Dolor
- Frase clave: "components come together into one complete performance machine" → necesitan que cada pieza encaje exacta en cada frame; si no, el coche se ve suelto.
- Resultado soñado: una experiencia premium en el sitio, que explique el producto con el coche, con piezas nombradas que se pueden tocar.
- Objeciones probables: si Eliam ha modelado un coche (no hay evidencia en el maestro); si puede hacer la parte web en tiempo real; si la experiencia corre en móvil.
- Instrucciones del post: pide tres ejemplos 3D en vivo, rol en cada uno, estimaciones de precio separadas (asset, animación, web), hitos y móvil. La propuesta solo cubre el primer paso y lo ofrece por separado.
- Señales: sin datos del cliente en el post.

## Boceto
1. Hook: la parte difícil de un coche que se arma con scroll es que cada pieza llegue al lugar exacto en cada frame.
2. Solución: separar el coche en piezas con nombre en Blender, con su propio origen para alinear exacto; exportar GLB ligero; animar con Three.js ligado al scroll.
3. Prueba: Top Rated en Upwork con 100% Job Success; un modelo 3D para un sitio con Three.js, reseña 5,0. Sin coche previo: decirlo.
4. Riesgo + pregunta: primer hito cotizado aparte (modelo del coche y una prueba de ensamblaje). Pregunta: ¿tienen planos o archivo CAD del coche?

## Propuesta final
The hard part of a scroll-driven assembly is timing: each part has to land exactly on every frame. I'd solve that in Blender first.

How I'd do it:
- Animate the whole car in Blender as one timeline, with each part named
- Export one light GLB and link the timeline's progress to the scroll
- Set stop points on the scroll, so the car never stops halfway through a part
- Quote the first milestone separately: the model plus one assembly test

I'm Top Rated on Upwork with 100% Job Success. I modeled a 3D asset for a Three.js site, and the client rated it 5.0. I haven't modeled a car yet, so the first milestone tests the fit.

Portfolio: https://www.behance.net/eliam_paredes

Two quick questions: do you already have the car model ready? And how much time do you have for this project?

## Precio
- Primer hito (modelo del coche + prueba de ensamblaje): [por confirmar con Eliam]. No se incluye número en la propuesta hasta que lo defina él.
- Producción completa (asset, animación, integración web): [por cotizar, tres estimaciones separadas, pendiente de datos de Eliam].

<!-- POST ORIGINAL
We are creating a premium interactive website for Super Boring AI ... (brief completo pegado en el chat: 3D del coche F1 con componentes nombrados,
scroll, Three.js, GLB, GSAP, PBR, móvil, accesibilidad, tres ejemplos 3D en vivo,
estimaciones separadas por hitos). Ver el chat del 2026-11.
-->
