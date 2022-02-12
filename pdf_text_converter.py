import PyPDF2
import os

# Initialize the paths
textPath = ""
pdfPath = ""

# Get the the source path and the output path
pdfPath = input("Enter the path to your pdf file: ")
textPath = input("(Optional) Enter the path to save the text file in: ")

# Create the default path in case when the output path is not provided
if (len(textPath) == 0): # Check if the output path is given or not
    if (os.path.isdir("temp") == False): # Check if the temp folder is already exist or not
        os.mkdir("temp")
    BASEDIR = os.path.realpath("temp")
    textPath = os.path.join(BASEDIR, os.path.basename(os.path.normpath(pdfPath)).replace(".pdf", "")+".txt")
    print("The text file is saved to the folder: ", BASEDIR)

# Open and read the pdf file
pdfObj = open(pdfPath, 'rb')
pdfRead = PyPDF2.PdfFileReader(pdfObj)

# Copy the content of each page in the pdf file to the text file
pages = pdfRead.numPages
for i in range(pages):
    pageObj = pdfRead.getPage(i)
    with open(textPath, 'a+') as f:
        f.write((pageObj.extractText()))

# Close the pdf file
pdfObj.close()