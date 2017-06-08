from Network.PNode import PNode
class CPNode(PNode):
    """Commercial Pricing Node in a Power System is defined as an aggregate of other PNodes"""

   #Constructor
    def __init__(self, id: int, name: str, settled: bool, reservezoneid: int):
        super(CPNode, self).__init__(id, name)
        """CPNode Constructor"""
        
        #Attributes
        self.FactorSum = 0.0
        self.Settled = settled
        self.ReserveZoneID = reservezoneid
        self.PNodeFactors = {}


    #Methods
    def AddPnodeFactor(self, pnode: PNode, factor: float):
        if pnode.ID in self.PNodeFactors:
            raise Exception("PNode factor already exists for the CPNode ", self.Name)
        if pnode.ID == self.ID:
            raise Exception("PNode factor cannot have the same ID as CPNode", self.Name)
        self.PNodeFactors[pnode.ID] = factor
        self.FactorSum += factor

 
    def GetNormalizedPNodeFactors(self):
        NormalizedPNodeFactors = {}
        if self.FactorSum == 0:
            raise Exception("Pnode Factor total is 0", self.Name)
        for pid in self.PNodeFactors.keys():
            NormalizedPNodeFactors[pid] = self.PNodeFactors[pid] / self.FactorSum

        return NormalizedPNodeFactors
