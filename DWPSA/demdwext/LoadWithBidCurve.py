import cvxpy as cvx
from dem.devices import *

class LoadWithBidCurve(Device):
    """Load withy cost function specified by bid curve.
    """
    def __init__(self, bid_curve=[],              
            power_max=None,
            name=None):
        super(LoadWithBidCurve, self).__init__([Terminal()], name)
        self.bid_curve = bid_curve
        self.power =0
        self.power_max=power_max

    @property
    def constraints(self):
        p = self.terminals[0].power_var

        constraints = []
        constraints += [p >= 0]
        if self.power_max is not None:
            constraints += [p <= self.power_max]

        return constraints
    @property
    def cost(self):
        if len(self.bid_curve) == 0: return cvx.Constant(0)
        p = self.terminals[0].power_var
        segments = [p*-self.bid_curve[0][1]]
        if len(self.bid_curve) == 1:
            return segments[0]
        offset = -self.bid_curve[0][1] * self.bid_curve[0][0]
        for i in range(len(self.bid_curve)-1):
            b = -self.bid_curve[i+1][1]
            segments.append(b*(p - self.bid_curve[i][0]) + offset)
            offset += b*(self.bid_curve[i+1][0] - self.bid_curve[i][0])
        return cvx.max_elemwise(*segments)
#gen = GeneratorWithBidCurve(
#    no_load_cost=290.42,
#    bid_curve=[
#        (30, 21.21),
#        (33.1, 21.43),
#        (36.2, 21.66),
#        (39.4, 21.93),
#        (42.5, 22.22),
#        (45.6, 22.53),
#        (48.8, 22.87),
#        (51.9, 23.22),
#        (55, 23.6)])
#fload = FixedLoad(32)
#load = LoadWithBidCurve(
#    bid_curve=[
#        (1, 33),
#        (2, 32),
#        (3, 30),
#        (4, 28),
#        (5, 25),
#        (6, 24),
#        (7, 23),
#        (8, 22),
#        (10, 20.9)], power_max=10)
#net = Net([gen.terminals[0], load.terminals[0], fload.terminals[0]])

#network = Group([gen, load, fload], [net])

#print(network.optimize())