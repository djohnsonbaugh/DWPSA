import unittest
from Network.Station import Station
from Network.Node import Node

class TestStation(unittest.TestCase):
    def test_Constructor(self):
        stname = "station"
        companyid = "companyid"
        divisionid = "divisionid"

        s = Station(stname, companyid, divisionid)

        self.assertEqual(s.ID, stname)
        self.assertEqual(s.CompanyID, companyid)
        self.assertEqual(s.DivisionID, divisionid)
        self.assertEqual(s.Company, None)
        self.assertEqual(s.Division, None)
        self.assertEqual(len(s.Nodes), 0)
        return


    def test_AddNode(self):
        stname = "station"
        kv = "115"
        ndid = "AB"
        company = "ABC"

        nd = Node(stname, kv, ndid, company)
        s = Station(stname)

        s.AddNode(nd)
        #checks if Station contains nodes
        self.assertEqual(s.Nodes[(stname, ndid)].Name, ndid)
        
        #checks if Node knows what Station it is at.
        self.assertEqual(nd.Station.ID, stname)
        return


if __name__ == '__main__':
    unittest.main()
