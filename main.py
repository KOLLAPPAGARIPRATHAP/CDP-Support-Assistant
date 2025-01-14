import os
import json
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from vectorize_documents import embeddings

working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
GROQ_API_KEY = config_data["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


def setup_vectorstore():
    persist_directory = f"{working_dir}/vector_db_dir"
    embeddings = HuggingFaceEmbeddings()
    vectorstore = Chroma(persist_directory=persist_directory,
                         embedding_function=embeddings)
    return vectorstore


def chat_chain(vectorstore):
    llm = ChatGroq(model="llama-3.1-70b-versatile",
                   temperature=0)
    retriever = vectorstore.as_retriever()
    memory = ConversationBufferMemory(
        llm=llm,
        output_key="answer",
        memory_key="chat_history",
        return_messages=True
    )
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        memory=memory,
        verbose=True,
        return_source_documents=True
    )

    return chain


st.set_page_config(
    page_title="MCDP Support Assistant",
    page_icon="🛃",
    layout="centered"
)

st.title("🛃 MCDP Support Assistant")

# Clear chat functionality
if st.button("Clear Chat"):
    st.session_state.chat_history.clear()
    st.experimental_rerun()

# Initialize chat history if not already in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize vectorstore if not already in session state
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = setup_vectorstore()

# Initialize conversational chain if not already in session state
if "conversational_chain" not in st.session_state:
    st.session_state.conversational_chain = chat_chain(st.session_state.vectorstore)

# Display previous conversation
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask AI...")

# Define irrelevant keywords or phrases
irrelevant_keywords = ["movie", "sports", "weather", "news", "music", "book", "celebrity", "tv", "game", "show"]

if user_input:
    # Add user input to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Display user message in chat
    with st.chat_message("user"):
        st.markdown(user_input)

    # Check if the user input contains irrelevant keywords
    if any(keyword in user_input.lower() for keyword in irrelevant_keywords):
        assistant_response = "I'm sorry, I can only help with CDP-related queries."
    else:
        # Show spinner while processing the response
        with st.spinner('Processing your request...'):
            response = st.session_state.conversational_chain({"question": user_input})
            assistant_response = response["answer"]

    # Display assistant response in chat
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    # Add assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
