import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        full_text = ""
       
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            full_text += f"\n[Page {page_num + 1}]\n{page_text}"
           
    return full_text