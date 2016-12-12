import unittest
from Network.Shunt import Shunt

class TestShunt(unittest.TestCase):
    def test_Constructor(self):
        st = "S1"
        kv = "161"
        nd = "N1"
        name = "D1"
        owner = "C1"
        mv = 100.1
        regnodename = "R1"
        pu = 1.1
        dev = .0005

        nc = Shunt(st, kv, nd, name, owner, mv, regnodename, pu , dev)

        self.assertEqual(nc.ID, (st,name))
        self.assertEqual(nc.Node, None)
        self.assertEqual(nc.NodeID, (st,nd))
        self.assertEqual(nc.NodeName, nd)
        self.assertEqual(nc.StationID, st)
        self.assertEqual(nc.Voltage, kv)
        self.assertEqual(nc.Name, name)
        self.assertEqual(nc.OwnerCompanyID, owner)

        self.assertEqual(nc.RegulationNode, None)
        self.assertEqual(nc.RegulationNodeName, regnodename)
        self.assertEqual(nc.RegulationNodeID, (st,regnodename))
        self.assertEqual(nc.MVar, mv)
        self.assertEqual(nc.VoltagePUTarget, pu)
        self.assertEqual(nc.VoltageTargetDeviation, dev)


if __name__ == '__main__':
    unittest.main()
