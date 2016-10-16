import unittest
from dwNode import Node

class TestNode(unittest.TestCase):
    """Unit Test class for Node"""

    def test_Constructor(self):
        stname = "station"
        kv = "115"
        ndid = "AB"
        company = "ABC"

        nd = Node(stname, kv, ndid, company)

        self.assertEqual(nd.ID, (stname, kv, ndid))
        self.assertEqual(nd.StationID, stname)
        self.assertEqual(nd.Voltage, kv)
        self.assertEqual(nd.Name, ndid)
        self.assertEqual(nd.Company, company)
        return


if __name__ == '__main__':
    unittest.main()