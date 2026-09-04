---
name: paiban-gongwen
description: Reformat an uploaded Word or Markdown file into a fixed Chinese official-document layout that matches the user WPS screenshot. Use when the user says 公文排版, 帮我进行公文排版, paiban-gongwen, or asks to apply this exact official-document preset to a .docx or Markdown file.
metadata:
  type: workflow
  version: "1.0"
  spec: user-wps-screenshot-2026-09-04
---

# 公文排版

Apply one frozen layout. Do not invent a second preset. Do not load `sanmu-document-formatting` for these requests.

Read [references/format-spec.md](references/format-spec.md) before changing any paragraph, section, header, or footer. The screenshot in `assets/format-spec.png` is the visual source of that spec.

## Scope

- Input: user-uploaded `.docx` or Markdown/plain text.
- Output: a new `.docx` and a matching `.pdf` with the same stem. Deliver both.
- Refuse `.doc`, `.docm`, encrypted files, and files with unresolved tracked changes or comments. Ask for a clean `.docx` or paste the text.
- Never overwrite the source file. Write `<stem>_公文排版.docx`. If that name exists, append `-2`, `-3`, and so on.
- Do not invent titles, issuing units, dates, addressees, or body sentences. Preserve wording. Allowed edits are whitespace normalization and, when a short line functions as a heading but has no prefix, inserting the official `一、` `（一）` `1.` `（1）` mark for that level.
- Do not persist per-document overrides as a new profile. This skill has one spec.

## Route

- Markdown, `.txt`, or pasted text → `scripts/format_gongwen.py create --input <file> --output <out.docx>`
- Existing `.docx` → `scripts/format_gongwen.py format --input <file> --output <out.docx>` after showing the plan
- If the user only says `公文排版` and no file is present, ask for the Word, Markdown, or text source. Do not fabricate a sample document.
- Read [references/structure-recognition.md](references/structure-recognition.md) before classifying.

## Required workflow

1. Read [references/format-spec.md](references/format-spec.md).
2. Confirm input type and output path. State that fonts are written as named East-Asian fonts so they resolve on a Chinese WPS/Word machine even if this sandbox lacks 方正/仿宋/楷体.
3. Read the whole source for meaning. Then classify with [references/structure-recognition.md](references/structure-recognition.md). Reliable author marks win. Broken form yields to meaning. Map every block onto 主标题 / 一级 / 二级 / 三级 / 四级 / 正文 / 落款 only.
4. If a short line functions as a heading and lacks an official prefix, add `一、` `（一）` `1.` or `（1）` for the chosen level and restart child counters after a parent heading. Write the normalized blocks if needed, then run `scripts/format_gongwen.py`. Print `role<TAB>text`. If several roles are uncertain, prefer 正文 or show the plan; do not stop for confirmation on an otherwise clear document.
5. If `python-docx` is missing, stop and report it. Do not install packages silently.
6. After the `.docx` is written, export PDF with the same stem via `scripts/format_gongwen.py` (LibreOffice `soffice --headless --convert-to pdf`). If conversion fails, still deliver the Word file and report the PDF error. A sandbox PDF may substitute fonts; say so. Report both paths and the page metrics.

## Layout rules the script must keep

- A4 portrait. Margins — top 37 mm, bottom 35 mm, left 28 mm, right 26 mm.
- Document grid — 指定行和字符网格, 28 characters per line, 22 lines per page.
- Header distance from edge 1.50 cm. Footer distance from edge 2.50 cm.
- Page numbers only, 宋体 4号, form `— n —`, duplex style 双面打印1, footer on the outer side (odd pages right, even pages left). No other header or footer text.
- 主标题 centered, 方正小标宋简体, 2号 (22 pt). After the title insert one blank body-pitched line.
- 一级标题 方正黑体简体 3号 (16 pt), prefix `一、`, first-line indent 2 characters.
- 二级标题 楷体_GB2312 3号 (16 pt), prefix `（一）`, first-line indent 2 characters.
- 三级标题 方正仿宋_GB18030 3号 (16 pt), prefix `1.`, first-line indent 2 characters.
- 四级标题 方正仿宋_GB18030 3号 (16 pt), prefix `（1）`, first-line indent 2 characters.
- 正文 方正仿宋_GB18030 3号 (16 pt), first-line indent of 2 characters.
- Fixed line pitch 28.9 pt on every managed paragraph so 22 lines fit the printable height. Do not set the body font size to 28.9 pt.
- 落款 right-aligned block after exactly one blank body-styled paragraph. Do not invent a unit or date.
- Text color black. Disable widow/orphan control on managed paragraphs.
- Latin letters and digits in body, title and heading runs use Times New Roman. East-Asian text uses the role font. Page-number digits stay 宋体. Do not force a 28-character grid onto Latin runs.
- Keep 指定行和字符网格 and first-line indent via firstLineChars=200 for 正文 and 一级至四级标题. The main title stays centered with no first-line indent.

## Fallbacks

Write the official font names into the document. Also set East-Asian fallback hints only when the named font is absent on the authoring machine. Never substitute a different visual style (for example do not turn 主标题 into 黑体).

| Role | Required name | Acceptable machine fallback if missing |
|---|---|---|
| 主标题 | 方正小标宋简体 | 华文中宋, then 宋体 |
| 一级标题 | 方正黑体简体 | 黑体 |
| 二级标题 | 楷体_GB2312 | 楷体 |
| 三/四级与正文 | 方正仿宋_GB18030 | 仿宋_GB2312, then 仿宋 |
| 页码 | 宋体 | 宋体 |

## After output

Do not claim visual proof unless a renderer produced page images. If only the `.docx` exists, report structural application of the spec, not printed appearance.
