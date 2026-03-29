from toonladders import *
from alle_tonen import *
from septime import *
from common import *


def normalize_toon(toon):
    toon = toon.strip()
    if len(toon) == 1:
        return toon.upper()
    else:
        return toon[0].upper() + toon[1:]

#Hier worden er tonen gegeven aan de trappen vanuit toonladders.py
def bereken_trappen():
    toonsoort = toonsoort_var.get()
    starttoon = starttoon_entry.get()
    
    #Hier wordt gekozen voor majeur
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


    #Hier wordt gekozen voor majeur 7
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



    #Hier wordt gekozen voor mineur
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


    #Hier wordt gekozen voor mineur 7
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