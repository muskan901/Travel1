from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk,Image

a=Tk()
a.title("Agra")
a.minsize(1540,1000)
a.config(bg="white")

label1 = Label(a,text="PLAN YOUR TRIP TO AGRA !",bg="white",fg="red",font=("Arial",18,"bold italic")).place(x=205,y=0,width=1140)

a.iconbitmap("C:\\Gui\\mahaltaj.ico.jpg")
Image1=Image.open("mahaltaj.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=70,y=100)

label=Label(a,text="Uttar Pradesh . India",bg="white",fg="blue",font=("Arial",15,"bold")).place(x=400,y=115)
label=Label(a,text="1 out of 27",bg="white",fg="black",font=("Arial",15,"bold")).place(x=400,y=160)
label=Label(a,text="Places to visit in Uttar Pradesh",bg="white",fg="blue",font=("Arial",15,"bold")).place(x=513,y=160)
label=Label(a,text="₹ 2,300 ",bg="white",fg="green",font=("Arial",22,"bold")).place(x=400,y=205)
label=Label(a,text="onwards",bg="white",fg="black",font=("Arial",15,"bold")).place(x=500,y=212)
label=Label(a,text="Weather: N.A.",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=115)
label=Label(a,text="Ideal Duration: 1-2 days",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=160)
label=Label(a,text="Best Time: October - March",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=210)
label=Label(a,text="Planning a Trip?",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=260)

def know_more():
    a.destroy()
    import know_more
button=Button(a,text="Know More",bg="white",fg="blue",command=know_more,font=("Arial",15,"bold")).place(x=1220,y=250)

def packages3():
    a.destroy()
    import packages3
button=Button(a,text="View Packages",bg="white",fg="blue",command=packages3,font=("Arial",20,"bold")).place(x=400,y=250)

label=Label(a,text="THE CITY OF TAJ MAHAL, THE MONUMENT OF ETERNAL LOVE  \n"
"Agra Tourism\n"
"Located on the banks of River Yamuna in Uttar Pradesh, Agra is a popular tourist destination as it is home to one \n"
"of the 7 wonders of the world, the Taj Mahal. It is a sneak peek into the architectural history and legacy of \n"
"the Mughal empire with two other UNESCO World Heritage Sites Agra Fort and Fatehpur Sikri. History, architecture, \n"
"romance all together create the magic of Agra, and hence, makes for a must-visit for anyone living in or visiting \n"
"India.Agra is one of the most populous cities in Uttar Pradesh and 24th most populous city in India. With its long\n"
"and rich history, it is no wonder that Agra forms part of the popular Golden Triangle Circuit for tourists along \n"
"with Delhi and Jaipur. It is also a part of the Uttar Pradesh Heritage Arc including Varanasi and Lucknow. \n"
"Apart from its monuments, Agra has some exciting stuff for foodies. It is as famous for its Petha (a sweet made \n"
"from pumpkin and flavoured with rose water and saffron) as it is for the Taj Mahal. Agra is also well known for \n"
"its marble artefacts which are best bought in the Sadar Bazaar or Kinaari Bazaar area. \n"
"Agra is mostly visited on a one-day trip from New Delhi or other nearby cities in Uttar Pradesh but is totally worth \n"
"it. Be prepared to be astounded, amazed, inspired and thrilled."
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