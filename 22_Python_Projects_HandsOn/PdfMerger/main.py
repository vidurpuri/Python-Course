from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("Enter how many PDF files you want to merge: "))

for i in range(n):
    name = input(f"Enter the path for PDF file {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

# for testing
# D:\Python Course\22_Python_Projects_HandsOn\PdfMerger\pdf1.pdf
# D:\Python Course\22_Python_Projects_HandsOn\PdfMerger\pdf2.pdf
