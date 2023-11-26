def oxford_comma(items):
    if len(items) == 2:
        return ' and '.join(items)
    if len(items) >= 3:
        first_strings = ', '.join(items[:-1])
        return ', and '.join([first_strings, items[-1]])
    return ''.join(items)
