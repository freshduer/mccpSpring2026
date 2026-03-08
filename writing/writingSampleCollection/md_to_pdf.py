#!/usr/bin/env python3
"""
将 finalDraft.md 转为可打印的 HTML，便于在浏览器中「打印 → 另存为 PDF」。
若已安装 pandoc，也可直接生成 PDF：pandoc finalDraft.md -o finalDraft.pdf
"""

import re
import sys
from pathlib import Path

# 打印友好的 HTML 模板
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Final Draft</title>
  <style>
    /* 学术格式: 12pt, Times New Roman, 1.5 倍行距, 页边距 2.54 cm */
    body {{
      font-family: "Times New Roman", serif;
      font-size: 12pt;
      line-height: 1.5;
      margin: 2.54cm;
      color: #000;
      max-width: none;
    }}
    h1 {{ font-size: 12pt; font-weight: bold; border-bottom: 1px solid #ccc; padding-bottom: 0.3em; margin-top: 1.2em; }}
    h2 {{ font-size: 12pt; font-weight: bold; margin-top: 1.5em; }}
    h3 {{ font-size: 12pt; font-weight: bold; margin-top: 1.2em; }}
    p {{ margin: 0.75em 0; text-align: justify; font-size: 12pt; line-height: 1.5; }}
    hr {{ border: none; border-top: 1px solid #ccc; margin: 1.5em 0; }}
    strong {{ font-weight: bold; }}
    em {{ font-style: italic; }}
    pre, code {{ font-family: "Times New Roman", serif; font-size: 12pt; background: #f5f5f5; padding: 0.2em 0.4em; }}
    pre {{ padding: 0.8em; overflow-x: auto; }}
    .comment {{ display: none; }}
    @media print {{ body {{ margin: 2.54cm; }} a {{ color: #000; }} }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def md_to_html(text: str) -> str:
    """简单将 Markdown 转为 HTML（支持标题、粗体、斜体、水平线、段落、注释隐藏）。"""
    lines = text.split("\n")
    out = []
    in_code_block = False
    code_lines = []
    in_comment = False

    def flush_code():
        nonlocal code_lines
        if code_lines:
            out.append("<pre><code>" + "\n".join(code_lines) + "</code></pre>")
            code_lines = []

    for line in lines:
        if line.strip() == "```":
            if in_code_block:
                flush_code()
                in_code_block = False
            else:
                in_code_block = True
            continue
        if in_code_block:
            code_lines.append(line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
            continue
        if line.strip().startswith("<!--"):
            in_comment = True
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if line.strip() == "---":
            out.append("<hr>")
            continue
        stripped = line.strip()
        if not stripped:
            out.append("<p></p>")
            continue
        # 标题
        if stripped.startswith("### "):
            out.append("<h3>" + inline_md(stripped[4:]) + "</h3>")
        elif stripped.startswith("## "):
            out.append("<h2>" + inline_md(stripped[3:]) + "</h2>")
        elif stripped.startswith("# "):
            out.append("<h1>" + inline_md(stripped[2:]) + "</h1>")
        else:
            out.append("<p>" + inline_md(stripped) + "</p>")
    flush_code()
    return "\n".join(out)


def inline_md(s: str) -> str:
    """粗体、斜体。"""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # *italic* 和 **bold**
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def main():
    base = Path(__file__).resolve().parent
    md_path = base / "finalDraft.md"
    html_path = base / "finalDraft.html"

    if not md_path.exists():
        print("未找到 finalDraft.md", file=sys.stderr)
        sys.exit(1)

    text = md_path.read_text(encoding="utf-8")
    body = md_to_html(text)
    html = HTML_TEMPLATE.format(body=body)
    html_path.write_text(html, encoding="utf-8")
    print("已生成:", html_path)
    print("请用浏览器打开该文件，按 Cmd+P（Mac）或 Ctrl+P（Windows）选择「另存为 PDF」即可得到 PDF。")


if __name__ == "__main__":
    main()
