
gridHeight = 20 + 1

array = [[0 for x in range(gridHeight + 1)] for x in range(gridHeight - 1)]

#array[2][3] = 666

for x in range(0, gridHeight + 1):
    array[0][x] = 1
for x in range(0,gridHeight -1):
    array[x][0] = 1

for x in range(1, gridHeight - 1):
    for y in range(1,gridHeight):
        array[x][y] = array[x-1][y] + array[x][y-1]


total = 0
for x in range(gridHeight + 1):
    total = total + array[gridHeight-2][x]


print(total)
print("hey")


