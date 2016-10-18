import unittest
from Network.Division import Division
from Network.Station import Station

class TestDivision(unittest.TestCase):
    def test_Constructor(self):
        divisionid = "divison"
        companyid = "company"
        d = Division(divisionid, companyid)

        self.assertEqual(d.ID, divisionid)
        self.assertEqual(d.CompanyID, companyid)
        self.assertEqual(len(d.Stations), 0)
        self.assertEqual(d.Company, None)
        return

    def test_AddStation(self):
        divisionid = "divison"
        companyid = "company"
        stationid = "station"
        stationid2 = "station2"
        d = Division(divisionid, companyid)
        s = Station(stationid, companyid, divisionid)
        s2 = Station(stationid, companyid, divisionid)
        s3 = Station(stationid2, companyid, divisionid)
        d.AddStation(s)
        with self.assertRaises(Exception):
            d.AddStation(s2)
        d.AddStation(s3)

        self.assertEqual(s.Division.ID, divisionid)
        self.assertEqual(s.DivisionID, divisionid)
        self.assertEqual(d.Stations[s.ID].ID, stationid)
        self.assertEqual(d.Stations[s3.ID].ID, stationid2)

if __name__ == '__main__':
    unittest.main()
