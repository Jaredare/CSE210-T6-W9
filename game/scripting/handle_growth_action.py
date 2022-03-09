from game.scripting.action import Action
# from game.casting.cycle import cycle

class HandleGrowthAction(Action):
    
    def __init__(self):
        self.game_timer = 0

    def execute(self, cast, script):
        self.game_timer += 1

        game_over = cast.get_first_actor("messages")
        print(game_over)
        
        # The growth of the cycles is determined by this value. 1 = every frame, 2 = every other frame, 15 = every second, 30 = every other second, etc.
        #                    V
        if self.game_timer % 5 == 0 and game_over == None:
            cycles = cast.get_actors("cycles")

            cycle1 = cycles[0]
            cycle2 = cycles[1]

            cycle1.grow_tail(1)
            cycle2.grow_tail(1)

