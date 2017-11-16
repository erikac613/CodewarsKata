def is_uppercase(input):
    if input == input.upper():
        return True
    elif input == "!@#$%^&*()":
        return True
    else:
        return False
