from CSVFileStream.CSVFileStream import CSVFileStream
from Network.UnitDailyOffer import UnitDailyOffer

class BidDataCSVStream(CSVFileStream):
    """Streams PROBE Unit Daily Offer Properties With Data Conversions"""
    DefaultPropertyToFileMap = {
                                "PNODEID" : "PNodeID",
                                "UNITID" : "UnitID",
                                "OPERATORNAME": "OperatorName",
                                "UNITTYPE" : "UnitType",
                                "UNITSHEDULEID" : "UnitScheduleID",
                                "MAX_MW" : "MaxEnergy",
                                "MIN_RUN_TIME_HOURS" : "MinRunTime",
                                "MIN_DOWN_TIME_HOURS" : "MinDownTime",
                                "COLDSTARTUPCOST" : "ColdStartupCost",
                                "INTERSTARTUPCOST" : "InterStartupCost",
                                "HOTSTARTUPCOST" : "HotStartupCost",
                                "HOTTOINTERTIME" : "HotToInterTime",
                                "HOTTOCOLDTIME" : "HotToColdTime",
                                "MAXRUN" : "MaxRunTime",
                                "PARTICIPANTNAME" : "Participant",
                                "USESTARTUPNOLOAD" : "UseStartupNoLoad",
                                "QUICKSTARTQUALIFIED" : "QuickStartQualified",
                                "ACTIVESCHEDULE" : "ActiveSchedule",
                                "DARAMPUPQUALIFIED" : "DARampUpQualified",
                                "DARAMPDOWNQUALIFIED" : "DARampDownQualified",
                                "INTERMITTENT" : "Intermittent",
                                "RAMPCAPQUALIFIED" : "RampCapQualified"
                                }

    DefaultFileName = "bid_data_{:%Y%m%d}.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(BidDataCSVStream, self).__init__(filepath, propertytofilemap, encoding)      
        self.ActiveSchedule = ""
        self.ColdStartupCost = ""
        self.DARampUpQualified = ""
        self.DARampDownQualified = ""
        self.HotStartupCost = ""
        self.HotToColdTime = ""
        self.HotToInterTime = ""
        self.Intermittent = ""
        self.InterStartupCost = ""
        self.MaxRunTime = ""
        self.MinDownTime = ""
        self.MinRunTime = ""
        self.MaxEnergy = ""
        self.OperatorName = ""
        self.Participant = ""
        self.PNodeID = ""
        self.QuickStartQualified = ""
        self.RampCapQualified = ""
        self.UnitID = ""
        self.UnitScheduleID = ""
        self.UnitType = ""
        self.UseStartupNoLoad = ""
        return

    def getActiveSchedule(self) -> bool:
        return (self.ActiveSchedule == "1")
    def getColdStartupCost(self) -> float:
        try:
            return float(self.ColdStartupCost)
        except:
            return 0
    def getDARampUpQualified(self) -> bool:
        return (self.DARampUpQualified == "1")
    def getDARampDownQualified(self) -> bool:
        return (self.DARampDownQualified == "1")
    def getHotStartupCost(self) -> float:
        try:
            return float(self.HotStartupCost)
        except:
            return 0
    def getHotToColdTime(self) -> float:
        try:
            return float(self.HotToColdTime)
        except:
            return 0
    def getHotToInterTime(self) -> float:
        try:
            return float(self.HotToInterTime)
        except:
            return 0
    def getIntermittent(self) -> bool:
        return (self.Intermittent == "1")
    def getInterStartupCost(self) -> float:
        try:
            return float(self.InterStartupCost)
        except:
            return 0
    def getMaxRunTime(self) -> float:
        try:
            return float(self.MaxRunTime)
        except:
            return 0
    def getMinDownTime(self) -> float:
        try:
            return float(self.MinDownTime)
        except:
            return 0
    def getMinRunTime(self) -> float:
        try:
            return float(self.MinRunTime)
        except:
            return 0
    def getMaxEnergy(self) -> float:
        try:
            return float(self.MaxEnergy)
        except:
            return 0
    def getOperatorName(self) -> str:
        return self.OperatorName
    def getParticipant(self) -> str:
        return self.Participant
    def getPNodeID(self) -> int:
        try:
            return int(self.PNodeID)
        except:
            return 0
    def getQuickStartQualified(self) -> bool:
        return (self.QuickStartQualified == "1")
    def getRampCapQualified(self) -> bool:
        return (self.RampCapQualified == "1")
    def getUnitID(self) -> int:
        try:
            return int(self.UnitID)
        except:
            return 0
    def getUnitScheduleID(self) -> int:
        try:
            return int(self.UnitScheduleID)
        except:
            return 0
    def getUnitType(self) -> str:
        return self.UnitType
    def getUseStartupNoLoad(self) -> bool:
        return (self.UseStartupNoLoad == "1")

    def getUnitDailyOffer(self) -> UnitDailyOffer:
        return UnitDailyOffer(self.getUnitID(),self.getPNodeID(), self.getParticipant(), 
                              self.getMaxEnergy(), self.getMinDownTime(), self.getMinRunTime(), self.getMaxRunTime(), 
                              self.getColdStartupCost(), self.getInterStartupCost(), self.getHotStartupCost(), self.getHotToInterTime(), self.getHotToColdTime(),
                              self.getActiveSchedule(), self.getIntermittent(), self.getDARampDownQualified(), self.getDARampUpQualified(), 
                              self.getRampCapQualified(),self.getUseStartupNoLoad(), self.getQuickStartQualified())

