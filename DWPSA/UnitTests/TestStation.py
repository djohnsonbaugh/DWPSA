import unittest
from dwStation import *
from dwNode import *

class TestStation(unittest.TestCase):
    def test_ConstructorA(self):
        stname = "station"

        s = Station(stname)

        self.assertEqual(s.ID, stname)
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
        self.assertEqual(s.Nodes[(stname, kv, ndid)].Name, ndid)
        
        #checks if Node knows what Station it is at.
        self.assertEqual(nd.Station.ID, stname)
        return


if __name__ == '__main__':
    unittest.main()
