#https://dodona.ugent.be/nl/courses/399/series/7773/activities/192047393/

def evenOneven(n):
    even = 0
    oneven = 0

    for c in enumerate(str(n)):
        if int(c[1])%2==0:
            even += 1
        else:
            oneven += 1
    
    return even, oneven

def volgende(n):
    evenOnevenResult = evenOneven(n)
    if evenOnevenResult[0]==0:
        return int(f'{evenOnevenResult[1]}{len(str(n))}')
    else:
        return int(f'{evenOnevenResult[0]}{evenOnevenResult[1]}{len(str(n))}')

def stappen(n):
    counter = 0

    while volgende(n) != 123:
        if counter == 0:
            counter += 1

        n = volgende(n)
        counter += 1

    return counter