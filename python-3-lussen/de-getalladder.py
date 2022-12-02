# https://dodona.ugent.be/nl/courses/399/series/3962/activities/257342570


def getalladder(n=9):
    out = ""

    for i in range(1, n+1):
        out += str(i)
        print(out)
    

n = int(input('Geef n in: '))
getalladder(n)