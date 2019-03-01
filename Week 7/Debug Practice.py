from random import choice

# Rock Paper Scissors that is played in multiple rounds
def rps():

    # Counters that are used throughout the program
    gamesPlayed = 0
    playerWins = 0
    compWins = 0
    choices = ['rock', 'paper', 'scissors']

    # Determine the minimum number of loops we're going to do
    print("You may play any odd number of games less than 10")
    numGames = int(input("Please enter the number of games you'd like to play: "))
    print("\n")

    # Verify that the user is giving us a valid input
    while int(numGames) not in range(1,10,2):
        print("You may play any odd number of games less than 10")
        numGames = int(input("Please enter the number of games you'd like to play: "))
        print("\n")

    # Begin looping 
    while gamesPlayed < numGames:
        playerChoice = input("What do you choose:  ")
        
        # Again, verify the user is giving a valid input
        while playerChoice not in choices:
            print("Please enter Rock, Paper, or Scissors\n")
            playerChoice = input("What do you choose:  ")
        

        print(f"Player chose {playerChoice}. Computer chose {compChoice}")

        # Begin rock, paper, scissors logic
        if playerChoice != compChoice:

            if playerChoice == choices[0]:
                if compChoice == choices[1]:
                    print("You lose this round")
                    compWins += 1
                else:
                    print("You win this round")
                    playerWins += 1

            if playerChoice == choices[1]:
                if compChoice == choices[2]:
                    print("You lose this round")
                    compWins += 1
                else:
                    print("You win this round")
                    playerWins += 1

            if playerChoice == choices[2]:
                if compChoice == choices[0]:
                    print("You lose this round")
                    compWins += 1
                else:
                    print("You win this round")
                    playerWins += 1

            # Increase the number of games played if we didn't end in a draw

        else:
            print("Draw")
        
        print(f"You have {playerWins} wins, the computer has {compWins}\n")
        gamesPlayed += 1

    # Determine overall outcome
    if playerWins > compWins:
        print(f"You beat the computer, {playerWins} to {compWins}")
    
    else:
        print(f"The computer beat you, {compWins} to {playerWins}")

    print("Game Over")


'''
This function could (and probably should) be split up into about 5 other
functions as to make it easier to follow what's going and to follow
the DRY mantra better
'''
rps()
