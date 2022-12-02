# https://dodona.ugent.be/nl/courses/399/series/3961/activities/1647887074


def berekenWinnaar(keuzeSpeler1, keuzeSpeler2):
    blad_defeats    = ['steen', 'spock']
    steen_defeats   = ['hagedis', 'schaar']
    schaar_defeats  = ['blad', 'hagedis']
    hagedis_defeats = ['blad', 'spock']
    spock_defeats   = ['schaar', 'steen']

    if keuzeSpeler1 == keuzeSpeler2:
        print('gelijkspel')
    else:
        if keuzeSpeler1 == 'blad':
            if keuzeSpeler2 in blad_defeats:
                print('speler1 wint')
            else:
                print('speler2 wint')
        elif keuzeSpeler1 == 'steen':
            if keuzeSpeler2 in steen_defeats:
                print('speler1 wint')
            else:
                print('speler2 wint')
        elif keuzeSpeler1 == 'schaar':
            if keuzeSpeler2 in schaar_defeats:
                print('speler1 wint')
            else:
                print('speler2 wint')
        elif keuzeSpeler1 == 'hagedis':
            if keuzeSpeler2 in hagedis_defeats:
                print('speler1 wint')
            else:
                print('speler2 wint')
        elif keuzeSpeler1 == 'spock':
            if keuzeSpeler2 in spock_defeats:
                print('speler1 wint')
            else:
                print('speler2 wint')

mogelijkeKeuzes = ['blad', 'steen', 'schaar', 'hagedis', 'spock']

keuzeSpeler1 = input('Keuze speler 1: ').strip().lower()
keuzeSpeler2 = input('Keuze speler 2: ').strip().lower()

if keuzeSpeler1 and keuzeSpeler2 in mogelijkeKeuzes:
    berekenWinnaar(keuzeSpeler1, keuzeSpeler2)
else:
    print('Gelieve te kiezen tussen blad, steen, schaar, hagedis of spock')