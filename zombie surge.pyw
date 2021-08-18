from tkinter import *
from threading import Thread
from random import randint

root=Tk()
root.state('zoomed')
root.title('Zombie Surge')
root.geometry('1184x559+38+36')

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

frame=Frame(root,width=width,height=height,bg='#23961d')
frame.pack()

entities={'character':{'Joe':PhotoImage(file='Joe.PNG'),'zombie':PhotoImage(file='zombie.PNG')},'hand':{'empty':PhotoImage(file='empty.PNG'),'knife':PhotoImage(file='knife.PNG'),'gun':PhotoImage(file='gun.PNG')},'drop':{'bullet':PhotoImage(file='bullet_drop.PNG'),'knife':PhotoImage(file='knife_drop.PNG')}}        

Joe=Label(frame,image=entities['character']['Joe'],bg='#23961d')
Joe.place(x=635,y=322)
health=10

def coord(entity=Joe):
    return entity.winfo_x(),entity.winfo_y()

def update(x,y):
    Joe.place_forget()
    Joe.place(x=x,y=y)

def replace(file,nfile):
    x,y=coord()
    file.place_forget()
    nfile.place(x=x,y=y)

def stop():
    pass        

def move_w(event):
    x,y=coord()
    update(x,y-10)

def move_a(event):
    x,y=coord()
    update(x-10,y)

def move_s(event):
    x,y=coord()
    update(x,y+10)

def move_d(event):
    x,y=coord()
    update(x+10,y)

w=move_w
a=move_a
s=move_s
d=move_d

def monitor():
    while True:
        x,y=coord()
        global w,a,s,d
        print(f'x: {x}, y: {y}')
        if x>width or x<=0 or y>height or y<=0:
            print('True')
            w=stop
            a=stop
            s=stop
            d=stop
        else:
            w=move_w
            a=move_a
            s=move_s
            d=move_d

monitor_thread=Thread(target=monitor)
monitor_thread.start()

frame.bind('<w>',w)
frame.bind('<Up>',w)
frame.bind('<a>',a)
frame.bind('<Left>',a)
frame.bind('<s>',s)
frame.bind('<Down>',s)
frame.bind('<d>',d)
frame.bind('<Right>',d)

frame.focus_set()
root.mainloop()
