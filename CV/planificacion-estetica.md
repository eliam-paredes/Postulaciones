# Planificación: cambios estéticos de los CV

Estado: aplicado a las 16 versiones de variantes/ (ES y EN), 2026-11-04. Verificado con verificar_cv.py.

## 1. Encabezado
- Nombre centrado (`h1`, `text-align: center`).
- Titular centrado (la línea debajo del nombre).
- Línea de contacto centrada.
- Titular sin la palabra "Junior" (ES: "Desarrollador de Software ·…"; EN: "Software Developer ·…"). Regla: el CV no debe decir que es novato. El objetivo "roles junior y mid" de `cv_total.md` es interno y no cambia.

## 2. Colores y enlaces
- Texto normal en gris `#4a4a4a`. Contacto en `#555`, titular en `#333`.
- Puesto (`h3`) y títulos de sección (`h2`) en negro (`#000` / `#111`), así el puesto destaca sobre la empresa.
- Todos los enlaces en azul `#1a56db` con subrayado.

## 3. Línea de cada puesto
- Estructura: puesto a la izquierda, fecha a la derecha, en la misma línea.
- Empresa en la misma línea, después del puesto, separada con `|`.
  - Ejemplo: `Fundador y Desarrollador de Software | Marav Studios`.
- Puesto: 11.5pt, negrita, negro.
- Empresa: 10pt, normal, gris `#555`.
- Fecha: 9.5pt, alineada a la derecha, `white-space: nowrap`.
- Se usa flexbox (`display: flex; justify-content: space-between`). No se usan tablas.

## 4. Espaciado (la segunda ronda, a pedido de Eliam)
| Elemento | Valor final | Antes |
|---|---|---|
| Título de sección `h2` | margen 20pt arriba, 8pt abajo | 7pt / 3pt |
| Línea del puesto `.rol` | margen 10pt arriba, 3pt abajo | 4pt / 0 |
| Bloque de cada trabajo `.bloque` | 10pt abajo | 0 |
| Lista `ul` | 2pt arriba, 3pt abajo | 1pt / 2pt |
| Elemento `li` | 2pt abajo | 1pt |

La versión 01 ES queda en 1 página con ~20% libre. Si se quiere más aire, subir `h2` y `.bloque` antes que la fuente.

## 5. Cambios en el código
- **Variante 01 (ya hecho):** HTML fuente `Eliam-Paredes-CV-Software-Engineer-ES.html` y EN `Eliam-Paredes-Resume-Software-Engineer-EN.html`. Se regeneran los PDF con Microsoft Edge en modo headless (`--print-to-pdf`).
- **Resto de variantes:** cada una tiene su HTML con el CSS antiguo. Copiar el bloque `<style>` de la 01 ES y reescribir la estructura de cada rol (`div.rol` con `h3` + `span.empresa` + `p.fechas`).
- **Ideal a largo plazo:** actualizar `Skills/cv-pdf/templates/cv.css` y `scripts/generar_cv.py` (función `md_a_html`), para que el PDF generado desde `cv.md` salga igual sin tocar HTML a mano. Hay que hacer que `md_a_html` junte la línea de `###` con la empresa y la fecha en un solo bloque `.rol`. Esto sería un cambio en la skill, así que va registrado en `CV/estilo.md`.

## 6. Reglas a registrar en `CV/estilo.md`
- Encabezado centrado; enlaces azul subrayado; texto gris; puesto destacado; empresa al lado del puesto con `|`; fecha a la derecha. (ya registrado 2026-11-04)
- Espaciado de la sección 4. (pendiente de registrar)
- Sin "Junior" en el titular ni en ningún texto del CV. (pendiente de registrar)

## 7. Verificación antes de dar por bueno un CV
- Sigue en 1 página (`pypdf`).
- Sin "junior" en el texto del PDF.
- Fechas en formato `Mes AAAA`.
- Regenerar el `*-texto-ats.txt` si cambió el texto.
- Revisar una captura visual del PDF.
