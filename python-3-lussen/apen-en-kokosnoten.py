# https://dodona.ugent.be/nl/courses/399/series/3962/activities/654951832
import math

def getNootString(c):
    nootStr = ''
    if c >= 2:
        nootStr = f'{c} noten'
    elif c == 1:
        nootStr = '1 noot'
    else:
        nootStr = 'geen noten'
    return nootStr

def berekenKokosnoten(p, k):
    a = k

    for n in range(1, p+1):
        b = math.floor(a / p)
        c = a % p
        print(f'{a} noten = {b} noten voor piraat#{n} en {getNootString(c)} voor de aap')
        a = (a - b) - c
        
    print(f'elke piraat krijgt {getNootString(math.floor(a / p))} en {getNootString(a % p)} voor de aap')

p = int(input('Aantal piraten: '))
k = int(input('Aantal kokosnoten: '))

berekenKokosnoten(p, k)