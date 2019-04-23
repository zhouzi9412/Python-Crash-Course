class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(self.first_name.title() + self.last_name.title())
    def greet_user(self):
        print("Dear " + self.first_name.title() + self.last_name.title() + ", Good morning!")

user_1 = User('benjumin', 'frinckin')
user_2 = User('micheal', 'jackson')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
