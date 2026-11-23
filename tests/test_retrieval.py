import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src import RagCode


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        directory = self.enterContext(tempfile.TemporaryDirectory())
        root = Path(directory)
        (root / "knowledgebase.txt").write_text(
            "Course overview\n\nStudents use tutoring tools.\n", encoding="utf-8"
        )
        self.enterContext(patch.object(RagCode, "ROOT", root))
        self.enterContext(patch.dict("os.environ", {"GROQ_API_KEY": ""}))

    def test_blank_line_preserves_source_alignment(self):
        result = RagCode.answer("Which tutoring tools?")
        self.assertEqual(result["sources"], ["Students use tutoring tools."])

    def test_unrelated_question_returns_no_sources(self):
        result = RagCode.answer("What is photosynthesis?")
        self.assertEqual(result["sources"], [])
