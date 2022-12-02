# https://dodona.ugent.be/nl/courses/399/series/7773/activities/581452346


def bovensteboven(n):
    count = 0
    n = str(n)
    for digit in n:
        if digit == '6':
            if n[-(count+1)] != '9':
                #print(digit + ' !not equals! ' + n[-(count+1)])
                return False
        elif digit == '9':
            if n[-(count+1)] != '6':
                #print(n[-(count+1)])
                #print(digit + ' !not equals! ' + n[-(count+1)])
                return False
        elif digit in '23457':
            return False
        elif digit != n[-(count+1)]:
            return False
        count +=1
    return True

def volgende(n):
    n=str(int(n) + 1)
    while not bovensteboven(n):
        n=str(int(n) + 1)
    return int(n)

#print(bovensteboven('690'))
volgende('98765')
