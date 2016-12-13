import unittest
from Network.Load import Load

class TestLoad(unittest.TestCase):
    def test_Constructor(self):
        st = "S1"
        kv = "161"
        nd = "N1"
        name = "D1"
        owner = "C1"
        mwcon = 100.1
        mvcon = 51.3
        pf = .75
        mwncon = 1.1
        mvncon = .5


        nc = Load(st, kv, nd, name, owner, mwcon, mvcon, pf, mwncon, mvncon)

        self.assertEqual(nc.ID, (st,name, "LD"))
        self.assertEqual(nc.Node, None)
        self.assertEqual(nc.NodeID, (st,nd))
        self.assertEqual(nc.NodeName, nd)
        self.assertEqual(nc.StationID, st)
        self.assertEqual(nc.Voltage, kv)
        self.assertEqual(nc.Name, name)
        self.assertEqual(nc.OwnerCompanyID, owner)

        self.assertEqual(nc.Conforming.real, mwcon)
        self.assertEqual(nc.Conforming.imag, mvcon)
        self.assertEqual(nc.NonConforming.real, mwncon)
        self.assertEqual(nc.NonConforming.imag, mvncon)
        self.assertEqual(nc.PowerFactor, pf)


if __name__ == '__main__':
    unittest.main()
