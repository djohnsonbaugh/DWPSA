from dem.network import Terminal
from dem.network import Device
class VirtualNet(Device):
    """Distributes MW from terminal[0] to other terminals by defined factors"""


    def __init__(self, vterminals: [float], name=None):
        super(VirtualNet, self).__init__(terminals=[Terminal()], name=name)

        self.vterminals = []
        self.nterminals = []
        for t in self.terminals:
            self.nterminals.append(t)
        for f in vterminals:
            vt = Terminal()
            self.terminals.append(vt)
            self.vterminals.append((vt,f))

    ##@property
    #def cost(self):
        

    @property
    def constraints(self):
        cons = []
        #cons += [sum(t.power_var for t in self.terminals) == 0]
        for vt, f in self.vterminals:
            cons.append(sum(t.power_var for t in self.nterminals) * f + vt.power_var == 0)
        return  cons

    def addvterm(self, terminal: Terminal, factor: float):
        self.vterminals.append((terminal, factor))
        self.terminals.append(terminal)