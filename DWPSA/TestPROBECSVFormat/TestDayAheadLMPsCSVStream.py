import unittest
import io
import os
from PROBECSVFormat.DayAheadLMPsCSVStream import DayAheadLMPsCSVStream
from Network.CPNode import CPNode
from Network.EPNode import EPNode

class TestDayAheadLMPsCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testLoadfilestream.csv"
        lines = [
                    "dayaheadlmps,PROBEMISO,Version 101,24\n",
                    "MKTDAY,PNODEID,PNODENAME,NAME,BUSNAME,VOLTAGE,EQUIP,DZONE,DPRIVATE,CONG_01,LOSS_01,CONG_02,LOSS_02,CONG_03,LOSS_03,CONG_04,LOSS_04,CONG_05,LOSS_05,CONG_06,LOSS_06,CONG_07,LOSS_07,CONG_08,LOSS_08,CONG_09,LOSS_09,CONG_10,LOSS_10,CONG_11,LOSS_11,CONG_12,LOSS_12,CONG_13,LOSS_13,CONG_14,LOSS_14,CONG_15,LOSS_15,CONG_16,LOSS_16,CONG_17,LOSS_17,CONG_18,LOSS_18,CONG_19,LOSS_19,CONG_20,LOSS_20,CONG_21,LOSS_21,CONG_22,LOSS_22,CONG_23,LOSS_23,CONG_24,LOSS_24,AREA,LOADID,UNITID,RESZONEID\n",
                    "20161222,0,REFBUS,REFBUS,REFBUS,ENERGY,LMP,VALUE,1,22.38,0,21.01,0,21.08,0,21.41,0,22.01,0,23.82,0,30.48,0,38.51,0,36.47,0,35.33,0,34.54,0,33.74,0,31.76,0,29.92,0,27.65,0,26.88,0,27.14,0,34.17,0,36.4,0,33.5,0,32.86,0,29.53,0,26.62,0,23.76,0,REFBUS,REFBUS,REFBUS,\n",
                    "20161222,122060562,L CONS ALPENA BANK_2,122033202,ALPENA,138,28,Central,1,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CONS,BANK_2,,3\n",
                    "20161222,767746826,MEC.STORMLK_1,,,,,North,0,-5.63,-3.3,-5.09,-2.59,-4.17,-3.1,-3.64,-3.16,-2,-3.79,-1.49,-2.9,-2.92,-4.37,-2.04,-2.19,1.06,-0.77,2.91,-0.73,2.56,-1.52,3.04,-0.58,1.4,-1.79,0.57,-1.69,-0.02,-1.45,-0.63,-1.82,-2.58,-1.08,-6.56,-0.72,-7.51,-3.57,-10.9,-3.3,-10.74,-2.4,-9.36,-3.69,-6.46,-3.28,-6.01,-2.88,MEC,,,0\n"
                ]
        with open(testfilename, 'w') as file:
            file.writelines(lines)
        with DayAheadLMPsCSVStream(testfilename) as c:
            i = 0
            for pnode in c:
                i+= 1
                if i == 1:
                    epn = c.getPNode()
                    self.assertEqual(type(epn), EPNode)
                    self.assertEqual(epn.ID, 122060562)
                    self.assertEqual(epn.Name, "L CONS ALPENA BANK_2")
                    self.assertEqual(epn.EPNodeID, 122033202)
                    self.assertEqual(epn.NodeID, ("ALPENA","28"))
                    self.assertEqual(epn.LoadUnitName, "BANK_2")
                    self.assertEqual(epn.ReserveZoneID, 3)
                elif i == 2:
                    cpn = c.getPNode()
                    self.assertEqual(type(cpn), CPNode)
                    self.assertEqual(cpn.ID, 767746826)
                    self.assertEqual(cpn.Name, "MEC.STORMLK_1")
                    self.assertEqual(cpn.Settled, True)

        os.remove(testfilename)
        return