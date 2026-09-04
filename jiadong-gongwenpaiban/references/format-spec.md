# 固定公文规格

Source: user WPS screenshot stored as `assets/format-spec.png` (2026-09-04). Do not change these values unless the user explicitly replaces the screenshot.

## Type hierarchy

| Role | Numbering example | Chinese font | 字号 | Points |
|---|---|---|---|---|
| 主标题 | none | 方正小标宋简体 | 2号 | 22 |
| 一级标题 | 一、 | 方正黑体简体 | 3号 | 16 |
| 二级标题 | （一） | 楷体_GB2312 | 3号 | 16 |
| 三级标题 | 1. | 方正仿宋_GB18030 | 3号 | 16 |
| 四级标题 | （1） | 方正仿宋_GB18030 | 3号 | 16 |
| 正文 | none | 方正仿宋_GB18030 | 3号 | 16 |
| 行距 | — | — | 固定值 | 28.9 |
| 页码 | — 1 — | 宋体 | 4号 | 14 |

The WPS screenshot printed 32 beside 2号 and 28.9 beside 3号. Those numbers are the half-point field and the fixed line pitch, not body type size. Body type at 28.9 pt yields about 15 characters per line and breaks the 28×22 grid. Use 二号 22 pt, 三号 16 pt, line pitch 28.9 pt.

Alignment

- 主标题: center
- 一级至四级标题: left, first-line indent 2 Chinese characters
- 正文: justify, first-line indent 2 Chinese characters
- 落款: right-side block on the last page

Line spacing

- Use exact line pitch derived from 22 lines per page on A4 with the stated top/bottom margins.
- Do not use Word "single" / "1.5 lines" spacing for managed styles.

## Page

- Paper: A4 (210 mm × 297 mm), portrait
- Gutter: 0
- Margins (unit is millimetre, not centimetre):
  - top 37 mm
  - bottom 35 mm
  - left 28 mm
  - right 26 mm
- Grid: 指定行和字符网格
  - characters per line: 28
  - lines per page: 22
- Header from edge: 1.50 cm
- Footer from edge: 2.50 cm
- Different odd and even headers/footers: yes (双面打印1)
- First page different: no
- Page number position: 页脚外侧
- Page number style: `— 1 —`, `— 2 —`, …
- Page number font: 宋体 4号

## Classification hints

Treat fullwidth parentheses `（）` as the official form. If the source uses halfwidth `()`, normalize only the numbering wrappers, not the body text.

Markdown ATX headings map as follows unless the user overrides:

- `#` → 主标题
- `##` → 一级标题
- `###` → 二级标题
- `####` → 三级标题
- `#####` → 四级标题
- paragraph → 正文

Do not emit a table of contents, running header title, red-seal line, or copy number unless the source already contains that text.
