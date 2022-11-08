#Importing of modules
from tkinter import *
from tkinter import messagebox as mb
import json
import os
import random

#Defining window,size and title
root=Tk()
root.geometry("806x470")
root.title("Quiz app using Tkinter")

#initialising images for screen background and buttons
bg = PhotoImage(file = "lvl3bg.png")
label2 = Label( root, image=bg)
label2.place(x=0,y=0,relwidth=1,relheight=1)
nextimg=PhotoImage(file="next3.png")
submitimg=PhotoImage(file="sub3.png")

#centering of quiz window on device screen
frame1 = Frame(root)
frame1.pack(pady = 20 )
app_width = 806
app_height = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#importing quiz data from json file
with open("data3.json") as f:
    data=json.load(f)
question=(data['question'])
answer=(data['answer'])
options=(data['options'])
hint=(data['hints'])

#initialising variables needed for functioning of program
question_number=0
correct_answers=0
data_size=len(question)
ans=0
wrong_answers=0
fifty_option=2
timer_time=15
timer_check=1

#function for checking if selected option is correct or not
def check_ans():
    global answer
    global question_number
    if ans==answer[question_number-1]:
        return 1
    else:
        return 0       

#function that defines what happens when next button is clicked
def nxt_btn():
    global correct_answers
    global question_number
    global timer_check
    
    question_number=question_number+1
    if (question_number-1)==data_size:
        end()
    elif (question_number-1)==data_size-1:
        nextb.config(image=submitimg)
        ques()
        option()
        for i in range(4):
            opts[i].config(state = "normal")
            opts[i].config(bg="white")
        nextb.place(x=705,y=250)
        timer_check=0    
    elif (question_number-1)==0:
        ques()
        option()
        for i in range(4):
            opts[i].config(state = "normal")
            opts[i].config(bg="white")
    else:
        ques()
        option()
        for i in range(4):
            opts[i].config(state = "normal")
            opts[i].config(bg="white")
        timer_check=0
    enable()

#function to load question onto screen based on current question_number        
def ques():
    global question
    qn1=Label(root,bg="#0C1013",fg="white",text=question[question_number-1],width=42,font=("ms sans serif",15),anchor='n')
    qn1.place(x=148,y=215)

#functions defining what buttons should do when clicked
def Button1():
    global ans
    global correct_answers
    global wrong_answers
    ans=1
    for i in range(4):
        opts[i].config(state = "disabled")
    if check_ans():
        opts[ans-1].config(bg="#B0FC38")
    else:
        opts[0].config(bg="#E3242B")
        opts[answer[question_number-1]-1].config(bg="#B0FC38")
    if check_ans()==1:
        correct_answers=correct_answers+1
    elif check_ans()==0:
        wrong_answers=wrong_answers+1
    question_display_color()
    if wrong_answers==5:
        mb.showwarning("Too many mistakes!","You have made five mistakes,Try again!")
        end()    
def Button2():
    global ans
    global correct_answers
    global wrong_answers
    ans=2
    for i in range(4):
        opts[i].config(state = "disabled")
    if check_ans():
        opts[ans-1].config(bg="#B0FC38")
    else:
        opts[1].config(bg="#E3242B")
        opts[answer[question_number-1]-1].config(bg="#B0FC38") 
    if check_ans()==1:
        correct_answers=correct_answers+1
    elif check_ans()==0:
        wrong_answers=wrong_answers+1
    question_display_color()
    if wrong_answers==5:
        mb.showwarning("Too many mistakes!","You have made five mistakes,Try again!")
        end()      
def Button3():
    global ans
    global correct_answers
    global wrong_answers
    ans=3
    for i in range(4):
        opts[i].config(state = "disabled")
    if check_ans():
        opts[ans-1].config(bg="#B0FC38")
    else:
        opts[2].config(bg="#E3242B")
        opts[answer[question_number-1]-1].config(bg="#B0FC38") 
    if check_ans()==1:
        correct_answers=correct_answers+1
    elif check_ans()==0:
        wrong_answers=wrong_answers+1
    question_display_color()    
    if wrong_answers==5:
        mb.showwarning("Too many mistakes!","You have made five mistakes,Try again!")
        end()    
