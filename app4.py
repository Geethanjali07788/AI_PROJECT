import os
from dotenv import load_dotenv
from google import genai
import streamlit as st
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
st.title("AI Translator")
st.caption("Powered by Gemini")
languages = ["English", "Telugu", "Hindi", "Tamil", "Urdu","Kannada", "Malayalam", "Spanish", "Japanese","Chinese", "Bengali"]
if "source_language" not in st.session_state:st.session_state.source_language = "English"
if "destination_language" not in st.session_state:
    st.session_state.destination_language = "Telugu"
col1, col2 = st.columns(2)
with col1:
    source_language = st.selectbox(
        "Source",languages,index=languages.index(st.session_state.source_language))
with col2:
    destination_language = st.selectbox("Destination",languages,index=languages.index(st.session_state.destination_language))
st.session_state.source_language = source_language
st.session_state.destination_language = destination_language
if st.button("Swap"):
    temp = st.session_state.destination_language
    st.session_state.destination_language = st.session_state.source_language
    st.session_state.source_language = temp
    st.rerun()
text = st.text_area("Enter text to translate")
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        prompt = f"""
Translate the following text from {source_language} to {destination_language}.Text:{text}
Strict rules:
1. Don't add extra information.
2. Don't remove existing information.
3. Don't summarize the text.
4. Act as a professional native translator.
5. Give the response naturally in {destination_language}.
6. Return only the translated text.
"""       
        response = client.models.generate_content(model="gemini-3.5-flash-lite",contents=prompt)
        st.subheader("Translated Text")
        st.text_area("Translation:",response.text,height=150)