import unittest
import io
import os

from EMSCSVFormat.NodeCSVStream import NodeCSVStream
class TestNodeCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testNodefilestream.csv"
        stationname = "s"
        nodename = "n"
        companyname = "c"
        voltage = "121"

        with open(testfilename, 'w') as file:
            file.write("NodeName,CompanyName,StationName,Voltage,changed")

        with NodeCSVStream(testfilename) as c:
            c.NodeName = nodename
            c.StationName = stationname
            c.CompanyName = companyname
            c.Voltage = voltage

            self.assertEqual(c.getCompanyName(), companyname)
            self.assertEqual(c.getStationName(), stationname)
            self.assertEqual(c.getNodeName(), nodename)
            self.assertEqual(c.getVoltage(), voltage)

        os.remove(testfilename)
        return