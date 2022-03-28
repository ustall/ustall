from PyPDF2 import PdfFileWriter, PdfFileMerger, PdfFileReader

# pdf_file='F:/max/Programs2/Myfiles/PDFbot/in.pdf'
# save_file='F:/max/Programs2/Myfiles/PDFbot/out.pdf'
def cropPDF(pdf_file,save_file):
    with open(pdf_file, "rb") as in_f:
        input1 = PdfFileReader(in_f)
        output = PdfFileWriter()

        numPages = input1.getNumPages()
        # print("document has %s pages." % numPages)

        for i in range(numPages):
            page = input1.getPage(i)
            # print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
            # page.trimBox.lowerLeft = (0, 50)
            # page.trimBox.upperRight = (0, 150)
            page.cropBox.lowerLeft = (0, 64)
            page.cropBox.upperRight = (1260, 2455)
            output.addPage(page)

        with open(save_file, "wb") as out_f:
            output.write(out_f)