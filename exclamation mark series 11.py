def replace_exclamation(s):
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        s = s.replace(vowel, '!')
    return s
