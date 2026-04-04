from tkinter import *
from songwriting import open_songwriting_venster
from toonladders import *
from alle_tonen import *
from septime import *
from common import *

#Hier wordt de invoer voor de starttoon genormaliseerd
def normalize_toon(toon):
    toon = toon.strip()
    if len(toon) == 1:
        return toon.upper()
    else:
        return toon[0].upper() + toon[1:].lower()
    
#button voor songwriting venster
venster_songwriting = tk.Button(root, padx=20, pady=50, text=f"Begin met songwriten!""\n""(opent een ander venster)", state=DISABLED, command=open_songwriting_venster)

#Hier worden er tonen gegeven aan de trappen vanuit toonladders.py
def bereken_trappen():
    toonsoort = toonsoort_var.get()
    starttoon = starttoon_entry.get()
       
    #Hier wordt gekozen voor majeur
    if toonsoort == "MAJEUR":
        if starttoon == "":
            output_label.config(text="Kies een toon om te beginnen. e.g. C of Ab")
            venster_songwriting.config(state=DISABLED)
            return None
        starttoon = normalize_toon(starttoon)
        if starttoon in sharp_to_flat:
            starttoon = sharp_to_flat[starttoon]
        try:
            akkoorden = majeur_toonladder(starttoon)
            output_label.config(text=f"Majeurtoonladder van {starttoon}: {akkoorden}""\n"f"Septime:{majeur_septime(starttoon)}")
            venster_songwriting.config(state=NORMAL)
            venster_songwriting.pack(pady=10)
        except ValueError:
            output_label.config(text=f"Sorry, {starttoon} is geen geldige toonsoort.")
            venster_songwriting.config(state=DISABLED)
        
        

    #Hier wordt gekozen voor mineur
    if toonsoort == "MINEUR":
        if starttoon == "":
            output_label.config(text="Kies een toon om te beginnen. e.g. C of Ab")
            venster_songwriting.config(state=DISABLED)
            return None
        starttoon = normalize_toon(starttoon)
        if starttoon in flat_to_sharp:
            starttoon = flat_to_sharp[starttoon]
        try:
            akkoorden = mineur_toonladder(starttoon)
            output_label.config(text=f"Mineurtoonladder van {starttoon}: {akkoorden}""\n"f"Septime:{mineur_septime(starttoon)}")
            venster_songwriting.config(state=NORMAL)
            venster_songwriting.pack(pady=10)
        except ValueError:
           output_label.config(text=f"Sorry, {starttoon} is geen geldige toonsoort.")
           venster_songwriting.config(state=DISABLED)
        

