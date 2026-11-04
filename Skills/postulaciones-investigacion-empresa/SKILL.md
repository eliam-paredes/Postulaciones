---
name: postulaciones-investigacion-empresa
description: >-
  Investiga con búsqueda web real la empresa de una oferta: qué hace, stack y
  cultura, competidores, noticias recientes y qué importa para la entrevista,
  con etiquetas [VERIFICADO] / [INFERIDO] / [SUPOSICIÓN]. Usar cuando el
  usuario va a postular o entrevistar en una empresa. Es la Skill 2 del flujo
  de postulación.
---

# postulaciones-investigacion-empresa

Objetivo: entender la empresa lo bastante para hablar su idioma en la carta y
en la entrevista. Datos útiles, no trivia.

## Qué leer (no preguntes, lee)

- `Casos/<slug>/oferta.md`: nombre de la empresa, web, país, puesto.
- `Casos/<slug>/analisis.md` si existe: los pain points.

Si la oferta no dice la empresa, búscala con frases literales de la oferta
antes de preguntar.

## Búsquedas obligatorias (WebSearch / WebFetch)

Haz al menos estas 5. Cambia `EMPRESA` por el nombre real:

1. `EMPRESA` → web oficial. Abre la home y la página "about" o "nosotros".
2. `EMPRESA careers` o `EMPRESA empleo` → página de empleo y otras vacantes
   (dicen mucho del stack y del momento de la empresa).
3. `EMPRESA LinkedIn` → tamaño, sede, sector.
4. `EMPRESA noticias 2026` (o el año actual) → lanzamientos, rondas,
   clientes, despidos.
5. `EMPRESA Glassdoor` o `EMPRESA opiniones empleados` → patrón de reseñas.

Si el puesto es técnico, añade `EMPRESA engineering blog` o `EMPRESA github`.

Si no aparece casi nada (empresa pequeña o nueva), dilo en la primera línea:
"Poca presencia pública: análisis limitado". No rellenes con suposiciones.

## Etiquetas (obligatorias en cada dato)

- **[VERIFICADO]**: lo leíste en una fuente. Pon la URL al lado.
- **[INFERIDO]**: deducido de datos verificados (di de cuáles).
- **[SUPOSICIÓN]**: lógica del sector, sin fuente. Úsala poco.

## Salida (5 secciones, resumidas)

```
## Empresa · [Nombre]

**1. Qué hace**
- Qué vende y a quién: ... [VERIFICADO] (url)
- Cómo gana dinero: ... [INFERIDO]
- Etapa y tamaño: ... [VERIFICADO] (url)

**2. Tech y cultura**
- Stack: ... [VERIFICADO] (url de la vacante o del blog)
- Forma de trabajar: ... [INFERIDO]
- Señales de cultura: ... [VERIFICADO] (url)

**3. Competencia**
- Competidores: ... [INFERIDO]
- En qué se diferencian: ... [INFERIDO]

**4. Noticias y tendencias**
- [Mes AAAA]: [hecho] → [por qué importa para este puesto] [VERIFICADO] (url)

**5. Lo que importa para la postulación**
- [Insight accionable 1: qué problema o momento tiene la empresa]
- [Insight accionable 2: qué beneficio de Eliam le importa más]
```

Máximo 2-3 líneas por sección. Guarda lo mismo en `Casos/<slug>/empresa.md`.

## Control antes de responder

- [ ] Hiciste las búsquedas de verdad (no escribas desde memoria).
- [ ] Cada [VERIFICADO] tiene su URL.
- [ ] Ninguna cifra (empleados, ventas, rondas) sin fuente.
- [ ] La sección 5 tiene al menos un insight que sirva para la carta o la respuesta.
