
def dubbel(getallenLijst):
    for getal in getallenLijst:
        if getallenLijst.count(getal) > 1:
            return getal
    return None

def dubbels(getallenLijst):
    eenmalig = []
    meerdereMalen = []

    for getal in getallenLijst:
        if getallenLijst.count(getal) == 1:
            eenmalig.append(getal)
        else:
            meerdereMalen.append(getal)

    return set(eenmalig), set(meerdereMalen)