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

    #Methods
    def AddNode(self, node):
        self.Nodes[node.ID] = node
        node.Station = self
        node.StationID = self.ID
