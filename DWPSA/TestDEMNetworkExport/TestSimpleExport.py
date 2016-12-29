import unittest
from Network.Network import Network
from Network.Load import Load
from Network.Unit import Unit
from Network.Branch import Branch
from Network.RatingSet import RatingSet
import dem
from DEMNetworkExport.SimpleExport import NetworkToDEMSimple

class TestSimpleExport(unittest.TestCase):
    def testNetworkToDEMSimple(self):

        st1 = "Home"
        st2 = "Grid"
        kv = "115"
        nd1 = "HomeNode"
        nd2 = "GridNode"
        sgen = "SolarGen"
        ggen = "GridGen"
        ld1 = "HomeLoad"

        n = Network()

        #HOME        
        n.AddStationByDef(st1)
        n.AddNodeByDef(st1, kv, nd1)
        sg = Unit(st1, kv, nd1, sgen,"",10, 0, 0, 0, 1, False, 0)
        ld = Load(st1, kv, nd1, ld1, "", 13, 0 , 1)
        n.AddDevice(sg)
        n.AddDevice(ld)
         
        #GRID
        n.AddStationByDef(st2)
        n.AddNodeByDef(st2, kv, nd2)
        gg = Unit(st2, kv, nd2, ggen, "", 1e6, 0 ,0 ,0 , 1, False, 0)
        n.AddDevice(gg)

        #LINE
        br = Branch(st1, kv, nd1, st2, kv, nd2, "Line", "", True, 0,0,"1", RatingSet(25, 25, 25), RatingSet(25, 25, 25))        
        n.AddNodeConnector(br)
        
        gp = NetworkToDEMSimple(n)
        gp.init_problem()
        gp.problem.solve()
        print(gp.results.summary())
        #with open("testdemresult.txt", 'w') as file:
        #    file.write(gp.results.summary())
if __name__ == '__main__':
    unittest.main()
