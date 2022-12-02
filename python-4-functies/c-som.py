# https://dodona.ugent.be/nl/courses/399/series/7773/activities/1706631167


def csom(n):
    while len(str(n)) > 1:
        sum = 0
        for i in str(n):
            sum += int(i)
        n = sum
    return n