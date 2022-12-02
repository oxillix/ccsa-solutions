# https://dodona.ugent.be/nl/courses/399/series/7773/activities/522641350

def eersteKlinkerIsKlein(str):
    klinkers = 'aeiou'
    eersteKlinkerIsKlein = False

    for char in str:
        if char in klinkers and char.isupper:
            eersteKlinkerIsKlein = True
    
    return eersteKlinkerIsKlein

def varkenswoord(str):
    klinkers = 'aeiou'
    oldstr = str

    if str[0] in klinkers:
        str += 'way'
    elif str[0] not in klinkers:
        if str[0] == 'q' and str[1] == 'u':
            str = str[2:] + str[0] + str[1] + 'ay'
        else:
            str = str[1:] + str[0] + 'ay'
    



    return str
