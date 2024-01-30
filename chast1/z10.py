from tkinter import *
root=Tk()

c = Canvas(width=300, height=300,bg='white')
c.pack()
ball = c.create_oval(140, 140, 160, 160,fill='blue')

def mouse(event):
    x=event.x
    y=event.y
    root.unbind('<Button-1>')
    move(x,y)
def move(x,y):
    if (c.coords(ball)[2]+c.coords(ball)[0])/2<x:
        c.move(ball, 1,0)
    if (c.coords(ball)[2]+c.coords(ball)[0])/2>x:
        c.move(ball, -1,0)
    if (c.coords(ball)[3]+c.coords(ball)[1])/2<y:
        c.move(ball, 0,1)
    if (c.coords(ball)[3]+c.coords(ball)[1])/2>y:
        c.move(ball, 0,-1)
    if (c.coords(ball)[3]+c.coords(ball)[1])/2!=y or (c.coords(ball)[2]+c.coords(ball)[0])/2!=x:
        root.after(10, move, x,y)
    else:
        root.bind('<Button-1>', mouse)
root.bind('<Button-1>', mouse)
root.mainloop()
