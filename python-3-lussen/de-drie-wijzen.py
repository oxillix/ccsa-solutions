prijs = float(input())
veelvoud = int(prijs * 100)
uitkomst = False
for i in range(0, veelvoud):
    for j in range(veelvoud, i-1, -1):
        a = i / 100
        b = j / 100
        if a * b -1 == 0:
            continue
        c = (a + b) / (a * b - 1)
        if round(a + b + c, 6) == prijs:
            if(round(a + b + c) == round(a * b * c)):
                if b < c:
                    x = a
                    y = b
                    z = c
                else:
                    x = a
                    y = c
                    z = b
                if a > y:
                    x = y
                    y = a
                print(f'€{x:.2f} + €{y:.2f} + €{z:.2f} = €{x:.2f} x €{y:.2f} x €{z:.2f} = €{prijs:.2f}')
                uitkomst = True
                break
    if uitkomst:
        break