from math import * 

#Calculates the length of the hypotenuse of a right triangle, given the length 
# of two sides
def pythag_one(sideOne, sideTwo):
    return sqrt((sideOne**2 + sideTwo**2))

#Calculates the length of a missing side of a right triangle, given the length
# of the hypotenuse and another side
def missing_side(hypotenuse, side):
    return sqrt((hypotenuse**2 - side**2))

def kilo_to_stones(kilos):
    return (kilos * 2.2 / 14)

def is_even(num):
    return (num % 2 == 0)

def pythag_two(side, angle):
    return side / sin(angle)
