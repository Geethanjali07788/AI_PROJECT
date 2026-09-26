import os
from dotenv import load_dotenv
from google import genai
import streamlit as st
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
prompt = st.text_input("ask anything")
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)
if st.button("submit"):
    st.write(response.text)