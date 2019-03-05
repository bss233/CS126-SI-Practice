#Converts a number less than or equal to 10, to a roman numeral
#NOTE: You normally shouldn't manipulate your input, ie how I subtract from num,
# but it saves some extra checking. There is most certainly a cleaner way to do
# this function
def romanNumeral(num):
    #define an empty string to add characters to
    result = ''

    #if num is 10, then the roman numeral is X
    if num == 10:
        result += 'X'
        num -= 10

    #if the num is greater than or equal to 5, add V to the string then subtract
    # 5 so that we can just use our other 4 comparisons
    elif num >= 5:
        result += 'V'
        num -= 5

    #as long as our num isn't 0, meaning it wasn't originally 5, we add more to
    # our return string
    if num > 0:

        #check if it's 1
        if num == 1:
            result += 'I'

        #check if it's 2
        elif num == 2:
            result += 'II'

        #check if it's 3
        elif num == 3:
            result += 'III'

        #check if it's 4
        else:
            result = 'I' + result
    
    #return out finished string
    return result


#Returns true or false based on whether or not a given year is a leap year
def isLeapYear(year):
    #set initial status so that we only use 1 return statement
    status = False
    #check if the year is divisible by 400
    if year % 400 == 0:
        status = True
    #check if the year is divisible by 4
    elif year % 4 == 0:
        #if the year is divisible by 4, make sure it isn't divisible by 100
        if year % 100 != 0:
            status = True
    #return the status
    return status


#Tests
print(romanNumeral(10)) #should print X
print(romanNumeral(4))  #should print IV
print(romanNumeral(7))  #should print VII
print(romanNumeral(5))  #should print V
print(romanNumeral(9))  #should print IX

print(isLeapYear(2006)) #should print False
print(isLeapYear(2000)) #should print True
print(isLeapYear(2016)) #should print True
print(isLeapYear(2100)) #should print False

