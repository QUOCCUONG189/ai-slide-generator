from docx import Document

def read_docx(file) -> str:
    """
    Đọc file .docx và trả về toàn bộ nội dung dạng text
    """
    doc = Document(file)
    paragraphs = []

    for p in doc.paragraphs:
        text = p.text.strip()
        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs)
