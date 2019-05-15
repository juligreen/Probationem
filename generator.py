import datetime

from fpdf import FPDF

name = 'Julius Dehner'
department = 'Kundensysteme'
count = 0
date = datetime.date(2018, 5, 5)

pdf = FPDF()
pdf.add_page()
pdf.rect(20, 45, 170, 400)
pdf.set_font('Arial', size=12)
pdf.text(110, 22, 'Name:')
pdf.line(129, 23, 190, 23)
pdf.output('tuto1.pdf', 'F')
