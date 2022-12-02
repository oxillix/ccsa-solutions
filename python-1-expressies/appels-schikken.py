# https://dodona.ugent.be/nl/courses/399/series/3960/activities/2071746302


aantalAppels = int(input('Aantal appels: '))

aantalKisten = aantalAppels // 20
aantalPaletten = int(aantalKisten // 35)

print(aantalPaletten)
print(aantalKisten % 35)
print(aantalAppels % 20)