import unittest
from TestNetwork import *
from TestEMSCSVFormat import *
from TestDEMNetworkExport import *
from TestCSVFileStream import *
from TestPROBECSVFormat import *
#from Network.Network import Network
#from EMSCSVFormat.EMSCSVImporter import EMSCSVImporter
#from dem import Group
#from DEMNetworkExport.SimpleExport import NetworkToDEMSimple
#import io

#n = Network()
#imp = EMSCSVImporter("C:\\PROBE\\2016Dec")
##imp = EMSCSVImporter("C:\EMS2016Dec")
#imp.Import(n)
#sn = n.CreateSubNetwork(n.ExpandSelectedCompanies(['CIN'],1,True))
#gp = Group([],[])
#gp = NetworkToDEMSimple(sn, [], [], "C:\\repo\\dwdem\\main.py", 1)
#gp.init_problem()
#gp.problem.solve()
#with open("testdemresult.txt", 'w') as file:
#    file.write(gp.results.summary())

testclasses = [
               TestBranch.TestBranch,
               TestCircuitBreaker.TestCircuitBreaker,
               TestCircuitBreakerCSVStream.TestCircuitBreakerCSVStream,
               TestCompany.TestCompany, 
               TestCompanyCSVStream.TestCompanyCSVStream,
               TestCPNode.TestCPNode,
               TestCSVFileStream.TestCSVFileStream,
               TestDevice.TestDevice,
               TestDivision.TestDivision, 
               TestDivisionCSVStream.TestDivisionCSVStream,
               TestEMSCSVImporter.TestEMSCSVImporter,
               TestEPNode.TestEPNode,
               TestLineCSVStream.TestLineCSVStream,
               TestLoad.TestLoad,
               TestLoadCSVStream.TestLoadCSVStream,
               TestNetwork.TestNetwork,
               TestNode.TestNode,
               TestNodeConnector.TestNodeConnector,
               TestNodeCSVStream.TestNodeCSVStream,
               TestPhaseShifter.TestPhaseShifter,
               TestPhaseShifterCSVStream.TestPhaseShifterCSVStream,
               TestPNode.TestPNode,
               TestRatingSet.TestRatingSet,
               TestSimpleExport.TestSimpleExport,
               TestShunt.TestShunt,
               TestShuntCSVStream.TestShuntCSVStream,
               TestStation.TestStation, 
               TestStationCSVStream.TestStationCSVStream,
               TestTransformer.TestTransformer,
               TestTransformerCSVStream.TestTransformerCSVStream,
               TestUnit.TestUnit,
               TestUnitCSVStream.TestUnitCSVStream
               ]



suitel = unittest.TestLoader()


suites_list = []
for test_class in testclasses:
    suite = suitel.loadTestsFromTestCase(test_class)
    suites_list.append(suite)

big_suite = unittest.TestSuite(suites_list)

runner = unittest.TextTestRunner(verbosity=2)
results = runner.run(big_suite)




