def ontleding(akkoord):
    if len(akkoord) > 1:
        if akkoord[1] == '#':
            return akkoord[:2], akkoord[2:]
        else:
            return akkoord[0], akkoord[1:]
    else:
        return akkoord[0], ''

def noten(grondnoot:str, toonintervallen:list):
    toonladder = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    noten = []

    for interval in toonintervallen:
        noten.append(toonladder[(toonladder.index(grondnoot)+interval) % len(toonladder)])

    return noten

def akkoord(akkoord, akkoordtypes, akkoordsymbolen):
    ontleeddeAkkoord = ontleding(akkoord)
    toonintervallen = akkoordtypes[akkoordsymbolen[ontleeddeAkkoord[1]]]

    return tuple(noten(ontleeddeAkkoord[0], toonintervallen))
