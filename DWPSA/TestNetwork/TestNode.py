import unittest
from Network.Node import Node

class TestNode(unittest.TestCase):
    """Unit Test class for Node"""

    def test_Constructor(self):
        stname = "station"
        kv = "115"
        ndid = "AB"
        companyid = "ABC"
        divisionid = "division"

        nd = Node(stname, kv, ndid, companyid, divisionid)

        self.assertEqual(nd.ID, (stname, kv, ndid))
        self.assertEqual(nd.StationID, stname)
        self.assertEqual(nd.Voltage, kv)
        self.assertEqual(nd.Name, ndid)
        self.assertEqual(nd.CompanyID, companyid)
        self.assertEqual(nd.DivisionID, divisionid)
        self.assertEqual(nd.Station, None)

        return


if __name__ == '__main__':
    unittest.main()