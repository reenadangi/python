class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert(self,value):
        if self.head:
            runner=self.head
            while runner.next:
                runner=runner.next
            runner.next=Node(value)
        else:
            self.head=Node(value)
        return self
    def display(self):
        if self.head:
            runner=self.head
            while runner:
                print(runner.value)
                runner=runner.next
    def insert_front(self,value):
        if self.head:
            tmp=self.head
            self.head=Node(value)
            self.head.next=tmp
        else:
            self.head=Node(value)
        return self
    def pop(self):
        if self.head:
            runner=self.head
            while runner.next.next:
                runner=runner.next
            runner.next=None
        return self

    def reverse(self):
        prev=None
        runner=self.head
        while runner:
            temp=runner
            runner=runner.next
            temp.next=prev
            prev=temp
        self.head=prev
        return self
    def deleteNode(self,value):
        
        prev=Node(0)
        prev.next=self.head
        runner=prev

        while runner and runner.next:
            if runner.next.value==value:
                runner.next=runner.next.next
            else:
                runner=runner.next
        self.head=prev.next
        return self
# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
    def hasCycle(self):
        head=self.head
        if head is None or head.next is None:
            return False
        fast=head.next
        slow=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False

# Add Two Numbers	34.0%	Medium	
# 19	
# Remove Nth Node From End of List	35.2%	Medium	
# 21	
# Merge Two Sorted Lists


sll1= SLL()

sll1.insert(1).insert(1).insert(2).insert(2).deleteNode(1)
sll1.display()
print(sll1.hasCycle())



      