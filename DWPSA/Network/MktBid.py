from enum import Enum
from datetime import datetime

class MktBidType(Enum):
    """Market Bid Types"""
    Unknown = 1
    Increment = 2
    Decrement = 3
    PriceSensitiveDemand = 4
    FixedDemand = 5
    MTLF = 6

class MktBid(object):
    """description of class"""


    def __init__(self, bidid: int, pnodeid: int, bidtype: MktBidType, mkthour: datetime, participant = "", fixedload = 0, bidcurve = {}):
        self.ID = bidid
        self.BidType = bidtype
        self.BidCurves = {}
        self.BidCurves[mkthour] = bidcurve
        self.FixedLoad = {}
        self.FixedLoad[mkthour] = fixedload         
        self.Participant = participant
        self.CPNodeID = pnodeid
        self.CPNode = None

    def Merge(self, mb):
        for d in mb.BidCurves.keys():
            self.BidCurves[d] = mb.BidCurves[d]
        for d in mb.FixedLoad.keys():
            self.FixedLoad[d] = mb.FixedLoad[d]

    def GetVariableName(self):
        return str(self.BidType.name) + "_" + str(self.ID)
