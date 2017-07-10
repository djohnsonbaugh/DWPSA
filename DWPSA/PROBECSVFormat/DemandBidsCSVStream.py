from CSVFileStream.CSVFileStream import CSVFileStream
from Network.MktBid import *
from Network.BidOfferCurve import BidOfferCurve

class DemandBidsCSVStream(CSVFileStream):
    """Streams PROBE Hourly Bid Data Properties With Data Conversions"""
    DefaultPropertyToFileMap = {
                                "BIDID" : "BidID",
                                "PNODEID" : "PNodeID",
                                "LOCALMKTHOUR" : "MktHour",
                                "PARTICIPANTNAME": "Participant",
                                "BIDTYPE" : "BidType",
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
                                "MW12" : "MW12",
                                "PRICE12" : "Price12",                              
                                "MW13" : "MW13",
                                "PRICE13" : "Price13",                              
                                "MW14" : "MW14",
                                "PRICE14" : "Price14",                              
                                "MW15" : "MW15",
                                "PRICE15" : "Price15",                              
                                "MW16" : "MW16",
                                "PRICE16" : "Price16",                              
                                "MW17" : "MW17",
                                "PRICE17" : "Price17",                              
                                "MW18" : "MW18",
                                "PRICE18" : "Price18",                              
                                "MW19" : "MW19",
                                "PRICE19" : "Price19",                              
                                "MW20" : "MW20",
                                "PRICE20" : "Price20"
                                }

    DefaultFileName = "demand_bids_{:%Y%m%d}.csv"

    def __init__(self, filepath=DefaultFileName,  propertytofilemap=DefaultPropertyToFileMap , encoding="utf-8"):
        super(DemandBidsCSVStream, self).__init__(filepath, propertytofilemap, encoding)      
        self.BidID = ""
        self.BidType = ""
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
        self.MW12 = ""
        self.MW13 = ""
        self.MW14 = ""
        self.MW15 = ""
        self.MW16 = ""
        self.MW17 = ""
        self.MW18 = ""
        self.MW19 = ""
        self.MW20 = ""
        self.Participant = ""
        self.PNodeID = ""
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
        self.Price12 = ""                              
        self.Price13 = ""                              
        self.Price14 = ""                              
        self.Price15 = ""                              
        self.Price16 = ""                              
        self.Price17 = ""                              
        self.Price18 = ""                              
        self.Price19 = ""                              
        self.Price20 = ""                              

        return

    def getBidID(self) -> int:
        try:
            return int(self.BidID)
        except:
            return 0

    def getBidType(self) -> MktBidType:
        try:
            return MktBidType[self.BidType.replace(" ","")]
        except:
            return MktBidType.Unknown

    def getBidCurve(self) -> BidOfferCurve:
        boc = BidOfferCurve(bidpointsareindependant=True)
        for i in range(1 , 20):  
            price = self.__getattribute__("Price{0}".format(i))
            mw = self.__getattribute__("MW{0}".format(i))
            if price == "" or mw == "": break
            try:
                boc.AddPoint(float(price),float(mw))
            except:
                raise Exception("Invalid Bid or Offer Data provided for Point", i)
        return boc

    def getFixedMW(self) -> float:
        try:
            return float(self.MW1)
        except:
            return 0

    def getMktHour(self) -> datetime:
        try: #12/22/2016 0:00
            return datetime.strptime(self.MktHour, "%m/%d/%Y %H:%M")
        except:
            return datetime.today()


    def getParticipant(self) -> str:
        return self.Participant

    def getPNodeID(self) -> int:
        try:
            return int(self.PNodeID)
        except:
            return 0

    def getMktBid(self):
        if self.getBidType() == MktBidType.FixedDemand:
            return MktBid(self.getBidID(), self.getPNodeID(), self.getBidType(), self.getMktHour(), self.getParticipant(), fixedload=self.getFixedMW())
        else:
            return MktBid(self.getBidID(), self.getPNodeID(), self.getBidType(), self.getMktHour(), self.getParticipant(),bidcurve=self.getBidCurve())
