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
        return self
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
        # Reverse a linked list
    def reverse(self):
        if self.head:
            print("IN REVERSE")
            prev=None
            runner=self.head
            while(runner):
                temp=runner
                runner=runner.next
                temp.next=prev
                prev=temp 
            self.head=prev
        return self
        # Do it with merge sort
    def sort(self):
        if self.head:
            print("Sort")
            runner=self.head
            while runner.next:
                runner2=runner.next
                while runner2:
                    if runner.value>runner2.value:
                        runner.value,runner2.value=runner2.value,runner.value
                    runner2=runner2.next
            runner=runner.next
        return self

# Middle of the Linked List
# If there are two middle nodes, return the second middle node.
    def middle(self):
        if self.head:
            slow=self.head
            fast=self.head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            print (f"Middle:{slow.value}")


node1=Node(100)
node2=Node(200)
sll=SLL()
sll.addNode(node1).addNode(node2).addNodeFront(Node(80)).addNode(Node(67)).remove(200).remove(80).addNode(Node(4)).addNode(Node(14)).display().reverse().display()

sll.middle()            