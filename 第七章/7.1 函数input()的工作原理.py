####input可以获取用户输入，while可以控制程序运行时间，从而可编写出交互式程序####

####函数input()的工作原理####

message = input("Tell me some,and I will repeat it back to you: ")
####input使程序暂停，等待用户输入一些文本，获取输入后，将其存储在一个变量中，方便使用####
print(message)

####使用int()来获取数值输入####

height = input("How tall are you,in inches?")
height = int(height)                                             ####int()将输入转换成了字符表示####
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

####求模运算符####

####%将两个数相除并返回余数####

number = input("Enter a number,and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
