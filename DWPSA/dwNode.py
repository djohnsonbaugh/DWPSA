import dwStation
import unittest


class Node(object):
    """Physical Location in a Power System"""


    #Constructor
    def __init__(self, stationid, voltage, name, company = "None"):
        """Node Constructor"""

        #Attributes
        self.StationID = stationid
        self.Voltage = voltage
        self.Name = name
        self.Company = company

        self.ID = (self.StationID, self.Voltage, self.Name)
        self.Station = dwStation.Station("Unknown")

    #Methods
