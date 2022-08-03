def is_armstrong_number(number):
    number_str = str(number)
    result = sum([int(i)**len(number_str) for i in number_str])
    return result == number
