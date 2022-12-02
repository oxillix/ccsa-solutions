def isISBN13(code:str):
    if not(
        len(code) == 13 and
        code.isdigit()
    ):
        return False
    
    if code[:3] not in {'978', '979'}:
        return False

    controle = 0
    for i in range(12):
        if i%2:
            controle += 3*int(code[i])
        else:
            controle += int(code[i])

    controlecijf = controle % 10
    controlecijf = (10 - controlecijf) % 10
    return controlecijf == int(code[-1])

def overzicht(codeList):
    landInfo = [0] * 11

    for code in codeList:
        if not isISBN13(code):
            landInfo[10] += 1 
        else:
            landInfo[int(code[3])] += 1

    print(f'Engelstalige landen: {landInfo[0] + landInfo[1]}')
    print(f'Franstalige landen: {landInfo[2]}')
    print(f'Duitstalige landen: {landInfo[3]}')
    print(f'Japan: {landInfo[4]}')
    print(f'Russischtalige landen: {landInfo[5]}')
    print(f'China: {landInfo[7]}')
    print(f'Overige landen: {landInfo[6] + landInfo[8] + landInfo[9]}')
    print(f'Fouten: {landInfo[10]}')