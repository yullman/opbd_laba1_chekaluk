from tkinter import *
ttt = Tk()
ttt.geometry('300x300')
def otkr():
    text.delete(1.0, END)
    with open(entrytxt.get()+".txt") as file:
        for items in file:
            text.insert(1.0, items )
def sohr():
    f = open(entrytxt.get()+".txt", 'w')
    f.write(text.get(0.0,END))

btn1= Button(command=otkr,text='Открыть')
btn2= Button(command=sohr, text='Сохранить')
entrytxt = Entry()
text = Text(width=25, height=5, bg="white",
            fg='Black', wrap=WORD)
text['height']=100
scroll = Scrollbar(command=text.yview)
text.config(yscrollcommand=scroll.set)
entrytxt.pack()
btn1.pack()
btn2.pack()
scroll.pack(side=RIGHT, fill=Y)
text.pack(side=BOTTOM)
ttt.mainloop()
