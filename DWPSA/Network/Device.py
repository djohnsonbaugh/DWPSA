class Device(object):
    """Physical Device at a Node"""

    #Constructor
    def __init__(self, stationid: str, voltage: str, nodename: str, name: str, owner: str):
        self.ID = (stationid, name)
        self.Name = name
        self.Node = None
        self.NodeID = (stationid, nodename)            
        self.NodeName = nodename
        self.OwnerCompanyID = owner
        self.StationID = stationid
        self.Voltage = voltage
        return

