from tkinter import *
from tkinter import ttk
import webbrowser as wb
from PIL import ImageTk,Image
import tkinter

a=Tk()
a.title("Know More")
a.config(bg="white")
a.minsize(1540,1100)

label=Label(a,text="The World is a book, and those who do not travel read only a page",bg="White",fg="Blue",font=("Arial",28,"bold italic")).place(x=180,y=0)

def search():
    x=var.get()
    wb.open(x)
var=StringVar()
et=Entry(a,fg="black",font=("Arial",15),borderwidth = 10,textvariable=var)
et.insert(1,"Type your question here")
et.place(x=240,y=70,width=1000)

a.iconbitmap("C:\Gui\search.ico.jpg")
Image1=Image.open("search.ico.jpg").resize((60,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

searchButton=Button(a,image = test,command=search,bd=2).place(x=1230,y=70,width=60)

label=Label(a,text="FAQs",fg="red",bg="white",font=("Arial",20,"bold underline")).place(x=70,y=130)
label=Label(a,text="How are you different from others?",fg="black",bg="white",font=("Times",20)).place(x=70,y=170)
label=Label(a,text="No Pre-Packaged Tours -",fg="black",bg="white",font=("Arial",17,"bold")).place(x=70,y=210)
label=Label(a,text="We provide platform to let travellers build, customize and edit their travel plan on the basis of their interests.",fg="black",bg="white",font=("Times",18)).place(x=350,y=210)
label=Label(a,text="Promote Indian culture -",fg="black",bg="white",font=("Arial",17,"bold")).place(x=70,y=245)
label=Label(a,text="The people abroad have a very different impression of Indian culture, they are not aware of so many good aspects which\n"
"make India the country it is today.We are not promoting tourism, we want you face-to face with your dream theme of\n"
"India's vast culture and heritage.We will provide tourist guide to travellers so that they can experience new things. ",fg="black",bg="white",font=("Times",18)).place(x=350,y=245)
label=Label(a,text="You long much more and we are there to get along !",fg="black",bg="white",font=("Arial",20,"bold")).place(x=450,y=335)
label=Label(a,text="Changes -",fg="black",bg="white",font=("Arial",17,"bold")).place(x=70,y=380)
label=Label(a,text="We provide real time chat support - we will be there for you throughout your vacation. Want to upgrade your room,plan a surprise \n"
"or change plans? Ping us and we will help you out!",fg="black",bg="white",font=("Times",18)).place(x=200,y=380)
label=Label(a,text="Exhaustive, Reliable Content -",fg="black",bg="white",font=("Arial",17,"bold")).place(x=70,y=440)
label=Label(a,text="Our travel guides are editorially curated, so you can trust that they will lead you to the right path.",fg="black",bg="white",font=("Times",18)).place(x=415,y=440)
label=Label(a,text="Travel planning has always been messy and difficult",fg="green",bg="white",font=("Arial",22,"bold")).place(x=400,y=510)
label=Label(a,text="Planning every single trip needs answers to a number of questions. We are attempting to collect all the information \n"
"that you will ever need to plan your trip - from when, where and how, to more hidden gems in every destination, it is the \n"
"one-stop solution to all your travel planning needs.",fg="black",bg="white",font=("Times",20)).place(x=100,y=550)
a.mainloop()