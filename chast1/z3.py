from tkinter import *
ttt = Tk()
def color(btn):
    text2.delete(0,END)
    text2.insert(0,btn['bg'])
    text1['text'] = btn['text']


text1=Label(text='цвет')
text2=Entry(width=50)
btn1 = Button(command=lambda: color(btn1),width=10,bg='#ff0000', text='красный')
btn2 = Button(command=lambda: color(btn2),width=10,bg='#ff7d00', text='оранжевый')
btn3 = Button(command=lambda: color(btn3),width=10,bg='#ffff00', text='желтый')
btn4 = Button(command=lambda: color(btn4),width=10,bg='#00ff00', text='зеленый')
btn5 = Button(command=lambda: color(btn5),width=10,bg='#007dff', text='голубой')
btn6 = Button(command=lambda: color(btn6),width=10,bg='#0000ff', text='синий')
btn7 = Button(command=lambda: color(btn7),width=10,bg='#7d00ff', text='фиолетовый')
text1.pack()
text2.pack()
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=LEFT)
btn5.pack(side=LEFT)
btn6.pack(side=LEFT)
btn7.pack(side=LEFT)
ttt.mainloop()
