#!/usr/bin/env python3
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from format_gongwen import build_document, parse_markdown  # noqa: E402
from validate_gongwen import validate  # noqa: E402


SAMPLE = """# 测试标题

这是一段正文，含 Latin 与 2026。

## 工作安排

后续说明。

[落款]
某办公室
2026年9月5日
"""


class FormatTests(unittest.TestCase):
    def test_parse_roles(self) -> None:
        blocks = parse_markdown(SAMPLE)
        roles = [role for role, _ in blocks]
        self.assertEqual(roles[0], "主标题")
        self.assertIn("一级", roles)
        self.assertEqual(roles[-2:], ["落款", "落款"])

    def test_validate_created_docx(self) -> None:
        blocks = parse_markdown(SAMPLE)
        document = build_document(blocks)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "out.docx"
            document.save(str(path))
            errors = validate(path)
            self.assertEqual(errors, [], msg="\n".join(errors))
            self.assertFalse(path.with_suffix(".pdf").exists())


if __name__ == "__main__":
    unittest.main()
