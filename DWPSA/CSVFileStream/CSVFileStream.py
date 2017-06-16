import io

class CSVFileStream(object):
    """Streams Properties from a CSV File"""

    DefaultPropertyToFileMap = {}
    InvalidPropertyData = {}

    def __init__(self, filepath,  propertytofilemap = DefaultPropertyToFileMap, encoding="utf-8", invalidpropertydata = InvalidPropertyData):
        self.Encoding = encoding
        self.PropertyToColumnNameMap = propertytofilemap
        self.InvalidPropertyData = invalidpropertydata
        self.Keys = {}
        self.Values = {}
        self.AllLines = []
        self.Index = 0
        self.FilePath = filepath
        with open(self.FilePath, mode='r') as f:
            self.AllLines = f.readlines()
        self.Index = 0
        #find key properties in file headers
        while len(self.AllLines) > self.Index:
            strs = self.ReadCSVLine()
            for col in range(len(strs)):
                for n in self.PropertyToColumnNameMap.keys():
                    if n.replace(" ","").upper() == strs[col].replace(" ","").upper():
                        self.Keys[self.PropertyToColumnNameMap[n]] = col
                        break
            if len(self.Keys) == len(self.PropertyToColumnNameMap):
                break
            self.Keys = {}
        if len(self.Keys) != len(self.PropertyToColumnNameMap):
            raise Exception("Expected column headers were not found")
        return

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.AllLines)

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    def __next__(self):
        while True:
            if len(self.AllLines) <= self.Index:
                raise StopIteration()
            strs = self.ReadCSVLine()
            if len(strs) > 1:
                break
            if strs[0] != "":
                break
        for key in self.Keys.keys():
            i = self.Keys[key]
            val = ""
            if i < len(strs):
                val = strs[i]
            setattr(self, key, val)
            self.Values[key] = val
            if key in self.InvalidPropertyData.keys():
                if self.InvalidPropertyData[key] == val:
                    return self.__next__()
        return self.Values

    def ReadCSVLine(self):
        strs = self.AllLines[self.Index].split(",")
        for i in range(len(strs)):
            strs[i] = strs[i].strip()
        self.Index += 1
        return strs