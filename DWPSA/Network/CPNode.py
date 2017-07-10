from Network.PNode import PNode

class CPNode(PNode):
    """Commercial Pricing Node in a Power System is defined as an aggregate of other PNodes"""

   #Constructor
    def __init__(self, id: int, name: str, settled: bool):
        super(CPNode, self).__init__(id, name)
        """CPNode Constructor"""
        
        #Attributes
        self.FactorSum = 0.0
        self.Settled = settled
        self.PNodeFactors = {}
        self.PNodes = {}
        self.MktUnits = {}
        self.MktBids = {}

    #Methods
    def AddPnodeFactor(self, pnode: PNode, factor: float):
        if pnode.ID in self.PNodeFactors:
            raise Exception("PNode factor already exists for the CPNode ", self.Name)
        if pnode.ID == self.ID:
            raise Exception("PNode factor cannot have the same ID as CPNode", self.Name)
        self.PNodeFactors[pnode.ID] = factor
        self.PNodes[pnode.ID] = pnode
        self.FactorSum += factor

    def AddMktUnit(self, mu):
        self.MktUnits[mu.ID] = mu
 
    def AddMktBid(self, mb):
        self.MktBids[mb.ID] = mb

    def GetNormalizedPNodeFactors(self):
        NormalizedPNodeFactors = {}
        if self.FactorSum == 0:
            raise Exception("Pnode Factor total is 0", self.Name)
        for pid in self.PNodeFactors.keys():
            NormalizedPNodeFactors[pid] = self.PNodeFactors[pid] / self.FactorSum

        return NormalizedPNodeFactors
    def __repr__(self):
        return "[" + self.ID + "] " + self.Name
    def __str__(self):
        return "[{0}] {1}".format(self.ID, self.Name)

    def GetVariableName(self):
        return "CPN_{0}".format(
            self.Name.replace("-","_d_").replace(".","__")
            )

    def Copy(self):
        return CPNode(self.ID, self.Name, self.Settled)