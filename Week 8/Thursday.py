def alphabetize(aList):
    '''Alphabetizes a list of strings using the bubble sort algorithm.
    There are definitely better ways to go about this but this does the
    trick for now'''
    listLength = len(aList)
    for iteration in range(listLength):
        for item in enumerate(aList):
            currentSpot = item[0]
            if currentSpot < (listLength - 1):
                nextSpot = currentSpot + 1
                if item[1] > aList[nextSpot]:
                    temp = aList[nextSpot]
                    aList[nextSpot] = item[1]
                    aList[currentSpot] = temp
    return aList


def min(aList):
    retNum = aList[0]
    for number in aList:
        if number < retNum:
            retNum = number
    return retNum
