import unittest
import io
import os
from EMSCSVFormat.LoadCSVStream import LoadCSVStream
from Network.Load import Load
import math
class TestLoadCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testLoadfilestream.csv"
        loadname = "L1"
        nd = "N1"
        owner = "ABC"
        st = "ST"
        kv = "115"
        mw = "100.2"
        pf = ".95"
        mwnon = "5.3"
        mvnon = "1"
        with open(testfilename, 'w') as file:
            file.write("Company,Station ,KV  ,Node Name,PTI Name    ,PTI Number,Load Name     ,MW NonConforming,MVar NonConforming,MW Conforming,Power Factor Conforming,Load Area,Load Control Area,Changed")

        with LoadCSVStream(testfilename) as c:
            c.LoadName = loadname
            c.MWNonCon = mwnon
            c.MVNonCon = mvnon
            c.MWCon = mw
            c.NodeName = nd
            c.Owner = owner
            c.PowerFactorCon = pf
            c.StationName = st
            c.Voltage = kv

            self.assertEqual(c.getLoadName(), loadname)
            self.assertEqual(c.getMWNonCon(), float(mwnon))
            self.assertEqual(c.getMVNonCon(), float(mvnon))
            self.assertEqual(c.getMWCon(), float(mw))
            self.assertEqual(c.getNodeName(), nd)
            self.assertEqual(c.getOwner(), owner)
            self.assertEqual(c.getPowerFactorCon(), float(pf))
            self.assertEqual(c.getStationName(), st)
            self.assertEqual(c.getVoltage(), kv)
            self.assertEqual(c.getMVCon(), math.sqrt((float(mw)/float(pf))**2 - (float(mw))**2))

            ld = c.getLoad()
            self.assertEqual(ld.ID, (st, loadname, "LD"))

        os.remove(testfilename)
        return