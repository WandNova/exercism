def translate(text):
    words = text.split(" ")
    vowel_sounds = ["a", "e", "i", "o", "u"]
    result = ""
    for word in words:
        if word[0] in vowel_sounds or word[0:2] in ["xr","yt"]:
            result += word + "ay "
        else:
            if word[1:3] == "qu":
                word = word[3:] + word[0:3]
            elif word[0:2] == "qu":
                word = word[2:] + word[0:2]
            else:
                if word[0] == "y":
                    word = word[1:] + word[0]
                while word[0] not in vowel_sounds and word[0] != "y":
                    word = word[1:] + word[0]
            result += word + "ay "
    return result[0:-1]
    