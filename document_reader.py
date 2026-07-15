import os
from PyPDF2 import PdfReader
from docx import Document


def read_document(filepath):

    extension = os.path.splitext(filepath)[1].lower()

    # Read TXT File
    if extension == ".txt":
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    # Read PDF File
    elif extension == ".pdf":

        text = ""

        pdf = PdfReader(filepath)

        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

        return text

    # Read DOCX File
    elif extension == ".docx":

        text = ""

        doc = Document(filepath)

        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        return text

    return ""