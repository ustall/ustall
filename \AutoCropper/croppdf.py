from tkinter import *
from tkinter import filedialog as fd
import crop
# import crop, read
from crop import cropPDF
# from read import readPDF


def callback():
    name = fd.askopenfilename()
    ePath.config(state='normal')
    ePath.delete('0', END)
    ePath.insert('1', name)
    ePath.config(state='readonly')


def cropAction():
    pdf_file = ePath.get()
    save_file = fd.asksaveasfile().name
    save_file = save_file + 'C.pdf'
    print(save_file)
    cropPDF(pdf_file, save_file)

# def bleedAction():
#     pdf_file = ePath.get()
#     save_file = fd.asksaveasfile().name
#     cropPDF(pdf_file, save_file)


# def PdfToDocx():
#     pdf_file = ePath.get()
#     readPDF(pdf_file)


root = Tk()
root.title('Eazy crop PDF by Maxim G')
root.geometry('500x250+500+200')
FileButton = Button(root, text="Выбрать PDF файл", font="Arial 15 bold", fg="black", command=callback)
FileButton.pack(pady=15)

lbPath = Label(root, text="Путь к файлу: ", font="Arial 15 bold", )
lbPath.pack()

ePath = Entry(root, width=60, state='readonly')
ePath.pack(pady=10)

cropbutton = Button(root, text="Обрезать и сохранить", font="Arial 15 bold", fg="black", command=cropAction)
cropbutton.pack(pady=10)

# bleedbutton = Button(root, text="Вырезать Айди", font="Arial 15 bold", fg="black", command=bleedAction)
# bleedbutton.pack(pady=10)

# DocxButton=Button(root, text="Pdf в Docx", font="Arial 15 bold", fg="black", command=PdfToDocx)
# DocxButton.pack(pady=10)

root.mainloop()
if __name__ == "__main__":
    input()
