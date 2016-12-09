import unittest
import io
import os
from EMSCSVFormat.PhaseShifterCSVStream import PhaseShifterCSVStream
from Network.PhaseShifter import PhaseShifter
from Network.RatingSet import RatingSet
class TestPhaseShifterCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testpsfilestream.csv"
        name = "XF1"
        fnd = "N1"
        owner = "ABC"
        st = "ST"
        tnd = "N2"
        fkv = "115"
        tkv = "365"
        mon = "TrUe"
        r = "0.004"
        x = "0.0001"
        sn = "400"
        se = "600.2"
        wn = "500.1"
        we = "700.5"
        avr = 4
        regnd = "RN"
        ftpt = "TT1"
        ftpn = 3
        ttpt = "TT2"
        ttpn = 4
        ptt = "PT1"
        awr = "T"

        with open(testfilename, 'w') as file:
            file.write("Company,Division,Station,TransformerName,FromNode,FromNominalVoltage,FromLTCTapType,FromNormalPosition,ToConnectionNode,ToNominalVoltage,ToLTCTapType,ToNormalTap,RegulationNode,r,x,VoltageRegulationSchedule,AVRStatus,PhaseTapType,AWRStatus,MWRegulationSchedule,Summer Normal,Summer Emergency,Winter Normal,Winter Emergency,changed")

        with PhaseShifterCSVStream(testfilename) as c:
            c.FromNodeName = fnd
            c.StationName = st
            c.FromTapNormPosition = ftpn
            c.FromTapType = ftpt
            c.FromVoltage = fkv
            c.PhaseShifterName = name
            c.Owner = owner
            c.r = r
            c.SumEmer = se
            c.SumNorm = sn
            c.ToNodeName = tnd
            c.ToTapNormPosition = ttpn
            c.ToTapType = ttpt
            c.ToVoltage = tkv
            c.x = x
            c.WinEmer = we
            c.WinNorm = wn
            c.PhaseTapType = ptt
            c.AWRStatus = awr

            self.assertEqual(c.getPhaseShifterName(), name)
            self.assertEqual(c.getFromNodeName(), fnd)
            self.assertEqual(c.getOwner(), owner)
            self.assertEqual(c.getToNodeName(), tnd)
            self.assertEqual(c.getx(), float(x))
            self.assertEqual(c.getr(), float(r))
            self.assertEqual(c.getSummerRatings().Normal, float(sn))
            self.assertEqual(c.getSummerRatings().Emergency, float(se))
            self.assertEqual(c.getWinterRatings().Normal, float(wn))
            self.assertEqual(c.getWinterRatings().Emergency, float(we))
            self.assertEqual(c.getAWRStatus(), True)
            self.assertEqual(c.getPhaseTapType(), ptt)


            ps = c.getPhaseShifter()
            self.assertEqual(ps.ID, (st, name, name))

        os.remove(testfilename)
        return