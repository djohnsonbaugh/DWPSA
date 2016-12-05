import unittest
from Network.Branch import Branch
from Network.RatingSet import RatingSet

class TestBranch(unittest.TestCase):
    def test_Constructor(self):
        fst = "S1"
        fkv = "161"
        fnd = "N1"
        tst = "S2"
        tkv = "161"
        tnd = "N1"
        name = "NC1"
        owner = "C1"
        x = 0.001
        r = 0.0005
        seg = "s1"
        mon = False
        su = RatingSet(45,35,323)
        wi = RatingSet(15,15,123)
        fa = RatingSet(25,25,223)
        sp = RatingSet(55,55,523)

        nc = Branch(fst, fkv, fnd,
                    tst,tkv,tnd,
                    name,owner, mon,
                    r,x,seg,su,wi,sp,fa)

        self.assertEqual(nc.ID, (fst,name,seg))
        self.assertEqual(nc.Impedance, complex(r,x))
        self.assertEqual(nc.FromNode, None)
        self.assertEqual(nc.FromNodeID, (fst,fnd))
        self.assertEqual(nc.FromNodeName, fnd)
        self.assertEqual(nc.FromStationID, fst)
        self.assertEqual(nc.FromVoltage, fkv)
        self.assertEqual(nc.Name, name)
        self.assertEqual(nc.OwnerCompanyID, owner)
        self.assertEqual(nc.Segment, seg)
        self.assertEqual(nc.ToNode, None)
        self.assertEqual(nc.ToNodeID, (tst,tnd))
        self.assertEqual(nc.ToNodeName, tnd)
        self.assertEqual(nc.ToStationID, tst)
        self.assertEqual(nc.ToVoltage, tkv)
        self.assertEqual(nc.Monitored, mon)
        self.assertEqual(nc.SuRating.Normal, su.Normal)
        self.assertEqual(nc.WiRating.Emergency, wi.Emergency)
        self.assertEqual(nc.FaRating.Alternate, fa.Alternate)


if __name__ == '__main__':
    unittest.main()
