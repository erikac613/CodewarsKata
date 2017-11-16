def disemvowel(string):
    string = ''.join( c for c in string if c not in 'aeiouAEIOU')
    return string
