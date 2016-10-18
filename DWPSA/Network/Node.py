class Node(object):
    """Physical Location in a Power System"""


    #Constructor
    def __init__(self, stationid, voltage, name, companyid = "", divisionid = ""):
        """Node Constructor"""

        #Attributes
        self.CompanyID = companyid
        self.DivisionID = divisionid
        self.ID = (stationid, voltage, name)
        self.Name = name
        self.Station = None
        self.StationID = stationid
        self.Voltage = voltage

    #Methods
