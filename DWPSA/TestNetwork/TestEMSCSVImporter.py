import unittest
import io
import os
from  Network.EMSCSVImporter import EMSCSVImporter
from EMSCSVFormat.FileType import FileType
from Network.Network import Network
from Network.Company import Company

class TestEMSCSVImporter(unittest.TestCase):
    #Test Network
    n = Network()
    #Test Company Data
    n.AddCompanyByDef("C1", False, True)
    n.AddCompanyByDef("C2", True, False)
    n.AddDivisionByDef("D1", "C1")
    n.AddDivisionByDef("D2", "C1")
    n.AddDivisionByDef("D3", "C2")
    n.AddDivisionByDef("D4", "C2")

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

    def test_Import(self):
        
        net = Network()
        imp = self.GetImporter()

        self.CreateCompanyFile(self.companyfile)        
        self.CreateDivisionFile(self.divisionfile)

        imp.Import(net)

        self.ValidateCompany(net)
        self.ValidateDivision(net)

        os.remove(self.companyfile)
        os.remove(self.divisionfile)

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
    def GetImporter(self):
        imp = EMSCSVImporter()
        imp.setCSVFileName(FileType.Company, self.companyfile)
        imp.setCSVPropertyMap(FileType.Company, self.companypmap)
        imp.setCSVFileName(FileType.Division, self.divisionfile)
        imp.setCSVPropertyMap(FileType.Division, self.divisionpmap)
        return imp
    def CSVLine(self, *args):
        line = ""
        for arg in args:
            line += str(arg)
            line += ","
        return line  + "\n"
if __name__ == '__main__':
    unittest.main()
