---
name: postulaciones-generador-respuesta
description: >-
  Genera respuestas persuasivas y auténticas a "¿Por qué quieres trabajar aquí?"
  aplicando principios de Dale Carnegie (How to Win Friends and Influence People)
  y técnicas de alto valor de Ofertas de 100MM. Use cuando el usuario prepara
  entrevistas tech y necesita una respuesta que conecte emocionalmente con el
  entrevistador mientras demuestra valor concreto.
---

# postulaciones-generador-respuesta

Esta skill construye respuestas a la pregunta "¿Por qué quieres trabajar aquí?"
que funcionan porque están escritas desde la perspectiva del otro, no desde tus
necesidades.

Se basa en dos fuentes:

- **"How to Win Friends and Influence People"** de Dale Carnegie — principios
  de hacer genuino interés por los demás, ver las cosas desde su punto de vista,
  despertar un deseo apasionado en ellos, y hacerlo de forma que se sientan
  importantes.
- **"Ofertas de 100MM"** — técnicas de posicionamiento de alto valor: crear
  deseo mutuo, no pedírir, ofrecer valor antes de pedir nada, dramatizar tu
  idea con ejemplos concretos, y anclarte como solución a un problema real.

## Input

Pide al usuario:

- Información de la empresa (o referencia a output de `postulaciones-investigacion-empresa`).
- Análisis del puesto con pain points (o referencia a `postulaciones-analisis-requerimientos`).
- Experiencia clave, intereses y motivaciones reales del candidato.
- Cualquier detalle personal genuino (producto que usan, artículo que leyeron,
  conversación con alguien de la empresa, etc.).

Si falta información, trabaja con lo disponible pero señala los huecos.

## Principios aplicados

### De Dale Carnegie (los que realmente importan aquí):

1. **"No critiques, condenes ni te quejes"** — La respuesta nunca menciona
  problemas de tu empleador actual ni se posa como escape. Se centra en atracción,
  no en fuga.

2. **"Dar apreciación honesta y sincera"** — Mencionar algo específico que admiras
  de la empresa (producto, postura pública, hito) de forma genuine, no adulación.
  Carnegie lo dice claro: la adulación barata se detecta.

3. **"Despertar en el otro un deseo apasionado"** — No hablas de lo que tú ganas,
  hablas de lo que ellos ganan. Estructures la respuesta para que el entrevistador
  piense: "este quiere ayudarnos a resolver X, no solo conseguir un salario".

4. **"Ver las cosas desde el punto de vista del otro"** — La respuesta habla el
  idioma de la empresa, no el tuyo. Si su dolor es escalar infraestructura, hablas
  de escalabilidad, no de que te gusta aprender nuevas tecnologías.

5. **"Hacer que el otro se sienta importante — de manera genuina"** — Conectas tu
  historia con logros reales del equipo o visión del CEO. Reconoces lo que ya
  lograron antes de proponer lo que harías.

### De Ofertas de 100MM:

6. **"Crear deseo mutuo, no pedir"** — Posiciona tu respuesta como propuesta de
  valor, no como súplica. "Quiero aportar mi experiencia en Y a su reto de X"
  no "Necesito este trabajo porque...".

7. **"Ofrecer valor antes de pedir"** — Incluye al menos una observación concreta
  sobre cómo podrías contribuir, no solo intenciones. Los detalles específicos
  crean credibilidad.

8. **"Dramatizar tus ideas"** — Usa un ejemplo breve y concreto en lugar de
  adjetivos abstractos. En lugar de "soy proactivo", cuenta en una frase "identifiqué
  un bottleneck en X que ahorró Y horas semanales".

9. **"Anclarte como solución, no como solicitante"** — Cerrá la respuesta
  recordando tácitamente el problema que resuelves, no repitiendo tu título.

## Proceso

### Paso 1: Identificar el hook emocional correcto

Dependiendo de la empresa y su momento actual, elige un hilo central:

- **Resolución de problema técnico complejo** — Ideal para empresas con pain
  points operativos claros detectados en el análisis de requerimientos.
- **Alineación con misión/visión** — Para empresas con propósito definido o
  productos que el usuario usa realmente.
- **Oportunidad de impacto y crecimiento** — Para startups en escala donde el
  margen de influencia es mayor.
- **Ecosistema tecnológico** — Cuando el stack, la arquitectura o el enfoque
  técnico es el imán real.

Unica respuesta = un hilo principal con soporte secundario. No mezcles cuatro
motivos en una respuesta de 60 segundos.

### Paso 2: Construir la estructura narrativa

Usa esta estructura (basada en Carnegie + Ofertas 100MM):

