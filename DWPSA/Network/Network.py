import random
import copy
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
from Network.PNode import PNode
from Network.EPNode import EPNode
from Network.CPNode import CPNode
from Network.MktUnitDailyOffer import MktUnitDailyOffer
from Network.MktUnitHourlyOffer import MktUnitHourlyOffer
from Network.MktUnit import MktUnit

class Network(object):
    """ Physical Description of a Power System """

    #Constructor
    def __init__(self):
        self.Nodes = {}
        self.Stations = {}
        self.Companies = {}
        self.CPNodes = {}
        self.EPNodes = {}
        self.NodeConnectors = {}
        self.CircuitBreakers = {}
        self.Lines = {}
        self.Transformers = {}
        self.PhaseShifters = {}
        self.PNodes = {}
        self.Devices = {}
        self.Loads = {}
        self.Shunts = {}
        self.Units = {}
        self.MktUnits = {}
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

    #PNode Methods
    def AddPNode(self, pn: PNode):
        if pn.ID in self.PNodes:
            raise Exception("PNode is already loaded", pn.Name)
        self.PNodes[pn.ID] = pn
        if type(pn) is CPNode:
            self.CPNodes[pn.ID] = pn
        if type(pn) is EPNode:
            if (pn.NodeID not in self.Nodes):
                raise Exception("PNode does not map to valid Node", pn.Name)
            pn.Node = self.Nodes[pn.NodeID]
            self.EPNodes[pn.ID] = pn
        return
    def AddPNodeFactor(self, cpnid: int, pnid: int, factor: float):
        if cpnid not in self.CPNodes:
            raise Exception("CPNode is not in the Network", cpnid)
        if pnid not in self.PNodes:
            raise Exception("PNode is not in the Network", pnid)
        self.CPNodes[cpnid].AddPnodeFactor(self.PNodes[pnid],factor)
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

