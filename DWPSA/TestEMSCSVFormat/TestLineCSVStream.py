import unittest
import io
import os
from EMSCSVFormat.LineCSVStream import LineCSVStream
from Network.Branch import Branch
from Network.RatingSet import RatingSet
class TestLineCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testlinefilestream.csv"
        name = "L1"
        seg = "1"
        fnd = "N1"
        owner = "ABC"
        fst = "ST1"
        tst = "ST2"
        tnd = "N2"
        kv = "115"
        mon = "TrUe"
        r = "0.004"
        x = "0.0001"
        sn = "400"
        se = "600.2"
        wn = "500.1"
        we = "700.5"
        with open(testfilename, 'w') as file:
            file.write("LINE_NDX,ZBR_NDX,FROM_CO,FROM_ST ,FROM_KV,FROM_ND,FROM_PTINAM,FROM_PTINUM,TO_CO,TO_ST   ,TO_KV,TO_ND,TO_PTINAM   ,TO_PTINUM,Line_Name     ,Segment Name,r,x,bch,CO_OWNER,Summer Normal rating,Summer Emergency rating,Winter Normal rating,Winter Emergency rating,Changed,Monitored")

        with LineCSVStream(testfilename) as c:
            c.FromNodeName = fnd
            c.FromStationName = fst
            c.FromVoltage = kv
            c.LineName = name
            c.Monitored = mon
            c.Owner = owner
            c.r = r
            c.Segment = seg
            c.SumEmer = se
            c.SumNorm = sn
            c.ToNodeName = tnd
            c.ToStationName = tst
            c.ToVoltage = kv
            c.x = x
            c.WinEmer = we
            c.WinNorm = wn

            self.assertEqual(c.getLineName(), name)
            self.assertEqual(c.getSegment(), seg)
            self.assertEqual(c.getFromNodeName(), fnd)
            self.assertEqual(c.getOwner(), owner)
            self.assertEqual(c.getToNodeName(), tnd)
            self.assertEqual(c.getx(), float(x))
            self.assertEqual(c.getr(), float(r))
            self.assertEqual(c.getMonitored(), True)
            self.assertEqual(c.getSummerRatings().Normal, float(sn))
            self.assertEqual(c.getSummerRatings().Emergency, float(se))
            self.assertEqual(c.getWinterRatings().Normal, float(wn))
            self.assertEqual(c.getWinterRatings().Emergency, float(we))


            br = c.getBranch()
            self.assertEqual(br.ID, (fst, name, seg))

        os.remove(testfilename)
        return