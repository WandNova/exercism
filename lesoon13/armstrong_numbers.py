def is_armstrong_number(number):
    x = str(number)
    r = 0
    for i in x:
        r += int(i)**len(x)
    return r == number
            