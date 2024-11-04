from tkinter import *
import PyPDF2
from tkinter import filedialog
root=Tk()

#root.iconbitmap('тут скоро будет путь')
#root.title('а тут заголовок')
root.geometry("500x500")

text = Text(root,height=30,width=60)
text.pack()
def open_pdf():
    pass
def get_audio():
    pass
def get_summary():
    pass
def get_picture():
    pass

menu = Menu(root)
root.config(menu=menu)

file_menu= Menu(menu, tearoff = False)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Открыть",command=open_pdf)
file_menu.add_command(label="Озвучка",command=get_audio)
file_menu.add_command(label="Сжатие",command=get_summary)
file_menu.add_command(label="Получить изображение",command=get_picture)
file_menu.add_command(label="Выйти",command=root.quit)


root.mainloop()

