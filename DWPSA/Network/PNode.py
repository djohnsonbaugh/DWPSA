class PNode(object):
    """Pricing Location in a Power System"""


    #Constructor
    def __init__(self, id: int, name: str):
        """PNode Constructor"""

        #Attributes
        self.ID = id
        self.Name = name


    def __repr__(self):
        return "[" + self.ID + "] " + self.Name

    def __str__(self):
        return "[" + self.ID + "] " + self.Name