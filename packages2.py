from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk,Image

a=Tk()
a.title("Packages2")
a.minsize(1540,1000)
a.config(bg="white")

a.iconbitmap("C:\\Gui\\udaipur.ico.jpg")
Image1=Image.open("udaipur.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=70,y=30)

def book():
    a.destroy()
    import book

label=Label(a,text="3 Nights / 4 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=70,y=255)
label=Label(a,text="Best of Udaipur 3 Nights & 4 Days Tour", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=280)
label=Label(a,text="Udaipur(3N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=380)

label=Label(a,text="₹ 14,800", fg="green",bg="white",font=("Arial",18,"bold")).place(x=290,y=310)
button=Button(a,text="Book Now",fg="blue",command=book,font=("Arial",15,"bold")).place(x=270,y=350)

a.iconbitmap("C:\Gui\jodhpur.ico.jpg")
Image1=Image.open("jodhpur.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=450,y=30)

label=Label(a,text="5 Nights / 6 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=450,y=255)
label=Label(a,text="Pearls of Rajasthan-Jaipur,Jodhpur & Udaipur", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=280)
label=Label(a,text="Jaipur(2N) -> Jodhpur(1N) -> Udaipur(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=380)

label=Label(a,text="₹ 18,999", fg="green",bg="white",font=("Arial",15,"bold")).place(x=650,y=320)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=640,y=350)

a.iconbitmap("C:\Gui\waterpark.ico.jpg")
Image1=Image.open("waterpark.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=820,y=30)

label=Label(a,text="4 Nights / 5 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=820,y=255)
label=Label(a,text="Magnificent Udaipur with Marvel Waterpark Trip", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=280)
label=Label(a,text="Udaipur(4N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=380)

label=Label(a,text="₹ 12,999", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1050,y=320)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1020,y=350)

a.iconbitmap("C:\Gui\mount.ico.jpg")
Image1=Image.open("mount.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=1190,y=30)

label=Label(a,text="3 Nights / 4 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=1190,y=255)
label=Label(a,text="Idyllic Udaipur Mount Abu", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=280)
label=Label(a,text="Udaipur(2N) -> Mount Abu(1N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=380)

label=Label(a,text="₹ 14,000", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1400,y=320)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1390,y=350)

a.iconbitmap("C:\Gui\pushkar.ico.jpg")
Image1=Image.open("pushkar.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=150,y=410)

label=Label(a,text="4 Nights / 5 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=150,y=640)
label=Label(a,text="Rangeelo Rajasthan Holiday for 4 Nights", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=660)
label=Label(a,text="Jaipur(2N) -> Udaipur(2N) -> Pushkar(0N) -> Ajmer(0N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=760)

label=Label(a,text="₹ 17,700", fg="green",bg="white",font=("Arial",15,"bold")).place(x=360,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=340,y=740)

a.iconbitmap("C:\Gui\chittorgarh.ico.jpg")
Image1=Image.open("chittorgarh.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=600,y=410)

label=Label(a,text="2 Nights / 3 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=600,y=640)
label=Label(a,text="Udaipur & Chittorgarh Fort", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=660)
label=Label(a,text="Udaipur(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=760)

label=Label(a,text="₹ 7,200", fg="green",bg="white",font=("Arial",15,"bold")).place(x=810,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=790,y=740)

a.iconbitmap("C:\Gui\jaisalmer.ico.jpg")
Image1=Image.open("jaisalmer.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=1000,y=410)

label=Label(a,text="5 Nights / 6 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=1000,y=640)
label=Label(a,text="Rajasthan Golden Triangle Tour", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=660)
label=Label(a,text="Jodhpur(0N) -> Jaisalmer(2N) -> Jodhpur(1N) -> Udaipur(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=760)

label=Label(a,text="₹ 16,560", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1210,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1190,y=740)

a.mainloop()