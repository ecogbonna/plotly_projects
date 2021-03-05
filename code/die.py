from random import randint

class Die():
    """Class to simulate a die"""
    def __init__(self, num_sides=6):
        """Assume a six-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value form 1 and number of sides"""
        return randint(1, self.num_sides)
