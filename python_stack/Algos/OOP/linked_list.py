class Node:
    def __init__(self,value):
       self.value=value
       self.next=None
class SLL:
    def __init__(self):
      self.head=None
    # add node at back
    def addNode(self,node):
        if self.head:
            runner=self.head
            while runner.next:
                runner=runner.next 
            runner.next=node
        else:
            self.head=node
        return self
    def display(self):
        if self.head:
            runner=self.head
            while(runner):
                print(runner.value)
                runner=runner.next
    def addNodeFront(self):
        
node1=Node(100)
node2=Node(200)
sll=SLL()
sll.addNode(node1).addNode(node2).display()
            