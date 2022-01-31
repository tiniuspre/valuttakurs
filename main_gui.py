from tkinter import *
from tkinter import ttk
from main import Valutta
import os

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("Valuta")


def knapp():
    L1.config(text=str(Valutta().getValutta(valutta_til.get(), valutta_fra.get(), mengde.get())) + " " + valutta_fra.get())

Label(root, text="Valutta Fra").grid(row=0, column=0)
Label(root, text="Valutta Til").grid(row=0, column=1)
Label(root, text="Mengde").grid(row=0, column=2)

L1 = Label(root, text="0.0")
L1.grid(row=3, columnspan=3)
valutta_til = Entry(root)
valutta_fra = Entry(root)
mengde = Entry(root)

valutta_til.grid(row=1, column=0)
valutta_fra.grid(row=1, column=1)
mengde.grid(row=1, column=2)

Button(root, text="Regn", command=knapp).grid(row=1, column=3)

root.mainloop()