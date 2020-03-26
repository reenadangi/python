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
    def addNodeFront(self,node):
        if self.head:
            temp=self.head
            self.head=node
            self.head.next=temp
        else:
            self.head=node
        return self
        # remove from front
    def remove(self):
        if self.head.next:
            self.head=self.head.next
        else:
            self.head=None
        return self
    def removeLastNode(self):
        if self.head:
            runner=self.head
            while(runner.next):
                runner=runner.next
            runner.next=None
        return self
        
    # method overriding 
    def remove(self,value):
        if self.head:
            runner=self.head
            if runner.value==value:
                # First Node Found - delete
                self.head=self.head.next
                return self
            else:
                while(runner.next):
                    if runner.next.value==value:
                        runner.next=runner.next.next
                        return self
                    else:
                        runner=runner.next
            return self
node1=Node(100)
node2=Node(200)
sll=SLL()
sll.addNode(node1).addNode(node2).addNodeFront(Node(80)).addNode(Node(67)).remove(200).remove(80).display()
            