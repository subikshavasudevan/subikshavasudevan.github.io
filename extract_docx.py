from docx import Document

# Open the DOCX file
doc = Document('AV - (1).docx')

# Extract all text content
full_text = []
for para in doc.paragraphs:
    if para.text.strip():
        full_text.append(para.text)

# Print all content
print('\n'.join(full_text))
