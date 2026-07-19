# app.py
import streamlit as st
import requests

st.title("⚽ FIFA 2026 Fan Concierge")
st.markdown("Ask me for directions, wait times, or accessibility routes!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("E.g., 'How do I get to Section 112 from Gate 4?'"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call your active FastAPI backend
    try:
        response = requests.post("https://fifa-worldcup-gen-ai.onrender.com", json={"query": prompt})
        response_data = response.json()
        answer = response_data.get("response", "Error: No response from API.")
    except Exception as e:
        answer = f"Error connecting to backend: {e}"

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})