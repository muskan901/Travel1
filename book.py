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
a.title("Booking")
a.minsize(1520,900)
a.iconbitmap("C:\Gui\indiabook.ico.jpg")
Image1=Image.open("indiabook.ico.jpg").resize((1530,910))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=0,y=-115)
def booking():
    try:
        Username=var1.get()
        phone=var2.get()
        email=var3.get()
        traveldate=cal.get()
        nights=var4.get()
        travelers=var5.get()
        if Username=="" or phone=="" or email=="" or traveldate==" " or nights=="" or phone=="" or travelers=="":
            messagebox.showwarning("Warning","Please Fill your Details")
        else:
            import sqlite3
            conn = sqlite3.connect('booking.db')
            a = conn.cursor()
            '''con.execute("CREATE TABLE book (Username CHAR(25), phone INT(10), email VARCHAR(50), traveldate DATE,nights INT(10), travelers INT(10))")'''
            a.execute("insert into book values('{}',{},'{}','{}',{},{})".format(Username,int(phone),email,traveldate,int(nights),int(travelers)))
            conn.commit()
            messagebox.showwarning("Success","Successfull")
            os._exit(1)
    except Exception as e:
        print(e)
        messagebox.showerror("Error","Please enter Valid information")
label2=Label(a,text="Booking",font=("Arial",40,"bold italic"),fg="black",bg="yellow")
label2.place(x=650,y=75)
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()

et1=Entry(a,font=("Arial",15,"bold"),textvariable=var1)
et1.insert(0,"Username")
et1.place(x=650,y=200,width=280)
et2=Entry(a,font=("Arial",15,"bold"),textvariable=var2)
et2.insert(0,"Phone")
et2.place(x=650,y=270,width=280)
et3=Entry(a,font=("Arial",15,"bold"),textvariable=var3)
et3.insert(0,"Email")
et3.place(x=650,y=340,width=280)
cal=DateEntry(a,width=18,fg="white",bd=2,font=("Arial",15,"bold"))
cal.place(x=650,y=410,width=280)
cal.insert(0," TravelDate :- ")
et4=Entry(a,font=("Arial",15,"bold"),textvariable=var4)
et4.insert(0,"Nights")
et4.place(x=650,y=480,width=280)
et5=Entry(a,font=("Arial",15,"bold"),textvariable=var5)
et5.insert(0,"Travelers")
et5.place(x=650,y=550,width=280)

bt1=Button(a,text="Book",font=("Arial",18,"bold"),fg="Black",bg="Red",bd=3,command=booking).place(x=730,y=600)
bt2=Button(a,text="Get Call",font=("Arial",18,"bold"),fg="black",bg="red",bd=3).place(x=720,y=680)

a.mainloop()

