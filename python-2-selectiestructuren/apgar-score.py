# https://dodona.ugent.be/nl/courses/399/series/3961/activities/668571979

ademhaling = {
    'geen': 0,
    'zwak': 1,
    'goed doorhuilen': 2
}

spierspanning = {
    'slap': 0,
    'enige flexie': 1,
    'actieve beweging': 2
}

kleur = {
    'blauw': 0,
    'bleek': 0,
    'extremiteiten': 1,
    'roze': 2
}

reactie = {
    'geen': 0,
    'enige beweging': 1,
    'krachtig huilen': 2
}

a = input('Ademhaling: ')
p = int(input('Pols- / hartslag: '))
g = input('Spierspanning / -tonus: ')
k = input('Aspect / kleur: ')
r = input('Reactie op prikkels: ')

if not a in [*ademhaling] or not g in [*spierspanning] or not k in [*kleur] or not r in [*reactie] or p < 0:
    print('ongeldige invoer')
else:
    score = 0

    if p == 0:
        score += 0
    elif p < 100:
        score += 1
    else:
        score += 2
    
    score += ademhaling[a]
    score += spierspanning[g]
    score += kleur[k]
    score += reactie[r]
    
    if score < 4:
        print('alarm')
    else:
        print(score)