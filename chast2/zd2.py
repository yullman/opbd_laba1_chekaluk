from customtkinter import *
from tkinter import *


def mess(arg):
    new_title = CTk()
    message = CTkTextbox(new_title)
        
    if arg['text']=='Веселое':
        message.insert("0.0", "НУ и хорошо")
    if arg['text']=='Грустное':
        message.insert("0.0", "Не грусти че ты")
    if arg['text']=='Безразличное':
        message.insert("0.0", "ну ладно")
    if arg['text']=='Взволнованое':
        message.insert("0.0", "Не волнуйся лол")
        
    message.pack()
    new_title.mainloop()

root = CTk()
root.title('настроение')
root.geometry('200x150')
root.resizable(False,False)
set_appearance_mode('dark')
set_default_color_theme('blue')
l1 = CTkLabel(root,text='выберите ваше настроение')
b1 = Button(root,text='Веселое',command=lambda: mess(b1))
b2 = Button(root,text='Грустное',command=lambda: mess(b2))
b3 = Button(root,text='Безразличное',command=lambda: mess(b3))
b4 = Button(root,text='Взволнованое',command=lambda: mess(b4))
l1.pack(),b1.pack(),b2.pack(),b3.pack(),b4.pack()

root.mainloop()