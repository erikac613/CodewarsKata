def triple_trouble(one, two, three):
    new_string = ""

    for a, b, c in zip(one, two, three):
        new_string = new_string + a + b + c

    return new_string
