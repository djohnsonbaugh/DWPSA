import unittest
from Network.RatingSet import RatingSet

class TestRatingSet(unittest.TestCase):
    def testConstructor(self):
        n = 44
        e = 45
        c = 23
        rs = RatingSet(n,e,c)

        self.assertEqual(rs.Normal,n)
        self.assertEqual(rs.Emergency,e)
        self.assertEqual(rs.Alternate,c)


if __name__ == '__main__':
    unittest.main()
