def omgekeerd(sleutelDict:dict):
    return {sleutelDict[sleutel]:sleutel for sleutel in sleutelDict}

def code39(zin:str, codeersleutel:dict):
    gecodeerdeZin = ''

    for letter in zin.upper():
        gecodeerdeZin += codeersleutel[letter] + 's'
    
    #remove last s and return
    return gecodeerdeZin[:-1]

def decode39(codeerdeZin, codeerSleutel):
    codeerSleutel = omgekeerd(codeerSleutel)
    decodeerdeZin = ''

    for i in range(0, len(codeerdeZin), 10):
        if i == 0:
            decodeerdeZin += codeerSleutel[codeerdeZin[i:i+9]]
        else:
            decodeerdeZin += codeerSleutel[codeerdeZin[i:i+9]]
        

    return decodeerdeZin