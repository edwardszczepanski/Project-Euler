value = 0

for x in range (1,1000):
    string = str(x)
    valueOne = 0
    valueTwo = 0
    valueThree = 0

    if len(string) == 1:
        string = "00" + string
    if len(string) == 2:
        string = "0" + string

    valueOne = string[0]
    valueTwo = string[1]
    valueThree = string[2]


    if(valueTwo == "1"):# here is 10-19
        #print("teens!")
        if(valueThree == "0"): #10
            value = value + 3
        if(valueThree == "1"): #11
            value = value + 6
        if(valueThree == "2"):
            value = value + 6
        if(valueThree == "3"):
            value = value + 8
        if(valueThree == "4"):
            value = value + 8
        if(valueThree == "5"):
            value = value + 7
        if(valueThree == "6"):
            value = value + 7
        if(valueThree == "7"):
            value = value + 9
        if(valueThree == "8"):
            value = value + 8
        if(valueThree == "9"):
            value = value + 8
    else:
        # Here are the one values 
        if valueThree == "1":
            value = value + 3
        elif valueThree == "2":
            value = value + 3
        elif valueThree == "3":
            value = value + 5
        elif valueThree == "4":
            value = value + 4
        elif valueThree == "5":
            value = value + 4
        elif valueThree == "6":
            value = value + 3
        elif valueThree == "7":
            value = value + 5
        elif valueThree == "8":
            value = value + 5
        elif valueThree == "9":
            value = value + 4

        #Here are the ten digits 
        if valueTwo == "2":
            value = value + 6
        elif valueTwo == "3":
            value = value + 6
        elif valueTwo == "4":
            value = value + 5
        elif valueTwo == "5":
            value = value + 5
        elif valueTwo == "6":
            value = value + 5
        elif valueTwo == "7":
            value = value + 7
        elif valueTwo == "8":
            value = value + 6
        elif valueTwo == "9":
            value = value + 5

    
    if valueOne != "0":
        if valueTwo != 0 and valueThree != 0:
            value = value + 3 # This is accounting for "And"
        value = value + 7 # this is for "hundred"

        if valueOne == "1":
            value = value + 3
        elif valueOne == "2":
            value = value + 2
        elif valueOne == "3":
            value = value + 5
        elif valueOne == "4":
            value = value + 4
        elif valueOne == "5":
            value = value + 4
        elif valueOne == "6":
            value = value + 3
        elif valueOne == "7":
            value = value + 5
        elif valueOne == "8":
            value = value + 5
        elif valueOne == "9":
            value = value + 4
        
        

  
    print(x)
    print(value)
    #value = 0
    
    #input("Press Enter")


    
