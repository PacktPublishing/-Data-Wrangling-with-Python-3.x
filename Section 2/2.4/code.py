from fpdf import FPDF
pdf = FPDF()

pdf.add_page()
pdf.set_font('Arial',size = 16)
pdf.cell(200,10,txt = "My Resume",ln = 1,align = "C")
pdf.cell(2,10,txt = "My Skills",ln = 1)
pdf.set_font('Arial',size = 10)
pdf.cell(2,10,txt = "DataScience",ln = 1)
pdf.cell(2,10,txt = "Machine Learning",ln = 1)
pdf.cell(2,10,txt = "Deep Learning",ln = 1)

pdf.image('image.png', x = 100, y = 25, w = 50)
pdf.output('sample_resume.pdf')

