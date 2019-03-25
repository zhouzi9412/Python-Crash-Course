current_users = ['admin','host','administration','user','login']
new_users = ['Admin','host','rxrn','cc','zw','boss']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("You need another user name.")
    else:
        print("the user name has not been used.")