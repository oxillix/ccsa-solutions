# https://dodona.ugent.be/nl/courses/399/series/3962/activities/1258720912


def geefSomEchteDelers(n):
    som = 0
    for i in range(1, n):
        if n%i == 0:
            som += i
    return som

a = int(input('Geef getal a: '))
b = int(input('Geef getal b: '))

if geefSomEchteDelers(a) == b and geefSomEchteDelers(b) == a:
    print(f'{a} en {b} zijn bevriende getallen')
else:
    print(f'{a} en {b} zijn geen bevriende getallen')