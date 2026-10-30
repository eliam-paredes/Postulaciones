---
name: postulaciones-analisis-requerimientos
description: >-
  Analiza ofertas de empleo tech: prioriza requerimientos críticos, mapea pain
  points implícitos y conecta fortalezas del candidato con necesidades reales de
  la empresa. Use cuando el usuario pega una oferta de trabajo y quiere entender
  qué importa realmente, qué problemas ocultos resuelve esa vacante y cómo
  posicionarse como el candidato ideal.
---

# postulaciones-analisis-requerimientos

Analiza una oferta de empleo desde la perspectiva de quien la escribe y de quien
la resuelve. No se trata de listar requisitos como un copiar-y-pegar, sino de
descifrar qué está pasando realmente detrás de esas líneas y por qué la empresa
no lo dice explícitamente.

## Input

Pide al usuario:

- La descripción completa de la oferta laboral (texto pegado o archivo).
- (Opcional) El CV o resumen profesional del candidato para cruce directo.

Si solo hay la oferta, trabaja con eso e indica dónde falta información del
candidato.

## Proceso

### 1. Desglosar los requerimientos sin repetir la oferta

Lee la descripción y clasifica cada requisito en:

- **Hard Skills**: tecnologías, frameworks, herramientas, metodologías.
- **Soft Skills**: comunicación, liderazgo, autonomía, resolución de conflictos.
- **Requerimientos implícitos**: lo que da por sentado pero no dice (ej: "trabajo
  autónomo" puede significar "nadie va a supervisarte").

### 2. Priorizar: cuáles son indispables y cuáles son deseables

No todo lo escrito tiene el mismo peso. Clasifica en tres niveles:

| nivel | criterio | ejemplo |
| --- | --- | --- |
| **Must-have** | Si no lo tienen, descartan al candidato de inmediato | "5+ años con React" |
| **Nice-to-have** | Suman puntos pero no bloquean | "Experiencia con GraphQL" |
| **Red flag indirecto** | Algo que revela un problema real | "Buscamos growth hacker" para un rol de mantenimiento |

Limita los must-have a 3-5 máximo. Si la oferta enumera 20 cosas como
indispensables, el que redactó no sabe qué necesita ni él mismo — y eso es
información útil también.

### 3. Detectar Pain Points (lo que NO dicen directamente)

Los pain points están embebidos en el lenguaje. Busca patrones como:

| frase en la oferta | dolor probable |
| --- | --- |
| "Equipo en crecimiento rápido" | Todo cae sobre una persona; falta proceso |
| "Desde cero" | Inconsistencia técnica previa; deuda acumulada |
| "Alta presión / dinámico" | Plazos irreales o giros constantes de prioridad |
| "Autónomo / proactivo" | Ausencia de mentoría o guía senior |
| "Múltiples stack technologies" | Fragmentación, poco foco |

Para cada pain point identificado, escribe qué problema operativo real podría
estar resolviendo la empresa con esta contratación. Sé específico, no genérico.

### 4. Mapear fortalezas del candidato contra lo crítico

Si el CV está disponible, cruza cada must-have con la experiencia del candidato.
Para cada match, redacta una línea de conexión directa entre lo que necesitan y
lo que el candidato ya resolvió. Si falta algún must-have, sugiere cómo mitigarlo
(experiencia transferible, proyectos personales, enfoque diferente).

## Output

```
### ANÁLISIS DE OFERTA · [Título del puesto]
[Empresa] · [Fecha]

### 1. REQUERIMIENTOS CRÍTICOS (Must-Have)
1. **[Requerimiento]** — Por qué es indispensable: [razón concreta]
2. **[Requerimiento]** — Por qué es indispensable: [razón concreta]
3. **[Requerimiento]** — Por qué es indispensable: [razón concreta]

### 2. Nice-to-Have (diferenciadores)
- **[Habilidad]** — Su valor si tienes experiencia.
- **[Habilidad]** — ...

### 3. PAIN POINTS DETECTADOS (Lo que probablemente necesitan resolver)
- **[Dolor 1]** — Frase clave de la oferta que lo revela: "[cita textual]"
  Qué problema opera: [descripción del problema real subyacente]
- **[Dolor 2]** — ...

### 4. MAPA CANDIDATO → NECESIDAD
[Vacío si no se proporcionó CV]

### 5. ALERTAS
- Lo que parece bueno pero es señal de problema (si aplica).
- Lo que falta en la descripción y debería investigarse antes de la entrevista.
```

## Reglas

- Nunca inventes pain points que no estén respaldados por evidencia textual de la
  oferta. Dilo abiertamente si no detectas ninguno claro.
- Si la oferta es ambigua o genérica (copiada de un portal), indícalo y explica
  qué información adicional se necesitaría para un análisis real.
- Señala siempre cuándo algo es inferencia tuya vs dato directo del texto.
