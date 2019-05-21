import datetime

from fpdf import FPDF

name = 'Julius Dehner'
department = 'Kundensysteme'
certificate_count = 0
date = datetime.date(2018, 5, 13)
date_endofweek = date + datetime.timedelta(days=4)
year = 1
corporate_activities = ['- Probationem enwickeln', '- VIM lernen', '- Liebe machen']
teachings = ['- ISO-OSI-Modell erklärung', '- Objektorientierung']
school_activities = ['Englisch: Mal was sinnvolles ', 'Vernetzte Systeme: Mehr Unsinn']

header_origin_x = 90
header_origin_y = 19
header_second_line = 34
left_edge = 18
right_edge = 190
box_start = 44
second_box_start = 108
third_box_start = 148
text_in_box_location = left_edge + 1
box_end = 175
sign_box_start = 226
sign_box_height = 34
sign_box_end = sign_box_start + sign_box_height
box_spacing = (right_edge - left_edge) / 3


def set_heading_font():
    pdf.set_font('Helvetica', 'B', size=14)


def set_box_heading_font():
    pdf.set_font('Helvetica', 'B', size=12)


def set_regular_font():
    pdf.set_font('Helvetica', size=11.5)


pdf = FPDF()
pdf.add_page()
set_regular_font()
pdf.set_line_width(0.3)
pdf.text(header_origin_x, header_origin_y, 'Name:')
pdf.text(header_origin_x + 20, header_origin_y, name)
pdf.line(header_origin_x + 19, header_origin_y + 1, right_edge, header_origin_y + 1)

pdf.text(header_origin_x, header_origin_y + 5, 'Ausbildungsabteilung:')
pdf.text(header_origin_x + 46, header_origin_y + 5, department)
pdf.line(header_origin_x + 45, header_origin_y + 6, right_edge, header_origin_y + 6)

set_heading_font()
pdf.text(left_edge, header_second_line, 'Ausbildungsnachweis')
set_regular_font()
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

pdf.set_line_width(0.4)
pdf.rect(left_edge, box_start, right_edge - left_edge, 7)
set_box_heading_font()
pdf.text(text_in_box_location, box_start + 5, 'Betriebliche Tätigkeiten')

set_regular_font()
for index, activity in enumerate(corporate_activities):
    pdf.text(left_edge + 2, box_start + 20 + index * 5, activity)

pdf.rect(left_edge, second_box_start, right_edge - left_edge, 7)
set_box_heading_font()
pdf.text(text_in_box_location, second_box_start + 5,
         'Unterweisungen, Lehrgespräche, betrieblicher Unterricht, sonstige Schulungen')

set_regular_font()
for index, activity in enumerate(teachings):
    pdf.text(left_edge + 2, second_box_start + 20 + index * 5, activity)

pdf.rect(left_edge, third_box_start, right_edge - left_edge, 7)
set_box_heading_font()
pdf.text(text_in_box_location, third_box_start + 5, 'Berufsschule (Unterrichtsthemen)')

set_regular_font()
for index, activity in enumerate(school_activities):
    pdf.text(left_edge + 2, third_box_start + 20 + index * 5, activity)

pdf.rect(left_edge, box_start, right_edge - left_edge, box_end)

pdf.set_font('Helvetica', size=9.7)
pdf.text(text_in_box_location - 1, box_start + box_end + 5,
         'Durch die nachfolgenden Unterschriften wird die Richtigkeit und Vollständigkeit der obigen Angaben bestätigt.'
         )

pdf.rect(left_edge, sign_box_start, right_edge - left_edge, sign_box_height)
set_box_heading_font()
pdf.text(text_in_box_location, sign_box_start + 6, f'Datum: {str(date_endofweek)}')
pdf.line_width = 0.2
pdf.line(left_edge + box_spacing, sign_box_start, left_edge + box_spacing, sign_box_start + sign_box_height)
pdf.text(left_edge + box_spacing + 1, sign_box_start + 6, f'Datum: {str(date_endofweek)}')
pdf.line(left_edge + box_spacing*2, sign_box_start, left_edge + box_spacing*2, sign_box_start + sign_box_height)
pdf.text(left_edge + box_spacing * 2 + 1, sign_box_start + 6, f'Datum: {str(date_endofweek)}')
pdf.line(left_edge, sign_box_start + 9, right_edge, sign_box_start + 9)

pdf.line(left_edge, sign_box_end - 5, right_edge, sign_box_end - 5)
pdf.set_font('Helvetica', 'B', size=11.5)
pdf.text(left_edge + 11, sign_box_end - 1, 'Auszubildende/-r')
pdf.text(left_edge + box_spacing + 15, sign_box_end - 1, 'Ausbilder/-in')
pdf.text(left_edge + box_spacing * 2 + 4, sign_box_end - 1, 'Gesetzliche/-r Vertreter/-in')
pdf.output('tuto1.pdf', 'F')
