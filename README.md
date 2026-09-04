# Paiban-Gongwen

作者：JiaD

一个 Skill 一个文件夹。

```text
Paiban-Gongwen/
├── jiadong-gongwenpaiban/     排版，输出 Word 与 PDF
└── jiadong-paiban-prompt/     中间稿格式，只锁结构
```

## 用一句话让 AI 安装

把下面整段发给 Grok 或任何能读 GitHub、能写本地 skills 目录的 AI。不用再解释。

### 两个都装

```text
请从 GitHub 仓库 https://github.com/JiaDDD/Paiban-Gongwen 安装两个 Skill。
把 jiadong-gongwenpaiban/ 整夹复制到 ~/.grok/skills/jiadong-gongwenpaiban/，
把 jiadong-paiban-prompt/ 整夹复制到 ~/.grok/skills/jiadong-paiban-prompt/。
每个目录里必须有 SKILL.md，目录名与 SKILL.md 里的 name 一致。
若目标已存在则覆盖更新。装完后列出落盘路径。
```

### 只装排版

```text
请从 https://github.com/JiaDDD/Paiban-Gongwen 安装 Skill jiadong-gongwenpaiban。
把仓库里的 jiadong-gongwenpaiban/ 整夹复制到 ~/.grok/skills/jiadong-gongwenpaiban/，覆盖已有文件。
```

### 只装中间稿

```text
请从 https://github.com/JiaDDD/Paiban-Gongwen 安装 Skill jiadong-paiban-prompt。
把仓库里的 jiadong-paiban-prompt/ 整夹复制到 ~/.grok/skills/jiadong-paiban-prompt/，覆盖已有文件。
```

若当前产品的用户 Skill 目录不是 `~/.grok/skills/`，把路径改成该产品要求的 skills 目录即可。Grok 工作区常见为 `/home/workdir/.grok/skills/`。

装好后开新对话，在输入框选中对应 Skill。

## 用 GitHub CLI 安装（可选）

```bash
gh skill install JiaDDD/Paiban-Gongwen jiadong-gongwenpaiban --agent grok
gh skill install JiaDDD/Paiban-Gongwen jiadong-paiban-prompt --agent grok
```

## 装好之后

1. 选中 `jiadong-paiban-prompt`，发题目或素材，得到中间稿。
2. 选中 `jiadong-gongwenpaiban`，把中间稿或链接、Word、TXT、Markdown 发过去，得到 Word 与 PDF。

许可：MIT
