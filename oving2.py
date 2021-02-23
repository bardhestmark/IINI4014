import math

def estimateArchimedesPi(iter = 100):

    numberOfSides = 6
    sideLength = 1

    for i in range(iter):
        halfSide = sideLength/2
        a = math.sqrt(1-math.pow(halfSide, 2))
        b = 1 - a
        newSide = math.sqrt(math.pow(b, 2) + math.pow(halfSide, 2))
        p = numberOfSides * sideLength

        PI = p/2

        numberOfSides *= 2
        sideLength = newSide
    return PI

print(estimateArchimedesPi(100))