print("If you want to quit, Please input quit.")
active =True
while active:
    reason = input("Why do you like programming? ")
    if reason =='quit':
        active = False
    else:
        filename = 'reason_why.txt'
        with open(filename, 'a') as file_object:
            file_object.write(reason.title() + "\n")

