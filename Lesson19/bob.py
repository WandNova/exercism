def response(hey_bob):
    while hey_bob and hey_bob[-1] in [" ", "\n", "\t", "\r"]:
        hey_bob=hey_bob[:-1]
        if hey_bob == "":
            break
    if hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob == "":
        return "Fine. Be that way!"
    if hey_bob[-1] == "?":
        return "Sure."
    return "Whatever."
    