# Paiban-Gongwen

作者：JiaD

本仓库含两个 Skill：根目录为公文排版（`jiadong-gongwenpaiban` / `paiban-gongwen`）；`jiadong-paiban-prompt/` 为中间稿格式约束。

---

# jiadong-gongwenpaiban

由 JiaD 创建的公文排版 Skill。粘贴 AI 回复或网页链接，或上传 Word、TXT、Markdown，即可自动生成公文规格的 Word 与 PDF，享受吧！

选中本 Skill 并附上来源后，即使不再说话也直接排版。

## Skill 描述

可直接用于 Grok / Agent Skills 的 description 字段：

```text
由 JiaD 创建的公文排版 Skill。粘贴 AI 回复或网页链接，或上传 Word、TXT、Markdown，即可自动生成公文规格的 Word 与 PDF，享受吧！选中本 Skill 并带来源后，即使用户不再说话也直接排版。用于公文排版、帮我进行公文排版、加东公文、JiaD公文、把这段排成公文、按这个链接排版。
```

## 做什么

把来稿套进一套冻结的中国公文版式，同时交出 Word 和 PDF。不改写内容，只恢复结构和版面。

| 可输入 | 会得到 |
| --- | --- |
| 粘贴的 AI 回答 | 主标题_公文排版.docx |
| 网页链接 | 同名 .pdf |
| Word / TXT / Markdown | 页码为 — n — 的双面页脚 |

链接抓不到正文时会停下来请您改贴文本，不会只凭标题猜结构。

## 怎么用

1. 把本仓库放到 `~/.grok/skills/jiadong-gongwenpaiban/`（或产品要求的 skills 目录）。
2. 在对话里选中本 Skill，发送文本、链接或文件。
3. 也可以直接说：公文排版、帮我进行公文排版、加东公文、JiaD公文、把这段排成公文、按这个链接排版。

若要先让其他模型按可识别结构写作，使用 [jiadong-paiban-prompt](jiadong-paiban-prompt/) ，或把 [references/upstream-prompt.md](references/upstream-prompt.md) 整段发给对方。中间稿约定为 `#`～`#####`，并配 `一、` `（一）` `1.` `（1）`。没有这套标记的散文，仍按文意排版。

## 规格摘要

- 主标题：方正小标宋简体，二号 22 磅，居中
- 一级：方正黑体简体，三号 16 磅，`一、`，首行缩进 2 字
- 二级：楷体_GB2312，三号 16 磅，`（一）`，首行缩进 2 字
- 三级 / 四级 / 正文：方正仿宋_GB18030，三号 16 磅；三级 `1.`，四级 `（1）`；正文两端对齐，首行缩进 2 字
- 数字与英文：Times New Roman；页码宋体四号，`— n —`，双面页脚外侧
- 页面：A4；边距上 37 / 下 35 / 左 28 / 右 26 毫米；行距固定 28.9 磅；网格 28 字 × 22 行

细则见 [references/format-spec.md](references/format-spec.md) 与 [references/structure-recognition.md](references/structure-recognition.md)。

## 本地脚本

```bash
python3 scripts/format_gongwen.py create --input source.md --output out.docx
python3 scripts/format_gongwen.py format --input source.docx --output out.docx
python3 scripts/format_gongwen.py create --input source.md --output out.docx --print-plan
```

依赖 `python-docx`。导出 PDF 需要本机 `soffice`（LibreOffice）。无方正字体时，屏幕显示会回退，文件里仍写入官方字体名。

---

# jiadong-paiban-prompt

公文中间稿格式 Skill。只锁结构，不锁内容，不排 Word 与 PDF。选中后只要给题目或素材即按中间稿直接成稿。

安装：将 [jiadong-paiban-prompt/](jiadong-paiban-prompt/) 整目录放到 `~/.grok/skills/jiadong-paiban-prompt/`。

中间稿为 ATX `#`～`#####`，配 `一、` `（一）` `1.` `（1）`，可选 `[落款]`。只要生成用 Prompt 时，原样返回 [jiadong-paiban-prompt/references/draft-format.md](jiadong-paiban-prompt/references/draft-format.md)。

排版请把中间稿交给根目录的排版 Skill。

## 许可

MIT
