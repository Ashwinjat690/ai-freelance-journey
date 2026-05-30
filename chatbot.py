import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

st.title("🌟 My First AI Chatbot - Day 2")
st.write("**AI Freelance Journey**")

# API Key
api_key = st.text_input("Enter your Groq API Key:", type="password")

if api_key:
    llm = ChatOpenAI(
        model="llama3-8b-8192",
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            response = llm.invoke([HumanMessage(content=prompt)])
            st.markdown(response.content)
            st.session_state.messages.append({"role": "assistant", "content": response.content})
else:
    st.info("👆 Enter your Groq API key above to start chatting!")