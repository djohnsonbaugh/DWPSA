from Network.Company import Company
from Network.Division import Division
from Network.Station import Station
from Network.Node import Node

class Network(object):
    """ Physical Description of a Power System """

    #Constructor
    def __init__(self):
        self.Nodes = {}
        self.Stations = {}
        self.Companies = {}
        return
    #Company Methods
    def AddCompany(self, company):
        if company.ID in self.Companies:
            raise Exception("Company already exists in the network", company.ID)
        self.Companies[company.ID] = company
        return self.Companies[company.ID]
    def AddCompanyByDef(self, companyid, enforcelosses = True, awr = True):
        return self.AddCompany(Company(companyid, enforcelosses, awr))
    def FindOrAddCompany(self, companyid):
        if companyid not in self.Companies:
            return self.AddCompanyByDef(companyid)
        else:
            return self.Companies[companyid]
    #Division Methods
    def AddDivision(self, division):
        company = self.FindOrAddCompany(division.CompanyID)
        company.AddDivision(division)
        return division
    def AddDivisionByDef(self, divisionid, companyid):
        return self.AddDivision(Division(divisionid, companyid))
    def FindOrAddDivision(self, divisionid, companyid):
        company = self.FindOrAddCompany(companyid)
        if divisionid in company.Divisions:
            return company.Divisions[divisionid]
        else:
            return self.AddDivisionByDef(divisionid, companyid)

    #Station Methods
    def AddStation(self, station):
        if station.ID in self.Stations:
            raise Exception("Station already exists in the network", station.ID)

        division = self.FindOrAddDivision(station.DivisionID, station.CompanyID)
        company = division.Company
        #Add Station to the Network
        self.Stations[station.ID] = station
        company.AddStation(station)
        division.AddStation(station)
        return station
    def AddStationByDef(self, stationid, companyid = "", divisionid = ""):
        return self.AddStation(Station(stationid, companyid, divisionid))
    def FindOrAddStation(self, stationid, companyid = "", divisionid = ""):
        if stationid in self.Stations:
            return self.Stations[stationid]  
        else:
            return self.AddStationByDef(stationid, companyid, divisionid)
    
    #Node Methods
    def AddNodeByDef(self, stationid, voltage, name, companyid = "", divisionid = ""):
        return self.AddNode(Node(stationid, voltage, name, companyid, divisionid))
    def AddNode(self, node):
        if node.ID in self.Nodes:
            raise Exception("Node already exists in the network", node.ID)
        station = self.FindOrAddStation(node.StationID, node.CompanyID, node.DivisionID)
        #Add Node to Network
        self.Nodes[node.ID] = node
        station.AddNode(node)               
        return node




