import pdfplumber
from pdf2image import convert_from_path
import pytesseract
import os

# Set the Tesseract path for Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read_pdf_file(path, lang='ara+eng'):
    """
    Extracts text from any PDF (including scanned/image-based, tables, and Arabic text).
    Tries pdfplumber first, then falls back to OCR if needed.
    """
    text = ""
    # Try pdfplumber for text and tables
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                text += page_text + "\n"
                # Extract tables as markdown
                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        text += " | ".join([cell if cell else "" for cell in row]) + "\n"
    except Exception as e:
        text += f"[pdfplumber error: {e}]\n"
    # If no text found, try OCR
    if not text.strip():
        try:
            images = convert_from_path(path)
            for img in images:
                text += pytesseract.image_to_string(img, lang=lang) + "\n"
        except Exception as e:
            text += f"[OCR error: {e}]\n"
    return text if text.strip() else "No extractable text found in PDF."

# Example usage:
if __name__ == "__main__":
    pdf_path = "7-8.pdf"  # Replace with your PDF path
    result = read_pdf_file(pdf_path)
    print(result)
