from asyncio.windows_events import NULL


def to_camel_case(text):
    _str = text.replace("_", "-")
    temp = _str.split('-')
    lst = []
    for i, item in enumerate(temp):
        if i == 0:
            lst.append(item)
            continue
        lst.append(item.title())
    str_temp = "".join(lst)
    return str_temp


_str = "the_Stealth-Warrior"
to_camel_case(_str)