from tkinter import *
from tkinter import ttk
import webbrowser as wb
from PIL import ImageTk,Image
import tkinter

a=Tk()
a.title("Help")
a.config(bg="white")
a.minsize(1540,1100)

label=Label(a,text="How can we help?",bg="White",fg="Blue",font=("Arial",28,"bold italic")).place(x=580,y=0)

def search():
    x=var.get()
    wb.open(x)
var=StringVar()
et=Entry(a,fg="black",font=("Arial",15),borderwidth = 10,textvariable=var)
et.insert(1,"Search help topics")
et.place(x=240,y=70,width=1000)

a.iconbitmap("C:\Gui\search.ico.jpg")
Image1=Image.open("search.ico.jpg").resize((60,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

searchButton=Button(a,image = test,command=search,bd=2).place(x=1230,y=70,width=60)

label=Label(a,text="Help",fg="black",bg="white",font=("Arial",20,"bold")).place(x=60,y=140)
label=Label(a,text="If you have questions about tour or need help making your booking, we'd be happy to help. Just call the number below",fg="black",bg="white",font=("Arial",18,"bold")).place(x=60,y=180)
label=Label(a,text="XXXXXXXXXX",fg="blue",bg="white",font=("Arial",18,"bold underline")).place(x=60,y=225)

label=Label(a,text="A journey of a thousand miles begins with a single step.",fg="green",bg="white",font=("Arial",20,"bold italic")).place(x=390,y=300)
def main_travel():
    a.destroy()
    import main_travel

button=Button(a,text="Start Now",fg="black",bg="green",command=main_travel,font=("Arial",18,"bold")).place(x=690,y=370)

label=Label(a,text="Talk to us",fg="grey",bg="white",font=("Arial",20,"bold underline")).place(x=520,y=480)
label=Label(a,text="Planning a Trip?",fg="black",bg="white",font=("Arial",18)).place(x=500,y=530)

a.iconbitmap("C:\Gui\mail.ico.jpg")
Image1=Image.open("mail.ico.jpg").resize((40,40))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=450,y=560)

a.iconbitmap("C:\Gui\phone.ico.jpg")
Image1=Image.open("phone.ico.jpg").resize((40,40))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=450,y=600)

a.iconbitmap("C:\Gui\wa.ico.jpg")
Image1=Image.open("wa.ico.jpg").resize((40,40))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=450,y=640)

label=Label(a,text="Social",fg="grey",bg="white",font=("Arial",20,"bold underline")).place(x=900,y=480)

a.iconbitmap("C:\Gui\iconfb.ico.jpg")
Image1=Image.open("iconfb.ico.jpg").resize((40,40))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=850,y=540)

a.iconbitmap("C:\Gui\icontw.ico.jpg")
Image1=Image.open("icontw.ico.jpg").resize((40,40))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=850,y=590)

a.iconbitmap("C:\Gui\insta.ico.jpg")
Image1=Image.open("insta.ico.jpg").resize((35,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=850,y=640)



a.mainloop()