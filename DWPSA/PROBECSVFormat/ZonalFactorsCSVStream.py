from CSVFileStream.CSVFileStream import CSVFileStream
from Network.PNode import PNode
from Network.CPNode import CPNode
from Network.EPNode import EPNode
class ZonalFactorsCSVStream(CSVFileStream):
    """Streams PROBE PNode Properties With Data Conversions"""
    DefaultPropertyToFileMap = {
                                "AGGREGATEDPNODEID" : "CPNodeID",
                                "PNODEID" : "PNodeID",
                                "FACTOR" : "Factor"                              
                                }

    DefaultFileName = "zonal_factors_{:%Y%m%d}.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(ZonalFactorsCSVStream, self).__init__(filepath, propertytofilemap, encoding)      
        self.CPNodeID = ""
        self.Factor = ""
        self.PNodeID = ""
        return

    def getCPNodeID(self) -> int:
        try:
            return int(self.CPNodeID)
        except:
            return 0
    def getFactor(self) -> float:
        try:
            return float(self.Factor)
        except:
            return 0
    def getPNodeID(self) -> int:
        try:
            return int(self.PNodeID)
        except:
            return 0