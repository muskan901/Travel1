from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk,Image

a=Tk()
a.title("Udaipur")
a.minsize(1540,1000)
a.config(bg="white")

label1 = Label(a,text="PLAN YOUR TRIP TO UDAIPUR !",bg="white",fg="red",font=("Arial",18,"bold italic")).place(x=205,y=0,width=1140)

a.iconbitmap("C:\\Gui\\udai.ico.jpg")
Image1=Image.open("udai.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=70,y=100)

label=Label(a,text="Rajasthan . India",bg="white",fg="blue",font=("Arial",15,"bold")).place(x=400,y=115)
label=Label(a,text="2 out of 30",bg="white",fg="black",font=("Arial",15,"bold")).place(x=400,y=160)
label=Label(a,text="Places to visit in Rajasthan",bg="white",fg="blue",font=("Arial",15,"bold")).place(x=513,y=160)
label=Label(a,text="₹ 5,000 ",bg="white",fg="green",font=("Arial",22,"bold")).place(x=400,y=205)
label=Label(a,text="onwards",bg="white",fg="black",font=("Arial",15,"bold")).place(x=500,y=212)
label=Label(a,text="Weather: N.A.",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=115)
label=Label(a,text="Ideal Duration: 2-3 days",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=160)
label=Label(a,text="Best Time: October - March",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=210)
label=Label(a,text="Planning a Trip?",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=260)

def know_more():
    a.destroy()
    import know_more
button=Button(a,text="Know More",bg="white",fg="blue",command=know_more,font=("Arial",15,"bold")).place(x=1220,y=250)

def packages2():
    a.destroy()
    import packages2
button=Button(a,text="View Packages",bg="white",fg="blue",command=packages2,font=("Arial",20,"bold")).place(x=400,y=250)

label=Label(a,text="THE CITY OF LAKES \n"
"Udaipur Tourism\n"
"Udaipur, also known as the City of Lakes, is one of the most visited tourist places in Rajasthan. Located around stunning\n"
"water lakes and enveloped by the Aravalli Hills in all directions, Udaipur is known for its azure lakes, magnificent palaces,\n" 
"vibrant culture and delectable food. Along with being a must-visit destination, it is also one of the best places to \n"
"experience luxury in India.\n"
"Boating through the shimmering Lake Pichola is one of the most beautiful sights and highlights of every Udaipur trip.\n"
"Also known as the VENICE OF THE EAST, Udaipur is inarguably one of the most romantic cities in India.Visit its larger\n"
"than life havelis and monuments, stroll through the bustling street markets, ride through one of the seven lakes of the \n"
"city or relax in one of the extraordinary hotels, and you will discover the charm of Udaipur.Lake Pichola,Jaisamand Lake,\n"
"City Palace, Monsoon Palace, Jagmandir, Fateh Sagar Lake, Jagdish Temple and Saheliyon ki Baari are some of the \n"
"popular tourist places in Udaipur. The city was founded in 1559 by Maharana Udai Singh II as the new capital of the \n"
"Mewar kingdom.The grandeur of the Rajput era is still prevalent in the city's architecture. A trip to Udaipur is often\n"
"combined with a visit to nearby Kumbhalgarh (80km) and Mount Abu."
,bg="white",fg="black",font=("Arial",18,"bold")).place(x=80,y=340,width=1400,height=400)

a.iconbitmap("C:\Gui\hotel.ico.jpg")
Image1=Image.open("hotel.ico.jpg").resize((35,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

button=Button(a,text="Hotels",fg="black",anchor='w',font=("Arial",15,"bold")).place(x=250,y=40,width=130)
label1 = Label(a,image=test,bg="white").place(x=335,y=40,width=40,height=40)

a.iconbitmap("C:\Gui\holiday.ico.jpg")
Image1=Image.open("holiday.ico.jpg").resize((35,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

button=Button(a,text="Places to Visit",fg="black",anchor='w',font=("Arial",15,"bold")).place(x=400,y=40,width=200)
label1 = Label(a,image=test,bg="white").place(x=555,y=40,width=40,height=40)

a.iconbitmap("C:\Gui\do.ico.jpg")
Image1=Image.open("do.ico.jpg").resize((35,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

button=Button(a,text="Things to Do",fg="black",anchor='w',font=("Arial",15,"bold")).place(x=630,y=40,width=200)
label1 = Label(a,image=test,bg="white").place(x=785,y=40,width=40,height=40)

a.iconbitmap("C:\Gui\eat.ico.jpg")
Image1=Image.open("eat.ico.jpg").resize((52,52))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

button=Button(a,text="Restaurants",fg="black",anchor='w',font=("Arial",15,"bold")).place(x=860,y=40,width=200)
label1 = Label(a,image=test,bg="white").place(x=1015,y=40,width=40,height=40)

a.iconbitmap("C:\Gui\logo.ico.jpg")
Image1=Image.open("logo.ico.jpg").resize((35,35))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test

button=Button(a,text="Travel Forums",fg="black",anchor='w',font=("Arial",15,"bold")).place(x=1090,y=40,width=200)
label1 = Label(a,image=test,bg="white").place(x=1245,y=40,width=40,height=40)

a.mainloop()