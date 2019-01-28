#Exercise 1
def simpleInterest(start, years, rate):
    #convert rate to a percent
    rate = rate / 100
    # Equation: A = P(1+rt)
    return (start*(1 + (years * rate)))


#Exercise 2
def minCoins(amount):
    runTot = 100*amount
    
    # create variable placeholders in case if statements aren't used
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    # if we have more than a quarter...
    if runTot >= 25:
        # find number of quarters
        quarters = (runTot // 25)  
        # could also use -= here
        runTot = runTot - (quarters * 25)

    # if we have more than a dime
    if runTot >= 10:
        # find number of dimes. could also use += here
        dimes = (runTot // 10)
        runTot = runTot - (dimes * 10)
    
    # if we have more than a nickel
    if runTot >= 5:
        # find number of nickels. could also use += here
        nickels = (runTot // 5)
        runTot = runTot - (nickels * 5)

    if runTot >= 1:
        # find number of pennies. could also use += here
        pennies = (runTot / 1)
        runTot = runTot - (pennies * 1)
    
    coins = quarters + dimes + nickels + pennies
    return int(coins)
        
