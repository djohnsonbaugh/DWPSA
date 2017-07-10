import unittest
from TestNetwork import *
from TestEMSCSVFormat import *
from TestDEMNetworkExport import *
from TestCSVFileStream import *
from TestPROBECSVFormat import *
#from Network.Network import Network
#from EMSCSVFormat.EMSCSVImporter import EMSCSVImporter
#from PROBECSVFormat.PROBECSVImporter import PROBECSVImporter
#from dem import Group
#from DEMNetworkExport.SimpleExport import NetworkToDEMSimple
#import io
#import random
#import os
#from datetime import date
#from datetime import datetime
#from shutil import copyfile

#n = Network()
#imp = EMSCSVImporter("C:\\PROBE\\2016Dec")
#imp.Import(n)
#mktday = date(2016, 12,22)
#dimp = PROBECSVImporter(mktday, "C:\\PROBE\\20161222")
#dimp.Import(n)
#dates = []
#for i in range(0,24):
#    dates.append(datetime(2016,12,22,i))
#for i in [1000, 1500, 2000, 2500]:
#    successcount =0
#    attempt = 0
#    while successcount <10:
#        attempt+=1
#        print("Attempt {0} for bus {1}".format(attempt, i))
#        try:
#            sn = n.CreateSubNetwork([],n.ExapandSelectedStations([n.GetRandomStationID(True)], 32, i, True))
#            gp = NetworkToDEMSimple(sn, [], [], date(2016,12,22), datetime(2016,12,22,14), "C:\\repo\\dwdem\\main.py", 1.0 + float(random.randint(-20,100))/100.0 , dates)
#            gp.init_problem(time_horizon=len(dates))   
#            gp.problem.solve()
#            with open("testdemresult.txt", 'w') as file:
#                file.write(gp.results.summary())
#            if os.path.getsize("testdemresult.txt") >100:
#                successcount+=1
#                print("Success {0} for bus {1}".format(successcount, i))
#                copyfile("C:\\repo\\dwdem\\main.py", "C:\\repo\\dwdem\\main_{0}bus_id{1}.py".format(i,successcount))
#                copyfile("testdemresult.txt", "C:\\repo\\dwdem\\result_{0}bus_id{1}.txt".format(i,successcount))
#        except: print("PROGRAM FAILURE")

#while input('Would you run subset  ?\n') == "y":
#    sn = n.CreateSubNetwork([],n.ExapandSelectedStations([n.GetRandomStationID(True)], 12, int(input('Enter Max Busses?\n')), True))
#    gp = NetworkToDEMSimple(sn, [], [], date(2016,12,22), datetime(2016,12,22,14), "C:\\repo\\dwdem\\main.py", 1)
#    gp.init_problem()
#    gp.problem.solve()
#    with open("testdemresult.txt", 'w') as file:
#        file.write(gp.results.summary())

testclasses = [
               TestBranch.TestBranch,
               TestBidDataCSVStream.TestBidDataCSVStream,
               TestCircuitBreaker.TestCircuitBreaker,
               TestCircuitBreakerCSVStream.TestCircuitBreakerCSVStream,
               TestCompany.TestCompany, 
               TestCompanyCSVStream.TestCompanyCSVStream,
               TestCostCurvesCSVStream.TestCostCurvesCSVStream,
               TestCPNode.TestCPNode,
               TestCSVFileStream.TestCSVFileStream,
               TestDayAheadLMPsCSVStream.TestDayAheadLMPsCSVStream,
               TestDemandBidsCSVStream.TestDemandBidsCSVStream,
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
               TestUnitCSVStream.TestUnitCSVStream,
               TestZonalFactorsCSVStream.TestZonalFactorsCSVStream
               ]



suitel = unittest.TestLoader()


suites_list = []
for test_class in testclasses:
    suite = suitel.loadTestsFromTestCase(test_class)
    suites_list.append(suite)

big_suite = unittest.TestSuite(suites_list)

runner = unittest.TextTestRunner(verbosity=2)
results = runner.run(big_suite)




