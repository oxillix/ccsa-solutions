# https://dodona.ugent.be/nl/courses/399/series/3960/activities/910319224

x10 = 0

for n in range(1, 10):
    x10 += n * int(input(f'x{n}: '))
    
x10 %= 11

print(x10)