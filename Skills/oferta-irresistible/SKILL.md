---
name: oferta-irresistible
description: >-
  Diseña ofertas irresistibles con el método de Alex Hormozi ($100M Offers):
  nicho, resultado soñado, ecuación de valor, problemas → soluciones, apilado
  de valor, precio, garantía, escasez, urgencia, bonos y nombre. Usar cuando el
  usuario quiere armar o mejorar una oferta de servicios (freelance 3D web,
  front-end, integración de IA para empresas), un paquete, un precio, un
  pitch de venta o su propuesta de valor como candidato. Guarda el resultado
  en Ventas/ofertas/.
---

# oferta-irresistible

Una oferta tan buena que decir que no se siente tonto. No se trata de bajar
el precio sino de subir el valor percibido. Basado en hormozi-skills
(alexsmedile, MIT) y grand-slam-offer (OnePathToFreedom, MIT). Los marcos
están explicados con palabras propias en `references/marcos-hormozi.md`:
léelo antes de empezar.

## Contexto del usuario
Lee `CV/cv_total.md` (si existe) para saber qué puede ofrecer de verdad:
React/front-end, 3D en web (Three.js), Unity, diseño, integración de IA,
freelance en Upwork, Marav Studios. Las pruebas (casos, números, reviews)
salen solo de ahí o de lo que diga el usuario.

## Modos
| Situación | Modo |
|---|---|
| Quiere vender un servicio, paquete o producto | **OFERTA** (completo) |
| Ya tiene una oferta y no vende | **AUDITORÍA**: puntúa con la ecuación de valor, señala lo débil y reconstruye |
| Necesita un pitch corto (30-60 s, bio, Upwork overview) | **PITCH**: pasos 1-3 + mensajes |
| Se "vende" como candidato a una empresa | **CANDIDATO**: ver abajo |

## Proceso (modo OFERTA)

Trabaja por fases y para al final de cada una para que el usuario reaccione.
No preguntes lo que ya se sabe; máximo 3-4 preguntas por ronda.

**Fase 1 · Mercado y cliente**
1. Resume lo que entiendes: "ayudas a X a lograr Y con Z" y qué falta.
2. Elige el nicho con los 4 filtros (dolor fuerte, poder de compra, fácil de
   encontrar, mercado creciendo). Propón 3 direcciones y recomienda 1.
3. Avatar en una frase, situación actual, intentos fallidos.

**Fase 2 · Resultado y valor**
4. Resultado soñado: lo que el cliente compra de verdad (no lo que haces).
5. Ecuación de valor: cómo subir resultado y probabilidad percibida, cómo
   bajar tiempo y esfuerzo. 3-5 ideas accionables en cada lado.

**Fase 3 · Construir la oferta**
6. Lista 10-15 obstáculos que el cliente encontrará antes, durante y después.
7. Convierte cada obstáculo en solución y elige el vehículo de entrega
   (hecho por ti, hecho contigo, hazlo tú; 1 a 1, grupo, plantilla,
   automatización, auditoría…).
8. Recorta y apila: quédate con lo de alto valor y bajo costo de entregar.

**Fase 4 · Potenciar y vender**
9. Precio: ancla con el valor del resultado, no con tus horas. Justifícalo.
10. Garantía: propone 3 tipos y recomienda una para este caso.
11. Escasez, urgencia y bonos, siempre honestos (nada de cuentas atrás falsas).
12. Nombre con la fórmula MAGIC.
13. Mensajes: 3-5 ganchos, 3 bullets de resultado, 3 respuestas a objeciones,
    pitch de 30 s y llamada a la acción.

Al terminar, guarda `Ventas/ofertas/<nombre-corto>.md` con el formato de
abajo.

## Modo CANDIDATO
Trata a la empresa como cliente y a Eliam como la oferta:
- Resultado soñado = el pain point principal del puesto (usa
  `Casos/<slug>/analisis.md` si existe).
- Probabilidad percibida = pruebas del CV maestro (proyectos, números).
- Tiempo = qué puede entregar en los primeros 30/60/90 días.
- Esfuerzo = qué le ahorra al equipo (no necesita formación en X, etc.).
Salida: pitch de 30-60 s + 3 pruebas + plan de 30/60/90 en 3 líneas. No
repitas lo que ya hace `postulaciones-generador-respuesta`.

## Formato de salida (Ventas/ofertas/<nombre>.md)
```
# [Nombre MAGIC de la oferta]
## Para quién es (y para quién no)
## Resultado soñado
## Ecuación de valor
- Sube resultado / probabilidad: ...
- Baja tiempo / esfuerzo: ...
## Qué incluye (valor apilado)
| Componente | Qué resuelve | Valor percibido |
## Precio y justificación
## Garantía
## Escasez / urgencia / bonos
## Mensajes
- Ganchos · Bullets · Objeciones · Pitch 30 s · CTA
## Próximos pasos
```

## Reglas
- Nunca inventes casos, clientes, testimonios ni números. Si no hay prueba,
  la oferta usa garantía y muestra gratis para compensar, no humo.
- Lenguaje simple y concreto. Nada de "transforma tu negocio" sin decir cómo,
  cuánto y en cuánto tiempo.
- Cuestiona las ideas débiles con respeto y propone la versión más afilada.
- Si el usuario está saturado, reduce a una sola recomendación.
- No cites ni copies texto de los libros de Hormozi; aplica los marcos.
