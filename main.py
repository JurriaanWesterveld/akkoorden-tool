from alle_tonen import *
from toonsoort import *
from grondtonen import *
import tkinter as tk

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
            output_label.config(text=f"Majeurtoonladder van {starttoon}: {akkoorden}")
        except ValueError:
            output_label.config(text=f"Sorry, {starttoon} is geen geldige toonsoort.")
    elif toonsoort == "MINEUR":
        starttoon = normalize_toon(starttoon)
        if starttoon in sharp_to_flat:
            starttoon = sharp_to_flat[starttoon]
        try:
            akkoorden = mineur_toonladder(starttoon)
            output_label.config(text=f"Mineurtoonladder van {starttoon}: {akkoorden}")
        except ValueError:
           output_label.config(text=f"Sorry, {starttoon} is geen geldige toonsoort.")

root = tk.Tk()
root.title("Toonladder Generator")

toonsoort_var = tk.StringVar(value="MAJEUR")
tk.Label(root, text="Werk je in mineur of majeur?").pack()
tk.OptionMenu(root, toonsoort_var, "MAJEUR", "MINEUR").pack()

tk.Label(root, text="Van welke toon wil je de akkoorden?").pack()
starttoon_entry = tk.Entry(root)
starttoon_entry.pack()

tk.Button(root, text="Bereken akkoorden", command=bereken_akkoorden).pack()

output_label = tk.Label(root, text="", fg="blue", font=("Helvetica", 12))
output_label.pack(pady=10)

root.mainloop()