from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk,Image

a=Tk()
a.title("Varanasi")
a.minsize(1540,1000)
a.config(bg="white")

label1 = Label(a,text="PLAN YOUR TRIP TO VARANASI !",bg="white",fg="red",font=("Arial",18,"bold italic")).place(x=205,y=0,width=1140)

a.iconbitmap("C:\Gui\kash.ico.jpg")
Image1=Image.open("kash.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=70,y=100)

label=Label(a,text="Uttar Pradesh . India",bg="white",fg="blue",font=("Arial",15,"bold")).place(x=400,y=115)
label=Label(a,text="2 out of 27",bg="white",fg="black",font=("Arial",15,"bold")).place(x=400,y=160)
label=Label(a,text="Places to visit in Uttar Pradesh",bg="white",fg="blue",font=("Arial",15,"bold")).place(x=513,y=160)
label=Label(a,text="₹ 5,877 ",bg="white",fg="green",font=("Arial",22,"bold")).place(x=400,y=205)
label=Label(a,text="onwards",bg="white",fg="black",font=("Arial",15,"bold")).place(x=500,y=212)
label=Label(a,text="Weather: N.A.",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=115)
label=Label(a,text="Ideal Duration: 2-3 days",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=160)
label=Label(a,text="Best Time: October - March",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=210)
label=Label(a,text="Planning a Trip?",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=260)

def packages():
    a.destroy()
    import packages

def know_more():
    a.destroy()
    import know_more

button=Button(a,text="Know More",bg="white",fg="blue",command=know_more,font=("Arial",15,"bold")).place(x=1220,y=250)
button=Button(a,text="View Packages",bg="white",fg="blue",command=packages,font=("Arial",20,"bold")).place(x=400,y=250)

label=Label(a,text="THE SPIRITUAL CAPITAL OF INDIA \n "
"Varanasi Tourism \n "
"World's oldest living city, Varanasi - also known as Kashi (City of Life) and Banaras, is the spiritual capital of India. It  is\n "
"one of Hinduism's seven holy cities. The old city of Varanasi lies along the western banks of the Ganges, spread across a \n "
"labyrinth of narrow galis. Be prepared to walk on foot and encounter some holy cows! Temples at almost every turn \n  "
"engulf Varanasi but the Kashi Vishwanath Temple is the most visited and the oldest of the lot. Benaras is known as the \n "
"city of Lord Shiva for a reason, and rightfully so. Varanasi is considered an auspicious place to die, as it is believed to \n "
"grant moksha or liberation from the cycle of life and death. Spiritually enlightening, the heart of the city pulsates around \n "
"the ghats, about 80 of which border the Ganges. Be prepared for the sights, sounds and smells! \n "
"Don't miss out on the hot chaat and cool lassi.\n  "
"Though, all chaos and noise on the ghats take a pause before dusk when the Ganga Aarti begins to take place, \n "
"a ceremony of immense grandeur. This divine city is also an important destination for Buddhists."
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