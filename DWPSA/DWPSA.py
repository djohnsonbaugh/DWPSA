import unittest
from TestNetwork import *
from TestEMSCSVFormat import *
from TestDEMNetworkExport import *
from Network.Network import Network
from EMSCSVFormat.EMSCSVImporter import EMSCSVImporter
from dem import Group
from DEMNetworkExport.SimpleExport import NetworkToDEMSimple
import io

n = Network()
#imp = EMSCSVImporter("C:\PROBE\Models\EMS2015Dec")
imp = EMSCSVImporter("C:\EMS2016Dec")
imp.Import(n)
gp = Group([],[])
gp = NetworkToDEMSimple(n, ["CIN"], [], "C:\\repo\\dem\\main.py")
gp.init_problem()
gp.problem.solve()
with open("testdemresult.txt", 'w') as file:
    file.write(gp.results.summary())

testclasses = [
               TestBranch.TestBranch,
               TestCircuitBreaker.TestCircuitBreaker,
               TestCircuitBreakerCSVStream.TestCircuitBreakerCSVStream,
               TestCompany.TestCompany, 
               TestCompanyCSVStream.TestCompanyCSVStream,
               TestCSVFileStream.TestCSVFileStream,
               TestDevice.TestDevice,
               TestDivision.TestDivision, 
               TestDivisionCSVStream.TestDivisionCSVStream,
               TestEMSCSVImporter.TestEMSCSVImporter,
               TestLineCSVStream.TestLineCSVStream,
               TestLoad.TestLoad,
               TestLoadCSVStream.TestLoadCSVStream,
               TestNetwork.TestNetwork,
               TestNode.TestNode,
               TestNodeConnector.TestNodeConnector,
               TestNodeCSVStream.TestNodeCSVStream,
               TestPhaseShifter.TestPhaseShifter,
               TestPhaseShifterCSVStream.TestPhaseShifterCSVStream,
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




