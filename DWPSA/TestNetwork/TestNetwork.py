import unittest
from Network.Network import Network
from Network.Station import Station
from Network.Node import Node
from Network.Company import Company
from Network.Division import Division
from Network.NodeConnector import NodeConnector
from Network.CircuitBreaker import CircuitBreaker
from Network.Branch import Branch
from Network.Transformer import Transformer
from Network.PhaseShifter import PhaseShifter
from Network.CircuitBreaker import CBState
from Network.Load import Load
from Network.Unit import Unit
from Network.Shunt import Shunt
from Network.PNode import PNode
from Network.EPNode import EPNode
from Network.CPNode import CPNode

class TestNetwork(unittest.TestCase):
    """Test class for the Network Class"""

    def test_Constructor(self):
        n = Network()

        self.assertEqual(len(n.Nodes),0)
        self.assertEqual(len(n.Stations), 0)
        self.assertEqual(len(n.Companies), 0)
        return

    def test_AddCompany(self):
        n = Network()
        companyid = "company"
        companyid2 = "company"
        companyid3 = "company3"
        c = Company(companyid)
        c2 = Company(companyid2)

        n.AddCompany(c)

        with self.assertRaises(Exception):
            n.AddCompany(c2)

        n.AddCompanyByDef(companyid3, False, False)

        self.assertEqual(n.Companies[companyid].ID, companyid)
        self.assertEqual(n.Companies[companyid3].ID,  companyid3)
        return

    def test_FindorAddCompany(self):
        n = Network()
        companyid = "company"
        companyid3 = "company3"
        c = Company(companyid)
        n.AddCompany(c)

        self.assertTrue(n.FindOrAddCompany(companyid).ID, companyid)
        self.assertTrue(n.FindOrAddCompany(companyid3).ID, companyid3)
        self.assertTrue(n.Companies[companyid3].ID, companyid3)
        return

    def test_AddDivision(self):
        n = Network()
        companyid = "company"
        companyid2 = "company2"
        companyid3 = "company3"
        divisionid = "division"
        divisionid2 = "division2"
        divisionid3 = "division3"

        c = Company(companyid)
        c3 = Company(companyid3)
        d = Division(divisionid, companyid)
        d2 = Division(divisionid2, companyid2)
        n.AddCompany(c)
        n.AddCompany(c3)
        n.AddDivision(d)
        n.AddDivision(d2)
        n.AddDivisionByDef(divisionid3, companyid3)
        n.AddDivisionByDef(divisionid, companyid2)

        with self.assertRaises(Exception):
            n.AddDivisionByDef(divisionid, companyid)

        self.assertEqual(n.Companies[companyid].Divisions[divisionid].ID, divisionid)
        self.assertEqual(n.Companies[companyid2].Divisions[divisionid2].ID, divisionid2)
        self.assertEqual(n.Companies[companyid3].Divisions[divisionid3].ID, divisionid3)
        self.assertEqual(len(n.Companies[companyid2].Divisions), 2)
        self.assertEqual(n.Companies[companyid2].Divisions[divisionid].ID, divisionid)
        return

    def test_FindorAddDivision(self):
        n = Network()
        companyid = "company"
        companyid3 = "company3"
        divisionid = "division"
        divisionid3 = "division3"
        c = Company(companyid)
        d = Division(divisionid, companyid)
        n.AddCompany(c)
        n.AddDivision(d)

        self.assertTrue(n.FindOrAddDivision(divisionid, companyid).ID, divisionid)
        self.assertTrue(n.FindOrAddDivision(divisionid3, companyid3).ID, divisionid3)
        self.assertTrue(n.Companies[companyid3].Divisions[divisionid3].ID, divisionid3)
        return

    def test_AddStation(self):
        n = Network()
        stationid = "station"
        stationid3 = "station3"
        companyid = "company"
        divisionid = "division"

        s = Station(stationid)
        s2 = Station(stationid)

        n.AddStation(s)
        with self.assertRaises(Exception):
            n.AddStation(s2)

        n.AddStationByDef(stationid3, companyid, divisionid)

        self.assertEqual(n.Stations[stationid].ID, stationid)
        self.assertEqual(n.Companies[""].Stations[stationid].ID, stationid)
        self.assertEqual(n.Companies[""].Divisions[""].Stations[stationid].ID, stationid)
        self.assertEqual(s.Company.ID, "")
        self.assertEqual(s.Division.ID, "")
        self.assertEqual(n.Stations[stationid3].ID, stationid3)
        self.assertEqual(n.Companies[companyid].Stations[stationid3].ID, stationid3)
        self.assertEqual(n.Companies[companyid].Divisions[divisionid].Stations[stationid3].ID, stationid3)
        self.assertEqual(n.Stations[stationid3].Company.ID, companyid)
        self.assertEqual(n.Stations[stationid3].Division.ID, divisionid)

        return

    def test_FindOrAddStation(self):
        n = Network()
        stationid = "station"
        stationid3 = "station3"
        companyid = "company"
        divisionid = "division"

        s = Station(stationid)
        s2 = Station(stationid)

        n.AddStation(s)

        self.assertEqual(n.FindOrAddStation(stationid).ID, stationid)
        self.assertEqual(n.FindOrAddStation(stationid3,companyid, divisionid).ID, stationid3)
        self.assertEqual(n.Stations[stationid3].ID, stationid3)
        self.assertEqual(n.Companies[companyid].Stations[stationid3].ID, stationid3)
        self.assertEqual(n.Companies[companyid].Divisions[divisionid].Stations[stationid3].ID, stationid3)
        self.assertEqual(n.Stations[stationid3].Company.ID, companyid)
        self.assertEqual(n.Stations[stationid3].Division.ID, divisionid)

        return

    def test_AddNode(self):

        stname = "station"
        kv = "115"
        ndid = "AB"
        ndid2 = "AB2"
        company = "ABC"

        n = Network()
        s = Station(stname)
        n.AddStation(s)     
        nd = Node(stname, kv, ndid, company)
        n.AddNode(nd)
        n.AddNodeByDef(stname, kv, ndid2, company, "div")

        with self.assertRaises(Exception):
            n.AddNodeByDef(stname,kv, ndid, company)

        self.assertEqual(n.Nodes[nd.ID].ID, (stname, ndid))
        self.assertEqual(n.Stations[stname].Nodes[nd.ID].ID, (stname, ndid))

        self.assertEqual(n.Nodes[(stname, ndid2)].ID, (stname, ndid2))
        self.assertEqual(n.Stations[stname].Nodes[(stname, ndid2)].ID, (stname, ndid2))

        return

    def test_AddNodeConnector(self):
        st1 = "ST1"
        st2 = "ST2"
        kv115 = "115"
        kv365 = "365"
        ndid1 = "N1"
        ndid2 = "N2"
        ndid3 = "N3"
        ndid4 = "N4"
        cbid1 = "12"
        trname = "23"
        psname = "ps12"
        lnname = "lnname"
        cbid2 = "34"        
        company = "ABC"

        n = Network()
        #Station #1
        s1 = Station(st1)
        nd11 = Node(st1, kv115, ndid1, company)
        nd12 = Node(st1, kv115, ndid2, company)
        nd13 = Node(st1, kv365, ndid3, company)
        nd14 = Node(st1, kv365, ndid4, company)
        cb11 = CircuitBreaker(st1, kv115, ndid1, ndid2, cbid1, company, CBState.Closed, "CB")
        tr11 = Transformer(st1, kv115, ndid2, kv365, ndid3, trname, company, True)
        cb12 = CircuitBreaker(st1, kv365, ndid3, ndid4, cbid2, company, CBState.Closed, "CB")

        n.AddStation(s1)
        #both nodes mising     
        with self.assertRaises(Exception):
            n.AddNodeConnector(cb11)

        n.AddNode(nd12)
        #from node missing
        with self.assertRaises(Exception):
            n.AddNodeConnector(cb11)

        n.AddNode(nd11)
        n.AddNodeConnector(cb11)
        #to node missing
        with self.assertRaises(Exception):
            n.AddNodeConnector(tr11)
        #duplicate connector
        with self.assertRaises(Exception):
            n.AddNodeConnector(cb11)


        n.AddNode(nd13)
        n.AddNode(nd14)
        n.AddNodeConnector(tr11)
        n.AddNodeConnector(cb12)
        
        #Station #2
        s2 = Station(st2)
        n.AddStation(s2) 
        nd21 = Node(st2, kv115, ndid1, company)
        n.AddNode(nd21)
        nd22 = Node(st2, kv115, ndid2, company)
        n.AddNode(nd22)
        ps = PhaseShifter(st2, kv115,  ndid1, kv115, ndid2, psname, company, False)
        n.AddNodeConnector(ps)

        ln = Branch(st1, kv115, ndid1, st2, kv115, ndid1, lnname, company, True)
        n.AddNodeConnector(ln)

        self.assertEqual(len(n.NodeConnectors), 5)
        self.assertEqual(len(n.CircuitBreakers), 2)
        self.assertEqual(len(n.Transformers), 1)
        self.assertEqual(len(n.PhaseShifters), 1)
        self.assertEqual(len(n.Lines), 1)
        self.assertEqual(len(nd11.NodeConnectors), 2)
        self.assertEqual(len(nd12.NodeConnectors), 2)
        self.assertEqual(len(nd13.NodeConnectors), 2)
        self.assertEqual(len(nd14.NodeConnectors), 1)
        self.assertEqual(len(nd21.NodeConnectors), 2)
        self.assertEqual(len(nd22.NodeConnectors), 1)
        
    def test_AddDevice(self):
        st1 = "ST1"
        st2 = "ST2"
        kv115 = "115"
        kv365 = "365"
        ndid1 = "N1"
        ndid2 = "N2"
        ndid3 = "N3"
        ndid4 = "N4"
        company = "ABC"
        ldid = "LD1"
        shid = "SH1"
        uid = "U1"
        n = Network()
        #Station #1
        s1 = Station(st1)
        nd11 = Node(st1, kv115, ndid1, company)
        nd12 = Node(st1, kv115, ndid2, company)
        nd13 = Node(st1, kv365, ndid3, company)
        nd14 = Node(st1, kv365, ndid4, company)
        l1 = Load(st1, kv115, ndid1, ldid, company, 1,1,.97)
        sh1 = Shunt(st1, kv115, ndid2, shid, company, 1)
        u1 = Unit(st1, kv365, ndid3, uid, company, 10, 10,5,5,.8, False, 7)

        with self.assertRaises(Exception):
            n.AddDevice(l1)

        n.AddStation(s1)

        with self.assertRaises(Exception):
            n.AddDevice(l1)

        n.AddNode(nd12)
        n.AddNode(nd11)
        n.AddNode(nd13)
        n.AddNode(nd14)
        n.AddDevice(l1)
        n.AddDevice(sh1)
        n.AddDevice(u1)
        #duplicate device
        with self.assertRaises(Exception):
            n.AddDevice(l1)



        self.assertEqual(len(n.Devices), 3)
        self.assertEqual(len(n.Loads), 1)
        self.assertEqual(len(n.Units), 1)
        self.assertEqual(len(n.Shunts), 1)
        self.assertEqual(len(nd11.Devices), 1)
        self.assertEqual(len(nd12.Devices), 1)
        self.assertEqual(len(nd13.Devices), 1)
        return

    def test_AddPNode(self):
        stname = "station"
        kv = "115"
        ndid = "AB"
        ndid2 = "AB2"
        company = "ABC"

        n = Network()
        s = Station(stname)
        n.AddStation(s)     
        nd = Node(stname, kv, ndid, company)
        n.AddNode(nd)
        n.AddNodeByDef(stname, kv, ndid2, company, "div")

        id =  122060565
        id2 = 122060564
        id3 = 122060562
        id4 = 122060563
        id5 = 34234234
        name = "nodename"
        name2 = "nodename2"
        name3 = "nodename3"
        name4 = "nodename4"
        name5 = "nodename5"
        ldun = "load1"
        sett = True
        sett2 = False
        rzid = 3

        cnd = CPNode(id, name, sett)
        cnd2=CPNode(id2,name2,sett2)
        pnd3 = PNode(id3, name3)
        end4=EPNode(id4, name4,234234,(stname,ndid), ldun, rzid)
        end5=EPNode(id5, name5,2634234,("",""), ldun, rzid)
    

        n.AddPNode(cnd)
        n.AddPNode(cnd2)
        n.AddPNode(pnd3)
        n.AddPNode(end4)
      
        with self.assertRaises(Exception):
            n.AddPNode(cnd)
        with self.assertRaises(Exception):
            n.AddPNode(end5)       

        self.assertEqual(n.PNodes[id].Name, name)
        self.assertEqual(n.CPNodes[id].Name, name)
        self.assertEqual(n.PNodes[id2].Name, name2)
        self.assertEqual(n.CPNodes[id2].Name, name2)
        self.assertEqual(n.PNodes[id3].Name, name3)
        self.assertEqual(n.PNodes[id4].Name, name4)
        self.assertEqual(n.EPNodes[id4].Name, name4)
        self.assertEqual(n.EPNodes[id4].Node.ID, nd.ID)

        self.assertEqual(n.CPNodes[id].FactorSum, 0)
        n.AddPNodeFactor(id, id4, .4)
        n.AddPNodeFactor(id, id3, .6)
        self.assertEqual(n.CPNodes[id].FactorSum, 1)
        self.assertEqual(n.CPNodes[id].PNodes[id4].Name, name4)
        self.assertEqual(n.CPNodes[id].PNodeFactors[id3], .6)

        with self.assertRaises(Exception):
            n.AddPNodeFactor(id, id4, .4)
        with self.assertRaises(Exception):
            n.AddPNodeFactor(34, id4, .4)
        with self.assertRaises(Exception):
            n.AddPNodeFactor(id, 45, .4)
        return
if __name__ == '__main__':
    unittest.main()