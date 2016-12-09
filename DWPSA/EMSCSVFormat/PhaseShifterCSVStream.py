from EMSCSVFormat.CSVFileStream import CSVFileStream
from Network.PhaseShifter import PhaseShifter
from Network.RatingSet import RatingSet
class PhaseShifterCSVStream(CSVFileStream):
    """Streams EMS Phase Shifter Transformer Branch Properties with Data Conversions"""
#PhaseTapType,AWRStatus,MWRegulationSchedule,Summer Normal,Summer Emergency,Winter Normal,Winter Emergency,changed

    DefaultPropertyToFileMap = {
                                "Company" : "Owner",
                                "Station" : "StationName",
                                "TransformerName" : "PhaseShifterName",
                                "FromNode" : "FromNodeName",
                                "FromNominalVoltage" : "FromVoltage",
                                "FromLTCTapType" : "FromTapType",
                                "FromNormalPosition" : "FromTapNormPosition",
                                "ToConnectionNode" : "ToNodeName",
                                "ToNominalVoltage" : "ToVoltage",
                                "ToLTCTapType" : "ToTapType",
                                "ToNormalTap" : "ToTapNormPosition",
                                "RegulationNode" : "RegulationNodeName",
                                "r" : "r",
                                "x" : "x",
                                "AVRStatus" : "AVRStatus",
                                "PhaseTapType" : "PhaseTapType",
                                "AWRStatus" : "AWRStatus",
                                "Summer Normal" : "SumNorm",
                                "Summer Emergency" : "SumEmer",
                                "Winter Normal" : "WinNorm",
                                "Winter Emergency" : "WinEmer"
                                }
    DefaultFileName = "PhaseShifters.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(PhaseShifterCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.AVRStatus = ""
        self.AWRStatus = ""
        self.FromNodeName = ""
        self.FromTapNormPosition = ""
        self.FromTapType = ""
        self.FromTapNormPosition = ""
        self.FromVoltage = ""
        self.Monitored = ""
        self.Owner = ""
        self.PhaseTapType = ""
        self.r = ""
        self.RegulationNodeName = ""
        self.StationName = ""
        self.SumEmer = ""
        self.SumNorm = ""
        self.ToNodeName = ""
        self.ToTapNormPosition = ""
        self.ToTapType = ""
        self.ToVoltage = ""
        self.PhaseShifterName = ""
        self.x = ""
        self.WinEmer = ""
        self.WinNorm = ""
        return

    def getAVRStatus(self) -> int:
        try:
            return int(self.AVRStatus)
        except ValueError:
            return 0
    def getAWRStatus(self) -> bool:
            return self.AWRStatus.upper() == "T" or self.AWRStatus.upper() == "TRUE"
    def getFromNodeName(self) -> str:
        return self.FromNodeName
    def getFromTapNormPosition(self) -> int:
        try:
            return int(self.FromTapNormPosition)
        except ValueError:
            return 0
    def getFromTapType(self) -> str:
        return self.FromTapType
    def getFromStationName(self) -> str:
        return self.FromStationName
    def getFromVoltage(self) -> str:
        return self.FromVoltage
    def getOwner (self) -> str:
        return self.Owner
    def getPhaseShifterName(self) -> str:
        return self.PhaseShifterName
    def getPhaseTapType(self) -> str:
        return self.PhaseTapType
    def getr (self) -> float:
        try:
            return float(self.r)
        except ValueError:
            return 0.0
    def getRegulationNodeName(self) -> str:
        return self.RegulationNodeName
    def getStationName (self) -> str:
        return self.StationName
    def getSummerRatings (self) -> RatingSet:
        try:
            n = float(self.SumNorm)
        except ValueError:
            n = 99999.0
        try:
            e = float(self.SumEmer)
        except ValueError:
            e = 99999.0
        return RatingSet(n, e) 
    def getToNodeName (self) -> str:
        return self.ToNodeName
    def getToTapNormPosition(self) -> int:
        try:
            return int(self.ToTapNormPosition)
        except ValueError:
            return 0.0
    def getToTapType(self) -> str:
        return self.ToTapType
    def getToStationName (self) -> str:
        return self.ToStationName
    def getToVoltage (self) -> str:
        return self.ToVoltage
    def getx (self) -> float:
        return float(self.x)
    def getWinterRatings (self) -> RatingSet:
        try:
            n = float(self.WinNorm)
        except ValueError:
            n = 99999.0
        try:
            e = float(self.WinEmer)
        except ValueError:
            e = 99999.0
        return RatingSet(n, e) 

    def getPhaseShifter(self) -> PhaseShifter:
        return PhaseShifter(self.getStationName(), self.getFromVoltage(), self.getFromNodeName(),
                      self.getToVoltage(), self.getToNodeName(),
                      self.getPhaseShifterName(), self.getOwner(), self.getr(), self.getx(),
                      self.getSummerRatings(), self.getWinterRatings(), None, None, 
                      self.getFromTapType(), self.getFromTapNormPosition(),
                      self.getToTapType(), self.getToTapNormPosition(),
                      self.getRegulationNodeName(), self.getAVRStatus(), self.getPhaseTapType(), self.getAWRStatus())