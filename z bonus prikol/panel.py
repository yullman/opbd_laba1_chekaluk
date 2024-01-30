from tkinter import *
import pyautogui
from random import randint
windows = []
class Window:

    def __init__(self,w,h,x,y,color):
        self.root = Tk()
        self.width = w
        self.height = h
        self.color = color
        self.x = x
        self.y = y
        self.c = Canvas(self.root,width=w,height=h)
        self.c.pack()
        self.ball = self.c.create_oval(w/2+20,h/2+20,w/2-20,h/2-20,fill=self.color)
        self.line= self.c.create_line(w/2,h/2,w/2,h/2,fill=self.color,width=5)
        self.root.geometry(str(self.width)+'x'+str(self.height)+'+'+str(x)+'+'+str(y))
        windows.append([self.root,self.x,self.y,self.line,self.width/2,self.height/2,self.c])


w1 = Window(500,500,randint(0,1000),randint(0,1000),'purple')
w2 = Window(500,500,randint(0,1000),randint(0,1000),'black')
blac=Tk()
blac.geometry('2000x1000')
bc = Canvas(blac,width=2000,height=1200,bg='black')
bl1 = bc.create_line(0,0,0,0,fill='white',width=5)
bl2 = bc.create_line(0,0,0,0,fill='white',width=5)
bc.pack()
l1 = windows[0][6].create_line(0,0,0,0,fill='black',width=5)
l2 = windows[1][6].create_line(0,0,0,0,fill='purple',width=5)
while True:
    for i in range(0,len(windows)):
        windows[i][6].coords(windows[i][3],windows[i][4],windows[i][5],pyautogui.position()[0]-windows[i][1],pyautogui.position()[1]-windows[i][2])
        blac.wm_attributes('-topmost',0)
        windows[i][0].wm_attributes('-topmost',1)
        windows[i][6]['width'] = windows[i][0].winfo_width()
        windows[i][6]['height'] = windows[i][0].winfo_height()
        bc['width'] = blac.winfo_width()
        bc['height'] = blac.winfo_height()
        bc.coords(bl1,pyautogui.position()[0]-blac.winfo_x(),pyautogui.position()[1]-blac.winfo_y(),windows[0][1]+windows[0][4]-blac.winfo_x(),windows[0][2]+windows[0][5]-blac.winfo_y())
        bc.coords(bl2,pyautogui.position()[0]-blac.winfo_x(),pyautogui.position()[1]-blac.winfo_y(),windows[1][1]+windows[1][4]-blac.winfo_x(),windows[1][2]+windows[1][5]-blac.winfo_y())
        windows[0][6].coords(l1,pyautogui.position()[0]-windows[0][1],pyautogui.position()[1]-windows[0][2],windows[1][1]+windows[1][4]-windows[0][1],windows[1][2]+windows[1][5]-windows[0][2])
        windows[1][6].coords(l2,pyautogui.position()[0]-windows[1][1],pyautogui.position()[1]-windows[1][2],windows[0][1]+windows[0][4]-windows[1][1],windows[0][2]+windows[0][5]-windows[1][2])
        windows[i][0].update()
        blac.update()
        windows[i][1] =  windows[i][0].winfo_x()
        windows[i][2] =  windows[i][0].winfo_y()
        
        