class NodeConnector(object):
    """Physical connector of 2 Nodes"""

    #Constructor
    def __init__(self, 
                fstationid: str, fvoltage: str, fnodename: str, 
                tstationid: str, tvoltage: str, tnodename: str, 
                name: str, owner: str, r: float = 0, x: float = 0, segment: str = ""):
        self.ID = (fstationid, name, segment)
        self.Impedance = complex(r,x)
        self.FromNode = None
        self.FromNodeID = (fstationid, fvoltage, fnodename)            
        self.FromNodeName = fnodename
        self.FromStationID = fstationid
        self.FromVoltage = fvoltage
        self.Name = name
        self.OwnerCompanyID = owner
        self.Segment = segment
        self.ToNode = None
        self.ToNodeID = (tstationid, tvoltage, tnodename)            
        self.ToNodeName = tnodename
        self.ToStationID = tstationid
        self.ToVoltage = tvoltage
        return

