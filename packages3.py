from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk,Image

a=Tk()
a.title("Packages3")
a.minsize(1540,1000)
a.config(bg="white")

a.iconbitmap("C:\\Gui\\mahal.ico.jpg")
Image1=Image.open("mahal.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=70,y=30)

def book():
    a.destroy()
    import book

label=Label(a,text="5 Nights / 6 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=70,y=255)
label=Label(a,text="Golden Triangle Tour : Agra, Delhi, Jaipur", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=280)
label=Label(a,text="Delhi(2N) → Agra(1N) → Jaipur(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=380)

label=Label(a,text="₹ 11,000", fg="green",bg="white",font=("Arial",15,"bold")).place(x=290,y=320)
button=Button(a,text="Book Now",fg="blue",command=book,font=("Arial",15,"bold")).place(x=270,y=350)

a.iconbitmap("C:\Gui\sikri.ico.jpg")
Image1=Image.open("sikri.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=450,y=30)

label=Label(a,text="0 Nights / 1 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=450,y=255)
label=Label(a,text="Same Day Agra & Fatehpur Sikri Tour", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=280)
label=Label(a,text="Delhi(0N) -> Agra(0N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=300)
label=Label(a,text="Tour guide in Agra", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=360)

label=Label(a,text="₹ 6,500", fg="green",bg="white",font=("Arial",15,"bold")).place(x=650,y=320)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=640,y=350)

a.iconbitmap("C:\Gui\mathura.ico.jpg")
Image1=Image.open("mathura.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=820,y=30)

label=Label(a,text="6 Nights / 7 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=820,y=255)
label=Label(a,text="Golden Triangle Tour with Mathura", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=280)
label=Label(a,text="Delhi(2N) → Mathura(1N) → Agra(1N) → Jaipur(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=380)

label=Label(a,text="₹ 12,000", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1050,y=320)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1020,y=350)

a.iconbitmap("C:\Gui\mathuravrind.ico.jpg")
Image1=Image.open("mathuravrind.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=1190,y=30)

label=Label(a,text="3 Nights / 4 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=1190,y=255)
label=Label(a,text="Mathura Agra Brajbhoomi Tour", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=280)
label=Label(a,text="Delhi → Mathura(2N) → Vrindavan → Agra(1N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=380)

label=Label(a,text="₹ 10,999", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1400,y=320)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1390,y=350)

a.iconbitmap("C:\Gui\shimla.ico.jpg")
Image1=Image.open("shimla.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=150,y=410)

label=Label(a,text="7 Nights / 8 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=150,y=640)
label=Label(a,text="Agra Family Tour with Shimla Manali", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=660)
label=Label(a,text="Shimla(2N) → Manali(3N) → Delhi(1N) → Agra(1N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=760)

label=Label(a,text="₹ 15,999", fg="green",bg="white",font=("Arial",15,"bold")).place(x=360,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=340,y=740)

a.iconbitmap("C:\Gui\jaipur.ico.jpg")
Image1=Image.open("jaipur.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=600,y=410)

label=Label(a,text="6 Nights / 7 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=600,y=640)
label=Label(a,text="Mesmering North India Tour including Taj Mahal", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=660)
label=Label(a,text="Delhi(1N) → Agra(1N) → Jaipur(3N) → Delhi(1N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=760)

label=Label(a,text="₹ 20,000", fg="green",bg="white",font=("Arial",15,"bold")).place(x=810,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=790,y=740)

a.iconbitmap("C:\Gui\jaipurfort.ico.jpg")
Image1=Image.open("jaipurfort.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=1000,y=410)

label=Label(a,text="6 Nights / 7 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=1000,y=640)
label=Label(a,text="Golden Triangle Tour with Ajmer", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=660)
label=Label(a,text="Delhi(2N) → Agra(1N) → Jaipur(3N) → Ajmer → Delhi", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=760)

label=Label(a,text="₹ 25,450", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1210,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1190,y=740)

a.mainloop()