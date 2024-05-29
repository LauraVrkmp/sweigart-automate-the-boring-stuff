import os, sys, PyPDF2

output_dir = os.path.abspath('Encrypted pdfs')
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

input_dir = os.path.abspath("C:\\Users\\Laura\\OneDrive\\Bureaublad\\programmeren\\sweigart-automate-the-boring-stuff\\Chapter 13\\Pdfs")

password = sys.argv[1]

for folderName, subfolders, filenames in os.walk(input_dir):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfFile = open(input_dir + '\\' + filename, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFile)
            pdfWriter = PyPDF2.PdfWriter()
            for pageNum in range(len(pdfReader.pages)):
                pdfWriter.add_page(pdfReader.pages[pageNum])
            
            pdfWriter.encrypt(password)
            resultPdf = open('Encrypted pdfs\\' + filename[:-4] + '_encrypted.pdf', 'wb')
            pdfWriter.write(resultPdf)
            pdfFile.close()
            resultPdf.close()