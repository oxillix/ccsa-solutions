# https://dodona.ugent.be/nl/courses/399/series/7098/activities/197813628


def zeef(n):
    getallenLijst = [i for i in range(2, n+1)]
    m = getallenLijst[0]

    while m**2 <= n+1:
        veelvoudenM = [i for i in range(getallenLijst[m], n+1) if i % m == 0 and i in getallenLijst]
        getallenLijst = [i for i in getallenLijst if i not in veelvoudenM]
        m +=1

    return getallenLijst