# https://dodona.ugent.be/nl/courses/399/series/7814/activities/431253538

#global var
woordenboek = {}

def vertalingToevoegen(woord:str, vertaling:str, woordenboek):
    if woord not in woordenboek:
        woordenboek[woord] = vertaling

def vertaling(woord, woordenboek):
    return woordenboek[woord] if woord in woordenboek else '???'
