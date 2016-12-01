from CSVFileStream  import CSVFileStream
class StationCSVStream(CSVFileStream):
    """Streams EMS Station Properties With Data Conversions"""

    DefaultPropertyToFileMap = {
                                "CompanyName" : "CompanyName",
                                "DivisionName" : "DivisionName",
                                "StationName" : "StationName"
                                }
    DefaultFileName = "Station.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(StationCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.CompanyName = ""
        self.DivisionName = ""
        self.StationName = ""

        return

    def getCompanyName(self):
        return self.CompanyName
    def getDivisionName(self):
        return self.DivisionName
    def getStationName(self):
        return self.StationName