# Document chatbot

A Streamlit chat app for asking questions about the bundled generative AI primer. Ask **How do students use GenAI?** and expand **Source passages** to read the text behind the answer.

## Run locally

Use Python 3.12 or newer. In PowerShell, clone the Streamlit branch and start the app:

```powershell
git clone --branch codex/streamlit-rebuild https://github.com/Chethanpb/Document_Based_ChatBot-RAG-.git document-chatbot
cd document-chatbot
python -m venv .venv
.\.venv\Scripts\python -m pip install .
.\.venv\Scripts\python -m streamlit run streamlit_app.py
```

Open the local URL printed by Streamlit. On macOS or Linux, use `.venv/bin/python` for the virtual environment commands.

## Documents and answers

Edit `knowledgebase.txt` to change the source material. Store one passage per nonempty line in UTF-8. Each question searches the current file, so document edits take effect on the next question. Retrieval ranks shared terms by rarity, adjusts for passage length, and returns up to three matching passages. Paraphrases without shared terms can yield no match.

The app works without an API key and displays retrieved passages directly. To enable generated answers, set `GROQ_API_KEY` in the server process environment before starting Streamlit. With this option enabled, the app sends each matching question and its retrieved passages to Groq. Set `GROQ_MODEL` to override the default `llama-3.3-70b-versatile`. If Groq is unavailable, the passages remain available.

Chat history lasts for the current Streamlit session. Each question is searched independently. Select **Clear conversation** in the sidebar to start fresh.

## Tests

Run the offline test suite from the repository root:

```powershell
.\.venv\Scripts\python -m unittest discover -s tests -v
```

The suite checks blank-line handling, unrelated questions, source display, and clearing a conversation.
