from Network.Device import Device
from Network.MktUnitDailyOffer import MktUnitDailyOffer
from Network.MktUnitHourlyOffer import MktUnitHourlyOffer
from Network.CPNode import CPNode
from Network.Unit import Unit
from Network.Load import Load

class MktUnit(object):
    """Market Unit which could represent a partial, single, or multiple physical units in an offer"""

    def __init__(self, id: int, name: str, unittype: str, cpnodeid: int, participant: str):

        self.ID = id
        self.Name = name
        self.DailyOffers = {}
        self.HourlyOffers = {}
        self.CPNodeID = cpnodeid
        self.CPNode = None
        self.Participant = participant
        self.IsCombinedCycle = False
        self.IsCombinedCycleParent = False
        self.CombinedCycleParent = None
        self.Unit = None
        self.Load = None
        self.DRR1 = (unittype.find("DRR1") >= 0)
        self.EAR = (unittype.find("EAR") >= 0)
        self.UnitType = unittype

    def AddDailyOffer(self, udo: MktUnitDailyOffer):
        self.DailyOffers[udo.MktDay]  = udo

    def AddHourlyOffer(self, uho: MktUnitHourlyOffer):
        self.HourlyOffers[uho.MktHour] = uho


    def __str__(self):
        return "[{0}] {1}".format(self.ID, self.Name)