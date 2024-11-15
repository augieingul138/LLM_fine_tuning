import PyPDF2

def extract_text_normally(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        full_text = ""
       
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            full_text += f"\n[Page {page_num + 1}]\n{page_text}"
           
    return full_text

import fitz  # PyMuPDF

def extract_text_with_styling(pdf_path, page_limit):
    doc = fitz.open(pdf_path)
    styled_text = ""

    for page_num in range(page_limit):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        styled_text += f"\n[Page {page_num + 1}]\n"

        for block in blocks:
            for line in block.get("lines", []):
                line_text = ""
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    font = span["font"]
                    font_size = round(span["size"])  # Rounded to nearest integer for simplicity
                    is_bold = "Bold" in font
                    is_italic = "Italic" in font or "Oblique" in font

                    # Add style markers and font size inline
                    if is_bold and is_italic:
                        line_text += f"****{text}****[{font_size}] "
                    elif is_bold:
                        line_text += f"**{text}**[{font_size}] "
                    elif is_italic:
                        line_text += f"*{text}*[{font_size}] "
                    else:
                        line_text += f"{text}[{font_size}] "

                styled_text += line_text.strip() + "\n"  # Add the full styled line

    return styled_text

