from TestNetwork import *
import unittest
from Network.EMSCSVFormat.CSVFileStream import CSVFileStream

testclasses = [
               TestCompany.TestCompany, 
               TestDivision.TestDivision, 
               TestStation.TestStation, 
               TestNode.TestNode, 
               TestNetwork.TestNetwork
               ]



suitel = unittest.TestLoader()


suites_list = []
for test_class in testclasses:
    suite = suitel.loadTestsFromTestCase(test_class)
    suites_list.append(suite)

big_suite = unittest.TestSuite(suites_list)

runner = unittest.TextTestRunner(verbosity=2)
results = runner.run(big_suite)

p2c = {}
p2c["ColA"] = "P2"
p2c["ColB"] = "P1"
p2c["ColC"] = "P3"
p2c["ColE"] = "P4"
p2c["ColD"] = "P5"

csv = CSVFileStream(".\TestNetwork\TestEMSCSVFormat\Test.csv", p2c) 
for line in csv:
    print(csv.P1)


