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
        self.privileges = []

    def show_privileges(self):
        for privilege in self.privileges:
            print("-" + privilege.title())

admin_user = Admin('Bnjamin', 'Joe')
admin_user.privileges = ['can add post', 'can delete post', 'can ban user']
admin_user.show_privileges()
