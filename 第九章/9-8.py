class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(self.first_name.title() + self.last_name.title())
    def greet_user(self):
        print("Dear " + self.first_name.title() + self.last_name.title() + ", Good morning!")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")

benjamin = Admin('Benjamin', ' Joe')
benjamin.describe_user()
benjamin.privileges.show_privileges()

print("\nAdding privileges...")
benjamin.privileges.privileges = ['can reset password', 
                                'can moderate discussions', 
                                'can suspend accounts'
                                ]
benjamin.privileges.show_privileges()


    