from customtkinter import *
from PIL import Image, ImageTk


def roate():
    global img, c, photo, image1
    img = img.rotate(90)
    c.delete(image1)
    photo = ImageTk.PhotoImage(img)
    image1 = c.create_image(0,0,anchor='nw',image=photo)

def Change_size():
    global img,c,photo,image1,e1,e2
    img=img.resize((int(e1.get()),int(e2.get())))
    width, height = img.size
    root.geometry(str(width)+'x'+str(height+50))
    c['width'],c['height']=width,height
    c.delete(image1)
    photo = ImageTk.PhotoImage(img)
    image1 = c.create_image(0,0,anchor='nw',image=photo)




root = CTk()
root.title('image')
set_appearance_mode('dark')
set_default_color_theme('blue')
path = filedialog.askopenfilename()
img = Image.open(path)
width, height = img.size
root.geometry(str(width)+'x'+str(height+50))

c = CTkCanvas(root, width=width,height=height)
c.pack()
photo = ImageTk.PhotoImage(img)
image1 = c.create_image(0,0,anchor='nw',image=photo)
b1 = CTkButton(root,text='rotate',command=roate)
b1.pack(side='left')
e1 = CTkEntry(root,placeholder_text='ширина')
e2 = CTkEntry(root,placeholder_text='высота')
b2 = CTkButton(root,text='scale',command=Change_size)
e1.pack(side='left')
e2.pack(side='left')
b2.pack(side='left')


root.mainloop()