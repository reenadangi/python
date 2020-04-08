#   Middle of the Linked List
class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        
class SLL():
    def __init__(self):
        self.head=None
    def addNode(self,node):
        if self.head:
            current=self.head
            while(current.next):
                current=current.next
            current.next=node    
            return self
        self.head=node
    def display(self):
        if self.head:
            current=self.head
            while(current):
                print(current.value)
                current=current.next
        return self   

    def middleNode(self):
        if self.head:
            slow=self.head
            fast=self.head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            print(slow.value)

sll=SLL()
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
node6=Node(6)
sll.addNode(node1)
sll.addNode(node2).addNode(node3).addNode(node4).addNode(node5).addNode(node6)
sll.display()
sll.middleNode()



