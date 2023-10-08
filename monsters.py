class Monster():
    """Base class for creating monsters"""

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def __str__(self):
        #return self.name + " pos= " + str(self.pos) + " c= " + self.colour
        return self.name + " c= " + self.colour
    
