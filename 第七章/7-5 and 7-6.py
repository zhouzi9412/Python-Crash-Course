prompt = "\nPlease input your age. "
prompt += "\nEnter 'quit' to end the program."
message = ""
while True:
    message = input(prompt)
    if message == 'quit':
        break
    message = int(message)
    if message < 3:
        print("You can enter free.")
    elif message < 12:
        print("Your ticket price is 10 dollars.")
    else:
        print("Your ticket price is 15 dollars.")

