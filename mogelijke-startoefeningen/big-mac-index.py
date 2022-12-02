# https://dodona.ugent.be/nl/courses/399/series/7773/activities/1131866318


def waardering(prijs, rWisselkoers):
    wisselkoers = prijs/4.07
    v = ((wisselkoers - rWisselkoers) / rWisselkoers) * 100

    if v <= -25:
        return 'sterk ondergewaardeerd'
    elif -25 < v <= -5:
        return "ondergewaardeerd"
    elif -5 < v <= 5:
        return "ongeveer gelijk"
    elif 5 < v <= 25:
        return "overgewaardeerd"
    elif v > 25:
        return "sterk overgewaardeerd"

def wisselkoersanalyse(prijsStr, rWisselkoers):
    prijs = float(prijsStr.split(' ', 1)[0])
    muntEenheid = prijsStr.split(' ', 1)[1]

    return f'De {muntEenheid} is {waardering(prijs, rWisselkoers)} ten opzichte van de dollar.'