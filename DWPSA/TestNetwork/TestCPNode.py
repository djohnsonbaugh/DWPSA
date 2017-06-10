import unittest
from Network.CPNode import CPNode
from Network.EPNode import EPNode
from Network.PNode import PNode

class TestCPNode(unittest.TestCase):
    """Unit Test class for PNode"""

    def test_Constructor(self):
        id =    122060565
        name = "nodename"
        sett = True


        nd = CPNode(id, name, sett)

        self.assertEqual(nd.ID, id)
        self.assertEqual(nd.Name, name)
        self.assertEqual(nd.Settled, sett)

    def test_AddPNodeFactor(self):
        id =  122060565
        id2 = 122060564
        id3 = 122060562
        id4 = 122060563
        name = "nodename"
        name2 = "nodename2"
        name3 = "nodename3"
        name4 = "nodename4"
        ldun = "load1"
        sett = True
        sett2 = False
        rzid = 3
        pf2 = .3
        pf3 = .2
        pf4 = .2

        nd = CPNode(id, name, sett)
        nd2=CPNode(id2,name2,sett2)
        nd3 = PNode(id3, name3)
        nd4=EPNode(id4, name4,234234,("ST","1"), ldun, rzid)


        with self.assertRaises(Exception):
            nd.AddPnodeFactor(nd,.45)
        with self.assertRaises(Exception):
            NormFacts = nd.GetNormalizedPNodeFactors()
        
        nd.AddPnodeFactor(nd2, pf2)
        nd.AddPnodeFactor(nd3,pf3)
        nd.AddPnodeFactor(nd4, pf4)

        with self.assertRaises(Exception):
            nd.AddPnodeFactor(nd2,.45)

        self.assertEqual(nd.FactorSum, pf2 + pf3 + pf4)
        self.assertEqual(nd.PNodeFactors[id2],pf2)
        self.assertEqual(nd.PNodeFactors[id3],pf3)
        self.assertEqual(nd.PNodeFactors[id4],pf4)
       
        NormFacts = nd.GetNormalizedPNodeFactors()

        self.assertAlmostEqual(NormFacts[id2] + NormFacts[id3] + NormFacts[id4], 1)
        return     