from Network.Unit import Unit
from Network.CPNode import CPNode
from datetime import date

class UnitDailyOffer(object):
    """Daily Unit Offer Data"""

    def __init__(self, unitid: int, cpnodeid: int, participant: str,
                maxenergy: float, mindowntime: float, minruntime: float, maxruntime: float,
                coldstartupcost: float, interstartupcost: float, hotstartupcost: float, hottointertime: float, hottocoldtime: float,
                activeschedule: bool, intermittent: bool, darampdownqualified: bool, darampupqualified: bool, rampcapqualified: bool, usestartupnoload: bool, quickstartqualfied: bool):
        self.ActiveSchedule = activeschedule
        self.ColdStartupCost = coldstartupcost
        self.CPNode = None
        self.CPNodeID = cpnodeid
        self.DARampDownQualified = darampdownqualified
        self.DARampUpQualified = darampupqualified
        self.HotStartupCost = hotstartupcost
        self.HotToColdTime = hottocoldtime
        self.HotToInterTime = hottointertime
        self.Intermittent = intermittent
        self.InterStartupCost = interstartupcost
        self.MaxEnergy = maxenergy
        self.MaxRunTime = maxruntime
        self.MinDownTime = mindowntime
        self.MinRunTime = minruntime
        self.Participant = participant
        self.QuickStartQualified = quickstartqualfied
        self.RampCapQualified = rampcapqualified
        self.Unit = None
        self.UnitID = unitid
        self.UseStartupNoLoad = usestartupnoload
