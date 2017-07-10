from Network.Network import Network
from Network.Branch import Branch
from Network.Station import Station
from Network.Unit import Unit
from Network.Load import Load
from dem.network import Group
from dem.network import Device
from dem.network import Net
from dem.devices import TransmissionLine
from dem.devices import Generator
from dem.devices import FixedLoad
from dem.network import Terminal
from Network.CPNode import CPNode
from Network.EPNode import EPNode
from Network.PNode import PNode
from Network.MktBid import *
import io
import math
from datetime import date
from datetime import datetime
from demdwext.VirtualNet import VirtualNet
from demdwext.GeneratorWithBidCurve import GeneratorWithBidCurve
from demdwext.LoadWithBidCurve import LoadWithBidCurve

class GroupDefinition(object):
    def __init__(self, name: str):
        self.Name = name
        self.Devices = []
        self.DevLabels = []
        self.DevTerminals = []
        self.DevTermLabels = []
        self.GroupTerminals = []
        self.GroupTermLabels = []

    @property
    def DeviceCount(self):
        return len(self.Devices)
    def AddDevice(self, dev: Device, label: str):
        self.Devices.append(dev)
        self.DevLabels.append(label)

    def AddDeviceTerminal(self, term: Terminal, label: str):
        self.DevTerminals.append(term)
        self.DevTermLabels.append(label)

    def AddGroupTerminal(self, term: Terminal, label: str):
        self.GroupTerminals.append(term)
        self.GroupTermLabels.append(label)

    def CreateGroup(self) -> Group:
        return Group(self.Devices, [Net(self.DevTerminals, self.Name)], self.GroupTerminals, self.Name)

    def CreateCode(self) -> str:
        groupstr = ""
        groupstr += "Nt_{0} = Net([".format(self.Name)
        for i in range (0 , len(self.DevTermLabels)):
            if i != 0: groupstr += ","
            groupstr += "\n                    {0}".format(self.DevTermLabels[i])
        groupstr += "\n                    ],\"{0}\")\n".format(self.Name)
        groupstr += "Gp_{0} = Group([".format(self.Name)
        for i in range (0 , len(self.DevLabels)):
            if i != 0: groupstr += ","
            groupstr += "\n                    {0}".format(self.DevLabels[i])
        groupstr += "\n                    ],"
        groupstr += "\n                    [Nt_{0}],".format(self.Name)
        groupstr += "\n                    ["
        for i in range (0 , len(self.GroupTermLabels)):
            if i != 0: groupstr += ","
            groupstr += "\n                    {0}".format(self.GroupTermLabels[i])
        groupstr += "\n                    ],"
        groupstr += "\n                    \"Gp_{0}\"".format(self.Name)
        groupstr += "\n                    )\n"
        return groupstr

