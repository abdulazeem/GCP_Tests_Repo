from google.cloud import translate_v3
from google.cloud import vision
import PyPDF2

# ... (Your existing code for initializing clients)

def translate_pdf_text(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # ... (Your existing translation code using `translate_client.translate_text()`)

# Example usage:
pdf_path = 'path/to/your/pdf_file.pdf'
translated_text = translate_pdf_text(pdf_path)