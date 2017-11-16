import re
def replace_dots(str):
    if "." in str:
        no_dots = str.replace(".", "-")
        return no_dots
    else:
        return str
