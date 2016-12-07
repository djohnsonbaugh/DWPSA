import unittest
import io
import os
from EMSCSVFormat.EMSCSVImporter import EMSCSVImporter
from EMSCSVFormat.FileType import FileType
from Network.Network import Network
from Network.Company import Company
from Network.CircuitBreaker import CircuitBreaker
from Network.CircuitBreaker import CBState

class TestEMSCSVImporter(unittest.TestCase):
    #Test Network
    n = Network()
    #Test Company Data
    n.AddCompanyByDef("C1", False, True)
    n.AddCompanyByDef("C2", True, False)
    #Test Division Data
    n.AddDivisionByDef("D1", "C1")
    n.AddDivisionByDef("D2", "C1")
    n.AddDivisionByDef("D3", "C2")
    n.AddDivisionByDef("D4", "C2")
    #Test Station Data
    n.AddStationByDef("S1","C1","D1")
    n.AddStationByDef("S2","C1","D1")
    n.AddStationByDef("S3","C1","D2")
    n.AddStationByDef("S4","C1","D2")
    n.AddStationByDef("S5","C2","D3")
    n.AddStationByDef("S6","C2","D3")
    n.AddStationByDef("S7","C2","D4")
    n.AddStationByDef("S8","C2","D4")
    #Test Node Data
    n.AddNodeByDef("S1", "115", "N1")
    n.AddNodeByDef("S1", "115", "N2")
    n.AddNodeByDef("S2", "15", "N1")
    n.AddNodeByDef("S2", "15", "N2")
    n.AddNodeByDef("S3", "5", "N1")
    n.AddNodeByDef("S3", "5", "N2")
    n.AddNodeByDef("S4", "1115", "N1")
    n.AddNodeByDef("S5", "1115", "N2")
    n.AddNodeByDef("S6", "115", "N1a")
    n.AddNodeByDef("S6", "115", "N2a")
    n.AddNodeByDef("S7", "15", "N1a")
    n.AddNodeByDef("S7", "15", "N2a")
    n.AddNodeByDef("S8", "5", "N11")
    n.AddNodeByDef("S8", "5", "N22")
    #Test CB Data
    n.AddNodeConnector(CircuitBreaker("S1", "115", "N1", "N2", "CB1", "C1", CBState.Closed, "CB"))
    n.AddNodeConnector(CircuitBreaker("S2", "15", "N1", "N2", "CB1", "C1", CBState.Closed, "CB"))
    n.AddNodeConnector(CircuitBreaker("S3", "5", "N1", "N2", "CB1", "C1", CBState.Closed, "CB"))
    n.AddNodeConnector(CircuitBreaker("S6", "115", "N1a", "N2a", "CB1", "C2", CBState.Open, "SW"))
    n.AddNodeConnector(CircuitBreaker("S7", "15", "N1a", "N2a", "CB1", "C2", CBState.Open, "BR"))
    n.AddNodeConnector(CircuitBreaker("S8", "5", "N11", "N22", "CB1", "C2", CBState.Open, "BR"))

    companyfile = "tempcompany.csv"
    companyheader = "CompanyName,Changed,PTINUM,LOSS_AREA,AWR_AREA"
    companypmap = {
                    "CompanyName" : "CompanyName",
                    "PTINUM" : "CompanyNumber",
                    "LOSS_AREA" : "EnforceLosses",
                    "AWR_AREA" : "AWR"
                    }

    divisionfile = "tempdivision.csv"
    divisionheader = "DivisionName,CompanyName,Changed"
    divisionpmap = {
                    "CompanyName" : "CompanyName",
                    "DivisionName" : "DivisionName"
                    }

    stationfile = "tempstation.csv"
    stationheader = "CompanyName,DivisionName,StationName,Changed"
    stationpmap = {
                    "CompanyName" : "CompanyName",
                    "DivisionName" : "DivisionName",
                    "StationName" : "StationName"
                    }

    nodefile = "tempnode.csv"
    nodeheader = "NodeName,CompanyName,StationName,Voltage,changed"
    nodepmap = {
                "NodeName" : "NodeName",
                "CompanyName" : "CompanyName",
                "StationName" : "StationName",
                "Voltage" : "Voltage"
                }
    cbfile = "tempcb.csv"
    cbheader = "ID_CO,ID_DV,ID_ST,CBTYP Name,CB Name,From Node,To Node,Normal State,KV_ID,Changed"
    cbpmap = {
                "ID_CO" : "Owner",
                "ID_ST" : "StationName",
                "CBTYP Name" : "CBType",
                "CB Name" : "CBName",
                "From Node" : "FromNodeName",
                "To Node" : "ToNodeName",
                "Normal State" : "NormalState",
                "KV_ID" : "Voltage"
                }

    def test_Constructor(self):

        encoding = "test"

        imp = EMSCSVImporter(os.getcwd(), encoding)

        self.assertEqual(imp.Directory, os.getcwd())
        self.assertEqual(encoding, imp.Encoding)
        self.assertEqual(len(imp.CSVFileNames), 0)
        self.assertEqual(len(imp.CSVPropertyMaps), 0)

        return

    def test_CSVParameters(self):

        filename = "testfilename"
        ft = FileType.Company
        propertytofilemap = {
                        "ColB" : "BCol",
                        "ColA" : "ACol",
                        }

        imp = EMSCSVImporter()

        imp.setCSVFileName(ft, filename)
        imp.setCSVPropertyMap(ft, propertytofilemap)

        self.assertEqual(filename, imp.CSVFileNames[ft])
        self.assertEqual(propertytofilemap, imp.CSVPropertyMaps[ft])


        return
    def test_ImportCompanies(self):
        net = Network()
        imp = self.GetImporter()

        self.CreateCompanyFile(self.companyfile)        

        imp.ImportCompanies(net)

        self.ValidateCompany(net)

        os.remove(self.companyfile)

        return

    def test_ImportDivisions(self):
        net = Network()
        imp = self.GetImporter()

        self.CreateDivisionFile(self.divisionfile)        

        imp.ImportDivisions(net)

        self.ValidateDivision(net)

        os.remove(self.divisionfile)

        return

    def test_ImportStations(self):
        net = Network()
        imp = self.GetImporter()

        self.CreateStationFile(self.stationfile)        

        imp.ImportStations(net)

        self.ValidateStation(net)

        os.remove(self.stationfile)

        return

    def test_ImportNodes(self):
        net = Network()
        imp = self.GetImporter()

        self.CreateNodeFile(self.nodefile)        

        imp.ImportNodes(net)

        self.ValidateNode(net)

        os.remove(self.nodefile)

        return

    def test_Import(self):
        
        net = Network()
        imp = self.GetImporter()

        self.CreateCompanyFile(self.companyfile)        
        self.CreateDivisionFile(self.divisionfile)
        self.CreateStationFile(self.stationfile)
        self.CreateNodeFile(self.nodefile)
        self.CreateCBFile(self.cbfile)

        imp.Import(net)

        self.ValidateCompany(net)
        self.ValidateDivision(net)
        self.ValidateStation(net)
        self.ValidateNode(net)
        self.ValidateCB(net)

        os.remove(self.companyfile)
        os.remove(self.divisionfile)
        os.remove(self.stationfile)
        os.remove(self.nodefile)
        os.remove(self.cbfile)

        return




    def ValidateCompany(self, net : Network):
        self.assertEqual(len(self.n.Companies),len(net.Companies))
        self.assertEqual(self.n.Companies["C1"].ID, net.Companies["C1"].ID)
        self.assertEqual(self.n.Companies["C1"].EnforceLosses, net.Companies["C1"].EnforceLosses)
        self.assertEqual(self.n.Companies["C1"].AWR, net.Companies["C1"].AWR)
        return

    def ValidateDivision(self, net : Network):
        self.assertEqual(len(self.n.Companies["C1"].Divisions),len(net.Companies["C1"].Divisions))
        self.assertEqual(len(self.n.Companies["C2"].Divisions),len(net.Companies["C2"].Divisions))
        self.assertEqual(self.n.Companies["C1"].Divisions["D1"].ID, net.Companies["C1"].Divisions["D1"].ID)
        self.assertEqual(self.n.Companies["C1"].Divisions["D1"].CompanyID, net.Companies["C1"].Divisions["D1"].CompanyID)
        return
    def ValidateStation(self, net : Network):
        self.assertEqual(len(self.n.Stations),len(net.Stations))
        self.assertEqual(self.n.Stations["S1"].ID, net.Stations["S1"].ID)
        self.assertEqual(self.n.Stations["S1"].CompanyID, net.Stations["S1"].CompanyID)
        self.assertEqual(self.n.Stations["S1"].DivisionID, net.Stations["S1"].DivisionID)
        return
    def ValidateNode(self, net : Network):
        self.assertEqual(len(self.n.Nodes),len(net.Nodes))
        self.assertEqual(self.n.Nodes[("S1","N1")].ID, net.Nodes[("S1","N1")].ID)
        self.assertEqual(self.n.Nodes[("S1","N1")].CompanyID, net.Nodes[("S1","N1")].CompanyID)
        return
    def ValidateCB(self, net : Network):
        self.assertEqual(len(self.n.CircuitBreakers),len(net.CircuitBreakers))
        self.assertEqual(self.n.CircuitBreakers[("S1","CB1","CB")].ID, net.CircuitBreakers[("S1","CB1","CB")].ID)
        self.assertEqual(self.n.CircuitBreakers[("S1","CB1","CB")].FromNodeID, net.CircuitBreakers[("S1","CB1","CB")].FromNodeID)
        self.assertEqual(self.n.CircuitBreakers[("S1","CB1","CB")].ToNodeID, net.CircuitBreakers[("S1","CB1","CB")].ToNodeID)
        return
    def CreateCompanyFile(self, filename=companyfile):
        with open(filename, 'w') as file:
            file.write(self.companyheader + "\n")
            for c in self.n.Companies.values():
                file.write(self.CSVLine(
                                        c.ID, 
                                        "FALSE", 
                                        "",
                                        int(c.EnforceLosses), 
                                        int(c.AWR)
                                      ))
        return
    def CreateDivisionFile(self, filename=divisionfile):
        with open(filename, 'w') as file:
            file.write(self.divisionheader + "\n")
            for c in self.n.Companies.values():
                for d in c.Divisions.values():
                    file.write(self.CSVLine(
                                            d.ID,
                                            d.CompanyID, 
                                            "FALSE"
                                          ))
        return
    def CreateStationFile(self, filename=stationfile):
        with open(filename, 'w') as file:
            file.write(self.stationheader + "\n")
            for s in self.n.Stations.values():
                file.write(self.CSVLine(
                                        s.CompanyID,
                                        s.DivisionID,
                                        s.ID, 
                                        "FALSE"
                                      ))
        return
    def CreateNodeFile(self, filename=nodefile):
        with open(filename, 'w') as file:
            file.write(self.nodeheader + "\n")
            for s in self.n.Nodes.values():
                file.write(self.CSVLine(
                                        s.Name,
                                        s.CompanyID,
                                        s.StationID,
                                        s.Voltage,
                                        "FALSE"
                                      ))
        return
    def CreateCBFile(self, filename=cbfile):
        with open(filename, 'w') as file:
            file.write(self.cbheader + "\n")
            for s in self.n.CircuitBreakers.values():
                file.write(self.CSVLine(
                                        s.OwnerCompanyID, "",
                                        s.StationID,
                                        s.CBType,
                                        s.Name,
                                        s.FromNodeName,
                                        s.ToNodeName,
                                        str(s.NormalState.name),
                                        s.Voltage,
                                        "FALSE"
                                      ))
        return
    def GetImporter(self):
        imp = EMSCSVImporter()
        imp.setCSVFileName(FileType.Company, self.companyfile)
        imp.setCSVPropertyMap(FileType.Company, self.companypmap)
        imp.setCSVFileName(FileType.Division, self.divisionfile)
        imp.setCSVPropertyMap(FileType.Division, self.divisionpmap)
        imp.setCSVFileName(FileType.Station, self.stationfile)
        imp.setCSVPropertyMap(FileType.Station, self.stationpmap)
        imp.setCSVFileName(FileType.Node, self.nodefile)
        imp.setCSVPropertyMap(FileType.Node, self.nodepmap)
        imp.setCSVFileName(FileType.CircuitBreaker, self.cbfile)
        imp.setCSVPropertyMap(FileType.CircuitBreaker, self.cbpmap)
        return imp
    def CSVLine(self, *args):
        line = ""
        for arg in args:
            line += str(arg)
            line += ","
        return line  + "\n"
if __name__ == '__main__':
    unittest.main()
