# Postulaciones con Claude Code

Un sistema para postular a trabajos y vender servicios freelance usando
[Claude Code](https://claude.com/claude-code). Pegas una oferta de empleo o un
post de Upwork y Claude te deja listo:

- el análisis de la oferta y qué tan bien encajas,
- la investigación de la empresa,
- la respuesta a "¿Por qué quieres trabajar aquí?" o la carta del correo,
- un CV adaptado a esa oferta, en PDF legible por los ATS,
- la propuesta de Upwork o el mensaje en frío.

Todo sale de **tu** CV maestro. El sistema no inventa experiencia, números ni
clientes, y todo dato de empresa sale de una búsqueda web real.

> Lo creé para mí (Eliam Paredes), así que las skills hablan de "Eliam".
> Más abajo explico cómo adaptarlo a ti.

---

## Requisitos

- [Claude Code](https://claude.com/claude-code) instalado y con sesión iniciada.
- Python 3.9 o superior.
- `pypdf` para verificar los PDF:
  ```
  pip install pypdf
  ```
- Un navegador Chromium para imprimir los PDF: Microsoft Edge (viene con
  Windows) o Google Chrome. El script lo busca solo.

---

## Instalación

### 1. Clona el repo

```
git clone https://github.com/eliam-paredes/Postulaciones.git
cd Postulaciones
```

### 2. Enlaza las skills

Las skills viven en `Skills/`, pero Claude Code las busca en `.claude/skills`.
Crea el enlace una vez:

**Windows (PowerShell):**
```
New-Item -ItemType Junction -Path .claude\skills -Target "$PWD\Skills"
```

**macOS / Linux:**
```
ln -s ../Skills .claude/skills
```

### 3. Comprueba que el PDF funciona

```
python Skills/cv-pdf/scripts/generar_cv.py --check
```

Si falta algo, el script te dice qué instalar.

### 4. Crea las carpetas privadas

El repo no trae datos personales. Crea estas carpetas (están en el
`.gitignore`, nunca se suben):

```
mkdir CV
mkdir CV/originales
mkdir Ventas/prospectos
```

---

## Adáptalo a ti

1. **Cambia el nombre.** Busca "Eliam" en `CLAUDE.md` y en `Skills/` y
   reemplázalo por tu nombre. Ajusta en `CLAUDE.md` tu perfil (qué haces,
   tu nivel de inglés, tu idioma).
2. **Cambia la firma.** `Herramientas/lint_texto.py` exige que los correos
   cierren con "Atentamente," y "Eliam Paredes". Pon tu nombre.
3. **Cambia tus enlaces.** `Skills/postular-upwork/references/enlaces.md`
   tiene los enlaces de portafolio que se ponen en las propuestas.
4. **Crea tu CV maestro** (siguiente sección).

---

## Primer paso: tu CV maestro

Todo el sistema lee `CV/cv_total.md`. Es la única fuente de tu experiencia.

1. Copia tu CV actual (PDF), tu LinkedIn exportado o lo que tengas en
   `CV/originales/`.
2. Abre Claude Code en la carpeta del proyecto:
   ```
   claude
   ```
3. Pídele:
   ```
   Crea mi CV maestro con lo que hay en CV/originales
   ```
   Se activa la skill `cv-maestro`. Te hará preguntas para sacar logros con
   números reales. Al final crea:

   | Archivo | Para qué |
   |---|---|
   | `CV/cv_total.md` | Toda tu experiencia, con logros y su fuente |
   | `CV/estilo.md` | Reglas de estilo que vas corrigiendo |
   | `CV/motivaciones.md` | Qué te atrae de verdad (para "¿Por qué aquí?") |
   | `CV/historias-entrevista.md` | Historias STAR para entrevistas |
   | `CV/datos-formulario.md` | Salario, disponibilidad y datos de portales |

Opcional: crea variantes de tu CV por área en `CV/variantes/NN-area/`
(cada una con `cv-es.md` y `cv-en.md`). La skill `postular-correo` las puntúa
contra la oferta para elegir cuál adjuntar.

---

## Uso diario

Abre `claude` en la carpeta del proyecto y pega lo que tengas. Antes de
empezar, Claude siempre te pregunta dos cosas: el modo (correo, Upwork o
portal) y si quieres un CV específico para ese puesto.

| Tú haces... | Se activa | Resultado |
|---|---|---|
| Pegas una oferta que se postula en un portal o LinkedIn | `postular-portal` | Carpeta en `Casos/` con análisis, empresa y respuesta |
| Pegas una oferta que pide mandar el CV a un correo | `postular-correo` | Carpeta con el correo listo y el CV elegido |
| Pegas un post de Upwork | `postular-upwork` | Propuesta de 50 a 150 palabras en `Ventas/propuestas/` |
| "Hazme el CV para esta oferta" | `cv-adaptador` + `cv-pdf` | `cv.md` y PDF adaptados |
| "Revisa este CV" | `cv-auditor` | Puntaje ATS y correcciones |
| "Escríbele al reclutador" / "mensaje de seguimiento" | `outreach-propuestas` | Mensaje en frío o seguimiento |
| "Ayúdame a armar mi oferta de servicios" | `oferta-irresistible` | Oferta en `Ventas/ofertas/` |
| Le corriges un dato de tu carrera | `cv-maestro` | Se guarda en el CV maestro |

Ejemplo:

```
Me quiero postular a esta oferta: <pegas el texto o el enlace>
```

Claude **nunca envía correos ni postula por ti**. Solo deja todo listo para
que lo revises y lo mandes tú.

### Cómo queda un caso

Cada postulación crea una carpeta `Casos/AAAA-MM-empresa-puesto/`. Mira los
ejemplos con empresas ficticias para ver el formato:

- `Casos/_ejemplo-portal/`
- `Casos/_ejemplo-correo/`
- `Ventas/propuestas/_ejemplo-upwork.md`

Lleva el estado de tus postulaciones en `Casos/registro.md`.

---

## Revisión automática de textos

`.claude/settings.json` tiene un hook que corre `Herramientas/lint_texto.py`
cada vez que Claude guarda un texto para enviar (`correo.md`, `respuesta.md`,
`mensajes.md`, `cv.md`, propuestas). Revisa:

- sin guiones largos, emojis ni signos de exclamación,
- sin frases de relleno típicas de IA,
- largo de la carta (80 a 130 palabras) y de la propuesta (50 a 150),
- `[placeholders]` sin rellenar.

Si algo falla, Claude lo corrige solo. También puedes correrlo a mano:

```
python Herramientas/lint_texto.py Casos/<carpeta>/correo.md
```

---

## Estructura

```
Skills/            Las skills del proyecto (fuente única)
  github/          Skills de terceros, solo como referencia (no activas)
.claude/
  skills           Enlace a Skills/ (lo creas tú en la instalación)
  settings.json    Permisos y hook de revisión de textos
Herramientas/
  lint_texto.py          Revisa los textos antes de enviarlos
  puntuar_variantes.py   Puntúa tus variantes de CV contra una oferta
CV/                Tu CV maestro y datos personales (privado)
Casos/             Una carpeta por postulación (privado, salvo ejemplos)
  _plantilla/      oferta.md y requisitos.md para copiar
Ventas/
  ofertas/         Tus ofertas de servicios (privado)
  propuestas/      Propuestas de Upwork (privado, salvo el ejemplo)
  prospectos/      Listas de empresas y correos en frío (privado)
CLAUDE.md          Las instrucciones que Claude sigue en este proyecto
```

---

## Privacidad

El `.gitignore` deja fuera todo lo personal: tu CV, tus datos de formulario,
tus postulaciones reales, tus clientes y tus listas de empresas. Si haces un
fork público, revisa `git status` antes de cada commit para no subir nada
de eso por error.

---

## Créditos

Varias skills se inspiran en material de terceros que está en `Skills/github/`,
cada uno con su licencia original. Las ideas de oferta y propuesta se basan en
*$100M Offers* de Alex Hormozi y en *Cómo ganar amigos e influir sobre las
personas* de Dale Carnegie.
