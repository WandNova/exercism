def is_valid(isbn):
    result = 0
    isbn = list(isbn.replace("-",""))
    if len(isbn) != 10:
        return False
    if isbn[-1] == "X":
        isbn[-1] = "10"
    leni = len(isbn)
    for i in range(leni):
        if not isbn[i].isdigit():
            return False
        result += int(isbn[i]) * (leni - i)
    if result % 11 == 0:
        return True
    return False