def CreateGroupFromCPNode(cpn: CPNode, ENodeTerms, mktday, bidmkthour, fixedloadscale, fixfactors = True, fixedloadmkthours=[]) -> (Group , str, VirtualNet):
    """Creates a dem Group from a CPNode definition and a python script to create the group"""
    factorscale = cpn.FactorSum if fixfactors else 1
    if len(fixedloadmkthours) == 0: fixedloadmkthours.append(bidmkthour)
    if factorscale == 0: factorscale = 1
    groupstr = "#Loading CPNode: {0}\n".format(cpn.Name)
    gpd = GroupDefinition(cpn.GetVariableName())
    vnet = VirtualNet([], "vnet_{0}".format(cpn.GetVariableName()))
    gpd.AddDevice(vnet, vnet.name)
    gpd.AddDeviceTerminal(vnet.terminals[0], "{0}.terminals[0]".format(vnet.name))
    groupstr = ("{0} = VirtualNet([".format(vnet.name))
    i = 0
    for pnode in cpn.PNodes.values():
        pn = pnode
        factor = cpn.PNodeFactors[pn.ID]/factorscale
        if type(pn) is CPNode:
            if len(pn.PNodes) == 1:
                for subpnode in cpn.PNodes.values():
                    pn = subpnode
        if type(pn) is EPNode:
            i+=1
            vnet.addvterm(Terminal(), factor)
            if pn.Node.Station.ID not in ENodeTerms: ENodeTerms[pn.Node.Station.ID] = {}
            ENodeTerms[pn.Node.Station.ID][cpn.ID] = i
            gpd.AddGroupTerminal(vnet.terminals[i], "{0}.terminals[{1}]".format(vnet.name, i))
            if i > 1: groupstr += ","
            groupstr += "\n                    {0}".format(factor)
        else:
            raise Exception("Unhandled CPNode")
    groupstr += "\n                    ],\"{0}\")\n".format(vnet.name)                             
    for mu in cpn.MktUnits.values():
        if mu.UnitType.find("DRR") < 0 and mu.UnitType != "EAR":
            g = GeneratorWithBidCurve(no_load_cost=mu.HourlyOffers[bidmkthour].NoLoadCost, 
                                        power_min=0,#power_min=mu.HourlyOffers[bidmkthour].EcoMin,
                                        power_max=mu.HourlyOffers[bidmkthour].EcoMax,
                                        bid_curve=mu.HourlyOffers[bidmkthour].OfferCurve.ToArray(), 
                                        name= str(mu))
            groupstr += "{0} = GeneratorWithBidCurve(no_load_cost={1}, power_min={2}, power_max={3}, bid_curve={4}, name=\"{5}\")\n".format(
                mu.GetVariableName(), 
                mu.HourlyOffers[bidmkthour].NoLoadCost,
                0,#mu.HourlyOffers[bidmkthour].EcoMin,
                mu.HourlyOffers[bidmkthour].EcoMax, 
                str(mu.HourlyOffers[bidmkthour].OfferCurve.ToArray()), 
                str(mu))
            gpd.AddDevice(g, mu.GetVariableName())
            gpd.AddDeviceTerminal(g.terminals[0], "{0}.terminals[0]".format(mu.GetVariableName()))

    for mb in cpn.MktBids.values():
        if bidmkthour in mb.BidCurves:
            varname = mb.GetVariableName()
            mktbid = None
            if mb.BidType == MktBidType.FixedDemand:
                fixedload = []
                for mkh in fixedloadmkthours:
                    if mkh in mb.FixedLoad:
                        fixedload.append(mb.FixedLoad[mkh]* fixedloadscale * factorscale)
                    else: fixedload.append(0)
                mktbid = FixedLoad(fixedload, varname)
                groupstr += "{0} = FixedLoad(power={1}, name=\"{2}\")\n".format(
                    varname, str(fixedload), varname)
            elif mb.BidType == MktBidType.Increment:
                mktbid = GeneratorWithBidCurve(no_load_cost=0, 
                                            power_min=0,#mu.HourlyOffers[mkthour].EcoMin,
                                            power_max=mb.BidCurves[bidmkthour].MaxMW,
                                            bid_curve=mb.BidCurves[bidmkthour].ToArray(), 
                                            name= varname)
                groupstr += "{0} = GeneratorWithBidCurve(no_load_cost={1}, power_min={2}, power_max={3}, bid_curve={4}, name=\"{5}\")\n".format(
                varname, 
                0,
                0,#mu.HourlyOffers[mkthour].EcoMin,
                mb.BidCurves[bidmkthour].MaxMW, 
                str(mb.BidCurves[bidmkthour].ToArray()), 
                varname)

            elif mb.BidType == MktBidType.Decrement or mb.BidType == MktBidType.PriceSensitiveDemand:
                mktbid = LoadWithBidCurve(power_max=mb.BidCurves[bidmkthour].MaxMW,
                                          bid_curve=mb.BidCurves[bidmkthour].ToArray(sortincreasing=False), 
                                          name= varname)
                groupstr += "{0} = LoadWithBidCurve(power_max={1}, bid_curve={2}, name=\"{3}\")\n".format(
                varname, 
                mb.BidCurves[bidmkthour].MaxMW, 
                str(mb.BidCurves[bidmkthour].ToArray(sortincreasing=False)), 
                varname)
            if mktbid != None:
                gpd.AddDevice(mktbid, varname)
                gpd.AddDeviceTerminal(mktbid.terminals[0], "{0}.terminals[0]".format(varname))

    groupstr += gpd.CreateCode()
    return (gpd.CreateGroup() , groupstr, vnet)

