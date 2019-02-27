def remove_vowels(word):

    retWord = word

    if 'a' in  retWord:
        retWord = retWord.replace('a', '') 
    if 'e' in retWord:
        retWord = retWord.replace('e', '') 
    if 'i' in retWord:
        retWord = retWord.replace('i', '') 
    if 'o' in retWord:
        retWord = retWord.replace('o', '') 
    if 'u' in retWord:
        retWord = retWord.replace('u', '') 
    if 'y' in retWord:
        retWord = retWord.replace('y', '') 
    return retWord

