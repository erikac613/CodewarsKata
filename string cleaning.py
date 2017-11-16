def string_clean(s):
    """
    Function will return the cleaned string
    """
    for char in '1234567890':
        s = s.replace(char, "")
    return s
