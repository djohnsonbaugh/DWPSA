import unittest
from dwNetwork import *


class TestNetwork(unittest.TestCase):
    """Test class for the Network Class"""

    def test_NodeAfterStation(self):
        """Node added after Stations - Station is found and node is stored"""

        stname = "station"
        kv = "115"
        ndid = "AB"
        company = "ABC"

        n = Network()
        s = Station(stname)
        n.AddStation(s)
        
        #checks if Station loaded properly
        self.assertEqual(n.Stations[stname].ID, stname)

        nd = Node(stname, kv, ndid, company)
        n.AddNode(nd)

        #checks if Network contains node
        self.assertEqual(n.Nodes[(stname, kv, ndid)].Company,  company)

        #checks if Station contains node
        self.assertEqual(s.Nodes[(stname, kv, ndid)].Company, company)

        return

    def test_NodeWithoutStation(self):
        """Node added without Station - Station created"""

        stname = "station"
        kv = "115"
        ndid1 = "AB"
        ndid2 = "AC"
        company = "ABC"

        n = Network()
        nd1 = Node(stname, kv, ndid1, company)
        nd2 = Node(stname, kv, ndid2, company)
        n.AddNode(nd1, False)
       
        #checks if Station was created
        self.assertTrue(len(n.Stations) == 0)

        n.AddNode(nd2)

        #checks if Station loaded properly
        self.assertEqual(n.Stations[stname].ID, stname)

        s = n.Stations[stname]

        #checks if Network contains nodes
        self.assertEqual(n.Nodes[(stname, kv, ndid1)].Name,  ndid1)
        self.assertEqual(n.Nodes[(stname, kv, ndid2)].Name,  ndid2)

        #checks if Station contains nodes
        self.assertEqual(s.Nodes[(stname, kv, ndid1)].Name, ndid1)
        self.assertEqual(s.Nodes[(stname, kv, ndid2)].Name, ndid2)


        return

    def test_DuplicateNode(self):
        """Duplicate Node added"""

        stname = "station"
        kv = "115"
        ndid = "AB"
        company = "ABC"

        n = Network()
        nd1 = Node(stname, kv, ndid, company)
        nd2 = Node(stname, kv, ndid, company)
        n.AddNode(nd1, False)

        with self.assertRaises(Exception):
            n.AddNode(nd2, False)
        

        return

    def test_DuplicateStation(self):
        """Duplicate Station added"""

        stname = "station"
        n = Network()
        st1 = Station(stname)
        st2 = Station(stname)
        n.AddStation(st1)

        with self.assertRaises(Exception):
            n.AddStation(st2)
        

        return
if __name__ == '__main__':
    unittest.main()