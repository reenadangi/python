# Create a Python class called MathDojo that has one attribute, result, and 2 methods: 
# add and subtract.
# The 2 methods each must take at least 1 parameter, but could take many more.
class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
        for n in nums:
            num+=n
        self.result=num
        return self.result
    def subtract(self, num, *nums):
    	for n in nums:
            num-=n
        # self.result=num
        # return self.result
# create an instance:
md = MathDojo()
# to test:
print(md.add(2,4,5))

# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x)	# should print 5
# run each of the methods a few more times and check the result!
