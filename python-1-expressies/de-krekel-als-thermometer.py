# https://dodona.ugent.be/nl/courses/399/series/3960/activities/933531418

def berekenTempInF(aantalTjirps):
    return 50 + ((aantalTjirps-40)/4)

def berekenTempInC(aantalTjirps):
    return 10 + ((aantalTjirps-40)/7)

aantalTjirps = int(input('Aantal Tjirps: ')) 

print(f'temperatuur (Fahrenheit): {berekenTempInF(aantalTjirps)}')
print(f'temperatuur (Celsius): {berekenTempInC(aantalTjirps)}')