from dotenv import load_dotenv
import os
from mistralai.client import Mistral
load_dotenv()
import streamlit as st


client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

st.title("AI chatbot")
st.caption("Made by Geethanjali")
#clear button
if st.button("clear"):
    st.session_state.messages = []
    st.rerun()

#memory
if "messages" not in st.session_state:
    st.session_state.messages = []

#display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt=st.chat_input("ask anything......")

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response=client.chat.complete(
        model="ministral-3b-latest",
        messages=st.session_state.messages
    )

    answer=response.choices[0].message.content
    st.session_state.messages.append({"role":"assistant","content":answer})
    with st.chat_message("assistant"):
        st.write(answer)