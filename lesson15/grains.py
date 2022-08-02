def square(number):
    if not 0 < number < 65:
        raise ValueError("square must be between 1 and 64")
    if 0 < number < 65:    
        number = 2**(number-1)
        return (number)
def total(number=64):
    number = 2**number-1
    return number
