import os, PyPDF2

input_file = os.path.abspath("Encrypted pdfs\\combinedminutes_encrypted.pdf")

dictionary = open('dictionary.txt', 'r')
words = dictionary.readlines()
dictionary.close()

pdfFile = open(input_file, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFile)

for word in words:
    word = word.strip('\n')
    lower = word.lower()
    upper = word.upper()
    if pdfReader.decrypt(lower) != 0:
        print('Found the password: ' + lower)
        break
    elif pdfReader.decrypt(upper) != 0:
        print('Found the password: ' + upper)
        break

pdfFile.close()