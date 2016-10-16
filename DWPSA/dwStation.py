import dwNode

class Station(object):
    """Physical Location containing a Node or Nodes"""

    #Constructor
    def __init__(self, name):
        self.Nodes = {}
        self.ID = name

    #Methods
    def AddNode(self, node):
        self.Nodes[node.ID] = node
        node.Station = self
