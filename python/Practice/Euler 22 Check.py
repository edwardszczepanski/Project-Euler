nameString = [5,4,7]
#insertion sort yo 

#nameString = nameString.split(",")

currentPiece = ""
holderSpot = ""

#print(len(nameString))
for i in range(len(nameString) - 1, -1, -1):
    currentPiece = nameString[i]
    for j in range(i, -1, -1):
        if nameString[i] < nameString[i-1]:
            #print("ay")
            holderSpot = nameString[i-1]
            nameString[i-1] = nameString[i]
            nameString[i] = holderSpot
        else:
            break 
        #Check to see if it is alphabetical
            # if so then switch
            # if not break

for i in range(0, len(nameString)):
    print(nameString[i])
#print(nameString[3])
