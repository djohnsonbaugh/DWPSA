import unittest
import io
import os
from PROBECSVFormat.DemandBidsCSVStream import DemandBidsCSVStream
from Network.MktBid import *
from Network.BidOfferCurve import BidOfferCurve
from Network.BidOfferCurve import BidOfferPoint
from datetime import datetime

class TestDemandBidsCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testfilestream.csv"
        lines = [
                    "BIDID,PNODEID,PNODENAME,PARTICIPANTNAME,BIDTYPE,LOCALMKTHOUR,PARENTOWNER,MW1,PRICE1,MW2,PRICE2,MW3,PRICE3,MW4,PRICE4,MW5,PRICE5,MW6,PRICE6,MW7,PRICE7,MW8,PRICE8,MW9,PRICE9,MW10,PRICE10,MW11,PRICE11,MW12,PRICE12,MW13,PRICE13,MW14,PRICE14,MW15,PRICE15,MW16,PRICE16,MW17,PRICE17,MW18,PRICE18,MW19,PRICE19,MW20,PRICE20\n",
                    "1961726401,767746826,MEC.STORMLK_1,ALME,Decrement,12/22/2016 01:00,,3.6,33.66,3.6,39.66,3.6,45.66,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n",
                    "1961726151,529571451,ALTW.TOI_2.3,ALME,Increment,12/22/2016 03:00,,2.2,8.52,2.2,3.52,2.2,-11.48,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n"
                    "1656072146,1656072145,SME.SME_LOAD,,Fixed Demand,12/22/2016 00:00,,690,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n"
                    "1656072147,1656072145,SME.SME_LOAD,,Price Sensitive Demand,12/22/2016 23:00,,2,47.5,2,47.13,28,23.7,27,23.6,1,-500,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n"
                ]
        with open(testfilename, 'w') as file:
            file.writelines(lines)
        with DemandBidsCSVStream(testfilename) as c:
            i = 0
            for bids in c:
                i += 1
                if i == 1:
                    mb = c.getMktBid()
                    d = datetime(2016, 12, 22, 1, 0, 0)
                    self.assertEqual(mb.ID, 1961726401)
                    self.assertEqual(mb.CPNodeID, 767746826)
                    self.assertEqual(mb.Participant, "ALME")
                    self.assertEqual(mb.BidType, MktBidType.Decrement)

                    self.assertEqual(mb.BidCurves[d][1].MW, 3.6) 
                    self.assertEqual(mb.BidCurves[d][1].Price, 33.66) 
                    self.assertEqual(mb.BidCurves[d][2].MW, 3.6) 
                    self.assertEqual(mb.BidCurves[d][2].Price, 39.66) 
                    self.assertEqual(mb.BidCurves[d][3].MW, 3.6)
                    self.assertEqual(mb.BidCurves[d][3].Price, 45.66)
                    self.assertEqual(mb.BidCurves[d].ToArray(sortincreasing=False), [(3.6, 45.66),(7.2, 39.66),(10.8, 33.66)]) 
                elif i == 2:
                    mb = c.getMktBid()
                    d = datetime(2016, 12, 22, 3, 0, 0)
                    self.assertEqual(mb.ID, 1961726151)
                    self.assertEqual(mb.CPNodeID, 529571451)
                    self.assertEqual(mb.Participant, "ALME")
                    self.assertEqual(mb.BidType, MktBidType.Increment)


                    self.assertEqual(mb.BidCurves[d][1].MW, 2.2) 
                    self.assertEqual(mb.BidCurves[d][1].Price, 8.52) 
                    self.assertEqual(mb.BidCurves[d][2].MW, 2.2) 
                    self.assertEqual(mb.BidCurves[d][2].Price, 3.52) 
                    self.assertEqual(mb.BidCurves[d][3].MW, 2.2)
                    self.assertEqual(mb.BidCurves[d][3].Price, -11.48)
                    self.assertEqual(mb.BidCurves[d].ToArray(), [(2.2, -11.48),(4.4, 3.52),(6.6, 8.52)]) 
                elif i == 3:
                    mb = c.getMktBid()
                    d = datetime(2016, 12, 22, 0, 0, 0)
                    self.assertEqual(mb.ID, 1656072146)
                    self.assertEqual(mb.CPNodeID, 1656072145)
                    self.assertEqual(mb.Participant, "")
                    self.assertEqual(mb.BidType, MktBidType.FixedDemand)
                    self.assertEqual(mb.FixedLoad[d], 690)
                elif i == 4:
                    mb = c.getMktBid()
                    d = datetime(2016, 12, 22, 23, 0, 0)
                    self.assertEqual(mb.ID, 1656072147)
                    self.assertEqual(mb.CPNodeID, 1656072145)
                    self.assertEqual(mb.Participant, "")
                    self.assertEqual(mb.BidType, MktBidType.PriceSensitiveDemand)


                    self.assertEqual(mb.BidCurves[d][1].MW, 2) 
                    self.assertEqual(mb.BidCurves[d][1].Price, 47.5) 
                    self.assertEqual(mb.BidCurves[d][2].MW, 2) 
                    self.assertEqual(mb.BidCurves[d][2].Price, 47.13) 
                    self.assertEqual(mb.BidCurves[d][3].MW, 28)
                    self.assertEqual(mb.BidCurves[d][3].Price, 23.7) 
                    self.assertEqual(mb.BidCurves[d][4].MW, 27) 
                    self.assertEqual(mb.BidCurves[d][4].Price, 23.6) 
                    self.assertEqual(mb.BidCurves[d][5].MW, 1) 
                    self.assertEqual(mb.BidCurves[d][5].Price, -500) 
                    self.assertEqual(mb.BidCurves[d].ToArray(sortincreasing=False), [(2, 47.5),(4, 47.13),(32, 23.7),(59, 23.6),(60, -500)]) 

        os.remove(testfilename)
        return