import unittest
import io
import os
from PROBECSVFormat.BidDataCSVStream import BidDataCSVStream
from Network.UnitDailyOffer import UnitDailyOffer

class TestBidDataCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testfilestream.csv"
        lines = [
                    "PNODEID,UNITID,OPERATORNAME,UNITTYPE,UNITSHEDULEID,SCHEDULESHORTNAME,OPERATING_RATE,MAX_MW,MIN_RUN_TIME_HOURS,MIN_DOWN_TIME_HOURS,COLDNOTIFICATIONTIME,INTERNOTIFICATIONTIME,HOTNOTIFICATIONTIME,COLDSTARTUPCOST,INTERSTARTUPCOST,HOTSTARTUPCOST,HOTTOINTERTIME,HOTTOCOLDTIME,COLDSTARTUPTIME,INTERSTARTUPTIME,HOTSTARTUPTIME,MAXRUN,EMERMAX,ECONMAX,ECONMIN,EMERMIN,MAXSTDAY,MAXSTWEEK,NOLOADCOST,CURRENTSTDAY,CURRENTSTARTWEEK,MIN_POINT,DEFAULT_RAMP_RATE,PARTICIPANTNAME,USEBIDSLOPE,USESTARTUPNOLOAD,PARENTOWNER,MMU_FUEL_TYPE,QUICKSTARTQUALIFIED,SCHEDULETYPE,ACTIVESCHEDULE,DARAMPUPQUALIFIED,DARAMPDOWNQUALIFIED,INTERMITTENT,RAMPCAPQUALIFIED\n",
                    "2226460307,9385,PRESQUE ISLE 6 (WEPM GO),Steam,938501,DA P1PRI,,0,24,12,,,,9130.84,7399.6,4398.79,12,24,,,,83333.32,,,,,1,1,,0,0,,,MIUP,,1,,,0,price,1,1,1,0,1\n",
                    "2632449894,10477,PRAIRIE STATE 1 JOU IMPA (PRAR STE),Steam,1047701,DA P1UN1,,2640,13.5,10,,,,0,0,0,18,48,,,,999,,,,,1,3,,0,0,,,AMIL,,1,,,0,price,1,1,1,0,1\n,"
                ]
        with open(testfilename, 'w') as file:
            file.writelines(lines)
        with BidDataCSVStream(testfilename) as c:
            i = 0
            for zonalfactor in c:
                i+= 1
                if i == 1:
                    self.assertEqual(c.getUnitScheduleID(), 938501)
                    self.assertEqual(c.getUnitType(), "Steam")
                    self.assertEqual(c.getOperatorName(), "PRESQUE ISLE 6 (WEPM GO)")
                    udo = c.getUnitDailyOffer()

                    self.assertEqual(udo.ActiveSchedule, True)
                    self.assertEqual(udo.ColdStartupCost, 9130.84)
                    self.assertEqual(udo.DARampUpQualified, True)
                    self.assertEqual(udo.DARampDownQualified, True)
                    self.assertEqual(udo.HotStartupCost, 4398.79)
                    self.assertEqual(udo.HotToColdTime, 24)
                    self.assertEqual(udo.HotToInterTime, 12)
                    self.assertEqual(udo.Intermittent, False)
                    self.assertEqual(udo.InterStartupCost, 7399.6)
                    self.assertEqual(udo.MaxRunTime, 83333.32)
                    self.assertEqual(udo.MinDownTime, 12)
                    self.assertEqual(udo.MinRunTime, 24)
                    self.assertEqual(udo.MaxEnergy, 0)
                    self.assertEqual(udo.Participant, "MIUP")
                    self.assertEqual(udo.CPNodeID, 2226460307)
                    self.assertEqual(udo.QuickStartQualified, False)
                    self.assertEqual(udo.RampCapQualified, True)
                    self.assertEqual(udo.UnitID, 9385)
                    self.assertEqual(udo.UseStartupNoLoad, True)
                elif i == 2:

                    self.assertEqual(c.getOperatorName(), "PRAIRIE STATE 1 JOU IMPA (PRAR STE)")
                    self.assertEqual(c.getUnitScheduleID(), 1047701)
                    self.assertEqual(c.getUnitType(), "Steam")
                    udo = c.getUnitDailyOffer()

                    self.assertEqual(udo.ActiveSchedule, True)
                    self.assertEqual(udo.ColdStartupCost, 0)
                    self.assertEqual(udo.DARampUpQualified, True)
                    self.assertEqual(udo.DARampDownQualified, True)
                    self.assertEqual(udo.HotStartupCost, 0)
                    self.assertEqual(udo.HotToColdTime, 48)
                    self.assertEqual(udo.HotToInterTime, 18)
                    self.assertEqual(udo.Intermittent, False)
                    self.assertEqual(udo.InterStartupCost, 0)
                    self.assertEqual(udo.MaxRunTime, 999)
                    self.assertEqual(udo.MinDownTime, 10)
                    self.assertEqual(udo.MinRunTime, 13.5)
                    self.assertEqual(udo.MaxEnergy, 2640)
                    self.assertEqual(udo.Participant, "AMIL")
                    self.assertEqual(udo.CPNodeID, 2632449894)
                    self.assertEqual(udo.QuickStartQualified, False)
                    self.assertEqual(udo.RampCapQualified, True)
                    self.assertEqual(udo.UnitID, 10477)
                    self.assertEqual(udo.UseStartupNoLoad, True)

        os.remove(testfilename)
        return