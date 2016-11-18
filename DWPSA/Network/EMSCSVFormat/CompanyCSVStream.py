from Network.EMSCSVFormat.CSVFileStream  import CSVFileStream
class CompanyCSVStream(CSVFileStream):
    """description of class"""

    DefaultPropertyToFileMap = {
                                "CompanyName" : "CompanyName",
                                "PTINUM" : "CompanyNumber",
                                "LOSS_AREA" : "EnforceLosses",
                                "AWR_AREA" : "AWR"
                                }

    def __init__(self, filepath,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(CompanyCSVStream, self).__init__(filepath, propertytofilemap, encoding)
        self.CompanyName = ""
        self.CompanyNumber = ""
        self.EnforceLosses = ""
        self.AWR = ""

        return

