import unittest
import io
import os

from EMSCSVFormat.StationCSVStream import StationCSVStream
class TestStationCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testStationfilestream.csv"
        stationname = "s"
        divisionname = "d"
        companyname = "c"
        with open(testfilename, 'w') as file:
            file.write("CompanyName,DivisionName,StationName,Changed")

        with StationCSVStream(testfilename) as c:
            c.DivisionName = divisionname
            c.StationName = stationname
            c.CompanyName = companyname

            self.assertEqual(c.getCompanyName(), companyname)
            self.assertEqual(c.getDivisionName(), divisionname)
            self.assertEqual(c.getStationName(), stationname)

        os.remove(testfilename)
        return