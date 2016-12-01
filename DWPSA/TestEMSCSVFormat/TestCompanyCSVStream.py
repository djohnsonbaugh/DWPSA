import unittest
import io
import os

from EMSCSVFormat.CompanyCSVStream import CompanyCSVStream
class TestCompanyCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testcompanyfilestream.csv"
        with open(testfilename, 'w') as file:
            file.write("CompanyName,Changed,PTINUM,LOSS_AREA,AWR_AREA")

        with CompanyCSVStream(testfilename) as c:
            c.AWR = "0"
            c.EnforceLosses = "0"

            self.assertEqual(c.getAWR(), False)
            self.assertEqual(c.getEnforceLosses(), False)

            c.AWR = "1"
            c.EnforceLosses = "1"

            self.assertEqual(c.getAWR(), True)
            self.assertEqual(c.getEnforceLosses(), True)

        os.remove(testfilename)
        return

