import os
from EMSCSVFormat.FileType import FileType
from EMSCSVFormat.CompanyCSVStream import CompanyCSVStream
from Network.Network import Network

class EMSCSVImporter(object):
    """description of class"""

    def __init__(self, foldername= os.getcwd(), encoding="utf-8"):
        self.CSVFileNames = {}
        self.CSVPropertyMaps = {}
        self.Directory = foldername
        self.Encoding = encoding
        return

    def Import(self, network: Network):
        """Parses all EMS CSV Files into provided network"""
        ospath = os.getcwd()
        try:
            os.chdir(self.Directory)
            self.ImportCompanies(network)


        finally:
            os.chdir(ospath)
        return

    def setCSVFileName(self, filetype: FileType, filename: str):
        """Change file name from default for filetype
            
           Parameters:
           -----------------------------
           filetype         - Enum          EMSCSVFormat.FileType
           filename         - string        name of file to be parsed
        """
        self.CSVFileNames[filetype] = filename
        return
 
    def setCSVPropertyMap(self, filetype: FileType, propertytofilemap : dict):
        """Change property to file map from default for filetype
            
           Parameters:
           -----------------------------
           filetype         - Enum          EMSCSVFormat.FileType
           propertytofilemap- Dictionary    key (file header) value (class property)
        """
        self.CSVPropertyMaps[filetype] = propertytofilemap
        return

    def ImportCompanies(self, network: Network):
                
        filename = CompanyCSVStream.DefaultFileName 
        if FileType.Company in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Company]
        
        propertymap = CompanyCSVStream.DefaultPropertyToFileMap 
        if FileType.Company in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Company]

        with CompanyCSVStream(filename, propertymap, self.Encoding) as csv:
            for company in csv:
                network.AddCompanyByDef(csv.getCompanyName(), csv.getEnforceLosses(), csv.getAWR())

        return