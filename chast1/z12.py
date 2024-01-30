from tkinter import *
test = 0
def okno():
    def change(r):
        global test
        test = r['text']
    def paint():
        global c
        global test
        if test == 'квадрат':
            c.create_rectangle(int(e1.get()), int(e2.get()), int(e3.get()),
            int(e4.get()))
        elif test =='овал':
            c.create_oval(int(e1.get()), int(e2.get()), int(e3.get()),
            int(e4.get()))
        else:
            print('выберите фигуру')
    new = Toplevel()
    new.geometry('200x150')
    l1=Label(new,text='x1')
    e1=Entry(new)
    e1.grid(row=0,column=0),l1.grid(row=0,column=1)
    l2=Label(new,text='y1')
    e2=Entry(new)
    e2.grid(row=1,column=0),l2.grid(row=1,column=1)
    l3=Label(new,text='x2')
    e3=Entry(new)
    e3.grid(row=2,column=0),l3.grid(row=2,column=1)
    l4=Label(new,text='y2')
    e4=Entry(new)
    e4.grid(row=3,column=0),l4.grid(row=3,column=1)
    r1=Radiobutton(new,text='квадрат', value=0,command= lambda: change(r1))
    r2=Radiobutton(new,text='овал', value=1, command= lambda: change(r2))
    r1.grid(row=4,column=0),r2.grid(row=4,column=1)
    b1=Button(new, text='нарисовать', command=paint)
    b1.grid(row=5,column=0)
root = Tk()
c=Canvas(root, width=300, height=200, bg="white")
c.pack()
Button(text="добавить фигуру", width=20,command=okno).pack()
root.mainloop()