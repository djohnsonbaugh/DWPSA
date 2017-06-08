from CSVFileStream.CSVFileStream import CSVFileStream
from Network.Load import Load
import math
class LoadCSVStream(CSVFileStream):
    """Streams EMS Load Device Properties with Data Conversions"""
    DefaultPropertyToFileMap = {
                                "Company" : "Owner",
                                "Station" : "StationName",
                                "KV" : "Voltage",
                                "Node Name" : "NodeName",
                                "Load Name" : "LoadName",
                                "MW NonConforming" : "MWNonCon",
                                "MVarNonConforming" : "MVNonCon",
                                "MW Conforming" : "MWCon",
                                "PowerFactor Conforming" : "PowerFactorCon"
                                }
    DefaultFileName = "Loads.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(LoadCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.LoadName = ""
        self.MWNonCon = ""
        self.MVNonCon = ""
        self.MWCon = ""
        self.NodeName = ""
        self.Owner = ""
        self.PowerFactorCon = ""
        self.StationName = ""
        self.Voltage = ""
        return

    def getLoadName(self) -> str:
        return self.LoadName
    def getMWNonCon(self) -> float:
        try:
            return float(self.MWNonCon)
        except:
            return 0
    def getMVNonCon(self) -> float:
        try:
            return float(self.MVNonCon)
        except:
            return 0
    def getMWCon(self) -> float:
        try:
            return float(self.MWCon)
        except:
            return 0
    def getMVCon(self) -> float:
        try:
            return math.sqrt((self.getMWCon()/self.getPowerFactorCon())**2 - (self.getMWCon())**2)
        except:
            return 0
    def getNodeName(self) -> str:
        return self.NodeName
    def getOwner(self) -> str:
        return self.Owner
    def getPowerFactorCon(self) -> float:
        try:
            return float(self.PowerFactorCon)
        except:
            return 0
    def getStationName(self) -> str:
        return self.StationName
    def getVoltage(self) -> str:
        return self.Voltage

    def getLoad(self) -> Load:
        return Load(self.getStationName(), self.getVoltage(), self.getNodeName(), self.getLoadName(), 
                    self.getOwner(), self.getMWCon(), self.getMVCon(), self.getPowerFactorCon(), 
                    self.getMWNonCon(), self.getMVNonCon())