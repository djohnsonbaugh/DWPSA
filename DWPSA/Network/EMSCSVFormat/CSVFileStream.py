from io import FileIO

class CSVFileStream(FileIO):
    """Streams Properties from a CSV File"""

    DefaultPropertytoFileMap = {}

    def __init__(self, filepath,  propertytofilemap = DefaultPropertytoFileMap, encoding="utf-8"):
        super(CSVFileStream, self).__init__(filepath, mode='r')
        self.Encoding = encoding
        self.PropertyToColumnNameMap = propertytofilemap
        self.Keys = {}
        self.Values = {}
        
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
        if len(self.Keys) != len(self.PropertyToColumnNameMap):
            raise Exception("Expected column headers were not found")
        return

    def __iter__(self):
        return self

    def __next__(self):
        strs = self.ReadCSVLine()
        if len(strs) == 0:
            raise StopIteration()
        for key in self.Keys.keys():
            i = self.Keys[key]
            val = ""
            if i < len(strs):
                val = strs[i]
            setattr(self, key, val)
            self.Values[key] = val
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