from Network.Unit import *
from datetime import datetime
from Network.BidOfferCurve import BidOfferCurve

class MktUnitHourlyOffer(object):
    """Hourly Unit Offer Data"""

    def __init__(self, unitid: int, unitscheduleid: int, mkthour: datetime, offercurve: BidOfferCurve, usebidslope: bool, noloadcost: float,
                  coldnottime: float, intnottime: float, hotnottime: float, coldstuptime: float, intstuptime: float, hotstuptime: float,
                  ecomax: float, ecomin: float, emermax: float, emermin: float, regmax: float, regmin: float, ramprate: float,
                  commitstaus: str, enstatus: str, rampcapstatus: str, regstatus: str, spinstatus: str, suponstatus: str,supoffstatus: str,
                  regmilprice: float, regprice: float, spinprice: float, suponprice: float, supoffprice: float,  
                  enselfmw: float, regselfmw: float, spinselfmw: float, suponselfmw: float, supoffmaxmw: float):
        self.ColdNotificationTime = coldnottime
        self.ColdStartupTime = coldstuptime
        self.CommitStatus = commitstaus
        self.EcoMax = ecomax
        self.EcoMin = ecomin
        self.EmerMax = emermax
        self.EmerMin = emermin
        self.EnergySelfMW = enselfmw
        self.EnergyStatus = enstatus
        self.HotNotificationTime = hotnottime
        self.HotStartupTime = hotstuptime
        self.InterNotificationTime = intnottime
        self.InterStartupTime = intstuptime
        self.MktHour = mkthour
        self.NoLoadCost = noloadcost
        self.OfferCurve = offercurve
        self.RampCapStatus = rampcapstatus
        self.RampRate = ramprate
        self.RegMax = regmax
        self.RegMin = regmin
        self.RegMileagePrice = regmilprice
        self.RegPrice = regprice
        self.RegSelfMW = regselfmw
        self.RegStatus = regstatus
        self.SpinPrice = spinprice
        self.SpinSelfMW = spinselfmw
        self.SpinStatus = spinstatus
        self.SuppOnPrice = suponprice
        self.SuppOnSelfMW = suponselfmw
        self.SuppOnStatus = suponstatus
        self.SuppOffMaxMW = supoffmaxmw
        self.SuppOffPrice = supoffprice
        self.SuppOffStatus = supoffstatus
        self.UnitID = unitid
        self.UnitScheduleID = unitscheduleid
        self.UseBidSlope = usebidslope