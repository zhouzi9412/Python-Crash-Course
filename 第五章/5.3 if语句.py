

age = 19
if age >=18:
    print("You are old enough to vote!")

###### if-else语句

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

###### if-elif-else语句

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:                              ##此处elif代码行为另一个if测试，仅在前面的测试未通过时才可运行##
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

####使上面代码更加简洁####

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

######使用多个elif代码块####

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

####省略else代码块####

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

####测试多个条件####有多个条件为true,且需要每个条件为True时都采取相应措施

requested_toppings = ['mushroom','extra cheese']
if 'mushroom' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:        ##不管之前的测试通没通过，都进行这个测试##
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
    
####




