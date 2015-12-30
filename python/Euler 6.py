squareSum = 0
sumSquared = 0

for x in range(1,101):
    squareSum = squareSum + x
    sumSquared = sumSquared + x * x
squareSum = squareSum * squareSum

print(squareSum)
print(sumSquared)
print(squareSum - sumSquared)
