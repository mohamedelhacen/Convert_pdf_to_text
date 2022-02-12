import PyPDF2
import os

textPath = ""
pdfPath = ""

pdfPath = input("Enter the path of your pdf file: ")
textPath = input("(Optional) Enter the path to save the text file in: ")

if (len(textPath) == 0):
    if (os.path.isdir("temp") == False):
        os.mkdir("temp")
    BASEDIR = os.path.realpath("temp")
    textPath = os.path.join(BASEDIR, os.path.basename(os.path.normpath(pdfPath)).replace(".pdf", "")+".txt")
    print("The text file is saved to the folder: ", BASEDIR)

pdfObj = open(pdfPath, 'rb')
pdfRead = PyPDF2.PdfFileReader(pdfObj)

x = pdfRead.numPages
for i in range(x):
    pageObj = pdfRead.getPage(i)
    with open(textPath, 'a+') as f:
        f.write((pageObj.extractText()))

pdfObj.close()