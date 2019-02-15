import PyPDF2
PDF_data = list()
with open('BestJobPostingSites.pdf','rb') as f:
    pdfReader = PyPDF2.PdfFileReader(f)
    number_of_pages = pdfReader.numPages
    for i in range(number_of_pages):
        page = pdfReader.getPage(i).extractText()
        PDF_data.append(page)
        print(page)
    































