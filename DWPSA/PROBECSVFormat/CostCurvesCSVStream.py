from CSVFileStream.CSVFileStream import CSVFileStream
from datetime import datetime
from Network.BidOfferCurve import BidOfferCurve
from Network.UnitHourlyOffer import UnitHourlyOffer

class CostCurvesCSVStream(CSVFileStream):
    """Streams PROBE PNode Properties With Data Conversions"""
    DefaultPropertyToFileMap = {
                                "UNITSCHEDULEID" : "UnitScheduleID",
                                "EFFECTIVEHOUR" : "MktHour",
                                "ECONOMICMIN" : "EcoMin",
                                "ECONOMICMAX" : "EcoMax",
                                "REGMIN" : "RegMin",
                                "REGMAX" : "RegMax",
                                "NOLOADCOST" : "NoLoadCost",
                                "MW1" : "MW1",
                                "PRICE1" : "Price1",                              
                                "MW2" : "MW2",
                                "PRICE2" : "Price2",                              
                                "MW3" : "MW3",
                                "PRICE3" : "Price3",                              
                                "MW4" : "MW4",
                                "PRICE4" : "Price4",                              
                                "MW5" : "MW5",
                                "PRICE5" : "Price5",                              
                                "MW6" : "MW6",
                                "PRICE6" : "Price6",                              
                                "MW7" : "MW7",
                                "PRICE7" : "Price7",                              
                                "MW8" : "MW8",
                                "PRICE8" : "Price8",                              
                                "MW9" : "MW9",
                                "PRICE9" : "Price9",                              
                                "MW10" : "MW10",
                                "PRICE10" : "Price10",                              
                                "MW11" : "MW11",
                                "PRICE11" : "Price11",
                                "COLDNOTIFICATIONTIME" : "ColdNotificationTime",
                                "INTERNOTIFICATIONTIME" : "InterNotificationTime",
                                "HOTNOTIFICATIONTIME" : "HotNotificationTime",
                                "COLDSTARTUPTIME" : "ColdStartupTime",
                                "INTERSTARTUPTIME" : "InterStartupTime",
                                "HOTSTARTUPTIME" : "HotStartupTime",
                                "COMMITSTATUS" : "CommitStatus",
                                "ENGSTATUS" : "EnergyStatus",
                                "REGSTATUS" : "RegStatus",
                                "SPINSTATUS" : "SpinStatus",
                                "SUPPONSTATUS" : "SuppOnStatus",
                                "SUPPOFFSTATUS" : "SuppOffStatus",
                                "REGPRICE" : "RegPrice",
                                "REGMILEAGEPRICE" : "RegMileagePrice",
                                "SPINPRICE" : "SpinPrice",
                                "SUPPONPRICE" : "SuppOnPrice",
                                "SUPPOFFPRICE" : "SuppOffPrice",
                                "REGSELFMW" : "RegSelfMW",
                                "SPINSELFMW" : "SpinSelfMW",
                                "SUPPONSELFMW" : "SuppOnSelfMW",
                                "ENSELFMW" : "EnergySelfMW",
                                "RAMPRATE" : "RampRate",
                                "USEBIDSLOPE" : "UseBidSlope",
                                "SUPPOFFMAXMW" : "SuppOffMaxMW",
                                "RAMPCAPSTATUS" : "RampCapStatus",
                                "EMERGENCYMAX" : "EmerMax",
                                "EMERGENCYMIN" : "EmerMin"
                                }
    DefaultFileName = "cost_curves_{:%Y%m%d}.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(CostCurvesCSVStream, self).__init__(filepath, propertytofilemap, encoding)      

        self.ColdNotificationTime = ""
        self.ColdStartupTime = ""
        self.CommitStatus = ""
        self.EcoMax = ""
        self.EcoMin = ""
        self.EmerMax = ""
        self.EmerMin = ""
        self.EnergySelfMW = ""
        self.EnergyStatus = ""
        self.HotNotificationTime = ""
        self.HotStartupTime = ""
        self.InterNotificationTime = ""
        self.InterStartupTime = ""
        self.MktHour = ""
        self.MW1 = ""
        self.MW2 = ""
        self.MW3 = ""
        self.MW4 = ""
        self.MW5 = ""
        self.MW6 = ""
        self.MW7 = ""
        self.MW8 = ""
        self.MW9 = ""
        self.MW10 = ""
        self.MW11 = ""
        self.NoLoadCost = ""
        self.Price1 = ""                              
        self.Price2 = ""                              
        self.Price3 = ""                              
        self.Price4 = ""                              
        self.Price5 = ""                              
        self.Price6 = ""                              
        self.Price7 = ""                              
        self.Price8 = ""                              
        self.Price9 = ""                              
        self.Price10 = ""                              
        self.Price11 = ""
        self.RampCapStatus = ""
        self.RampRate = ""
        self.RegMax = ""
        self.RegMin = ""
        self.RegMileagePrice = ""
        self.RegPrice = ""
        self.RegSelfMW = ""
        self.RegStatus = ""
        self.SpinPrice = ""
        self.SpinSelfMW = ""
        self.SpinStatus = ""
        self.SuppOnPrice = ""
        self.SuppOnSelfMW = ""
        self.SuppOnStatus = ""
        self.SuppOffMaxMW = ""
        self.SuppOffPrice = ""
        self.SuppOffStatus = ""
        self.UnitScheduleID = ""
        self.UseBidSlope = ""
        return

    def getBidOfferCurve(self) -> BidOfferCurve:
        boc = BidOfferCurve()
        for i in range(1 , 11):  
            price = self.__getattribute__("Price{0}".format(i))
            mw = self.__getattribute__("MW{0}".format(i))
            if price == "" or mw == "": break
            try:
                boc.AddPoint(float(price),float(mw))
            except:
                raise Exception("Invalid Bid or Offer Data provided for Point", i)
        return boc

    def getColdNotificationTime(self) -> float:
        try:
            return float(self.ColdNotificationTime)
        except:
            return 0
    def getColdStartupTime(self) -> float:
        try:
            return float(self.ColdStartupTime)
        except:
            return 0
    def getCommitStatus(self) -> str:
        return self.CommitStatus
    def getEcoMax(self) -> float:
        try:
            return float(self.EcoMax)
        except:
            return 0
    def getEcoMin(self) -> float:
        try:
            return float(self.EcoMin)
        except:
            return 0
    def getEmerMax(self) -> float:
        try:
            return float(self.EmerMax)
        except:
            return 0
    def getEmerMin(self) -> float:
        try:
            return float(self.EmerMin)
        except:
            return 0
    def getEnergySelfMW(self) -> float:
        try:
            return float(self.EnergySelfMW)
        except:
            return 0
    def getEnergyStatus(self) -> str:
        return self.EnergyStatus
    def getHotNotificationTime(self) -> float:
        try:
            return float(self.HotNotificationTime)
        except:
            return 0
    def getHotStartupTime(self) -> float:
        try:
            return float(self.HotStartupTime)
        except:
            return 0
    def getInterNotificationTime(self) -> float:
        try:
            return float(self.InterNotificationTime)
        except:
            return 0
    def getInterStartupTime(self) -> float:
        try:
            return float(self.InterStartupTime)
        except:
            return 0
    def getMktHour(self) -> datetime:
        try: #12/22/2016 0:00
            return datetime.strptime(self.MktHour, "%m/%d/%Y %H:%M")
        except:
            return datetime.today()
    def getNoLoadCost(self) -> float:
        try:
            return float(self.NoLoadCost)
        except:
            return 0
    def getRampCapStatus(self) -> str:
        return self.RampCapStatus
    def getRampRate(self) -> float:
        try:
            return float(self.RampRate)
        except:
            return 0
    def getRegMax(self) -> float:
        try:
            return float(self.RegMax)
        except:
            return 0
    def getRegMin(self) -> float:
        try:
            return float(self.RegMin)
        except:
            return 0
    def getRegMileagePrice(self) -> float:
        try:
            return float(self.RegMileagePrice)
        except:
            return 0
    def getRegPrice(self) -> float:
        try:
            return float(self.RegPrice)
        except:
            return 0
    def getRegSelfMW(self) -> float:
        try:
            return float(self.RegSelfMW)
        except:
            return 0
    def getRegStatus(self) -> str:
        return self.RegStatus
    def getSpinPrice(self) -> float:
        try:
            return float(self.SpinPrice)
        except:
            return 0
    def getSpinSelfMW(self) -> float:
        try:
            return float(self.SpinSelfMW)
        except:
            return 0
    def getSpinStatus(self) -> str:
        return self.SpinStatus
    def getSuppOnPrice(self) -> float:
        try:
            return float(self.SuppOnPrice)
        except:
            return 0
    def getSuppOnSelfMW(self) -> float:
        try:
            return float(self.SuppOnSelfMW)
        except:
            return 0
    def getSuppOnStatus(self) -> str:
        return self.SuppOnStatus
    def getSuppOffMaxMW(self) -> float:
        try:
            return float(self.SuppOffMaxMW)
        except:
            return 0
    def getSuppOffPrice(self) -> float:
        try:
            return float(self.SuppOffPrice)
        except:
            return 0
    def getSuppOffStatus(self) -> str:
        return self.SuppOffStatus
    def getUnitID(self) -> int:
        try:
            return int(self.UnitScheduleID[:-2])
        except:
            return 0
    def getUnitScheduleID(self) -> int:
        try:
            return int(self.UnitScheduleID)
        except:
            return 0
    def getUseBidSlope(self) -> bool:
        return (self.UseBidSlope == "1")

    def getUnitHourlyOffer(self):
        return UnitHourlyOffer(self.getUnitID(), self.getUnitScheduleID(), self.getMktHour(), self.getBidOfferCurve(), self.getUseBidSlope(), self.getNoLoadCost(),
                  self.getColdNotificationTime(), self.getInterNotificationTime(), self.getHotNotificationTime(), 
                  self.getColdStartupTime(), self.getInterStartupTime(), self.getHotStartupTime(),
                  self.getEcoMax(), self.getEcoMin(), self.getEmerMax(), self.getEmerMin(), self.getRegMax(), self.getRegMin(), self.getRampRate(),
                  self.getCommitStatus(), self.getEnergyStatus(), self.getRampCapStatus(), self.getRegStatus(), self.getSpinStatus(), self.getSuppOnStatus(),self.getSuppOffStatus(),
                  self.getRegMileagePrice(), self.getRegPrice(), self.getSpinPrice(), self.getSuppOnPrice(), self.getSuppOffPrice(),  
                  self.getEnergySelfMW(), self.getRegSelfMW(), self.getSpinSelfMW(), self.getSuppOnSelfMW(), self.getSuppOffMaxMW())