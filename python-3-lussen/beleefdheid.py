# https://dodona.ugent.be/nl/courses/399/series/3962/activities/2134730675
import math


n = int(input('Geef getal n in: '))
beleefdCounter = 0

for i in range(1, n):
    sum = 0
    j = i
    while sum < n:
        sum += j
        if sum == n:
            beleefdCounter += 1
        j += 1

print(beleefdCounter)