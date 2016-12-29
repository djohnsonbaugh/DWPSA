from EMSCSVFormat.CSVFileStream import CSVFileStream
from Network.Transformer import Transformer
from Network.RatingSet import RatingSet
class TransformerCSVStream(CSVFileStream):
    """Streams EMS Transformer Branch Properties with Data Conversions"""
#,SummerEmergencyLimit,WinterNormalLimit,WinterEmergencyLimit,Changed,Monitored
    DefaultPropertyToFileMap = {
                                "ID_CO" : "Owner",
                                "ID_ST" : "StationName",
                                "ID" : "TransformerName",
                                "From Connection Node (LTC SIDE)" : "FromNodeName",
                                "From Nominal Voltage (LTC SIDE)" : "FromVoltage",
                                "From Tap Type (LTC SIDE)" : "FromTapType",
                                "From Normal Position (LTC SIDE)" : "FromTapNormPosition",
                                "To Connection Node (FIXED SIDE)" : "ToNodeName",
                                "To Nominal KV (FIXED SIDE)" : "ToVoltage",
                                "To Tap Type (FIXED SIDE)" : "ToTapType",
                                "To Normal Tap (FIXED SIDE)" : "ToTapNormPosition",
                                "Regulation Node" : "RegulationNodeName",
                                "r" : "r",
                                "x" : "x",
                                "AVR Status" : "AVRStatus",
                                "SummerNormalLimit" : "SumNorm",
                                "SummerEmergencyLimit" : "SumEmer",
                                "WinterNormalLimit" : "WinNorm",
                                "WinterEmergencyLimit" : "WinEmer",
                                "Monitored" : "Monitored"
                                }
    DefaultFileName = "Transformers.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(TransformerCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.AVRStatus = ""
        self.FromNodeName = ""
        self.FromTapNormPosition = ""
        self.FromTapType = ""
        self.FromTapNormPosition = ""
        self.FromVoltage = ""
        self.Monitored = ""
        self.Owner = ""
        self.r = ""
        self.RegulationNodeName = ""
        self.StationName = ""
        self.SumEmer = ""
        self.SumNorm = ""
        self.ToNodeName = ""
        self.ToTapNormPosition = ""
        self.ToTapType = ""
        self.ToVoltage = ""
        self.TransformerName = ""
        self.x = ""
        self.WinEmer = ""
        self.WinNorm = ""
        return

    def getAVRStatus(self) -> int:
        try:
            return int(self.AVRStatus)
        except ValueError:
            return 0
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
    def getMonitored (self) -> bool:
        return (self.Monitored.upper() == "TRUE")
    def getOwner (self) -> str:
        return self.Owner
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
    def getTransformerName(self) -> str:
        return self.TransformerName
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

    def getTransformer(self) -> Transformer:
        return Transformer(self.getStationName(), self.getFromVoltage(), self.getFromNodeName(),
                      self.getToVoltage(), self.getToNodeName(),
                      self.getTransformerName(), self.getOwner(), self.getMonitored(), self.getr(), self.getx(),
                      self.getSummerRatings(), self.getWinterRatings(), None, None, 
                      self.getFromTapType(), self.getFromTapNormPosition(),
                      self.getToTapType(), self.getToTapNormPosition(),
                      self.getRegulationNodeName(), self.getAVRStatus())