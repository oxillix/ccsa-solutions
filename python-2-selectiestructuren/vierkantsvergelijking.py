# https://dodona.ugent.be/nl/courses/399/series/3961/activities/1437422481
import math


a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

D = (b**2) - (4*a*c)

if D < 0:
    print('geen wortels')
elif D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)

    print('twee wortels')
    if x1<x2:
        print(x1)
        print(x2)
    else:
        print(x2)
        print(x1)
else:
    print('een wortel')
    print(-b / (2*a))