def Button4():
    global ans
    global correct_answers
    global wrong_answers
    ans=4
    for i in range(4):
        opts[i].config(state = "disabled")
    if check_ans():
        opts[ans-1].config(bg="#B0FC38")
    else:
        opts[3].config(bg="#E3242B")
        opts[answer[question_number-1]-1].config(bg="#B0FC38") 
    if check_ans()==1:
        correct_answers=correct_answers+1
    elif check_ans()==0:
        wrong_answers=wrong_answers+1
    question_display_color()
    if wrong_answers==5:
        mb.showwarning("Too many mistakes!","You have made five mistakes,Try again!")
        end()
#function that initialises options on buttons based on question_number
def option():
        val=0
        for i in options[question_number-1]:
            opts[val]['text']=i
            val+=1

#function for initialising buttons onto the screen               
pixel = PhotoImage(width=1, height=1)
def ansbuttons():
        btn1 = Button(root,text='',borderwidth=0,command=Button1,image=pixel,
          width=211,
          height=50,
          compound="c",font = ("ms sans serif",14))
        btn1.place(x=146,y=297)
        btn2 = Button(root,text='',borderwidth=0,command=Button2,image=pixel,
          width=211,
          height=50,
          compound="c",font = ("ms sans serif",14))
        btn2.place(x=445,y=297)
        btn3 = Button(root,text='',borderwidth=0,command=Button3,image=pixel,
          width=211,
          height=50,
          compound="c",font = ("ms sans serif",14))
        btn3.place(x=146,y=373)
        btn4 = Button(root,text='',borderwidth=0,command=Button4,image=pixel,
          width=211,
          height=50,
          compound="c",font = ("ms sans serif",14))
        btn4.place(x=445,y=373)
        q_list=[btn1,btn2,btn3,btn4]
        return q_list
opts=ansbuttons()

