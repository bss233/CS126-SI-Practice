def is_vowel(letter):
    """Returns true if a given letter is a vowel, false otherwise."""
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return letter in vowels


def string_cleaner(aString):
    """Returns a sanitized string by removing leading or trailing whitespace
    and changes string to lowercase."""
    return aString.strip().lower()


def find_first_vowel(aString):
    """Returns the index of the first vowel found in a string. If no vowel is
    found, the function returns -1"""
    no_vowel = -1
    for letter in enumerate(aString):
        if is_vowel(letter[1]):
            return letter[0]
    return no_vowel
