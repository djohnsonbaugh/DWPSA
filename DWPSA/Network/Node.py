from Network.NodeConnector import NodeConnector
class Node(object):
    """Physical Location in a Power System"""


    #Constructor
    def __init__(self, stationid, voltage, name, companyid = "", divisionid = ""):
        """Node Constructor"""

        #Attributes
        self.CompanyID = companyid
        self.DivisionID = divisionid
        self.ID = (stationid, name)
        self.Name = name
        self.Station = None
        self.StationID = stationid
        self.Voltage = voltage
        self.NodeConnectors = {}
    #Methods
    def AddNodeConnector(self, nc: NodeConnector):
        self.NodeConnectors[nc.ID] = nc
        if self.ID == nc.FromNodeID:
            nc.FromNode = self
        if self.ID == nc.ToNodeID:
            nc.ToNode = self

    def __repr__(self):
        return self.StationID + " " + self.Name + " " + self.Voltage

    o = object()
