# Patrones de fallo ATS (con antes y después)

Adaptado de ats-resume-skill/references/failure-patterns.md (msdanyg, MIT).
Ninguno se ve mal a ojo humano; por eso hay que hacer la prueba de pegado
(seleccionar todo → copiar → pegar en un editor de texto).

## 1. Fecha solo con año (el más común)
Antes: `2020 – 2024` → algunos parsers dejan TODO el puesto sin fechas.
Después: `Nov 2020 – Abr 2024`. Si no recuerda el mes, usa uno fijo (Ene) siempre igual.

## 2. Cargo con paréntesis descriptivo
Antes: `Desarrollador Front-end (React & Three.js)` → el parser puede tomar el
paréntesis como empresa.
Después: `Desarrollador Front-end`. El detalle va al titular bajo el nombre o a un bullet.

## 3. Empresa y lugar en la misma línea
Antes: `Promo Design DP Group, Santo Domingo` → se lee como ubicación y la empresa queda vacía.
Después: `Promo Design DP Group` sola en su línea. La ciudad va en el contacto.

## 4. Marca en minúsculas o estilo dominio
Antes: `maravstudios` o `Marav.io` → parece palabra común o URL.
Después: `Marav Studios`.

## 5. Educación con viñeta, siglas y guion
Antes: `• Ing. Software — UNAPEC` → la sección puede salir vacía.
Después:
```
Ingeniería de Software
UNAPEC
Abr 2024 – Actualidad
```
Grado escrito completo; si hay sigla, junto al nombre completo.

## 6. Habilidades en columnas con tabulador
Antes: `React	Three.js	Unity` alineado en columnas → se mezclan con otras líneas.
Después: una línea por grupo: `Front-end: React, TypeScript, Vite`.

## 7. Contacto en encabezado o pie de página
Varios parsers (Workday entre ellos) ignoran encabezados/pies. El contacto va en el cuerpo.

## 8. Freelance mal etiquetado
Antes: un rol por cada cliente de Upwork → CV fragmentado y fechas solapadas.
Después: un rol `Desarrollador Front-end y 3D Freelance` / `Upwork` / fechas, con los mejores proyectos como bullets.

## 9. Títulos de sección creativos
Antes: `Mi trayectoria`, `Lo que sé hacer` → el parser no segmenta.
Después: `Experiencia`, `Habilidades` (o `Work Experience`, `Skills`).
