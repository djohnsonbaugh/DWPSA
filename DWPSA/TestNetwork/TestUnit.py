import unittest
from Network.Unit import Unit

class TestUnit(unittest.TestCase):
    def test_Constructor(self):
        st = "S1"
        kv = "161"
        nd = "N1"
        name = "D1"
        owner = "C1"
        mw = 100
        mwmax = 150
        mwmin = 50
        mvmax = 30.3
        mvmin = -40
        partf = .5
        agc = True

        regnodename = "R1"
        pu = 1.1
        dev = .0005

        nc = Unit(st, kv, nd, name, owner, mwmax, mvmax, mwmin, mvmin, partf, agc, mw, regnodename, pu , dev)

        self.assertEqual(nc.ID, (st,name, "UN"))
        self.assertEqual(nc.Node, None)
        self.assertEqual(nc.NodeID, (st,nd))
        self.assertEqual(nc.NodeName, nd)
        self.assertEqual(nc.StationID, st)
        self.assertEqual(nc.Voltage, kv)
        self.assertEqual(nc.Name, name)
        self.assertEqual(nc.OwnerCompanyID, owner)

        self.assertEqual(nc.AGC, agc)
        self.assertEqual(nc.InitialMW, mw)
        self.assertEqual(nc.MVAMax.real, mwmax)
        self.assertEqual(nc.MVAMax.imag, mvmax)
        self.assertEqual(nc.MVAMin.real, mwmin)
        self.assertEqual(nc.MVAMin.imag, mvmin)
        self.assertEqual(nc.ParticipationFactor, partf)

        self.assertEqual(nc.RegulationNode, None)
        self.assertEqual(nc.RegulationNodeName, regnodename)
        self.assertEqual(nc.RegulationNodeID, (st,regnodename))
        self.assertEqual(nc.VoltagePUTarget, pu)
        self.assertEqual(nc.VoltageTargetDeviation, dev)


if __name__ == '__main__':
    unittest.main()
