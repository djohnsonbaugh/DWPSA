import unittest
from Network.Network import Network
from Network.Station import Station
from Network.Node import Node
from Network.Company import Company
from Network.Division import Division

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



if __name__ == '__main__':
    unittest.main()