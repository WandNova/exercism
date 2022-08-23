from string import ascii_letters
def is_isogram(string):
    string = string.lower()
    if not string:
        return True
    for char in string:
        if string.count(char) > 1:
            print(string.count(char))
            return False
    return True
