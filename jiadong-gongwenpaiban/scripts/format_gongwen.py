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
