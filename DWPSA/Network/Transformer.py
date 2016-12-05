from Network.Branch import Branch
from Network.RatingSet import RatingSet

class Transformer(Branch):
    """Tranformer Branch Node Connector"""


    def __init__(self, stationid: str, fvoltage: str, fnodename: str, 
                 tvoltage: str, tnodename: str,
                 name: str, owner: str, monitored: bool,
                 r: float = 0, x: float = 0, 
                 summer : RatingSet = None, winter : RatingSet = None,
                 spring : RatingSet = None, fall : RatingSet = None,
                 ftaptype: str = "", fnormtapposition: int = 0, 
                 ttaptype: str = "", tnormtapposition: int = 0, regnodename : str = "", avr: int = 0 ):
        super(Transformer, self).__init__(stationid, fvoltage, fnodename, 
                                          stationid, tvoltage, tnodename,
                                          name, owner, monitored, r, x, name,
                                          summer, winter, spring, fall)
        self.StationID = stationid
        self.FromTapType = ftaptype
        self.FromTapNormPosition = fnormtapposition
        self.ToTapType = ttaptype
        self.ToTapNormPosition = tnormtapposition
        self.RegulationNode = None
        self.RegulationNodeName = regnodename
        self.RegulationNodeID = (stationid, regnodename)
        self.AVRStatus = avr