from alle_tonen import *
from toonladders import *
from septime import *
import tkinter as tk
import tkinter.font as tkFont

def normalize_toon(toon):
    toon = toon.strip()
    if len(toon) == 1:
        return toon.upper()
    else:
        return toon[0].upper() + toon[1:]


def bereken_akkoorden():
    toonsoort = toonsoort_var.get()
    starttoon = starttoon_entry.get()
    
    if toonsoort == "MAJEUR":
        starttoon = normalize_toon(starttoon)
        if starttoon in sharp_to_flat:
            starttoon = sharp_to_flat[starttoon]
        try:
            akkoorden = majeur_toonladder(starttoon)
            if starttoon == "Gb":
                akkoorden = ["Cb" if akkoord == "B" else akkoord for akkoord in akkoorden]
            elif starttoon == "F#":
                akkoorden = ["E#°" if akkoord == "F°" else akkoord for akkoord in akkoorden]
            output_label.config(text=f"Majeurtoonladder van {starttoon}: {akkoorden}")
        except ValueError:
            output_label.config(text=f"Sorry, {starttoon} is geen geldige toonsoort.")
    tk.Button(root, padx=20, pady=50, text=f"Begin met songwriten!""\n""(opent een ander venster)", command=open_songwriting_venster).pack()



    if toonsoort == "MAJEUR 7":
        starttoon = normalize_toon(starttoon)
        if starttoon in sharp_to_flat:
            starttoon = sharp_to_flat[starttoon]
        try:
            akkoorden = majeur_toonladder(starttoon)
            if starttoon == "Gb":
                akkoorden = ["Cb" if akkoord == "B" else akkoord for akkoord in akkoorden]
            elif starttoon == "F#":
                akkoorden = ["E#°" if akkoord == "F°" else akkoord for akkoord in akkoorden]
            akkoorden = majeur_septime(akkoorden)
            output_label.config(text=f"Majeurtoonladder van {starttoon}: {akkoorden}")
        except ValueError:
            output_label.config(text=f"Sorry, {starttoon} is geen geldige toonsoort.")
    tk.Button(root, padx=20, pady=50, text=f"Begin met songwriten!""\n""(opent een ander venster)", command=open_songwriting_venster).pack()




    if toonsoort == "MINEUR":
        starttoon = normalize_toon(starttoon)
        if starttoon in flat_to_sharp:
            starttoon = flat_to_sharp[starttoon]
        try:
            akkoorden = mineur_toonladder(starttoon)
            if starttoon == "D#":
                akkoorden = ["E#°" if akkoord == "F°" else akkoord for akkoord in akkoorden]
            output_label.config(text=f"Mineurtoonladder van {starttoon}: {akkoorden}")
        except ValueError:
           output_label.config(text=f"Sorry, {starttoon} is geen geldige toonsoort.")
    tk.Button(root, padx=20, pady=50, text=f"Begin met songwriten!""\n""(opent een ander venster)", command=open_songwriting_venster).pack()



    if toonsoort == "MINEUR 7":
        starttoon = normalize_toon(starttoon)
        if starttoon in flat_to_sharp:
            starttoon = flat_to_sharp[starttoon]
        try:
            akkoorden = mineur_toonladder(starttoon)
            if starttoon == "D#":
                akkoorden = ["E#°" if akkoord == "F°" else akkoord for akkoord in akkoorden]
            akkoorden = mineur_septime(akkoorden)
            output_label.config(text=f"Mineurtoonladder van {starttoon}: {akkoorden}")
        except ValueError:
            output_label.config(text=f"Sorry, {starttoon} is geen geldige toonsoort.")
    tk.Button(root, padx=20, pady=50, text=f"Begin met songwriten!""\n""(opent een ander venster)", command=open_songwriting_venster).pack()


root = tk.Tk()
root.title("Toonladder Generator")
root.geometry("600x300")

toonsoort_var = tk.StringVar(value="MAJEUR")
tk.Label(root, text="Werk je in mineur of majeur?").pack()
tk.OptionMenu(root, toonsoort_var, "MAJEUR", "MAJEUR 7", "MINEUR", "MINEUR 7").pack()

tk.Label(root, text="Van welke toon wil je de akkoorden?").pack()
starttoon_entry = tk.Entry(root)
starttoon_entry.pack()

tk.Button(root, text="Bereken akkoorden", command=bereken_akkoorden).pack()

normal_font = tkFont.Font(family="Arial", size=18, weight="bold")
output_label = tk.Label(root, text="", fg="green", font=normal_font)
output_label.pack(pady=10)

def open_songwriting_venster():
    songwriting_venster = tk.Toplevel(root)
    songwriting_venster.title("Songwriting")
    songwriting_venster.geometry("400x400")

    tk.Label(songwriting_venster, text="Hier kunnen we songwriten!").pack(pady=10)
    tk.Button(songwriting_venster, text="Afsluiten", width=25, command=songwriting_venster.destroy).pack()



tk.Button(root, text="Afsluiten", width=25, command=root.destroy).pack()





root.mainloop()