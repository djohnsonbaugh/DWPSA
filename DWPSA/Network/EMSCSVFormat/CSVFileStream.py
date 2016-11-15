from io import FileIO

class CSVFileStream(FileIO):
    """Streams Properties from a CSV File"""

    def __init__(self, filepath,  propertytofilemap, encoding="utf-8"):
        super(CSVFileStream, self).__init__(filepath, mode='r')
        self.Encoding = encoding
        self.PropertyToColumnNameMap = propertytofilemap
        self.Keys = {}
        self.Values = {}
        
        self.P1 = None
        self.P2 = None
        self.P3 = None
        self.P4 = None
        self.P5 = None

        #find key properties in file headers
        strs = self.ReadCSVLine()
        while len(strs) != 0:
            for col in range(len(strs)):
                for n in self.PropertyToColumnNameMap.keys():
                    if n == strs[col]:
                        self.Keys[self.PropertyToColumnNameMap[n]] = col
                        break
            if len(self.Keys) == len(self.PropertyToColumnNameMap):
                break
            strs = self.ReadCSVLine()
            self.Keys = {}

        return

    def __iter__(self):
        return self

    def __next__(self):
        strs = self.ReadCSVLine()
        if len(strs) == 0:
            raise StopIteration()
        for key in self.Keys.keys():
            setattr(self, key, strs[self.Keys[key]])
            self.Values[key] = strs[self.Keys[key]]
        return self.Values

    def ReadCSVLine(self):
        strs = {}
        buff = self.readline().decode(self.Encoding)
        if buff == "":
            return strs
        strs = buff.split(",")
        for i in range(len(strs)):
            strs[i] = strs[i].strip()
        return strs