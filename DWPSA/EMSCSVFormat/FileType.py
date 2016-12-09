from enum import Enum
class FileType(Enum):
    """EMS CSV File Types"""
    Company = 1
    Division = 2
    Station = 3
    Node = 4
    CircuitBreaker = 5
    Line = 6
    Transformer = 7
    PhaseShifter = 8

