from CSVFileStream.CSVFileStream import CSVFileStream
from Network.PNode import PNode
from Network.CPNode import CPNode
from Network.EPNode import EPNode
class DayAheadLMPsCSVStream(CSVFileStream):
    """Streams PROBE PNode Properties With Data Conversions"""
    DefaultPropertyToFileMap = {
                                "PNODEID" : "PNodeID",
                                "PNODENAME" : "PNodeName",
                                "NAME" : "EPNodeID",
                                "BUSNAME" : "StationName",
                                "Voltage" : "Voltage",
                                "EQUIP" : "NodeName",
                                "DPRIVATE" : "Private",
                                "LOADID" : "LoadName",
                                "UNITID" : "UnitName",
                                "RESZONEID" : "ReserveZoneID"                                
                                }
    InvalidPropertyData = {
                            "PNodeName" : "REFBUS"
                          }
    DefaultFileName = "day_ahead_lmps_{%Y%m%d}.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , invalidpropertydata = InvalidPropertyData, encoding="utf-8"):
        super(DayAheadLMPsCSVStream, self).__init__(filepath, propertytofilemap, encoding, invalidpropertydata)      
        self.EPNodeID = ""
        self.LoadName = ""
        self.NodeName = ""
        self.PNodeID = ""
        self.PNodeName = ""
        self.Private = ""
        self.ReserveZoneID = ""
        self.StationName = ""
        self.UnitName = ""
        self.Voltage = ""
        return

    def getEPNodeID(self) -> int:
        if self.EPNodeID == "":
            return 0
        try:
            return int(self.EPNodeID)
        except:
            return 0
    def getLoadName(self) -> str:
        return self.LoadName
    def getLoadUnitName(self) -> str:
        if self.getLoadName() != "": return self.getLoadName()
        if self.getUnitName() != "": return self.getUnitName()
        else: return ""
    def getNodeID(self) -> (str, str):       
        return (self.getStationName(), self.getNodeName())
    def getNodeName(self) -> str:
        return self.NodeName
    def getPNodeID(self) -> int:
        try:
            return int(self.PNodeID)
        except:
            return 0
    def getPNodeName(self) -> str:
        return self.PNodeName
    def getReserveZoneID(self) -> int:
        try:
            return int(self.ReserveZoneID)
        except:
            return -1
    def getSettled(self) -> bool:
        return (self.Private == "0")
    def getStationName(self) -> str:
        return self.StationName
    def getUnitName(self) -> str:
        return self.UnitName
    def getVoltage(self) -> str:
        return self.Voltage

    def IsCPNode(self) -> bool:
        return (self.getEPNodeID() == 0)


    def getPNode(self) -> PNode:
        if self.IsCPNode():
            return CPNode(self.getPNodeID(), self.getPNodeName(), self.getSettled())
        else:
            return EPNode(self.getPNodeID(), self.getPNodeName(), self.getEPNodeID(), self.getNodeID(), self.getLoadUnitName(), self.getReserveZoneID())