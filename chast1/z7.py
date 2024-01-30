from tkinter import *
root = Tk()

def add1(d):
    global e1
    box.insert(END,  e1.get())


def add2(d):
    global e1
    select = list(box.curselection())
    select.reverse()
    for i in select:
        e1.delete(0,END)
        e1.insert(END,box.get(i))

e1 = Entry()
box = Listbox(selectmode=EXTENDED)
e1.bind('<Return>', add1)
box.bind('<Double-Button-1>',add2)
e1.pack()
box.pack()
root.mainloop()
