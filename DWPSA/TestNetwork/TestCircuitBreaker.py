import unittest
from Network.CircuitBreaker import CircuitBreaker
from Network.CircuitBreaker import CBState

class TestCircuitBreaker(unittest.TestCase):
    def test_Constructor(self):
        st = "S1"
        kv = "161"
        fnd = "N1"
        tnd = "N1"
        name = "NC1"
        owner = "C1"
        ns = CBState.Closed
        type = "CB"

        nc = CircuitBreaker(st, kv, fnd, tnd, name, owner, ns, type)

        self.assertEqual(nc.CBType, type)
        self.assertEqual(nc.ID, (st, name, type))
        self.assertEqual(nc.FromNode, None)
        self.assertEqual(nc.FromNodeID, (st,fnd))
        self.assertEqual(nc.FromNodeName, fnd)
        self.assertEqual(nc.Name, name)
        self.assertEqual(nc.NormalState, ns)
        self.assertEqual(nc.OwnerCompanyID, owner)
        self.assertEqual(nc.StationID, st)
        self.assertEqual(nc.ToNode, None)
        self.assertEqual(nc.ToNodeID, (st,tnd))
        self.assertEqual(nc.ToNodeName, tnd)
        self.assertEqual(nc.Voltage, kv)

if __name__ == '__main__':
    unittest.main()
