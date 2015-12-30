# The first goal here is to find all the abundant numbers


sum = 0

for k in range(0, 15000, 2):
    for i in range(1, num(k/2) + 1):
        if k % i == 0:
            sum = sum + i
    if sum > k:
        print(k)
        print(sum)
        print("...")    

    sum = 0

print("done")





