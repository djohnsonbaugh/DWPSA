from Network.Device import Device
class Shunt(Device):
    """Shunt Device"""

    def __init__(self, stationid: str, voltage: str, nodename: str, name: str, owner: str, 
                 mvar: float, regnodename : str = "", puvolttarget: float = 1, deviation: float = .05 ):
        super(Shunt, self).__init__(stationid, voltage, nodename, name, "SH", owner)
        
        self.MVar = mvar
        self.RegulationNode = None
        self.RegulationNodeName = regnodename
        self.RegulationNodeID = (stationid, regnodename)
        self.VoltagePUTarget = puvolttarget
        self.VoltageTargetDeviation = deviation
