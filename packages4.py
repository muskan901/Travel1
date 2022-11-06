from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk,Image

a=Tk()
a.title("Packages4")
a.minsize(1540,1000)
a.config(bg="white")

a.iconbitmap("C:\Gui\gangtok.ico.jpg")
Image1=Image.open("gangtok.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=70,y=30)

def book():
    a.destroy()
    import book

label=Label(a,text="3 Nights / 4 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=70,y=255)
label=Label(a,text="3 Nights in Darjeeling ", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=280)
label=Label(a,text="Darjeeling(3N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=380)

label=Label(a,text="₹ 15,750", fg="green",bg="white",font=("Arial",15,"bold")).place(x=290,y=320)
button=Button(a,text="Book Now",fg="blue",command=book,font=("Arial",15,"bold")).place(x=270,y=350)

a.iconbitmap("C:\Gui\gangdar.ico.jpg")
Image1=Image.open("gangdar.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=450,y=30)

label=Label(a,text="4 Nights / 5 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=450,y=255)
label=Label(a,text="4 Nights in Gangtok Darjeeling", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=280)
label=Label(a,text="Gangtok(2N) → Darjeeling(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=380)

label=Label(a,text="₹ 13,800", fg="green",bg="white",font=("Arial",15,"bold")).place(x=650,y=320)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=640,y=350)

a.iconbitmap("C:\Gui\kalimpong.ico.jpg")
Image1=Image.open("kalimpong.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=820,y=30)

label=Label(a,text="3 Nights / 4 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=820,y=255)
label=Label(a,text="Kalimpong Darjeeling Delight Tour", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=280)
label=Label(a,text="Kalimpong(1N) → Darjeeling(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=380)

label=Label(a,text="₹ 9,500", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1050,y=320)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1020,y=350)

a.iconbitmap("C:\Gui\siliguri.ico.jpg")
Image1=Image.open("siliguri.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=1190,y=30)

label=Label(a,text="4 Nights / 5 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=1190,y=255)
label=Label(a,text="Himalayan Grandeur Gangtok Darjeeling ", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=280)
label=Label(a,text="Siliguri(0N) → Darjeeling(2N) → Gangtok(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=380)

label=Label(a,text="₹ 18,400", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1400,y=320)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1390,y=350)

a.iconbitmap("C:\Gui\dargang.ico.jpg")
Image1=Image.open("dargang.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=130,y=410)

label=Label(a,text="5 Nights / 6 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=130,y=640)
label=Label(a,text="Himalayan Golden Triangle", fg="black",bg="white",font=("Arial",11,"bold")).place(x=130,y=660)
label=Label(a,text="Siliguri → Gangtok(2N) → Kalimpong(1N) → Darjeeling(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=130,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=130,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=130,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=130,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=130,y=760)

label=Label(a,text="₹ 15,691", fg="green",bg="white",font=("Arial",15,"bold")).place(x=340,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=320,y=740)

a.iconbitmap("C:\Gui\pelling.ico.jpg")
Image1=Image.open("pelling.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=600,y=410)

label=Label(a,text="4 Nights / 5 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=600,y=640)
label=Label(a,text="Explore the Mystical Darjelling and Pelling", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=660)
label=Label(a,text="Darjeeling(2N) → Pelling(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=760)

label=Label(a,text="₹ 16,050", fg="green",bg="white",font=("Arial",15,"bold")).place(x=810,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=790,y=740)

a.iconbitmap("C:\Gui\lachung.ico.jpg")
Image1=Image.open("lachung.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=1000,y=410)

label=Label(a,text="6 Nights / 7 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=1000,y=640)
label=Label(a,text="Mesmerizing Darjeeling, Gangtok, and Lachung", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=660)
label=Label(a,text="Darjeeling (2N) → Gangtok (1N) → Lachung (2N) → Gangtok (1N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1000,y=760)

label=Label(a,text="₹ 24,726", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1210,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1190,y=740)

a.mainloop()