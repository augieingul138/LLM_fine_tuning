import fitz  # PyMuPDF
pdf_path = "C:/Users/augus/Documents/STKboka.pdf"

def extract_text_from_pdf(pdf_path):
    text_content = []
    doc = fitz.open(pdf_path)
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text_content.append(page.get_text("text"))
    return text_content

print(extract_text_from_pdf(pdf_path))