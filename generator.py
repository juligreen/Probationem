import datetime

from fpdf import FPDF

name = 'Julius Dehner'
department = 'Kundensysteme'
certificate_count = 0
date = datetime.date(2018, 5, 13)
date_endofweek = date + datetime.timedelta(days=4)
year = 1

header_origin_x = 90
header_origin_y = 19
header_second_line = 34
left_edge = 18
right_edge = 190

pdf = FPDF()
pdf.add_page()
pdf.set_font('Helvetica', size=11.5)
pdf.text(header_origin_x, header_origin_y, 'Name:')
pdf.text(header_origin_x + 20, header_origin_y, name)
pdf.line(header_origin_x + 19, header_origin_y + 1, right_edge, header_origin_y + 1)

pdf.text(header_origin_x, header_origin_y + 5, 'Ausbildungsabteilung:')
pdf.text(header_origin_x + 46, header_origin_y + 5, department)
pdf.line(header_origin_x + 45, header_origin_y + 6, right_edge, header_origin_y + 6)

pdf.set_font('Helvetica', 'B', size=14)
pdf.text(left_edge, header_second_line, 'Ausbildungsnachweis')
pdf.set_font('Helvetica', size=11.5)
pdf.text(left_edge + 63, header_second_line, str(certificate_count))
pdf.text(left_edge + 70, header_second_line, str(date))
pdf.text(left_edge + 103, header_second_line, str(date_endofweek))
pdf.text(left_edge + 165, header_second_line, str(year))
pdf.line(left_edge + 61, header_second_line + 1, left_edge + 96, header_second_line + 1)
pdf.line(left_edge + 103, header_second_line + 1, left_edge + 135, header_second_line + 1)
pdf.line(left_edge + 160, header_second_line + 1, right_edge, header_second_line + 1)
pdf.set_font('Helvetica', size=7.5)
pdf.text(left_edge + 63, header_second_line + 4, 'Nr.')
pdf.text(left_edge + 70, header_second_line + 4, 'Ausbildungswoche vom')
pdf.text(left_edge + 103, header_second_line + 4, 'bis')
pdf.text(right_edge - 18.9, header_second_line + 4, 'Ausbildungsjahr')

pdf.rect(left_edge, 45, right_edge - left_edge, 175)

pdf.output('tuto1.pdf', 'F')
