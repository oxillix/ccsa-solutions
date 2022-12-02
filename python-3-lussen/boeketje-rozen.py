# https://dodona.ugent.be/nl/courses/399/series/3962/activities/1047652305

totaalRozen = int(input('Totaal aantal rozen: '))
totaalWitBlauw = int(input('Totaal aantal witte en blauwe rozen: '))
groterKleiner = input('Meer of minder blauwe/rode dan blauwe/witte rozen? (< of >): ')

#init rozen
rood = 0
wit = 0
blauw = 0

if totaalRozen > totaalWitBlauw:
    # minstens twee rozen van elke kleur.
    rood = totaalRozen - totaalWitBlauw + 2
    wit = totaalRozen - rood
    blauw = totaalWitBlauw - wit

elif groterKleiner == ">":
    blauw = totaalWitBlauw - totaalRozen + 4
    wit = totaalWitBlauw - blauw

    if wit == 1:
        wit += 1
        blauw -= 1

    rood = totaalRozen - wit
else:
    blauw = 2 + totaalWitBlauw - totaalRozen
    wit = totaalWitBlauw - blauw
    rood = totaalRozen - wit

print(f'{blauw}\n{wit}\n{rood}')