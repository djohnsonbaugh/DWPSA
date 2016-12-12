import unittest
from Network.Device import Device

class TestDevice(unittest.TestCase):
    def test_Constructor(self):
        st = "S1"
        kv = "161"
        nd = "N1"
        name = "D1"
        owner = "C1"

        nc = Device(st, kv, nd, name, owner)

        self.assertEqual(nc.ID, (st,name))
        self.assertEqual(nc.Node, None)
        self.assertEqual(nc.NodeID, (st,nd))
        self.assertEqual(nc.NodeName, nd)
        self.assertEqual(nc.StationID, st)
        self.assertEqual(nc.Voltage, kv)
        self.assertEqual(nc.Name, name)
        self.assertEqual(nc.OwnerCompanyID, owner)

if __name__ == '__main__':
    unittest.main()
