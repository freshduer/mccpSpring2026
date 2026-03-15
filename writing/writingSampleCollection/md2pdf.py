#!/usr/bin/env python3
"""Convert finalDraft.md to PDF."""
import markdown
from xhtml2pdf import pisa

MD_PATH = "finalDraft.md"
PDF_PATH = "finalDraft.pdf"

with open(MD_PATH, "r", encoding="utf-8") as f:
    md_text = f.read()

html_body = markdown.markdown(
    md_text,
    extensions=["extra", "nl2br"],
    output_format="html5",
)

html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
  body {{ font-family: "Times New Roman", Times, serif; font-size: 11pt; line-height: 1.5; margin: 2cm; color: #222; }}
  h1 {{ font-size: 18pt; margin-top: 0; margin-bottom: 12pt; border-bottom: 1pt solid #ccc; padding-bottom: 4pt; }}
  h2 {{ font-size: 14pt; margin-top: 18pt; margin-bottom: 8pt; }}
  h3 {{ font-size: 12pt; margin-top: 12pt; margin-bottom: 6pt; }}
  p {{ margin: 0 0 8pt; text-align: justify; }}
  ul {{ margin: 8pt 0; padding-left: 24pt; }}
  li {{ margin-bottom: 4pt; }}
  strong {{ font-weight: bold; }}
  hr {{ border: none; border-top: 1pt solid #ccc; margin: 12pt 0; }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

with open(PDF_PATH, "wb") as pdf_file:
    pisa_status = pisa.CreatePDF(html_doc.encode("utf-8"), dest=pdf_file, encoding="utf-8")

if pisa_status.err:
    print("PDF generation had errors:", pisa_status.err)
    exit(1)
print("Generated:", PDF_PATH)
