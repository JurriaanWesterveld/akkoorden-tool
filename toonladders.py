from alle_tonen import *
from common import *


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
   
