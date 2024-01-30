from tkinter import *

root = Tk()

c = Canvas(root, width=300, height=350, bg='white')
c.pack()

c.create_polygon(150,150,150,300,300,300,300,150,fill='blue')
c.create_polygon(150,150,225,100,300,150,fill='blue')
c.create_polygon(0,300,300,300,300,350,0,350,fill='green')
c.create_oval(10,100,100,10,fill='yellow')

root.mainloop()
