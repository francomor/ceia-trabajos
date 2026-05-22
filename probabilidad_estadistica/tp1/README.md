# TP1 — Render PDF

```bash
jupyter nbconvert --to latex TP1_Morero_Franco.ipynb
sed -i.bak '/\\maketitle/d' TP1_Morero_Franco.tex && rm TP1_Morero_Franco.tex.bak
xelatex TP1_Morero_Franco.tex
xelatex TP1_Morero_Franco.tex
```

Salida: `TP1_Morero_Franco.pdf`.

Requisitos: `jupyter`, `nbconvert`, `xelatex` (TeX Live / MacTeX).
