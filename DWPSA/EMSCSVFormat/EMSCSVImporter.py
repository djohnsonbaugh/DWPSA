import os
from EMSCSVFormat.CircuitBreakerCSVStream import CircuitBreakerCSVStream
from EMSCSVFormat.CompanyCSVStream import CompanyCSVStream
from EMSCSVFormat.DivisionCSVStream import DivisionCSVStream
from EMSCSVFormat.FileType import FileType
from EMSCSVFormat.LineCSVStream import LineCSVStream
from EMSCSVFormat.LoadCSVStream import LoadCSVStream
from EMSCSVFormat.PhaseShifterCSVStream import PhaseShifterCSVStream
from EMSCSVFormat.NodeCSVStream import NodeCSVStream
from EMSCSVFormat.StationCSVStream import StationCSVStream
from EMSCSVFormat.TransformerCSVStream import TransformerCSVStream
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
            self.ImportDivisions(network)
            self.ImportStations(network)
            self.ImportNodes(network)
            self.ImportCircuitBreakers(network)
            self.ImportLines(network)
            self.ImportTransformers(network)
            self.ImportPhaseShifters(network)
            self.ImportLoads(network)
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
    def ImportTransformers(self, network: Network):
                
        filename = TransformerCSVStream.DefaultFileName 
        if FileType.Transformer in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Transformer]
        
        propertymap = TransformerCSVStream.DefaultPropertyToFileMap 
        if FileType.Transformer in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Transformer]

        with TransformerCSVStream(filename, propertymap, self.Encoding) as csv:
            for XF in csv:
                network.AddNodeConnector(csv.getTransformer())

        return
    def ImportPhaseShifters(self, network: Network):
                
        filename = PhaseShifterCSVStream.DefaultFileName 
        if FileType.PhaseShifter in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.PhaseShifter]
        
        propertymap = PhaseShifterCSVStream.DefaultPropertyToFileMap 
        if FileType.PhaseShifter in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.PhaseShifter]

        with PhaseShifterCSVStream(filename, propertymap, self.Encoding) as csv:
            for PS in csv:
                network.AddNodeConnector(csv.getPhaseShifter())

        return
    def ImportLoads(self, network: Network):
                
        filename = LoadCSVStream.DefaultFileName 
        if FileType.Load in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Load]
        
        propertymap = LoadCSVStream.DefaultPropertyToFileMap 
        if FileType.Load in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Load]

        with LoadCSVStream(filename, propertymap, self.Encoding) as csv:
            for LN in csv:
                network.AddDevice(csv.getLoad())

        return