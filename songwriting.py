from common import *
import tkinter as tk


#Dit opent een songwriting venster
def open_songwriting_venster():
    songwriting_venster = tk.Toplevel(root)
    songwriting_venster.title("Songwriting")
    songwriting_venster.geometry("400x400")

    tk.Label(songwriting_venster, text="Hier kunnen we songwriten!").pack(pady=10)
    tk.Button(songwriting_venster, text="Afsluiten", width=25, command=songwriting_venster.destroy).pack()