#Math Solver Tool


import math
try:
    print("Welcome to our Math Solver Tool !\n")
    
    first_digit = int(input("Enter first digit: "))
    symbol = input("Enter symbol (+, -, *, /,%,//,**,√): ")
    if symbol != '√':
        second_digit = int(input("Enter second digit: "))
    
    print(f"Your Answer is:\n", end='')
except ValueError:
    print("Invalid input! Please enter valid numbers and symbols.")
    exit()


if symbol == '+':
    print(first_digit + second_digit)
elif symbol == '-':
    print(first_digit - second_digit)
elif symbol == '*':
    print(first_digit * second_digit)
elif symbol == '/':
    if second_digit != 0:
        print(first_digit / second_digit)
    else:
        print("Error! Division by zero.")
elif symbol == '%':
    print(first_digit % second_digit)
elif symbol == '**':
    print(first_digit ** second_digit)
elif symbol == '//':
    if second_digit != 0:
        print(first_digit // second_digit)
    else:
        print("Error! Division by zero.")
elif symbol == '√':
    if first_digit >= 0:
        print(f"√{first_digit} = {math.sqrt(first_digit)}")
    else:
        print("Error! Invalid digit.")

else:
    print("Invalid symbol!")



