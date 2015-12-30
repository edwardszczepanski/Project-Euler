total = 1

for x in range(1, 1000 +1):
    total = total * 2
#print(total)

string = str(total)

total = 0
# we are going to reuse total 
for x in range(0, len(string)):
    total = total + int(string[x])

print(total)

