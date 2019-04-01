####使用循环####
current_number = 1
while current_number <= 5:                ###只要满足此条件，就接着执行此循环####
    print(current_number)
    current_number += 1

####游戏在玩家想玩时玩，想停止时停止就依赖这个循环####

####让用户选择何时退出####

prompt = "\ntell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""                                                      ####message是一个空字符串，等待用户输入####
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

####使用标志####

prompt = "\ntell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True                                                    ####active 设置成了true,则其一直处于活动状态####
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

####使用break推出循环####

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\nEnter 'quit' when you are finishied. "
while True:
    city = input(prompt)
    if city == 'quit':
        break                                               ####不再执行剩下的代码，并退出整个循环####
    else:
        print("I'd love to go to " + city.title() + "!") 

####在循环中使用continue####

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue                                            ####不再执行剩下代码并执行新的循环####
    print(current_number)

####避免无限循环####ctrl + c中断无限循环
