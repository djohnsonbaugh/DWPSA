from EMSCSVFormat.CSVFileStream import CSVFileStream
class NodeCSVStream(CSVFileStream):
    """Streams EMS Node Properties With Data Conversions"""

    DefaultPropertyToFileMap = {
                                "NodeName" : "NodeName",
                                "CompanyName" : "CompanyName",
                                "StationName" : "StationName",
                                "Voltage" : "Voltage"
                                }
    DefaultFileName = "Nodes.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(NodeCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.CompanyName = ""
        self.StationName = ""
        self.NodeName = ""
        self.Voltage = ""
        return

    def getCompanyName(self):
        return self.CompanyName
    def getStationName(self):
        return self.StationName
    def getNodeName(self):
        return self.NodeName
    def getVoltage(self):
        return self.Voltage