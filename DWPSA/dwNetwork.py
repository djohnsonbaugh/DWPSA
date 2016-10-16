from dwNode import Node
from dwStation import Station

class Network(object):
    """ Physical Description of a Power System """

    #Constructor
    def __init__(self):
        self.Nodes = {}
        self.Stations = {}
        return
    #Methods
    def AddNode(self, node, createstations = True):
        """
        Adds a Node to the Network
            node:               Node to be added
            createstations:     Will create a station if it does not already exist
        """

        if node.ID in self.Nodes:
            raise Exception("Node already exists in the network", node.ID)

        #Add Node to Network
        self.Nodes[node.ID] = node
        
        #Verify Station exists or possibly create it
        if node.StationID not in self.Stations:
            if not createstations:
                return
            else:
                self.AddStation(Station(node.StationID), True)

        #Add Node to Station
        self.Stations[node.StationID].AddNode(node)
        return

    def AddStation(self, station, linknodes = True):
        """
        Adds a Station to the Network
            Station station:       Station to be added
            bool    linknodes:     Will add existing nodes to this station if they have the same stationid
        """
        if station.ID in self.Stations:
            raise Exception("Station already exists in the network", station.ID)

        #Link existing nodes with this station id?
        if linknodes:
            for n in self.Nodes.values():
                if n.StationID == station.ID:
                    station.AddNode(n)
        #Add Station to the Network
        self.Stations[station.ID] = station
        return


