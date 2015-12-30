f = open("names2.txt")
names = f.read().split(",")

start = True
grandTotal = 0
localString = ""
commaCounter = []
localNumber = 0




# You have to sort this alphabetically first 


for i in range(0,len(names)):
    for j in range(0,len(names[i])):          
        #if names[i][j] != '"':

        localNumber = localNumber + ord(names[i][j])- 64

    localNumber = localNumber + 1
    localNumber = localNumber * i

    grandTotal = grandTotal + localNumber
    localNumber = 0
                   

    
print(grandTotal)
