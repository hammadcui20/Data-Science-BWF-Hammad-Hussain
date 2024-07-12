from user_module import User

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, email, location, privileges=[]):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges(privileges)
