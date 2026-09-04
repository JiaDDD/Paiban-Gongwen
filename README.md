# jiadong-gongwenpaiban

作者：JiaD

按固定中国公文规格，将 Word、Markdown 或纯文本排成 `.docx`，并导出同名 `.pdf`。

面向 Grok / Agent Skills：把本目录放到 `~/.grok/skills/jiadong-gongwenpaiban/`（或产品要求的 skills 目录）。触发语包括「公文排版」「帮我进行公文排版」「加东公文」「JiaD公文」「把这段排成公文」「按这个链接排版」。

生成内容前可把 `references/upstream-prompt.md` 整段发给上游模型。中间稿为 `#`～`#####` 加公文编号。链接抓取失败则停止并请改贴文本。散文来稿仍按文意排版。

## 规格摘要

- 主标题：方正小标宋简体，二号 22 磅，居中
- 一级：方正黑体简体，三号 16 磅，`一、`，首行缩进 2 字
- 二级：楷体_GB2312，三号 16 磅，`（一）`，首行缩进 2 字
- 三级 / 四级 / 正文：方正仿宋_GB18030，三号 16 磅；三级 `1.`，四级 `（1）`；正文两端对齐，首行缩进 2 字
- 数字与英文：Times New Roman；页码宋体四号，`— n —`，双面页脚外侧
- 页面：A4；边距上 37 / 下 35 / 左 28 / 右 26 毫米；行距固定 28.9 磅；网格 28 字 × 22 行

结构识别见 `references/structure-recognition.md`。来稿标记可靠时跟标记；格式混乱时按文意恢复层级。功能上是标题但无编号的短句，按公文层级补 `一、` `（一）` `1.` `（1）`。

## 本地脚本

```bash
python3 scripts/format_gongwen.py create --input source.md --output out.docx
python3 scripts/format_gongwen.py format --input source.docx --output out.docx
python3 scripts/format_gongwen.py create --input source.md --output out.docx --print-plan
```

依赖：`python-docx`。导出 PDF 需要本机 `soffice`（LibreOffice）。无方正字体时，Word/PDF 会回退，文件中仍写入官方字体名。

## 许可

MIT
