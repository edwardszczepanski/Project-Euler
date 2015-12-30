amicableSum = []
sum = 0

ANSWER = 0


for counter in range(0,10000):
    sum = 0
    for i in range(1,round(counter / 2 + 1)):
        if counter % i == 0:
            sum = sum + i
    amicableSum.append(sum)



# so know we have an array of a shit ton of factors

# counter should be set at 10000 now

for i in range(10000 - 2, 280, -1):
    for j in range(i - 1, 0, -1):
        #if i == 284 and j == 220:
            #print(amicableSum[i])
            #print(amicableSum[j])
        
        if amicableSum[i] == j:
            if amicableSum[j] == i:
                ANSWER = ANSWER + i + j
                print(i)
                print(j)
                print("***")
                break
print(ANSWER)
