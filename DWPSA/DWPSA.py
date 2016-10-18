from TestNetwork import *
import unittest

suite = unittest.TestLoader().loadTestsFromTestCase(TestCompany.TestCompany)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(TestDivision.TestDivision)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(TestStation.TestStation)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(TestNode.TestNode)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(TestNetwork.TestNetwork)
unittest.TextTestRunner(verbosity=2).run(suite)

