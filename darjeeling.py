from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk,Image

a=Tk()
a.title("Darjeeling")
a.minsize(1540,1000)
a.config(bg="white")

label1 = Label(a,text="PLAN YOUR TRIP TO DARJEELING !",bg="white",fg="red",font=("Arial",18,"bold italic")).place(x=205,y=0,width=1140)

a.iconbitmap("C:\Gui\darjeeling.ico.jpg")
Image1=Image.open("darjeeling.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=70,y=100)

label=Label(a,text="West Bengal . India",bg="white",fg="blue",font=("Arial",15,"bold")).place(x=400,y=115)
label=Label(a,text="2 out of 38",bg="white",fg="black",font=("Arial",15,"bold")).place(x=400,y=160)
label=Label(a,text="Places to visit in West Bengal",bg="white",fg="blue",font=("Arial",15,"bold")).place(x=513,y=160)
label=Label(a,text="₹ 6,550 ",bg="white",fg="green",font=("Arial",22,"bold")).place(x=400,y=205)
label=Label(a,text="onwards",bg="white",fg="black",font=("Arial",15,"bold")).place(x=500,y=212)
label=Label(a,text="Weather: N.A.",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=115)
label=Label(a,text="Ideal Duration: 2-3 days",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=160)
label=Label(a,text="Best Time: February - March, \n September - December",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=210)
label=Label(a,text="Planning a Trip?",bg="white",fg="magenta",font=("Arial",15,"bold")).place(x=1050,y=280)

def know_more():
    a.destroy()
    import know_more
button=Button(a,text="Know More",bg="white",fg="blue",command=know_more,font=("Arial",15,"bold")).place(x=1220,y=275)

def packages4():
    a.destroy()
    import packages4
button=Button(a,text="View Packages",bg="white",fg="blue",command=packages4,font=("Arial",20,"bold")).place(x=400,y=250)

label=Label(a,text="QUEEN OF THE HIMALAYAS  \n"
"Darjeeling Tourism\n"
"The previous summer capital of India under the British Raj, Darjeeling has come off age as one of the most sought \n"
"after hill stations in India. Located in West Bengal, this scenic hill station is the perfect getaway for a romantic\n"
"honeymoon.\n"
"The toy train established back in 1881 is conferred the title of World Heritage Status by UNESCO. The train begins \n"
"its journey from the plains and rises to over 2000 metres above sea level, offering breathtaking views of the \n"
"mountains as it chugs along.Over 86 tea estates in Darjeeling are responsible for producing the worldwide famous \n"
"'Darjeeling Tea'. Have a cup of locally brewed chai at the tea estate, or get down amidst the plantations to pluck \n"
"a few tea leaves yourself; you are free to take your pick!\n"
"The third highest peak in the world and the highest in India, the Kanchenjunga peak, is visible from here, and you \n"
"can enjoy a panoramic view of the peak. Some of Darjeeling's most popular attractions include monasteries, \n"
"botanical gardens, a zoo, and the Darjeeling-Rangeet Valley Passenger Ropeway cable car, which is the longest Asian\n"
"cable car. Tiger Hill is a fantastic spot to see the sunrise over the mountains in all its fiery glory. "
,bg="white",fg="black",font=("Arial",18,"bold")).place(x=80,y=340,width=1400,height=450)

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