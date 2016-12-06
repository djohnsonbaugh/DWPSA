import unittest
import io
import os
from EMSCSVFormat.CircuitBreakerCSVStream import CircuitBreakerCSVStream
from Network.CircuitBreaker import CircuitBreaker
from Network.CircuitBreaker import CBState
class TestCircuitBreakerCSVStream(unittest.TestCase):
    def test_DataConversion(self):
        testfilename = "testCBfilestream.csv"
        cbname = "CB1"
        cbtype = "CB"
        fnd = "N1"
        ns = "Open"
        owner = "ABC"
        st = "ST"
        tnd = "N2"
        kv = "115"
        with open(testfilename, 'w') as file:
            file.write("ID_CO,ID_DV,ID_ST,CBTYP Name,CB Name,From Node,To Node,Normal State,KV_ID,Changed")

        with CircuitBreakerCSVStream(testfilename) as c:
            c.CBName = cbname
            c.CBType = cbtype
            c.FromNodeName = fnd
            c.NormalState = ns
            c.Owner = owner
            c.StationName = st
            c.ToNodeName = tnd
            c.Voltage = kv

            self.assertEqual(c.getCBName(), cbname)
            self.assertEqual(c.getCBType(), cbtype)
            self.assertEqual(c.getFromNodeName(), fnd)
            self.assertEqual(c.getNormalState(), CBState.Open)
            self.assertEqual(c.getOwner(), owner)
            self.assertEqual(c.getStationName(), st)
            self.assertEqual(c.getToNodeName(), tnd)
            self.assertEqual(c.getVoltage(), kv)

            cb = c.getCircuitBreaker()
            self.assertEqual(cb.ID, (st, cbname, cbtype))

        os.remove(testfilename)
        return