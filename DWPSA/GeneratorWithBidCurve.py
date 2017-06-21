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
    def __init__(self, no_load_cost=0, bid_curve=[],             
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

    @property
    def cost(self):
        p = -self.terminals[0].power_var

        segments = [cvx.Constant(self.no_load_cost)]
        prev_power = 0
        prev_price = 0
        offset = self.no_load_cost
        for power, price in self.bid_curve[1:]:
            if self.power_min != None:
                if power > self.power_min and prev_power == 0:
                    offset += (self.power_min)*price
                    segments.append(price*(p - self.power_min) + offset)
                    prev_power = self.power_min
                    prev_price = price
            offset += (power - prev_power)*prev_price
            segments.append(price*(p - power) + offset)
            prev_power = power
            prev_price = price
        if self.power_max != None:
            if prev_power < self.power_max:
                offset += (self.power_max - prev_power)*prev_price
                segments.append(prev_price*(p - self.power_max) + offset)

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