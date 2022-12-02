# https://dodona.ugent.be/nl/courses/399/series/3961/activities/182880102

def checkISBN():
    x10Check = 0

    for n in range(1, 10):
        x10Check += n * int(input(f'x{n}: '))
    x10 = int(input(f'x{10}: '))
    
    x10Check %= 11
    
    if x10 == x10Check:
        return 'OK'
    else:
        return 'FOUT'

print(checkISBN())