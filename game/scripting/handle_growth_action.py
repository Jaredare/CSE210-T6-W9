from game.scripting.action import Action
# from game.casting.cycle import cycle

class HandleGrowthAction(Action):
    
    def __init__(self):
        self.game_timer = 0

    def execute(self, cast, script):
        self.game_timer += 1
        
        if self.game_timer % 2 == 0:
            cycles = cast.get_actors("cycles")

            cycle1 = cycles[0]
            cycle2 = cycles[1]

            cycle1.grow_tail(1)
            cycle2.grow_tail(1)

