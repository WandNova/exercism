from string import punctuation,whitespace,digits


dg = set(digits)
wh = set(whitespace)
pun = set(punctuation)
def rotate(text, key):
    result = "" 
    for i in range(len(text)): 
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)    
        if char.islower(): 
            result += chr((ord(char) + key - 97) % 26 + 97) 
        if char in wh or char in dg or char in pun:
            result += char
    return result