from cow import Cow
class Dragon(Cow):
    def __init__(self, name, image):
        # inherits the name of the cow class
        super().__init__(name)
        # sets the self.image to image
        self.image = image

    # returns true because the dragon can
    def can_breathe_fire(self):
        return True