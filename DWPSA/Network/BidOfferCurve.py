from math import *
class BidOfferPoint(object):
    """Bid or Offer Price MW pair"""

    #Constructor
    def __init__(self, price: float, mw: float):
        self.Price = price
        self.MW = mw

class BidOfferCurve(object):
    """Collection of BidOfferPoints that form a curve"""

    #Constructor
    def __init__(self, bidpointsareindependant = False):
        self.Curve = {}
        self.IndependantBidPoints = bidpointsareindependant

    def __getitem__(self, key) -> BidOfferPoint:
        if (key) not in self.Curve.keys(): 
            raise Exception("BidOfferCurve does not contain Point ", key)
        return self.Curve[key]

    def __setitem__(self, key, value):
        if type(value) is not BidOfferPoint:
            raise Exception("Value provided was not type BidOfferPoint")
        self.Curve[key] = value

    def getCount(self):
        return len(self.Curve)
    def AddPoint(self, price: float, mw: float):
        self.Curve[self.getCount() + 1] = BidOfferPoint(price, mw)

    @property
    def MaxMW(self):
        if self.IndependantBidPoints:
            maxmw = 0
            for i in range(1, self.getCount()+1):
                maxmw += self[i].MW
        else:
            maxmw = -99999
            for i in range(1, self.getCount()+1):
                if self[i].MW > maxmw: maxmw = self[i].MW
        return maxmw

    @property
    def MinMW(self):
        minmw = 99999
        for i in range(1, self.getCount()+1):
            if self[i].MW < minmw: minmw = self[i].MW
        return minmw

    def ToArray(self, sortincreasing = True, maxdecimals = 2) -> [(float,float)]:
        curvearray = []
        if self.IndependantBidPoints:
            mwtotal = 0.0
            used = []
            nexti = -1
            while len(used) != self.getCount():
                bestprice = 999999 if sortincreasing else -999999
                for i in range(1, self.getCount()+1):
                    if i not in used:
                        if (sortincreasing and  self[i].Price < bestprice) or (not sortincreasing and self[i].Price > bestprice):
                            nexti = i
                            bestprice = self[i].Price
                used.append(nexti)
                mwtotal += self[nexti].MW
                curvearray.append((round(mwtotal,maxdecimals), round(self[nexti].Price,maxdecimals)))
        else:
            for i in range(1, self.getCount()+1):
                curvearray.append((self[i].MW, self[i].Price))
        return curvearray

