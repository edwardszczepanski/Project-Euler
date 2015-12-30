leftSide = 0
rightSide = 0
for x in range(500, 0, -1): # possible c value
    for y in range(500-1, 0, -1): # possible b value
        leftSide = x*x-y*y
        leftSide = leftSide**.5
        rightSide = 1000 - x -y
        if leftSide == rightSide:
            print("b: ")
            print(y)
            print("c: ")
            print(x)
        
