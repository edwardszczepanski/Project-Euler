#number = 13
counter = 0


answer = 0
highScore = 1 

for x in range(999999,0,-2):
    number = x
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        counter = counter + 1

    if counter > highScore:
        highScore = counter
        answer = x
    print(answer)
    print(highScore + 1)

    counter = 0

    
print("*****")
print(answer)

# the answer ends up being 837799 but it takes a shitload of time to generate it 



