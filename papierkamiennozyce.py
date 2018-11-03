from tkinter import *
import random
window = Tk()
window.title("Papier, kamień, nożyce")
window.geometry("800x600")

alfa = ["s"]

def losoweRucha():
    losoweRuch()
    spr1()
def losoweRucha():
    losoweRuch()
    spr2()
def losoweRuchaa():
    losoweRuch()
    spr3()

def losoweRuch():  
    ruchy = ["papier", "kamien", "nozyce"]
    randomy = random.choice(ruchy)
    alfa = random
    ruchjawny.configure(text=randomy)

def spr1():
    if alfa == "papier":
        wynik.configure(text="remis")
    elif alfa == "kamien":
        wynik.configure(text="wygrałeś")
    elif alfa == "nozyce":
        wynik.configure(text="przegrałes")
def spr2():
    if alfa == "papier":
        wynik.configure(text="przegrałes")
    elif alfa == "kamien":
        wynik.configure(text="remis")
    elif alfa == "nozyce":
        wynik.configure(text="wygrałes")
def spr3():
    if alfa == "papier":
        wynik.configure(text="wygrales")
    elif alfa == "kamien":
        wynik.configure(text="przegrales")
    elif alfa == "nozyce":
        wynik.configure(text="remis")

ruchjawny = Label(window, text="smieski", bg="red" )
ruchjawny.grid(row=1, column = 0)

napisGorny  = Label(window, text="Podaj ruch",bg="red")
napisGorny.grid(row=0, column = 0)

baton1 = Button(window, text="Papier", command=losoweRucha )
baton1.grid(row=0,column=1)

baton2 = Button(window, text="Kamień", command=losoweRuchaa )
baton2.grid(row=0,column=2)

baton3 = Button(window, text="Nożyce", command=losoweRuch )
baton3.grid(row=0,column=3)

wynik = Label(window, text="smiesski", bg="red" )
wynik.grid(row=2, column = 0)




window.mainloop()