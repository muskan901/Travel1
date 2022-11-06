from tkinter import *
import sqlite3
import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
a=Tk()
a.minsize(1540,1100)
a.iconbitmap("C:\Gui\india.ico.jpg")
Image1=Image.open("india.ico.jpg").resize((1530,800))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=0,y=0)

frame=Frame(bg="White")
frame.place(x=510,y=20,width=540,height=759)

a.iconbitmap("C:\Gui\login.ico.jpg")
Image1=Image.open("login.ico.jpg").resize((220,150))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test,bg="white")
label1.image=test
label1.place(x=650,y=90)

label2=Label(frame,text="Forgot Password",font=("Arial",25,"bold"),fg="Blue",bg="white").place(x=130,y=10)

var1=StringVar()
var2=StringVar()
var3=StringVar()

label3=Label(frame,text="Email Address:",font=("Arial",15,"bold"),fg="black",bg="white").place(x=40,y=250)
et1=Entry(frame,font=("Arial",15,"bold"),bd=2,textvariable=var1)
et1.insert(0,"Email")
et1.place(x=100,y=310,width=280)

label4=Label(frame,text="New Password:",font=("Arial",15,"bold"),fg="black",bg="white").place(x=40,y=400)
et2=Entry(frame,font=("Arial",15,"bold"),bd=2,textvariable=var2)
et2.insert(0,"New Password")
et2.place(x=100,y=460,width=280)

label5=Label(frame,text="Confirm Password:",font=("Arial",15,"bold"),fg="black",bg="white").place(x=40,y=550)
et3=Entry(frame,font=("Arial",15,"bold"),bd=2,textvariable=var3)
et3.insert(0,"Confirm Password")
et3.place(x=100,y=610,width=280)

def main():
    a.destroy()
    import main_travel

b1=Button(frame,text="EXIT->",bg="lightblue",font=("Arial",15,"bold"),command=main).place(x=350,y=670)

a.mainloop()