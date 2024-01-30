from dragon import Dragon
class IceDragon(Dragon):
    def __init__(self, name, image):
        # inherits dragons class
        super().__init__(name, image)
    # returns false since its a ice dragon
    def can_breathe_fire(self):
        return False