# https://dodona.ugent.be/nl/courses/399/series/7773/activities/1563511392

def maximale_blootstelling(n):
    if n < 80:
        return float(-1)
    else:
        tijdsduur = 60*60*8
        for i in range(83,n+1,3):
            tijdsduur /= 2

        return float(tijdsduur)

