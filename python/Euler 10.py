check = False
total= 0
primes = [2]

for x in range(3, 2000000 + 1, 2):
    for y in range(0,len(primes)):

        if primes[y]>x**.5:
                break
        if x % primes[y] == 0:
            check = True
            break
            
    if check == False:
        primes.append(x)
        total = total + x
            
    check = False

print (total + 2)
