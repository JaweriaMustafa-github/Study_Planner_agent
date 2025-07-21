import streamlit as st 
from datetime import datetime
from agents.planner_agent import generate_study_plan
from utils.pdf_export import generate_pdf

# --- Page Config and Styling ---
st.set_page_config(page_title="Study Planner Agent", layout="centered")
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #E0EAFC, #80BD9E);
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title and Date ---
st.title("📚 Study Planner Agent")

now = datetime.now()
date_str = now.strftime("%d-%m-%Y")
day_str = now.strftime("%A")
st.markdown(f"**📅 Date:** {date_str} | **🗓️ Day:** {day_str}")

# --- UI Inputs ---
start = st.slider("Start Hour", 6, 12, 8)
end = st.slider("End Hour", 13, 22, 20)
topic = st.text_input("What do you want motivation for?", "focus")

# --- Session State Init ---
if "schedule" not in st.session_state:
    st.session_state.schedule = None
    st.session_state.quote = ""

# --- Generate Button ---
if st.button("Generate Study Plan"):
    schedule, quote = generate_study_plan(start, end, topic)
    st.session_state.schedule = schedule
    st.session_state.quote = quote

# --- Render Schedule ---
if st.session_state.schedule:
    st.subheader("📅 Your Study Schedule")
    st.markdown(f"📅 **Date**: {st.session_state.schedule['date']} ({st.session_state.schedule['day']})")
    st.markdown("---")

    for block in st.session_state.schedule["blocks"]:
        st.markdown(f"**{block['type']}**: {block['start']} → {block['end']}")

    # --- Motivational Quote ---
    st.subheader("🌟 Motivational Quote")
    st.success(st.session_state.quote)

    # --- Debug View (optional) ---
    st.write("🧾 Current Schedule:", st.session_state.schedule)

    # --- PDF Download ---
    pdf_buffer = generate_pdf(st.session_state.schedule)
    st.download_button(
        label="📥 Download Schedule as PDF",
        data=pdf_buffer,
        file_name="study_schedule.pdf",
        mime="application/pdf"
    )
