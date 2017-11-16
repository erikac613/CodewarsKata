def band_name_generator(name):
    if name[0] == name[-1]:
        band_name = (name[:-1] + name).title()
        return band_name
    else:
        return "The " + name.title()
