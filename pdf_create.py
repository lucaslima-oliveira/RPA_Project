from reportlab.pdfgen import canvas

from reportlab.lib.units import inch

from reportlab.lib import colors

from reportlab.lib.pagesizes import A4,landscape,letter

from PyPDF2 import PdfReader, PdfWriter

from datetime import date

#  Create Function from text

def texte_stanp(name,cpf,curso,instituicao):

    day_current = date.today().strftime('%d/%m/%Y')

    model_text = f"""Certificamos que, para os devidos fins,




    
portador do CPF n° {cpf},concluiu o curso livre de {curso}, 
ministrado pelo profissional Haroldo Kobayashi, 
entre o período de {day_current}, na {instituicao}."""
    
    pdf_text = canvas.Canvas('marcad´agua.pdf', pagesize=A4)

    pdf_text.setPageSize(landscape(A4))

    pdf_text.translate(inch, inch)

    pdf_text.setFont('Helvetica', 16)

    pdf_text.setFillColor(colors.blue, alpha=0.80)    

    text_object = pdf_text.beginText(inch, 300)

    for line in model_text.splitlines(False):

        text_object.textLine(line.rstrip())

    pdf_text.drawText(text_object)

    pdf_text.drawCentredString(5*inch, 35, f'{name.title()}')        

    pdf_text.setFont('Helvetica', 44)

    pdf_text.drawString(inch, 250, f"{name.title()}")

    pdf_text.save() 

def cria_certificado(name,cpf,curso,instituicao):

    texte_stanp(name,cpf,curso,instituicao)

    directory_certificate = r"arquives/modelo certificado.pdf" 

    estampa = r'marcad´agua.pdf'

    certificate = f'certificado {name.title()}.pdf'

    with open(directory_certificate, 'rb') as inputfile, open(estampa, 'rb') as estampa_file:

        inputfile = PdfReader(inputfile)
        estampa_file = PdfReader(estampa_file)

        estampa_file = estampa_file.pages[0]

        output = PdfWriter()

        for i in range(len(inputfile.pages)):
            pdf_page = inputfile.pages[i]
            pdf_page.merge_page(estampa_file)

            output.add_page(pdf_page)

        with open(certificate,'wb') as merged:
            output.write(merged)
