---
name: postulaciones-analisis-requerimientos
description: >-
  Analiza una oferta de empleo para Eliam: must-have, nice-to-have, pain
  points, mapa contra su CV (CV/cv_total.md) y si es sospechosa de estafa.
  Usar cuando el usuario pega una oferta de trabajo (texto, archivo o URL) o
  pide "analiza esta oferta". Es la Skill 1 del flujo de postulación.
---

# postulaciones-analisis-requerimientos

Objetivo: decir en pocas líneas qué necesita de verdad la empresa y qué tiene
Eliam para cubrirlo. Nada más.

## Qué leer (no preguntes, lee)

1. `Casos/<slug>/oferta.md`: la oferta literal.
2. `CV/cv_total.md`: la única fuente de la experiencia de Eliam.

Solo pregunta al usuario si no hay oferta. Si falta un dato del candidato,
márcalo como hueco y sigue.

## Pasos

1. **Must-have (máx. 5).** Lo que haría descartar al candidato si falta. Pistas:
   "requerido", "imprescindible", "must", "X+ años", lo que se repite, lo que
   aparece en el título del puesto. Si la oferta lista 15 "requisitos", elige
   los 5 que más se repiten o que van primero.
2. **Nice-to-have.** "Deseable", "plus", "valorable", "bonus", "nice to have".
3. **Pain points.** Busca frases que revelan un problema. Cita la frase literal.

   | Frase en la oferta | Problema real probable |
   |---|---|
   | "Equipo en crecimiento rápido" | Mucho trabajo y poco proceso |
   | "Desde cero" | No hay base; deuda técnica previa |
   | "Dinámico / alta presión" | Plazos cortos o prioridades que cambian |
   | "Autónomo / proactivo" | Poca guía de un senior |
   | "Varias tecnologías / multitarea" | Una persona cubre varios roles |
   | "Comunicación con clientes" | Han tenido problemas de entregas o expectativas |

   No inventes pain points. Si no hay ninguno claro, escribe "No se detectan
   pain points claros en el texto".
4. **Mapa candidato → necesidad.** Para cada must-have (y los nice-to-have
   importantes), busca en `cv_total.md` la mejor evidencia: proyecto, rol o
   métrica. Usa solo lo que está escrito ahí. Estado:
   - **Cumple**: hay proyecto o rol real que lo demuestra.
   - **Parcial**: solo aparece en habilidades, o la evidencia es floja.
   - **Hueco**: no aparece. Nunca lo tapes.
5. **¿Estafa?** "Sí" si hay 2 o más de estas señales: piden pago o compra de
   equipo, piden datos bancarios o documentos antes de entrevistar, sueldo
   muy alto para el nivel sin explicación, correo personal (gmail, hotmail)
   que dice ser de una empresa grande, no existe la empresa en la web,
   contratan solo por chat (Telegram, WhatsApp). Si no, "No".

## Salida (exacta, sin secciones extra)

```
## Análisis de requerimientos

**Must-have**
1. [requisito] ([por qué en 4-8 palabras])
2. ...

**Nice-to-have**
- [requisito], [requisito], [requisito]

**Pain points**
- "[frase literal]" → [problema real, una línea]

**Mapa candidato → necesidad**
| Necesidad | Evidencia de Eliam | Estado |
|---|---|---|
| React | Planeao y CV_buildeao (React, TypeScript, Vite) | Cumple |
| GraphQL | - | Hueco |

**¿Sospechoso de estafa?** No
```

Guarda lo mismo en `Casos/<slug>/analisis.md`.

## Control antes de responder

- [ ] Máximo 5 must-have, una línea cada uno.
- [ ] Cada pain point cita una frase que existe en la oferta.
- [ ] Cada evidencia del mapa existe en `cv_total.md` (proyecto, rol o métrica real).
- [ ] Los huecos están marcados como "Hueco", no escondidos.
- [ ] La línea de estafa dice solo "Sí" o "No", sin explicación.
- [ ] Sin sección de "Alertas", sin introducción ni cierre.
