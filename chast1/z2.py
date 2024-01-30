from tkinter import *
ttt = Tk()
def color(btn):
    text2.delete(0,END)
    text2.insert(0,btn['bg'])
    text1['text'] = btn['text']


text1=Label(text='цвет')
text2=Entry(width=50)
btn1 = Button(command=lambda: color(btn1),width=30,bg='#ff0000', text='красный')
btn2 = Button(command=lambda: color(btn2),width=30,bg='#ff7d00', text='оранжевый')
btn3 = Button(command=lambda: color(btn3),width=30,bg='#ffff00', text='желтый')
btn4 = Button(command=lambda: color(btn4),width=30,bg='#00ff00', text='зеленый')
btn5 = Button(command=lambda: color(btn5),width=30,bg='#007dff', text='голубой')
btn6 = Button(command=lambda: color(btn6),width=30,bg='#0000ff', text='синий')
btn7 = Button(command=lambda: color(btn7),width=30,bg='#7d00ff', text='фиолетовый')
text1.pack()
text2.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()
ttt.mainloop()
