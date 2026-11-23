import streamlit as st

from src.RagCode import answer

st.set_page_config(page_title="Document chatbot")
st.title("Document chatbot")
st.caption("Ask about generative AI and explore the passages behind each answer.")
if "messages" not in st.session_state:
    st.session_state.messages = []
if st.sidebar.button("Clear conversation"):
    st.session_state.messages.clear()


def show_message(message):
    with st.chat_message(message["role"]):
        st.write(message["text"])
        if message.get("sources"):
            with st.expander("Source passages"):
                for passage in message["sources"]:
                    st.text(passage)


for previous in st.session_state.messages:
    show_message(previous)

if question := st.chat_input("Ask about the document", max_chars=1000):
    if question.strip():
        user_message = {"role": "user", "text": question.strip()}
        st.session_state.messages.append(user_message)
        show_message(user_message)
        with st.spinner("Searching the document…"):
            result = answer(question.strip())
        reply = {"role": "assistant", "text": result["answer"], "sources": result["sources"]}
        st.session_state.messages.append(reply)
        show_message(reply)
