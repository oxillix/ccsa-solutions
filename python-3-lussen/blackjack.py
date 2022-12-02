# https://dodona.ugent.be/nl/courses/399/series/3962/activities/1319193582

import random
random.randint(1, 11)

kaartTotaal = 0


while kaartTotaal < 21:
    kaart = int(input('Geef kaart in: '))
    if kaart == 0:
        print(f'Voorzichtig gespeeld ({kaartTotaal})')
        break
    kaartTotaal += kaart
    if kaartTotaal == 21:
        print('Gewonnen!')
        break
else:
    print(f'Verbrand ({kaartTotaal})')