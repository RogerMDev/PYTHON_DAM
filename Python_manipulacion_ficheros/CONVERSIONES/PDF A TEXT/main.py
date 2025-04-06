import PyPDF2

def pdf_to_text(pdf_file, txt_file):
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        # Extraer texto de cada página
        for page in reader.pages:
            text += page.extract_text() + "\n"

    # Guardar el texto en un archivo .txt
    with open(txt_file, "w", encoding="utf-8") as txt:
        txt.write(text)

    print(f"✅ Texto extraído y guardado en {txt_file}")

# ⚡️ USO: Convertir "documento.pdf" en "salida.txt"
pdf_to_text("text.pdf", "conversion.txt")