#MKTUNIT Methods

    def AddMktUnit(self, mu: MktUnit):
        if mu.ID not in self.MktUnits.keys():
            self.MktUnits[mu.ID] = mu
            if mu.CPNodeID not in self.CPNodes.keys():
                raise Exception("CPNode ID not found in Network", mu.CPNodeID)
            mu.CPNode = self.CPNodes[mu.CPNodeID]
            if len(mu.CPNode.PNodes) > 1:
                mu.IsCombinedCycle = True
                mu.IsCombinedCycleParent = True
                mu.CombinedCycleParent = mu
            else:
                for p in mu.CPNode.PNodes.values():
                    if type(p) is not EPNode:
                        raise Exception("Unexpected PNodes type for Unit CPNode", mu.CPNodeID)               
                    n = p.Node
                    if not mu.EAR:
                        if mu.DRR1:
                            loadid = (n.StationID, p.LoadUnitName, "LD")
                            if loadid not in self.Loads.keys():
                                raise Exception("Mkt Unit device not found in Network", mu.ID)
                            mu.Load = self.Loads[loadid]
                        else:                        
                            unitid = (n.StationID, p.LoadUnitName, "UN")
                            if unitid not in self.Units.keys():
                                raise Exception("Mkt Unit device not found in Network", mu.ID)
                            mu.Unit =  self.Units[unitid]
        return                

    def AddMktUnitDailyOffer(self, udo: MktUnitDailyOffer):
        if udo.UnitID not in self.MktUnits.keys():
            raise Exception("Mkt Unit ID not found in Network", udo.UnitID)
        self.MktUnits[udo.UnitID].AddDailyOffer(udo)
        return
    def AddMktUnitHourlyOffer(self, uho: MktUnitHourlyOffer):
        if uho.UnitID not in self.MktUnits.keys():
            raise Exception("Mkt Unit ID not found in Network", uho.UnitID)
        self.MktUnits[uho.UnitID].AddHourlyOffer(uho)
        return
    def GetRandomStationID(self, internalcompaniesonly: bool = False) ->str:
        sts = self.GetStationIDs(internalcompaniesonly)
        return sts[random.randint(0,len(sts)-1)]

    def GetStationIDs(self, internalcompaniesonly: bool = False) -> []:
        sts = []
        if internalcompaniesonly:
            for st in self.Stations.values():
                if st.Company.EnforceLosses:
                    sts.append(st.ID)
        else:
            sts = list(self.Stations.keys())
        return sts

    def GetRandomCompanyID(self, internalcompaniesonly: bool = False) ->str:
        cps = self.GetCompanyIDs(internalcompaniesonly)
        return cps[random.randint(0,len(cps)-1)]
    def GetCompanyIDs(self, internalcompaniesonly: bool = False) -> []:
        cps = []
        if internalcompaniesonly:
            for cp in self.Companies.values():
                if cp.EnforceLosses:
                    cps.append(cp.ID)
        else:
            cps = list(self.Companies.keys())
        return cps

    def GetDefaultLoadTotal(self):
        load = 0
        for ld in self.Loads.values():
            load += ld.Conforming.real
        return load

    def GetMinMaxGeneration(self)->(float, float):
        min = 0
        max = 0
        for g in self.Units.values():
            min += g.MVAMin.real
            max += g.MVAMax.real
        return (min, max)
    
    def ExapandSelectedStations(self, selectedstations = [], expansiondegree: int = 1, internalcompaniesonly: bool = False) -> []:
        sts = []
        
        for st in selectedstations:
            if st in self.Stations and st not in sts:
                if self.Stations[st].Company.EnforceLosses or not internalcompaniesonly:
                    sts.append(st)
        for i in range(expansiondegree):
            nexttiersts = []
            for st in sts:
                for nc in self.Stations[st].NodeConnectors.values():
                    if nc.FromNode.StationID not in sts and nc.FromNode.StationID not in nexttiersts: 
                        nexttiersts.append(nc.FromNode.StationID) 
                    if nc.ToNode.StationID not in sts and nc.ToNode.StationID not in nexttiersts: 
                        nexttiersts.append(nc.ToNode.StationID) 
            for st in nexttiersts:
                if st in self.Stations:
                    if self.Stations[st].Company.EnforceLosses or not internalcompaniesonly:
                        sts.append(st)
        return sts

    def ExpandSelectedCompanies(self, selectedcompanies = [], expansiondegree: int = 1, internalcompaniesonly: bool = False) -> []:
        '''Takes a list of company names 'selectedcompanies' and adds connected companies by degree provided 'expansiondegree'. 
           Setting 'intenralcompaniesonly' will prevent any company from being returned that is external. 
        '''
        cps = []
        for cp in selectedcompanies:
            if cp in self.Companies and cp not in cps:
                if self.Companies[cp].EnforceLosses or not internalcompaniesonly:
                    cps.append(cp)
 
        for i in range(expansiondegree):
            nexttiercps = []
            for cp in cps:
                for st in self.Companies[cp].Stations:
                    for nc in self.Stations[st].NodeConnectors.values():
                        if nc.FromNode.CompanyID not in cps and nc.FromNode.CompanyID not in nexttiercps: 
                            nexttiercps.append(nc.FromNode.CompanyID) 
                        if nc.ToNode.CompanyID not in cps and nc.ToNode.CompanyID not in nexttiercps: 
                            nexttiercps.append(nc.ToNode.CompanyID) 
            for cp in nexttiercps:
                if cp in self.Companies:
                    if self.Companies[cp].EnforceLosses or not internalcompaniesonly:
                        cps.append(cp)
        return cps         

    def CreateSubNetwork(self, companies = [], stations=[], kvs = []):
        '''
        'companies' is array of Company names to include in the subsytem - default is all companies
        'stations' is array of Station names to include in the subsystem - default is all stations in selected 'companies'
        'kvs' is array of KV levels to include in the subsystem - default is all
        '''
        #Create new network
        n = Network()
        #Company
        if len(companies) == 0:
            #Add All Companies When none are selected
            for cp in self.Companies.values():
                n.AddCompany(cp.Copy())
        else:
            #Add selected Companies
            for cp in companies:
                if cp in self.Companies:
                    n.AddCompany(self.Companies[cp].Copy())
        #Division
        for cp in n.Companies.keys():
            for dv in self.Companies[cp].Divisions.values():
                n.AddDivision(dv.Copy())

        #Station
        if len(stations) == 0:
            for st in self.Stations.values():
                if st.CompanyID in n.Companies:
                    n.AddStation(st.Copy())
        else:
            for st in stations:
                if st in self.Stations:
                    if self.Stations[st].CompanyID in n.Companies:
                        n.AddStation(self.Stations[st].Copy())
            
        #Node
        for nd in self.Nodes.values():
            if nd.StationID in n.Stations:
                n.AddNode(nd.Copy())

        #NodeConnector
        for nc in self.NodeConnectors.values():
            if nc.FromNodeID in n.Nodes and nc.ToNodeID in n.Nodes:
                #stupid code to prevent infinite recursion on deep copy
                FromNode = nc.FromNode
                ToNode = nc.ToNode
                nc.FromNode = nc.ToNode = None
                rNode = None
                if hasattr(nc, 'RegulationNode'):
                    rNode = nc.RegulationNode
                    nc.RegulationNode = None
                n.AddNodeConnector(copy.deepcopy(nc))
                nc.FromNode = FromNode
                nc.ToNode = ToNode
                if hasattr(nc, 'RegulationNode'):
                    nc.RegulationNode = rNode

        #Device
        for d in self.Devices.values():
            if d.NodeID in n.Nodes:
                #stupid code to prevent infinite recursion on deep copy
                dNode = d.Node
                rNode = None
                if hasattr(d, 'RegulationNode'):
                    rNode = d.RegulationNode
                    d.RegulationNode = None
                d.Node = None
                n.AddDevice(copy.deepcopy(d))
                d.Node = dNode
                if hasattr(d, 'RegulationNode'):
                    d.RegulationNode = rNode
        return n