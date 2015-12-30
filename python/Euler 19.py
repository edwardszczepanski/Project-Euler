masterCounter = 0 # + 1 if Sunday is First day of the Month
dayCounter = 2


def printDate(): # this was just for debugging
    if dayCounter % 7 == 0:
        print("Sunday")
    if dayCounter % 7 == 1:
        print("Monday")
    if dayCounter % 7 == 2:
        print("Tuesday")
    if dayCounter % 7 == 3:
        print("Wednesday")
    if dayCounter % 7 == 4:
        print("Thursday")
    if dayCounter % 7 == 5:
        print("Friday")
    elif dayCounter % 7 == 6:
        print("Saturday")
    
    print(k + 1) # This is the Date
    print(j + 1) # This is the Month
    print(i + 1900)


for i in range(1,100 + 1):
    print(i)
    #print("New Year!!!")
    for j in range(0,12):
        if j == 8 or j == 3 or j == 5 or j == 10:
            for k in range(0,30):
                #printDate()
                #input("***")
                if k == 0 and dayCounter % 7 == 0:
                    masterCounter = masterCounter + 1
                    
                dayCounter = dayCounter + 1
        elif j == 1:
            if i % 4 == 0 and i != 100:
                for k in range(0,29):
                    #printDate()
                    #input("***")
                    if k == 0 and dayCounter % 7 == 0:
                        masterCounter = masterCounter + 1
                    dayCounter = dayCounter + 1
                    #print("feburary leap year")
            else:
                for k in range(0,28):
                    #printDate()
                    #input("***")
                    if k == 0 and dayCounter % 7 == 0:
                        masterCounter = masterCounter + 1
                    dayCounter = dayCounter + 1
                    #print("feburary")
        else:
            for k in range(0,31):
                #printDate()
                #input("***")
                if k == 0 and dayCounter % 7 == 0:
                    masterCounter = masterCounter + 1
                    
                dayCounter = dayCounter + 1
                #print("everything else")
    print(masterCounter)
    print(dayCounter)
    print("***")
        
print(masterCounter)



