# https://dodona.ugent.be/nl/courses/399/series/3962/activities/32506927
import math

def calculateEuler(n=100):
    som = 0
    for i in range(1, n+1):
        som += 1/i**2
    return som

def getKleinsteWaarde():
    n = 1
    while True:
        waarde = abs((calculateEuler(n) - (math.pi**2)/6))
        if waarde <= 1/100:
            return n
        n += 1

print(calculateEuler(100))
print(getKleinsteWaarde())