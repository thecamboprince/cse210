from thegame.thrower import Thrower

class Director:

    def  __init__(self):
        self.keep_playing = True
        self.score = 0
        self.thrower = Thrower()

    def startgame(self):
        # Starts the game loop to control the sequence of play
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        # gets the inputs at the beginning of each round of play
        # In this case, it means throwing the dice
        self.thrower.throwdice()

    def do_updates(self):
        # Updates the important game information for each round of play. In 
        #         this case, that means updating the score.
        
        points = self.thrower.get_points()
        self.score += points

    def do_outputs(self):
        # Outputs the important game information for each round of play. In 
        #      this case, that means the dice that were rolled and the score.
        
        print(f"\nYou rolled: {self.thrower.dice}")
        print(f"Your score is: {self.score}")
        if self.thrower.can_throw():
            choice = input("Roll again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False