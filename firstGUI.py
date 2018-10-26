from tkinter import *

window = Tk()
window.title("Bardzo Ciekawe")
window.geometry("800x800")

etykieta = Label(window, text = "Podaj numer swojej karty")
etykieta.grid(row=0, column=0)

kod = Entry(window, bg="black" )
kod.grid(row=1, column=0)

btn = Button(window, text="Frre V-Bucks")
btn.grid(row=1, column=1)
def kradnijKarte():
    etykieta.configure(text=kod.get())
btn.configure(command=kradnijKarte)
window.mainloop()