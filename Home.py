import os
from tkinter import *
from tkinter import messagebox as mb

gui=Tk()
gui.geometry("807x450")
gui.title("Home")

bg=PhotoImage(file="homebg.png")  
label1 = Label( gui, image=bg)
label1.place(x=0,y=0,relwidth=1,relheight=1)

frame1 = Frame(gui)
frame1.pack(pady = 20 )

app_width = 807
app_height = 450
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

gui.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

f=open("level.txt","r")
lvl=f.read(1)
f.close()

def call1():
    instructions()
    gui.destroy()
    os.system("python quiz1.py")
def call2():
    instructions()
    gui.destroy()
    os.system("python quiz2.py")
def call3():
    instructions()
    gui.destroy()
    os.system("python quiz3.py")  

def level():
    if lvl=='2':
        quiz2.config(state="normal")
        quiz3.config(state="disabled")
        lvls.config(image=lvl2)
    elif lvl=='3':
        quiz2.config(state="normal")
        quiz3.config(state="normal")
        lvls.config(image=lvl3) 
    else:
        quiz2.config(state="disabled")
        quiz3.config(state="disabled")
        lvls.config(image=lvl1)



pixel = PhotoImage(width=1, height=1)

opt1=PhotoImage(file="opt1.png")
opt2=PhotoImage(file="opt2.png")
opt3=PhotoImage(file="opt3.png")
lvl1=PhotoImage(file="lvl1.png")
lvl2=PhotoImage(file="lvl2.png")
lvl3=PhotoImage(file="lvl3.png")

quiz1=Button(gui,bg="#1D2932",activebackground="#1D2932",borderwidth=0,command=call1,image=opt1,height=300,width=210)
quiz1.place(x=57,y=60)
quiz2=Button(gui,bg="#1D2932",activebackground="#1D2932",borderwidth=0,command=call2,image=opt2,height=300,width=210)
quiz2.place(x=297,y=60)
quiz3=Button(gui,bg="#1D2932",activebackground="#1D2932",borderwidth=0,command=call3,image=opt3,height=300,width=210)
quiz3.place(x=537,y=60)


lvls=Label(gui,image=lvl1,borderwidth=0)
lvls.place(y=366,x=0)
pix=Label(bg="#1B262F",text="",fg="#1B262F")
pix.place(x=400,y=9)

level()

def instructions():
    mb.showinfo("Instructions","This Quiz has fifteen questions\nIf you make five mistakes, the quiz ends!\nTwo lifelines are provided.\n50-50 lifeline eliminates two incorrect options,\nIt is available two times.\nHints lifeline gives a hint about the answer,\nIt is available from the 11th question.")   

def enable1(e):
    if lvl=='1' or lvl=='2' or lvl=='3':
      info.config(text=r"Click to continue") 
def enable1_end(e):
    info.config(text="Welcome, to play click on topic")
quiz1.bind("<Enter>",enable1)
quiz1.bind("<Leave>",enable1_end)

def enable2(e):
    if lvl=='1':
      info.config(text=r"To unlock level 2, score 80% or more in level 1")  
    elif lvl=='2'or lvl=='3':
        info.config(text=r"Click to continue")

    else:
      info.config(text="Welcome, to play click on topic")
def enable2_end(e):
    info.config(text="Welcome, to play click on topic")
quiz2.bind("<Enter>",enable2)
quiz2.bind("<Leave>",enable2_end)

def enable3(e):
    if lvl=='2'or lvl=="1":
      info.config(text=r"To unlock level 3, score 80% or more in level 2")
    elif lvl=='3':
        info.config(text=r"Click to continue")  
    else:
      info.config(text="Welcome, to play click on topic")
def enable3_end(e):
    info.config(text="Welcome, to play click on topic")
quiz3.bind("<Enter>",enable3)
quiz3.bind("<Leave>",enable3_end)

info=Label(gui,bg='#1D2932',fg="#587683",text="Welcome, to play click on topic",width=114,font=("agency fb",15,"bold"),anchor=N)
info.place(x=2,y=1)

def end():
    r=mb.askquestion("Warning!","Do you want to exit?",icon="warning")
    if r=="yes":
        gui.destroy()

def reset():
    r=mb.askquestion("Warning!","Are you sure you want to reset?\nThis will clear all your progress.",icon="warning")
    if r=='yes':
        f=open("level.txt","w")
        f.write("1")
        f.close()
        level()
        gui.destroy()
        os.system("python Home.py")        

menubar = Menu(gui)
filemenu = Menu(menubar,background="#587683")
menubar.add_cascade(label='Menu', menu=filemenu)
filemenu.add_command(label="Reset",background='#1D2932',foreground="white",command=reset)
filemenu.add_separator()
filemenu.add_command(label='Instructions',background='#1D2932',foreground="white",command=instructions)
filemenu.add_separator()
filemenu.add_command(label='Exit',background='#1D2932',foreground="white", command=end)
gui.config(menu=menubar)

gui.mainloop()