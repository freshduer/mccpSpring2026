# Poster images

Export figures from **pre2/longer/image/** as PNG and place them in this folder so the poster displays correctly.

## Required image files

| Filename (PNG) | Paper figure | Description |
|----------------|--------------|-------------|
| `longer-v5.png` | Figure 1 | LONGER model architecture |
| `jaguar.png` | Training framework | Training Framework |
| `kvcache.png` | KV Cache Serving | KV cache at inference |
| `TokenAuc.png` | Sequence length vs AUC | Scaling experiment |
| `TokenLoss.png` | Sequence length vs LogLoss | Scaling experiment |
| `ParamsAuc.png` | Params vs AUC | Optional |
| `FlopsAuc.png` | FLOPs vs AUC | Optional |

## How to export

From the `pre2/longer/image/` directory, convert PDFs to PNG using one of the following:

- **Command line (macOS/Linux):**  
  `for f in *.pdf; do pdftoppm -png -r 150 "$f" "${f%.pdf}"; done`  
  This produces `xxx-1.png`; rename to `xxx.png` and copy into this folder.

- **Online tool:** Use a PDF-to-PNG website, then name and place files as in the table above.

- **Copying PDFs:** If you skip conversion, you can copy PDFs here and use the names above (some browsers may not display PDF in `<img>`; PNG is recommended).
