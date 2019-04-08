prompt = "\nPlease input pizza ingredient: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print("We will add " + message.title())
    