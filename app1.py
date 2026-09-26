from dotenv import load_dotenv
import os
from mistralai.client import Mistral
import streamlit as st
load_dotenv()

client=Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
prompt=st.text_input("ask anything......")

response=client.chat.complete(
    model="ministral-3b-latest",
    messages=[
        {"role":"user","content":prompt}
    ]
)

# print(response.choices[0].message.content)
st.write(response.choices[0].message.content)





