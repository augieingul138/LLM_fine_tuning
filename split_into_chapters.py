import openai
import re
import os
from extract_text import extract_text_from_pdf

# Initialize OpenAI API key
key = "none"

def find_pages_for_chapters(text_chunk):
    """
    Calls OpenAI API to identify chapters and subchapters within a text chunk.
    """
    client = openai.OpenAI(api_key=key)
    prompt = f"Given to you in this prompt are the first 20 pages of a textbook in the form of a continuous text string. Find the pages showing the contents of the book, and extract the chapters (and subchapters), and their corresponding page numbers. Return it on the format (Name1: page1 newline, Name2: page2 newline, etc)"
    GPT_MODEL = "gpt-4o" #"gpt-3.5-turbo-1106"
    messages = [
            {"role": "system", "content": text_chunk},
            {"role": "user", "content": prompt},
        ]
    response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=messages,
            temperature=0
        )
    response_dict = response.model_dump()
    print(response_dict)
    return response_dict['choices'][0]["message"]["content"] 


# Example usage:
pdf_path = "C:/Users/augus/Documents/Jakki.pdf"
text = extract_text_from_pdf(pdf_path).split("[Page 20]")[0]
structured_data = find_pages_for_chapters(text)
print(structured_data)
