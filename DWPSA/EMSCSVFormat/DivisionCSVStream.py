from EMSCSVFormat.CSVFileStream import CSVFileStream
class DivisionCSVStream(CSVFileStream):
    """Streams EMS Division Properties With Data Conversions"""

    DefaultPropertyToFileMap = {
                                "CompanyName" : "CompanyName",
                                "DivisionName" : "DivisionName"
                                }
    DefaultFileName = "Division.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(DivisionCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.CompanyName = ""
        self.DivisionName = ""

        return

    def getCompanyName(self):
        return self.CompanyName
    def getDivisionName(self):
        return self.DivisionName