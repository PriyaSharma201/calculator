# # PROPER CALCULATOR:-

import tkinter as tk
from tkinter import *

root=Tk()
root.geometry("450x480")
root.maxsize(450,480)
root["bg"]="pink"
root.title("Calculator002")

def numeric(num):
    value = entery_box.get(1.0,'end-1c')
    entery_box.delete(1.0,END)
    entery_box.insert(END,str(value)+str(num))
def exitt():
    entery_box.delete(1.0,END)
def add():
    global add
    add =  entery_box.get(1.0,'end-1c') 
    global oper 
    oper = "+"
    entery_box.delete(1.0,END)
def sub():
    global sub
    sub = entery_box.get(1.0,'end-1c')
    global oper 
    oper = "-"
    entery_box.delete(1.0,END)
def mul():
    global m
    m = entery_box.get(1.0,'end-1c')
    global oper 
    oper = "*"
    entery_box.delete(1.0,END)

def div():
    global d
    d = entery_box.get(1.0,'end-1c')
    global oper 
    oper = "/"
    entery_box.delete(1.0,END)


def equal():
    second = entery_box.get(1.0,'end-1c') 
    entery_box.delete(1.0,END)
    if oper == "+":
        entery_box.insert(END,int(add) + int(second))
    elif oper == '-':
        entery_box.insert(END,int(sub) - int(second))
    elif oper == '*':
        entery_box.insert(END,int(m) * int(second))
        
    elif oper == '/':
        entery_box.insert(END,int(d) / int(second))



lbl=Label(text="CALCULATOR",font="serif 20 bold",fg="violet",bg="black")
lbl.grid(columnspan=5)

entery_box=Text(root,height=4,width=54)
entery_box.grid(row=1,column=1,columnspan=4)

btn1=Button(root,text="1",font="serif 20 bold",padx=29,pady=10,bd=8,command=lambda:numeric("1"))
btn1.grid(row=2,column=1)
btn2=Button(root,text="2",font="serif 20 bold",padx=29,pady=10,bd=8,command=lambda:numeric("2"))
btn2.grid(row=2,column=2)
btn3=Button(root,text="3",font="serif 20 bold",padx=29,pady=10,bd=8,command=lambda:numeric("3"))
btn3.grid(row=2,column=3)
btn4=Button(root,text="+",font="serif 20 bold",padx=29,pady=10,bd=8,command=add)
btn4.grid(row=2,column=4)

btn5=Button(root,text="4",font="serif 20 bold",padx=29,pady=10,bd=8,command=lambda:numeric("4"))
btn5.grid(row=3,column=1)
btn6=Button(root,text="5",font="serif 20 bold",padx=29,pady=10,bd=8,command=lambda:numeric("5"))
btn6.grid(row=3,column=2)
btn7=Button(root,text="6",font="serif 20 bold",padx=29,pady=10,bd=8,command=lambda:numeric("6"))
btn7.grid(row=3,column=3)
btn8=Button(root,text="-",font="serif 20 bold",padx=29,pady=10,bd=8,command=sub)
btn8.grid(row=3,column=4)

btn9=Button(root,text="7",font="serif 20 bold",padx=29,pady=10,bd=8,command=lambda:numeric("7"))
btn9.grid(row=4,column=1)
btn10=Button(root,text="8",font="serif 20 bold",padx=29,pady=10,bd=8,command=lambda:numeric("8"))
btn10.grid(row=4,column=2)
btn11=Button(root,text="9",font="serif 20 bold",padx=29,pady=10,bd=8,command=lambda:numeric("9"))
btn11.grid(row=4,column=3)
btn12=Button(root,text="x",font="serif 20 bold",padx=29,pady=10,bd=8,command=mul)
btn12.grid(row=4,column=4)

btn13=Button(root,text="%",font="serif 20 bold",padx=35,pady=10,bd=8,command=div)
btn13.grid(row=5,column=1)
btn14=Button(root,text="0",font="serif 20 bold",padx=29,pady=10,bd=8,command=lambda:numeric("0"))
btn14.grid(row=5,column=2)
btn15=Button(root,text="=",font="serif 20 bold",padx=29,pady=10,bd=8,command=equal)
btn15.grid(row=5,column=3)
btn16 = Button(root,text="c",font='serif 20 bold',padx=29,pady=10,bd=8,command=exitt)
btn16.grid(row=5,column=4)

mainloop()