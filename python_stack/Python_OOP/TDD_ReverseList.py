# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on
def reverseList(lst):
    lst.reverse()
    return lst
# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class reverseListTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def testThree(self):
        self.assertEqual(reverseList([6,3,5]), [5,3,6])
    # any task you want run before any method above is executed,
    # put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
    # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests
