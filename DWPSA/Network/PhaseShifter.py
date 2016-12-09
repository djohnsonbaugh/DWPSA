from Network.Transformer import Transformer
from Network.RatingSet import RatingSet

class PhaseShifter(Transformer):
    """Phase Shifter Transformer Branch Node Connector"""


    def __init__(self, stationid: str, fvoltage: str, fnodename: str, 
                 tvoltage: str, tnodename: str,
                 name: str, owner: str,
                 r: float = 0, x: float = 0, 
                 summer : RatingSet = None, winter : RatingSet = None,
                 spring : RatingSet = None, fall : RatingSet = None,
                 ftaptype: str = "", fnormtapposition: int = 0, 
                 ttaptype: str = "", tnormtapposition: int = 0, regnodename : str = "", avr: int = 0,
                 ptaptype: str = "", awr: bool = False ):

        super(PhaseShifter, self).__init__(stationid, fvoltage, fnodename, tvoltage, tnodename,
                                           name, owner, False, r, x, 
                                           summer, winter, spring, fall,
                                           ftaptype, fnormtapposition, ttaptype, tnormtapposition, regnodename, avr)

        self.PhaseTapType = ptaptype
        self.AWRStatus = awr