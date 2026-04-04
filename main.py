from alle_tonen import *
from common import *

#Hier wordt de invoer voor de starttoon genormaliseerd
def normalize_toon(toon):
    toon = toon.strip()
    if len(toon) == 1:
        return toon.upper()
    else:
        return toon[0].upper() + toon[1:].lower()
    
#Hier worden de septime akkoorden berekend voor zowel mineur als majeur    
def mineur_septime(starttoon):
    toonladder = mineur_toonladder(starttoon)
    septime_akkoorden = toonladder.copy()
    septime_akkoorden[0] += "7"
    septime_akkoorden[1] += "7"
    septime_akkoorden[2] += "maj7"
    septime_akkoorden[3] += "7"
    septime_akkoorden[4] += "7"
    septime_akkoorden[5] += "maj7"
    septime_akkoorden[6] += "7"
    return septime_akkoorden

def majeur_septime(starttoon):
    toonladder = majeur_toonladder(starttoon)
    septime_akkoorden = toonladder.copy()
    septime_akkoorden[0] += "maj7"
    septime_akkoorden[1] += "7"
    septime_akkoorden[2] += "7"
    septime_akkoorden[3] += "maj7"
    septime_akkoorden[4] += "7"
    septime_akkoorden[5] += "7"
    septime_akkoorden[6] += "7"
    return septime_akkoorden

#Hier worden er tonen gegeven aan de trappen vanuit toonladders.py
def bereken_trappen(toonsoort=None, starttoon=None):
    if toonsoort is None:
        toonsoort = toonsoort_var.get()
    if starttoon is None:
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
            return akkoorden
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
            return akkoorden
        except ValueError:
           output_label.config(text=f"Sorry, {starttoon} is geen geldige toonsoort.")
           venster_songwriting.config(state=DISABLED)

#Hier worden de trappen in majeur berekend zonder direct een toonsoort te geven
def majeur_toonladder(starttoon):
    trappen = majeur_toonladders
    if starttoon in majeur_toonladders:
        akkoorden = trappen[starttoon]
        return akkoorden
    else:
        raise ValueError(f"{starttoon} is geen geldige toonsoort.")

#Hier worden de trappen in mineur berekend zonder direct een toonsoort te geven
def mineur_toonladder(starttoon):
    trappen = mineur_toonladders
    if starttoon in mineur_toonladders:
        akkoorden = trappen[starttoon]
        return akkoorden
    else:
        raise ValueError(f"{starttoon} is geen geldige toonsoort.")
    
#Dit maakt het venster
root.title("Toonladder Generator")
root.geometry("600x400")

#Dit is de menu waar je kiest tussen verschillende toonsoorten
tk.Label(root, text="Werk je in mineur of majeur?").pack()
tk.OptionMenu(root, toonsoort_var, "MAJEUR", "MINEUR").pack()

#Hier kies je de grondtoon en wordt dat doorgestuurd naar de "bereken_trappen" functie
tk.Label(root, text="Van welke toon wil je de akkoorden?").pack()
starttoon_entry.pack()
tk.Button(root, text="Bereken akkoorden", command=bereken_trappen).pack()
output_label.pack()


#button voor afsluiten
afsluiten_button = tk.Button(root, text="Afsluiten", width=25, activebackground="red", command=root.destroy)
afsluiten_button.place(relx=0.5, rely=0.9, anchor=CENTER)
    
