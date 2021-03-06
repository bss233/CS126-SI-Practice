# A ROT13 cypher generator
''' 
Converts a given string to a string encrypted in ROT13.
ROT13 moves any alphabetic character 13 places to the right.
Ex) A -> N
If a letter would go past Z, it wraps back around
Ex) O -> B
Hint : The ord() and chr() functions could prove to be helpful
Hint : using the .isalpha() method could also prove helpful
'''
def ROT13 (word):
    retWord = ''
    word = word.lower()
    for letter in word:
        if letter.isalpha():
            wordNum = ord(letter)
            newNum = wordNum + 13
            if newNum > 122:
                newNum -= 26 
            rotLetter = chr(newNum)
            retWord += rotLetter
        else:
            retWord += letter
    return retWord


print("I don't know...")
print(ROT13("I don't know..."))
        
        

# Same function as above, just using a while loop
# definitely could improve the logic inside the loop
def ROT13_while (word):
    retWord = ''
    word = word.lower()
    wordLen = len(word)
    itter = 0
    while itter < wordLen:
        letter = word[itter]
        if letter.isalpha():
            wordNum = ord(letter)
            newNum = wordNum + 13
            if newNum > 122:
                newNum -= 26 
            rotLetter = chr(newNum)
            retWord += rotLetter
        else:
            retWord += letter
        itter += 1
    return retWord


print(ROT13_while('This is a test string.'))

        
