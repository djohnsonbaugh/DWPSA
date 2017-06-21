class Device(object):
    """Physical Device at a Node"""

    #Constructor
    def __init__(self, stationid: str, voltage: str, nodename: str, name: str, dtype: str,  owner: str):
        self.ID = (stationid, name, dtype)
        self.Name = name
        self.Node = None
        self.NodeID = (stationid, nodename)            
        self.NodeName = nodename
        self.OwnerCompanyID = owner
        self.StationID = stationid
        self.Voltage = voltage
        self.MktUnit = None
        return

    def __repr__(self):
        return self.StationID + " " + self.Name + " " + self.Voltage

    def __str__(self):
        return self.StationID + " " + self.Name + " " + self.Voltage