"""
move_actors_action.py
This class is a simple child of the Action class which moves the actors in the cast.

for cse210 w05
by Alexander Turner
"""


from game.scripting.action import Action


class MoveActorsAction(Action):
    """
    This is the child of the action class, which moves actors in the cast.
    """
    def __init__(self):
        """
        Initializes the superclass.
        """
        super().__init__() 

    def execute(self, cast, script):
        """
        Loops through the acotrs in our cast and calls the move_next function of each.
        """
        for actor in cast.get_all_actors():
            actor.move_next()