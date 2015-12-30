total = 1
valueSum = 0
for i in range (1,101):
    total = total * i

print(total)

character = str(total)

for i in range(0, len(character)):
    valueSum = valueSum + int(character[i])

print(valueSum)


#648?
