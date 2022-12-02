# https://dodona.ugent.be/nl/courses/399/series/7098/activities/1333299580


def beweeg(coords, toets):
    coords = list(coords)

    if toets == '<':
        coords[0] -= 1
    elif toets == '>':
        coords[0] += 1
    elif toets == 'v':
        coords[1] -= 1
    elif toets == '^':
        coords[1] += 1
    
    return tuple(coords)

def teruggekeerd(toetsen):
    tegenovergestelde_x_as = ['<', '>']
    tegenovergestelde_y_as = ['^', 'v']
    
    if sum(toets in toetsen for toets in tegenovergestelde_x_as) >= 2 or sum(toets in toetsen for toets in tegenovergestelde_y_as) >= 2:
        return True
    else:
        return False

def laatste_levende_positie(zetten):
    coords = [0, 0]
    geldigeZetten = 0
    
    for i, zet in enumerate(zetten):
        if i > 0:
            if teruggekeerd([zetten[i-1], zet]):
                return (geldigeZetten, coords[0], coords[1])
        
        coords = list(beweeg(tuple(coords), zet))
        geldigeZetten += 1

    return (geldigeZetten, coords[0], coords[1])