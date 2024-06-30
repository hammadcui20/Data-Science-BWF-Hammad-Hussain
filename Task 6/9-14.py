from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)
six_sided_die = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    print(six_sided_die.roll_die(), end=" ")
ten_sided_die = Die(10)
print("\n\nRolling a 10-sided die 10 times:")
for _ in range(10):
    print(ten_sided_die.roll_die(), end=" ")
twenty_sided_die = Die(20)
print("\n\nRolling a 20-sided die 10 times:")
for _ in range(10):
    print(twenty_sided_die.roll_die(), end=" ")
