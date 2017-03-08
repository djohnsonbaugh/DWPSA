from Network.Node import *

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

    #Methods
    def AddNode(self, node):
        self.Nodes[node.ID] = node
        node.Station = self
        node.StationID = self.ID

    def AddNodeConnector(self, nc: NodeConnector):
        self.NodeConnectors[nc.ID] = nc
    
    def AddDevice(self, d: Device):
        self.Devices[d.ID] = d

    def GettVariableName(self, prefix: str):
        return "{0}_{1}".format(
            prefix,
            self.ID.replace("-","_d_")
            )