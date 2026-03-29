

def majeur_septime(toonladder):
    for i in [0,3]:
        toonladder[i] += "Maj7"
    for i in [1,2,4,5,6]:
        toonladder[i] += "7"
    return toonladder

def mineur_septime(toonladder):
    for i in [2,5]:
        toonladder[i] += "Maj7"
    for i in [0,1,3,4,6]:
        toonladder[i] += "7"
    return toonladder