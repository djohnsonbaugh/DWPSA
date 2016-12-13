from Network.Device import Device
class Load(Device):
    """Load Device"""

    def __init__(self, stationid: str, voltage: str, nodename: str, name: str, owner: str, 
                 mwcon: float, mvcon: float, pfcon: float, mwncon: float = 0, mvncon: float = 0):
        super(Load, self).__init__(stationid, voltage, nodename, name, owner)

        self.Conforming = complex(mwcon, mvcon)
        self.NonConforming = complex(mwncon, mvncon)
        self.PowerFactor = pfcon

    def __repr__(self):
        return super(Load, self).__repr__() + " " + str(self.Conforming)