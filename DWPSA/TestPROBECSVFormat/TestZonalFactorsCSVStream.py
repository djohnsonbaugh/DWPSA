import unittest
import io
import os
from PROBECSVFormat.ZonalFactorsCSVStream import ZonalFactorsCSVStream

class TestZonalFactorsCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testfilestream.csv"
        lines = [
                    "AGGREGATEDPNODEID,AGGPNODENAME,PNODEID,PNODENAME,FACTOR\n",
                    "767746826,MEC.STORMLK_1,122070026,U MEC BVISTA BVISTA_1_UNIT,1\n",
                    "619071935,MGE.DRR.DG01,158830287,L MGE AMERICN AMN_MGE_TR1,0.02236\n"
                ]
        with open(testfilename, 'w') as file:
            file.writelines(lines)
        with ZonalFactorsCSVStream(testfilename) as c:
            i = 0
            for zonalfactor in c:
                i+= 1
                if i == 1:
                    self.assertEqual(c.getCPNodeID(), 767746826)
                    self.assertEqual(c.getPNodeID(), 122070026)
                    self.assertEqual(c.getFactor(), 1)
                elif i == 2:
                    self.assertEqual(c.getCPNodeID(), 619071935)
                    self.assertEqual(c.getPNodeID(), 158830287)
                    self.assertEqual(c.getFactor(), 0.02236)

        os.remove(testfilename)
        return