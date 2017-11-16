def how_many_dalmatians(dogs):
    response = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];

    if dogs <= 10:
        return response[0]
    elif dogs <= 50:
        return response[1]
    elif dogs == 101:
        return response[3]
    else:
        return response[2]
