from Network.Node import *
from Network.MktUnit import MktUnit

class Station(object):
    """Physical Location containing a Node or Nodes"""

    #Constructor
    def __init__(self, stationid, companyid = "", divisionid = ""):
        self.Company = None
        self.CompanyID = companyid
        self.Division = None
        self.DivisionID = divisionid
        self.ID = stationid
        self.Nodes = {}
        self.NodeConnectors = {}
        self.Devices = {}
        self.MktUnits = {}

    #Methods
    def AddNode(self, node):
        self.Nodes[node.ID] = node
        node.Station = self
        node.StationID = self.ID

    def AddNodeConnector(self, nc: NodeConnector):
        self.NodeConnectors[nc.ID] = nc
    
    def AddDevice(self, d: Device):
        self.Devices[d.ID] = d

    def AddMktUnit(self, mu: MktUnit):
        self.MktUnits[mu.ID] = mu

    def GetVariableName(self):
        return "{0}".format(
            self.ID.replace("-","_d_")
            )

    def Copy(self):
        '''Deep Copy including all non collection based properties'''
        return Station(self.ID, self.CompanyID, self.DivisionID)