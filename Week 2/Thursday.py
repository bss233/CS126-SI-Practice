# Returns true if a number is odd, else, returns false
def isOdd(num):
    return num % 2 > 0


# Takes in the price of a meal and a score from 1 to 10
# If the score is 7 or greater, it adds a 25% tip
# If the score is less than 7 but greater than or equal to 5, it adds a 20% tip
# Else, if the score is less than 5, it adds a 15% tip
# Returns the cost of the meal, including tip, as a float, rounded to 2 decimals
def tipCalc(price, score):
    if score >= 8:
        cost = price * 1.25
    elif score >= 5:
        cost = price * 1.20
    else:
        cost = price * 1.15
    return round(cost, 2)

