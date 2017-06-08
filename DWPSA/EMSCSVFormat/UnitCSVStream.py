from CSVFileStream.CSVFileStream import CSVFileStream
from Network.Unit import Unit
import math
class UnitCSVStream(CSVFileStream):
    """Streams EMS Unit Device Properties with Data Conversions"""
    #Voltage Target (PU),Deviation,Mvar Capability Curve,NO AGC,Changed
    DefaultPropertyToFileMap = {
                                "Company" : "Owner",
                                "Station" : "StationName",
                                "KV" : "Voltage",
                                "UnitName" : "UnitName",
                                "Connection Node" : "NodeName",
                                "Regulation Node" : "RegNodeName",
                                "BaseM" : "InitialMW",
                                "Participation Factor" : "ParticipationFactor",
                                "MW Max" : "MWMax",
                                "MW MN" : "MWMin",
                                "Mvar Max" : "MVarMax",
                                "Mvar Min" : "MVarMin",
                                "Voltage Tartet(PU)" : "VoltagePUTarget",
                                "Deviation" : "VoltageTargetDeviation",
                                "NOAGC" : "NoAGC"
                                }
    DefaultFileName = "Units.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(UnitCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.InitialMW = ""
        self.MVarMax = ""
        self.MVarMin = ""
        self.MWMax = ""
        self.MWMin = ""
        self.NoAGC = ""
        self.NodeName = ""
        self.Owner = ""
        self.ParticipationFactor = ""
        self.RegNodeName = ""
        self.StationName = ""
        self.UnitName = ""
        self.Voltage = ""
        self.VoltagePUTarget = ""
        self.VoltageTargetDeviation = ""
        return

    def getAGC (self) -> bool:
        return not (self.NoAGC.upper() == "TRUE")
    def getInitialMW (self) -> float:
        try:
            return float(self.InitialMW)
        except:
            return 0
    def getMVarMax (self) -> float:
        try:
            return float(self.MVarMax)
        except:
            return 0
    def getMVarMin (self) -> float:
        try:
            return float(self.MVarMin)
        except:
            return 0
    def getMWMax (self) -> float:
        try:
            return float(self.MWMax)
        except:
            return 0
    def getMWMin (self) -> float:
        try:
            return float(self.MWMin)
        except:
            return 0
    def getNodeName(self) -> str:
        return self.NodeName
    def getOwner(self) -> str:
        return self.Owner
    def getParticipationFactor (self) -> float:
        try:
            return float(self.ParticipationFactor)
        except:
            return 0
    def getRegNodeName(self) -> str:
        return self.RegNodeName
    def getStationName(self) -> str:
        return self.StationName
    def getUnitName(self) -> str:
        return self.UnitName
    def getVoltage(self) -> str:
        return self.Voltage
    def getVoltagePUTarget(self) -> float:
        try:
            return float(self.VoltagePUTarget)
        except:
            return 0
    def getVoltageTargetDeviation(self) -> float:
        try:
            return float(self.VoltageTargetDeviation)
        except:
            return 0

    def getUnit(self) -> Unit:
        return Unit(self.getStationName(), self.getVoltage(), self.getNodeName(), self.getUnitName(), 
                    self.getOwner(), self.getMWMax(), self.getMVarMax(), self.getMWMin(), self.getMVarMin(),
                    self.getParticipationFactor(), self.getAGC(), self.getInitialMW(), 
                    self.getRegNodeName(), self.getVoltagePUTarget(), self.getVoltageTargetDeviation())