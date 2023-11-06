class Cow:
    def __init__(self, name):
        # set self.name to be name
        self.name = name
        self.image = None


    def get_name (self):
        # retrieve the attribute self.name
        return self.name

    def get_image(self):
        # retrieve the attribute self.image
        return self.image

    def set_image(self, image):
        # set the self.image to be image
        self.image = image