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
        mb.showerror("ошибка")
 
 
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
        mb.showerror("ошибка")
 
 
root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)

mainmenu = Menu(root) 
root.config(menu=mainmenu) 
mainmenu.add_command(label="открыть", command=insert_text)
mainmenu.add_command(label="сохранить", command=extract_text)
mainmenu.add_command(label="очистить", command=clear)



root.mainloop()