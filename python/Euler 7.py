check = False
primeCounter = 0

for x in range(1, 10000000000,2):
    for y in range(2,x):
        if x % y == 0:
            check = True
            break
    if check == False:
        primeCounter = primeCounter + 1
        if primeCounter == 10001:
            print(x)
            break
            
    check = False

