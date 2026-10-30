---
name: cv-auditor
description: >-
  Audita un CV (PDF, DOCX, texto o el cv.md de una postulación): puntúa
  compatibilidad ATS, claridad, impacto y credibilidad, detecta los patrones
  que hacen que Workday/Greenhouse/Lever/iCIMS lean mal campos (fechas solo con
  año, cargo y empresa pegados, etc.) y devuelve correcciones concretas. Usar
  cuando el usuario pide revisar, evaluar, auditar o "ver si pasa el ATS" un
  CV, propio o ajeno, o antes de enviar un CV importante.
---

# cv-auditor

Revisa un CV como lo verían un parser ATS y un reclutador con prisa. Basado en
ats-resume-skill (msdanyg, MIT) y ResumeSkills/resume-ats-optimizer (MIT).

## Input
- El CV: ruta (PDF/DOCX/MD), texto pegado, o `Casos/<slug>/cv.md`.
- (Opcional) La oferta, para medir cobertura de palabras clave.

## Proceso

### 1. Ver lo que ve la máquina
- **PDF:** extrae el texto con `python .claude/skills/cv-pdf/scripts/verificar_cv.py <pdf>`
  (o pypdf/pdftotext). Si sale vacío o desordenado, es un PDF imagen o de
  columnas: falla crítica.
- **DOCX:** extrae con python-docx; revisa si hay tablas, cuadros de texto o
  contenido en encabezado/pie.
- Guarda el texto plano junto al CV como `*-texto-ats.txt` para que el usuario
  vea lo que lee el parser.

### 2. Revisar patrones de fallo ATS
Lee `references/patrones-ats.md` y busca cada uno: fechas solo con año, marca
en minúsculas, cargo con paréntesis, empresa y lugar en la misma línea, marca
estilo dominio (.io), educación con viñeta y siglas, habilidades en columnas
con tabulador, contacto en encabezado/pie.

### 3. Revisar contenido
Con `../cv-adaptador/references/playbook-cv.md`:
- Bullets: ¿verbo + qué + resultado? ¿cuántos tienen número?
- Lista negra: foto, objetivo, "responsable de", prosa de IA, relleno.
- Longitud y palabras (objetivo ~475-600).
- Si hay oferta: cobertura de los must-have con su redacción literal.
- Si existe `CV/cv_total.md`: ¿alguna afirmación no está respaldada?

### 4. Puntuar
| Área | Peso |
|---|---|
| Lectura ATS (texto extraíble, campos, fechas, títulos) | 35 |
| Impacto (bullets XYZ, métricas) | 30 |
| Claridad y formato (longitud, coherencia, faltas) | 20 |
| Ajuste a la oferta (solo si hay oferta; si no, se reparte) | 15 |

## Output (conciso)

```
## Auditoría CV · [archivo] · [N]/100

### Críticos (arreglar antes de enviar)
- [problema] → [corrección exacta, con la línea antes/después]

### Mejoras
- [problema] → [corrección]

### Bien
- [lo que ya funciona, 2-3 puntos]

### Prueba de pegado
- Texto ATS guardado en [ruta]. Campos que probablemente salgan vacíos: [lista o "ninguno"].
```

Ofrece aplicar las correcciones: si el CV viene de `cv.md`, edítalo y
regenera con `cv-pdf`; si las correcciones revelan datos nuevos, guárdalos con
`cv-maestro`.

## Reglas
- Señala el problema con la línea literal del CV y su versión corregida.
- No reescribas logros inventando números: si falta la métrica, di
  "añade un número aquí" y pregunta.
- Diferencia lo que rompe el parseo (crítico) de lo que es preferencia.
