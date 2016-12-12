from Network.Company import Company
from Network.Division import Division
from Network.Station import Station
from Network.Node import Node
from Network.NodeConnector import NodeConnector
from Network.CircuitBreaker import CircuitBreaker
from Network.Branch import Branch
from Network.Transformer import Transformer
from Network.PhaseShifter import PhaseShifter
from Network.Unit import Unit
from Network.Device import Device
from Network.Shunt import Shunt
from Network.Load import Load

class Network(object):
    """ Physical Description of a Power System """

    #Constructor
    def __init__(self):
        self.Nodes = {}
        self.Stations = {}
        self.Companies = {}
        self.NodeConnectors = {}
        self.CircuitBreakers = {}
        self.Lines = {}
        self.Transformers = {}
        self.PhaseShifters = {}
        self.Devices = {}
        self.Loads = {}
        self.Shunts = {}
        self.Units = {}
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
    def AddNode(self, node: Node):
        if node.ID in self.Nodes:
            raise Exception("Node already exists in the network", node.ID)
        station = self.FindOrAddStation(node.StationID, node.CompanyID, node.DivisionID)
        #Add Node to Network
        self.Nodes[node.ID] = node
        station.AddNode(node)               
        return node

    #Node Connector Methods
    def AddNodeConnector(self, nc: NodeConnector):
        if nc.FromStationID not in self.Stations or nc.ToStationID not in self.Stations:
            raise Exception("From or To Station for node connector does not exit in network", nc.FromStationID, nc.ToStationID)
        self.Stations[nc.FromStationID].AddNodeConnector(nc)
        if nc.FromStationID != nc.ToStationID:
            self.Stations[nc.ToStationID].AddNodeConnector(nc)
        if nc.FromNodeID not in self.Nodes or nc.ToNodeID not in self.Nodes:
            raise Exception("From or To Node for node connector does not exit in network", nc.FromNodeID, nc.ToNodeID)
        if nc.ID in self.NodeConnectors:
            raise Exception("Node Connector already exists in the network", nc.ID)        
        self.Nodes[nc.FromNodeID].AddNodeConnector(nc)
        if nc.FromNodeID != nc.ToNodeID:
            self.Nodes[nc.ToNodeID].AddNodeConnector(nc)
        self.NodeConnectors[nc.ID] = nc
        if isinstance(nc, Transformer):
            if nc.RegulationNodeID in self.Nodes:
                nc.RegulationNode = self.Nodes[nc.RegulationNodeID]
        if type(nc) is PhaseShifter:
            self.PhaseShifters[nc.ID] = nc
        if type(nc) is Transformer:
            self.Transformers[nc.ID] = nc
        if type(nc) is Branch:
            self.Lines[nc.ID] = nc
        if type(nc) is CircuitBreaker:
            self.CircuitBreakers[nc.ID] = nc
        return


    #Device Methods
    def AddDevice(self, d: Device):
        if d.StationID not in self.Stations:
            raise Exception("Station for device does not exit in network", d.StationID)
        self.Stations[d.StationID].AddDevice(d)
        if d.NodeID not in self.Nodes:
            raise Exception("Node for device does not exit in network", d.NodeID)
        if d.ID in self.Devices:
            raise Exception("Device already exists in the network", d.ID)        
        self.Nodes[d.NodeID].AddDevice(d)
        if isinstance(d, Shunt) or isinstance(d, Unit):
            if d.RegulationNodeID in self.Nodes:
                d.RegulationNode = self.Nodes[d.RegulationNodeID]
        self.Devices[d.ID] = d
        if type(d) is Load:
            self.Loads[d.ID] = d
        if type(d) is Shunt:
            self.Shunts[d.ID] = d
        if type(d) is Unit:
            self.Units[d.ID] = d
        return
