import PyPDF2 as pyf
from pathlib import Path

nome = "MGLU_ER_3T20_POR.pdf"
arquivo_pdf = pyf.PdfReader(nome)

for i, pagina in enumerate(arquivo_pdf.pages):
    num_pagina = i + 1
    novo_pdf = pyf.PdfWriter()
    novo_pdf.add_page(pagina)
    with Path(f"paginas/Arquivo Pagina {num_pagina}.pdf").open(mode="wb") as arquivo:
        novo_pdf.write(arquivo)

