def steps(number, step=0):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return step
    step += 1
    if number % 2 == 0:
        return steps(number // 2, step)
    return steps(number * 3 + 1, step)
