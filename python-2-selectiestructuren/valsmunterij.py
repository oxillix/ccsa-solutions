# https://dodona.ugent.be/nl/courses/399/series/3961/activities/408865752

def returnZwaarsteGroep(helling, nCoins):
    if helling == 'links':
        return nCoins[len(nCoins)//3:(len(nCoins)//3)*2]
    elif helling == 'rechts':
        return nCoins[:len(nCoins)//3]
    else:
        return nCoins[-len(nCoins)//3:]

def returnValseCoin(helling, nCoins):
    if helling == 'links':
        return nCoins[1]
    elif helling == 'rechts':
        return nCoins[0]
    else:
        return nCoins[2]

weging1 = input('Helling weegschaal eerste weging: ')
weging2 = input('Helling weegschaal tweede weging: ')

aantalCoins = 9
nCoins = list(range(1,1+aantalCoins))

valseCoinIndex = returnValseCoin(weging2, returnZwaarsteGroep(weging1, nCoins))
print(f'muntstuk #{valseCoinIndex} is vervalst')