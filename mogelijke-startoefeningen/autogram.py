def letterfrequenties(zin:str):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    aantalLettersInZin = {}

    for letter in zin.lower():
        if letter in alfabet:
            #print(letter)
            if letter in aantalLettersInZin:
                aantalLettersInZin[letter] += 1
            else:
                aantalLettersInZin[letter] = 1
    return aantalLettersInZin

def letterposities(zin:str):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    aantalLettersInZin = {}

    for letterAlfabet in alfabet:
        posities = []

        for i, letter in enumerate(zin.lower()):
            if letter in alfabet:
                if letterAlfabet == letter:
                    posities.append(i)
        
        if posities != []:
            aantalLettersInZin[letterAlfabet] = set(posities)

    return aantalLettersInZin
