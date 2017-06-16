import unittest
import io
import os
from PROBECSVFormat.CostCurvesCSVStream import CostCurvesCSVStream
from Network.MktUnitHourlyOffer import MktUnitHourlyOffer
from Network.BidOfferCurve import BidOfferCurve
from Network.BidOfferCurve import BidOfferPoint
from datetime import datetime

class TestCostCurvesCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testfilestream.csv"
        lines = [
                    "UNITSCHEDULEID,OPERATORNAME,EFFECTIVEHOUR,ECONOMICMIN,ECONOMICMAX,REGMIN,REGMAX,NOLOADCOST,MW1,PRICE1,MW2,PRICE2,MW3,PRICE3,MW4,PRICE4,MW5,PRICE5,MW6,PRICE6,MW7,PRICE7,MW8,PRICE8,MW9,PRICE9,MW10,PRICE10,MW11,PRICE11,COLDNOTIFICATIONTIME,INTERNOTIFICATIONTIME,HOTNOTIFICATIONTIME,COLDSTARTUPTIME,INTERSTARTUPTIME,HOTSTARTUPTIME,COMMITSTATUS,ENGSTATUS,REGSTATUS,SPINSTATUS,SUPPONSTATUS,SUPPOFFSTATUS,REGPRICE,REGMILEAGEPRICE,SPINPRICE,SUPPONPRICE,SUPPOFFPRICE,REGSELFMW,SPINSELFMW,SUPPONSELFMW,SUPPOFFSELFMW,ENSELFMW,RAMPRATE,USEBIDSLOPE,SUPPOFFMAXMW,RAMPCAPSTATUS,EMERGENCYMAX,EMERGENCYMIN,IOH\n",
                    "938501,PRESQUE ISLE 6 (WEPM GO),12/22/2016 00:00,30,55,40,55,290.42,30,21.21,33.1,21.43,36.2,21.66,39.4,21.93,42.5,22.22,45.6,22.53,48.8,22.87,51.9,23.22,55,23.6,,,,,1,1,1,12,10,8,EC,EC,EC,EC,EC,NQ,3.04,0,1.43,0.89,0,1,1,1,,,1,1,30,EC,55,30,973\n",
                    "1104701,UPS2_ST,12/22/2016 21:00,120,235,120,165,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,OU,EC,EC,EC,EC,NQ,,,,,,,,,,,6,0,0,EC,235,120,-133\n"
                ]
        with open(testfilename, 'w') as file:
            file.writelines(lines)
        with CostCurvesCSVStream(testfilename) as c:
            i = 0
            for zonalfactor in c:
                i+= 1
                if i == 1:
                    uho = c.getMktUnitHourlyOffer()
                    self.assertEqual(uho.ColdNotificationTime, 1 )
                    self.assertEqual(uho.ColdStartupTime, 12 )
                    self.assertEqual(uho.CommitStatus, "EC" )
                    self.assertEqual(uho.EcoMax, 55 )
                    self.assertEqual(uho.EcoMin, 30 )
                    self.assertEqual(uho.EmerMax, 55 )
                    self.assertEqual(uho.EmerMin, 30 )
                    self.assertEqual(uho.EnergySelfMW, 0 )
                    self.assertEqual(uho.EnergyStatus, "EC" )
                    self.assertEqual(uho.HotNotificationTime, 1 )
                    self.assertEqual(uho.HotStartupTime, 8 )
                    self.assertEqual(uho.InterNotificationTime, 1 )
                    self.assertEqual(uho.InterStartupTime, 10 )
                    self.assertEqual(uho.MktHour, datetime(2016, 12, 22, 0, 0, 0))
                    self.assertEqual(uho.NoLoadCost, 290.42 )
                    self.assertEqual(uho.RampCapStatus, "EC" )
                    self.assertEqual(uho.RampRate, 1 )
                    self.assertEqual(uho.RegMax, 55 )
                    self.assertEqual(uho.RegMin, 40 )
                    self.assertEqual(uho.RegMileagePrice, 0 )
                    self.assertEqual(uho.RegPrice, 3.04 )
                    self.assertEqual(uho.RegSelfMW, 1 )
                    self.assertEqual(uho.RegStatus, "EC" )
                    self.assertEqual(uho.SpinPrice, 1.43 )
                    self.assertEqual(uho.SpinSelfMW, 1 )
                    self.assertEqual(uho.SpinStatus, "EC" )
                    self.assertEqual(uho.SuppOnPrice, 0.89 )
                    self.assertEqual(uho.SuppOnSelfMW, 1 )
                    self.assertEqual(uho.SuppOnStatus, "EC" )
                    self.assertEqual(uho.SuppOffMaxMW, 30 )
                    self.assertEqual(uho.SuppOffPrice, 0 )
                    self.assertEqual(uho.SuppOffStatus, "NQ" )
                    self.assertEqual(uho.UnitID, 9385 )
                    self.assertEqual(uho.UnitScheduleID, 938501 )
                    self.assertEqual(uho.UseBidSlope, True )
                    self.assertEqual(uho.OfferCurve.getCount(), 9) 
                    self.assertEqual(uho.OfferCurve[1].MW, 30) 
                    self.assertEqual(uho.OfferCurve[1].Price, 21.21) 
                    self.assertEqual(uho.OfferCurve[2].MW, 33.1) 
                    self.assertEqual(uho.OfferCurve[2].Price, 21.43) 
                    self.assertEqual(uho.OfferCurve[3].MW, 36.2) 
                    self.assertEqual(uho.OfferCurve[3].Price, 21.66) 
                    self.assertEqual(uho.OfferCurve[4].MW, 39.4) 
                    self.assertEqual(uho.OfferCurve[4].Price, 21.93) 
                    self.assertEqual(uho.OfferCurve[5].MW, 42.5) 
                    self.assertEqual(uho.OfferCurve[5].Price, 22.22) 
                    self.assertEqual(uho.OfferCurve[6].MW, 45.6) 
                    self.assertEqual(uho.OfferCurve[6].Price, 22.53) 
                    self.assertEqual(uho.OfferCurve[7].MW, 48.8) 
                    self.assertEqual(uho.OfferCurve[7].Price, 22.87) 
                    self.assertEqual(uho.OfferCurve[8].MW, 51.9) 
                    self.assertEqual(uho.OfferCurve[8].Price, 23.22) 
                    self.assertEqual(uho.OfferCurve[9].MW, 55) 
                    self.assertEqual(uho.OfferCurve[9].Price, 23.6) 
                elif i == 2:
                    uho = c.getMktUnitHourlyOffer()
                    self.assertEqual(uho.ColdNotificationTime, 0 )
                    self.assertEqual(uho.ColdStartupTime, 0 )
                    self.assertEqual(uho.CommitStatus, "OU" )
                    self.assertEqual(uho.EcoMax, 235 )
                    self.assertEqual(uho.EcoMin, 120 )
                    self.assertEqual(uho.EmerMax, 235 )
                    self.assertEqual(uho.EmerMin, 120 )
                    self.assertEqual(uho.EnergySelfMW, 0 )
                    self.assertEqual(uho.EnergyStatus, "EC" )
                    self.assertEqual(uho.HotNotificationTime, 0 )
                    self.assertEqual(uho.HotStartupTime, 0 )
                    self.assertEqual(uho.InterNotificationTime, 0 )
                    self.assertEqual(uho.InterStartupTime, 0 )
                    self.assertEqual(uho.MktHour, datetime(2016, 12, 22, 21, 0, 0))
                    self.assertEqual(uho.NoLoadCost, 0 )
                    self.assertEqual(uho.RampCapStatus, "EC" )
                    self.assertEqual(uho.RampRate, 6 )
                    self.assertEqual(uho.RegMax, 165 )
                    self.assertEqual(uho.RegMin, 120 )
                    self.assertEqual(uho.RegMileagePrice, 0 )
                    self.assertEqual(uho.RegPrice, 0 )
                    self.assertEqual(uho.RegSelfMW, 0 )
                    self.assertEqual(uho.RegStatus, "EC" )
                    self.assertEqual(uho.SpinPrice, 0 )
                    self.assertEqual(uho.SpinSelfMW, 0 )
                    self.assertEqual(uho.SpinStatus, "EC" )
                    self.assertEqual(uho.SuppOnPrice, 0 )
                    self.assertEqual(uho.SuppOnSelfMW, 0 )
                    self.assertEqual(uho.SuppOnStatus, "EC" )
                    self.assertEqual(uho.SuppOffMaxMW, 0 )
                    self.assertEqual(uho.SuppOffPrice, 0 )
                    self.assertEqual(uho.SuppOffStatus, "NQ" )
                    self.assertEqual(uho.UnitID, 11047 )
                    self.assertEqual(uho.UnitScheduleID, 1104701 )
                    self.assertEqual(uho.UseBidSlope, False )
                    self.assertEqual(uho.OfferCurve.getCount(), 0) 

        os.remove(testfilename)
        return