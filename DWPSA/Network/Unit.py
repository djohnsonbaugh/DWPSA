from Network.Device import Device
class Unit(Device):
    """Unit Device"""

    def __init__(self, stationid: str, voltage: str, nodename: str, name: str, owner: str, 
                 mwmax: float, mvmax: float, mwmin: float, mvmin: float, partfact: float, agc: bool, imw: float,
                 regnodename : str = "", puvolttarget: float = 1, deviation: float = .05 ):
        super(Unit, self).__init__(stationid, voltage, nodename, name, owner)
        
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
