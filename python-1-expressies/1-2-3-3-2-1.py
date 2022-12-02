# https://dodona.ugent.be/nl/courses/399/series/3960/activities/558538104

aantalGetallen = 3
outputString = ''

for n in range(aantalGetallen):
    getal = input(f'Geef getal {n+1} in: ')
    outputString = f'{getal} ' + outputString 

print(outputString)