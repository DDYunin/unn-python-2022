def disemvowel(string_):
    alphabet = ('a', 'e', 'u', 'i', 'o', 'A', 'E', 'U', 'I', 'O')
    result_string = ""
    for word in string_:
        if word in alphabet:
            continue
        result_string += word
    return result_string

_str = "This website is for losers LOL!"
print(disemvowel(_str))