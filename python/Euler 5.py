check = True

for x in range(12252240, 1000000000000, 2):
    for y in range(11, 20 + 1):
        #input("Press Enter to continue...")
        #print(y)
        if x % y != 0:
            check = False
            break
    if check == True:
        print(x)
        break
    check = True
        
