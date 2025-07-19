import streamlit as st 
from agents.planner_agent import generate_study_plan
from utils.pdf_export import generate_pdf

st.set_page_config(page_title="Study Planner Agent", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #E0EAFC, #80BD9E);
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📚 Study Planner Agent")

start = st.slider("Start Hour", 6, 12, 8)
end = st.slider("End Hour", 13, 22, 20)
topic = st.text_input("What do you want motivation for?", "focus")

# Store in session state
if "schedule" not in st.session_state:
    st.session_state.schedule = None
    st.session_state.quote = ""

if st.button("Generate Study Plan"):
    schedule, quote = generate_study_plan(start, end, topic)
    st.session_state.schedule = schedule
    st.session_state.quote = quote

# Render if we already have a schedule
if st.session_state.schedule:
    st.subheader("📅 Your Study Schedule")
    for block in st.session_state.schedule:
        st.markdown(f"**{block['type']}**: {block['start']} → {block['end']}")

    st.subheader("🌟 Motivational Quote")
    st.success(st.session_state.quote)

    st.write("🧾 Current Schedule:", st.session_state.schedule)

    # Export Button Outside of "Generate" block
    pdf_buffer = generate_pdf(st.session_state.schedule)
    st.download_button(
        label="📥 Download Schedule as PDF",
        data=pdf_buffer,
        file_name="study_schedule.pdf",
        mime="application/pdf"
    )
