def remove_vowel(txt):
    vowels = 'aeiouAEIOU'
    for i in vowels:
        txt = txt.replace(i, '')
    return txt


print(duplicate_count("We're gonna build a wall!"))
