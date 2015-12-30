total = 0
factorCounter = 0

counter = 1
while total < 999999999:
    factorCounter = 1
    
    total = total + counter

    print(total)
    
    for x in range(1, round(total ** .5)):
        if total % x == 0:
            factorCounter = factorCounter + 1
    print(factorCounter*2)
    if factorCounter >= 250:
        print(total)
        break
    print("***")
    
    counter = counter +1

    
