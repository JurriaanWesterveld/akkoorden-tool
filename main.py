from alle_tonen import *
from toonsoort import *
from grondtonen import *

def normalize_toon(toon):
    toon = toon.strip()
    if len(toon) == 1:
        return toon.upper()
    else:
        return toon[0].upper() + toon[1:]

def main():
    
    toonsoort = input("Wil je mineur of majeur? ").strip().upper()
    if toonsoort == "MAJEUR":

        starttoon = input("Van welke toon wil je de akkoorden? ").strip()
        starttoon = normalize_toon(starttoon)
        if starttoon in sharp_to_flat:
            starttoon = sharp_to_flat[starttoon]
        try:
            akkoorden = majeur_toonladder(starttoon)
            print(f"Majeurtoonladder van {starttoon}: {akkoorden}")
        except ValueError:
            print(f"Sorry, {starttoon} is geen geldige toonsoort.")
    elif toonsoort == "MINEUR":

        starttoon = input("Van welke toon wil je de akkoorden? ").strip()
        starttoon = normalize_toon(starttoon)
        if starttoon in sharp_to_flat:
            starttoon = sharp_to_flat[starttoon]
        try:
            akkoorden = mineur_toonladder(starttoon)
            print(f"Mineurtoonladder van {starttoon}: {akkoorden}")
        except ValueError:
            print(f"Sorry, {starttoon} is geen geldige toonsoort.")
    else:
        raise ValueError("Geen geldige invoer")

main()
