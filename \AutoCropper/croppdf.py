from tkinter import *
from tkinter import filedialog as fd
import crop
from crop import cropPDF

def callback():
    name = fd.askopenfilename()
    ePath.config(state='normal')
    ePath.delete('1', END)
    ePath.insert('1', name)
    ePath.config(state='readonly')

def cropAction():
    pdf_file=ePath.get()
    save_file=fd.asksaveasfile().name
    # print(save_file)
    cropPDF(pdf_file,save_file)

root = Tk()
root.title('Eazy crop PDF by Maxim G')
root.geometry('500x500+500+200')
FileButton = Button(root, text="Выбрать PDF файл", font="Arial 15 bold", fg="black", command=callback)
FileButton.pack(pady=15)

lbPath=Label(root, text="Путь к файлу: ", font="Arial 15 bold",)
lbPath.pack()

ePath = Entry(root,width=60,state='readonly')
ePath.pack(pady=10)

cropbutton = Button(root, text="Обрезать и сохранить", font="Arial 15 bold", fg="black", command=cropAction)
cropbutton.pack(pady=10)
root.mainloop()
if __name__ == "__main__":
    input()

