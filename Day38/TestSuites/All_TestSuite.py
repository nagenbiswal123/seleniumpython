import unittest

from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentReturns import PaymentReturnsTest
from Package2.TC_PaymentTest import PaymentTest

# Get all tests from LoginTest,SignupTest, PaymentTest and PaymentReturnsTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)


# Creating Test Suite
#sanityTestSuite = unittest.TestSuite([tc1,tc2]) #Sanity Test suite
#unittest.TextTestRunner().run(sanityTestSuite)

functionalTestSuite=unittest.TestSuite([tc3, tc4]) #functional test suite
unittest.TextTestRunner(verbosity=2).run(functionalTestSuite)



