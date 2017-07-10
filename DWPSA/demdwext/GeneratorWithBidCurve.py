"""An example of generator with cost function specified by bid curve."""

import cvxpy as cvx
from dem import *

class GeneratorWithBidCurve(Generator):
    """Generators with cost function specified by bid curve.
    Cost function will have the form:
       max(cost0, a_1*p + b_1, ..., a_N*p + b_N),
    where a_i is the price for bid curve segment i and b_i is the appropriate
    offset, depending on previous segments.
    """
    def __init__(self, no_load_cost=0, bid_curve=[], use_bid_slope=False,             
            power_min=None,
            power_max=None,
            ramp_min=None,
            ramp_max=None,
            power_init=0, name=None):
        super(GeneratorWithBidCurve, self).__init__(
            power_min=power_min,
            power_max=power_max,
            ramp_min=ramp_min,
            ramp_max=ramp_max,
            power_init=power_init, 
            name=name)
        self.no_load_cost = no_load_cost
        self.bid_curve = bid_curve
        self.use_bid_slope = use_bid_slope
        self.power =0

    @property
    def cost(self):
        noload = cvx.Constant(self.no_load_cost) 
        if len(self.bid_curve) == 0: return noload
        p = -self.terminals[0].power_var
        offset = self.no_load_cost
        segments = [offset + p*self.bid_curve[0][1]]
        if len(self.bid_curve) == 1:
            return segments[0]
        offset += self.bid_curve[0][1] * self.bid_curve[0][0]
        for i in range(len(self.bid_curve)-1):
            b = self.bid_curve[i+1][1]
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
#load = FixedLoad(power=43)
#net = Net([gen.terminals[0], load.terminals[0]])

#network = Group([gen, load], [net])
#print(network.optimize())