# https://dodona.ugent.be/nl/courses/399/series/7773/activities/862295437

def codeer(t, s):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    versleuteldeText = ''
    
    for i in range(len(t)):
        if t[i].isupper():
            versleuteldeText += alfabet[((alfabet.index(t[i]) + alfabet.index(s[i%len(s)])) % 26)]
        else:
            versleuteldeText += t[i]
    return versleuteldeText

def decodeer(t, s):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    clearText = ''
    
    for i in range(len(t)):
        if t[i].isupper():
            #leuke oefening deze lool
            clearText += alfabet[((alfabet.index(t[i]) - alfabet.index(s[i%len(s)])) % 26)]
        else:
            clearText += t[i]
    return clearText