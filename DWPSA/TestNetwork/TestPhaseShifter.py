import unittest
from Network.PhaseShifter import PhaseShifter
from Network.RatingSet import RatingSet

class TestPhaseShifter(unittest.TestCase):
    def test_Constructor(self):
        st = "S1"
        fkv = "161"
        fnd = "N1"
        tkv = "115"
        tnd = "N2"
        name = "NC1"
        owner = "C1"
        x = 0.001
        r = 0.0005
        mon = True
        su = RatingSet(45,35,323)
        wi = RatingSet(15,15,123)
        fa = RatingSet(25,25,223)
        sp = RatingSet(55,55,523)
        ftap = "T1"
        ttap = "T2"
        ftapn = 1
        ttapn = 2
        regnode = "N3"
        avr =2
        awr=False
        ptap = "PT1"

        nc = PhaseShifter(st, fkv, fnd, tkv,tnd,
                    name,owner, mon,
                    r,x,su,wi,sp,fa,
                    ftap, ftapn, ttap, ttapn, regnode, avr, ptap,awr)

        self.assertEqual(nc.ID, (st,name,name))
        self.assertEqual(nc.Impedance, complex(r,x))
        self.assertEqual(nc.FromNode, None)
        self.assertEqual(nc.FromNodeID, (st,fnd))
        self.assertEqual(nc.FromNodeName, fnd)
        self.assertEqual(nc.StationID, st)
        self.assertEqual(nc.FromVoltage, fkv)
        self.assertEqual(nc.Name, name)
        self.assertEqual(nc.OwnerCompanyID, owner)
        self.assertEqual(nc.ToNode, None)
        self.assertEqual(nc.ToNodeID, (st,tnd))
        self.assertEqual(nc.ToNodeName, tnd)
        self.assertEqual(nc.ToVoltage, tkv)
        self.assertEqual(nc.Monitored, mon)
        self.assertEqual(nc.SuRating.Normal, su.Normal)
        self.assertEqual(nc.WiRating.Emergency, wi.Emergency)
        self.assertEqual(nc.FaRating.Alternate, fa.Alternate)
        self.assertEqual(nc.FromTapType, ftap)
        self.assertEqual(nc.FromTapNormPosition, ftapn)
        self.assertEqual(nc.ToTapType, ttap)
        self.assertEqual(nc.ToTapNormPosition, ttapn)
        self.assertEqual(nc.RegulationNodeID, (st, regnode))
        self.assertEqual(nc.RegulationNodeName, regnode)
        self.assertEqual(nc.RegulationNode, None)
        self.assertEqual(nc.AVRStatus, avr)
        self.assertEqual(nc.PhaseTapType, ptap)
        self.assertEqual(nc.AWRStatus, awr)

if __name__ == '__main__':
    unittest.main()
