from Network.Device import Device
class Unit(Device):
    """Unit Device"""

    def __init__(self, stationid: str, voltage: str, nodename: str, name: str, owner: str, 
                 mwmax: float, mvmax: float, mwmin: float, mvmin: float, partfact: float, agc: bool, imw: float,
                 regnodename : str = "", puvolttarget: float = 1, deviation: float = .05 ):
        super(Unit, self).__init__(stationid, voltage, nodename, name, "UN", owner)
        
        self.AGC = agc
        self.InitialMW = imw
        self.MVAMax = complex(mwmax, mvmax)
        self.MVAMin = complex(mwmin, mvmin)
        self.ParticipationFactor = partfact
        self.RegulationNode = None
        self.RegulationNodeName = regnodename
        self.RegulationNodeID = (stationid, regnodename)
        self.VoltagePUTarget = puvolttarget
        self.VoltageTargetDeviation = deviation


    def __str__(self):
        return "{UN} " + super(Unit, self).__repr__() + " " + str(self.MVAMax.real)

    def GetVariableName(self):
        return "Un_{0}__{1}__{2}".format(
            self.ID[0].replace("-","_d_"), 
            self.ID[1].replace("-","_d_"),
            self.ID[2].replace("-","_d_")
            )