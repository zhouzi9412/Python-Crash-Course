use_names = []
if use_names:
    for use_name in use_names:
        if use_name == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("hello Eric,thank you for logging in again.")
else:
    print("We need to find some users!")
