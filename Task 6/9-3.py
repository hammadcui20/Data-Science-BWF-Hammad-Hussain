class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

user1 = User("Hammad", "Hussain", 28, "hammad.hussain@gmail.com", "Pakistan")
user2 = User("Muhammad", "Farhan", 34, "m.farhan@gmail.com", "Pakistan")
user3 = User("Arham", "Mazhar", 22, "arham.mazhar@gmail.com", "Pakistan")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
