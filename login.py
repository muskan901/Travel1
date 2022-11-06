from tkinter import *
import sqlite3
import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
a=Tk()
a.title("Travel n Tourism")
a.minsize(1540,1100)
a.iconbitmap("C:\Gui\india.ico.jpg")
Image1=Image.open("india.ico.jpg").resize((1530,800))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=0,y=0)

frame=Frame(bg="White")
frame.place(x=550,y=70,width=440,height=659)

a.iconbitmap("C:\Gui\login.ico.jpg")
Image1=Image.open("login.ico.jpg").resize((230,140))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test,bg="white")
label1.image=test
label1.place(x=660,y=88)

label3=Label(frame,text="Get Started",font=("Arial",20,"bold"),fg="Red",bg="White").place(x=140,y=160)

def create():
    a.destroy()
    import registration
def passw():
    a.destroy()
    import password

bt2=Button(frame,text="Create Account",font=("Arial",20,"bold"),fg="Black",bg="White",bd=0,command=create).place(x=50,y=500,width=260)
bt3=Button(frame,text="Forgot Password?",font=("Arial",20,"bold"),fg="Black",bg="White",bd=0,command=passw).place(x=50,y=560,width=280)

def login():
    try:
        Username=var1.get()
        Password=var2.get()
        if Username=="" or Password=="":
            messagebox.showwarning("Warning","Please Fill your Details")
        elif Username=="muskan" and Password=="muskan":
            messagebox.showwarning("Success","Successfull")
            os._exit(1)
        else:
            messagebox.showerror("Error","Please enter Invalid information")
    except:
       messagebox.showerror("Error","Please enter Invalid information")
var1=StringVar()
var2=StringVar()

label4=Username=Label(frame,text="Username",font=("Arial",20,"bold"),fg="black",bg="white").place(x=70,y=220)
et1=Entry(frame,font=("Arial",15,"bold"),textvariable=var1).place(x=70,y=260,width=280)

label5=Password=Label(frame,text="Password",font=("Arial",20,"bold"),fg="black",bg="white").place(x=70,y=320)
et2=Entry(frame,font=("Arial",15,"bold"),show='*',textvariable=var2).place(x=70,y=360,width=280)

bt1=Button(frame,text="login",font=("Arial",18,"bold"),fg="Black",bg="Red",bd=3,command=login).place(x=165,y=420)
lb=Label(a,text="Travel India !",fg="Blue",font=("Arial",18,"bold")).place(x=70,y=10)

a.mainloop()


