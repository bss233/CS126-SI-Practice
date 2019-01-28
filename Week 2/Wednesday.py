#Exercise 1
def simpleInterest(start, years, rate):
    #convert rate to a percent
    rate = rate / 100
    # Equation: A = P(1+rt)
    return (start*(1 + (years * rate)))


#Exercise 2
def minCoins(amount):
    wholeNum = int(amount // 1)
    if amount == wholeNum:
        return amount // .25
    else:
        cents = round((amount % 1), 2)
        quarters = wholeNum // .25
        if (cents * 100) % 25 == 0:
            
