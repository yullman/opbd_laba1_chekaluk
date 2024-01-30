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
    new.geometry('200x250')
    l1=Label(new,text='x1')
    e1=Entry(new)
    e1.pack(),l1.pack()
    l2=Label(new,text='y1')
    e2=Entry(new)
    e2.pack(),l2.pack()
    l3=Label(new,text='x2')
    e3=Entry(new)
    e3.pack(),l3.pack()
    l4=Label(new,text='y2')
    e4=Entry(new)
    e4.pack(),l4.pack()
    r1=Radiobutton(new,text='квадрат', value=0,command= lambda: change(r1))
    r2=Radiobutton(new,text='овал', value=1, command= lambda: change(r2))
    r1.pack(),r2.pack()
    b1=Button(new, text='нарисовать', command=paint)
    b1.pack()
root = Tk()
c=Canvas(root, width=300, height=200, bg="white")
c.pack()
Button(text="добавить фигуру", width=20,command=okno).pack()
root.mainloop()