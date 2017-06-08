from CSVFileStream.CSVFileStream import CSVFileStream
from Network.CircuitBreaker import CircuitBreaker
from Network.CircuitBreaker import CBState
class CircuitBreakerCSVStream(CSVFileStream):
    """Streams EMS Circuit Breaker Properties with Data Conversions"""

    DefaultPropertyToFileMap = {
                                "ID_CO" : "Owner",
                                "ID_ST" : "StationName",
                                "CBTYP Name" : "CBType",
                                "CB Name" : "CBName",
                                "From Node" : "FromNodeName",
                                "To Node" : "ToNodeName",
                                "Normal State" : "NormalState",
                                "KV_ID" : "Voltage"
                                }
    DefaultFileName = "CBs.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(CircuitBreakerCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.CBName = ""
        self.CBType = ""
        self.FromNodeName = ""
        self.NormalState = ""
        self.Owner = ""
        self.StationName = ""
        self.ToNodeName = ""
        self.Voltage = ""
        return

    def getCBName(self):
        return self.CBName
    def getCBType(self):
        return self.CBType
    def getFromNodeName(self):
        return self.FromNodeName
    def getNormalState(self):
        return CBState[self.NormalState]
    def getOwner(self):
        return self.Owner
    def getStationName(self):
        return self.StationName
    def getToNodeName(self):
        return self.ToNodeName
    def getVoltage(self):
        return self.Voltage

    def getCircuitBreaker(self) -> CircuitBreaker:
        return CircuitBreaker(self.getStationName(), self.getVoltage(), self.getFromNodeName(), self.getToNodeName(), 
                              self.getCBName(), self.getOwner(), self.getNormalState(), self.getCBType())