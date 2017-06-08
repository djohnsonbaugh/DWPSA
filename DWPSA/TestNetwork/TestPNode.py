import unittest
from Network.PNode import PNode

class TestPNode(unittest.TestCase):
    """Unit Test class for PNode"""

    def test_Constructor(self):
        id =    122060565
        name = "nodename"

        nd = PNode(id, name)

        self.assertEqual(nd.ID, id)
        self.assertEqual(nd.Name, name)