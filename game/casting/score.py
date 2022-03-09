from game.casting.actor import Actor
from game.shared import constants as constants
from game.shared.point import Point
from game.casting.cast import Cast


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, player):
        super().__init__()
        self._points = 0
        self.add_points(0, player)
        

    def add_points(self, points, player):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Player {player}: {self._points}")

    def prepare_score(self, score):
        """Prepares the body of the score"""
        cast = Cast()
        # scores = cast.get_actors("scores")

        # score1 = scores[0]
        # score2 = scores[1]

        print("Preparing score")

        if score == "One":
            """This is for the first player's score. """
            score = Score("One")
            x = int(constants.MAX_X / 4 * 1)
            y = int(constants.MAX_Y)
        
        elif score == "Two":
            """This is for the second player's score. """
            score = Score("Two")
            x = int(constants.MAX_X / 4 * 3)
            y = int(constants.MAX_Y / 4)
        
        else:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
        
        position = Point(x, y)
        Score.set_position(position)
            
        