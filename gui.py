#tkinter
#import tkinter
#import tkinter as tk
from tkinter import *
import random
#tworzy glowne okno
window = Tk()
#zmiana tytulu okna
window.title("biedny kalkulator")
#zmiana wielkosci okna
window.geometry("800x600")
#Label, fg ustawia kolor napisu, bg ustawia kolor tła
napisGorny  = Label(window, text="Meme TOP", bg="red" )
napisGorny.grid(row=0, column = 0)
#napisGorny.pack(anchor = "n")
fotka = Label(window, bg="black")
fotka.grid(row=1, column=0)

NapisDolny = Label(window, text="MEMEBOT", bg="black", fg="white")
NapisDolny.grid(row=2, column=0)
def losoweZdj():
    img = PhotoImage(file = "zdj.png")
    imga = PhotoImage(file = "zdj1.png")
    imgb = PhotoImage(file = "zdj2.png")
    zdjecia = [img, imga, imgb]
    randomy = random.choice(zdjecia)
    fotka.configure(image=randomy)
   

def losoweNapisy():
    listaNapisow = ["jestem igor", "jestem tomasz", "pozdrawiam huberta", "github" ]
    napisGorny.configure(text=random.choice(listaNapisow))
    NapisDolny.configure(text=random.choice(listaNapisow))
    losoweZdj()

losoweNapisy()
btn = Button(window, command=losoweNapisy, text="Losuj mnie")
btn.grid(row=0,column=1)
    
poleTekstowe = Entry(window)
poleTekstowe.grid(row = 0, column = 0)
#zwraca zawartosc pola tekstowego
poleTekstowe.get()

#zapetla okno aby nie zniklo
window.mainloop()