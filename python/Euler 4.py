palindrome = "Leggo"
number1 = 999
number2 = 999
check = True
endProgram = False

for x in range(1000000, 0, -1):
    palindrome = str(x)
    if palindrome[0] != palindrome[5]:
        check = False
    if palindrome[1] != palindrome[4]:
        check = False
    if palindrome[2] != palindrome[3]:
        check = False
    if check == True:
        for y in range(999, 500, -1):
            for z in range(999, 500, -1):
                if y*z == x:
                    print(x)
                    endProgram = True
    if endProgram == True:
        break
    check = True
    
