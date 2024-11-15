import openai
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from extract_text import extract_text_normally, extract_text_with_styling

load_dotenv()
key = os.getenv("api_key")

def find_pages_for_chapters(text_chunk):
    client = openai.OpenAI(api_key=key)
    prompt = ("Given to you in this prompt are the first 20 pages of a textbook in the form of a continuous text string." + 
    "Find the pages showing the contents of the book, and extract the chapters (and subchapters), and their corresponding page numbers." +
    "Return it on the format (Chap1: (page, name) newline, Sub1: (page, name) newline, Sub2: (page, name) newline, Chap2: (page, name) newline etc)." +
    "If there are several layers of subchapters, the next layer can be called something like SubSub1, SubSub2, etc..." +
    "The last thing you should now is that newlines can appear where they should not, and ** encapsulates bold text, * italic, and **** a combo." +
    "[number] indicates font size.")
    GPT_MODEL = "gpt-4o" 
    messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": text_chunk},
        ]
    response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=messages,
            temperature=0
        )
    response_dict = response.model_dump()
    return response_dict['choices'][0]["message"]["content"] 


pdf_path = "C:/Users/augus/Documents/STKboka.pdf"
text = extract_text_with_styling(pdf_path, 20)
structured_data = find_pages_for_chapters(text)
print(structured_data)
