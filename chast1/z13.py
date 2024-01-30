from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def clear():
    answer = mb.askyesno(
        title="подтверждение", 
        message="очистить данные?")
    if answer:
        text.delete('0.0', END)

 
def insert_text():
    try:
        file_name = fd.askopenfilename()
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    except:
        mb.showerror("файл то выбери")
 
 
def extract_text():
    try:
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                    ("HTML files", "*.html;*.htm"),
                    ("All files", "*.*")))
        f = open(file_name, 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
    except:
        mb.showerror("файл то выбери")
 
 
root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extract_text)
b2.grid(row=1, column=1, sticky=W)
b3 = Button(text='очистить', command=clear)
b3.grid(row=1,column=1)
 
root.mainloop()