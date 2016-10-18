import unittest
from Network.Division import Division
from Network.Station import Station
from Network.Company import Company

class TestCompany(unittest.TestCase):
    def test_Constructor(self):
        companyid = "company"
        c = Company(companyid, False, False)
        c2 = Company(companyid)

        self.assertEqual(c.ID, companyid)
        self.assertEqual(c.EnforceLosses, False)
        self.assertEqual(len(c.Stations), 0)
        self.assertEqual(len(c.Divisions), 0)
        self.assertEqual(c.AWR, False)

        self.assertEqual(c2.EnforceLosses, True)
        self.assertEqual(c2.AWR, True)

        return

    def test_AddStation(self):
        divisionid = "divison"
        companyid = "company"
        stationid = "station"
        stationid2 = "station2"
        c = Company(companyid)
        s = Station(stationid, companyid, divisionid)
        s2 = Station(stationid, companyid, divisionid)
        s3 = Station(stationid2, companyid, divisionid)
        c.AddStation(s)
        with self.assertRaises(Exception):
            c.AddStation(s2)
        c.AddStation(s3)

        self.assertEqual(s.Company.ID, companyid)
        self.assertEqual(s.CompanyID, companyid)
        self.assertEqual(c.Stations[s.ID].ID, stationid)
        self.assertEqual(c.Stations[s3.ID].ID, stationid2)
        return

    def test_AddDivision(self):
        divisionid = "divison"
        divisionid2 = "divison2"
        companyid = "company"
        c = Company(companyid)
        d = Division(divisionid, companyid)
        d2 = Division(divisionid, companyid)
        d3 = Division(divisionid2, companyid)
        c.AddDivision(d)
        with self.assertRaises(Exception):
            c.AddDivision(d2)
        c.AddDivision(d3)

        self.assertEqual(d.Company.ID, companyid)
        self.assertEqual(d.CompanyID, companyid)
        self.assertEqual(c.Divisions[d.ID].ID, divisionid)
        self.assertEqual(c.Divisions[d3.ID].ID, divisionid2)
        return


if __name__ == '__main__':
    unittest.main()
