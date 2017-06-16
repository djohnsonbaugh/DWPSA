import os
from EMSCSVFormat.CircuitBreakerCSVStream import CircuitBreakerCSVStream
from EMSCSVFormat.CompanyCSVStream import CompanyCSVStream
from EMSCSVFormat.DivisionCSVStream import DivisionCSVStream
from EMSCSVFormat.FileType import FileType
from EMSCSVFormat.LineCSVStream import LineCSVStream
from EMSCSVFormat.LoadCSVStream import LoadCSVStream
from EMSCSVFormat.PhaseShifterCSVStream import PhaseShifterCSVStream
from EMSCSVFormat.NodeCSVStream import NodeCSVStream
from EMSCSVFormat.ShuntCSVStream import ShuntCSVStream
from EMSCSVFormat.StationCSVStream import StationCSVStream
from EMSCSVFormat.TransformerCSVStream import TransformerCSVStream
from EMSCSVFormat.UnitCSVStream import UnitCSVStream
from Network.Network import Network

class EMSCSVImporter(object):
    """description of class"""

    def __init__(self, foldername= os.getcwd(), encoding="utf-8", printstatus = True):
        self.CSVFileNames = {}
        self.CSVPropertyMaps = {}
        self.Directory = foldername
        self.Encoding = encoding
        self.PrintStatus = printstatus
        return

    def Import(self, network: Network):
        """Parses all EMS CSV Files into provided network"""
        ospath = os.getcwd()
        try:
            os.chdir(self.Directory)
            print("Processing         Company Data", end = '.')
            self.ImportCompanies(network)
            print("Done!")
            print("Processing        Division Data", end = '.')
            self.ImportDivisions(network)
            print("Done!")
            print("Processing         Station Data", end = '.')
            self.ImportStations(network)
            print("Done!")
            print("Processing            Node Data", end = '.')
            self.ImportNodes(network)
            print("Done!")
            print("Processing Circuit Breaker Data", end = '.')
            self.ImportCircuitBreakers(network)
            print("Done!")
            print("Processing            Line Data", end = '.')
            self.ImportLines(network)
            print("Done!")
            print("Processing     Transformer Data", end = '.')
            self.ImportTransformers(network)
            print("Done!")
            print("Processing   Phase Shifter Data", end = '.')
            self.ImportPhaseShifters(network)
            print("Done!")
            print("Processing            Load Data", end = '.')
            self.ImportLoads(network)
            print("Done!")
            print("Processing           Shunt Data", end = '.')
            self.ImportShunts(network)
            print("Done!")
            print("Processing            Unit Data", end = '.')
            self.ImportUnits(network)
            print("Done!")
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
            i = 0
            d = 0
            for company in csv:
                network.AddCompanyByDef(csv.getCompanyName(), csv.getEnforceLosses(), csv.getAWR())
                i+=1
                while i > ((d+1)*.10 * len(csv)):
                    print("", end = '.')
                    d+=1
        return

    def ImportDivisions(self, network: Network):
                
        filename = DivisionCSVStream.DefaultFileName 
        if FileType.Division in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Division]
        
        propertymap = DivisionCSVStream.DefaultPropertyToFileMap 
        if FileType.Division in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Division]

        with DivisionCSVStream(filename, propertymap, self.Encoding) as csv:
            i = 0
            d = 0
            for Division in csv:
                network.AddDivisionByDef(csv.getDivisionName(), csv.getCompanyName())
                i+=1
                while i > ((d+1)*.10 * len(csv)):
                    print("", end = '.')
                    d+=1

        return

    def ImportStations(self, network: Network):
                
        filename = StationCSVStream.DefaultFileName 
        if FileType.Station in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Station]
        
        propertymap = StationCSVStream.DefaultPropertyToFileMap 
        if FileType.Station in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Station]

        with StationCSVStream(filename, propertymap, self.Encoding) as csv:
            i = 0
            d = 0
            for Station in csv:
                network.AddStationByDef(csv.getStationName(), csv.getCompanyName(), csv.getDivisionName())
                i+=1
                while i > ((d+1)*.10 * len(csv)):
                    print("", end = '.')
                    d+=1

        return
    def ImportNodes(self, network: Network):
                
        filename = NodeCSVStream.DefaultFileName 
        if FileType.Node in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Node]
        
        propertymap = NodeCSVStream.DefaultPropertyToFileMap 
        if FileType.Node in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Node]

        with NodeCSVStream(filename, propertymap, self.Encoding) as csv:
            i = 0
            d = 0
            for Node in csv:
                network.AddNodeByDef(csv.getStationName(), csv.getVoltage(), csv.getNodeName(), csv.getCompanyName())
                i+=1
                while i > ((d+1)*.10 * len(csv)):
                    print("", end = '.')
                    d+=1

        return
    def ImportCircuitBreakers(self, network: Network):
                
        filename = CircuitBreakerCSVStream.DefaultFileName 
        if FileType.CircuitBreaker in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.CircuitBreaker]
        
        propertymap = CircuitBreakerCSVStream.DefaultPropertyToFileMap 
        if FileType.CircuitBreaker in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.CircuitBreaker]

        with CircuitBreakerCSVStream(filename, propertymap, self.Encoding) as csv:
            i = 0
            d = 0
            for LN in csv:
                network.AddNodeConnector(csv.getCircuitBreaker())
                i+=1
                while i > ((d+1)*.10 * len(csv)):
                    print("", end = '.')
                    d+=1

        return
    def ImportLines(self, network: Network):
                
        filename = LineCSVStream.DefaultFileName 
        if FileType.Line in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Line]
        
        propertymap = LineCSVStream.DefaultPropertyToFileMap 
        if FileType.Line in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Line]

        with LineCSVStream(filename, propertymap, self.Encoding) as csv:
            i = 0
            d = 0
            for LN in csv:
                network.AddNodeConnector(csv.getBranch())
                i+=1
                while i > ((d+1)*.10 * len(csv)):
                    print("", end = '.')
                    d+=1

        return
    def ImportTransformers(self, network: Network):
                
        filename = TransformerCSVStream.DefaultFileName 
        if FileType.Transformer in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Transformer]
        
        propertymap = TransformerCSVStream.DefaultPropertyToFileMap 
        if FileType.Transformer in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Transformer]

        with TransformerCSVStream(filename, propertymap, self.Encoding) as csv:
            i = 0
            d = 0
            for XF in csv:
                network.AddNodeConnector(csv.getTransformer())
                i+=1
                while i > ((d+1)*.10 * len(csv)):
                    print("", end = '.')
                    d+=1

        return
    def ImportPhaseShifters(self, network: Network):
                
        filename = PhaseShifterCSVStream.DefaultFileName 
        if FileType.PhaseShifter in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.PhaseShifter]
        
        propertymap = PhaseShifterCSVStream.DefaultPropertyToFileMap 
        if FileType.PhaseShifter in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.PhaseShifter]

        with PhaseShifterCSVStream(filename, propertymap, self.Encoding) as csv:
            i = 0
            d = 0
            for PS in csv:
                network.AddNodeConnector(csv.getPhaseShifter())
                i+=1
                while i > ((d+1)*.10 * len(csv)):
                    print("", end = '.')
                    d+=1

        return
    def ImportLoads(self, network: Network):
                
        filename = LoadCSVStream.DefaultFileName 
        if FileType.Load in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Load]
        
        propertymap = LoadCSVStream.DefaultPropertyToFileMap 
        if FileType.Load in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Load]

        with LoadCSVStream(filename, propertymap, self.Encoding) as csv:
            i = 0
            d = 0
            for LD in csv:
                network.AddDevice(csv.getLoad())
                i+=1
                while i > ((d+1)*.10 * len(csv)):
                    print("", end = '.')
                    d+=1

        return
    def ImportShunts(self, network: Network):
                
        filename = ShuntCSVStream.DefaultFileName 
        if FileType.Shunt in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Shunt]
        
        propertymap = ShuntCSVStream.DefaultPropertyToFileMap 
        if FileType.Shunt in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Shunt]

        with ShuntCSVStream(filename, propertymap, self.Encoding) as csv:
            i = 0
            d = 0
            for SH in csv:
                network.AddDevice(csv.getShunt())
                i+=1
                while i > ((d+1)*.10 * len(csv)):
                    print("", end = '.')
                    d+=1

        return
    def ImportUnits(self, network: Network):
                
        filename = UnitCSVStream.DefaultFileName 
        if FileType.Unit in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.Unit]
        
        propertymap = UnitCSVStream.DefaultPropertyToFileMap 
        if FileType.Unit in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.Unit]

        with UnitCSVStream(filename, propertymap, self.Encoding) as csv:
            i = 0
            d = 0
            for UN in csv:
                network.AddDevice(csv.getUnit())
                i+=1
                while i > ((d+1)*.10 * len(csv)):
                    print("", end = '.')
                    d+=1

        return