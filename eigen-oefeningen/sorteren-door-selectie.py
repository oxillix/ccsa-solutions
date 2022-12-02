import numpy as np

#arr = np.random.randint(1, 20, 20)

"""
invoer: een array a met grootte n
uitvoer: array a is gesorteerd van klein naar groot
"""
def selection_sort_vooraan(a):
    n = len(a)
    # Start vooraan i = 0
    # Range is niet inclusief, dus achterste waarde is n-2
    for i in range(0, n-1):
        positie = i
        max = a[i]

        for j in range(i+1, n):
            if a[j] < max:
                positie = j
                max = a[j]
    
        a[positie] = a[i]
        a[i] = max
        print(a)

a = [int(_) for _ in input().split()]
selection_sort_vooraan(a)