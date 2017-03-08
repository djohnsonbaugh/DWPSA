from enum import Enum
from Network.NodeConnector import NodeConnector
from Network.RatingSet import RatingSet

class Branch(NodeConnector):
    """Branch Node Connector"""

    def __init__(self, fstationid: str, fvoltage: str, fnodename: str, 
                 tstationid: str, tvoltage: str, tnodename: str,
                 name: str, owner: str, monitored: bool,
                 r: float = 0.0, x: float = 0.0, segment: str = "",
                 summer : RatingSet = None, winter : RatingSet = None,
                 spring : RatingSet = None, fall : RatingSet = None):
        super(Branch, self).__init__(fstationid, fvoltage, fnodename, 
                                             tstationid, tvoltage, tnodename, 
                                             name, owner, r, x, segment)

        self.Monitored = monitored
        self.SuRating = summer
        self.WiRating = winter
        self.SpRating = spring
        self.FaRating = fall

    def __repr__(self):
        return "{BR} " + self.FromStationID + "->" + self.ToStationID + " " + self.FromVoltage + " [" + self.Name + " " + self.Segment + "]"

    def __str__(self):
        return "{BR} " + self.FromStationID + "->" + self.ToStationID + " " + self.FromVoltage + " [" + self.Name + " " + self.Segment + "]"

    def GetVariableName(self):
        return "Tr_{0}__{1}__{2}".format(
            self.ID[0].replace("-","_d_"), 
            self.ID[1].replace("-","_d_"),
            self.ID[2].replace("-","_d_")
            )