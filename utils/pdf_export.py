from fpdf import FPDF
from io import BytesIO
from datetime import datetime  # <-- Import datetime to get date and day

def generate_pdf(schedule):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Get current date and weekday
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%D")
    day_str = now.strftime("%A")

    # Title
    pdf.cell(200, 10, txt="Personalized Study Schedule", ln=True, align="C")
    pdf.ln(5)

    # Date and Day
    pdf.set_font("Arial", size=11)
    pdf.cell(200, 10, txt=f"Date: {date_str} | Day: {day_str}", ln=True, align="C")
    pdf.ln(10)

    # Schedule content
    for block in schedule:
        pdf.cell(200, 10, txt=f"{block['type']} | {block['start']} - {block['end']}", ln=True)

    pdf_output = pdf.output(dest='S').encode('latin-1')
    return BytesIO(pdf_output)
