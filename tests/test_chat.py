import unittest
from unittest.mock import patch

from streamlit.testing.v1 import AppTest


class StreamlitChatTests(unittest.TestCase):
    @patch.dict("os.environ", {"GROQ_API_KEY": ""})
    def test_question_sources_and_clear(self):
        app = AppTest.from_file("streamlit_app.py").run()
        app.chat_input[0].set_value("How do students use GenAI?").run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.chat_message), 2)
        self.assertIn("Students", app.expander[0].text[0].value)
        app.sidebar.button[0].click().run()
        self.assertEqual(len(app.chat_message), 0)
