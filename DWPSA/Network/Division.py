from Network.Station import Station

class Division(object):
    """Division of an Owner of Network Assets"""

    def __init__(self, divisionid, companyid):
        #Properties
        self.Company = None
        self.CompanyID = companyid
        self.ID = divisionid
        self.Stations = {}
        return


    def AddStation(self, station):
        if station.ID in self.Stations:
            raise Exception("Station already exists in the company", station.ID)
        self.Stations[station.ID] = station
        station.Division = self
        station.DivisionID = self.ID
        

