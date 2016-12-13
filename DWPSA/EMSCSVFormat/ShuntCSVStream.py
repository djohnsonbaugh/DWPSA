from EMSCSVFormat.CSVFileStream import CSVFileStream
from Network.Shunt import Shunt
import math
class ShuntCSVStream(CSVFileStream):
    """Streams EMS Shunt Device Properties with Data Conversions"""
    #Company,Station,KV,Shunt Name,Node,Regulation Node,Nominal MVar,Voltage Target PU,Deviation,Changed
    DefaultPropertyToFileMap = {
                                "Company" : "Owner",
                                "Station" : "StationName",
                                "KV" : "Voltage",
                                "Node" : "NodeName",
                                "Regulation Node" : "RegNodeName",
                                "Shunt Name" : "ShuntName",
                                "Nominal MVar" : "MVar",
                                "Voltage Target PU" : "VoltagePUTarget",
                                "Deviation" : "VoltageTargetDeviation"
                                }
    DefaultFileName = "Shunts.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(ShuntCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.MVar = ""
        self.NodeName = ""
        self.Owner = ""
        self.RegNodeName = ""
        self.ShuntName = ""
        self.StationName = ""
        self.Voltage = ""
        self.VoltagePUTarget = ""
        self.VoltageTargetDeviation = ""
        return

    def getMVar(self) -> float:
        try:
            return float(self.MVar)
        except:
            return 0
    def getNodeName(self) -> str:
        return self.NodeName
    def getOwner(self) -> str:
        return self.Owner
    def getRegNodeName(self) -> str:
        return self.RegNodeName
    def getShuntName(self) -> str:
        return self.ShuntName
    def getStationName(self) -> str:
        return self.StationName
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

    def getShunt(self) -> Shunt:
        return Shunt(self.getStationName(), self.getVoltage(), self.getNodeName(), self.getShuntName(), 
                    self.getOwner(), self.getMVar(), self.getRegNodeName(), 
                    self.getVoltagePUTarget(), self.getVoltageTargetDeviation())