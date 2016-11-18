from TestNetwork import *
import unittest
from Network.EMSCSVFormat.CompanyCSVStream import CompanyCSVStream

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
#results = runner.run(big_suite)

with CompanyCSVStream(".\TestNetwork\TestEMSCSVFormat\Company.csv")  as csv:
    for line in csv:
        print(line)


