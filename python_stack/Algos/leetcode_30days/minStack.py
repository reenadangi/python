
class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minval=float('inf')
    

    def push(self, x):
        if (x<=self.minval):
            self.stack.append(self.minval)
            self.minval=x
        self.stack.append(x)



    def pop(self):
        if(self.stack and self.stack.pop()==self.minval): 
            self.minval=self.stack.pop()    

    def top(self):
        return self.stack[-1]


    def getMin(self):
        return self.minval
      
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]      
obj = MinStack()

obj.push(-3)
obj.push(-2)
print(obj.top())
print(obj.getMin())
# print(obj.pop())
# param_3 = obj.top()
# param_4 = obj.getMin()