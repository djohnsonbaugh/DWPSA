import unittest
from Network.Node import Node
from Network.NodeConnector import NodeConnector
from Network.PhaseShifter import PhaseShifter

class TestNode(unittest.TestCase):
    """Unit Test class for Node"""

    def test_Constructor(self):
        stname = "station"
        kv = "115"
        ndid = "AB"
        companyid = "ABC"
        divisionid = "division"

        nd = Node(stname, kv, ndid, companyid, divisionid)

        self.assertEqual(nd.ID, (stname, ndid))
        self.assertEqual(nd.StationID, stname)
        self.assertEqual(nd.Voltage, kv)
        self.assertEqual(nd.Name, ndid)
        self.assertEqual(nd.CompanyID, companyid)
        self.assertEqual(nd.DivisionID, divisionid)
        self.assertEqual(nd.Station, None)

        return

    def test_AddNodeConnector(self):
        st1 = "station1"
        st2 = "station2"
        kv = "115"
        kv2 = "365"
        ndid1 = "N1"
        ndid2 = "N2"
        ndid3 = "N3"
        companyid = "ABC"
        divisionid = "division"
        ncname = "NC1"
        psname = "PS1"
        seg = "1"
        nd1 = Node(st1, kv, ndid1, companyid, divisionid)
        nd2 = Node(st2, kv, ndid2, companyid, divisionid)
        nd3 = Node(st1, kv2, ndid3, companyid, divisionid)
        nc = NodeConnector(st1, kv, ndid1, st2, kv, ndid2, ncname, companyid,0,0,seg)
        ps = PhaseShifter(st1, kv, ndid1, kv2, ndid3, psname, companyid, True)

        nd1.AddNodeConnector(nc)
        nd2.AddNodeConnector(nc)
        nd1.AddNodeConnector(ps)
        nd3.AddNodeConnector(ps)

        #checks if Station contains nodes
        self.assertEqual(nd1.NodeConnectors[(st1, ncname, seg)].Name, ncname)
        self.assertEqual(nd2.NodeConnectors[(st1, ncname, seg)].Name, ncname)
        self.assertEqual(nd1.NodeConnectors[(st1, psname, psname)].Name, psname)
        self.assertEqual(nd3.NodeConnectors[(st1, psname, psname)].Name, psname)
        
        #checks if Node knows what Station it is at.
        self.assertEqual(nc.FromNode, nd1)
        self.assertEqual(nc.ToNode, nd2)
        self.assertEqual(ps.FromNode, nd1)
        self.assertEqual(ps.ToNode, nd3)
        
        return

if __name__ == '__main__':
    unittest.main()