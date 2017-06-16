from datetime import date

class MktUnitDailyOffer(object):
    """Daily Market Unit Offer Data"""

    def __init__(self, unitid: int,  maxenergy: float, mindowntime: float, minruntime: float, maxruntime: float,
                coldstartupcost: float, interstartupcost: float, hotstartupcost: float, hottointertime: float, hottocoldtime: float,
                activeschedule: bool, intermittent: bool, darampdownqualified: bool, darampupqualified: bool, rampcapqualified: bool, usestartupnoload: bool, quickstartqualfied: bool):
        self.ActiveSchedule = activeschedule
        self.ColdStartupCost = coldstartupcost
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
        self.MktDay = date.today()
        self.QuickStartQualified = quickstartqualfied
        self.RampCapQualified = rampcapqualified
        self.UnitID = unitid
        self.UseStartupNoLoad = usestartupnoload

    def __str__(self):
        return "[{0}] {1} Active={2}".format(self.MktDay, self.UnitID, self.ActiveSchedule)