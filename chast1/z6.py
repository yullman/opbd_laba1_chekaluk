from tkinter import *
root = Tk()

def addbox():
    select = list(box.curselection())
    select.reverse()
    for i in select:
        box2.insert(END,box.get(i))


def delbox():
    select = list(box2.curselection())
    select.reverse()
    for i in select:
        box2.delete(i)


box = Listbox(selectmode='multiple')
for i in ('колбаса','сыр','молоко','хлеб'):
    box.insert(0,i)
box.pack(side=LEFT)
box2 = Listbox(selectmode='multiple')
box2.pack(side=RIGHT)
f = Frame()
f.pack()
b1=Button(f, text="Add", command=addbox)
b2=Button(f, text="Delete", command=delbox)
b1.pack()
b2.pack()
root.mainloop()
