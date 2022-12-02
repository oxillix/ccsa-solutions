# https://dodona.ugent.be/nl/courses/399/series/3961/activities/1797346540


uur = int(input('Geef het uur in waarop de babysit begint: '))
minuut = int(input('Geef de minuut in waarop de babysit begint: '))
beginTijdstip = uur + minuut/60

uur = int(input('Geef het uur in waarop de babysit eindigt: '))
minuut = int(input('Geef de minuut in waarop de babysit eindigt: '))
eindTijdstip = uur + minuut/60

if beginTijdstip < 18 or eindTijdstip < 18 or beginTijdstip > eindTijdstip:
    print('ongeldige invoer')
else:
    #print(beginTijdstip)
    if eindTijdstip < 21.5:
        verdiendVoor2130 = (eindTijdstip - beginTijdstip) * 2
        verdiendNa2130 = 0
    else:
        if beginTijdstip < 21.5:
            verdiendVoor2130 = (21.5 - beginTijdstip) * 2
            verdiendNa2130 = (eindTijdstip - 21.5) * 4
        else:
            verdiendVoor2130 = 0
            verdiendNa2130 = (eindTijdstip - beginTijdstip) * 4

    print(verdiendVoor2130+verdiendNa2130)