import unittest
import io
import os
from EMSCSVFormat.ShuntCSVStream import ShuntCSVStream
from Network.Shunt import Shunt
import math
class TestShuntCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testShuntfilestream.csv"
        shuntname = "SH1"
        nd = "N1"
        rnd = "N2"
        owner = "ABC"
        st = "ST"
        kv = "115"
        mvar = "100.2"
        vt = "1.1"
        dev = "0.1"
        with open(testfilename, 'w') as file:
            file.write("Company,Station,KV,Shunt Name,Node,Regulation Node,Nominal MVar,Voltage Target PU,Deviation,Changed")

        with ShuntCSVStream(testfilename) as c:
            c.ShuntName = shuntname
            c.VoltagePUTarget = vt
            c.VoltageTargetDeviation = dev
            c.MVar = mvar
            c.NodeName = nd
            c.RegNodeName = rnd
            c.Owner = owner
            c.StationName = st
            c.Voltage = kv

            self.assertEqual(c.getShuntName(), shuntname)
            self.assertEqual(c.getVoltagePUTarget(), float(vt))
            self.assertEqual(c.getVoltageTargetDeviation(), float(dev))
            self.assertEqual(c.getNodeName(), nd)
            self.assertEqual(c.getRegNodeName(), rnd)
            self.assertEqual(c.getOwner(), owner)
            self.assertEqual(c.getMVar(), float(mvar))
            self.assertEqual(c.getStationName(), st)
            self.assertEqual(c.getVoltage(), kv)

            sh = c.getShunt()
            self.assertEqual(sh.ID, (st, shuntname, "SH"))

        os.remove(testfilename)
        return