from tkinter import *
from random import randint
from tkinter import filedialog

def movik():
    b1.place(x=randint(0,root.winfo_width()-20), y=randint(0,root.winfo_height()-20))


root = Tk()
root.geometry('500x500')
path = filedialog.askopenfilename()
img = PhotoImage(file=path)
b1 = Button(root,image=img,command = movik,width=20,height=20)
b1.pack()

root.mainloop()