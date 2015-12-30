numberString = [9,8,2]
holderNumber = -1



for i in range(0, len(numberString) - 1):
    for j in range(i, len(numberString) - 1):
        if numberString[j] > numberString[j+1]:
            holderNumber = numberString[j+1]
            numberString[j+1] = numberString[j]
            numberString[j] = holderNumber
        else:
            break


print("ayy")
for i in range(0, len(numberString)):
    print(numberString[i])
