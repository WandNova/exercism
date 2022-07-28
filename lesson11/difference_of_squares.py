def square_of_sum(number, result=0, sum=0):
    for i in range(number,0,-1):
        sum += i
        if i == 1:
            result = (sum**2)
            return (result)

def sum_of_squares(number, result=0, sum=0):
    for i in range(number,0,-1):
        sum += i**2
        if i == 1:
            return (sum)

def difference_of_squares(number):
    return square_of_sum(number, result=0, sum=0)-sum_of_squares(number, result=0, sum=0)
    
