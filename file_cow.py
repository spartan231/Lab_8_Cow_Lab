import os

from cow import Cow
class FileCow(Cow):
    def __init__(self, name, filename):
        super().__init__(name) # inheritiets the cow class
        self.filename = filename # sets filename to filename
        """
        try:
            file = open(f'{filename}')
            print(file.read())
        except RuntimeError:
            print("Mooooo!!!!!!")
        """
        self.image = None


    def set_image(self, image):
        try:
            self.image = open(f"{self.filename}") #opens the file
            return self.image.read() # return the image
        except RuntimeError:
            print("Cannot reset FileCow Image") # error if the file can not be read

    def get_image(self):


        #return self.image
        return """        
            .--.
           |o_o |
           |:_/ |
          //   \ \\
         (|     | )
        /'\_   _/`\\
        \___)=(___/
        """

        #return "pass"