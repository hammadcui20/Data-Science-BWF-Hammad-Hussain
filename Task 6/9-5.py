class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("Hammad", "Hussain", 23, "hammad.hussain@gmail.com", "Pakistan")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")
