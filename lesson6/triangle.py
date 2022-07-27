def isvalid(sides):
    a, b, c = sides  # it's a = sides[0], b = sides[1] and c = sides[2]
    if a == 0 or b == 0 or c == 0:
        return False
    elif a + b <= c or a + c <= b or b + c <= a:
        return False
    return True
            
def equilateral(sides):
    if not isvalid(sides):
        return False
    sides = set(sides)
    return len(sides) == 1  # it's already return Bool value
        
def isosceles(sides):
    if not isvalid(sides):
        return False
    sides = set(sides)
    return len(sides) <= 2   # it's already return Bool value
    
def scalene(sides):
    if not isvalid(sides):
        return False
    sides = set(sides)
    return len(sides) == 3   # it's already return Bool value