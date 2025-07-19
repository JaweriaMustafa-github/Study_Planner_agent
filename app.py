import streamlit as st 
from datetime import datetime
from agents.planner_agent import generate_study_plan
from utils.pdf_export import generate_pdf

# Set page configuration
st.set_page_config(page_title="Study Planner Agent", layout="centered")

# Gradient background style
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #E0EAFC, #80BD9E);
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("📚 Study Planner Agent")

# Show today's date and day
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
day_str = now.strftime("%A")
st.markdown(f"**📅 Date:** {date_str} | **🗓️ Day:** {day_str}")

# User inputs
start = st.slider("Start Hour", 6, 12, 8)
end = st.slider("End Hour", 13, 22, 20)
topic = st.text_input("What do you want motivation for?", "focus")

# Session state defaults
if "schedule" not in st.session_state:
    st.session_state.schedule = None
    st.session_state.quote = ""

# Generate schedule when button clicked
if st.button("Generate Study Plan"):
    schedule_dict, quote = generate_study_plan(start, end, topic)  # ✅ FIXED unpacking
    st.session_state.schedule = schedule_dict
    st.session_state.quote = quote

# Display the schedule if available
if st.session_state.schedule:
    st.subheader("📅 Your Study Schedule")
    st.markdown(f"📅 **Date**: {st.session_state.schedule['date']} ({st.session_state.schedule['day']})")
    st.markdown("---")
    
    for block in st.session_state.schedule["blocks"]:
        st.markdown(f"**{block['type']}**: {block['start']} → {block['end']}")

    # Show motivational quote
    st.subheader("🌟 Motivational Quote")
    st.success(st.session_state.quote)

    # Debug/log view (optional)
    st.write("🧾 Current Schedule:", st.session_state.schedule)

    # Download PDF button
    pdf_buffer = generate_pdf(st.session_state.schedule)
    st.download_button(
        label="📥 Download Schedule as PDF",
        data=pdf_buffer,
        file_name="study_schedule.pdf",
        mime="application/pdf"
    )
