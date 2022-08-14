def is_pangram(sentence):
    if not sentence:
        return False
    pangram = set(sentence.lower())
    pan = sorted(pangram)
    while pan and pan[0] != "a": 
        pan = pan[1:]
    if len(pan) < 26:
        return False
    return True
