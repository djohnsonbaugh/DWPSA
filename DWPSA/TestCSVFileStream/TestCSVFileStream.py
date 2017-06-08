import unittest
import io
import os
from CSVFileStream.CSVFileStream import CSVFileStream


class TestCSVFileStream(unittest.TestCase):
    def test_Constructor(self):
        testfilename = "testcsvfilestream.csv"
        lines = [
                    "\n",
                    "\n",
                    "#GARBAGE IN THE FILE, 23233232\n" ,
                    "ColA, ColB, ColC, Col, ColE, ColD\n",
                    "2,3,,,,,,,,,,\n",
                    "\n",
                    "2\n",
                    "1,5,6,8,9,12,\n",
                    "\n"
                    ]
        propertytofilemap = {
                                "ColB" : "BCol",
                                "ColA" : "ACol",
                                "ColD" : "DCol",
                                "Col" : "loC",
                                "ColE" : "ECol",
                                "ColC" : "CCol"
                                }
        badpropertytofilemap = {
                                "ColAB" : "BCol",
                                "ColAA" : "ACol",
                                "ColAD" : "DCol",
                                "ColA" : "loC",
                                "ColAE" : "ECol",
                                "ColAC" : "CCol"
                                }      
        with open(testfilename, 'w') as file:
            file.writelines(lines)
        with self.assertRaises(Exception):
            with CSVFileStream(testfilename,badpropertytofilemap) as c:
                for line in c:
                    print(line)

        with self.assertRaises(Exception):
            with CSVFileStream("filethatdoesntexist.abc",propertytofilemap) as c:
                for line in c:
                    print(line)
                

        with CSVFileStream(testfilename,propertytofilemap) as c:
            i = 0
            for line in c:
                i += 1
                if i == 1:
                    self.assertEqual(c.ACol, "2")
                    self.assertEqual(c.BCol, "3")
                    self.assertEqual(c.ECol, "")
                if i == 2:
                    self.assertEqual(c.ACol, "2")
                    self.assertEqual(c.DCol, "")
                if i == 3:
                    self.assertEqual(c.ACol, "1")
                    self.assertEqual(c.BCol, "5")
                    self.assertEqual(c.CCol, "6")
                    self.assertEqual(c.loC, "8")
                    self.assertEqual(c.ECol, "9")
                    self.assertEqual(c.DCol, "12")

        os.remove(testfilename)
        return

