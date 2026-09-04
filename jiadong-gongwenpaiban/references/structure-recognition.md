# 结构识别

## Intent

Author intent first. When form cannot recover that intent, recover structure from meaning. Recover structure only — do not rewrite the article.

Allowed roles: 主标题, 一级, 二级, 三级, 四级, 正文, 落款. Do not invent another style.

## Preferred intermediate form

When the source already uses this contract, trust it over later heuristics:

- `#` 主标题
- `##` plus `一、` 一级
- `###` plus `（一）` 二级
- `####` plus `1.` 三级
- `#####` plus `（1）` 四级
- `[落款]` then unit then date

Blank line between paragraphs. No table of contents, running header, or extra heading levels.

## When form wins

Use the author's marks when they are consistent with the text:

- The intermediate form above
- Markdown ATX `#`–`#####`
- Word Title / Heading 1–4 whose outline matches the wording
- Already-correct official prefixes `一、` `（一）` `1.` `（1）`

Do not "improve" a deliberately flat narrative into a tree.

## When meaning wins

Use this path for unstructured AI prose and for messy Word or pasted text. Treat the source as noisy when any of these hold: no ATX headings; almost every paragraph is Normal; lines are broken mid-sentence; numbering is missing or jumps; list styles lost their numbers; PDF line-wrap was pasted as paragraphs.

Then:

1. Merge hard wraps into meaning units.
2. Split only at a finished idea or a real topic change.
3. Assign each unit one allowed role from what it does in the text, not from how it looked on screen.
4. If a short sentence functions as a heading but has no official prefix, add the prefix for that level. Default is to number it. Do not add any other words.

## Heading evidence

A block may be a heading when most of these are true: it governs what follows; it is short; it does not end with `。！？；`; it is not a `标签：较长说明` field.

A block is body when it argues, explains, quotes, answers, or lists facts in full sentences.

## Official prefixes to insert

| Role | Prefix when missing |
|---|---|
| 一级 | `一、` `二、` … |
| 二级 | `（一）` `（二）` … |
| 三级 | `1.` `2.` … |
| 四级 | `（1）` `（2）` … |

Restart 二级以下 after a new 一级. Restart 三级以下 after a new 二级. Restart 四级 after a new 三级. If the line already has the correct prefix, keep the author's number and do not write a second one.

主标题 and 落款 never receive these prefixes.

## Line joining

Merge when the previous unit is unfinished and the next line is not a heading or a new numbered item. A blank line starts a new candidate unit. Strip `**` `__` `` ` ``, `>`, and bullets. Collapse internal whitespace.

## URLs

Fetch the main article text only. If the request fails, the page needs login, or no usable body remains after stripping chrome, stop and ask the user to paste the text. Do not invent structure from the page title.

## Uncertainty

If two roles are equally plausible, prefer 正文. If several blocks are uncertain, print the plan before or with the output. User corrections always override.