#Dit opent een songwriting venster
def open_songwriting_venster():
    songwriting_venster = tk.Toplevel(root)
    songwriting_venster.title("Songwriting")
    songwriting_venster.geometry("400x400")
    tk.Label(songwriting_venster, text="Hier kunnen we songwriten!").pack(pady=10)
    tk.Label(songwriting_venster, text="Hier kunnen we de akkoorden gebruiken die we net hebben berekend!").pack(pady=10)
    current_akkoord = bereken_trappen()[0]
    tk.Button(songwriting_venster, text=f"{bereken_trappen()[0]}").pack(pady=10)
    tk.Label(songwriting_venster, text="Dit zijn de laddereigen akkoorden die je kan gebruiken:").pack(pady=10)
    tweedetrap = tk.Button(songwriting_venster, text=f"{bereken_trappen()[1]}")
    tweedetrap.place(relx=0.13, rely=0.43, anchor=CENTER)
    derdetrap = tk.Button(songwriting_venster, text=f"{bereken_trappen()[2]}")
    derdetrap.place(relx=0.28, rely=0.43, anchor=CENTER)
    vierdetrap = tk.Button(songwriting_venster, text=f"{bereken_trappen()[3]}")
    vierdetrap.place(relx=0.43, rely=0.43, anchor=CENTER)
    vijfdetrap = tk.Button(songwriting_venster, text=f"{bereken_trappen()[4]}")
    vijfdetrap.place(relx=0.58, rely=0.43, anchor=CENTER)
    zesdetrap = tk.Button(songwriting_venster, text=f"{bereken_trappen()[5]}")
    zesdetrap.place(relx=0.73, rely=0.43, anchor=CENTER)
    zevendetrap = tk.Button(songwriting_venster, text=f"{bereken_trappen()[6]}")
    zevendetrap.place(relx=0.88, rely=0.43, anchor=CENTER)
    tk.Label(songwriting_venster, text="Dit zijn de alternatieve akkoorden die je kan gebruiken:").pack(pady=30)
    if current_akkoord in majeur_opties:
        optie1 = tk.Button(songwriting_venster, text=f"{majeur_opties[bereken_trappen()[0]][0]}")
        optie1.place(relx=0.13, rely=0.58, anchor=CENTER)
        optie2 = tk.Button(songwriting_venster, text=f"{majeur_opties[bereken_trappen()[0]][1]}")
        optie2.place(relx=0.28, rely=0.58, anchor=CENTER)
    if current_akkoord in mineur_opties:
        optie1 = tk.Button(songwriting_venster, text=f"{mineur_opties[bereken_trappen()[0]][0]}")
        optie1.place(relx=0.13, rely=0.58, anchor=CENTER)
        optie2 = tk.Button(songwriting_venster, text=f"{mineur_opties[bereken_trappen()[0]][1]}")
        optie2.place(relx=0.28, rely=0.58, anchor=CENTER)
    if current_akkoord in dominant_opties:
        optie1 = tk.Button(songwriting_venster, text=f"{dominant_opties[bereken_trappen()[0]][0]}")
        optie1.place(relx=0.13, rely=0.58, anchor=CENTER)
        optie2 = tk.Button(songwriting_venster, text=f"{dominant_opties[bereken_trappen()[0]][1]}")
        optie2.place(relx=0.28, rely=0.58, anchor=CENTER)
        optie3 = tk.Button(songwriting_venster, text=f"{dominant_opties[bereken_trappen()[0]][2]}")
        optie3.place(relx=0.43, rely=0.58, anchor=CENTER)
        optie4 = tk.Button(songwriting_venster, text=f"{dominant_opties[bereken_trappen()[0]][3]}")
        optie4.place(relx=0.58, rely=0.58, anchor=CENTER)
    if current_akkoord in verminderd_opties:
        optie1 = tk.Button(songwriting_venster, text=f"{verminderd_opties[bereken_trappen()[0]][0]}")
        optie1.place(relx=0.13, rely=0.58, anchor=CENTER)
        optie2 = tk.Button(songwriting_venster, text=f"{verminderd_opties[bereken_trappen()[0]][1]}")
        optie2.place(relx=0.28, rely=0.58, anchor=CENTER)
        optie3 = tk.Button(songwriting_venster, text=f"{verminderd_opties[bereken_trappen()[0]][2]}")
        optie3.place(relx=0.43, rely=0.58, anchor=CENTER)
        optie4 = tk.Button(songwriting_venster, text=f"{verminderd_opties[bereken_trappen()[0]][3]}")
        optie4.place(relx=0.58, rely=0.58, anchor=CENTER)
        optie5 = tk.Button(songwriting_venster, text=f"{verminderd_opties[bereken_trappen()[0]][4]}")
        optie5.place(relx=0.73, rely=0.58, anchor=CENTER)



    #button voor afsluiten
    afsluiten_button2 = tk.Button(songwriting_venster, text="Afsluiten", width=25, activebackground="red", command=songwriting_venster.destroy)
    afsluiten_button2.place(relx=0.5, rely=0.9, anchor=CENTER)

#button voor songwriting venster
venster_songwriting = tk.Button(root, padx=20, pady=50, text=f"Begin met songwriten!""\n""(opent een ander venster)", state=DISABLED, command=open_songwriting_venster)



root.mainloop()