import unittest
from TestNetwork import *
from TestEMSCSVFormat import *
from TestCSVFileStream import TestCSVFileStream
#from Network.Network import Network
#from Network.EMSCSVImporter import EMSCSVImporter

#n = Network()
#imp = EMSCSVImporter("C:\EMS2015Dec")
#imp.Import(n)

testclasses = [
               TestCompany.TestCompany, 
               TestDivision.TestDivision, 
               TestStation.TestStation, 
               TestNode.TestNode, 
               TestNetwork.TestNetwork,
               TestCSVFileStream,
               TestCompanyCSVStream.TestCompanyCSVStream,
               TestDivisionCSVStream.TestDivisionCSVStream,
               TestStationCSVStream.TestStationCSVStream,
               TestEMSCSVImporter.TestEMSCSVImporter
               ]



suitel = unittest.TestLoader()


suites_list = []
for test_class in testclasses:
    suite = suitel.loadTestsFromTestCase(test_class)
    suites_list.append(suite)

big_suite = unittest.TestSuite(suites_list)

runner = unittest.TextTestRunner(verbosity=2)
results = runner.run(big_suite)




