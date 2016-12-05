from enum import Enum
from Network.NodeConnector import NodeConnector

class Branch(NodeConnector):
    """Branch Node Connector"""

    def __init__(self, fstationid: str, fvoltage: str, fnodename: str, 
                 tstationid: str, tvoltage: str, tnodename: str,
                 name: str, owner: str, monitored: bool,
                 r: float = 0, x: float = 0, segment: str = ""):
        super(Branch, self).__init__(fstationid, fvoltage, fnodename, 
                                             tstationid, tvoltage, tnodename, 
                                             name, owner, r, x, segment)

        self.Monitored = monitored