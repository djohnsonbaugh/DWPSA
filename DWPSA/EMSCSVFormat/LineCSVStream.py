from CSVFileStream.CSVFileStream import CSVFileStream
from Network.Branch import Branch
from Network.RatingSet import RatingSet
class LineCSVStream(CSVFileStream):
    """Streams EMS Branch Properties with Data Conversions"""

    DefaultPropertyToFileMap = {
                                "FROM_ST" : "FromStationName",
                                "FROM_KV" : "FromVoltage",
                                "FROM_ND" : "FromNodeName",
                                "TO_ST" : "ToStationName",
                                "TO_KV" : "ToVoltage",
                                "TO_ND" : "ToNodeName",
                                "Line_Name" : "LineName",
                                "Segment Name" : "Segment",
                                "r" : "r",
                                "x" : "x",
                                "CO_OWNER" : "Owner",
                                "Summer Normal rating" : "SumNorm",
                                "Summer Emergency rating" : "SumEmer",
                                "Winter Normal rating" : "WinNorm",
                                "Winter Emergency rating" : "WinEmer",
                                "Monitored" : "Monitored"
                                }
    DefaultFileName = "Lines.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(LineCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.FromNodeName = ""
        self.FromStationName = ""
        self.FromVoltage = ""
        self.LineName = ""
        self.Monitored = ""
        self.Owner = ""
        self.r = ""
        self.Segment = ""
        self.SumEmer = ""
        self.SumNorm = ""
        self.ToNodeName = ""
        self.ToStationName = ""
        self.ToVoltage = ""
        self.x = ""
        self.WinEmer = ""
        self.WinNorm = ""
        return

    def getFromNodeName(self) -> str:
        return self.FromNodeName
    def getFromStationName(self) -> str:
        return self.FromStationName
    def getFromVoltage(self) -> str:
        return self.FromVoltage
    def getLineName(self) -> str:
        return self.LineName
    def getMonitored (self) -> bool:
        return (self.Monitored.upper() == "TRUE")
    def getOwner (self) -> str:
        return self.Owner
    def getr (self) -> float:
        return float(self.r)
    def getSegment (self) -> str:
        return self.Segment
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
        return RatingSet(float(self.SumNorm), float(self.SumEmer)) 
    def getToNodeName (self) -> str:
        return self.ToNodeName
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
        return RatingSet(float(self.WinNorm), float(self.WinEmer))

    def getBranch(self) -> Branch:
        return Branch(self.getFromStationName(), self.getFromVoltage(), self.getFromNodeName(),
                      self.getToStationName(), self.getToVoltage(), self.getToNodeName(),
                      self.getLineName(), self.getOwner(), self.getMonitored(), 
                      self.getr(), self.getx(), self.getSegment(),
                      self.getSummerRatings(), self.getWinterRatings())