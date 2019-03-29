def palindrome(word):
    word = word.lower().replace(' ', '').replace(',', '').replace("'", '')
    forward = 0
    backward = -1
    for count in range(len(word)):
        if word[forward] != word[backward]:
            return False
        forward += 1
        backward -= 1
    return True
    
