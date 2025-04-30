from fpdf import FPDF

def clean_text(text):
    return text.encode('latin-1', 'replace').decode('latin-1')

def convert_to_pdf(text, title, subtitle=None):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(0, 10, clean_text(title), align='C')
    pdf.ln(2)

    if subtitle:
        pdf.set_font("Arial", 'I', 12)
        pdf.multi_cell(0, 10, clean_text(subtitle), align='C')
        pdf.ln(5)

    pdf.set_font("Arial", '', 11)
    for line in text.split('\n'):
        line = clean_text(line.strip())
        if line.startswith("### "):
            pdf.set_font("Arial", 'B', 12)
            pdf.multi_cell(0, 10, line[4:])
            pdf.set_font("Arial", '', 11)
        elif line.startswith("## "):
            pdf.set_font("Arial", 'B', 13)
            pdf.multi_cell(0, 10, line[3:])
            pdf.set_font("Arial", '', 11)
        elif line.startswith("# "):
            pdf.set_font("Arial", 'B', 14)
            pdf.multi_cell(0, 10, line[2:])
            pdf.set_font("Arial", '', 11)
        elif line == "":
            pdf.ln(4)
        else:
            pdf.multi_cell(0, 8, line)

    return pdf.output(dest='S').encode('latin-1')
