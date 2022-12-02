# https://dodona.ugent.be/nl/courses/399/series/3962/activities/364433585

#global vars h&b, x&y for simplicity
h = int(input('Vul de hoogte in: '))
b = int(input('Vul de breedte in: '))
x=1
y=1

#helper functions
def inPocketLO(x, y):
    return x==0 and y==0

def inPocketLB(x, y):
    return x==0 and y==h

def inPocketRO(x, y):
    return x==b and y==0

def inPocketRB(x, y):
    return x==b and y==h

def veranderKoers(richting, kantGeraakt):
    if kantGeraakt == 'b':
        if richting == 'rb':
            richting = 'ro'
        elif richting == 'lb':
            richting = 'lo'
    if kantGeraakt == 'o':
        if richting == 'ro':
            richting = 'rb'
        elif richting == 'lo':
            richting = 'lb'
    if kantGeraakt == 'l':
        if richting == 'lb':
            richting = 'rb'
        elif richting == 'lo':
            richting = 'ro'
    if kantGeraakt == 'r':
        if richting == 'rb':
            richting = 'lb'
        elif richting == 'ro':
            richting = 'lo'

    return richting


#start calculatie

#richting kan lb(linksboven), lo(linksonder), rb(rechtsboven) of ro(rechtsonder) zijn.
richting = 'rb'
count = 0

count = 0 
while not any([inPocketLO(x, y), inPocketRO(x, y), inPocketLB(x, y), inPocketRB(x, y)]):
    #verplaats de bal 1 stap
    if richting == 'rb':
        x += 1
        y += 1
    elif richting == 'ro':
        x += 1
        y -= 1
    elif richting == 'lo':
        x -= 1
        y -= 1
    elif richting == 'lb':
        x -= 1
        y += 1

    #check of het in pocket zit
    if any([inPocketLO(x, y), inPocketRO(x, y), inPocketLB(x, y), inPocketRB(x, y)]):
        break

    #check of het de rand raakt
    if y == h: #bovenkant geraakt
        print(f'bovenband ({x}, {y})')
        richting = veranderKoers(richting, 'b')
    if y == 0: #onderkant geraakt
        print(f'onderband ({x}, {y})')
        richting = veranderKoers(richting,'o')
    if x == b: #rechterkant geraakt
        print(f'rechterband ({x}, {y})')
        richting = veranderKoers(richting, 'r')
    if x == 0: #linkerkant geraakt
        print(f'linkerband ({x}, {y})')
        richting = veranderKoers(richting, 'l')

#check of het in pocket zit
if inPocketLO(x, y):
    print(f'linkeronderpocket ({x}, {y})')

if inPocketRO(x, y):
    print(f'rechteronderpocket ({x}, {y})')

if inPocketLB(x, y):
    print(f'linkerbovenpocket ({x}, {y})')

if inPocketRB(x, y):
    print(f'rechterbovenpocket ({x}, {y})')
