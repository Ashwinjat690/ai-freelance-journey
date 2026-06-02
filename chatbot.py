import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="Buddy", page_icon="🤖", layout="centered")

# Name
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if not st.session_state.user_name:
    name = st.text_input("Heyy friend! What's your name? 😊", placeholder="Your name...")
    if name:
        st.session_state.user_name = name
        st.rerun()
    st.stop()

st.title(f"🤖 Hey {st.session_state.user_name}! I'm Buddy")
st.markdown("**Your friendly AI bro who talks like a real person** ❤️")

api_key = st.text_input("Groq API Key:", type="password", value=st.session_state.get("api_key", ""))

if api_key:
    st.session_state.api_key = api_key
    
    llm = ChatOpenAI(
        model="llama-3.1-8b-instant",
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
        temperature=0.9
    )

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": f"Arre {st.session_state.user_name}! Wassup bro? 👋 I'm Buddy, your personal AI friend. I can help you with Python doubts, college assignments, motivation, or just chill talks. Kya help chahiye aaj? 🔥"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Bolo kya scene hai..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Buddy soch raha hai..."):
                response = llm.invoke([HumanMessage(content=prompt)])
                st.markdown(response.content)
                st.session_state.messages.append({"role": "assistant", "content": response.content})
else:
    st.info("Enter your Groq API key above to talk with Buddy 👆")