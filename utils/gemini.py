import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def get_motivational_quote(topic: str) -> str:
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(f"Give me a short motivational quote related to {topic}.")
    return response.text.strip()
