# https://dodona.ugent.be/nl/courses/399/series/7098/activities/623087135

def nieuw_kaartspel(kleurLijst, waardeLijst):
    mergedList = [f'{k}{w}' for k in kleurLijst for w in waardeLijst]
    
    return mergedList

def splits_kaartspel(kaartlijst):
    eersteHelftLijst = kaartlijst[:len(kaartlijst)//2]
    tweedeHelftLijst = kaartlijst[len(kaartlijst)//2:]
    
    return eersteHelftLijst, tweedeHelftLijst
    
def faro_shuffle(kaartlijst1, kaartlijst2):
    newList = []

    for i, w in enumerate(kaartlijst2):
        if i < len(kaartlijst1):
            newList.append(kaartlijst1[i])
        newList.append(w)

    return newList