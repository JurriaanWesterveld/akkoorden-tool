from toonladders import *

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