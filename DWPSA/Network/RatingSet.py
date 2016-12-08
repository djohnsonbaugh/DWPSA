class RatingSet(object):
    """description of class"""

    def __init__(self, normal: float = 99999.0, emergency: float = 99999.0,  alt : float = 99999.0):
        self.Normal = normal
        self.Emergency = emergency
        self.Alternate = alt
        return
