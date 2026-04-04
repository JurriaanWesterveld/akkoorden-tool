from common import *
import tkinter as tk
from toonladders import *


#Dit opent een songwriting venster
def open_songwriting_venster():
    songwriting_venster = tk.Toplevel(root)
    songwriting_venster.title("Songwriting")
    songwriting_venster.geometry("400x400")
    tk.Label(songwriting_venster, text="Hier kunnen we songwriten!").pack(pady=10)
    tk.Label(songwriting_venster, text="Hier kunnen we de akkoorden gebruiken die we net hebben berekend!").pack(pady=10)
    tk.Button(songwriting_venster, text=f"{starttoon_entry.get().upper()}").pack(pady=10)































    #button voor afsluiten
    tk.Button(songwriting_venster, text="Afsluiten", width=25, activebackground="red", command=songwriting_venster.destroy).pack()
