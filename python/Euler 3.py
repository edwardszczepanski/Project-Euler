check = False
total = 12

x = 2

primeList = []



first = True

while total > 1:
    for y in range(2,x):
        if x % y == 0:
            check = True
            
    if check == False:
 
        while total % x == 0:
            print(x)
            if first == True:
                primeList.append(x)
            if first == True:
                first = False
                
            total = total / x


        
            
    check = False
    x = x + 1

for z in range (0, len(primeList)):
    print(primeList[z])
