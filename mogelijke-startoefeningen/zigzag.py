def iszigzag(getallen):
    getallen = list(getallen)
    iszigzag = True

    for i in range(1, len(getallen)):
        if i % 2 == 0:
            if getallen[i-1] > getallen[i]:
                iszigzag = False
            #print(f'i: {i}, {getallen[i-1]} is kleiner of gelijk aan {getallen[i]}')
        else:
            if getallen[i-1] < getallen[i]:
                iszigzag = False
            #print(f'i: {i}, {getallen[i-1]} is groter of gelijk aan {getallen[i]}')
    return iszigzag

def zigzag_traag(getallen):
    getallen.sort()
    zigzagGetallen = getallen
    
    for i in range(0, len(zigzagGetallen), 2):
        if len(zigzagGetallen) - 1 != i:
            zigzagGetallen[i], zigzagGetallen[i+1] = zigzagGetallen[i+1], zigzagGetallen[i]

    getallen = zigzagGetallen
    #print(getallen)
    return None

def zigzag_snel(getallen):
    zigzagGetallen = getallen

    for i in range(0, len(getallen), 2):
        #print(f'i: {i}, {len(getallen)}')
        if zigzagGetallen[i] < zigzagGetallen[i-1] and i > 0:
            zigzagGetallen[i-1], zigzagGetallen[i] = zigzagGetallen[i], zigzagGetallen[i-1]
        if i < len(zigzagGetallen)-1 and getallen[i] < zigzagGetallen[i+1]:
            zigzagGetallen[i+1], zigzagGetallen[i] = zigzagGetallen[i], zigzagGetallen[i+1]
    
    getallen = zigzagGetallen
    return None