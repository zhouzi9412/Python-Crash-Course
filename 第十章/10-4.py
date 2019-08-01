active = True
while active:
    name = input("\nWhat's your name? ")
    filename ='guest.txt'

    with open(filename, 'a') as file_object:
        file_object.write(name.title() + "\n")