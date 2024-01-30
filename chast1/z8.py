from tkinter import *
root = Tk()

def change():
    box['width']=e1.get()
    box['height'] = e2.get()

def focus(event):
    box['bg']='white'

def focus2(event):
    box['bg']='lightgrey'



e1 = Entry()
e2 = Entry()
box = Text()
b1= Button(command=change)
box.bind('<FocusIn>', focus)
box.bind('<FocusOut>', focus2)
b1['text']="изменить"
e1.pack()
e2.pack()
b1.pack()
box.pack()
root.mainloop()
