---
name: postular-correo
description: >-
  Flujo completo cuando la vacante se postula enviando el CV por correo: crea
  la carpeta del caso, mide el encaje de las 8 variantes del CV con un script,
  elige el adjunto, investiga la empresa y escribe la carta en el cuerpo del
  correo. Usar cuando Eliam dice que la vacante es por correo, o cuando la
  oferta pide enviar el CV a un correo y no tiene formulario ni portal.
---

# postular-correo

Sigue los pasos en orden. No te saltes ninguno. Ejemplo completo de un caso
bien hecho: `Casos/_ejemplo-correo/`. Imita su formato y su largo.

## Paso 1 · Carpeta del caso

Igual que en `postular-portal`: `Casos/AAAA-MM-empresa-puesto/` (fecha de hoy,
minúsculas, sin tildes) con `oferta.md` copiado de `Casos/_plantilla/oferta.md`.
Si falta la empresa, búscala en la web antes de preguntar.

## Paso 2 · Requisitos

Escribe `requisitos.md` copiando `Casos/_plantilla/requisitos.md`:
- Must-have (máx. 8) y nice-to-have, uno por línea.
- Añade sinónimos con `|` en el idioma del CV que vas a usar
  (ej.: `- Edición de video | DaVinci Resolve | Premiere`). Más sinónimos =
  puntuación más justa.

## Paso 3 · ¿Estafa?

"Sí" si hay 2 o más: correo genérico (gmail, hotmail) de una supuesta
empresa grande, piden pago, datos bancarios o documentos antes de
entrevistar, sueldo muy alto sin explicación, empresa que no existe en la
web, contacto solo por Telegram o WhatsApp.
**Si es "Sí": escríbelo arriba de todo y detente.**

## Paso 4 · Empresa

Ejecuta `postulaciones-investigacion-empresa` completa (búsquedas web
reales). Guarda `empresa.md`. Fíjate en la sección 5: qué beneficio le
importa a la empresa. Lo usarás en el párrafo 2 de la carta.

## Paso 5 · Correo destino

- El de la oferta, tal cual → `[VERIFICADO]`.
- Si no viene: búscalo (`EMPRESA correo empleo`, `EMPRESA rrhh email`,
  página de contacto). Si lo encuentras en una web → `[VERIFICADO]` con la
  URL. Si lo deduces del formato → `[INFERIDO]`.
- Nunca lo inventes. Si no hay ninguno, escribe `[correo por confirmar]`.
- Si hay varios, elige uno y di por qué en una línea.

## Paso 6 · Asunto

Si la oferta da un formato o código de referencia, úsalo tal cual. Si no:
- Español: `Postulación: [Puesto] - Eliam Paredes`
- Inglés: `Application: [Position] - Eliam Paredes`

## Paso 7 · Elección del CV (lo decide el script)

```
python Herramientas/puntuar_variantes.py Casos/<slug>/requisitos.md --idioma es
```
(`--idioma en` si la oferta está en inglés.)

- Copia la tabla que imprime.
- Si dice "usar …": ese es el adjunto (la ruta del PDF la da el script).
- Si dice "ninguna llega a 80%": ejecuta `cv-adaptador` desde
  `CV/cv_total.md` (sin inventar) y `cv-pdf` en la carpeta del caso. El
  adjunto es ese PDF.
- Si avisa que ni el `cv_total.md` llega a 80%: haz igual el mejor CV
  posible y lista los requisitos que faltan.
- Si dos variantes empatan, elige la que coincide con el título del puesto
  y dilo en una línea debajo de la tabla.
- Revisa los huecos a ojo: si un hueco es un sinónimo que faltó en
  `requisitos.md`, añádelo y vuelve a ejecutar.

## Paso 8 · Carta (cuerpo del correo)

