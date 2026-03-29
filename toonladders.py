from alle_tonen import alle_tonen_sharp, alle_tonen_flat, majeur_trappen, mineur_trappen, sharp_toonsoorten_maj, sharp_toonsoorten_min



def majeur_toonladder(starttoon):
    trappen = majeur_trappen
    if starttoon in sharp_toonsoorten_maj:
        tonen = alle_tonen_sharp
    else:
        tonen = alle_tonen_flat

    start_index = tonen.index(starttoon)
    tonen = tonen[start_index:] + tonen[:start_index]
    akkoorden = []
    i = 0
    j = 0
    while i < len(tonen) and j < len(trappen):
        if trappen[j] != "no":
            akkoorden.append(tonen[i])
        i += 1
        j += 1   
    for i in [1,2,5]:
        akkoorden[i] += "m"
    akkoorden[6] += "°"
    return akkoorden

def mineur_toonladder(starttoon):
    trappen = mineur_trappen
    if starttoon in sharp_toonsoorten_min:
        tonen = alle_tonen_sharp
    else:
        tonen = alle_tonen_flat

    start_index = tonen.index(starttoon)
    tonen = tonen[start_index:] + tonen[:start_index]
    akkoorden = []
    i = 0
    j = 0
    while i < len(tonen) and j < len(trappen):
        if trappen[j] != "no":
            akkoorden.append(tonen[i])
        i += 1
        j += 1   
    for i in [0,3,4]:
        akkoorden[i] += "m"
    akkoorden[1] += "°"
    return akkoorden    


