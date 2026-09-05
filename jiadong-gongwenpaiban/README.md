# jiadong-gongwenpaiban

公文排版 Skill。按冻结规格生成 Word，不生成 PDF。

## 一行命令安装

```bash
npx -y skills add https://github.com/JiaDDD/Paiban-Gongwen -g --skill jiadong-gongwenpaiban --copy
```

需要 Node.js。`-g` 装到用户级目录，`--copy` 可避免 Windows 符号链接权限问题。

更新：

```bash
npx -y skills update jiadong-gongwenpaiban -g
```

## 发给当前 Agent

```text
帮我安装公文排版 Skill（jiadong-gongwenpaiban）：
https://github.com/JiaDDD/Paiban-Gongwen

请安装到当前 Agent 的个人 Skills 目录。若已存在同名 Skill，请先告诉我，不要直接覆盖。
```
