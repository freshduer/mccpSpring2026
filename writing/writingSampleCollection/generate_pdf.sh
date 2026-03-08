#!/bin/bash
# 从 finalDraft.md 生成 finalDraft.pdf（无页眉页脚）
cd "$(dirname "$0")"
python3 md_to_pdf.py
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-sandbox \
  --no-pdf-header-footer \
  --print-to-pdf="$(pwd)/finalDraft.pdf" \
  "file://$(pwd)/finalDraft.html"
echo "已生成: $(pwd)/finalDraft.pdf"
