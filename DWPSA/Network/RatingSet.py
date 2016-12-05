class RatingSet(object):
    """description of class"""

    def __init__(self, normal: float = 99999, emergency: float = 99999,  alt : float = 99999):
        self.Normal = normal
        self.Emergency = emergency
        self.Alternate = alt
        return
