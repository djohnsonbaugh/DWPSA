class BidOfferPoint(object):
    """Bid or Offer Price MW pair"""

    #Constructor
    def __init__(self, price: float, mw: float):
        self.Price = price
        self.MW = mw

class BidOfferCurve(object):
    """Collection of BidOfferPoints that form a curve"""

    #Constructor
    def __init__(self):
        self.Curve = {}

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


