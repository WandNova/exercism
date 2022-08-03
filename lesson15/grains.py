def square(number):
    if not 0 < number < 65:
        raise ValueError("square must be between 1 and 64")
    if 0 < number < 65:
        return 2 ** (number - 1)


def total(number=64):
    return 2 ** number - 1
