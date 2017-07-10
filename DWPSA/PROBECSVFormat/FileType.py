from enum import Enum
class FileType(Enum):
    """PROBE CSV File Types"""
    DayAheadLMPs = 1
    ZonalFactors = 2
    BidData = 3
    CostCurves = 4
    DemandBids = 5

