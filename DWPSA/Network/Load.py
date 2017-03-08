from Network.Device import Device
class Load(Device):
    """Load Device"""

    def __init__(self, stationid: str, voltage: str, nodename: str, name: str, owner: str, 
                 mwcon: float, mvcon: float, pfcon: float, mwncon: float = 0, mvncon: float = 0):
        super(Load, self).__init__(stationid, voltage, nodename, name, "LD", owner)

        self.Conforming = complex(mwcon, mvcon)
        self.NonConforming = complex(mwncon, mvncon)
        self.PowerFactor = pfcon

    def __repr__(self):
        return super(Load, self).__repr__() + " " + str(self.Conforming)

    def __str__(self):
        return "{LD} " + super(Load, self).__repr__() + " " + str(self.Conforming.real)

    def GetVariableName(self):
        return "Ld_{0}__{1}__{2}".format(
            self.ID[0].replace("-","_d_"), 
            self.ID[1].replace("-","_d_"),
            self.ID[2].replace("-","_d_")
            )