Idioma de la oferta. **Solo texto corrido, nunca listas.** 80-130 palabras
y **máximo 700 caracteres con espacios** (saludo y firma incluidos).
Tono formal y directo, frases simples, sin rodeos. Cada frase conecta un
requisito de la oferta con algo real del CV maestro. Estructura fija:

1. Saludo: "Estimado [Nombre]," si se conoce; si no, "Estimado equipo de
   reclutamiento de [Empresa],". "Hola," solo si la oferta es informal.
   (Inglés: "Dear [Name]," / "Dear [Company] hiring team,".)
2. Párrafo 1 (2-3 frases): "Como [formación o perfil], cuento con
   experiencia en..." con las habilidades y herramientas de los must-have,
   usando las palabras de la oferta.
3. Párrafo 2 (2-3 frases): el beneficio concreto para la empresa, muy simple:
   "Aporto...", "Destaco por...", "Puedo encargarme de... para que [Empresa]...".
4. "Les invito a revisar mis proyectos en [enlace]." Elige el enlace que mejor
   muestre lo que pide la oferta:

   | La oferta pide | Enlace |
   |---|---|
   | Software, web, front-end, IA | https://eliam-paredes.github.io |
   | Código, repos | https://github.com/eliam-paredes |
   | Videojuegos | https://marav-stress.itch.io/ |
   | Video, animación, 3D en movimiento | https://youtu.be/In5x3WFofhs |
   | Arte 3D, diseño | https://www.behance.net/eliam_paredes |

5. "Quedo a su disposición para conversar sobre [esta oportunidad / cómo
   aportar a Empresa]."
6. "Atentamente," y "Eliam Paredes". (Inglés: "Sincerely," y "Eliam Paredes".)

Prohibido en la carta: hook de la empresa, listas de logros, cifras sueltas
que rompan la lectura, guiones largos, emojis, signos de exclamación. Pon
`[placeholder]` donde falte un dato.

## Paso 9 · Guardar `correo.md`

Con este formato exacto (el hook revisa palabras, caracteres y listas al
guardar; si se queja, corrige):

```
Para: [correo] [VERIFICADO]
Asunto: [asunto]
Adjunto: [ruta del PDF] ([N]% de encaje)

## Carta
[cuerpo completo]

## Encaje del CV
[tabla del script]
```

Luego añade una fila a `Casos/registro.md` con estado `lista para enviar`.

## Paso 10 · Borrador en Gmail (siempre al final)

Crea el borrador con `create_draft` (conector de Gmail). Nunca `send_message`.

- Solo si el correo destino es `[VERIFICADO]` (o Eliam lo confirmó). Si es
  `[correo por confirmar]` o `[INFERIDO]`, no crees el borrador: dilo en la
  respuesta.
- Solo si la respuesta de "¿Estafa?" es "No".
- `to`: el correo de `correo.md`. `subject`: la línea `Asunto:`.
- `body`: la carta en texto plano, sin Markdown, sin firma extra.
- `attachments`: el PDF elegido en el paso 7, en base64, con
  `filename` (nombre del PDF) y `mimeType: application/pdf`.
- Después, anota el id del borrador en `Casos/<slug>/correo.md` (línea
  `Borrador Gmail: [id]`) y cambia el estado en `registro.md` a
  `borrador en Gmail`.
- Si la herramienta de Gmail no está disponible, no lo des por hecho: deja
  el caso con estado `lista para enviar` y dilo en la respuesta.

## Paso 11 · Responder (UNA sola respuesta, en este orden)

```
## Correo
Para: ...  [VERIFICADO]
Asunto: ...
Adjunto: <ruta del PDF> (encaje %)
Borrador: <id de Gmail> (o motivo por el que no se creó)

## Carta
...

## Encaje del CV
| Variante | % | Parcial | Huecos |

## Empresa
(Skill 2 resumida)

¿Estafa? No
Siguiente paso: seguimiento a los 5-7 días (outreach-propuestas) o preparar la entrevista.
```

No envíes el correo ni hagas el siguiente paso hasta que lo pida.
