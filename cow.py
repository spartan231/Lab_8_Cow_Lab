class Cow:
    # initalize the cow class
    def __init__(self, name):
        # sets name
        self.name = name
        # sets default image to None
        self.image = None

    # gets the cow name
    def get_name(self):
        return self.name

    # gets the image
    def get_image(self):
        return self.image

    # sets the image
    def set_image(self, image):
        self.image = image