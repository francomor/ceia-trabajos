# CLAUDE.md — Análisis de Series de Tiempo (CEIA)

Guía para armar los TP de esta materia. Idioma: español argentino.

## Flujo de un TP

Franco resuelve el TP a mano en su cuaderno y saca fotos (`ejN_pagM.jpg`). La entrega es **solo LaTeX → PDF**, sin notebook.

1. Enunciado: el PDF del profesor (`TPn_Morero_Franco_a2533.pdf`, se extrae con `pdftotext -layout`). Ese archivo no se pisa; la salida es `TPn_Morero_Franco.pdf`.
2. Transcribir las fotos a LaTeX **tal como las escribió Franco** (sus pasos, orden y comentarios; resultados encuadrados con `\boxed`). Un subagente por ejercicio en paralelo funciona bien.
3. Dudas de lectura: usar la conversación de ChatGPT exportada a `.md` en la carpeta del TP (el link compartido de chatgpt.com no se puede leer con WebFetch). Teoría: `../../CEIA-AST/Clase N/*.pdf`.
4. Reportar los errores algebraicos o de notación del cuaderno y preguntar antes de corregirlos (en el TP1 se pidió corregirlos todos).
5. Al final, anexo con las fotos del cuaderno (ver abajo).

## Formato (debe coincidir con el PDF del profesor)

Plantilla: `tp1/TP1_Morero_Franco.tex`. Copiar el preámbulo y el encabezado de ahí.

- `extarticle` 9pt, Computer Modern, carta, márgenes `left=68.5pt,right=53.85pt`, `enumitem` con `leftmargin=-2.5pt,labelsep=5pt` para que el número del enunciado cuelgue del margen como en el original.
- Sin logos. Títulos en `\huge\textbf`, recuadro con Nombre/Código/Fecha sin negrita (fecha escrita sobre la línea).
- Cada enunciado en su `enumerate` ("1. (4 puntos) Sea:"), seguido de la resolución. `\hrule` entre ejercicios.
- Para ajustar el encabezado contra el original se comparan posiciones con `pdftotext -bbox -f 1 -l 1`.
- Anexo: `\clearpage`, título "Anexo: resolución manuscrita" (no todo en mayúsculas), una foto por página con rótulo "Ejercicio N, página M". Usar copias comprimidas en `tpN/anexo/` (`sips -Z 1600 -s formatOptions 70 foto.jpg --out anexo/foto.jpg`); con las originales el PDF pesa ~27 MB.

## Estilo de la prosa

- Coloquial, como escribe Franco, sin dos puntos en la prosa ("Notemos que…" en vez de "Nota:"). Sin negritas en el cuerpo.
- Cuidar la notación: no usar el nombre de la variable a demostrar para una densidad conocida (ej. `f_Z` con `Z\sim N(0,1)`, no `f_X`).
- Mantener juntas en horizontal las cuentas con `\Rightarrow` (usar `alignat*` con `\qquad`).

## Compilar

```bash
cd tpN
pdflatex -interaction=nonstopmode TPn_Morero_Franco.tex   # dos veces
rm -f TPn_Morero_Franco.aux TPn_Morero_Franco.log
```

Verificar mirando las páginas renderizadas (`pdftoppm -r 80 -png`) y `grep -E '^!|Overfull'` en la salida.
