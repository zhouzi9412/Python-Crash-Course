
while True:
    number1 = input("Please input first number:")
    if number1 == 'q':
        break
    number2 = input("Please input second number:")
    try:
        num = int(number1) + int(number2)
    except ValueError:
        print("Your number is wrong!")
    else:
        print(num)