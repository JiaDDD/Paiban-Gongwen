# Paiban-Gongwen

由 JiaD 创建的公文中间稿与公文排版 Skill。

**不改写正文｜不覆盖原文件｜只输出 Word｜不静默安装依赖或字体**

建议先用 `jiadong-paiban-prompt` 写中间稿，再把稿件交给 `jiadong-gongwenpaiban` 排版。

## 30 秒开始

### 一行命令安装

两个都装：

```bash
npx -y skills add https://github.com/JiaDDD/Paiban-Gongwen -g --skill jiadong-gongwenpaiban --copy
npx -y skills add https://github.com/JiaDDD/Paiban-Gongwen -g --skill jiadong-paiban-prompt --copy
```

只装排版：

```bash
npx -y skills add https://github.com/JiaDDD/Paiban-Gongwen -g --skill jiadong-gongwenpaiban --copy
```

只装中间稿：

```bash
npx -y skills add https://github.com/JiaDDD/Paiban-Gongwen -g --skill jiadong-paiban-prompt --copy
```

安装器会检测本机已有的 Agent，并让你选择安装目标。该命令需要 Node.js；`-g` 表示安装到用户级目录，`--copy` 可以避免 Windows 符号链接权限问题。

### 也可以直接发给你的 Agent

```text
帮我从 https://github.com/JiaDDD/Paiban-Gongwen 安装两个 Skill：jiadong-gongwenpaiban 与 jiadong-paiban-prompt。
请安装到当前 Agent 的个人 Skills 目录。若已存在同名 Skill，请先告诉我，不要直接覆盖。
```

只装排版时，把仓库地址和 Skill 名 `jiadong-gongwenpaiban` 发给 Agent 即可。

### 已安装？这样更新

```bash
npx -y skills update jiadong-gongwenpaiban -g
npx -y skills update jiadong-paiban-prompt -g
```

也可以重新运行上面的一行安装命令，并选择原来的安装目标。

## 这两个 Skill 做什么

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
- 写出后做 OOXML 结构校验（字体名、28.9 磅行距、网格、页边距、页码域）

装好后开新对话，选中对应 Skill。需要 PDF 时，在已安装公文字体的 WPS 或 Word 中自行导出。

许可：MIT
