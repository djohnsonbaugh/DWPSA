import unittest
import io
import os

from EMSCSVFormat.DivisionCSVStream import DivisionCSVStream
class TestDivisionCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testDivisionfilestream.csv"
        divisionname = "d"
        companyname = "c"
        with open(testfilename, 'w') as file:
            file.write("DivisionName,CompanyName,Changed")

        with DivisionCSVStream(testfilename) as c:
            c.DivisionName = divisionname
            c.CompanyName = companyname

            self.assertEqual(c.getCompanyName(), companyname)
            self.assertEqual(c.getDivisionName(), divisionname)

        os.remove(testfilename)
        return