from docx import Document

def read_docx(file):
    doc = Document(file)
    blocks = []

    for p in doc.paragraphs:
        if p.style.name.startswith("Heading"):
            blocks.append(f"\n{p.text}\n")
        else:
            blocks.append(p.text)

    return "\n".join(blocks)
