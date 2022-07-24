def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == 0 or b == 0 or c == 0:
        return False
    elif a == b and b == c:
        return True
    return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == 0 or b == 0 or c == 0:
        return False
    elif a + b <= c or a + c <= b or b + c <= a:
        return False
    if a == b or a == c or b == c:
        return True
    return False

def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == 0 or b == 0 or c == 0:
        return False
    elif a + b <= c or a + c <= b or b + c <= a:
        return False
    elif a != b and a != c and b != c:
        return True
    return False