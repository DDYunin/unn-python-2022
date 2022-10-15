def is_valid_walk(walk):
    if len(walk != 10):
        return False
    dictionary = {'n':0, 'w':0, 'e':0, 's':0}
    for item in walk:
        dictionary[item] += 1
    if dictionary['e'] == dictionary['w'] and dictionary['n'] == dictionary['s']:
        return True
    else:
        return False