from Network.Network import Network
from Network.Branch import Branch
from Network.Station import Station
from Network.Unit import Unit
from Network.Load import Load
from dem.network import Group
from dem.network import Net
from dem.devices import TransmissionLine
from dem.devices import Generator
from dem.devices import FixedLoad
import io
import math

def NetworkToDEMSimple(net : Network, companies = [], stations = [], codefile = "testdem.py") -> Group:
    """Reduces all Stations to 1 Node,
       Lines are the only Node Connector Exported,
       Unmonitored Line limits set to 99999,
       Monitored Line limits set to Winter Emergency"""
    defalpha = 0
    defbeta = 0
    AllCom = (len(companies) == 0)
    AllSt = (len(stations) == 0)
    #Define all Transmission Lines
    Stations = []
    StCode = []
    TLs = {}
    tr = Branch("","","","","","","","",False)
    st = Station("")

    with open(codefile, 'w') as file:
        file.write("from dem import * \n")
        file.write(" \n")
        file.write("#Loading Transmission Lines\n".format(st.ID))
        for tr in net.Lines.values():
            if (tr.FromStationID in stations and tr.ToStationID in stations) or AllSt:
                if (tr.FromNode.CompanyID in companies and tr.ToNode.CompanyID in companies) or AllCom:
                    if tr.FromStationID != tr.ToStationID:
                        limit = int(tr.WiRating.Emergency * (765 / float(tr.FromVoltage)))
                        if not tr.Monitored:
                            limit = 99999
                        TLs[tr.ID] = TransmissionLine(limit, str(tr))
                        file.write("Tr_{0}__{1}__{2} = TransmissionLine(power_max={3}, name=\"{4}\")\n".format(
                                   tr.ID[0], tr.ID[1], tr.ID[2], limit, str(tr)))

        for st in net.Stations.values():
            brcount = 0
            if (st.CompanyID in companies or AllCom) and (st.ID in stations or AllSt):
                file.write(" \n")
                file.write("#Loading Station: {0}\n".format(st.ID))
                Devices = []
                GroupTerminals = []
                DeviceTerminals = []
                DeviceCode = []
                GTCode = []
                DTCode = []
                for tr in st.NodeConnectors.values():
                    if type(tr) is Branch:
                        if (tr.FromStationID in stations and tr.ToStationID in stations) or AllSt:
                            if (tr.FromNode.CompanyID in companies and tr.ToNode.CompanyID in companies) or AllCom:
                                if tr.FromStationID != tr.ToStationID:
                                    brcount +=1
                                    if tr.FromStationID == st.ID:
                                        DeviceTerminals.append(TLs[tr.ID].terminals[0])
                                        DTCode.append("Tr_{0}__{1}__{2}.terminals[0]".format(
                                            tr.ID[0], tr.ID[1], tr.ID[2]))
                                        GroupTerminals.append(TLs[tr.ID].terminals[1])
                                        GTCode.append("Tr_{0}__{1}__{2}.terminals[1]".format(
                                            tr.ID[0], tr.ID[1], tr.ID[2]))
                                        Devices.append(TLs[tr.ID])
                                        DeviceCode.append("Tr_{0}__{1}__{2}".format(
                                            tr.ID[0], tr.ID[1], tr.ID[2]))
                                    else:
                                        DeviceTerminals.append(TLs[tr.ID].terminals[1])
                                        DTCode.append("Tr_{0}__{1}__{2}.terminals[1]".format(
                                            tr.ID[0], tr.ID[1], tr.ID[2]))
                                
                for d in st.Devices.values():
                    if type(d) is Unit:
                        g = Generator(power_min=d.MVAMin.real, power_max=d.MVAMax.real, alpha=defalpha, beta=defbeta, name=str(d))
                        file.write("Un_{0}__{1}__{2} = Generator(power_min={3}, power_max={4}, alpha={5}, beta={6}, name=\"{7}\")\n".format(
                            d.ID[0], d.ID[1], d.ID[2], d.MVAMin.real, d.MVAMax.real, defalpha, defbeta, str(d)))    
                        Devices.append(g)
                        DeviceCode.append("Un_{0}__{1}__{2}".format(
                            d.ID[0], d.ID[1], d.ID[2]))
                        DeviceTerminals.append(g.terminals[0])
                        DTCode.append("Un_{0}__{1}__{2}.terminals[0]".format(
                            d.ID[0], d.ID[1], d.ID[2]))
                    if type(d) is Load:
                        fl = FixedLoad(d.Conforming.real, str(d))
                        file.write("Ld_{0}__{1}__{2} = FixedLoad(power={3}, name=\"{4}\")\n".format(
                            d.ID[0], d.ID[1], d.ID[2], d.Conforming.real, str(d)))    
                        Devices.append(fl)
                        DeviceCode.append("Ld_{0}__{1}__{2}".format(
                            d.ID[0], d.ID[1], d.ID[2]))
                        DeviceTerminals.append(fl.terminals[0])
                        DTCode.append("Ld_{0}__{1}__{2}.terminals[0]".format(
                            d.ID[0], d.ID[1], d.ID[2]))
                if brcount > 0:
                    file.write("Nt_{0} = Net([".format(st.ID))
                    for i in range (0 , len(DTCode)):
                        if i != 0:
                            file.write(",")
                        file.write("\n                    {0}".format(DTCode[i]))
                    file.write("\n                    ],\"{0}\")\n".format(st.ID))
                    file.write("Gp_{0} = Group([".format(st.ID))
                    for i in range (0 , len(DeviceCode)):
                        if i != 0:
                            file.write(",")
                        file.write("\n                    {0}".format(DeviceCode[i]))
                    file.write("\n                    ],")
                    file.write("\n                    [Nt_{0}],".format(st.ID))
                    file.write("\n                    [")
                    for i in range (0 , len(GTCode)):
                        if i != 0:
                            file.write(",")
                        file.write("\n                    {0}".format(GTCode[i]))
                    file.write("\n                    ],")
                    file.write("\n                    \"Gp_{0}\"".format(st.ID))
                    file.write("\n                    )\n")

                    
                    Stations.append(Group(Devices, [Net(DeviceTerminals, st.ID)], GroupTerminals, st.ID))
                    StCode.append("Gp_{0}".format(st.ID))
        file.write("#Creating Final Network Group\n")
        file.write("network = Group([".format(st.ID))
        for i in range (0 , len(StCode)):
            if i != 0:
                file.write(",")
            file.write("\n                    {0}".format(StCode[i]))
        file.write("\n                    ],[])\n")
        

        file.write("#Solve Problem\n")
        file.write("network.init_problem()\n")
        file.write("network.problem.solve()\n")
        file.write("print(network.results.summary())\n") 
    return Group(Stations, [])