#function for calculating and displaying the result
def result():
        unattempted = data_size - correct_answers - wrong_answers
        correct_answerss = f"Correct: {correct_answers}"
        wrong_answerss = f"Wrong_answers: {wrong_answers}"
        unans=f"Unattempted:{unattempted}"
        score = int(correct_answers / data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result", f"{result}\n{correct_answerss}\n{wrong_answerss}\n{unans}")        

#function for fifty-fifty helpline
def fifty():
    global fifty_option
    if opts[0]["state"]=="normal" and opts[1]["state"]=="normal" and opts[2]["state"]=="normal" and opts[3]["state"]=="normal":
        fifty_option=fifty_option-1
        if int(answer[question_number-1])==1:
            choices=[1,2,3]
            a=random.choice(choices)
            choices.remove(a)
            opts[a].config(state="disabled")
            b=random.choice(choices)
            choices.remove(b)
            opts[b].config(state="disabled")
        elif int(answer[question_number-1])==2:
            choices=[0,2,3]
            a=random.choice(choices)
            choices.remove(a)
            opts[a].config(state="disabled")
            b=random.choice(choices)
            choices.remove(b)
            opts[b].config(state="disabled")
        elif int(answer[question_number-1])==3:
            choices=[0,1,3]
            a=random.choice(choices)
            choices.remove(a)
            opts[a].config(state="disabled")
            b=random.choice(choices)
            choices.remove(b)
            opts[b].config(state="disabled")
        elif int(answer[question_number-1])==4:
            choices=[0,1,2]
            a=random.choice(choices)
            choices.remove(a)
            opts[a].config(state="disabled")
            b=random.choice(choices)
            choices.remove(b)
            opts[b].config(state="disabled")   
        if fifty_option == 0:
            fiftyb.config(state="disabled")
            fiftyb.config(background="#E3242B")

#functions for hints helpline
def hints():
    if (question_number)>10:
        h=hint[question_number-11]
        mb.showinfo("Hint",h)
    hintb.config(state="disabled")
    hintb.config(background="#E3242B")
def enable():
    if (question_number)==11:
        hintb.config(state="normal")
        hintb.config(background="#171C20")

#function for instructions and displaying it
def instructions():
    mb.showinfo("Instructions",f"This Quiz has fifteen questions\nIf you make five mistakes, the quiz ends!\nTwo lifelines are provided.\n50-50 lifeline eliminates two incorrect options,\nIt is available two times.\nHints lifeline gives a hint about the answer,\nIt is available from the 11th question.")

#function that displays question numbers on top that indicates if answer is correct or not
def question_display():
    x_pos=90
    l_list=[]
    for i in range(1,16):
        labe=Label(root,text=i,width=5,bg="#37444F",fg="white")
        labe.place(x=x_pos,y=1)
        x_pos=x_pos+42
        l_list.append(labe)
    return l_list
def question_display_color():
    x_pos=90+(question_number-1)*(42)
    if check_ans():
        labe=Label(root,text=question_number,width=5,bg="#B0FC38")    
        labe.place(x=x_pos,y=1)
    else:
        labe=Label(root,text=question_number,width=5,bg="#E3242B")    
        labe.place(x=x_pos,y=1)    

#function for returning to home screen
def home():
    root.destroy()
    os.system("python home.py")

#functions and label to initialise timer and ensure its functioning when next button is clicked
def timer_chk():
    global timer_time
    global timer_check
    if timer_check==1:
        return True
    elif timer_check==0:
        if question_number>0 and question_number<=10:
            timer_time=15
            timer_check=1
            timerl.config(bg="#3B454E")
        elif question_number>10:
            timer_time=25
            timer_check=1
            timerl.config(bg="#3B454E")
counter=15
timer_label = StringVar()
timer_label.set(counter)
timerl=Label(root, textvariable=timer_label,width=4,font=(6),bg="#3B454E")
timerl.place(x=379,y=172)
def timer_quiz(i, label):
    global timer_time
    if timer_time > -1:
        timer_time -= 1
        timer_chk()
        if timer_time<=4:
            timerl.config(bg="#E3242B")
        label.set(i)
        root.after(1000, lambda: timer_quiz(timer_time, label))
    else:
        if question_number>0 and question_number<=10:
            timer_time=15
            timerl.config(bg="#3B454E")
            nxt_btn()
            timer_quiz(timer_time,label)
        elif question_number>10:
            timer_time=25
            timerl.config(bg="#3B454E")
            nxt_btn()
            timer_quiz(timer_time,label)        
        
timer_quiz(counter, timer_label)

#function for ending quiz program
def end():
    result()
    home()

#function to display warning messageboxes
def quit():
    r=mb.askquestion("Warning!","Do you want to exit?",icon="warning")
    if r=="yes":
        root.destroy()
def quithome():
    r=mb.askquestion("Warning!","Do you want to return to Home?",icon="warning")
    if r=="yes":
        home()
        root.destroy()
                
#defining and placing next button 
nextb=Button(root,command=nxt_btn,image=nextimg,borderwidth=0,activebackground="#121619",bg="#121619",fg="white")
nextb.place(x=740,y=250)
fiftyb=Button(root,text="50-50",command=fifty,borderwidth=0,activebackground="#171C20",bg="#171C20",fg="white",font=("lucida",12),width=8)
fiftyb.place(x=723,y=100)
hintb=Button(root,text="Hints",command=hints,borderwidth=0,activebackground="#171C20",bg="#E3242B",fg="white",font=("lucida",12),width=8,state="disabled")
hintb.place(x=723,y=134)

#creation of menubar
menubar = Menu(root)
filemenu = Menu(menubar,background="#0C1013")
menubar.add_cascade(label='Menu',background="#0C1013", menu=filemenu)
filemenu.add_command(label="Home",background="#3B454E",foreground="white",command=quithome)
filemenu.add_separator()
filemenu.add_command(label='Instructions',background="#3B454E",foreground="white",command=instructions)
filemenu.add_separator()
filemenu.add_command(label='Exit',background="#3B454E",foreground="white", command=quit)
root.config(menu=menubar)

#calling of functions
question_display()
ques()
check_ans()
option()
nxt_btn()

root.mainloop()
