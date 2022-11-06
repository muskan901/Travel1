from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk,Image

a=Tk()
a.title("Packages")
a.minsize(1540,1000)
a.config(bg="white")

a.iconbitmap("C:\Gui\india.ico.jpg")
Image1=Image.open("india.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=70,y=30)

def book():
    a.destroy()
    import book

label=Label(a,text="2 Nights / 3 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=70,y=255)
label=Label(a,text="Varanasi Holy Ganges Tour with Ganga Aarti", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=280)
label=Label(a,text="Varanasi(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=70,y=380)

label=Label(a,text="₹ 6,100", fg="green",bg="white",font=("Arial",18,"bold")).place(x=290,y=310)
button=Button(a,text="Book Now",fg="blue",command=book,font=("Arial",15,"bold")).place(x=270,y=350)

a.iconbitmap("C:\Gui\kashi.ico.jpg")
Image1=Image.open("kashi.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=450,y=30)

label=Label(a,text="3 Nights / 4 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=450,y=255)
label=Label(a,text="Kashi Yatra Tour (Day trip to Allahabad)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=280)
label=Label(a,text="Varanasi(3N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=450,y=380)

label=Label(a,text="₹ 13,500", fg="green",bg="white",font=("Arial",18,"bold")).place(x=650,y=310)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=640,y=350)

a.iconbitmap("C:\Gui\gaya.ico.jpg")
Image1=Image.open("gaya.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=820,y=30)

label=Label(a,text="4 Nights / 5 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=820,y=255)
label=Label(a,text="Varanasi, Bodh Gaya, Allahabad", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=280)
label=Label(a,text="Varanasi(2N) -> Gaya(1N) -> Allahabad(1N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=820,y=380)

label=Label(a,text="₹ 12,800", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1050,y=320)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1020,y=350)

a.iconbitmap("C:\Gui\lucknow.ico.jpg")
Image1=Image.open("lucknow.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=1190,y=30)

label=Label(a,text="6 Nights / 7 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=1190,y=255)
label=Label(a,text="Kashi, Chitrakoot, Lucknow & More", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=280)
label=Label(a,text="Varanasi(2N) -> Allahabad(2N) -> Lucknow(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=300)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=320)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=340)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=360)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1190,y=380)

label=Label(a,text="₹ 20,000", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1400,y=320)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1390,y=350)

a.iconbitmap("C:\Gui\gayabodh.ico.jpg")
Image1=Image.open("gayabodh.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=150,y=410)

label=Label(a,text="4 Nights / 5 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=150,y=640)
label=Label(a,text="Varanasi & Bodh Gaya Tour", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=660)
label=Label(a,text="Varanasi(1N) -> Bodh Gaya(1N) -> Varanasi(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=150,y=760)

label=Label(a,text="₹ 14,000", fg="green",bg="white",font=("Arial",15,"bold")).place(x=360,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=340,y=740)

a.iconbitmap("C:\Gui\city.ico.jpg")
Image1=Image.open("city.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=600,y=410)

label=Label(a,text="5 Nights / 6 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=600,y=640)
label=Label(a,text="Holy Trail including Ayodhya & Varanasi", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=660)
label=Label(a,text="Varanasi(2N) -> Allahabad(1N) -> Ayodhya(1N) -> Varanasi(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=600,y=760)

label=Label(a,text="₹ 17,500", fg="green",bg="white",font=("Arial",15,"bold")).place(x=810,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=790,y=740)

a.iconbitmap("C:\Gui\jaipur.ico.jpg")
Image1=Image.open("jaipur.ico.jpg").resize((300,220))
test=ImageTk.PhotoImage(Image1)
label1=tkinter.Label(image=test)
label1.image=test
label1.place(x=1100,y=410)

label=Label(a,text="6 Nights / 7 Days",fg="red",bg="white",font=("Arial",13,"bold")).place(x=1100,y=640)
label=Label(a,text="Delhi-Agra-Jaipur-Varanasi", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1100,y=660)
label=Label(a,text="Delhi(1N) -> Jaipur(1N) -> Agra(2N) -> Varanasi(2N)", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1100,y=680)
label=Label(a,text="Breakfast", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1100,y=700)
label=Label(a,text="Sightseeing", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1100,y=720)
label=Label(a,text="Private cab with driver", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1100,y=740)
label=Label(a,text="Twin-sharing rooms", fg="black",bg="white",font=("Arial",11,"bold")).place(x=1100,y=760)

label=Label(a,text="₹ 16,000", fg="green",bg="white",font=("Arial",15,"bold")).place(x=1310,y=710)
button=Button(a,text="Book Now",command=book,fg="blue",font=("Arial",15,"bold")).place(x=1290,y=740)


a.mainloop()