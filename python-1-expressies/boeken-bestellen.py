# https://dodona.ugent.be/nl/courses/399/series/3960/activities/1886659767

def boekenBestellen(aantalBoeken):
    boekPrijs = 24.95
    procentKorting = 40
    totaalPrijs = 0

    for n in range(aantalBoeken):
        totaalPrijs += (boekPrijs * ((100-procentKorting)/100))

        if n == 0:
            totaalPrijs += 3
        else:
            totaalPrijs += 0.75

    return round(totaalPrijs, 2)

print(boekenBestellen(60))