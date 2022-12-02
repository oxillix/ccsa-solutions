# https://dodona.ugent.be/nl/courses/399/series/7098/activities/117689921


def alfabetisch(str):
    #maak lijst van string met split
    woorden = str.split(' ')
    
    #sorteer woorden alfabetisch
    woorden.sort()
    
    return ' '.join(woorden)