def NetworkToDEMSimple(net : Network, companies = [], stations = [], mktday = date.today(), bidmkthour= datetime.now(), codefile = "testdem.py", fixedloadscale = 1.0, fixedloadmkthours=[]) -> Group:
    """Reduces all Stations to 1 Node,
       Lines are the only Node Connector Exported,
       Unmonitored Line limits set to 99999,
       Monitored Line limits set to Winter Emergency and converted to 765kV
       Unit Minimum is 0
       """
    if len(fixedloadmkthours) == 0: fixedloadmkthours.append(bidmkthour)
    defalpha = 10
    defbeta = 20
    AllCom = (len(companies) == 0)
    AllSt = (len(stations) == 0)
    #Define all Transmission Lines
    Stations = []
    StCode = []
    TLs = {}
    EnodeTerms = {}
    CPNodeVnets = {}
    tr = Branch("","","","","","","","",False)
    st = Station("")

    with open(codefile, 'w') as file:
        file.write("#Stations: {0}\n".format(len(net.Stations)))
        file.write("#Lines: {0}\n".format(len(net.Lines)))
        file.write("#MktBids: {0}\n".format(len(net.MktBids)))
        file.write("#Generators: {0}\n".format(len(net.MktUnits)))
        file.write("#Total Load: {0}\n".format(round(net.GetDefaultLoadTotal() * fixedloadscale)))
        file.write("#Load Scale: {0}\n".format(round(fixedloadscale,2)))
        file.write("#Min, Max Gen: {0}, {1} \n".format(str(round(net.GetMinMaxGeneration()[0])),str(round(net.GetMinMaxGeneration()[1]))))

        file.write("from dem import * \n")
        file.write("from demdwext.VirtualNet import * \n")
        file.write("from demdwext.GeneratorWithBidCurve import * \n")
        file.write("from demdwext.LoadWithBidCurve import * \n")
        file.write(" \n")


        for cpn in net.CPNodes.values():
            cpngroup, cpnstr, vnet = CreateGroupFromCPNode(cpn, EnodeTerms, mktday, bidmkthour, fixedloadscale, True, fixedloadmkthours)
            if len(cpngroup.devices) > 1:
                CPNodeVnets[cpn.ID] = vnet
                Stations.append(cpngroup)
                StCode.append("Gp_" + cpn.GetVariableName())
                file.write(cpnstr)
        file.write("#Loading Transmission Lines\n")
        for tr in net.Lines.values():
            if (tr.FromStationID in stations and tr.ToStationID in stations) or AllSt:
                if (tr.FromNode.CompanyID in companies and tr.ToNode.CompanyID in companies) or AllCom:
                    if tr.FromStationID != tr.ToStationID:
                        limit = int(tr.WiRating.Emergency * (765 / float(tr.FromVoltage)))
                        if not tr.Monitored:
                            TLs[tr.ID] = TransmissionLine(name=str(tr))
                            file.write("{0} = TransmissionLine(name=\"{1}\")\n".format(
                                       tr.GetVariableName(), str(tr)))
                        else:
                            TLs[tr.ID] = TransmissionLine(limit, str(tr))
                            file.write("{0} = TransmissionLine(power_max={1}, name=\"{2}\")\n".format(
                                       tr.GetVariableName(), limit, str(tr)))

        for st in net.Stations.values():
            brcount = 0
            if (st.CompanyID in companies or AllCom) and (st.ID in stations or AllSt):
                file.write(" \n")
                file.write("#Loading Station: {0}\n".format(st.ID))
                gpd = GroupDefinition(st.GetVariableName())
                if st.ID in EnodeTerms:
                    for cid in EnodeTerms[st.ID].keys():
                        if cid in CPNodeVnets:
                            ind = EnodeTerms[st.ID][cid]
                            vnet = CPNodeVnets[cid]
                            gpd.AddDeviceTerminal(vnet.terminals[ind], "{0}.terminals[{1}]".format(vnet.name, ind))                     
                for tr in st.NodeConnectors.values():
                    if type(tr) is Branch:
                        if (tr.FromStationID in stations and tr.ToStationID in stations) or AllSt:
                            if (tr.FromNode.CompanyID in companies and tr.ToNode.CompanyID in companies) or AllCom:
                                if tr.FromStationID != tr.ToStationID:
                                    brcount +=1
                                    if tr.FromStationID == st.ID:
                                        gpd.AddDeviceTerminal(TLs[tr.ID].terminals[0], "{0}.terminals[0]".format(tr.GetVariableName()))
                                        gpd.AddGroupTerminal(TLs[tr.ID].terminals[1],"{0}.terminals[1]".format(tr.GetVariableName()))
                                        gpd.AddDevice(TLs[tr.ID], tr.GetVariableName())
                                    else:
                                        gpd.AddDeviceTerminal(TLs[tr.ID].terminals[1], "{0}.terminals[1]".format(tr.GetVariableName()))                                
                #for d in st.Devices.values():
                #    usemktunit = False
                #    if d.MktUnit != None: usemktunit = True
                #    if not usemktunit:
                #        device = None
                #        if type(d) is Unit:
                #            device = Generator(power_min=0, power_max=d.MVAMax.real, alpha=defalpha, beta=defbeta, name=str(d))
                #            file.write("{0} = Generator(power_min={1}, power_max={2}, alpha={3}, beta={4}, name=\"{5}\")\n".format(
                #                d.GetVariableName(), 0, d.MVAMax.real, defalpha, defbeta, str(d)))
                #        if type(d) is Load:
                #            device = FixedLoad(d.Conforming.real * fixedloadscale, str(d))
                #            file.write("{0} = FixedLoad(power={1}, name=\"{2}\")\n".format(
                #                d.GetVariableName(), d.Conforming.real * fixedloadscale, str(d)))
                #        if device != None:    
                #            gpd.AddDevice(device, d.GetVariableName())
                #            gpd.AddDeviceTerminal(device.terminals[0], "{0}.terminals[0]".format(d.GetVariableName()))
                if brcount > 0:
                    file.write(gpd.CreateCode())
                    Stations.append(gpd.CreateGroup())
                    StCode.append("Gp_" + st.GetVariableName())
        file.write("#Creating Final Network Group\n")
        file.write("network = Group([".format(st.ID))
        for i in range (0 , len(StCode)):
            if i != 0:
                file.write(",")
            file.write("\n                    {0}".format(StCode[i]))
        file.write("\n                    ],[])\n")
        

        file.write("#Solve Problem\n")
        file.write("network.init_problem(time_horizon={0})\n".format(len(fixedloadmkthours)))
        file.write("network.problem.solve()\n")
        file.write("print(network.results.summary())\n") 
    return Group(Stations, [])



