check = False

x = 2

primeList = []
factors = 1
first = True


total = 0

counter = 1

realTotal = 0

while factors < 500:
    realTotal = realTotal + counter
    total = realTotal
    print(total)

    factors = 1
    primeList = []
    x = 2
    first = True
    while total > 1:
        for y in range(2,x):
            if x % y == 0:
                check = True
                
        if check == False:
     
            while total % x == 0:
                #print(x)
                if first == True:
                    primeList.append(1)
                    first = False
                else:
                    primeList[len(primeList)- 1] = primeList[len(primeList) - 1] + 1
                    
                total = total / x
            first = True

            
                
        check = False
        x = x + 1

    for z in range (0, len(primeList)):
        factors = factors * (primeList[z] + 1)
        
    
    print(factors)
    print("*****")

    #input("eiarntei")


    

    counter = counter + 1








