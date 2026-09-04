# Paiban-Gongwen

作者：JiaD

一个 Skill 一个文件夹。看文件夹名就能区分用途。

```text
Paiban-Gongwen/
├── README.md
├── LICENSE
├── jiadong-gongwenpaiban/     排版，输出 Word 与 PDF
│   ├── SKILL.md
│   ├── references/
│   └── scripts/
└── jiadong-paiban-prompt/     中间稿格式，只锁结构
    ├── SKILL.md
    └── references/
```

|文件夹|作用|安装到|
|---|---|---|
|[jiadong-gongwenpaiban](jiadong-gongwenpaiban/)|把来稿套成冻结公文版式|`~/.grok/skills/jiadong-gongwenpaiban/`|
|[jiadong-paiban-prompt](jiadong-paiban-prompt/)|按中间稿结构生成或给出生成用 Prompt|`~/.grok/skills/jiadong-paiban-prompt/`|

先选 `jiadong-paiban-prompt` 写稿，再把中间稿交给 `jiadong-gongwenpaiban` 排版。

许可：MIT
