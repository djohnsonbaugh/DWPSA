import os
from Network.Network import Network
from PROBECSVFormat.DayAheadLMPsCSVStream import DayAheadLMPsCSVStream
from PROBECSVFormat.ZonalFactorsCSVStream import ZonalFactorsCSVStream
from PROBECSVFormat.BidDataCSVStream import BidDataCSVStream
from PROBECSVFormat.CostCurvesCSVStream import CostCurvesCSVStream
from PROBECSVFormat.DemandBidsCSVStream import DemandBidsCSVStream
from PROBECSVFormat.FileType import FileType
from datetime import date

class PROBECSVImporter(object):
    """Imports a DA PROBE CSV File Set for a Specified Market Day"""

    def __init__(self, mktday: date, foldername= os.getcwd(),encoding="utf-8"):
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
            self.ImportZonalFactors(network)
            self.ImportBidData(network)
            self.ImportCostCurves(network)
            self.ImportDemandBids(network)

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
        
        filename = filename.format(self.MktDay)
        propertymap = DayAheadLMPsCSVStream.DefaultPropertyToFileMap 
        if FileType.DayAheadLMPs in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.DayAheadLMPs]

        with DayAheadLMPsCSVStream(filename, propertymap, self.Encoding) as csv:
            for pnode in csv:
                network.AddPNode(csv.getPNode())

        return

    def ImportZonalFactors(self, network: Network):
                
        filename = ZonalFactorsCSVStream.DefaultFileName 
        if FileType.ZonalFactors in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.ZonalFactors]
        
        filename = filename.format(self.MktDay)
        propertymap = ZonalFactorsCSVStream.DefaultPropertyToFileMap 
        if FileType.ZonalFactors in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.ZonalFactors]

        with ZonalFactorsCSVStream(filename, propertymap, self.Encoding) as csv:
            for zf in csv:
                network.AddPNodeFactor(csv.getCPNodeID(), csv.getPNodeID(), csv.getFactor())

        return

    def ImportBidData(self, network: Network):
                
        filename = BidDataCSVStream.DefaultFileName 
        if FileType.BidData in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.BidData]
        
        filename = filename.format(self.MktDay)
        propertymap = BidDataCSVStream.DefaultPropertyToFileMap 
        if FileType.BidData in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.BidData]

        with BidDataCSVStream(filename, propertymap, self.Encoding) as csv:
            for udo in csv:
                mu = csv.getMktUit()
                network.AddMktUnit(mu)
                unitoffer = csv.getMktUnitDailyOffer()
                unitoffer.MktDay = self.MktDay
                network.AddMktUnitDailyOffer(unitoffer)

        return

    def ImportCostCurves(self, network: Network):
                
        filename = CostCurvesCSVStream.DefaultFileName 
        if FileType.CostCurves in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.CostCurves]
        
        filename = filename.format(self.MktDay)
        propertymap = CostCurvesCSVStream.DefaultPropertyToFileMap 
        if FileType.CostCurves in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.CostCurves]

        with CostCurvesCSVStream(filename, propertymap, self.Encoding) as csv:
            for uho in csv:
                network.AddMktUnitHourlyOffer(csv.getMktUnitHourlyOffer())

        return

    def ImportDemandBids(self, network: Network):
                
        filename = DemandBidsCSVStream.DefaultFileName 
        if FileType.DemandBids in self.CSVFileNames:
            filename = self.CSVFileNames[FileType.DemandBids]
        
        filename = filename.format(self.MktDay)
        propertymap = DemandBidsCSVStream.DefaultPropertyToFileMap 
        if FileType.DemandBids in self.CSVPropertyMaps:
            propertymap = self.CSVPropertyMaps[FileType.DemandBids]

        with DemandBidsCSVStream(filename, propertymap, self.Encoding) as csv:
            for mb in csv:
                network.AddMktBid(csv.getMktBid())

        return
