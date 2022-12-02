zijde = input('Zijde kaart (kleur, waarde): ')
kleur_waarde = input('Kleur of waarde van kaart: ')
kaartOmdraaien = input('Als op de ene zijde van een kaart een even getal staat, heeft de andere zijde dan een rode kleur? ')

if zijde == 'kleur':
    if kaartOmdraaien == 'nee':
        if kleur_waarde == 'rood':
            print(f'Juist: kaarten met {zijde} {kleur_waarde} moeten niet gedraaid worden.')
        else:
            print(f'Fout: kaarten met {zijde} {kleur_waarde} moeten gedraaid worden.')
    else:
        if kleur_waarde != 'rood':
            print(f'Juist: kaarten met {zijde} {kleur_waarde}  moeten gedraaid worden.')
        else:
            print(f'Fout: kaarten met {zijde} {kleur_waarde}  moeten niet gedraaid worden.')
else:
    if kaartOmdraaien == 'ja':
        if int(kleur_waarde) % 2 != 0:
            print(f'Fout: kaarten met {zijde} {kleur_waarde} moeten niet gedraaid worden.')
        else:
            print(f'Juist: kaarten met {zijde} {kleur_waarde} moeten gedraaid worden.')
    else:
        if int(kleur_waarde) % 2 == 0:
            print(f'Fout: kaarten met {zijde} {kleur_waarde} moeten gedraaid worden.')
        else:
           print(f'Juist: kaarten met {zijde} {kleur_waarde} moeten niet gedraaid worden.')