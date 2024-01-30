from tkinter import *
from random import *
okno = Tk()
okno.title('рандулятор')
okno.geometry('600x600')
but1 = Button(okno, text="+", width=50,height=3,bd=10)
but2 = Button(okno, text="-",width=50,height=3,bd=10)
but3 = Button(okno, text="x",width=50,height=3,bd=10)
but4 = Button(okno, text="/",width=50,height=3,bd=10)
but5 = Button(okno, text="рандомный пример",width=50,height=3,bd=10)
lab = Label(okno, width=50, bg='black', fg='white',height=3,bd=10)
ent = Entry(okno, width=50)
ent2 = Entry(okno, width=50)
def rann():
    ok = randint(1,5)
    b1 = randint(1,5)
    b2 = randint(1,5)
    b3 = randint(1,5)
    b4 = randint(1,5)
    if ok == 1:
        ok = 'blue'
    elif ok ==2:
        ok ='red'
    elif ok ==3:
        ok ='purple'
    elif ok ==4:
        ok ='yellow'
    elif ok ==5:
        ok ='green'
    if b1 == 1:
        b1 = 'blue'
    elif b1 ==2:
        b1 ='red'
    elif b1 ==3:
        b1 ='purple'
    elif b1 ==4:
        b1 ='yellow'
    elif b1 ==5:
        b1 ='green'
    if b2 == 1:
        b2 = 'blue'
    elif b2 ==2:
        b2 ='red'
    elif b2 ==3:
        b2 ='purple'
    elif b2 ==4:
        b2 ='yellow'
    elif b2 ==5:
        b2 ='green'
    if b3 == 1:
        b3 = 'blue'
    elif b3 ==2:
        b3 ='red'
    elif b3 ==3:
        b3 ='purple'
    elif b3 ==4:
        b3 ='yellow'
    elif b3 ==5:
        b3 ='green'
    if b4 == 1:
        b4 = 'blue'
    elif b4 ==2:
        b4 ='red'
    elif b4 ==3:
        b4 ='purple'
    elif b4 ==4:
        b4 ='yellow'
    elif b4 ==5:
        b4 ='green'
    okno['bg'] = ok
    but1['bg'] = b1
    but2['bg'] = b2
    but3['bg'] = b3
    but4['bg'] = b4
rann()
def plus(event):
    rann()
    g = str(float(ent.get()) + float(ent2.get()))
    lab['text'] = ' '.join(g)
def minus(event):
    rann()
    g = str(float(ent.get()) - float(ent2.get()))
    lab['text'] = ' '.join(g)
def umnoj(event):
    rann()
    g = str(float(ent.get()) * float(ent2.get()))
    lab['text'] = ' '.join(g)
def delit(event):
    rann()
    g = str(float(ent.get()) / float(ent2.get()))
    lab['text'] = ' '.join(g)
def ran(event):
    rann()
    f = randint(-10000000000,10000000000)
    s = randint(-10000000000,10000000000)
    ent.delete(0,END)
    ent2.delete(0,END)
    ent.insert(0,f)
    ent2.insert(0,s)
but1.bind('<Button-1>', plus)
but2.bind('<Button-1>', minus)
but3.bind('<Button-1>', umnoj)
but4.bind('<Button-1>', delit)
but5.bind('<Button-1>', ran)
ent.pack()
ent2.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
lab.pack()
okno.mainloop()