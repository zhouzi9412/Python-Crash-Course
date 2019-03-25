numbers = list(range(1,10))
for number in numbers:
    if number < 2:
        print("1st")
    elif number < 3:
        print("2nd")
    elif number < 4:
        print("3rd")
    else:
        print(str(number) + "th")