from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

def roll_dice(die, rolls=10):
    results = [die.roll_die() for _ in range(rolls)]
    return results
