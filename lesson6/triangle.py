def isvalid(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == 0 or b == 0 or c == 0:
        return False
    elif a + b <= c or a + c <= b or b + c <= a:
        return False
    return True
            
def equilateral(sides):
    if not isvalid(sides):
        return False
    sides = set(sides)
    if len(sides) == 1:
        return True
    return False
        
def isosceles(sides):
    if not isvalid(sides):
        return False
    sides = set(sides)
    if len(sides) <= 2:
        return True
    return False
    
def scalene(sides):
    if not isvalid(sides):
        return False
    sides = set(sides)
    if len(sides) == 3:
        return True
    return False