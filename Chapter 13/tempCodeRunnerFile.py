pdfFile = open(input_file, 'rb')
# pdfReader = PyPDF2.PdfReader(pdfFile)
# pdfWriter = PyPDF2.PdfWriter()

# for word in words:
#     if pdfReader.decrypt(word) == 0:
#         print('Password is wrong')
#     else:
#         for pageNum in range(len(pdfReader.pages)):
#             pdfWriter.add_page(pdfReader.pages[pageNum])
#         resultPdf = open('combinedminutes.pdf', 'wb')
#         pdfWriter.write(resultPdf)
#         pdfFile.close()
#         resultPdf.close()