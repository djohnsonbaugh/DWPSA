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
               TestBranch.TestBranch,
               TestCircuitBreaker.TestCircuitBreaker,
               TestCompany.TestCompany, 
               TestCompanyCSVStream.TestCompanyCSVStream,
               TestCSVFileStream,
               TestDivision.TestDivision, 
               TestDivisionCSVStream.TestDivisionCSVStream,
               TestEMSCSVImporter.TestEMSCSVImporter,
               TestNetwork.TestNetwork,
               TestNode.TestNode,
               TestNodeConnector.TestNodeConnector,
               TestNodeCSVStream.TestNodeCSVStream,
               TestPhaseShifter.TestPhaseShifter,
               TestRatingSet.TestRatingSet, 
               TestStation.TestStation, 
               TestStationCSVStream.TestStationCSVStream,
               TestTransformer.TestTransformer
               ]



suitel = unittest.TestLoader()


suites_list = []
for test_class in testclasses:
    suite = suitel.loadTestsFromTestCase(test_class)
    suites_list.append(suite)

big_suite = unittest.TestSuite(suites_list)

runner = unittest.TextTestRunner(verbosity=2)
results = runner.run(big_suite)




