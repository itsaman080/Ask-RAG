import streamlit as st
from dotenv import load_dotenv
from rag_chatbot import ChatBot

load_dotenv()

st.set_page_config(page_title="Bangalore Travel Assistant", page_icon="🧭", layout="centered")
st.title("Bangalore Travel Assistant Bot")

# Initialize chatbot once per session
if "bot" not in st.session_state:
    with st.spinner("Loading knowledge base and connecting to Pinecone / Groq..."):
        st.session_state.bot = ChatBot(doc_path="./Data/Bangalore_travel_assistant.txt")

bot: ChatBot = st.session_state.bot

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm Bangalore TravelBot — ask me about sights, food, transport, or itineraries."}
    ]

# Display conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask me about Bangalore (e.g., 'best time to visit Lalbagh', 'where to eat dosa')")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... retrieving relevant info"):
            try:
                response_text = bot.answer(user_input)
            except Exception as e:
                response_text = "Sorry — I hit an error while generating an answer."
                st.error(f"Error: {e}")

        st.write(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
