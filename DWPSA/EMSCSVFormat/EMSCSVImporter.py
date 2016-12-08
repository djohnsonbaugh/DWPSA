import os
from EMSCSVFormat.FileType import FileType
from EMSCSVFormat.CompanyCSVStream import CompanyCSVStream
from EMSCSVFormat.DivisionCSVStream import DivisionCSVStream
from EMSCSVFormat.StationCSVStream import StationCSVStream
from EMSCSVFormat.NodeCSVStream import NodeCSVStream
from EMSCSVFormat.LineCSVStream import LineCSVStream
from Network.Network import Network
from EMSCSVFormat.CircuitBreakerCSVStream import CircuitBreakerCSVStream

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
            self.ImportDivisions(network)
            self.ImportStations(network)
            self.ImportNodes(network)
            self.ImportCircuitBreakers(network)
            self.ImportLines(network)

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

    def ImportDivisions(self, network: Network):
                
        filename = DivisionCSVStream.DefaultFileName 
        if FileType.Division in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Division]
        
        propertymap = DivisionCSVStream.DefaultPropertyToFileMap 
        if FileType.Division in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Division]

        with DivisionCSVStream(filename, propertymap, self.Encoding) as csv:
            for Division in csv:
                network.AddDivisionByDef(csv.getDivisionName(), csv.getCompanyName())

        return

    def ImportStations(self, network: Network):
                
        filename = StationCSVStream.DefaultFileName 
        if FileType.Station in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Station]
        
        propertymap = StationCSVStream.DefaultPropertyToFileMap 
        if FileType.Station in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Station]

        with StationCSVStream(filename, propertymap, self.Encoding) as csv:
            for Station in csv:
                network.AddStationByDef(csv.getStationName(), csv.getCompanyName(), csv.getDivisionName())

        return
    def ImportNodes(self, network: Network):
                
        filename = NodeCSVStream.DefaultFileName 
        if FileType.Node in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Node]
        
        propertymap = NodeCSVStream.DefaultPropertyToFileMap 
        if FileType.Node in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Node]

        with NodeCSVStream(filename, propertymap, self.Encoding) as csv:
            for Node in csv:
                network.AddNodeByDef(csv.getStationName(), csv.getVoltage(), csv.getNodeName(), csv.getCompanyName())

        return
    def ImportCircuitBreakers(self, network: Network):
                
        filename = CircuitBreakerCSVStream.DefaultFileName 
        if FileType.CircuitBreaker in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.CircuitBreaker]
        
        propertymap = CircuitBreakerCSVStream.DefaultPropertyToFileMap 
        if FileType.CircuitBreaker in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.CircuitBreaker]

        with CircuitBreakerCSVStream(filename, propertymap, self.Encoding) as csv:
            for LN in csv:
                network.AddNodeConnector(csv.getCircuitBreaker())

        return
    def ImportLines(self, network: Network):
                
        filename = LineCSVStream.DefaultFileName 
        if FileType.Line in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Line]
        
        propertymap = LineCSVStream.DefaultPropertyToFileMap 
        if FileType.Line in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Line]

        with LineCSVStream(filename, propertymap, self.Encoding) as csv:
            for LN in csv:
                network.AddNodeConnector(csv.getBranch())

        return