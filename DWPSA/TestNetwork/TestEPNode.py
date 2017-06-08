import unittest
from Network.EPNode import EPNode

class TestEPNode(unittest.TestCase):
    """Unit Test class for EPNode"""

    def test_Constructor(self):
        id =    122060565
        epid = 122033205
        name = "nodename"
        ndid = ("station","abc123")
        

        nd = EPNode(id, name, epid, ndid)

        self.assertEqual(nd.ID, id)
        self.assertEqual(nd.EPNodeID , epid)
        self.assertEqual(nd.NodeID, ndid)
        self.assertEqual(nd.Name, name)
        self.assertEqual(nd.Node, None)