```
[APRECIACIÓN GENUINA] Lo que admirás de la empresa (algo específico, verificable).

[PUENTE DESDE SU PERSPECTIVA] Cómo ese aspecto conecta con UN problema o
  oportunidad que ellos enfrentan actualmente (tu investigación habla aquí, no tus
  deseos).

[VALOR CONCRETO] Un ejemplo breve y dramatizado de algo similar que resolviste
  o resultados que generaste (números, no adjetivos).

[CERRAR CON DESEO MUTUO] Qué aporta TU combinación específica a SU momento actual,
  planteado como propuesta bidireccional, no como petición.
```

### Paso 3: Redactar dos variantes + opción bonus

- **Opción A — Impacto técnico y resolución de retos**
  Enfocada en pain points del puesto,_stack_, desafíos arquitectónicos o de
  producto. La más indicada para roles IC deep-tech.

- **Opción B — Misión, producto y alineación cultural**
  Enfocada en propósito, visión, producto real que el candidato usa/conoce, y
  cómo su crecimiento personal se alinea con el de la empresa.

- **Opción C (bonus) — Breve/pitch de 30 segundos**
  Versión condensada para situaciones informales: coffee chat, networking, primer
  round con HR.

### Paso 4: Lint de detección de IA / autenticidad

Antes de entregar, revisa cada respuesta contra estos check-lists de Carnegie
adaptados:

| check | qué buscar |
| --- | --- |
| ¿Es específica? | Menciona nombres, productos, hitos reales, no "su innovadora cultura" |
| ¿Es verificable? | Todo lo que dice sobre la empresa puede comprobarse en 30 segundos en Google |
| ¿Habla de "nosotros" o de "yo"? | Debería equilibrarse. Demasiado "yo" = egoísmo. Demasiado "ustedes" = adulación vacía |
| ¿Hay números concretos? | Al menos uno en cada respuesta (resultado medible, métrica, escala) |
| ¿El cierre apela a valor mutuo? | Termina en intercambio, no en necesidad |
| ¿Suena como humano escribiéndole a otro humano? | Sin frases tipo "Me entusiasma la oportunidad de formar parte de su dinámico equipo liderado por visionarios". Carnegie diría que eso es "hablar sin convicción" |

## Output

```
### ESTRATEGIA: Hook seleccionado — [tipo de hilo elegido]
[Razón de por qué este hook es el mejor para ESTE puesto en ESTE momento de la
empresa]

### PUNTOS CLAVE A MENCIONAR (conectar explícitamente)
1. [Elemento de la empresa que debes nombrar]
2. [Pain point o necesidad que tu respuesta aborda]
3. [Resultado o experiencia del candidato que funciona como prueba]

### OPCIÓN A: Enfoque Técnico y Resolución de Retos (~60-90 segs hablados)
"[Texto completo de la respuesta. Escrito para decirlo oralmente, no para leerlo.]"

— Por qué funciona: [Conexión con principio de Carnegie + lógica de Ofertas 100MM]

### OPCIÓN B: Enfoque Misión, Producto y Cultura (~60-90 segs hablados)
"[Texto completo de la respuesta.]"

— Por qué funciona: [Conexión con principio de Carnegie + lógica de Ofertas 100MM]

### OPCIÓN C: Pitch Express (~30 segs)
"[Versión corta para coffee chat / networking.]"

### ADAPTACIONES RECOMENDADAS
- Lo que el candidato debería cambiar con SU información real: [breve lista]
- Lo que NUNCA debería mencionar (red flags en respuesta): [lista]
- Señales de que el entrevistador está conectado con tu respuesta: [qué observar
  para saber si funcionó]
```

## Reglas

- **Nunca inventes datos sobre la empresa.** Si no estás seguro de algo, omítelo.
  Una respuesta con medias verdades es peor que una respuesta simple.
- **La respuesta debe sonar como el candidato, no como un manual corporativo.**
  Si usas palabras que el candidato nunca usaría naturalmente, cámbialas o
  marcalas como adaptables.
- **Si el candidato no tiene experiencia directa relevante, enfoca en transferencia
  de habilidades y curiosidad genuina** — Carnegie dice que el interés sincero por
  el otro vale más que cualquier talento superficial.
- **Incluye siempre al menos un número o métrica concreta** en cada respuesta larga.
  Los números dramatizan tu idea mejor que cualquier adjetivo (Ofertas 100MM).
- **Prohibido mencionar** problemas con empleador actual, salario como motivación,
  ubicación geográfica como razón principal, o frases genéricas como "crecer
  profesionalmente". Eso debilita tu posición inmediatamente.
