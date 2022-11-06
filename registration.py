from tkinter import *
import sqlite3
import tkinter
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar,DateEntry
from PIL import ImageTk, Image
import datetime
import os
a=Tk()
a.title("create account")
a.minsize(1540,1100)
a.iconbitmap("C:\Gui\india.ico.jpg")
Image1=Image.open("india.ico.jpg").resize((1525,800))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=0,y=0)
def create_account():
    try:
        Username=var1.get()
        age=var2.get()
        gen=com1.get()
        dob=cal.get()
        email=var3.get()
        phone=var4.get()
        Password=var5.get()
        if Username=="" or age=="" or gen=="" or dob==" " or email=="" or phone=="" or Password=="":
            messagebox.showwarning("Warning","Please Fill your Details")
        else:
            import sqlite3
            conn = sqlite3.connect('create_account.db')
            a = conn.cursor()
            '''con.execute("CREATE TABLE tour (Username CHAR(25), age INT(3), gen CHAR, dob DATE, email VARCHAR(50), phone INT(10), password CHAR(10))")'''
            a.execute("insert into tour values('{}',{},'{}','{}','{}',{},'{}')".format(Username,int(age),gen,dob,email,int(phone),Password))
            conn.commit()
            messagebox.showwarning("Success","Successfull")
            os._exit(1)
    except Exception as e:
        print(e)
        messagebox.showerror("Error","Please enter Valid information")
label2=Label(a,text="Create Account",font=("Arial",40,"bold italic"),fg="black",bg="yellow")
label2.place(x=650,y=75)
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()

et1=Entry(a,font=("Arial",15,"bold"),textvariable=var1)
et1.insert(0,"Username")
et1.place(x=700,y=200,width=280)
et2=Entry(a,font=("Arial",15,"bold"),textvariable=var2)
et2.insert(0,"Age")
et2.place(x=700,y=270,width=280)
com1=ttk.Combobox(a,values=['Male','Female','Other'],font=("Arial",15,"bold"))
com1.set("Choose Your Gender")
com1.place(x=700,y=340,width=280)
cal=DateEntry(a,width=18,fg="white",bd=2,font=("Arial",15,"bold"))
cal.place(x=700,y=410,width=280)
cal.insert(0," D.O.B :- ")
et3=Entry(a,font=("Arial",15,"bold"),textvariable=var3)
et3.insert(0,"Email")
et3.place(x=700,y=480,width=280)
et4=Entry(a,font=("Arial",15,"bold"),textvariable=var4)
et4.insert(0,"Phone")
et4.place(x=700,y=550,width=280)
et5=Entry(a,font=("Arial",15,"bold"),textvariable=var5,show="*")
et5.insert(0,"Password")
et5.place(x=700,y=620,width=280)

bt1=Button(a,text="Create Account",font=("Arial",18,"bold"),fg="Black",bg="Red",bd=3,command=create_account).place(x=635,y=700)

def main_travel():
    a.destroy()
    import main_travel
bt2=Button(a,text="Next ->",fg="black",bg="red",bd=3,command=main_travel,font=("Arial",18,"bold")).place(x=950,y=700)

a.mainloop()

