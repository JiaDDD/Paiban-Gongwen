#!/usr/bin/env python3
"""Create or reformat a .docx using the frozen 公文排版 spec."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Emu, Mm, Pt, Twips

# Font sizes: 2号=22pt, 3号=16pt, line pitch 28.9pt, page number 14pt.
PT_TITLE = 22.0
PT_BODY = 16.0
PT_LINE = 28.9
PT_PAGE = 14.0

FONT_TITLE = "方正小标宋简体"
FONT_H1 = "方正黑体简体"
FONT_H2 = "楷体_GB2312"
FONT_BODY = "方正仿宋_GB18030"
FONT_PAGE = "宋体"
FONT_LATIN = "Times New Roman"

CN_NUM = "一二三四五六七八九十百千零〇"
CN_SEQ = (
    "一 二 三 四 五 六 七 八 九 十 "
    "十一 十二 十三 十四 十五 十六 十七 十八 十九 二十"
).split()

RE_H1 = re.compile(rf"^[{CN_NUM}]+、\s*")
RE_H2 = re.compile(rf"^[（(][{CN_NUM}]+[）)]\s*")
RE_H3 = re.compile(r"^[0-9０-９]+[．.\u3001]\s*")
RE_H4 = re.compile(r"^[（(][0-9０-９]+[）)]\s*")
RE_MD = re.compile(r"^(#{1,5})\s+(.*)$")
RE_BULLET = re.compile(r"^[-*•·]\s+")
RE_DATE = re.compile(
    r"(20\d{2}\s*年\s*\d{1,2}\s*月\s*\d{1,2}\s*日|20\d{2}\s*年\s*\d{1,2}\s*月).*(印发)?$"
)
END_PUNCT = "。！？；…」』”’"
STYLE_ROLE = {
    "title": "title",
    "heading 1": "h1",
    "heading 2": "h2",
    "heading 3": "h3",
    "heading 4": "h4",
    "toc heading": "h1",
}

print("placeholder-will-replace")
