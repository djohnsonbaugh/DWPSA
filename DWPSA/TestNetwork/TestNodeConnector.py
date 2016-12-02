import unittest
from Network.NodeConnector import NodeConnector

class TestNodeConnector(unittest.TestCase):
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

        nc = NodeConnector(fst, fkv, fnd,tst,tkv,tnd,name,owner,r,x,seg)

        self.assertEqual(nc.ID, (fst,name,seg))
        self.assertEqual(nc.Impedance, complex(r,x))
        self.assertEqual(nc.FromNode, None)
        self.assertEqual(nc.FromNodeID, (fst,fkv,fnd))
        self.assertEqual(nc.FromNodeName, fnd)
        self.assertEqual(nc.FromStationID, fst)
        self.assertEqual(nc.FromVoltage, fkv)
        self.assertEqual(nc.Name, name)
        self.assertEqual(nc.OwnerCompanyID, owner)
        self.assertEqual(nc.Segment, seg)
        self.assertEqual(nc.ToNode, None)
        self.assertEqual(nc.ToNodeID, (tst,tkv,tnd))
        self.assertEqual(nc.ToNodeName, tnd)
        self.assertEqual(nc.ToStationID, tst)
        self.assertEqual(nc.ToVoltage, tkv)

if __name__ == '__main__':
    unittest.main()
