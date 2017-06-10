import unittest
import io
import os
from EMSCSVFormat.UnitCSVStream import UnitCSVStream
from Network.Unit import Unit
class TestUnitCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testUnitfilestream.csv"
        unitname = "SH1"
        nd = "N1"
        rnd = "N2"
        owner = "ABC"
        st = "ST"
        kv = "115"
        mwma = "100.2"
        mwmi = "50"
        mvma = "20"
        mvmi = "-20"
        pf = ".98"
        mw = "75"
        vt = "1.1"
        dev = "0.1"
        noagc = "TrUe"
        with open(testfilename, 'w') as file:
            file.write("Company,Station,KV,UnitName,Connection Node, Regulation Node,BaseM,Participation Factor,MW Max,MW MN,Mvar Max,Mvar Min,Voltage Tartet(PU),Deviation,Mvar Capability Curve,NOAGC,Changed")

        with UnitCSVStream(testfilename) as c:
            c.UnitName = unitname
            c.InitialMW = mw
            c.MVarMax = mvma
            c.MVarMin = mvmi
            c.MWMax = mwma
            c.MWMin = mwmi
            c.NoAGC = noagc
            c.ParticipationFactor = pf
            c.VoltagePUTarget = vt
            c.VoltageTargetDeviation = dev
            c.NodeName = nd
            c.RegNodeName = rnd
            c.Owner = owner
            c.StationName = st
            c.Voltage = kv

            self.assertEqual(c.getUnitName(), unitname)
            self.assertEqual(c.getVoltagePUTarget(), float(vt))
            self.assertEqual(c.getVoltageTargetDeviation(), float(dev))
            self.assertEqual(c.getNodeName(), nd)
            self.assertEqual(c.getRegNodeName(), rnd)
            self.assertEqual(c.getOwner(), owner)
            self.assertEqual(c.getMVarMax(), float(mvma))
            self.assertEqual(c.getMVarMin(), float(mvmi))
            self.assertEqual(c.getMWMax(), float(mwma))
            self.assertEqual(c.getMWMin(), float(mwmi))
            self.assertEqual(c.getParticipationFactor(), float(pf))
            self.assertEqual(c.getInitialMW(), float(mw))
            self.assertEqual(c.getStationName(), st)
            self.assertEqual(c.getVoltage(), kv)

            un = c.getUnit()
            self.assertEqual(un.ID, (st, unitname, "UN"))

        os.remove(testfilename)
        return