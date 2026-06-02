import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="Buddy", page_icon="🤖", layout="centered")

# User Name
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if not st.session_state.user_name:
    name = st.text_input("Heyy! What's your name? 😊", placeholder="Enter your name...")
    if name:
        st.session_state.user_name = name
        st.rerun()
    st.stop()

st.title(f"🤖 Hey {st.session_state.user_name}! I'm Buddy")
st.markdown("**Your Friendly AI Bro** ❤️ | Made by Ashwin | NMIMS AIML")

api_key = st.text_input("Enter Groq API Key:", type="password", value=st.session_state.get("api_key", ""))

if api_key:
    st.session_state.api_key = api_key
    
    llm = ChatOpenAI(
        model="llama-3.1-8b-instant",   # ✅ Fixed Model
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
        temperature=0.85
    )

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": f"Arre waah {st.session_state.user_name}! 👋 Kya haal hai bhai? I'm Buddy - your chill AI friend. I can help with Python, college doubts, motivation, or just bakchodi. Bol kya scene hai aaj? 🔥"}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Bolo kya baat hai..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Buddy soch raha hai..."):
                response = llm.invoke([HumanMessage(content=prompt)])
                st.markdown(response.content)
                st.session_state.messages.append({"role": "assistant", "content": response.content})
else:
    st.info("👆 Enter your Groq API key above to start chatting with Buddy")