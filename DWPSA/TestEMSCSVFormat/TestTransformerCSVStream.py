import unittest
import io
import os
from EMSCSVFormat.TransformerCSVStream import TransformerCSVStream
from Network.Transformer import Transformer
from Network.RatingSet import RatingSet
class TestTransformerCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testxffilestream.csv"
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

        with open(testfilename, 'w') as file:
            file.write("ID_CO,ID_DV,ID_ST,ID,From Connection Node (LTC SIDE),From Nominal Voltage (LTC SIDE),From Tap Type (LTC SIDE),From Normal Position (LTC SIDE),To Connection Node (FIXED SIDE),To Nominal KV (FIXED SIDE),To Tap Type (FIXED SIDE),To Normal Tap (FIXED SIDE),Regulation Node,r,x,Regulation Schedule,AVR Status,SummerNormalLimit,SummerEmergencyLimit,WinterNormalLimit,WinterEmergencyLimit,Changed,Monitored")

        with TransformerCSVStream(testfilename) as c:
            c.FromNodeName = fnd
            c.StationName = st
            c.FromTapNormPosition = ftpn
            c.FromTapType = ftpt
            c.FromVoltage = fkv
            c.TransformerName = name
            c.Monitored = mon
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


            self.assertEqual(c.getTransformerName(), name)
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


            xf = c.getTransformer()
            self.assertEqual(xf.ID, (st, name, name))

        os.remove(testfilename)
        return