def convert(number):
    pling = "Pling"
    plang = "Plang"
    plong = "Plong"
    if number < 3:
        return str(number)
    elif (number % 3 == 0 and number % 5 == 0 and number % 7 == 0):
        return (pling+plang+plong)
    elif (number % 3 == 0 and number % 5 == 0):
        return (pling+plang)
    elif (number % 3 == 0 and number % 7 == 0):
        return (pling+plong)
    elif number % 3 == 0:
        return pling
    elif (number % 5 == 0 and number % 7 == 0):
        return (plang+plong)
    elif number % 5 == 0:
        return plang
    elif number % 7 == 0:
        return plong
    else:
        return str(number)
