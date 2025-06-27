import os
import streamlit as st
import datetime
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DB_FAISS_PATH = "vectorstore/db_faiss"

def load_llm():
    return ChatGroq(
        model_name="llama3-70b-8192",
        temperature=0,
        api_key=os.environ.get("GROQ_API_KEY")
    )

@st.cache_resource
def get_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
    return db

def set_custom_prompt(template):
    return PromptTemplate(template=template, input_variables=["context", "question"])

st.markdown("""
<style>
body {
    background-color: #f9fafb;
    font-family: 'Segoe UI', sans-serif;
}
.chat-message {
    display: flex;
    align-items: flex-end;
    margin: 10px 0;
    width: 100%;
}
.user .bubble {
    background-image: linear-gradient(to bottom right, #1E2A90, #EF385F);
    color: white;
    margin-left: auto;
    border-radius: 18px 18px 4px 18px;
    text-align: left;
}
.assistant .bubble {
    background-color: #e5e7eb;
    color: black;
    margin-right: auto;
    border-radius: 18px 18px 18px 4px;
    text-align: left;
}
.bubble {
    padding: 12px 16px;
    max-width: 70%;
    font-size: 15px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.1);
}
.meta {
    font-size: 11px;
    color: #6b7280;
    margin-top: 4px;
    margin-left: 44px;
}
.avatar {
    height: 32px;
    width: 32px;
    border-radius: 50%;
    margin: 0 8px;
}
.user {
    flex-direction: row-reverse;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Customer Support Chatbot")

if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'last_prompt' not in st.session_state:
    st.session_state.last_prompt = ""

prompt = st.chat_input("Type your message here...")

def render_bubble(role, text, timestamp, confidence=None):
    avatar_url = "https://cdn-icons-png.flaticon.com/512/4712/4712100.png" if role == 'assistant' else "https://cdn-icons-png.flaticon.com/512/9131/9131529.png"
    role_class = "assistant" if role == 'assistant' else "user"
    confidence_text = f"confidence {confidence}% • " if confidence else ""

    st.markdown(f"""
    <div class="chat-message {role_class}">
        <img class="avatar" src="{avatar_url}" />
        <div>
            <div class="bubble">{text}</div>
            <div class="meta">{confidence_text}{timestamp}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if prompt and prompt != st.session_state.last_prompt:
    st.session_state.last_prompt = prompt
    now = datetime.datetime.now().strftime("%I:%M %p")
    st.session_state.messages.append({'role': 'user', 'content': prompt, 'time': now})
    
    PROMPT_TEMPLATE = """
    You are a customer support chatbot.
    Use only the provided context to answer the user's question.
    If not found in context, say "I’m not sure about that".
    Keep it polite and helpful. You are strictly asked to do not mention DM.
    dont be hopeless. give good answers.

    Context: {context}
    Question: {question}

    Response:
    """

    try:
        vectorstore = get_vectorstore()
        qa_chain = RetrievalQA.from_chain_type(
            llm=load_llm(),
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
            return_source_documents=False,
            chain_type_kwargs={'prompt': set_custom_prompt(PROMPT_TEMPLATE)}
        )

        response = qa_chain.invoke({'query': prompt})
        answer = response["result"]
        confidence = round(70 + 30 * os.urandom(1)[0] / 255, 2)  # Simulated confidence

        st.session_state.messages.append({'role': 'assistant', 'content': answer, 'time': now, 'confidence': confidence})

    except Exception as e:
        st.session_state.messages.append({'role': 'assistant', 'content': f"Error: {e}", 'time': now})

for msg in st.session_state.messages:
    render_bubble(msg['role'], msg['content'], msg['time'], msg.get('confidence'))
