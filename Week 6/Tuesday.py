# Program
# A game where we guess a random number between 1-9999

# Input
# Input is a random number, given to us by the user

# Output
# Is it correct number or is it incorrect
   # If incorrect, is it higher or lower
   
# IRL Solution
# Start in the middle and move up or down by half of our previous guess

# Tools (Python)
# Comparison (<, >, <=, >=)
# Boolean evaluation (if, elif, ..., else)
# A way to generate a random number 
    # from random import randint
    # Google Python random doc
    # for i in range()
# While loop (while guess is not the computer's number, keep going)
# Main function
# A way to get input from the user

from random import randint

def checkGuess(correct, guess):
    guess = int(guess)
    correct = int(correct)
    if guess == correct:
        return True
    elif guess < correct:
        print("The correct number is higher")
        return False
    else:
        print("The correct number is lower")
        return False

def validRange(guess):
    guess = int(guess)
    if guess > 9999 or guess < 1:
        return False
    else:
        return True

def isNumber(guess):
    while not guess.isdigit():
        guess = input("Please enter a number: ")
    return guess

def menu():
    print("Welcome to the High-Low game")
    print("Please choose an option: ")
    print("0: Computer guesses number")
    print("1: Player guesses number")
    return input(": ")
    

def computerGuessesNumber():
    correctNumber = randint(1,9999)
    userGuess = input("Please enter a number from 1 to 9999: ")
    isNumber(userGuess)
    while not checkGuess(correctNumber, userGuess):
        userGuess = int(input("Try Again: "))
    print(f"The number was {correctNumber}!")
    print("You won!")

def playerGuessesNumber():
    correctNumber = input("Please choose your number: ") 
    isNumber(correctNumber)
    while not validRange(correctNumber):
        correctNumber = input("The number must be between 1 and 9999: ") 
        isNumber(correctNumber)
    

def main():
    playerGuessesNumber()

 
# make a second mode, where the computer guesses our number
    # make a main menu

if __name__ == "__main__":
    main()

