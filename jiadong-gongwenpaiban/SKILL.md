---
name: jiadong-gongwenpaiban
description: 由 JiaD 创建的公文排版 Skill。粘贴 AI 回复或网页链接，或上传 Word、TXT、Markdown，即可自动生成公文规格的 Word，享受吧！
metadata:
  type: workflow
  version: "1.4"
  spec: user-wps-screenshot-2026-09-04
---

# 公文排版

Apply one frozen layout. Do not invent a second preset. Do not load `sanmu-document-formatting` for these requests.

Read [references/format-spec.md](references/format-spec.md) before changing any paragraph, section, header, or footer. The screenshot in `assets/format-spec.png` is the visual source of that spec.

## Scope

- Input: pasted AI answers, `http(s)` URLs, `.docx`, Markdown, or plain text.
- Output: a new `.docx` only. Do not export, generate, or deliver a `.pdf`. If the user wants a PDF, tell them to export it from WPS or Word on a machine that has the official fonts.
- Canonical intermediate form is ATX `#`–`#####` plus official numbering. Prefer that form. Fall back to meaning when the source is prose.
- Refuse `.doc`, `.docm`, encrypted files, and files with unresolved tracked changes or comments. Ask for a clean `.docx` or paste the text.
- Never overwrite the source file. Write `<stem>_公文排版.docx`. If no stem exists, use the title or `公文排版.docx`. If that name exists, append `-2`, `-3`, and so on.
- Do not invent titles, issuing units, dates, addressees, or body sentences. Preserve wording. Allowed edits are whitespace normalization and, when a short line functions as a heading but has no prefix, inserting the official `一、` `（一）` `1.` `（1）` mark for that level.
- Do not persist per-document overrides as a new profile. This skill has one spec.
- If the user asks for the generation prompt, return [references/upstream-prompt.md](references/upstream-prompt.md) verbatim. Do not invent a second prompt.

## Route

- Pasted text or Markdown (including an AI answer) → normalize to the intermediate form if needed → `scripts/format_gongwen.py create --input <file> --output <out.docx>`
- `http(s)` URL → fetch main text. If fetch fails or the page has no usable body, stop and ask the user to paste the text. Do not guess structure from the title alone.
- Existing `.docx` → `scripts/format_gongwen.py format --input <file> --output <out.docx>`
- If this skill is selected and the message contains pasted text, a URL, or an uploaded `.docx` / `.txt` / Markdown file, start typesetting immediately. Extra words such as 公文排版 are optional. Do not ask whether to format.
- If this skill is selected but no source is present, ask for text, a link, Word, TXT, or Markdown. Do not fabricate a sample document.
- Read [references/structure-recognition.md](references/structure-recognition.md) before classifying.

## Required workflow

1. Read [references/format-spec.md](references/format-spec.md).
2. If a source is already in the message or attachments, skip confirmation chat and go straight to classification and output. Mention fonts only in the short completion note. State that fonts are written as named East-Asian fonts so they resolve on a Chinese WPS/Word machine even if this sandbox lacks 方正/仿宋/楷体.
3. Detect input type. For a URL, fetch the article body first. Classify with [references/structure-recognition.md](references/structure-recognition.md). Intermediate ATX plus official numbering wins when present. Otherwise recover structure from meaning. Map every block onto 主标题 / 一级 / 二级 / 三级 / 四级 / 正文 / 落款 only. Do not expand, shrink, or polish the wording.
4. If a short line functions as a heading and lacks an official prefix, add `一、` `（一）` `1.` or `（1）` for the chosen level and restart child counters after a parent heading. Write the normalized blocks if needed, then run `scripts/format_gongwen.py`. Print `role<TAB>text`. If several roles are uncertain, prefer 正文 or show the plan; do not stop for confirmation on an otherwise clear document.
5. If `python-docx` is missing, stop and report it. Do not install packages silently.
6. After the `.docx` is written, run `scripts/validate_gongwen.py --input <out.docx>`. Print `VALIDATE OK` or the `ERROR` lines. Do not call LibreOffice, `soffice`, or any PDF converter. Deliver only the Word path. If validation fails, still keep the Word file, report the structural errors, and do not claim the spec is fully applied.

## Layout rules the script must keep

- A4 portrait. Margins — top 37 mm, bottom 35 mm, left 28 mm, right 26 mm.
- Document grid — 指定行和字符网格, 28 characters per line, 22 lines per page.
- Header distance from edge 1.50 cm. Footer distance from edge 2.50 cm.
- Page numbers only, 宋体 4号, form `— n —`, centered in the footer on odd and even pages. No other header or footer text.
- 主标题 centered, 方正小标宋简体, 2号 (22 pt). After the title insert one blank body-pitched line.
- 一级标题 方正黑体简体 3号 (16 pt), prefix `一、`, first-line indent 2 characters.
- 二级标题 楷体_GB2312 3号 (16 pt), prefix `（一）`, first-line indent 2 characters.
- 三级标题 方正仿宋_GB18030 3号 (16 pt), prefix `1.`, first-line indent 2 characters.
- 四级标题 方正仿宋_GB18030 3号 (16 pt), prefix `（1）`, first-line indent 2 characters.
- 正文 方正仿宋_GB18030 3号 (16 pt), first-line indent of 2 characters.
- Fixed line pitch 28.9 pt on every managed paragraph so 22 lines fit the printable height. Do not set the body font size to 28.9 pt.
- 落款 after exactly one blank body-styled paragraph. Place the block in the right-side region by a shared left indent estimated from the longest signature line. Do not invent a unit or date. Do not use a naive full-paragraph right alignment as the only layout.
- Text color black. Disable widow/orphan control on managed paragraphs.
- Latin letters and digits in body, title and heading runs use Times New Roman. East-Asian text uses the role font. Page-number digits stay 宋体. Do not force a 28-character grid onto Latin runs.
- Keep 指定行和字符网格 and first-line indent via firstLineChars=200 for 正文 and 一级至四级标题. The main title stays centered with no first-line indent.
- Use named paragraph styles `GW 主标题` / `GW 一级` / `GW 二级` / `GW 三级` / `GW 四级` / `GW 正文` / `GW 落款`. Strip theme colors when forcing black. Page-number fields use `PAGE \\* CHARFORMAT` with 宋体 in every font slot.

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

Deliver the `.docx` only. Do not attach or render a PDF. Report the validator result. A passing validator means the named fonts, 28.9 pt line pitch, grid, margins, page-number field, and paragraph roles were written into OOXML; it is not printed appearance. If asked how to obtain a PDF, say to open the Word file in WPS or Word and export there so the named official fonts can embed.
