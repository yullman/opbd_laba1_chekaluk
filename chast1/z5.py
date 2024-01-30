from tkinter import *
root = Tk()

def test(r):
    if r==r1:
        lab['text'] = 'это саня'
    if r== r2:
        lab['text'] = 'это паня'
    if r == r3:
        lab['text'] = 'это маня'

r1 = Radiobutton(command=lambda: test(r1), text="саня", value=1, indicatoron=0)
r2 = Radiobutton(text="паня", value=2, indicatoron=0, command=lambda: test(r2))
r3 = Radiobutton(text="маня", value=3, indicatoron=0, command=lambda: test(r3))

lab = Label(width=25, height=5, bg="white")
lab.pack(side=RIGHT)
r1.pack()
r2.pack()
r3.pack()

root.mainloop()
