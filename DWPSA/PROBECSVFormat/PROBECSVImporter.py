import os
from Network.Network import Network
from PROBECSVFormat.DayAheadLMPsCSVStream import DayAheadLMPsCSVStream
from PROBECSVFormat.FileType import FileType
import datetime

class PROBECSVImporter(object):
    """Imports a DA PROBE CSV File Set for a Specified Market Day"""

    def __init__(self, mktday: datetime, foldername= os.getcwd(),encoding="utf-8"):
        self.CSVFileNames = {}
        self.CSVPropertyMaps = {}
        self.Directory = foldername
        self.Encoding = encoding
        self.MktDay = mktday
        return

    def Import(self, network: Network):
        """Parses all PROBE CSV Files into provided network"""
        ospath = os.getcwd()
        try:
            os.chdir(self.Directory)
            self.ImportDayAheadLMPs(network)

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

    def ImportDayAheadLMPs(self, network: Network):
                
        filename = DayAheadLMPsCSVStream.DefaultFileName 
        if FileType.DayAheadLMPs in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.DayAheadLMPs]
        
        propertymap = DayAheadLMPsCSVStream.DefaultPropertyToFileMap 
        if FileType.DayAheadLMPs in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.DayAheadLMPs]

        with DayAheadLMPsCSVStream(filename.format(self.MktDay), propertymap, self.Encoding) as csv:
            for pnode in csv:
                network.AddPNode(csv.getPNode())

        return

