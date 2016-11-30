from CSVFileStream  import CSVFileStream
class CompanyCSVStream(CSVFileStream):
    """Streams ECS Company Properties With Data Conversions"""

    DefaultPropertyToFileMap = {
                                "CompanyName" : "CompanyName",
                                "PTINUM" : "CompanyNumber",
                                "LOSS_AREA" : "EnforceLosses",
                                "AWR_AREA" : "AWR"
                                }
    DefaultFileName = "Company.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(CompanyCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.CompanyName = ""
        self.CompanyNumber = ""
        self.EnforceLosses = ""
        self.AWR = ""

        return

    def getCompanyName(self):
        return self.CompanyName

    def getCompanyNumber(self):
        return self.CompanyNumber

    def getAWR(self):
        return bool(self.AWR)

    def getEnforceLosses(self):
        return bool(self.EnforceLosses)