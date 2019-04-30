class User():
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + self.last_name.title() + str(self.login_attempts()))

    def greet_user(self):
        print("Dear " + self.first_name.title() + self.last_name.title() + ", Good morning!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('benjumin', 'franklin', 3)
user.increment_login_attempts()
user.describe_user()