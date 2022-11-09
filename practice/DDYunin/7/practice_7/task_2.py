import timeit

def test1(input_str: str):
    splits = []
    for char in (' ', ',', ';', ':', '.', '-', '_'):
         splits.append(input_str.split(char))
    return splits

def test2(input_str: str):
    splits = []
    append = splits.append
    split = input_str.split
    for char in (' ', ',', ';', ':', '.', '-', '_'):
         append(split(char))
    return splits