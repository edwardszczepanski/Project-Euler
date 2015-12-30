number1 = 1
number2 = 2
holder = 0
total = 0


while number1 <=4000000:
    print(number1)

    holder = number1 + number2
    if number1 % 2 == 0:
        total = total + number1

    number1 = number2
    number2 = holder

print(total)
