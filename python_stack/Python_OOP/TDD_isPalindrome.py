# Write a function that checks whether the given word is a palindrome
# (a word that spells the same backward).
# Example: isPalindrome("racecar") should return True
# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on
def isPalindrome(word):
    index = len(word)-1//2
    end=len(word)-1
    print(end)
    for start in range(index):
        print(word[start],word[end])
        if (word[start]!=word[end]):
            return False
        else:
            end=end-1
    return True
    

# print (isPalindrome("racecar"))

# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class isPalindromeTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(isPalindrome("racecar"), True)
    def testThree(self):
        self.assertEqual(isPalindrome("rabcr"), False)
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
