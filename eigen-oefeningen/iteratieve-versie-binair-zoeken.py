"""
Invoer: een te zoeken item zoekItem, een GESORTEERDE array rij met lengte n
Uitvoer: De index van het eerste voorkomende zoekItem in rij, indien zoekItem niet voorkomt in rij -1
"""
#rij = list(range(0, 5000))
#n = len(rij)
#zoekItem = 2324

def zoekBinair(rij, zoekItem):
    n = len(rij)
    l = 0
    r = n - 1

    while l != r:
        print(f'{l}, {r}')
        import math
        m = int(math.floor((l + r) / 2))

        if rij[m] < zoekItem:
            l = m + 1
        else:
            r = m
    
    if rij[l] == zoekItem:
        return l
    else:
        return -1

index = zoekBinair([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], 70)
print(f"index = {index}")