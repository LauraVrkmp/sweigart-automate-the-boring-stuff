import os, PyPDF2

output_dir = os.path.abspath('Decrypted pdfs')
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

input_dir = os.path.abspath("Encrypted pdfs")

for folderName, subfolders, filenames in os.walk(input_dir):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfFile = open(input_dir + '\\' + filename, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFile)
            pdfWriter = PyPDF2.PdfWriter()
            if pdfReader.decrypt('password') != 1:
                print(filename + ' failed to decrypt.')
                pdfFile.close()
            else:
                for pageNum in range(len(pdfReader.pages)):
                    pdfWriter.add_page(pdfReader.pages[pageNum])
                resultPdf = open('Decrypted pdfs\\' + filename[:-14] + '.pdf', 'wb')
                pdfWriter.write(resultPdf)
                pdfFile.close()
                resultPdf.close()