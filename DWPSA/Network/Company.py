class Company(object):
    """Owner of Network Assets"""

    def __init__(self, companyid, enforcelosses = True, awr = True):
        #Properties
        self.AWR = awr
        self.Divisions = {}
        self.EnforceLosses = enforcelosses
        self.ID = companyid
        self.Stations = {}
        return

    def AddDivision(self, division):
        if division.ID in self.Divisions:
            raise Exception("Division already exists in the company", division.ID)
        self.Divisions[division.ID] = division
        division.Company = self
        division.CompanyID = self.ID

    def AddStation(self, station):
        if station.ID in self.Stations:
            raise Exception("Station already exists in the company", station.ID)
        self.Stations[station.ID] = station
        station.Company = self
        station.CompanyID = self.ID

    def Copy(self):
        '''Deep Copy including all non collection based properties'''
        return Company(self.ID, self.EnforceLosses, self.AWR)
        