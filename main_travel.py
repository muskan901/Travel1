from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk,Image
import sqlite3
import webbrowser as wb

a=Tk()
a.title("Main")
a.minsize(1540,1000)
a.config(bg="white")

label=Label(a,text="The world is now open, are you?",bg="red",fg="black",font=("Arial",22,"bold italic")).place(x=200,y=0,width=1350)

a.iconbitmap("C:\Gui\main.ico.jpg")
Image1=Image.open("main.ico.jpg").resize((1200,350))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test,bg="white")
label1.image=test
label1.place(x=250,y=105)

frame=Frame(bg="black")
frame.place(x=0,y=0,width=200,height=800)

a.iconbitmap("C:\Gui\marks.ico.jpg")
Image1=Image.open("marks.ico.jpg").resize((40,40))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

reviewButton = Button(frame,image=test).place(x=20,y=60,width=40,height=40)

label=Label(frame,text="Reviews",fg="white",bg="black",font=("Arial",15,"bold")).place(x=75,y=65)

a.iconbitmap("C:\Gui\liked.ico.jpg")
Image1=Image.open("liked.ico.jpg").resize((35,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

reviewButton = Button(frame,image=test).place(x=20,y=140,width=40,height=40)

label=Label(frame,text="Trips",fg="white",bg="black",font=("Arial",15,"bold")).place(x=75,y=145)

a.iconbitmap("C:\Gui\downloads.ico.jpg")
Image1=Image.open("downloads.ico.jpg").resize((40,40))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

alertsButton = Button(frame,image=test).place(x=20,y=220,width=40,height=40)

label=Label(frame,text="Alerts",fg="white",bg="black",font=("Arial",15,"bold")).place(x=75,y=225)

a.iconbitmap("C:\Gui\shop.ico.jpg")
Image1=Image.open("shop.ico.jpg").resize((50,50))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

basketButton = Button(frame,image=test).place(x=20,y=300,width=40,height=40)

label=Label(frame,text="Basket",fg="white",bg="black",font=("Arial",15,"bold")).place(x=75,y=305)

a.iconbitmap("C:\Gui\guide.ico.jpg")
Image1=Image.open("guide.ico.jpg").resize((40,40))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

guideButton = Button(frame,image=test,bg="white").place(x=20,y=380,width=40,height=40)

label=Label(frame,text="Guide",fg="white",bg="black",font=("Arial",15,"bold")).place(x=75,y=385)

a.iconbitmap("C:\Gui\help.ico.jpg")
Image1=Image.open("help.ico.jpg").resize((35,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

def help():
    a.destroy()
    import help

helpButton = Button(frame,image=test,bg="white",command=help).place(x=20,y=460,width=40,height=40)

label=Label(frame,text="Help",fg="white",bg="black",font=("Arial",15,"bold")).place(x=75,y=465)

a.iconbitmap("C:\Gui\hotel.ico.jpg")
Image1=Image.open("hotel.ico.jpg").resize((35,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

button=Button(a,text="Hotels",fg="black",anchor='w',font=("Arial",15,"bold")).place(x=250,y=50,width=130)
label1 = Label(a,image=test,bg="white").place(x=335,y=50,width=40,height=40)

a.iconbitmap("C:\Gui\holiday.ico.jpg")
Image1=Image.open("holiday.ico.jpg").resize((35,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

button=Button(a,text="Holiday Homes",fg="black",anchor='w',font=("Arial",15,"bold")).place(x=400,y=50,width=200)
label1 = Label(a,image=test,bg="white").place(x=555,y=50,width=40,height=40)

a.iconbitmap("C:\Gui\do.ico.jpg")
Image1=Image.open("do.ico.jpg").resize((35,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

button=Button(a,text="Things to Do",fg="black",anchor='w',font=("Arial",15,"bold")).place(x=630,y=50,width=200)
label1 = Label(a,image=test,bg="white").place(x=785,y=50,width=40,height=40)

a.iconbitmap("C:\Gui\eat.ico.jpg")
Image1=Image.open("eat.ico.jpg").resize((52,52))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

button=Button(a,text="Restaurants",fg="black",anchor='w',font=("Arial",15,"bold")).place(x=860,y=50,width=200)
label1 = Label(a,image=test,bg="white").place(x=1015,y=50,width=40,height=40)

a.iconbitmap("C:\Gui\logo.ico.jpg")
Image1=Image.open("logo.ico.jpg").resize((35,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

button=Button(a,text="Travel Forums",fg="black",anchor='w',font=("Arial",15,"bold")).place(x=1090,y=50,width=200)
label1 = Label(a,image=test,bg="white").place(x=1245,y=50,width=40,height=40)

a.iconbitmap("C:\Gui\more.ico.jpg")
Image1=Image.open("more.ico.jpg").resize((45,45))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

def main():
    a.destroy()
    import know_more
label=Label(a,text="More",fg="black",anchor='w',bd=2,font=("Arial",15,"bold")).place(x=1330,y=50,width=120,height=42)
button = Button(a,command=main,image=test,bg="white").place(x=1410,y=50,width=40,height=40)

def search():
    x=var.get()
    wb.open(x)
var=StringVar()
et=Entry(a,fg="black",font=("Arial",15,"italic"),borderwidth = 10,textvariable=var)
et.insert(1,"Start Planning .....")
et.place(x=330,y=200,width=1000)

a.iconbitmap("C:\Gui\search.ico.jpg")
Image1=Image.open("search.ico.jpg").resize((60,40))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

searchButton=Button(a,image = test,command=search,bd=2).place(x=1300,y=200,width=60)

a.iconbitmap("C:\Gui\kashi.ico.jpg")
Image1=Image.open("kashi.ico.jpg").resize((250,200))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

def varanasi():
    a.destroy()
    import varanasi

kashiButton=Button(a,image = test,bd=2,command=varanasi).place(x=280,y=480,width=250)
label=Label(a,text="Feel the real Varanasi \n vibe with unforgettable, \n hand-picked tour and activities",fg="black",font=("Arial",14,"bold")).place(x=250,y=700,width=305,height=70)

a.iconbitmap("C:\\Gui\\udaipur.ico.jpg")
Image1=Image.open("udaipur.ico.jpg").resize((250,200))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

def udaipur():
    a.destroy()
    import udaipur
udaipurButton=Button(a,image = test,bd=2,command=udaipur).place(x=580,y=480,width=250)
label=Label(a,text="Breathe in Udaipur, and \n you'll never want to leave ",fg="black",font=("Arial",14,"bold")).place(x=580,y=700,width=255,height=70)

a.iconbitmap("C:\Gui\mahal.ico.jpg")
Image1=Image.open("mahal.ico.jpg").resize((250,200))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

def agra():
    a.destroy()
    import agra
mahalButton=Button(a,image = test,bd=2,command=agra).place(x=880,y=480,width=250)
label=Label(a,text="Better to see something \n once than to hear about it \n a thousand times",fg="black",font=("Arial",14,"bold")).place(x=880,y=700,width=255,height=70)

a.iconbitmap("C:\Gui\gangtok.ico.jpg")
Image1=Image.open("gangtok.ico.jpg").resize((250,200))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

def darjeeling():
    a.destroy()
    import darjeeling

darjeelingButton=Button(a,image = test,bd=2,command=darjeeling).place(x=1180,y=480,width=250)
label=Label(a,text="There is so much to \n discover in Darjeeling!",fg="black",font=("Arial",14,"bold")).place(x=1180,y=700,width=255,height=70)

a.mainloop()