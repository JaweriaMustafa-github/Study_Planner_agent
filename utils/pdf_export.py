from fpdf import FPDF
from io import BytesIO

def generate_pdf(schedule):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Personalized Study Schedule", ln=True, align="C")
    pdf.ln(10)

    for block in schedule:
        pdf.cell(200, 10, txt=f"{block['type']} | {block['start']} - {block['end']}", ln=True)

    pdf_output = pdf.output(dest='S').encode('latin-1')  # correct way to export as string
    return BytesIO(pdf_output)
