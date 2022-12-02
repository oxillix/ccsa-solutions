from itertools import combinations
from collections import deque

def precies_een_verschillend(w1,w2):
    if len(w1) != len(w2):
        return False
    ok = False

    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            if ok:
                return False
            else:
                ok = True

    return ok
       

def maak_graaf(woorden):
    graaf = { w:set() for w in woorden} 
    
    for w1,w2 in combinations(woorden,2):
        if precies_een_verschillend(w1,w2):
            graaf[w1].add(w2)
            graaf[w2].add(w1)
    
    return graaf

def kortste_pad(graaf, woord):
    pred = {w: None for w in graaf}
    queue = deque('')
    
    queue.append(woord)
    pred[woord] = woord
    
    while len(queue) != 0:
        v = queue.popleft()
        for w in sorted(graaf[v]):
            if pred[w] is None:
                pred[w] = v
                queue.append(w)

    return pred
    


def geef_pad(pred,doel):
    
    pad =[]
    
    huidig = doel
    while huidig != pred[huidig]:
        pad.append(huidig)
        huidig = pred[huidig]
    pad.append(huidig)
    
    
    return pad[::-1]