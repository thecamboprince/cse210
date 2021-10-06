import random

# Assigning class to this file
class Thrower:
    
    def __init__(self):
        # Declares instance attributes
        self.dice = []
        self.num_throws = 0

    def can_throw(self):
        # To determine weather or not Thrower can throw again 
        # Returns: boolean: True if the list of dice has at least a Five, or a One, or the number
        #          of throws is Zero; false if otherwise.
        return (self.dice.count(5) > 0 or self.dice.count(1) > 0
                or self.num_throws == 0)

    def get_points(self):
        # Calculates the total number of points for the current throw.
        # Fives are worth 50 points. Ones are worth 100 points.
        # Returns the number of the total points for the current throw.
        return self.dice.count(5) * 50 + self.dice.count(1) * 100

    def throwdice(self):
        # This function will throw 5 random values
        for i in range(5):
            result = random.randint(1, 6)
            self.dice.append(result)
        self.num_throws += 1