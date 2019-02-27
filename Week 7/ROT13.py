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


print('This is a test string.')
print(ROT13('This is a test string.'))
        
        

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
            itter += 1
        else:
            retWord += letter
            itter += 1
    return retWord


print(ROT13_while('This is a test string.'))



# Rock Paper Scissors with a main menu

def rps():
    print("You may play any odd number of games less than 10")
    numGames = input("Please enter the number of games you'd like to play")
    while numGames not in range(1,10,2):
        print("You may play any odd number of games less than 10")
        numGames = input("Please enter the number of games you'd like to play")
    pass
        
