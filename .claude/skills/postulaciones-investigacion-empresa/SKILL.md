---
name: postulaciones-investigacion-empresa
description: >-
  Investiga empresas tech: modelo de negocio, cultura, stack, competidores y
  contexto estratégico relevante para entrevistas. Use cuando el usuario va a
  postular o entrevistar en una empresa y necesita entender de qué va realmente,
  quiénes son sus rivales, y qué está pasando en su sector.
---

# postulaciones-investigacion-empresa

Investigar una empresa antes de una entrevista no es coleccionar datos triviales.
Es construir una lectura estratégica que te permita hablar el mismo idioma que
quien te evalúa y demostrar que entiendes su mundo mejor que otros candidatos.

## Input

Pide al usuario:

- Nombre de la empresa.
- URL de la oferta de empleo, website u otra fuente relevante.
- (Opcional) Industria o país si no es obvio.

## Proceso

### 1. Identificar a la empresa realmente

Va más allá del nombre. Determina:

- **¿Qué vende exactamente?** Producto, servicio, licensing, subscription,
  transaction fee. Sé específico, no digas "hacen software".
- **¿A quién se lo venden?** B2B, B2C, B2B2C, enterprise, SMB, developer-led.
- **¿Cómo generan ingresos?** Subscription SaaS, on-premise licensing, marketplace
  take rate, ads, consulting services, hardware + software bundle.
- **¿En qué etapa están?** Seed, Series A, scale-up, public enterprise, bootstrap/
  profitable. Esto define urgencias diferentes.

### 2. Stack tecnológico y enfoque de ingeniería

Infiere o investiga:

- Tecnologías probables según el producto y el rol mencionado.
- Metodologías comunes en empresas de esa etapa/sector.
- Señales culturales: "agile", "data-driven", "move fast", "enterprise-grade"
  cada una comunica valores distintos sobre velocidad vs estabilidad.

Si puedes encontrar evidencias concretas (blog engineering, talks de devs,
stack shared en Glassdoor, jobs postings pasados), agrégalas y cita la fuente.

### 3. Contexto competitivo

- **Competidores directos:** Quiénes compiten por el mismo cliente/producto.
- **Competidores indirectos:** Soluciones alternativas que reemplazan su categoria.
- **Posicionamiento:** En qué intentan diferenciarse (price, feature, UX, support,
  ecosystem).

### 4. Hitos recientes y tendencias del sector

Busca o razona sobre:

- Rondas de financiamiento recientes (si aplica).
- Lanzamientos de producto, partnerships, adquisiciones.
- Cambios regulatorios relevantes para su industria.
- Tendencias macro que afectan su mercado (IA, cloud consolidation, security
  mandates, etc.).

Esto no es trivia. Es lo que te permite decir en una entrevista: "Vi que lanzaron
X producto el mes pasado y considerando Y cambio en la industria, tiene sentido
que necesiten alguien enfocándose en Z".

### 5. Cultura e indicadores indirectos

Sin vivir dentro de la empresa, usa señales públicas:

- LinkedIn: antigüedad promedio de empleados, turnover visible.
- Reviews (Glassdoor/Indeed): patrón recurrente en comentarios positivos Y
  negativos (no tomes uno aislado).
- Contenido público: tono de blog, participaciones en conference, contribuciones
  open-source. Todo habla de prioridades reales, no las que pintan en la pared.

## Output

```
### INVESTIGACIÓN DE EMPRESA · [Nombre]
[Fuente principal consultada]

### 1. RESUMEN EJECUTIVO
- **Qué hace:** [1-2 oraciones precisas sobre qué venden y a quién]
- **Modelo de negocio:** [cómo generan ingresos]
- **Etapa:** [seed / series / scale-up / public / bootstrap]

### 2. ENFOQUE TECH Y CULTURA
- **Stack probable / tecnologías asociadas:** [lista fundamentada]
- **Metodología / filosofía de ingeniería:** [inferida de fuentes públicas]
- **Señales culturales:** [turnover, contenido, reviews — con advertencia de
  confiabilidad]

### 3. CONTEXTO COMPETITIVO
- **Competidores directos:** [nombres]
- **Posicionamiento diferencial:** [qué intentan ganar]
- **Competidores indirectos / amenazas:** [alternativas del mercado]

### 4. HITOS RECIENTES Y TENDENCIAS
- **[Evento/Hito]:** [fecha + relevancia para el puesto]
- **[Tendencia de sector]:** [cómo impacta su negocio]

### 5. LO QUE IMPORTA PARA LA ENTREVISTA
[2-3 insights accionables. Esto es lo único que el candidato debería memorizar.]
  Ejemplo: "Su dolor actual es escalar infraestructura tras la ronda Serie B.
   Tu respuesta debe conectar con ese momento específico, no hablar de tecnología
   en abstracto."
```

## Reglas

- Siempre distingue entre hecho verificado, inferencia fundamentada y suposición.
  Usa etiquetas: `[VERIFICADO]`, `[INFERIDO]`, `[SUPOSIÓN]`.
- Si la empresa es muy nueva, privada o de nicho sin presencia digital, dilo
  claramente y adapta el alcance del análisis. Mejor ser honesto que inventar.
- No termines la investigación hasta tener al menos un insight accionable para
  la entrevista. Datos sin utilidad no son investigación, son trivia.
