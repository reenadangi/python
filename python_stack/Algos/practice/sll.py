class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def insert(self,value):
        if self.head:
            runner=self.head
            while runner.next:
                runner=runner.next
            runner.next=Node(value)
            return self
        else:
            self.head=Node(value)
    def display(self):
        if self.head:
            runner=self.head
            while runner:
                print(runner.value)
                runner=runner.next
            
    def reverse(self):
        if self.head:
            runner=self.head
            prev=None
            while runner:
                next=runner.next
                runner.next=prev
                prev=runner
                runner=next
            self.head=prev

sll1=Sll()
sll1.insert(20)
sll1.insert(45) 
sll1.insert(50)      
sll1.display()
sll1.reverse()
print("***")
sll1.display()
