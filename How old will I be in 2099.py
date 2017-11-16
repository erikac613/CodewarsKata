def calculate_age(year_of_birth, current_year):
    not_born_yet = abs(current_year - year_of_birth)
    future_age = abs(current_year - year_of_birth)

    if year_of_birth < current_year:
        if future_age == 1:
            return 'You are ' + str(future_age) + ' year old.'
        else:
            return 'You are ' + str(future_age) + ' years old.'

    if year_of_birth > current_year:
        if not_born_yet == 1:
            return 'You will be born in ' + str(not_born_yet) + ' year.'
        else:
            return 'You will be born in ' + str(not_born_yet) + ' years.'

    else:
        return 'You were born this very year!'
