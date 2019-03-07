def fibonacci(nterms):
    '''Prints the Fibonacci sequence to the given nth term'''
    n1 = 0
    n2 = 1
    nextVal = 0
    for terms in range(0, nterms):
        if terms == 0:
            print(n1)
        elif terms == 1:
            print(n2)
        else:
            nextVal = n1 + n2
            n1 = n2
            n2 = nextVal
            print(nextVal)

      
def alliteration_check(aString):
    '''Checks to see if all words in a string begin with the same letter'''
    aString = aString.lower().replace(',', '').strip()
    wordList = aString.split(" ")
    prefix = wordList[0][0]
    for word in wordList:
        if word[0] != prefix:
            return False
    return True
