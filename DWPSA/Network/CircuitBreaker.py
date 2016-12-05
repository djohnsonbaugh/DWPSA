from enum import Enum
from Network.NodeConnector import NodeConnector

class CBState(Enum):
    Open = 0
    Closed = 1

class CircuitBreaker(NodeConnector):
    """Circuit Breaker Node Connector"""


    def __init__(self, stationid: str, voltage: str, fnodename: str, tnodename: str,
                 name: str, owner: str, normalstate: CBState, type: str):
        super(CircuitBreaker, self).__init__(stationid, voltage, fnodename, 
                                             stationid, voltage, tnodename, 
                                             name, owner, 0, 0, type)
        self.CBType = type
        self.NormalState = normalstate
        self.StationID = stationid
        self.Voltage = voltage

