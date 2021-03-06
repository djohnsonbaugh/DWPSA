from Network.PNode import PNode
from Network.Node import Node
class EPNode(PNode):
    """Elemental Pricing Node that is at a specific physical Location in a Power System"""

   #Constructor
    def __init__(self, id: int, name: str, epnodeid: int, nodeid: (str,str), loadunitname: str, reszoneid: int):
        super(EPNode, self).__init__(id, name)
        """EPNode Constructor"""
        
        #Attributes
        self.EPNodeID = epnodeid
        self.Node = None
        self.NodeID = nodeid
        self.LoadUnitName = loadunitname
        self.ReserveZoneID = reszoneid
    def __repr__(self):
        return "[" + self.ID + "] " + self.Name
    def __str__(self):
        return "[" + self.ID + "] " + self.Name

    def Copy(self):
        return EPNode(self.ID, self.Name, self.EPNodeID, self.NodeID, self.LoadUnitName, self.ReserveZoneID)
