# TP1 — Render PDF

```bash
pdflatex TP1_Morero_Franco.tex
pdflatex TP1_Morero_Franco.tex
```

Salida: `TP1_Morero_Franco.pdf`.

Requisitos: `pdflatex` con `extsizes` (TeX Live / MacTeX).

Fuentes: la resolución manuscrita (`ej*_pag*.jpg`) transcrita a LaTeX; enunciado en `TP1_Morero_Franco_a2533.pdf`. El anexo del PDF usa copias comprimidas de las fotos en `anexo/` (regenerar con `sips -Z 1600 -s formatOptions 70 ej1_pag1.jpg --out anexo/ej1_pag1.jpg`, etc.).
