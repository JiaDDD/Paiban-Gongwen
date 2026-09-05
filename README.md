# Paiban-Gongwen

由 JiaD 创建的 Skill

### jiadong-paiban-prompt

限定公文中间稿格式：

- 输出 ATX `#` 至 `#####`，配公文序号 `一、` `（一）` `1.` `（1）`，可选 `[落款]`
- 只锁结构，不改题目、立场、措辞或事实
- 只要生成用 Prompt 时，原样返回仓库里的围栏全文

### jiadong-gongwenpaiban

选中并附上来源后自动进行公文排版。

- 可输入：粘贴的 AI 回复、网页链接、Word、TXT、Markdown
- 只交出公文规格的 Word，不生成 PDF
- 不改写正文；中间稿优先，散文则按文意恢复结构

建议先用 `jiadong-paiban-prompt` 写稿，再把中间稿交给 `jiadong-gongwenpaiban` 排版。

## 用一句话让 AI 安装

把下面整段发给当前正在用的 AI。由它查明本产品的用户 Skill 目录并完成复制，不要手写路径。

### 两个都装

```text
请从 GitHub 仓库 https://github.com/JiaDDD/Paiban-Gongwen 安装两个 Skill：jiadong-gongwenpaiban 与 jiadong-paiban-prompt。
先查明本产品用户 Skill 的落盘目录，再把仓库里同名文件夹整夹复制过去。
每个目录必须含 SKILL.md，目录名必须与 SKILL.md 的 name 一致。
目标已存在则覆盖更新。装完列出实际路径。
```

### 只装排版

```text
请从 https://github.com/JiaDDD/Paiban-Gongwen 安装 Skill jiadong-gongwenpaiban。
先查明本产品用户 Skill 目录，再把仓库里的 jiadong-gongwenpaiban/ 整夹复制过去，已存在则覆盖。
```

### 只装中间稿

```text
请从 https://github.com/JiaDDD/Paiban-Gongwen 安装 Skill jiadong-paiban-prompt。
先查明本产品用户 Skill 目录，再把仓库里的 jiadong-paiban-prompt/ 整夹复制过去，已存在则覆盖。
```

装好后开新对话，选中对应 Skill。

## 装好之后

1. 选中 `jiadong-paiban-prompt`，发题目或素材，得到中间稿。
2. 选中 `jiadong-gongwenpaiban`，把中间稿或链接、Word、TXT、Markdown 发过去，得到 Word。若需要 PDF，在已安装公文字体的 WPS 或 Word 中自行导出。

许可：MIT
