import unittest
import io
import os
from EMSCSVFormat.EMSCSVImporter import EMSCSVImporter
from EMSCSVFormat.FileType import FileType
from Network.Network import Network
from Network.Company import Company
from Network.Branch import Branch
from Network.RatingSet import RatingSet
from Network.CircuitBreaker import CircuitBreaker
from Network.CircuitBreaker import CBState
from Network.Transformer import Transformer
from Network.PhaseShifter import PhaseShifter
from Network.Load import Load
from Network.Shunt import Shunt
from Network.Unit import Unit

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
    n.AddNodeByDef("S1", "345", "N3")
    n.AddNodeByDef("S2", "15", "N1")
    n.AddNodeByDef("S2", "15", "N2")
    n.AddNodeByDef("S2", "115", "N3")
    n.AddNodeByDef("S3", "5", "N1")
    n.AddNodeByDef("S3", "5", "N2")
    n.AddNodeByDef("S3", "115", "N3")
    n.AddNodeByDef("S4", "1115", "N1")
    n.AddNodeByDef("S5", "1115", "N2")
    n.AddNodeByDef("S6", "115", "N1a")
    n.AddNodeByDef("S6", "115", "N2a")
    n.AddNodeByDef("S6", "345", "N3")
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
    #Test Branch Data
    n.AddNodeConnector(Branch("S1","115","N1", "S6", "115", "N1a", "LN1", "C1", False, 0.001, 0.002, "1", RatingSet(400,500), RatingSet(600, 700)))
    n.AddNodeConnector(Branch("S1","115","N2", "S6", "115", "N2a", "LN1", "C1", False, 0.01, 0.02, "2", RatingSet(40,50), RatingSet(60, 70)))
    n.AddNodeConnector(Branch("S2","15","N1", "S7", "15", "N1a", "LN2", "C1", False, 0.0001, 0.0002, "1", RatingSet(4000,5000), RatingSet(6000, 7000)))
    n.AddNodeConnector(Branch("S2","15","N1", "S7", "15", "N1a", "LN2", "C2", False, 0.1, 0.2, "2", RatingSet(4,5), RatingSet(6, 7)))
    n.AddNodeConnector(Branch("S3","5","N1", "S8", "5", "N11", "LN3", "C2", False, 0.0005, 0.001, "A", RatingSet(1400,1500), RatingSet(1600, 1700)))
    n.AddNodeConnector(Branch("S3","5","N1", "S8", "5", "N22", "LN4", "C2", False, 0.051, 0.052, "B", RatingSet(140,150), RatingSet(160, 170)))
    n.AddNodeConnector(Branch("S4","1115","N1", "S5", "1115", "N2", "LN5", "C1", False, 0.051, 0.052, "C", RatingSet(140,150), RatingSet(160, 170)))
    #Test Transformer Data
    n.AddNodeConnector(Transformer("S1", "115", "N1", "345", "N3", "XF", "C1", True, 1.1, 2.2))
    n.AddNodeConnector(Transformer("S2", "15", "N1", "115", "N3", "XF", "C1", True, 1.1, 2.2))
    n.AddNodeConnector(Transformer("S3", "5", "N1", "115", "N3", "XF", "C1", True, 1.1, 2.2))
    n.AddNodeConnector(Transformer("S6", "115", "N1a", "345", "N3", "XF", "C2", False, 1.1, 2.2))
    #Test PhaseShifter Data
    n.AddNodeConnector(PhaseShifter("S1", "115", "N1", "115", "N2","PS1","C1",1.1,2.5, RatingSet(400,500), RatingSet(600, 700)))
    n.AddNodeConnector(PhaseShifter("S2", "15", "N1", "15", "N2","PS1","C1",1.1,2.5, RatingSet(400,500), RatingSet(600, 700)))
    n.AddNodeConnector(PhaseShifter("S3", "5", "N1", "5", "N2","PS1","C1",1.1,2.5, RatingSet(400,500), RatingSet(600, 700)))
    n.AddNodeConnector(PhaseShifter("S6", "115", "N1a", "115", "N2a","PS2","C2",1.1,2.5, RatingSet(400,500), RatingSet(600, 700)))
    n.AddNodeConnector(PhaseShifter("S8", "5", "N11", "5", "N22","PS","C2",1.1,2.5, RatingSet(400,500), RatingSet(600, 700)))
    #Test Load Data
    n.AddDevice(Load("S1", "115", "N1", "LD1", "C1", 1,.5, .95))
    n.AddDevice(Load("S2", "15", "N2", "LD2", "C1", 1,.5, .95))
    n.AddDevice(Load("S3", "5", "N3", "LD3", "C1", 1,.5, .95))
    n.AddDevice(Load("S4", "1115", "N1", "LD4", "C1", 1,.5, .95))
    n.AddDevice(Load("S6", "115", "N1a", "LD1", "C2", 1,.5, .95))
    n.AddDevice(Load("S7", "15", "N1a", "LD2", "C2", 1,.5, .95))
    n.AddDevice(Load("S8", "5", "N11", "LD3", "C2", 1,.5, .95))
    n.AddDevice(Load("S5", "1115", "N2", "LD4", "C2", 1,.5, .95))
    #Test Shunt Data
    n.AddDevice(Shunt("S1", "115", "N1", "SH1", "C1", 20))
    n.AddDevice(Shunt("S2", "15", "N2", "SH2", "C1", 20))
    n.AddDevice(Shunt("S3", "5", "N3", "SH3", "C1", 20))
    n.AddDevice(Shunt("S4", "1115", "N1", "SH4", "C1", 20))
    n.AddDevice(Shunt("S6", "115", "N1a", "SH1", "C2", 20))
    n.AddDevice(Shunt("S7", "15", "N1a", "SH2", "C2", 20))
    n.AddDevice(Shunt("S8", "5", "N11", "SH3", "C2", 20))
    n.AddDevice(Shunt("S5", "1115", "N2", "SH4", "C2", 20))
    #Test Unit Data
    n.AddDevice(Unit("S1", "115", "N1", "UN1", "C1", 100.5, 10, 10, -10, .95, False, 20))
    n.AddDevice(Unit("S2", "15", "N2", "UN2", "C1", 100.5, 10, 10, -10, .95, False, 20))
    n.AddDevice(Unit("S3", "5", "N3", "UN3", "C1", 100.5, 10, 10, -10, .95, False, 20))
    n.AddDevice(Unit("S4", "1115", "N1", "UN4", "C1", 100.5, 10, 10, -10, .95, False, 20))
    n.AddDevice(Unit("S6", "115", "N1a", "UN1", "C2", 100.5, 10, 10, -10, .95, False, 20))
    n.AddDevice(Unit("S7", "15", "N1a", "UN2", "C2", 100.5, 10, 10, -10, .95, False, 20))
    n.AddDevice(Unit("S8", "5", "N11", "UN3", "C2", 100.5, 10, 10, -10, .95, False, 20))
    n.AddDevice(Unit("S5", "1115", "N2", "UN4", "C2", 100.5, 10, 10, -10, .95, False, 20))

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
    linefile = "templine.csv"
    lineheader = "LINE_NDX,ZBR_NDX,FROM_CO,FROM_ST ,FROM_KV,FROM_ND,FROM_PTINAM,FROM_PTINUM,TO_CO,TO_ST   ,TO_KV,TO_ND,TO_PTINAM   ,TO_PTINUM,Line_Name     ,Segment Name,r,x,bch,CO_OWNER,Summer Normal rating,Summer Emergency rating,Winter Normal rating,Winter Emergency rating,Changed,Monitored"
    linepmap = {
                "FROM_ST" : "FromStationName",
                "FROM_KV" : "FromVoltage",
                "FROM_ND" : "FromNodeName",
                "TO_ST" : "ToStationName",
                "TO_KV" : "ToVoltage",
                "TO_ND" : "ToNodeName",
                "Line_Name" : "LineName",
                "Segment Name" : "Segment",
                "r" : "r",
                "x" : "x",
                "CO_OWNER" : "Owner",
                "Summer Normal rating" : "SumNorm",
                "Summer Emergency rating" : "SumEmer",
                "Winter Normal rating" : "WinNorm",
                "Winter Emergency rating" : "WinEmer",
                "Monitored" : "Monitored"
                }
    xffile = "tempxf.csv"
    xfheader = "ID_CO,ID_DV,ID_ST,ID,From Connection Node (LTC SIDE),From Nominal Voltage (LTC SIDE),From Tap Type (LTC SIDE),From Normal Position (LTC SIDE),To Connection Node (FIXED SIDE),To Nominal KV (FIXED SIDE),To Tap Type (FIXED SIDE),To Normal Tap (FIXED SIDE),Regulation Node,r,x,Regulation Schedule,AVR Status,SummerNormalLimit,SummerEmergencyLimt,WinterNormalLimit,WinterEmergencyLimit,Changed,Monitored"
    xfpmap = {
                "ID_CO" : "Owner",
                "ID_ST" : "StationName",
                "ID" : "TransformerName",
                "From Connection Node (LTC SIDE)" : "FromNodeName",
                "From Nominal Voltage (LTC SIDE)" : "FromVoltage",
                "From Tap Type (LTC SIDE)" : "FromTapType",
                "From Normal Position (LTC SIDE)" : "FromTapNormPosition",
                "To Connection Node (FIXED SIDE)" : "ToNodeName",
                "To Nominal KV (FIXED SIDE)" : "ToVoltage",
                "To Tap Type (FIXED SIDE)" : "ToTapType",
                "To Normal Tap (FIXED SIDE)" : "ToTapNormPosition",
                "Regulation Node" : "RegulationNodeName",
                "r" : "r",
                "x" : "x",
                "AVR Status" : "AVRStatus",
                "SummerNormalLimit" : "SumNorm",
                "SummerEmergencyLimt" : "SumEmer",
                "WinterNormalLimit" : "WinNorm",
                "WinterEmergencyLimit" : "WinEmer",
                "Monitored" : "Monitored"
                }
    psfile = "tempps.csv"
    psheader = "Company,Division,Station,TransformerName,FromNode,FromNominalVoltage,FromLTCTapType,FromNormalPosition,ToConnectionNode,ToNominalVoltage,ToLTCTapType,ToNormalTap,RegulationNode,r,x,VoltageRegulationSchedule,AVRStatus,PhaseTapType,AWRStatus,MWRegulationSchedule,Summer Normal,Summer Emergency,Winter Normal,Winter Emergency,changed"
    pspmap = {
                "Company" : "Owner",
                "Station" : "StationName",
                "TransformerName" : "PhaseShifterName",
                "FromNode" : "FromNodeName",
                "FromNominalVoltage" : "FromVoltage",
                "FromLTCTapType" : "FromTapType",
                "FromNormalPosition" : "FromTapNormPosition",
                "ToConnectionNode" : "ToNodeName",
                "ToNominalVoltage" : "ToVoltage",
                "ToLTCTapType" : "ToTapType",
                "ToNormalTap" : "ToTapNormPosition",
                "RegulationNode" : "RegulationNodeName",
                "r" : "r",
                "x" : "x",
                "AVRStatus" : "AVRStatus",
                "PhaseTapType" : "PhaseTapType",
                "AWRStatus" : "AWRStatus",
                "Summer Normal" : "SumNorm",
                "Summer Emergency" : "SumEmer",
                "Winter Normal" : "WinNorm",
                "Winter Emergency" : "WinEmer"
                }
    ldfile = "templd.csv"
    ldheader = "Company,Station ,KV  ,Node Name,PTI Name    ,PTI Number,Load Name     ,MW NonConforming,MVar NonConforming,MW Conforming,Power Factor Conforming,Load Area,Load Control Area,Changed"
    ldpmap = {
                "Company" : "Owner",
                "Station" : "StationName",
                "KV" : "Voltage",
                "Node Name" : "NodeName",
                "Load Name" : "LoadName",
                "MW NonConforming" : "MWNonCon",
                "MVar NonConforming" : "MVNonCon",
                "MW Conforming" : "MWCon",
                "Power Factor Conforming" : "PowerFactorCon"
                }
    shfile = "tempsh.csv"
    shheader = "Company,Station,KV,Shunt Name,Node,Regulation Node,Nominal MVar,Voltage Target PU,Deviation,Changed"
    shpmap = {
                "Company" : "Owner",
                "Station" : "StationName",
                "KV" : "Voltage",
                "Node" : "NodeName",
                "Regulation Node" : "RegNodeName",
                "Shunt Name" : "ShuntName",
                "Nominal MVar" : "MVar",
                "Voltage Target PU" : "VoltagePUTarget",
                "Deviation" : "VoltageTargetDeviation"
                }
    unfile = "tempun.csv"
    unheader = "Company,Station,KV,Unit Name,Connection Node,Regulation Node,BaseM,Participation Factor,MW Max,MW MN,Mvar Max,Mvar Min,Voltage Target (PU),Deviation,Mvar Capability Curve,NO AGC,Changed"
    unpmap = {
                "Company" : "Owner",
                "Station" : "StationName",
                "KV" : "Voltage",
                "Unit Name" : "UnitName",
                "Connection Node" : "NodeName",
                "Regulation Node" : "RegNodeName",
                "BaseM" : "InitialMW",
                "Participation Factor" : "ParticipationFactor",
                "MW Max" : "MWMax",
                "MW MN" : "MWMin",
                "Mvar Max" : "MVarMax",
                "Mvar Min" : "MVarMin",
                "Voltage Target (PU)" : "VoltagePUTarget",
                "Deviation" : "VoltageTargetDeviation",
                "NO AGC" : "NoAGC"
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
        self.CreateLineFile(self.linefile)
        self.CreateTransformerFile(self.xffile)
        self.CreatePhaseShifterFile(self.psfile)
        self.CreateLoadFile(self.ldfile)
        self.CreateShuntFile(self.shfile)
        self.CreateUnitFile(self.unfile)

        imp.Import(net)

        self.ValidateCompany(net)
        self.ValidateDivision(net)
        self.ValidateStation(net)
        self.ValidateNode(net)
        self.ValidateCB(net)
        self.ValidateLine(net)
        self.ValidatePhaseShifter(net)
        self.ValidateLoad(net)
        self.ValidateShunt(net)
        self.ValidateUnit(net)

        os.remove(self.companyfile)
        os.remove(self.divisionfile)
        os.remove(self.stationfile)
        os.remove(self.nodefile)
        os.remove(self.cbfile)
        os.remove(self.linefile)
        os.remove(self.xffile)
        os.remove(self.psfile)
        os.remove(self.ldfile)
        os.remove(self.shfile)
        os.remove(self.unfile)
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
    def ValidateLine(self, net : Network):
        self.assertEqual(len(self.n.Lines),len(net.Lines))
        self.assertEqual(self.n.Lines[("S1","LN1","1")].ID, net.Lines[("S1","LN1","1")].ID)
        self.assertEqual(self.n.Lines[("S2","LN2","1")].Impedance, net.Lines[("S2","LN2","1")].Impedance)
        self.assertEqual(self.n.Lines[("S3","LN3","A")].Monitored, net.Lines[("S3","LN3","A")].Monitored)
        self.assertEqual(self.n.Lines[("S4","LN5","C")].WiRating.Normal, net.Lines[("S4","LN5","C")].WiRating.Normal)
        self.assertEqual(self.n.Lines[("S1","LN1","1")].ID, net.Lines[("S1","LN1","1")].ID)
        return
    def ValidateTransformer(self, net : Network):
        self.assertEqual(len(self.n.Transformers),len(net.Transformers))
        self.assertEqual(self.n.Transformers[("S1","XF","XF")].ID, net.Transformers[("S1","XF","XF")].ID)
        self.assertEqual(self.n.Transformers[("S2","XF","XF")].Impedance, net.Transformers[("S2","XF","XF")].Impedance)
        self.assertEqual(self.n.Transformers[("S3","XF","XF")].Monitored, net.Transformers[("S3","XF","XF")].Monitored)
        self.assertEqual(self.n.Transformers[("S6","XF","XF")].ID, net.Transformers[("S6","XF","XF")].ID)
        return
    def ValidatePhaseShifter(self, net : Network):
        self.assertEqual(len(self.n.PhaseShifters),len(net.PhaseShifters))
        self.assertEqual(self.n.PhaseShifters[("S1","PS1","PS1")].ID, net.PhaseShifters[("S1","PS1","PS1")].ID)
        self.assertEqual(self.n.PhaseShifters[("S2","PS1","PS1")].Impedance, net.PhaseShifters[("S2","PS1","PS1")].Impedance)
        self.assertEqual(self.n.PhaseShifters[("S3","PS1","PS1")].Monitored, net.PhaseShifters[("S3","PS1","PS1")].Monitored)
        self.assertEqual(self.n.PhaseShifters[("S8","PS","PS")].ID, net.PhaseShifters[("S8","PS","PS")].ID)
        return
    def ValidateLoad(self, net : Network):
        self.assertEqual(len(self.n.Loads),len(net.Loads))
        self.assertEqual(self.n.Loads[("S1","LD1", "LD")].ID, net.Loads[("S1","LD1", "LD")].ID)
        self.assertEqual(self.n.Loads[("S1","LD1", "LD")].PowerFactor, net.Loads[("S1","LD1", "LD")].PowerFactor)
        self.assertEqual(self.n.Loads[("S1","LD1", "LD")].Conforming.real, net.Loads[("S1","LD1", "LD")].Conforming.real)
        return
    def ValidateShunt(self, net : Network):
        self.assertEqual(len(self.n.Shunts),len(net.Shunts))
        self.assertEqual(self.n.Shunts[("S1","SH1", "SH")].ID, net.Shunts[("S1","SH1", "SH")].ID)
        self.assertEqual(self.n.Shunts[("S1","SH1", "SH")].MVar, net.Shunts[("S1","SH1", "SH")].MVar)
        return
    def ValidateUnit(self, net : Network):
        self.assertEqual(len(self.n.Units),len(net.Units))
        self.assertEqual(self.n.Units[("S1","UN1", "UN")].ID, net.Units[("S1","UN1", "UN")].ID)
        self.assertEqual(self.n.Units[("S1","UN1", "UN")].MVAMax, net.Units[("S1","UN1", "UN")].MVAMax)
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
    def CreateLineFile(self, filename=linefile):
        with open(filename, 'w') as file:
            file.write(self.lineheader + "\n")
            for s in self.n.Lines.values():
                file.write(self.CSVLine("","","",
                                        s.FromStationID,
                                        s.FromVoltage,
                                        s.FromNodeName,
                                        "","","",
                                        s.ToStationID,
                                        s.ToVoltage,
                                        s.ToNodeName,
                                        "","",
                                        s.Name,
                                        s.Segment,
                                        str(s.Impedance.real),
                                        str(s.Impedance.imag),
                                        "",
                                        s.OwnerCompanyID,
                                        str(s.SuRating.Normal),
                                        str(s.SuRating.Emergency),
                                        str(s.WiRating.Normal),
                                        str(s.WiRating.Emergency),
                                        "",
                                        str(s.Monitored)
                                      ))
        return
    def CreateTransformerFile(self, filename=xffile):
        with open(filename, 'w') as file:
            file.write(self.xfheader + "\n")
            for s in self.n.Transformers.values():
                file.write(self.CSVLine(
                                        s.OwnerCompanyID,
                                        "",
                                        s.StationID,
                                        s.Name,
                                        s.FromNodeName,
                                        s.FromVoltage,
                                        s.FromTapType,
                                        s.FromTapNormPosition,
                                        s.ToNodeName,
                                        s.ToVoltage,
                                        s.ToTapType,
                                        s.ToTapNormPosition,
                                        s.RegulationNodeName,
                                        str(s.Impedance.real),
                                        str(s.Impedance.imag),
                                        "",
                                        str(s.AVRStatus),
                                        "","","","",
                                        "",
                                        str(s.Monitored)
                                      ))
        return
    def CreatePhaseShifterFile(self, filename=psfile):
        with open(filename, 'w') as file:
            file.write(self.psheader + "\n")
            for s in self.n.PhaseShifters.values():
                file.write(self.CSVLine(
                                        s.OwnerCompanyID,
                                        "",
                                        s.StationID,
                                        s.Name,
                                        s.FromNodeName,
                                        s.FromVoltage,
                                        s.FromTapType,
                                        s.FromTapNormPosition,
                                        s.ToNodeName,
                                        s.ToVoltage,
                                        s.ToTapType,
                                        s.ToTapNormPosition,
                                        s.RegulationNodeName,
                                        str(s.Impedance.real),
                                        str(s.Impedance.imag),
                                        "",
                                        str(s.AVRStatus),
                                        s.PhaseTapType,
                                        str(s.AWRStatus),
                                        "","","","",
                                        ""                                      
                                        ))
        return
    def CreateLoadFile(self, filename=ldfile):
        with open(filename, 'w') as file:
            file.write(self.ldheader + "\n")
            for s in self.n.Loads.values():
                file.write(self.CSVLine(
                                        s.OwnerCompanyID,
                                        s.StationID,
                                        s.Voltage,
                                        s.NodeName,
                                        "","",
                                        s.Name,
                                        str(s.NonConforming.real),
                                        str(s.NonConforming.imag),
                                        str(s.Conforming.real),
                                        str(s.PowerFactor)
                                      ))
        return
    def CreateShuntFile(self, filename=shfile):
        with open(filename, 'w') as file:
            file.write(self.shheader + "\n")
            for s in self.n.Shunts.values():
                file.write(self.CSVLine(
                                        s.OwnerCompanyID,
                                        s.StationID,
                                        s.Voltage,
                                        s.Name,
                                        s.NodeName,
                                        s.RegulationNodeName,
                                        str(s.MVar),
                                        str(s.VoltagePUTarget),
                                        str(s.VoltageTargetDeviation),""
                                      ))
        return
    def CreateUnitFile(self, filename=unfile):
        with open(filename, 'w') as file:
            file.write(self.unheader + "\n")
            #Company,Station,KV,Unit Name,Connection Node,Regulation Node,BaseM,Participation Factor,MW Max,MW MN,Mvar Max,Mvar Min,Voltage Target (PU),Deviation,Mvar Capability Curve,NO AGC,Changed
            for s in self.n.Units.values():
                file.write(self.CSVLine(
                                        s.OwnerCompanyID,
                                        s.StationID,
                                        s.Voltage,
                                        s.Name,
                                        s.NodeName,
                                        s.RegulationNodeName,
                                        str(s.InitialMW),
                                        str(s.ParticipationFactor),
                                        str(s.MVAMax.real),
                                        str(s.MVAMin.real),
                                        str(s.MVAMax.imag),
                                        str(s.MVAMin.imag),    
                                        str(s.VoltagePUTarget),
                                        str(s.VoltageTargetDeviation),
                                        "",
                                        "FALSE", ""
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
        imp.setCSVFileName(FileType.Line, self.linefile)
        imp.setCSVPropertyMap(FileType.Line, self.linepmap)
        imp.setCSVFileName(FileType.Transformer, self.xffile)
        imp.setCSVPropertyMap(FileType.Transformer, self.xfpmap)
        imp.setCSVFileName(FileType.PhaseShifter, self.psfile)
        imp.setCSVPropertyMap(FileType.PhaseShifter, self.pspmap)
        imp.setCSVFileName(FileType.Load, self.ldfile)
        imp.setCSVPropertyMap(FileType.Load, self.ldpmap)
        imp.setCSVFileName(FileType.Shunt, self.shfile)
        imp.setCSVPropertyMap(FileType.Shunt, self.shpmap)
        imp.setCSVFileName(FileType.Unit, self.unfile)
        imp.setCSVPropertyMap(FileType.Unit, self.unpmap)
        return imp
    def CSVLine(self, *args):
        line = ""
        for arg in args:
            line += str(arg)
            line += ","
        return line  + "\n"
if __name__ == '__main__':
    unittest.main()
